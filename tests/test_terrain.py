import unittest
import dcs


class CaucasusTest(unittest.TestCase):
    def test_parking_slots(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())
        large_slots = m.terrain.airports["Batumi"].free_parking_slots(dcs.planes.KC_135)
        self.assertEqual(len(large_slots), 2)

        slots = m.terrain.airports["Batumi"].free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), len(m.terrain.airports["Batumi"].parking_slots))

        slot = m.terrain.airports["Batumi"].free_parking_slot(dcs.planes.A_10C)
        slot.unit_id = 1

        slots = m.terrain.airports["Batumi"].free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 9)

        slot.unit_id = None
        slots = m.terrain.airports["Batumi"].free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 10)

    def test_parking_large_used(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        for x in range(0, 2):
            large_slot = m.terrain.airports["Batumi"].free_parking_slot(dcs.planes.KC_135)
            self.assertIsNotNone(large_slot)
            large_slot.unit_id = x

        self.assertIsNone(m.terrain.airports["Batumi"].free_parking_slot(dcs.planes.KC_135))

    def test_heli_parking_slots(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        self.assertEqual(len(m.terrain.airports["Tbilisi-Lochini"].parking_slots), 74)

        hslots = m.terrain.airports["Tbilisi-Lochini"].free_parking_slots(dcs.helicopters.UH_1H)
        self.assertEqual(len(hslots), 44)

        slots = m.terrain.airports["Tbilisi-Lochini"].free_parking_slots(dcs.planes.A_10A)
        self.assertEqual(len(slots), 70)

        slot = m.terrain.airports["Tbilisi-Lochini"].free_parking_slot(dcs.planes.A_10C)
        slot.unit_id = 1

        hslots = m.terrain.airports["Tbilisi-Lochini"].free_parking_slots(dcs.helicopters.UH_1H)
        self.assertEqual(len(hslots), 44)

    def test_parking_mixed_used(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        used = []
        for x in range(0, 1):
            large_slot = m.terrain.airports["Batumi"].free_parking_slot(dcs.planes.KC_135)
            self.assertIsNotNone(large_slot)
            large_slot.unit_id = x
            used.append(large_slot)

        self.assertIsNotNone(m.terrain.airports["Batumi"].free_parking_slot(dcs.planes.KC_135))

        for x in range(3, 10):
            slot = m.terrain.airports["Batumi"].free_parking_slot(dcs.planes.A_10A)
            self.assertIsNotNone(slot)
            slot.unit_id = x
            used.append(slot)

        slot = m.terrain.airports["Batumi"].free_parking_slot(dcs.planes.A_10A)

        self.assertEqual(len(used)+2, len(m.terrain.airports["Batumi"].parking_slots))


class NevadaTest(unittest.TestCase):

    def test_parking_slots(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Nevada())
        slots = m.terrain.airports["Nellis"].free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 104)

        slot = m.terrain.airports["Nellis"].free_parking_slot(dcs.planes.A_10C)
        slot.unit_id = 1

        slots = m.terrain.airports["Nellis"].free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 103)

        slot.unit_id = None
        slots = m.terrain.airports["Nellis"].free_parking_slots(dcs.planes.A_10C)
        self.assertEqual(len(slots), 104)

        hslots = m.terrain.airports["Nellis"].free_parking_slots(dcs.helicopters.UH_1H)
        self.assertEqual(len(hslots), 51)

        slots = m.terrain.airports["Nellis"].free_parking_slots(dcs.planes.KC_135)


class WarehousesTest(unittest.TestCase):

    def test_load_dict_reads_warehouses(self):
        # __str__ serializes both "airports" and "warehouses", but load_dict
        # historically read only "airports", silently dropping unit/FARP/ship
        # warehouse state on every save->load round-trip.  load_dict must read
        # "warehouses" symmetrically with the serializer.
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())
        m.warehouses.load_dict({
            "airports": {},
            "warehouses": {"4242": {"coalition": "BLUE", "size": 100}},
        })

        self.assertIn(4242, m.warehouses.warehouses)
        self.assertEqual(m.warehouses.warehouses[4242]["coalition"], "BLUE")
        self.assertEqual(m.warehouses.warehouses[4242]["size"], 100)

    def test_load_dict_skips_airport_absent_from_terrain(self):
        # airport_by_id() returns None when warehouse data references an airport
        # id not present in the current terrain (e.g. a mission authored before
        # a map update that renumbered or removed airports).  load_dict must
        # skip the absent id instead of crashing on None.load_from_dict(), and
        # must still load any valid airport entries in the same dict.
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        present = m.terrain.airport_by_id(12)  # Anapa-Vityazevo
        self.assertIsNotNone(present)
        present_data = present.dict()
        present_data["coalition"] = "BLUE"
        present_data["size"] = 7777

        # The absent id is iterated first, so the loop must continue past it to
        # reach the present id.  This must not raise.
        m.warehouses.load_dict({
            "airports": {
                999999: {},   # not present in Caucasus -> airport_by_id() is None
                12: present_data,
            },
            "warehouses": {},
        })

        self.assertEqual(present.coalition, "BLUE")
        self.assertEqual(present.size, 7777)


class NormandyTest(unittest.TestCase):

    def test_creation(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Normandy())
        self.assertIsInstance(m.terrain, dcs.terrain.Normandy)


class SyriaTest(unittest.TestCase):
    
    def test_airplane_parking_used(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Syria())

        self.assertEqual(len(m.terrain.airports["Aleppo"].parking_slots), 23)

        hslots = m.terrain.airports["Aleppo"].free_parking_slots(dcs.helicopters.UH_1H)
        self.assertEqual(len(hslots), 17)

        slots = m.terrain.airports["Aleppo"].free_parking_slots(dcs.planes.A_10A)
        self.assertEqual(len(slots), 9)

        for x in range(0, 9):
            airplane_slot = m.terrain.airports["Aleppo"].free_parking_slot(dcs.planes.A_10A)
            self.assertIsNotNone(airplane_slot)
            airplane_slot.unit_id = x

        self.assertIsNone(m.terrain.airports["Aleppo"].free_parking_slot(dcs.planes.A_10A))

        hslots = m.terrain.airports["Aleppo"].free_parking_slots(dcs.helicopters.UH_1H)
        self.assertEqual(len(hslots), 8)

