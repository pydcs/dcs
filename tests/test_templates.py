import unittest

import dcs
from dcs.templates import ShipTemplate, VehicleTemplate


class TemplateTests(unittest.TestCase):
    def test_all_templates(self) -> None:
        templates = {
            "sa10_site": lambda m, pos: VehicleTemplate.Russia.sa10_site(m, pos, 90),
            "patriot_site": lambda m, pos: VehicleTemplate.USA.patriot_site(m, pos, 90),
            "hawk_site": lambda m, pos: VehicleTemplate.USA.hawk_site(m, pos, 90),
            "sa11_site": lambda m, pos: VehicleTemplate.sa11_site(m, m.country("Russia"), pos, 90),
            "sa15_site": lambda m, pos: VehicleTemplate.sa15_site(m, m.country("Russia"), pos, 90),
            "sa6_site": lambda m, pos: VehicleTemplate.sa6_site(m, m.country("Russia"), pos, 90),
            "kuznetsov_taskgroup": lambda m, pos: ShipTemplate.kuznetsov_taskgroup(m, pos, 90),
        }
        for name, create in templates.items():
            with self.subTest(name):
                m = dcs.Mission()
                group = create(m, m.terrain.airports["Batumi"].position)
                self.assertIsNotNone(group)
                self.assertGreater(len(group.units), 1)
