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

    @classmethod
    def setUpClass(cls) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            for path in sorted(glob.glob("tests/**/*.miz", recursive=True)):
                m = dcs.Mission()
                m.load_file(path)
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
