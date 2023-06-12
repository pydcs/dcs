# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Difarsuwar_Airfield(Airport):
    id = 1
    name = "Difarsuwar Airfield"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=118550000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(40837.050781, 105395.976562, terrain), terrain)

        self.runways.append(Runway(id=2, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.runways.append(Runway(id=1, name='36-18', main=RunwayApproach(name='36', heading=360, beacons=[]), opposite=RunwayApproach(name='18', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(40401.515625, 106091.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(40304.28125, 106119.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(40993.53125, 105645.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(40838.15625, 105808.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(40761.578125, 105888.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(41047.859375, 105560.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(40902.375, 105714.4921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(39961.890625, 105986.7109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(40095.171875, 105995.6796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(40260.671875, 105891.7734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(40169.546875, 105850.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(40183.390625, 106060.7109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(40607.15625, 106049.5078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(40619.203125, 106150.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))


class Abu_Suwayr(Airport):
    id = 2
    name = "Abu Suwayr"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4300000, vhf_low_hz=39500000, vhf_high_hz=118950000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(57580.1875, 82564.84375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield2_2'))
        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[RunwayBeacon(id='airfield2_1', runway_name='27-09', runway_id=1, runway_side='27'), RunwayBeacon(id='airfield2_0', runway_name='27-09', runway_id=1, runway_side='27')]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.runways.append(Runway(id=2, name='29-11', main=RunwayApproach(name='29', heading=290, beacons=[]), opposite=RunwayApproach(name='11', heading=110, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(58384.940515907, 81352.07683942, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(58412.292207447, 81450.817388234, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(58306.178681915, 81555.6526899, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(58335.324394108, 81661.605623096, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(57512.297814005, 83562.808643261, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(57659.504631416, 83710.443862168, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(57359.812703329, 83885.399922107, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(57335.744412425, 83890.762064307, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(57310.904386853, 83895.975803874, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(57468.735746643, 84047.647507129, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(57377.022980286, 84037.609852142, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(57128.64453125, 84022.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(57150.68359375, 84017.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(57170.4375, 84013.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(57106.43359375, 84027.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(57198.503166636, 84154.005926754, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(57157.856508473, 84207.138647968, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(56574.453125, 83622.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(56559.81640625, 83650.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(56544.53125, 83678.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(56529.89453125, 83707.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(56498.44921875, 83765.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(56513.375, 83736.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(56483.3046875, 83794.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(56522.890625, 84147.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(56543.140383561, 84290.729364144, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(56374.623121989, 83196.068730705, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(56207.87890625, 83126.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(56237.304387892, 83049.312793671, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(56472.453125848, 82424.419699925, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(56430.556912933, 82492.418710561, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(56250.55859375, 82379.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(56293.44921875, 82310.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(56367.578125, 82228.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(56287.5546875, 82125.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(56479.511315932, 82012.48904363, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(56497.440222263, 81925.707030703, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(56499.33258209, 81843.239851413, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(56491.422862971, 81757.69202384, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(56581.159123277, 81432.174720889, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(56612.072539989, 81265.329671375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(56468.58984375, 81199.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(56653.861025727, 81136.769489231, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(57261.931451117, 81318.909645771, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(57399.706476484, 81354.097302114, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(57470.55098993, 81371.659065026, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(57588.929704852, 81386.308231507, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(57666.905981538, 81486.568960784, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))


class As_Salihiyah(Airport):
    id = 3
    name = "As Salihiyah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4350000, vhf_low_hz=39600000, vhf_high_hz=119000000, uhf_hz=251200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(81974.308594, 77620.761719, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield3_2'))
        self.runways.append(Runway(id=2, name='02R-20L', main=RunwayApproach(name='02R', heading=20, beacons=[]), opposite=RunwayApproach(name='20L', heading=200, beacons=[])))
        self.runways.append(Runway(id=1, name='02L-20R', main=RunwayApproach(name='02L', heading=20, beacons=[RunwayBeacon(id='airfield3_1', runway_name='02L-20R', runway_id=1, runway_side='02L'), RunwayBeacon(id='airfield3_0', runway_name='02L-20R', runway_id=1, runway_side='02L')]), opposite=RunwayApproach(name='20R', heading=200, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(80605.1953125, 76764.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(80689.546875, 76898.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(80767.9609375, 76815.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(80852.734375, 76945.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(80929.125, 76860.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(82547.53125, 77421.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(82657.71875, 77454.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(83117.3046875, 78384.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(82962.28125, 78334.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(82810.984375, 78286.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(82659.625, 78238.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(82613.9296875, 78119.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(82763.984375, 78171.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(82917, 78221.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(83069.140625, 78271.4921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(81299.546875, 76942.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(81163.421875, 76935.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(81077.984375, 76905.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(81402.28125, 77103.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(81924.6015625, 77312.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(81966.296875, 77325.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(82006.9140625, 77339.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(82127.859375, 77379.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(82169.5625, 77391.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(82210.171875, 77405.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(82418.984375, 78752.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(82528.4140625, 78787.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(82638.328125, 78821.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(82858.046875, 78887.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(82967.171875, 78921.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(83087.2109375, 79013.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(83187.2890625, 78947.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(83258.1796875, 79052.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(83333.9921875, 78989.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(83416.4921875, 79025.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(83568.9453125, 78565.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(83445.3984375, 78542.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(83757.0390625, 77859.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(83378.328125, 78363.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(83365.96875, 78388.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(83356.8046875, 78418.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(83347.703125, 78446.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(82162.21875, 78566.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(82118.7265625, 78554.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(82074.5078125, 78539.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(82031.453125, 78524.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(81945.03125, 78497.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(81903.5234375, 78488.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(81988.4765625, 78511.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(80719.296875, 77505.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(80708.8515625, 77528.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(80699.6875, 77555.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(80690.6796875, 77580.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(81605.2890625, 77795.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(81497.34375, 77759.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(81388.234375, 77723.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(81278.3671875, 77686.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(81154.5, 77647.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(81044.6328125, 77612.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(81074.390625, 78315.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(80964.7734375, 78278.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(80856.1796875, 78241.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(80714.527883809, 78245.742538807, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(82747.953125, 78853.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(83679.4453125, 77811.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(83622.5390625, 77750.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(83529.25, 77720.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(83240.8671875, 77657.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(83137.3046875, 77533.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(83041.015625, 77528.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(82012.6171875, 77200.7890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=26.0, width=22.0, height=11.0, shelter=False))


class Al_Ismailiyah(Airport):
    id = 4
    name = "Al Ismailiyah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4375000, vhf_low_hz=39650000, vhf_high_hz=118100000, uhf_hz=251250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(60078.449219, 95845.40625, terrain), terrain)

        self.runways.append(Runway(id=1, name='31-13', main=RunwayApproach(name='31', heading=310, beacons=[RunwayBeacon(id='airfield4_1', runway_name='31-13', runway_id=1, runway_side='31'), RunwayBeacon(id='airfield4_0', runway_name='31-13', runway_id=1, runway_side='31')]), opposite=RunwayApproach(name='13', heading=130, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(59649.740903798, 96742.552748161, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(59614.311216298, 96788.677748161, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(59577.694028798, 96834.474623161, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(59604.04296875, 96856.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(59640.23828125, 96810.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(59676.8203125, 96764.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(59720.5546875, 96751.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(59321.963259913, 97208.972848263, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(59322.126890857, 97232.549135395, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(59322.162205874, 97255.028937357, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(59321.863675603, 97277.275037647, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(59247.50571518, 97311.927539932, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(59250.48458368, 97333.938430371, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(59253.879580115, 97354.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))


class Melez(Airport):
    id = 5
    name = "Melez"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4400000, vhf_low_hz=39700000, vhf_high_hz=119050000, uhf_hz=251300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(38907.09375, 183604.53125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield5_0'))
        self.runways.append(Runway(id=1, name='33R-15L', main=RunwayApproach(name='33R', heading=330, beacons=[]), opposite=RunwayApproach(name='15L', heading=150, beacons=[])))
        self.runways.append(Runway(id=2, name='33L-15R', main=RunwayApproach(name='33L', heading=330, beacons=[]), opposite=RunwayApproach(name='15R', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(38624.652448428, 183424.84485741, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(38610.038765436, 183592.6807747, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(38645.855573428, 183411.15735741, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(38916.525514402, 183253.69818072, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(39997.429615885, 184729.73146599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(38846.78382116, 183299.09177212, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(37372.984375, 184236.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(38708.574323428, 183369.21985741, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(38458.8203125, 183538.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(40057.867115885, 184702.98146599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(40177.796384003, 184644.03581777, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(39750.234303385, 184837.16896599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(38687.490715913, 183383.49113242, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(39933.617115885, 184755.04396599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(38666.894635928, 183397.03235741, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(38728.988385928, 183355.71985741, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(38563.234375, 183469.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(38542.3125, 183482.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(38988.569620369, 183204.97982613, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(37438.4609375, 184189.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(40117.843678385, 184673.48146599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(38560.148140436, 183627.3057747, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(37234.765625, 184318.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(39809.976490885, 184806.41896599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(38521.265625, 183497.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(38501.0703125, 183510.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(39059.197586935, 183158.09770576, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(39870.367115885, 184778.54396599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(37306.71875, 184279.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(38479.015625, 183524.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))


class Fayed(Airport):
    id = 6
    name = "Fayed"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4425000, vhf_low_hz=39750000, vhf_high_hz=119100000, uhf_hz=251350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(30164.332031, 98806.203125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield6_2'))
        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[RunwayBeacon(id='airfield6_1', runway_name='27-09', runway_id=1, runway_side='27'), RunwayBeacon(id='airfield6_0', runway_name='27-09', runway_id=1, runway_side='27')]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(30781.74609375, 99087.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(30575.366792433, 100048.53520576, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(30551.309621396, 99766.965826681, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30629.5859375, 99058.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(30564.072636446, 100147.63409774, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30548.164531567, 99638.798803903, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(30547.856358923, 99915.802215022, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(30985.19140625, 99457.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(30898.43761609, 98838.554742276, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30952.461265745, 98976.405295716, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(29974.119165255, 97849.137841858, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(30640.23046875, 97778.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(29957.640625, 97748.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(30615.02734375, 97597.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(31045.827681101, 98810.899525037, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(29990.372369741, 97656.737094373, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(30670.80078125, 97683.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(30611.734375, 97872.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(30613.12109375, 97974.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(31282.82421875, 99154.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(29924.546231998, 100065.67260017, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(29875.564493677, 100300.85508973, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(29878.156975166, 100155.38529581, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(29875.382716848, 99960.063382545, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(29894.44496635, 100445.19033493, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(29963.08203125, 99119.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(30794.85546875, 99455.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(30841.73046875, 99457.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(30938.52734375, 99457.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(29756.047968217, 99580.301371128, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(29866.88671875, 99100.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(29885.138586442, 99568.513702532, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(29987.313571316, 99568.578915898, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(29764.966865345, 99156.793153517, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(30889.55078125, 99457.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(29976.69921875, 97573.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(29958.87109375, 97425.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(31092.9296875, 99092.7734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))


class Hatzerim(Airport):
    id = 7
    name = "Hatzerim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4450000, vhf_low_hz=39800000, vhf_high_hz=119150000, uhf_hz=251400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(131918.421875, 327167.53125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_0'))
        self.runways.append(Runway(id=1, name='28L-10R', main=RunwayApproach(name='28L', heading=280, beacons=[RunwayBeacon(id='airfield7_1', runway_name='28L-10R', runway_id=1, runway_side='28L'), RunwayBeacon(id='airfield7_2', runway_name='28L-10R', runway_id=1, runway_side='28L')]), opposite=RunwayApproach(name='10R', heading=100, beacons=[])))
        self.runways.append(Runway(id=2, name='28R-10L', main=RunwayApproach(name='28R', heading=280, beacons=[]), opposite=RunwayApproach(name='10L', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(131491.25, 328296.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(131528.53125, 328306.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(131443.75, 328336.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(131513.5, 328358.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(131478.375, 328347.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(132265.46875, 325993, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(132292.1875, 326000.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(132316.96875, 326007.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(132342, 326014.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(131454.4375, 328287.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(131419, 328281.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(130687.046875, 328877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='139', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(132063.40625, 328380.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='110', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(130663.5078125, 328868.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='140', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(131712.5, 328389.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(130712.234375, 328882.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='138', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(131268.34375, 328632.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='120', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(130640.796875, 328859.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='141', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(132634.4375, 326381.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(132618.625, 326377.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(132602.84375, 326373.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(132586.984375, 326369.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(132571.28125, 326365.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(132539.640625, 326357.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(132523.984375, 326353.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(132508.140625, 326349.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(132476.625, 326341.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(132460.984375, 326337.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(132445.09375, 326333.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(132429.296875, 326329.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(132413.4375, 326325.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(132382.03125, 326317.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(132473.4375, 326492.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(132520.8125, 326504.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(132552.21875, 326512.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(132583.90625, 326520.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(132505.21875, 326500.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(132568.078125, 326516.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(132599.5625, 326524.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(132394.5625, 326472.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(132410.375, 326476.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(132489.328125, 326496.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(132426.125, 326480.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(132378.765625, 326468.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(132457.640625, 326488.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(132347.171875, 326460.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(132432.5625, 326686.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(132479.875, 326698.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(132463.953125, 326694.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(132354.046875, 326665.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(132369.4375, 326670.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(132448.234375, 326690.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(132385.140625, 326674.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(132338.203125, 326661.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(132416.75, 326682.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(132306.359375, 326654.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(132412.703125, 326830.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(132428.609375, 326833.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(132334.015625, 326809.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(132318.171875, 326805.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(132396.96875, 326826.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(132349.78125, 326813.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(132365.625, 326817.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(132286.53125, 326797.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(132444.421875, 326837.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(132270.875, 326793.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(132375.015625, 326978.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(132390.890625, 326981.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(132296.328125, 326958.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(132280.484375, 326954.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(132359.53125, 326974.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(132328.125, 326965.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(132343.46875, 326970.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(132249.09375, 326945.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(132406.625, 326985.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(132233.296875, 326941.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(132359.578125, 327468.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(132320.8125, 327458.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(132262.65625, 327443.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(132340.1875, 327463.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(132301.421875, 327453.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(132282.046875, 327448.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(132223.890625, 327433.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(132204.515625, 327428.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(132126.984375, 327409, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(132107.59375, 327404.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(132185.125, 327423.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(132243.28125, 327438.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(132165.75, 327418.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(132146.359375, 327413.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(132293.03125, 327568.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(132230.046875, 327551.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(132308.765625, 327572.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(132277.375, 327564.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(132261.453125, 327560.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(132099.265625, 327517.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(132118.65625, 327522.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(132196.1875, 327542.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(132176.796875, 327537.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(132157.421875, 327532.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(132214.171875, 327547.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(132079.890625, 327513, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(132138.03125, 327527.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(132324.703125, 327576.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(132064.46875, 327845.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(132017.3125, 327832.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(132048.796875, 327840.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(132001.484375, 327828.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(131985.109375, 328026.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(132017.0625, 328034.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='103', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(131953.765625, 328018.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(131969.5625, 328022.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(132067.53125, 328365.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(132071.546875, 328349.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(132075.5625, 328333.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(132079.65625, 328317.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='106', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(132083.703125, 328302.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='105', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(132088.03125, 328286.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='104', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(131259.796875, 328618.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='121', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(131251.484375, 328604.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='122', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(131243.078125, 328590.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='123', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(131225.828125, 328562.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='124', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(131217.1875, 328548.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='125', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(130846.71875, 328896.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='132', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(130821.890625, 328854.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='134', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(130788.2109375, 328799.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='137', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(130796.59375, 328813.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='136', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(130830.125, 328868.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='133', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(130813.53125, 328840.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='135', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(131686.671875, 328383.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(131132.421875, 328842.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='127', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(131140.875, 328856.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='128', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(131123.84375, 328828.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='126', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(131149.265625, 328869.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='129', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(131166.421875, 328897.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='130', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(131174.90625, 328911.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='131', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(131254.5, 328235.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='142', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(131212.671875, 328260, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='143', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(131170.125, 328284.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='144', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(131149.28125, 328222.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='145', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(131191.609375, 328197.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='146', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(131233.21875, 328174.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='147', length=21.0, width=15.0, height=8.0, shelter=False))


class Nevatim(Airport):
    id = 8
    name = "Nevatim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4475000, vhf_low_hz=39850000, vhf_high_hz=132400000, uhf_hz=251450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(129123.667969, 360907.984375, terrain), terrain)

        self.runways.append(Runway(id=1, name='08L-26R', main=RunwayApproach(name='08L', heading=80, beacons=[]), opposite=RunwayApproach(name='26R', heading=260, beacons=[RunwayBeacon(id='airfield8_1', runway_name='08L-26R', runway_id=1, runway_side='26R'), RunwayBeacon(id='airfield8_0', runway_name='08L-26R', runway_id=1, runway_side='26R')])))
        self.runways.append(Runway(id=3, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield8_2', runway_name='07-25', runway_id=3, runway_side='25'), RunwayBeacon(id='airfield8_3', runway_name='07-25', runway_id=3, runway_side='25')])))
        self.runways.append(Runway(id=2, name='08R-26L', main=RunwayApproach(name='08R', heading=80, beacons=[]), opposite=RunwayApproach(name='26L', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(129447.609375, 361887, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(129466.53125, 361874.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(129162.640625, 361705.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(129135.71875, 361723.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(129044.3203125, 361785.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(129098.3515625, 361748.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(129483.875, 361863.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(129503.2890625, 361849.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(129190.15625, 361687.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(129520.703125, 361837.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(127129.8828125, 363605.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(127115.6015625, 363550.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(127174.8984375, 363780.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(127170.3984375, 364006.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(127159.546875, 363720.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(128338.8828125, 363699.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(127101.296875, 363487.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(127086.78125, 363432.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(128346.125, 363731.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(127144.25, 363666.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(128322.5390625, 363636.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(128459.4453125, 363738.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(128404.953125, 363652.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(128436.703125, 363645.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(128500.25, 363629.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(128468.046875, 363636.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(128427.5859375, 363746.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(128330.484375, 363668.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(128491.171875, 363731.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(128522.6953125, 363723.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(129557.765625, 361811.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(129593.921875, 361785.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(128551.6484375, 363576.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(129540.4765625, 361823.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(129612.484375, 361772.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(129576.5078125, 361797.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(128537.265625, 363519.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(129630.015625, 361760.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(128543.8671875, 363548.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(128557.9609375, 363605.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(128528.15625, 359637.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(128557.4609375, 359955.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(128532.2109375, 360009.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(128494.59375, 359599.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(128463.390625, 359563.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(128488.609375, 359503.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(128520.4375, 359538.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(128557.3828125, 359578.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(128612.203125, 359961.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(128510.3046875, 359950.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(126983.359375, 362998.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(127021.1484375, 363148.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(127007.2578125, 363097.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(127045.828125, 363246.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(126969.734375, 362944, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(126932.375, 362818.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(126907.7890625, 362716.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(126850.3671875, 362504.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(126882.609375, 362615.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(126865.0390625, 362563.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(126898.734375, 362666.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(127033.375, 363197, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(126924.453125, 362764.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(126968.34375, 363846.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(126924.140625, 363858.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(127060.5859375, 363299.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(127012.625, 363837.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(126878.8671875, 363870.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(126995.3125, 363047.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(128717.2265625, 360282.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(128667.375, 362041.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(129030.484375, 361793.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(128724.4296875, 360234.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(128640.2578125, 362060.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(128694.640625, 362023.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(128613.5625, 362078.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(128662.3046875, 360245.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(128732.921875, 360180.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(129016.8828125, 361803.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(128454.59375, 359205.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(128407.734375, 359177.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(128418.609375, 359117.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(128442.2109375, 359331.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(128486.8515625, 359319.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(128465.7578125, 359325.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(128533.2890625, 359308.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(128556.25, 359301.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(128459.375, 359141.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(128419.59375, 359339.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(128508.9609375, 359312.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(128366.5, 359153.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(128504.8203125, 359167.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(128679.3046875, 360146.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(128669.53125, 360198.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(128628.796875, 360023.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(128576.59375, 360018, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(128819.921875, 359236.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(128855.125, 359228.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(128790.5078125, 359247.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(128887.640625, 359219.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(128923.46875, 359210.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(128956.2734375, 359201.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(126475.265625, 363027.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(126462.2109375, 362967.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='105', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(126433.1953125, 362891.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(126420.625, 362841.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(129172.9609375, 362519.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(129219.9296875, 362534.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(129265.0859375, 362550.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(129202.46875, 362466.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='110', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(129247.4375, 362482.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='111', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(129295.328125, 362497.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='112', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(129417.125, 362756.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='115', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(129398.1953125, 362801.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='114', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(129379.9140625, 362848.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='113', length=21.0, width=15.0, height=8.0, shelter=False))


class Ramon_Airbase(Airport):
    id = 9
    name = "Ramon Airbase"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4500000, vhf_low_hz=39900000, vhf_high_hz=119200000, uhf_hz=251500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(80825.4375, 328661.15625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield9_2'))
        self.runways.append(Runway(id=1, name='07R-25L', main=RunwayApproach(name='07R', heading=70, beacons=[]), opposite=RunwayApproach(name='25L', heading=250, beacons=[])))
        self.runways.append(Runway(id=2, name='07L-25R', main=RunwayApproach(name='07L', heading=70, beacons=[]), opposite=RunwayApproach(name='25R', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(79515.140625, 329132.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(79468.921875, 329151.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(79454.8359375, 330063.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(79478.9609375, 330083.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(79502.625, 330102.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(79589.53125, 330170.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(79613.9140625, 330189.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(79637.2109375, 330208.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(79662.234375, 330227.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(79686.078125, 330246.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(79684.5625, 330367.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(79345.796875, 330075.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(79365.59375, 330091.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(79385.5078125, 330106.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(79444.203125, 330152.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(79424.515625, 330137.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(79404.9296875, 330122.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(79483.3203125, 330184.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(79463.6640625, 330168.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(79503.0703125, 330199.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(79522.78125, 330215.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(79542.46875, 330230.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(79562.09375, 330245.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(79581.7578125, 330261.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(79601.421875, 330276.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(79620.8203125, 330292.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(79640.7890625, 330307.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(79477.046875, 328942.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(79452.328125, 328953.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(79426, 328965.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(79398.5390625, 328975.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(79373.203125, 328985.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(79715.1953125, 328978.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(79737.9375, 328967.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(79760.734375, 328957.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(79783.7421875, 328947.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(79806.5859375, 328937.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(79848.7421875, 328909.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(79871.1640625, 328898.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(79894.1640625, 328888.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(79917.2421875, 328878.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(79940.3203125, 328869.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(79963.46875, 328860.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(79986.78125, 328850.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(80009.703125, 328840.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(79845.90625, 328674.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(79867.6875, 328663.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(79888.65625, 328654.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(79911.65625, 328644.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(79587.796875, 327247, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(79548.578125, 327219.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(79508.9296875, 327191, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(79669.6484375, 327230.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(79363.6015625, 327501.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(79244.59375, 327453.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(79278.4296875, 327491.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(79307.71875, 327528.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(79681.609375, 327505.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(79698.6484375, 327493.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(79722.8984375, 327484.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(79744.0390625, 327474.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(79764.21875, 327463.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(79787.9765625, 327454.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(79502.0390625, 327987.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(79532.8984375, 328026.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(79562.0859375, 328063.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(79622.4140625, 328036.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(79504, 328269.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(79527.125, 328328.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(79487.0234375, 328356.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(79445.59375, 328385.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(79278.140625, 327680.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(79162.109375, 327799.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(79207.828125, 327778.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(79253.3515625, 327758.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(80167.1484375, 329572.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(80200.546875, 329607.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(80235.09375, 329642.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(80316.921875, 329639.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(80224.5390625, 329862.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(80198.703125, 329943.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(80245.3203125, 329921.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(80288.1875, 329903.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(80491.0625, 330188.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(80522.859375, 330225.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(80554.4140625, 330261.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(80605.7265625, 330224.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(80461.4375, 330497.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(80461.75, 330580.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(80499.296875, 330548.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(80537.2578125, 330516.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(81046.7109375, 330474.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(81104.5, 330497.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(81099.5625, 330545.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(81094.3125, 330594, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(81040.9375, 330221.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(81004.6015625, 330237.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(80969.7421875, 330253.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(80933.75, 330273.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(80900.6015625, 330283.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(79818.375, 328714.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(79795.34375, 328724.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(79773.4296875, 328735.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(79750.015625, 328745.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(79281.4296875, 330049.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(81041.125, 330522.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(81035.6640625, 330571.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(80497.9296875, 330465.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(80534.8359375, 330432.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(80637.046875, 330261.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(80573.2421875, 330188.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(80268.5703125, 329842.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(80313.1484375, 329822.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(80283.3828125, 329603.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(80250.4296875, 329568.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(79462.7265625, 328297.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(79422.5390625, 328323.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(79591.3828125, 327997.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(79561.6484375, 327960.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(79232.9140625, 327700.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(79188.71875, 327719.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(79333.6484375, 327462.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(79302.0859375, 327424.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(79630.734375, 327201.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(79590.8203125, 327173.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))


class Ovda(Airport):
    id = 10
    name = "Ovda"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=129900000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-11512.652832, 355892.671875, terrain), terrain)

        self.runways.append(Runway(id=2, name='03R-21L', main=RunwayApproach(name='03R', heading=30, beacons=[]), opposite=RunwayApproach(name='21L', heading=210, beacons=[])))
        self.runways.append(Runway(id=1, name='03L-21R', main=RunwayApproach(name='03L', heading=30, beacons=[]), opposite=RunwayApproach(name='21R', heading=210, beacons=[RunwayBeacon(id='airfield10_1', runway_name='03L-21R', runway_id=1, runway_side='21R'), RunwayBeacon(id='airfield10_0', runway_name='03L-21R', runway_id=1, runway_side='21R')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-13089.150390625, 355755.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-13099.053710938, 355784.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-13112.072265625, 355814.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-13122.634765625, 355844.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-13135.317382812, 355874.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-13147.985351562, 355905.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-13439.055664062, 355694.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-13494.80859375, 355767.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-13449.061523438, 355764.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-13400.7578125, 355759.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-13452.575195312, 356049.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-13466.625, 356111.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-13420.362304688, 356116.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-13373.416992188, 356122.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-13261.71484375, 356286.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-13235.107421875, 356456.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-13222.94140625, 356410.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-13212.458984375, 356363.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-12877.564453125, 356341.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-12872.709960938, 356404.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-12826.576171875, 356396.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-12778.5234375, 356386.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-12420.90234375, 356470.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-12388.791992188, 356503.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-12356.400390625, 356535.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-12447.771484375, 356537.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-11862.40234375, 356622.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-11873.599609375, 356649.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-11883.848632812, 356676.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-11894.767578125, 356704.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-11925.56640625, 356783.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-11895.16015625, 356795.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-11860.782226562, 356808.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-11833.40625, 356819.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-11806.34765625, 356829.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-11778.922851562, 356840.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-11818.291992188, 356711.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-11791.323242188, 356721.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-11763.821289062, 356731.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-11736.40234375, 356742.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-11214.426757812, 356934.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-11220.896484375, 356996.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-11173.833007812, 356996.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-11124.65234375, 356994.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-10816.41796875, 356631.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-10829.5390625, 356657.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-10841.040039062, 356687.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-10851.951171875, 356718.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-10863.3671875, 356748.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-10874.952148438, 356777.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-10845.02734375, 357213, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-10807.264648438, 357151.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-10782.8984375, 357191.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-10758.264648438, 357233.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-10543.947265625, 357344.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-10492.556640625, 357386.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-10469.682617188, 357343.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-10444.936523438, 357302.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-10304.133789062, 357283.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-10140.760742188, 357321.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-10179.247070312, 357293.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-10218.346679688, 357265.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-10039.358398438, 357022.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-10006.081054688, 357058.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-9973.3330078125, 357094.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-9922.619140625, 357058.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-9955.16015625, 357023.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-9987.166015625, 356987.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-10240.881835938, 356845.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-10259.946289062, 356887.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-10277.198242188, 356932.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-10295.98046875, 356974.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-10309.79296875, 356439.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-10321.577148438, 356467.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-10332.900390625, 356497.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-10344.4765625, 356526.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-10355.96875, 356556.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-10366.762695312, 356587.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-10305.711914062, 356088.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-10376.810546875, 356022.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-10337.262695312, 355967.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-10271.11328125, 355981.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-10263.731445312, 357311.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-10224.3125, 357339.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-10519.561523438, 357302.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-10494.326171875, 357259.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-10871.38671875, 357171.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-10896.467773438, 357129.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-11166.80078125, 356934.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-11117.146484375, 356932.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-12482.185546875, 356503.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-12517.62109375, 356469.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-12830.407226562, 356333.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-12782.1328125, 356324, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-13273.1796875, 356334.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-13284.280273438, 356382.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-13404.5859375, 356056.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-13355.11328125, 356062.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-13391.083984375, 355693.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-13341.693359375, 355690.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))


class Kibrit_Air_Base(Airport):
    id = 11
    name = "Kibrit Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=118050000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(20567.87793, 120267.300781, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield11_0'))
        self.runways.append(Runway(id=2, name='32R-14L', main=RunwayApproach(name='32R', heading=320, beacons=[]), opposite=RunwayApproach(name='14L', heading=140, beacons=[])))
        self.runways.append(Runway(id=1, name='32L-14R', main=RunwayApproach(name='32L', heading=320, beacons=[]), opposite=RunwayApproach(name='14R', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(21507.98308942, 119067.16159036, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(21450.98239712, 119172.3559135, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(21349.164955264, 119129.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(21312.796627447, 119265.66297411, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(20839.248604444, 119748.19542205, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(20725.007622992, 119811.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(19570.997255553, 120899.79024906, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(19473.444218007, 120915.9995109, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(19507.782532735, 121015.25036258, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(19383.326024191, 121016.04707304, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(19397.181083056, 121117.40855201, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(20037.266044992, 121379.96004716, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(20017.251310123, 121478.67477566, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(19920.71579129, 121445.77637103, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(19908.27145962, 121542.58669574, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(19813.681714891, 121537.00949416, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))


class Kedem(Airport):
    id = 12
    name = "Kedem"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=118150000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(134332.039062, 325363.625, terrain), terrain)

        self.runways.append(Runway(id=1, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(134032.61518929, 325668.41126978, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(134027.296875, 325693.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(134022.125, 325719.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(134016.4375, 325744.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(134010.640625, 325769.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(134004.71875, 325795.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(133962.67644714, 325962.89019768, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(133957.90625, 325986.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(133952.14153943, 326011.39796036, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(133945.95770512, 326038.29229488, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(133940.46230914, 326063.05698951, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(133935.30882634, 326088.40441317, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(133928.96781963, 326113.93382634, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(133923.48804866, 326138.81984731, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(134533.265625, 325759.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(134538.515625, 325837.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(134533.0625, 325863.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(134527.59375, 325888.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(134522.203125, 325913.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(134516.734375, 325939.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(134511.296875, 325964.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(134505.84375, 325990.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(134498.75, 325829.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(134492.59375, 325854.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(134482.140625, 325905.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(134487.625, 325879.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(134475.984375, 325931.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='27', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(134470.765625, 325955.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='28', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(134466.203125, 325981.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='29', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(134579.3125, 326379.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='43', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(134595.859375, 326757.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(134504.421875, 326038.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(134499.0625, 326063.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(134493.875, 326088.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='32', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(134488.15625, 326114.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(134482.6875, 326139.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(134477.328125, 326164.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(134471.9375, 326190.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(134466.578125, 326216.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(134430.796875, 326101.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(134436.0625, 326076.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(134415.125, 326178.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(134420.03125, 326152.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(134409.890625, 326202.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(134527.09375, 326513.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='44', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(134528.125, 326543.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(134529.75, 326573.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='46', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(134531.21875, 326604.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='47', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(134532, 326633.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(134533.21875, 326664.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='49', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(134457.59375, 326457.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='50', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(134460.796875, 326505.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='51', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(134463.609375, 326553.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='52', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(134465, 326601.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='53', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(134467.03125, 326649.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='54', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(134469.359375, 326697.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='55', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(134407.5625, 326460.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='56', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(134409.703125, 326508.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='57', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(134411.765625, 326556.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='58', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(134414.265625, 326604.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='59', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(134416.515625, 326652, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='60', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(134418.5, 326700, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='61', length=30.0, width=23.0, height=10.0, shelter=False))


class Wadi_al_Jandali(Airport):
    id = 13
    name = "Wadi al Jandali"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=118900000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(2085.398132, 56774.521484, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield13_2'))
        self.runways.append(Runway(id=1, name='01R-19L', main=RunwayApproach(name='01R', heading=10, beacons=[]), opposite=RunwayApproach(name='19L', heading=190, beacons=[])))
        self.runways.append(Runway(id=2, name='01L-19R', main=RunwayApproach(name='01L', heading=10, beacons=[RunwayBeacon(id='airfield13_1', runway_name='01L-19R', runway_id=2, runway_side='01L'), RunwayBeacon(id='airfield13_0', runway_name='01L-19R', runway_id=2, runway_side='01L')]), opposite=RunwayApproach(name='19R', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-2020.6274397718, 56508.741215841, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-2145.3559570312, 56472.83203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-2311.512586902, 56993.25845529, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-2169.5693542919, 57039.396360598, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-2095.9883365678, 57101.506773795, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-1996.1820374537, 57107.301961397, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-1835.7633056641, 57141.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-1812.4378662109, 57149.87109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-1789.0079345703, 57158.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-1765.5548095703, 57167.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-1742.2889404297, 57176.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-1718.8199462891, 57185.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-1695.2272949219, 57193.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-1671.9129638672, 57202.16796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-1476.7272949219, 57227.546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='49', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-1154.3685302734, 57326.45703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-663.90100097656, 56941.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-639.85852050781, 56948.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-615.75354003906, 56955.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-591.73089599609, 56962.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-567.73419189453, 56969.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-543.69866943359, 56976.07421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-519.81707763672, 56983.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-495.73645019531, 56990.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-252.79245543654, 57647.673209751, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-292.18443846877, 57632.260729555, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-291.05137643363, 57785.171079961, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-336.76864784472, 57765.385703545, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(371.15786743164, 57906.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(394.61383056641, 57915.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(417.91857910156, 57924.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(441.32446289062, 57933.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(464.78088378906, 57941.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(488.21130371094, 57950.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(499.13756093892, 58267.148195083, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(629.21954329664, 58290.254355277, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(626.01570350814, 58045.453780637, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(696.96642374934, 58138.874307869, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(823.77111816406, 58231.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-1844.1940687544, 56561.832116065, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-1763.1457212243, 56588.014143922, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-1696.5216960773, 56635.607893922, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-1613.3855647994, 56662.8430205, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-1567.8363792401, 56666.420868648, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-2080.0724161562, 57289.361282649, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-2101.2807915087, 57374.850640992, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-1974.9837530669, 57411.99009383, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-1810.388419439, 57411.421753732, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-738.0951107276, 57629.568185768, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-924.69158696083, 57565.93388776, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(277.859375, 57208.71484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(671.92012245345, 57248.497405024, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(770.19071222058, 57277.84416322, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(876.49849159408, 57287.754005437, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(959.85109341498, 57360.527999387, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(1125.7532948806, 57340.246936448, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(1206.7453568978, 57366.341230047, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(1254.9566928774, 57426.223003842, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(1324.9264978067, 57461.553353767, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(1220.6034944053, 57912.704188366, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(1273.2024371027, 58060.956582223, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(1140.6815405859, 58347.589445629, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(905.0303788763, 58320.215273441, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(2146.8883194935, 57447.589577003, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(2211.4097080901, 57465.199367282, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(2276.3607578891, 57483.59278033, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(2340.7272129673, 57500.582686887, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(2404.918293122, 57519.466639859, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(2469.3603498393, 57537.82072572, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(2533.6201154643, 57556.09278033, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(2598.2717267924, 57573.64746783, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))


class Al_Mansurah(Airport):
    id = 14
    name = "Al Mansurah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118250000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(101487.527344, 19421.140625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield14_0'))
        self.runways.append(Runway(id=2, name='35-17', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='17', heading=170, beacons=[])))
        self.runways.append(Runway(id=1, name='32-14', main=RunwayApproach(name='32', heading=320, beacons=[]), opposite=RunwayApproach(name='14', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(100268.28125, 20078.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(100191.203125, 20101.376953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(100187.7109375, 20167.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(100225.8515625, 19963.13671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(100332.3828125, 19911.529296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(100377.28125, 20551.185546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(100458.1640625, 20490.470703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(100630.3125, 20417.650390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(100758.8359375, 20494.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(100865.8046875, 20431.927734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(100983.703125, 20441.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(100667.0546875, 19855.517578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(100655.8984375, 19805.337890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(100714.140625, 19689.572265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(100708.359375, 19736.865234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(100882.140625, 19438.607421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(100893.3984375, 19329.80078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(101019.046875, 19435.310546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(101187.2109375, 19240.88671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(101255.5078125, 19231.345703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(101349.40625, 19151.662109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(101373.8515625, 19098.57421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(101492.03125, 18996.126953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(101802.9140625, 18778.298828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(101874.8515625, 18660.666015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(101999.53125, 18565.447265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(102067.6953125, 18547.041015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(102593.0859375, 18172.947265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(102627.640625, 18702.5703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(102596.765625, 18777.513671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(102453.0859375, 18712.2890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(102419.890625, 18829.814453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(102325.9609375, 18917.16015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(102267.390625, 18870.646484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(102788.0625, 18354.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(102777.1171875, 18378.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(102766.84375, 18401.658203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(102756.3671875, 18424.927734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(102745.953125, 18447.224609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(103187.2109375, 19178.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(103311.609375, 19196.193359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(103411.140625, 19720.79296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(103314.0703125, 19715.888671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(103240.65625, 19839.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))


class AzZaqaziq(Airport):
    id = 15
    name = "AzZaqaziq"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=118300000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(60146.006775, 41192.934448, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield15_0'))
        self.runways.append(Runway(id=2, name='36R-18L', main=RunwayApproach(name='36R', heading=360, beacons=[]), opposite=RunwayApproach(name='18L', heading=180, beacons=[])))
        self.runways.append(Runway(id=1, name='36L-18R', main=RunwayApproach(name='36L', heading=360, beacons=[]), opposite=RunwayApproach(name='18R', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(61825.319091797, 41083.471405029, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(61713.11328125, 41072.621826172, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(61604.445800781, 40997.91897583, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(61519.531616211, 41076.186126709, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(60918.097900391, 41579.110443115, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(61023.893310547, 41625.119598389, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(61141.740112305, 41468.940437317, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(60820.052612305, 41661.558074951, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(60713.50793457, 41486.111473083, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(60475.042663574, 41402.53997612, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(60472.884521484, 41433.467887878, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(60471.01751709, 41464.395896912, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(60469.297424316, 41495.395332336, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(60032.454193115, 41475.582206726, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(59849.218093872, 41516.758789062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(58956.490905762, 40959.701568604, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(58774.750366211, 41041.664154053, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(58646.180114746, 41035.686584473, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(58800.52130127, 40934.469482422, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(58737.670593262, 40859.917419434, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(58628.547546387, 40859.917541504, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(58503.356811523, 40924.164428711, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(61386.828857422, 41178.64251709, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(61326.60925293, 41481.696533203, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(61299.58581543, 41527.411499023, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(59711.174331665, 41326.783504486, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(59662.423408508, 41323.955097198, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(59563.278354645, 41319.298377991, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(59501.259162903, 41315.13319397, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))


class Bilbeis_Air_Base(Airport):
    id = 16
    name = "Bilbeis Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=118350000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(38473.015625, 35431.076172, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield16_1'))
        self.runways.append(Runway(id=3, name='27L-09R', main=RunwayApproach(name='27L', heading=270, beacons=[]), opposite=RunwayApproach(name='09R', heading=90, beacons=[])))
        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.runways.append(Runway(id=2, name='35R-17L', main=RunwayApproach(name='35R', heading=350, beacons=[RunwayBeacon(id='airfield16_2', runway_name='35R-17L', runway_id=2, runway_side='35R'), RunwayBeacon(id='airfield16_0', runway_name='35R-17L', runway_id=2, runway_side='35R')]), opposite=RunwayApproach(name='17L', heading=170, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(40207.5546875, 35040.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(40253.6328125, 35095.30859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(40292.28515625, 35140.69140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(39715.80859375, 35742.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(39595.79296875, 35761.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(39541.07421875, 35842.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(39427.94140625, 35903.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(39274.69921875, 35829.05078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(38473.77734375, 35772.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(38495.08203125, 35790.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(38517.46875, 35808.35546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(38539.30859375, 35826.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(38560.96484375, 35844.93359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(38582.80078125, 35862.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(38604.3359375, 35881.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(38625.5703125, 35900.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(39901.453125, 35487.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(39954.3828125, 35696.60546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(39989.08203125, 35731.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(40027.07421875, 35771.93359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(40068.08203125, 35809.54296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(40099.2578125, 35351.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(40146.4296875, 35399.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(40186.80859375, 35451.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(36638.015625, 35714.34765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(36686.37890625, 35587.81640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(36733.13671875, 35536.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(36784.8359375, 35507.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(36834.80859375, 35472.5078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(36886.93359375, 35440.63671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(36921.32421875, 35400.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(36968.8046875, 35359.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(37025.921875, 35317.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(37079.41796875, 35295.84765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(37124.17578125, 35247.67578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(37149.48828125, 33896.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(37094.68359375, 33772.16015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(37133.500610368, 33665.99609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(37161.324829118, 33540.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(37104.83984375, 33173.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(37148.6171875, 33118.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(37045.62890625, 33062.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(37140.14453125, 33014.4921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(37778.88671875, 33214.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(37826.86328125, 33254.19140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(37867.25390625, 33295.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(38751.859375, 35871.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(38527.09765625, 35684.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(38561.19140625, 35713.80859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))


class Cairo_International_Airport(Airport):
    id = 17
    name = "Cairo International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=118100000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(6582.669189, 18419.84375, terrain), terrain)

        self.runways.append(Runway(id=2, name='05C-23C', main=RunwayApproach(name='05C', heading=50, beacons=[RunwayBeacon(id='airfield17_1', runway_name='05C-23C', runway_id=2, runway_side='05C'), RunwayBeacon(id='airfield17_9', runway_name='05C-23C', runway_id=2, runway_side='05C')]), opposite=RunwayApproach(name='23C', heading=230, beacons=[RunwayBeacon(id='airfield17_5', runway_name='05C-23C', runway_id=2, runway_side='23C'), RunwayBeacon(id='airfield17_8', runway_name='05C-23C', runway_id=2, runway_side='23C')])))
        self.runways.append(Runway(id=3, name='05L-23R', main=RunwayApproach(name='05L', heading=50, beacons=[RunwayBeacon(id='airfield17_10', runway_name='05L-23R', runway_id=3, runway_side='05L'), RunwayBeacon(id='airfield17_0', runway_name='05L-23R', runway_id=3, runway_side='05L')]), opposite=RunwayApproach(name='23R', heading=230, beacons=[RunwayBeacon(id='airfield17_6', runway_name='05L-23R', runway_id=3, runway_side='23R'), RunwayBeacon(id='airfield17_11', runway_name='05L-23R', runway_id=3, runway_side='23R')])))
        self.runways.append(Runway(id=1, name='05R-23L', main=RunwayApproach(name='05R', heading=50, beacons=[RunwayBeacon(id='airfield17_2', runway_name='05R-23L', runway_id=1, runway_side='05R'), RunwayBeacon(id='airfield17_3', runway_name='05R-23L', runway_id=1, runway_side='05R')]), opposite=RunwayApproach(name='23L', heading=230, beacons=[RunwayBeacon(id='airfield17_4', runway_name='05L-23L', runway_id=1, runway_side='23L'), RunwayBeacon(id='airfield17_7', runway_name='05R-23L', runway_id=1, runway_side='23L')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(9090.685546875, 15114.026367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(9040.2802734375, 15165.369140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(8984.818359375, 15217.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(8988.9775390625, 15016.747070312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(8940.0673828125, 14963.115234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(8890.93359375, 14907.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(8843.1259765625, 14854.794921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(8803.4560546875, 14794.475585938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(8755.091796875, 14741.220703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(8707.6259765625, 14687.243164062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(8657.8134765625, 14632.901367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(8609.7607421875, 14578.685546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(8562.71484375, 14524.846679688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(8513.65625, 14470.127929688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(8465.744140625, 14415.962890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(8415.935546875, 14362.424804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(8366.7626953125, 14308.389648438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(8341.9873046875, 14210.829101562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(8307.220703125, 14170.360351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(8274.845703125, 14135.177734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(8236.0146484375, 14086.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(8190.5834960938, 14033.063476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(8144.5439453125, 13981.740234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(7623.75390625, 13432.20703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(7606.2333984375, 13404.248046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(7588.203125, 13375.944335938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(7571.1166992188, 13348.794921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(7009.109375, 15852.967773438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(7064.6484375, 15907.971679688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(7115.0971679688, 15969.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(7170.2182617188, 16026.514648438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(7220.2016601562, 16087.126953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(6732.0650199144, 14895.740971265, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(6656.7246747985, 14912.521270872, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(6583.1315046725, 14928.783120469, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(6509.6793038963, 14947.765991371, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(6652.80078125, 14574.142578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(6577.279296875, 14591.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(6504.9541015625, 14609.358398438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(6430.7778320312, 14627.797851562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(6566.8193359375, 14246.672851562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(6491.2983398438, 14263.815429688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(6418.9731445312, 14281.888671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(6344.7963867188, 14300.329101562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(6296.236328125, 14119.645507812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(6367.486328125, 14102.450195312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(6443.4155273438, 14082.862304688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(6511.2700195312, 14065.430664062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(6385.2397460938, 14457.16796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(6453.1518554688, 14437.970703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(6524.0166015625, 14418.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(6594.1928710938, 14400.11328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(6461.3466796875, 14770.986328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(6530.3452148438, 14752.604492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(6602.025390625, 14734.080078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(6670.26953125, 14716.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(6615.2005658315, 15069.619301789, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(6545.2138671875, 15084.702148438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(7355.7553710938, 15289.125976562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(7313.4711914062, 15228.145507812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(7268.1889648438, 15172.518554688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(7187.3002929688, 15113.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(7095.3012695312, 15155.049804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(7034.7618448076, 15208.707379747, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(6999.5328278167, 15285.226274637, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(6978.2444932701, 15355.287771905, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(6907.5693359375, 15453.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(6829.1137695312, 15501.197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(6881.650390625, 15159.865234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(6854.9852608748, 15227.26115494, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(6833.3717732488, 15296.681353667, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(6804.7720993554, 15373.988965802, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(7750.1518554688, 15993.751953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(7694.2163085938, 16013.350585938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(7631.0004882812, 16033.868164062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(7567.4755859375, 16052.233398438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(7511.8583984375, 16069.197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(8453.861328125, 15798.021484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(8370.392578125, 15823.888671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(9105.8134765625, 15243.001953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(9058.9521484375, 15290.126953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(9007.7666015625, 15342.892578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(8994.48046875, 15507.741210938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(9012.48828125, 15579.264648438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(9025.96875, 15654.245117188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(8769.841796875, 15582.424804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(8698.4814453125, 15611.850585938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(9770.998046875, 16018.11328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='124', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(9690.9853515625, 16041.548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(9611.755859375, 16065.849609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(9523.3095703125, 16047.06640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(9475.1611328125, 16061.901367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(9426.599609375, 16075.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(9296.1767578125, 16114.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(9248.0888671875, 16129.517578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(9200.3974609375, 16145.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(9512.5537109375, 15951.341796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(9483.412109375, 15959.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(9453.4326171875, 15969.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(9422.71875, 15977.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(9392.2138671875, 15986.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(9250.2568359375, 16029.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(9220.5693359375, 16038.473632812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(9190.1279296875, 16047.908203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(8584.677734375, 16268.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(8517.7568359375, 16290.256835938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(8452.357421875, 16311.356445312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(8386.255859375, 16333.084960938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(8321.599609375, 16352.708007812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(8171.8842773438, 16376.038085938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(8115.8022460938, 16393.333984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(8058.8818359375, 16410.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(9047.1630859375, 16094.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(9017.0498046875, 16103.723632812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(8986.1123046875, 16112.241210938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(8955.904296875, 16121.602539062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(8925.1875, 16131.313476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(8894.6865234375, 16140.485351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(8864.6220703125, 16149.293945312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(8834.265625, 16158.612304688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(8802.9638671875, 16168.366210938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(8772.7529296875, 16177.174804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(8742.470703125, 16186.274414062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(9054.02734375, 16188.130859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(9007.1171875, 16202.369140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(8959.3115234375, 16215.420898438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(8911.0283203125, 16229.833007812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(8862.6611328125, 16244.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(8813.904296875, 16259.361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=40.0, width=40.0, height=12.0, shelter=False))


class Cairo_West(Airport):
    id = 18
    name = "Cairo West"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=118400000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(7349.451904, -33538.970703, terrain), terrain)

        self.runways.append(Runway(id=3, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.runways.append(Runway(id=2, name='34R-16L', main=RunwayApproach(name='34R', heading=340, beacons=[]), opposite=RunwayApproach(name='16L', heading=160, beacons=[])))
        self.runways.append(Runway(id=1, name='34L-16R', main=RunwayApproach(name='34L', heading=340, beacons=[RunwayBeacon(id='airfield18_1', runway_name='34L-16R', runway_id=1, runway_side='34L'), RunwayBeacon(id='airfield18_0', runway_name='34L-16R', runway_id=1, runway_side='34L')]), opposite=RunwayApproach(name='16R', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(7587.4819335938, -34102.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(7523.4580078125, -34087.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(7457.9458007812, -34071.43359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(7391.0390625, -34055.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(7326.5151367188, -34040.43359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(7261.17578125, -34025.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(7196.0395507812, -34010.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(7131.587890625, -33995.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(9082.2021484375, -32738.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(9112.4873046875, -32597.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(9171.83984375, -32455.49609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(8907.6298828125, -32629.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(8890.6083984375, -32391.126953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(8995.8837890625, -32274.966796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(8721.576171875, -32294.78515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(7303.5883789062, -32184.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(7335.4506835938, -32151.09765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(7367.4248046875, -32118.68359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(7397.7568359375, -32086.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(7432.03125, -32050.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(7466.609375, -32014.70703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(7501.1875, -31978.55078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(7585.6098632812, -31890.986328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(7621.2631835938, -31854.708984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(7656.318359375, -31818.505859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(7690.7016601562, -31782.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(7725.8754882812, -31746.400390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(7475.849609375, -31638.529296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(7425.9897460938, -31627.060546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(7354.923828125, -31602.134765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(7624.283203125, -31244.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(7661.9638671875, -31172.849609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(7700.0708007812, -31100.787109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(7218.283203125, -31018.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(7042.5629882812, -30869.478515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(7043.748046875, -31008.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(6893.65234375, -30899.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(6897.0200195312, -31044.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(7323.4682617188, -30125.662109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(7219.5932617188, -30153.583984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(7463.166015625, -30078.294921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(7403.02734375, -29874.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(7313.08203125, -29928.509765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(7224.630859375, -29953.486328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(7381.234375, -28822.669921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(7421.5688476562, -28868.08203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(7446.185546875, -28930.982421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(7473.0014648438, -29018.90234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(7510.2241210938, -29073.80078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(7515.6518554688, -29138.88671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(7546.0590820312, -29236.48046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(7741.1831054688, -29550.939453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(7771.3911132812, -29611.537109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(7812.0083007812, -29712.115234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(7830.4033203125, -29764.736328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(7854.775390625, -29810.525390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(7886.2622070312, -29889.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(7922.5869140625, -29977.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(7950.1254882812, -30040.517578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(8010.9111328125, -30066.01953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(8087.9409179688, -30139.310546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(8647.21484375, -32138.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(8626.84375, -32147.20703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(9305.48046875, -32218.51171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(9272.97265625, -32211.646484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(9394.861328125, -32124.736328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(9369.4404296875, -32118.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(9344.2822265625, -32111.634765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(9695, -32212.224609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(9804.19921875, -32233.33203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(9971.2734375, -32431.341796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(10039.5546875, -31910.267578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(9933.5908203125, -31873.470703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(9852.7236328125, -31786.05859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(9783.12109375, -31743.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(9597.05859375, -31521.419921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(9447.6943359375, -31596.994140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(9442.576171875, -31466.794921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(10439.37109375, -31636.638671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(10561.4375, -31463.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(10669.193359375, -31349.349609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(10639.333984375, -31163.05859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(10342.241210938, -31337.79296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(10450.653320312, -31070.310546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(10759.401367188, -30544.900390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(10646.498046875, -30395.845703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(10154.84765625, -30809.865234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(10180.896484375, -30405.005859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(9975.2763671875, -30558.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(9797.8037109375, -30456.337890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(9868.7626953125, -30172.7734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(10316.745117188, -30100.978515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(9885.9375, -29742.79296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(8767.892578125, -30248.630859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(8518.345703125, -30363.02734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(9058.7607421875, -32093.45703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(8800.7119140625, -31959.4140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(8522.455078125, -31897.806640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(8078.9096679688, -31771.984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(7996.1967773438, -31759.00390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(7945.8032226562, -31751.08984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(7813.5893554688, -31783.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(7623.0102539062, -31998.349609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))


class Inshas_Airbase(Airport):
    id = 19
    name = "Inshas Airbase"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118450000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(31044.584961, 20003.525391, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield19_1'))
        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[RunwayBeacon(id='airfield19_2', runway_name='04-22', runway_id=1, runway_side='22'), RunwayBeacon(id='airfield19_0', runway_name='04-22', runway_id=1, runway_side='22')])))
        self.runways.append(Runway(id=2, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(30594.619140625, 21334.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(30559.111328125, 21358.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(30525.169921875, 21383.564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30491.62890625, 21406.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(30458.390625, 21430.533203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30426.201171875, 21453.267578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(30393.4140625, 21476.232421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(30360.9375, 21498.876953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(30327.734375, 21522.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30295.19140625, 21545.556640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(31365.7265625, 19317.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(31346.162109375, 19295.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(31385.62109375, 19339.650390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(31405.625, 19361.470703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(31445.25390625, 19409.251953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(31296.125, 18885.458984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(31310.109375, 18790.927734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(31232.58984375, 18726.806640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(31260.220703125, 18635.82421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(30908.23046875, 18556.033203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(30783.51171875, 18603.947265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(30704.474609375, 18605.36328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(30654.083984375, 18692.935546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(30284.296875, 19051.08203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(30388.140625, 19129.841796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(30409.47265625, 19278.708984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(30520.23046875, 19335.900390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(29973.490234375, 19912.763671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(29911.150390625, 19938.90234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(30072.76953125, 20521.490234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(30141.482421875, 20501.29296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(30215.814453125, 20491.30859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(30272.779296875, 20476.33984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(30300.921875, 20524.134765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(30358.47265625, 20588.806640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(30373.27734375, 20660.25390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(30350.421875, 20731.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(30714.537109375, 20910.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(30779.2421875, 20982.46484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(31858.73828125, 21010.904296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(31923.478515625, 20800.728515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(31846.75, 20711.095703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(31735.021484375, 20867.134765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(31616.287109375, 20846.92578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(32095.251953125, 21085.134765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(32180.93359375, 21070.654296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(32261.298828125, 21130.666015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(32184.021484375, 21206.61328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(32332.67578125, 21246.05078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(32320.185546875, 20420.119140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(32322.3046875, 20535.16015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(32444.36328125, 20552.439453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(32449.369140625, 20678.076171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(30950.70703125, 18622.638671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(30986.990234375, 18590.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(31023.123046875, 18554.244140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(31566.033203125, 19349.197265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(31558.873046875, 19453.314453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(31607.521484375, 19398.189453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(31596.244140625, 19513.482421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))


class Hatzor(Airport):
    id = 20
    name = "Hatzor"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=118600000, uhf_hz=250600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(189869.304688, 332622.0625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield20_1'))
        self.beacons.append(AirportBeacon(id='airfield20_0'))
        self.runways.append(Runway(id=3, name='29R-11L', main=RunwayApproach(name='29R', heading=290, beacons=[]), opposite=RunwayApproach(name='11L', heading=110, beacons=[])))
        self.runways.append(Runway(id=2, name='29L-11R', main=RunwayApproach(name='29L', heading=290, beacons=[]), opposite=RunwayApproach(name='11R', heading=110, beacons=[])))
        self.runways.append(Runway(id=1, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[RunwayBeacon(id='airfield20_2', runway_name='05-23', runway_id=1, runway_side='05'), RunwayBeacon(id='airfield20_3', runway_name='05-23', runway_id=1, runway_side='05')]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(190508.15625, 333683.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(190495.21875, 333673.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(190482.203125, 333663.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(190469.421875, 333653.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(190422.765625, 333500.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(190396.5625, 333515.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(190369.71875, 333532.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(190340.84375, 333553.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(190183.859375, 333452.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(190202.734375, 333813.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(190064.53125, 334061.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(189091.8125, 334490.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(189085.109375, 334476.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(189098.953125, 334505.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(189105.984375, 334520.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(189112.765625, 334535.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(189119.75, 334549.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(188968.140625, 334232.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(188962.109375, 334217.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(188956.5625, 334201.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(188950.53125, 334186.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(188941.421875, 334024.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(188938.578125, 334044.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(188935.921875, 334064.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(188933.1875, 334084.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(189108.171875, 334003.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(189105.75, 334019.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(189103.390625, 334035.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(189101.140625, 334051.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(189098.734375, 334068.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(189096.421875, 334084.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(189275.9375, 332097.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(189262.921875, 332107.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(189236.703125, 332127.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(189249.71875, 332117.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(189210.625, 332146.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(189223.625, 332136.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(189184.4375, 332165.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(189197.453125, 332155.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(189158.25, 332184.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(189171.265625, 332175.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(189132.015625, 332204.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(189145.015625, 332194.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(189118.71875, 332213.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(189456.390625, 332298, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(189469.40625, 332288.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(189430.21875, 332317.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(189443.21875, 332307.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(189404.03125, 332336.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(189417.03125, 332327.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(189377.78125, 332355.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(189390.796875, 332346.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(189364.484375, 332365.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(189436.21875, 332728.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(189451, 332735.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(189406.59375, 332715.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(189421.375, 332721.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(189376.84375, 332701.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(189391.625, 332708.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(189347.1875, 332688.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(189361.96875, 332695.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(189332.3125, 332681.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(189315.9375, 332992.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(189330.71875, 332999.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(189286.3125, 332979.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(189301.09375, 332985.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(189256.546875, 332965.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(189271.328125, 332972.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(189226.90625, 332952.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(189241.6875, 332959.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(189212.015625, 332945.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(189334.9375, 334028.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(189337.28125, 334012.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(189330.125, 334061.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(189332.46875, 334045.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(189325.40625, 334093.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(189327.75, 334077.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(189320.546875, 334125.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(189322.890625, 334109.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(189317.953125, 334141.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(189341.234375, 333898.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(189337.390625, 333921.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(189333.625, 333945.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(189489.953125, 333380.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(189474.171875, 333377, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(189458.328125, 333373.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(189442.4375, 333369.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(189570.203125, 333495.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(190799.15625, 333463.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(189128.53125, 333851.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(189126.109375, 333868.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(189123.734375, 333884.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(189121.484375, 333900.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(189119.09375, 333916.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(189116.78125, 333932.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(189111.84375, 333965.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(189114.15625, 333948.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(189109.140625, 333981.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))


class Palmahim(Airport):
    id = 21
    name = "Palmahim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=118650000, uhf_hz=250650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(205486.703125, 329304.75, terrain), terrain)

        self.runways.append(Runway(id=1, name='03R-21L', main=RunwayApproach(name='03R', heading=30, beacons=[]), opposite=RunwayApproach(name='21L', heading=210, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(206004.984375, 329723, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(206032.671875, 329735.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H29', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(206060.640625, 329748.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(206182.03125, 329802.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(206209.546875, 329815.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(206237.6875, 329827.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(206576.21875, 329998.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(206611.265625, 330013.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(206645.625, 330029.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(206692.109375, 330050.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(206727.84375, 330065.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(206772.234375, 330086.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(206807.171875, 330101.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(206841.4375, 330116.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(206906.328125, 330250.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(206852.125, 330201.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(206806.5, 330181.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(206761.3125, 330159.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(206714.53125, 330140.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(206668.734375, 330120.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(206622.640625, 330100.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(206576.625, 330079.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(206531.078125, 330059.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(206242.5625, 329908.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(206197.671875, 329888.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(206150.75, 329867.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(206105.125, 329846.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(206059.21875, 329826.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(206014.21875, 329806.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(205967.734375, 329785.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(205842.453125, 329756.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(206038.65625, 329071.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(206032.046875, 329086.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(206025.28125, 329101.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(206018.703125, 329115.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(206012, 329130.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(206005.453125, 329145.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(205998.6875, 329160.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(205992.046875, 329175.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(205976.359375, 329210.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(205969.625, 329225.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(205956.203125, 329159.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(205962.546875, 329144.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(205969.03125, 329129.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(205975.34375, 329114.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(205981.765625, 329099.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(205988.046875, 329084.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(205994.53125, 329069.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(206000.90625, 329054.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(205931.78125, 329208.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(205938.484375, 329193.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(205639.8125, 329529.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(205646.328125, 329514.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(205633.03125, 329544.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(205621.609375, 329569.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(205615.15625, 329584.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(205593.5625, 329508.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(205600.078125, 329493.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(205586.78125, 329523.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(205575.359375, 329548.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(205568.6875, 329563.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(205481.359375, 329467.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(205487.890625, 329452.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(205474.578125, 329481.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(205463.15625, 329507.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(205456.484375, 329521.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(205686.96875, 329598.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(205680.53125, 329613.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(205698.125, 329573.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(205704.921875, 329558.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(205711.5, 329543.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(204805.359375, 329318.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(204811.875, 329303.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(204798.578125, 329333.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(204791.890625, 329348.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(205059.015625, 329426.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(205035.234375, 329415.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(204828.515625, 329195, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))


class Sde_Dov(Airport):
    id = 22
    name = "Sde Dov"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=118700000, uhf_hz=250700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(229223.96875, 337369.84375, terrain), terrain)

        self.runways.append(Runway(id=1, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(229101.578125, 337442.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(229070.875, 337428.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(229038.6875, 337410.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(229006.5625, 337395.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(228976.34375, 337379.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(228943.9375, 337364.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(228737.453125, 337404.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(228746.390625, 337450.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(228680.59375, 337416.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(228689.75, 337462.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(228743.046875, 337272.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(228702.125, 337280.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(228784.078125, 337263.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(228792.765625, 337309.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(228751.328125, 337318.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(228710.171875, 337326.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(228442.203125, 337257.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(228438.640625, 337273.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(228434.734375, 337291.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(228395.25, 337560.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(228391.890625, 337576.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(228388.5625, 337592.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(228385.25, 337608.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(228291.796875, 337614.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(228296.171875, 337594.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(228300.328125, 337575.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(228304.40625, 337555.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(228240.734375, 337590.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(228245.125, 337570.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(228249.28125, 337551.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(228253.359375, 337531.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(228236.875, 337610.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(228259.0625, 337508.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(228264.390625, 337480.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(228211.109375, 337508.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(228216.5625, 337481.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(228199.703125, 337556.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(228206.25, 337530.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(228282.234375, 337669.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(228286.984375, 337646.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(228274.328125, 337708.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(228277.671875, 337692.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))


class Tel_Nof(Airport):
    id = 23
    name = "Tel Nof"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4125000, vhf_low_hz=39150000, vhf_high_hz=118750000, uhf_hz=250750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(198386.8125, 341243.3125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield23_0'))
        self.runways.append(Runway(id=2, name='33L-15R', main=RunwayApproach(name='33L', heading=330, beacons=[]), opposite=RunwayApproach(name='15R', heading=150, beacons=[])))
        self.runways.append(Runway(id=3, name='33R-15L', main=RunwayApproach(name='33R', heading=330, beacons=[]), opposite=RunwayApproach(name='15L', heading=150, beacons=[])))
        self.runways.append(Runway(id=1, name='36-18', main=RunwayApproach(name='36', heading=360, beacons=[RunwayBeacon(id='airfield23_1', runway_name='36-18', runway_id=1, runway_side='36'), RunwayBeacon(id='airfield23_2', runway_name='36-18', runway_id=1, runway_side='36')]), opposite=RunwayApproach(name='18', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(199667.40625, 341034.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(199611, 341007.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(199205.375, 340963.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(199179.09375, 340992.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(199075.015625, 340937.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(199035.90625, 340938.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(198996.96875, 340870.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(198969.421875, 340898.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(198728.578125, 340806.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(198707.421875, 340827.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(198688.171875, 340848.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(198669.171875, 340868.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(198648.796875, 340890.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(198660.671875, 340708.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(198639.84375, 340730.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(198619.015625, 340753.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(198599.484375, 340774.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(198579, 340795.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(198558.75, 340817.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(198475.5625, 340927.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(198497.203125, 340946.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(198519.84375, 340966.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(198541.171875, 340986.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(198583.265625, 341412.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(198561.171875, 341433.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(198517.359375, 341474.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(198495.59375, 341494.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(198474.015625, 341515.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(198452.1875, 341537.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(198492.421875, 341416.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(198470.90625, 341437.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(198450.015625, 341458.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(198428.171875, 341480.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(198212.90625, 341341.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H32', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(198236.4375, 341364.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(198259.5, 341388.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(198282.078125, 341412.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H29', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(198303.796875, 341435.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(198251.140625, 341486.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(198228.8125, 341464, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(198206.53125, 341439.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(198184.359375, 341415.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(198161.65625, 341391.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(198757.71875, 340304.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(198745.515625, 340339.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(198665.046875, 340247.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(198678.140625, 340212.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(198620.5625, 340128.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(198607.234375, 340162.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(198495.28125, 340201.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(198483.1875, 340236.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(197912.515625, 340051.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(197913.140625, 340100.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(197914.09375, 340148.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(197707.71875, 340465.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(197756.328125, 340469.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(197804.875, 340473.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(197573.265625, 340686.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(197609.53125, 340719.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(197645.53125, 340752.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(197870.734375, 340703.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(197865.09375, 340718.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(197859.421875, 340733.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(197853.703125, 340749, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(197848.015625, 340764.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(197842.296875, 340779.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(197836.53125, 340794.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(197164.796875, 340908.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(197153.453125, 340920.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(197141.953125, 340931.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(197130.5, 340943.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(197119.125, 340954.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(197080.265625, 340870.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(197060.171875, 340869.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(197040.015625, 340869.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(196945.546875, 340922.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(196930.71875, 340935.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(196915.765625, 340950.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(197020.8125, 342451.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(197010.59375, 342464.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(197000.328125, 342476.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(196990.015625, 342489.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(196979.8125, 342502.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(196969.453125, 342514.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(196959.109375, 342527.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(197283.34375, 342435.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(197294.484375, 342447.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(197305.5625, 342459.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(197316.734375, 342471.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(197327.875, 342483.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(197338.796875, 342495.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(197349.859375, 342507.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(197380.046875, 342680.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(197431.9375, 342656.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(197409.4375, 342595.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(197268.46875, 342683.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(197235.546875, 342704.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(197955.03125, 342038.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(197966.171875, 342050.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(197977.25, 342062.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(197988.40625, 342074.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(197999.546875, 342086.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(198010.46875, 342098, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(198021.53125, 342110, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(198785.5, 341526.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(198792.140625, 341512.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(198798.515625, 341497.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(198805.1875, 341482.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(198822.59375, 341451.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(198463.859375, 341973.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(198449.8125, 341981.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(198435.765625, 341989.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(198421.640625, 341998.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(198407.625, 342006.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(198393.53125, 342014.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(198959.671875, 341443.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(198959.328125, 341459.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(198958.859375, 341475.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(198958.4375, 341491.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(198958.0625, 341508.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(198957.578125, 341524.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(198957.21875, 341540.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(198960.1875, 341426.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(199188.546875, 341513.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(199188.078125, 341530.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(199187.71875, 341546.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(199190.6875, 341432.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(199190.171875, 341448.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(199189.828125, 341465.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(199189.359375, 341481.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(199188.9375, 341497.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(198865, 341331.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(198827.03125, 341332.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))


class Ben_Gurion(Airport):
    id = 24
    name = "Ben-Gurion"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4150000, vhf_low_hz=39200000, vhf_high_hz=134600000, uhf_hz=250800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(217467.90625, 348036.15625, terrain), terrain)

        self.runways.append(Runway(id=3, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[RunwayBeacon(id='airfield24_1', runway_name='08-26', runway_id=3, runway_side='08'), RunwayBeacon(id='airfield24_0', runway_name='08-26', runway_id=3, runway_side='08')]), opposite=RunwayApproach(name='26', heading=260, beacons=[RunwayBeacon(id='airfield24_5', runway_name='08-26', runway_id=3, runway_side='26'), RunwayBeacon(id='airfield24_6', runway_name='08-26', runway_id=3, runway_side='26')])))
        self.runways.append(Runway(id=2, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[RunwayBeacon(id='airfield24_7', runway_name='30-12', runway_id=2, runway_side='30'), RunwayBeacon(id='airfield24_9', runway_name='30-12', runway_id=2, runway_side='30')]), opposite=RunwayApproach(name='12', heading=120, beacons=[RunwayBeacon(id='airfield24_2', runway_name='30-12', runway_id=2, runway_side='12'), RunwayBeacon(id='airfield24_8', runway_name='30-12', runway_id=2, runway_side='12')])))
        self.runways.append(Runway(id=1, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[RunwayBeacon(id='airfield24_3', runway_name='03-21', runway_id=1, runway_side='21'), RunwayBeacon(id='airfield24_4', runway_name='03-21', runway_id=1, runway_side='21')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(217111.796875, 345531.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(217217.28125, 345597.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(217310.578125, 345656.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(217398.578125, 345713.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(217486.296875, 345764.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(217613.671875, 345836.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(217211.140625, 345948.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(217275.453125, 345921.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(217344.125, 345934.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(217374.984375, 345998.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(217367.21875, 346066.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(217373.734375, 346211.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(217369.046875, 346276.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(217331.421875, 346338.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(217219.390625, 346310.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(217135.65625, 346450.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(217138.421875, 346382.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(216987.859375, 346336.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(216799.015625, 346316.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(216850.90625, 346173.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(216754.9375, 346242.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(216609.1875, 346486.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(216673.46875, 346523.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(216733.625, 346558, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(216813.015625, 346601.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(216910.921875, 346654.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(216998.1875, 346700.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(217079.1875, 346744.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(216808.203125, 347184.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(216784.59375, 347223.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(216760.90625, 347264.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(216737.953125, 347303.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(216760.296875, 347103.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(216737.3125, 347143.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(216714.78125, 347183.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(216692.453125, 347223.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(216669.140625, 347263.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(216923.890625, 346968, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(216862.3125, 346929.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(216797.953125, 346889.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(216381.625, 347752.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(216290.34375, 347728.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(216223.578125, 347712.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(216068.53125, 347665.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(215998.953125, 347646.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(215897.078125, 347686.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(215994.75, 347802.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(216068.40625, 347824.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(216137.1875, 347852.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(216209.234375, 347872.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(216287.125, 347893.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(216357.78125, 347913.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(216439.40625, 347936.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(216366.125, 348037.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(216295.578125, 348012.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(216194.9375, 347983.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(216107.3125, 347951.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(216017.28125, 347929.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(215971.75, 348085.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(215929.59375, 348045.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(215872.796875, 348011.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(215842.953125, 348078.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(215932.046875, 348817.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(215991.875, 348807.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(216063.96875, 348771.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(216134.28125, 348737.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(216205.765625, 348700, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(216942.34375, 348437.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(216996.09375, 348460.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(217057.953125, 348484.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(217418.6875, 348306.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(217452.578125, 348326.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(217485.4375, 348344.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(217517.5, 348361.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(217550.53125, 348378.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(217585.109375, 348396.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(217669.296875, 348439.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(217700.640625, 348457.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(217733.21875, 348473.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(217692.640625, 348549.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(217658.15625, 348531.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(217623.84375, 348511.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(217588.796875, 348493.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(217554.390625, 348475.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(217519.109375, 348456.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(217483.296875, 348438.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(217446.46875, 348419.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(217413.703125, 348402.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(217377.921875, 348386, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))


class St_Catherine(Airport):
    id = 25
    name = "St Catherine"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4175000, vhf_low_hz=39250000, vhf_high_hz=121900000, uhf_hz=250850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-151745.453125, 273037.234375, terrain), terrain)

        self.runways.append(Runway(id=1, name='35-17', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='17', heading=170, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-151833.203125, 272886.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-151863.140625, 272891.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-151891.9375, 272896, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-151920.875, 272900.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-151951.6875, 272905.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-151980.75, 272910.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-152012.578125, 272914.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))


class Abu_Rudeis(Airport):
    id = 26
    name = "Abu Rudeis"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4200000, vhf_low_hz=39300000, vhf_high_hz=118500000, uhf_hz=250900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-128441.046875, 188948.640625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield26_0'))
        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-127853.7578125, 188166.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-127872.328125, 188187.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-127891.234375, 188208.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))


class Baluza(Airport):
    id = 27
    name = "Baluza"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=39350000, vhf_high_hz=118800000, uhf_hz=250950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(104349.492188, 126474, terrain), terrain)

        self.runways.append(Runway(id=1, name='25-07', main=RunwayApproach(name='25', heading=250, beacons=[]), opposite=RunwayApproach(name='07', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(104181.5, 126797.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(104196.1953125, 126863.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(104175, 126828.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))


class Bir_Hasanah(Airport):
    id = 28
    name = "Bir Hasanah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=118850000, uhf_hz=251000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(15112.084473, 208960.679688, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(14317.133789062, 209569.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(14220.36328125, 209122.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(14241.053710938, 208871.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(14083.901367188, 208933.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(14027.005859375, 209439.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(14008.465820312, 209973.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(14008.685546875, 209992.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(14008.685546875, 210012.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(14008.534179688, 210033.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(14008.836914062, 210054.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(14008.98828125, 210076.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(14008.98828125, 210098.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(14009.21484375, 210119.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(14009.365234375, 210141.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(15578.922851562, 207384.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(15561.928710938, 207394.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(15544.831054688, 207404.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(15526.61328125, 207414.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(15509.009765625, 207425.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(15489.638671875, 207436.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(15470.84375, 207447.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(15453.141601562, 207458.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(15433.76953125, 207469.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(14733.806640625, 208181.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(14711.07421875, 207996.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(14964.50390625, 208040.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(15048.521484375, 207768.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(15270.484375, 207960.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))


class El_Arish(Airport):
    id = 29
    name = "El Arish"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4275000, vhf_low_hz=39450000, vhf_high_hz=121000000, uhf_hz=251050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(108774.84375, 247387.734375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield29_0'))
        self.runways.append(Runway(id=1, name='34R-16L', main=RunwayApproach(name='34R', heading=340, beacons=[]), opposite=RunwayApproach(name='16L', heading=160, beacons=[])))
        self.runways.append(Runway(id=1, name='34L-16R', main=RunwayApproach(name='34L', heading=340, beacons=[]), opposite=RunwayApproach(name='16R', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(109992.0078125, 247529.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(109965.9296875, 247540.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(109942.390625, 247552.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(109797.7421875, 247621.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(109771.6640625, 247632.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(109748.125, 247644.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(109895.359375, 247458.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(109849.1015625, 247478.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(109803.7109375, 247498.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(109757.375, 247518.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(113258.34375, 248012.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(113202.6171875, 248063.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(113147.625, 248115.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(113091.890625, 248168.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(113035.6171875, 248221.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(112980.4765625, 248273.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(113348.6953125, 248913.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(113318.171875, 248920, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(113272.046875, 248933.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(113224.484375, 248955.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(113164.0703125, 248979.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(113447.703125, 248952.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))


class El_Gora(Airport):
    id = 30
    name = "El Gora"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4325000, vhf_low_hz=39550000, vhf_high_hz=118200000, uhf_hz=251150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(112947.074219, 278771.265625, terrain), terrain)

        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(113295.5859375, 279168.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(113302.359375, 279192.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(113309.2265625, 279216.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(113315.96875, 279240.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(113356.9375, 279285.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(113443.7734375, 279303.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(113199.2890625, 278919.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(113224.8984375, 278869.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(113220.140625, 278850.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(113214.2109375, 278830.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(113175.4609375, 278807.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(113170.046875, 278788.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(113164.890625, 278769.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(113159.6484375, 278750.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(113154.0625, 278730.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Difarsuwar_Airfield,
    Abu_Suwayr,
    As_Salihiyah,
    Al_Ismailiyah,
    Melez,
    Fayed,
    Hatzerim,
    Nevatim,
    Ramon_Airbase,
    Ovda,
    Kibrit_Air_Base,
    Kedem,
    Wadi_al_Jandali,
    Al_Mansurah,
    AzZaqaziq,
    Bilbeis_Air_Base,
    Cairo_International_Airport,
    Cairo_West,
    Inshas_Airbase,
    Hatzor,
    Palmahim,
    Sde_Dov,
    Tel_Nof,
    Ben_Gurion,
    St_Catherine,
    Abu_Rudeis,
    Baluza,
    Bir_Hasanah,
    El_Arish,
    El_Gora,
]

