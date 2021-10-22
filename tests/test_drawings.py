import unittest
import dcs
from dcs.mission import Mission


class DrawingTests(unittest.TestCase):
    def test_load_save_load(self) -> None:
        m: Mission = dcs.mission.Mission()
        self.assertEqual(0, len(m.load_file('tests/missions/Draw_tool_test.miz')))
        self.assert_expected_stuff(m)
        
        mission_path = 'missions/Draw_tool_test_saved.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))
        self.assert_expected_stuff(m2)
    
    def assert_expected_stuff(self, m: Mission) -> None:
        self.assertEqual(5, len(m.drawings.layers))
        self.assertEqual(False, m.drawings.options.hiddenOnF10Map["Observer"]["Neutral"])
        self.assertEqual(True, m.drawings.layers[0].visible)
        self.assertEqual("Red", m.drawings.layers[0].name)
