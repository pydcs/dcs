import os
import unittest
import dcs
from dcs.drawing.drawing import LineStyle, Rgba
from dcs.drawing.drawings import StandardLayer
from dcs.drawing.icon import StandardIcon
from dcs.drawing.polygon import Circle
from dcs.mapping import Point
from dcs.mission import Mission


class DrawingTests(unittest.TestCase):
    def setUp(self):
        os.makedirs('missions', exist_ok=True)

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
        red_layer = m.drawings.get_layer(StandardLayer.Red)
        self.assertEqual(True, red_layer.visible)
        self.assertEqual("Red", red_layer.name)
        self.assertEqual("Icon 2", red_layer.objects[0].name)

        line = m.drawings.get_layer(StandardLayer.Blue).objects[0]
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
        
        circle = Circle(
            True,
            Point(10, 10, m.terrain),
            "TEST CIRCLE",
            Rgba(20, 30, 40, 200),
            ":S",
            Rgba(50, 60, 70, 150),
            10,
            LineStyle.Solid,
            100
        )
        m.drawings.layers[0].add_drawing(circle)
        self.assertEqual("TEST CIRCLE", m.drawings.layers[0].objects[1].name)

        mission_path = 'missions/Draw_tool_test_added_drawings.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))
        self.assert_expected_stuff(m2)
        self.assertEqual("TEST CIRCLE", m2.drawings.layers[0].objects[1].name)
        

    def test_add_drawings_to_new_mission(self) -> None:
        m: Mission = dcs.mission.Mission()
        
        circle = Circle(
            True,
            Point(10, 10, m.terrain),
            "TEST CIRCLE",
            Rgba(20, 30, 40, 200),
            ":S",
            Rgba(50, 60, 70, 150),
            10,
            LineStyle.Solid,
            100
        )
        red_layer = m.drawings.get_layer(StandardLayer.Red)
        red_layer.add_drawing(circle)
        red_layer.add_line_segments(
            Point(1, 1, m.terrain),
            [Point(6, 6, m.terrain), Point(7, 7, m.terrain)],
            closed=True,
        )

        m.drawings.options.hiddenOnF10Map["Pilot"]["Red"] = True
        m.drawings.options.hiddenOnF10Map["Instructor"]["Blue"] = True
        m.drawings.options.hiddenOnF10Map["Observer"]["Neutral"] = True

        mission_path = 'missions/New_mission_w_added_drawings.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))
        red_layer2 = m2.drawings.get_layer(StandardLayer.Red)
        self.assertEqual("TEST CIRCLE", red_layer2.objects[0].name)
        self.assertEqual("A line", red_layer2.objects[1].name)
        self.assertEqual(True, red_layer2.objects[1].closed)
        self.assertEqual("Red", red_layer2.objects[0].layer_name)
        self.assertEqual("Red", red_layer2.objects[1].layer_name)


    def test_set_options_hidden_f10(self) -> None:
        m: Mission = dcs.mission.Mission()
        
        m.drawings.options.hiddenOnF10Map["Pilot"]["Red"] = True
        m.drawings.options.hiddenOnF10Map["Instructor"]["Blue"] = True
        m.drawings.options.hiddenOnF10Map["Observer"]["Neutral"] = True
        mission_path = 'missions/New_mission_w_added_drawings.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))
        self.assertEqual(False, m2.drawings.options.hiddenOnF10Map["Pilot"]["Blue"])
        self.assertEqual(True, m2.drawings.options.hiddenOnF10Map["Pilot"]["Red"])
        self.assertEqual(True, m2.drawings.options.hiddenOnF10Map["Instructor"]["Blue"])
        self.assertEqual(True, m2.drawings.options.hiddenOnF10Map["Observer"]["Neutral"])

    def test_add_std_icon(self) -> None:
        m: Mission = dcs.mission.Mission()

        red_layer = m.drawings.get_layer(StandardLayer.Red)
        red_layer.add_icon(
            Point(1000, 1000, m.terrain),
            StandardIcon.MechanizedArtillery,
        )
        mission_path = 'missions/New_mission_w_added_std_icon.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))
        red_layer = m.drawings.get_layer(StandardLayer.Red)
        
        self.assertEqual(StandardIcon.MechanizedArtillery.value, red_layer.objects[0].file)

    def test_add_oblong(self) -> None:
        m: Mission = dcs.mission.Mission()

        layer = m.drawings.get_layer(StandardLayer.Common)
        self.assertEqual(0, len(layer.objects))
        oblong = layer.add_oblong(
            Point(1000, 1000, m.terrain),
            Point(4000, 1000, m.terrain),
            1000,
            resolution=20,
        )
        self.assertEqual(1, len(layer.objects))
        # Resolution 20 should give 43 points
        # (21 in each end and one extra to close polygon)
        self.assertEqual(43, len(oblong.points))
