import unittest

import dcs
from dcs.unitgroup import VehicleGroup


class VehicleGroupFormationTests(unittest.TestCase):
    def test_all_formations_for_any_group_size(self) -> None:
        for formation in VehicleGroup.Formation:
            for size in range(1, 8):
                with self.subTest(formation=formation.name, size=size):
                    m = dcs.Mission()
                    group = m.vehicle_group(m.country("USA"), "group", dcs.vehicles.Armor.M_1_Abrams,
                                            m.terrain.airports["Batumi"].position, group_size=size)
                    group.formation(formation, heading=90)
                    positions = {(round(u.position.x, 3), round(u.position.y, 3)) for u in group.units}
                    self.assertEqual(len(positions), size)
