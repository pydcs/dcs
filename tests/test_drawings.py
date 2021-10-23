import unittest
import dcs
from dcs.drawing.drawing import LineStyle, Rgba
from dcs.drawing.polygon import Circle
from dcs.mapping import Point
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
        self.assertEqual("Icon 2", m.drawings.layers[0].objects[0].name)

        line = m.drawings.layers[1].objects[0]
        self.assertEqual("Line 2 segments closed", line.name)
        
        self.assertEqual(Rgba(255, 255, 0, 131), line.color)
        self.assertEqual(-260885.56415634, line.position.x)
        self.assertEqual(671996.90379981, line.position.y)
        self.assertEqual(0, line.points[0].x)
        self.assertEqual(0, line.points[0].y)
        self.assertEqual(-6076.521389334, line.points[2].x)
        self.assertEqual(3038.260694667, line.points[2].y)


    def test_add_drawings_to_loaded_mission(self) -> None:
        m: Mission = dcs.mission.Mission()
        self.assertEqual(0, len(m.load_file('tests/missions/Draw_tool_test.miz')))
        
        circle = Circle(True, Point(10, 10), "TEST CIRCLE", Rgba(20, 30, 40, 200), ":S", Rgba(50, 60, 70, 150), 10, LineStyle.Solid, 100)
        m.drawings.layers[0].add_drawing(circle)
        self.assertEqual("TEST CIRCLE", m.drawings.layers[0].objects[1].name)

        mission_path = 'missions/Draw_tool_test_added_drawings.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))
        self.assert_expected_stuff(m2)
        self.assertEqual("TEST CIRCLE", m.drawings.layers[0].objects[1].name)
        

    def test_add_drawings_to_new_mission(self) -> None:
        m: Mission = dcs.mission.Mission()
        
        circle = Circle(True, Point(10, 10), "TEST CIRCLE", Rgba(20, 30, 40, 200), ":S", Rgba(50, 60, 70, 150), 10, LineStyle.Solid, 100)
        m.drawings.layers[0].add_drawing(circle)
        self.assertEqual("TEST CIRCLE", m.drawings.layers[0].objects[0].name)

        mission_path = 'missions/New_mission_w_added_drawings.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))
        self.assertEqual("TEST CIRCLE", m.drawings.layers[0].objects[0].name)
