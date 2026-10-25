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
