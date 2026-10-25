import inspect
import os
import tempfile
import unittest

import dcs
import dcs.task as task


def _load_task(d):
    return task._create_from_dict(dict({"auto": False, "enabled": True, "number": 1}, **d))


class TaskLoadTests(unittest.TestCase):

    def test_all_tasks_load_back(self) -> None:
        # tasks that need constructor arguments
        instances = {
            task.FACAttackGroup: task.FACAttackGroup(7, "target"),
            task.RecoveryTanker: task.RecoveryTanker(5, 400.0, 3000.0, 2),
        }
        for _, cls in inspect.getmembers(task, inspect.isclass):
            if not issubclass(cls, task.Task) or cls.__module__ != "dcs.task" \
                    or cls in (task.Task, task.Option, task.WrappedAction, task.EmptyTaskAction, task.EngageTargets):
                continue
            t = instances.get(cls) or cls()
            with self.subTest(cls.__name__):
                loaded = _load_task(t.dict())
                self.assertIs(type(loaded), cls)
                self.assertEqual(loaded.dict(), t.dict())

    def test_unknown_tasks_are_preserved(self) -> None:
        unknown = [
            {"id": "SomeFutureTask", "params": {"x": 1}},
            {"id": "WrappedAction", "params": {"action": {"id": "Option", "params": {"name": 999, "value": 3}}}},
            {"id": "WrappedAction", "params": {"action": {"id": "FutureCommand", "params": {"v": 2}}}},
            {"id": "EngageTargets", "key": "FutureKey", "params": {"targetTypes": {}}},
        ]
        for d in unknown:
            with self.subTest(d["id"]):
                t = _load_task(d)
                self.assertIsInstance(t, task.EmptyTaskAction)
                self.assertEqual(t.dict()["id"], d["id"])
                self.assertEqual(t.dict()["params"], d["params"])

    def test_mission_with_tasks_reloads(self) -> None:
        m = dcs.Mission()
        group = m.flight_group_inflight(m.country("USA"), "F", dcs.planes.FA_18C_hornet,
                                        m.terrain.airports["Batumi"].position, 5000)
        tasks = [task.OptJettisonEmptyTanks(), task.RecoveryTanker(5, 400.0, 3000.0, 2),
                 task.FACAttackGroup(7, "target"), task.NoTask()]
        group.points[0].tasks.extend(tasks)
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "tasks.miz")
            m.save(path)
            m2 = dcs.Mission()
            self.assertEqual(m2.load_file(path), [])
        loaded = m2.country("USA").plane_group[0].points[0].tasks[-len(tasks):]
        self.assertEqual([type(t) for t in loaded], [type(t) for t in tasks])


class FormationTests(unittest.TestCase):

    @staticmethod
    def _decode(value: int):
        # formation values are encoded as formationIndex << 16 | zInverse << 8 | variantIndex
        return value >> 16, (value >> 8) & 0xFF, value & 0xFF

    def test_values_decode_to_known_formations(self) -> None:
        formations = {int(x) for x in task.OptFormation.FormationIndex}
        for name, value in task.OptFormation.Values.__members__.items():
            if name == "RotaryWedge":
                continue  # DCS uses the plain value 8 for it
            with self.subTest(name):
                formation, z_inverse, variant = self._decode(int(value))
                self.assertIn(formation, formations)
                self.assertIn(z_inverse, (0, 1))
                self.assertIn(variant, (0, 1, 2, 3))

    def test_factories_match_their_value(self) -> None:
        for name, factory in inspect.getmembers(task.OptFormation, predicate=inspect.isfunction):
            if name.startswith("_") or inspect.signature(factory).parameters:
                continue
            params = factory().params["action"]["params"]
            if params["value"] == task.OptFormation.Values.RotaryWedge:
                continue
            with self.subTest(name):
                formation, z_inverse, variant = self._decode(int(params["value"]))
                self.assertEqual(params["formationIndex"], formation)
                self.assertEqual(params.get("variantIndex", 0), variant)
                self.assertEqual(params.get("zInverse", 0), z_inverse)
