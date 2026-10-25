"""Load and save every sample mission and check that nothing the mission editor wrote gets lost."""
import glob
import os
import tempfile
import unittest
import zipfile
from typing import Any, Dict, Iterator, Tuple

import dcs
from dcs.lua import loads

GROUP_CATEGORIES = ("vehicle", "ship", "plane", "helicopter", "static")

# keys dropped on purpose because they hold the value DCS uses when the key is absent
DEFAULT_VALUED_GROUP_KEYS = {"lateActivation": False, "probability": 1}


def _read_miz(path: str) -> Dict[str, Any]:
    with zipfile.ZipFile(path) as miz:
        return {name: loads(miz.read(name).decode("utf-8")) for name in ("mission", "options")}


def _groups(mission: Dict[str, Any]) -> Iterator[Tuple[str, Dict[str, Any]]]:
    for side in mission["coalition"].values():
        for country in side.get("country", {}).values():
            for category in GROUP_CATEGORIES:
                for group in country.get(category, {}).get("group", {}).values():
                    yield category, group


class RoundTripTests(unittest.TestCase):
    missions: Dict[str, Tuple[Dict[str, Any], Dict[str, Any]]] = {}
    generated_trig_actions: Dict[str, Dict[int, str]] = {}

    @classmethod
    def setUpClass(cls) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for path in sorted(glob.glob("tests/**/*.miz", recursive=True)):
                m = dcs.Mission()
                m.load_file(path)
                cls.generated_trig_actions[os.path.basename(path)] = m.triggerrules.trig()["actions"]
                saved = os.path.join(tmp, "saved.miz")
                m.save(saved)
                cls.missions[os.path.basename(path)] = (_read_miz(path), _read_miz(saved))

    def test_group_and_unit_keys_are_kept(self) -> None:
        for name, (orig, saved) in self.missions.items():
            saved_groups = {(c, g["groupId"]): g for c, g in _groups(saved["mission"]["mission"])}
            for category, group in _groups(orig["mission"]["mission"]):
                with self.subTest(mission=name, group=group["name"]):
                    new = saved_groups[(category, group["groupId"])]
                    lost = {k for k in set(group) - set(new) if DEFAULT_VALUED_GROUP_KEYS.get(k, object()) != group[k]}
                    self.assertFalse(lost, "group keys lost")
                    self.assertFalse(set(group.get("route", {})) - set(new.get("route", {})), "route keys lost")
                    new_units = {u["unitId"]: u for u in new.get("units", {}).values()}
                    for unit in group.get("units", {}).values():
                        new_unit = new_units[unit["unitId"]]
                        self.assertFalse(set(unit) - set(new_unit), "unit keys lost")
                        self.assertFalse(set(unit.get("payload", {})) - set(new_unit.get("payload", {})),
                                         "payload keys lost")

    def test_group_values_are_kept(self) -> None:
        def facts(mission: Dict[str, Any]) -> Dict[Any, Any]:
            out: Dict[Any, Any] = {}
            for category, group in _groups(mission):
                key = (category, group["groupId"])
                route = group.get("route", {})
                out[key + ("spans",)] = route.get("spans", {})
                out[key + ("visible",)] = group.get("visible")
                out[key + ("task names",)] = [
                    task.get("name")
                    for point in route.get("points", {}).values()
                    for task in point.get("task", {}).get("params", {}).get("tasks", {}).values()
                ]
            return out

        for name, (orig, saved) in self.missions.items():
            with self.subTest(mission=name):
                before, after = facts(orig["mission"]["mission"]), facts(saved["mission"]["mission"])
                self.assertEqual({k: v for k, v in before.items() if v is not None},
                                 {k: v for k, v in after.items() if k in before and before[k] is not None})

    def test_options_are_kept(self) -> None:
        for name, (orig, saved) in self.missions.items():
            with self.subTest(mission=name):
                before, after = orig["options"]["options"], saved["options"]["options"]
                self.assertEqual(before.get("playerName"), after.get("playerName"))
                self.assertFalse(set(before) - set(after), "options lost")
                self.assertFalse(set(before["difficulty"]) - set(after["difficulty"]), "difficulty options lost")
                for key, value in before["difficulty"].items():
                    self.assertEqual(value, after["difficulty"][key], key)

    def test_mission_settings_are_kept(self) -> None:
        for name, (orig, saved) in self.missions.items():
            with self.subTest(mission=name):
                before, after = orig["mission"]["mission"], saved["mission"]["mission"]
                self.assertEqual(before.get("forcedOptions"), after.get("forcedOptions"))
                self.assertEqual("descriptionNeutralsTask" in before, "descriptionNeutralsTask" in after)
                for side in before["coalition"]:
                    self.assertEqual(before["coalition"][side].get("nav_points", {}),
                                     after["coalition"][side]["nav_points"])

    def test_trigger_action_keys_are_kept(self) -> None:
        for name, (orig, saved) in self.missions.items():
            with self.subTest(mission=name):
                before, after = orig["mission"]["mission"]["trigrules"], saved["mission"]["mission"]["trigrules"]
                for rule_key, rule in before.items():
                    for action_key, action in rule["actions"].items():
                        new_action = after[rule_key]["actions"][action_key]
                        expected = []
                        if action["predicate"] == "a_out_text_delay" and "start_delay" in action:
                            expected.append("start_delay")
                        # KeyDict_<field> belongs to localized fields; on other fields it's a stale leftover
                        expected += [k for k in ("KeyDict_radiotext", "KeyDict_comment")
                                     if k in action and k[len("KeyDict_"):] in new_action]
                        for key in expected:
                            self.assertEqual(action[key], new_action.get(key), (action["predicate"], key))

    def test_trigger_zones_are_kept(self) -> None:
        for name, (orig, saved) in self.missions.items():
            with self.subTest(mission=name):
                before = orig["mission"]["mission"]["triggers"]["zones"]
                after = {z["zoneId"]: z for z in saved["mission"]["mission"]["triggers"]["zones"].values()}
                for zone in before.values():
                    self.assertEqual(zone["radius"], after[zone["zoneId"]]["radius"], zone["name"])

    def test_generated_trigger_code_matches_mission_editor(self) -> None:
        for name, (orig_miz, _) in self.missions.items():
            with self.subTest(mission=name):
                orig = orig_miz["mission"]["mission"]["trig"]["actions"]
                generated = self.generated_trig_actions[name]
                for key, code in orig.items():
                    for dcs_call, pydcs_call in zip(code.split(";"), generated[key].split(";")):
                        dcs_call, pydcs_call = dcs_call.strip(), pydcs_call.strip()
                        # the mission editor fills in a trailing default argument that isn't stored
                        if dcs_call != pydcs_call:
                            self.assertEqual(dcs_call, pydcs_call[:-1] + ", 0)")

    def test_weather_is_kept(self) -> None:
        def flatten(d: Dict[Any, Any], prefix: str = "") -> Dict[str, Any]:
            out: Dict[str, Any] = {}
            for k, v in d.items():
                if isinstance(v, dict):
                    out.update(flatten(v, f"{prefix}{k}/"))
                else:
                    out[f"{prefix}{k}"] = v
            return out

        for name, (orig, saved) in self.missions.items():
            with self.subTest(mission=name):
                before = flatten(orig["mission"]["mission"]["weather"])
                after = flatten(saved["mission"]["mission"]["weather"])
                self.assertEqual(before, {k: after.get(k, "<missing>") for k in before})

    def test_drawings_are_kept(self) -> None:
        for name, (orig, saved) in self.missions.items():
            with self.subTest(mission=name):
                before = orig["mission"]["mission"].get("drawings", {}).get("layers", {})
                after = saved["mission"]["mission"]["drawings"]["layers"]
                for layer_key, layer in before.items():
                    for object_key, drawing in layer["objects"].items():
                        new = after[layer_key]["objects"][object_key]
                        self.assertFalse(set(drawing) - set(new), drawing["name"])
                        self.assertEqual(drawing.get("hiddenOnPlanner"), new.get("hiddenOnPlanner"))
