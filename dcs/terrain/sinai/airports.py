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
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=118450000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(40837.050781, 105395.976563, terrain), terrain)

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
    atc_radio = AtcRadio(hf_hz=4300000, vhf_low_hz=39500000, vhf_high_hz=118850000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(57580.1875, 82564.84375, terrain), terrain)

        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[RunwayBeacon(id='airfield2_1', runway_name='27-09', runway_id=1, runway_side='27'), RunwayBeacon(id='airfield2_0', runway_name='27-09', runway_id=1, runway_side='27')]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.runways.append(Runway(id=2, name='29-11', main=RunwayApproach(name='29', heading=290, beacons=[]), opposite=RunwayApproach(name='11', heading=110, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(58384.940515907, 81352.07683942, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(58412.687240262, 81449.716939678, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(58306.571999159, 81555.26424849, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(58335.324394108, 81661.605623096, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(57512.73053431, 83563.045414748, self._terrain), large=False, heli=False,
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
                crossroad_idx=9, position=mapping.Point(57468.599671076, 84047.749563805, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(57377.218929103, 84037.805800959, self._terrain), large=False, heli=False,
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
                crossroad_idx=15, position=mapping.Point(57199.254303768, 84154.38149532, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(57157.856508473, 84207.138647968, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=24, position=mapping.Point(56523.161504645, 84147.899864045, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(56541.289425635, 84290.102796029, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(56374.917045215, 83195.398585751, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(56207.87890625, 83126.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(56236.810596873, 83049.518775067, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(56472.453125848, 82424.419699925, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(56430.556912933, 82492.418710561, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(56251.021797942, 82378.808245771, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(56293.000169378, 82311.174603151, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(56367.578125, 82228.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(56287.5546875, 82125.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(56479.511315932, 82012.883662776, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(56497.651846985, 81924.884045672, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(56499.322784649, 81842.867548661, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(56491.484966045, 81757.217746057, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=42, position=mapping.Point(56653.66507691, 81136.859299105, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(57261.324780879, 81318.501419069, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(57399.206807001, 81353.783784007, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(57470.371370181, 81371.479445277, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(57588.7255915, 81386.038801884, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(57666.847196893, 81486.098683624, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))


class As_Salihiyah(Airport):
    id = 3
    name = "As Salihiyah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4575000, vhf_low_hz=40050000, vhf_high_hz=119350000, uhf_hz=251650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(81974.308594, 77620.761719, terrain), terrain)

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
                crossroad_idx=30, position=mapping.Point(83085.991979099, 79014.337398778, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(83187.2890625, 78947.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(83257.964143801, 79053.665004617, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(83333.9921875, 78989.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(83415.508066702, 79026.353675815, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(83568.879996228, 78564.936511649, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(83445.604183758, 78542.935769586, self._terrain), large=False, heli=False,
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
                crossroad_idx=55, position=mapping.Point(81388.104519642, 77723.17776803, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(81278.385815488, 77687.057311077, self._terrain), large=False, heli=False,
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
                crossroad_idx=69, position=mapping.Point(83622.533392685, 77750.323379406, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(83529.380632545, 77720.621899445, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(83240.937729074, 77656.904799197, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(83137.140752728, 77533.666809669, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(83040.566575628, 77527.683011679, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=12.5, height=5.5, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=4750000, vhf_low_hz=40400000, vhf_high_hz=118100000, uhf_hz=252000000)

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
    atc_radio = AtcRadio(hf_hz=4775000, vhf_low_hz=40450000, vhf_high_hz=119650000, uhf_hz=252050000)

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
    atc_radio = AtcRadio(hf_hz=4800000, vhf_low_hz=40500000, vhf_high_hz=119700000, uhf_hz=252100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(30164.332031, 98806.203125, terrain), terrain)

        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[RunwayBeacon(id='airfield6_1', runway_name='27-09', runway_id=1, runway_side='27'), RunwayBeacon(id='airfield6_0', runway_name='27-09', runway_id=1, runway_side='27')]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(30782.070584991, 99088.031708148, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(30575.935044002, 100048.9760906, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(30550.784792085, 99767.50758597, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30629.444854352, 99057.733000555, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(30563.167352911, 100148.42181198, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30547.62567232, 99639.174372469, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(30547.962171285, 99915.661131874, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(30985.19140625, 99457.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(30898.43761609, 98838.554742276, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30952.787847107, 98976.87883869, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(29974.465023988, 97849.16052112, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(30640.23046875, 97778.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(29958.392316014, 97748.670392387, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(30615.086128395, 97597.46055571, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(31045.827681101, 98810.899525037, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(29990.725077612, 97656.835852577, self._terrain), large=False, heli=False,
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
                crossroad_idx=20, position=mapping.Point(29925.117749381, 100066.33937045, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(29875.711908875, 100300.67365564, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(29879.422477943, 100155.7200417, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(29875.87258889, 99960.533659706, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(29895.023407258, 100444.75297717, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(29963.846525202, 99121.459931339, self._terrain), large=False, heli=False,
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
                crossroad_idx=29, position=mapping.Point(29756.080626353, 99580.309535662, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(29867.11205989, 99101.268424795, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(29886.676392758, 99567.328604087, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(29987.82147065, 99567.817066897, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(29765.341073155, 99157.450852092, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(30889.55078125, 99457.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(29977.376180215, 97573.692980562, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(29959.117989259, 97425.765472284, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(31093.133800851, 99092.698595938, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))


class Hatzerim(Airport):
    id = 7
    name = "Hatzerim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4825000, vhf_low_hz=40550000, vhf_high_hz=119750000, uhf_hz=252150000)

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
                crossroad_idx=9, position=mapping.Point(131454.40625, 328287.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(131419, 328281.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(130687.046875, 328877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='139', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(132073.953125, 328384.875, self._terrain), large=False, heli=False,
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
                crossroad_idx=16, position=mapping.Point(131281.96875, 328624.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='120', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(130640.796875, 328859.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='141', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(132632.46875, 326385.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(132616.671875, 326381.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(132600.921875, 326377.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(132585.1875, 326373.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(132569.40625, 326369.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(132537.859375, 326361.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(132522.109375, 326357.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(132506.3125, 326353.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(132474.796875, 326345.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(132459.046875, 326341.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(132443.28125, 326336.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(132427.5, 326332.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(132411.734375, 326328.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(132380.21875, 326320.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(132470.984375, 326498.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(132518.140625, 326511.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(132549.703125, 326519.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(132581.203125, 326527.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(132502.390625, 326507.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(132565.453125, 326523.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(132596.96875, 326531.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(132392.03125, 326478.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(132407.796875, 326482.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(132486.765625, 326502.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(132423.59375, 326486.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(132376.28125, 326474.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(132455.078125, 326494.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(132344.75, 326466.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(132431.90625, 326693.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(132479.21875, 326705.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(132463.421875, 326701.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(132353.078125, 326672.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(132368.828125, 326676.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(132447.65625, 326697.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(132384.578125, 326680.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(132337.3125, 326668.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(132416.15625, 326688.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(132305.765625, 326660.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(132410.984375, 326836.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(132426.8125, 326840.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(132332.1875, 326816.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(132316.421875, 326812.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(132395.203125, 326832.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(132347.953125, 326820.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(132363.75, 326824.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(132284.890625, 326804.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(132443.0625, 326843.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(132269.109375, 326800.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(132370.234375, 326984.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(132386, 326988.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(132291.375, 326964.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(132275.578125, 326960.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(132354.453125, 326980.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(132322.921875, 326972.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(132338.671875, 326976.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(132244.109375, 326952.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(132401.75, 326992.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(132228.3125, 326948.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(132357.734375, 327474.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(132318.96875, 327464.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(132260.8125, 327450.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(132338.34375, 327469.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(132299.578125, 327459.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(132280.203125, 327455, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(132222.046875, 327440.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(132202.671875, 327435.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(132125.140625, 327415.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(132105.75, 327410.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(132183.28125, 327430.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(132241.4375, 327445.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(132163.90625, 327425.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(132144.515625, 327420.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(132289.78125, 327576.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(132226.640625, 327560.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(132305.515625, 327580.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(132273.9375, 327572.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(132258.171875, 327568.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(132095.828125, 327526.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(132115.21875, 327531, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(132192.75, 327550.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(132173.359375, 327545.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(132153.984375, 327540.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(132210.90625, 327556.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(132076.453125, 327521.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(132134.59375, 327535.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(132321.21875, 327584.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(132062.265625, 327851, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(132015.109375, 327838.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(132046.5, 327846.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(131999.28125, 327834.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(131983.6875, 328032.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(132015.28125, 328040.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='103', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(131952.21875, 328024.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(131967.96875, 328028.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(132078.078125, 328369.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(132082.09375, 328353.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(132086.171875, 328337.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(132090.203125, 328321.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='106', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(132094.25, 328306.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='105', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(132098.578125, 328290.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='104', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(131273.4375, 328610.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='121', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(131264.96875, 328596.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='122', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(131256.4375, 328582.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='123', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(131239.4375, 328554.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='124', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(131230.9375, 328540.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='125', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(130857.765625, 328890.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='132', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(130832.796875, 328848.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='134', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(130799.484375, 328792.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='137', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(130807.796875, 328806.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='136', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(130841.125, 328862.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='133', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(130824.453125, 328834.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='135', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(131686.671875, 328383.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(131123.921875, 328847.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='127', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(131132.265625, 328861.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='128', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(131115.28125, 328833.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='126', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(131140.828125, 328875.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='129', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(131157.875, 328902.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='130', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(131166.328125, 328916.84375, self._terrain), large=False, heli=False,
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
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(130615.625, 329236.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='159', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(130632.9765625, 329225.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='158', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(130668.2265625, 329205.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='157', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(130685.5546875, 329195.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='156', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(130569.3828125, 329314.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='160', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(131289.6875, 326372.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(131280.390625, 326409.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(131270.765625, 326447.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(131261.21875, 326484.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(131251.609375, 326521.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(132290.21875, 328388.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='161', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(132273.09375, 328399, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='162', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(132229.796875, 328572.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='168', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(132239.796875, 328590.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='169', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(132219.6875, 328547.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='167', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(132204.59375, 328520.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='166', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(132252.21875, 328414.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='163', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(132226.078125, 328431.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='165', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(130579.8046875, 328962.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='155', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(130602.0859375, 328957.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='154', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(130624.7109375, 328951.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='153', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(130646.703125, 328945.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='152', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(130669.8046875, 328939.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='151', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(130692.0625, 328933.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='150', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(130716.15625, 328929.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='149', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(130738.6015625, 328924.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='148', length=21.0, width=15.0, height=8.0, shelter=False))


class Nevatim(Airport):
    id = 8
    name = "Nevatim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4850000, vhf_low_hz=40600000, vhf_high_hz=132400000, uhf_hz=252200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(127170.644531, 361898.1875, terrain), terrain)

        self.runways.append(Runway(id=2, name='08R-26L', main=RunwayApproach(name='08R', heading=80, beacons=[]), opposite=RunwayApproach(name='26L', heading=260, beacons=[])))
        self.runways.append(Runway(id=1, name='08L-26R', main=RunwayApproach(name='08L', heading=80, beacons=[]), opposite=RunwayApproach(name='26R', heading=260, beacons=[RunwayBeacon(id='airfield8_0', runway_name='08L-26R', runway_id=1, runway_side='26R')])))
        self.runways.append(Runway(id=3, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield8_1', runway_name='07-25', runway_id=3, runway_side='25'), RunwayBeacon(id='airfield8_2', runway_name='07-25', runway_id=3, runway_side='25')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(129557.765625, 361811.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(129219.9296875, 362534.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(128442.2109375, 359331.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(128346.125, 363731.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(128717.2265625, 360282.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(129540.4765625, 361823.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(128669.53125, 360198.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(128479.296875, 361779.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(128471.5625, 361753.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(126834.375, 363879.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(129138.5546875, 362259.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(129265.0859375, 362550.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(129447.609375, 361887, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(128537.265625, 363519.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(127159.546875, 363720.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(126994.578125, 363046.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(128468.33942502, 363636.39937917, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(128484.640625, 361806.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(129398.1953125, 362801.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='114', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(129202.46875, 362466.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='110', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(128613.5625, 362078.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(128557.3828125, 359578.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(126922, 362774.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(128322.5390625, 363636.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(128551.6484375, 363576.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(128819.921875, 359236.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(128569.734375, 361731.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='124', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(128491.6484375, 361832.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(129379.9140625, 362848.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='113', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(126981.3515625, 362993.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(128533.2890625, 359308.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(129162.640625, 361705.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(126923.65625, 363853.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(128405.05064167, 363652.98315418, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(129135.71875, 361723.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(128790.5078125, 359247.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(128582.7578125, 361783.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(128576.28125, 361757.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(128732.921875, 360180.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(127020.7578125, 363154.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(128407.734375, 359177.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(129630.015625, 361760.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(127115.6015625, 363550.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(129520.703125, 361837.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(128923.46875, 359210.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(128590.34375, 361810.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(127007.90625, 363101.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(128508.9609375, 359312.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(126879.921875, 362611.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(127129.8828125, 363605.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(127013.8125, 363832.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(129593.921875, 361785.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(128855.125, 359228.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(129417.125, 362756.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='115', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(128557.9609375, 363605.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(128679.3046875, 360146.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(129098.3515625, 361748.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(129125.4765625, 362206.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(129247.4375, 362482.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='111', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(127033.6875, 363207.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(127174.8984375, 363780.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(128491.171875, 363731.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(128956.2734375, 359201.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(129483.875, 361863.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(129133.2109375, 362232.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(126476.5, 363031.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(126850.265625, 362500.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(128528.15625, 359637.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(129503.2890625, 361849.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(128510.3046875, 359950.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(128557.4609375, 359955.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(128338.8828125, 363699.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(126878.9921875, 363866.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(129190.15625, 361687.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(129172.9609375, 362519.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(126463.1015625, 362973.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(129612.484375, 361772.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(128662.3046875, 360245.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(127046.875, 363260.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(128459.4453125, 363738.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(127060.7265625, 363315.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(128522.6953125, 363723.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(126967.46875, 362937.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(128556.25, 359301.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(128532.2109375, 360009.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(128419.59375, 359339.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(128463.390625, 359563.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(128628.796875, 360023.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(129244.2578125, 362263.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(126936.59375, 362830.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(128366.5, 359153.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(129466.53125, 361874.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(126894.28125, 362665.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(128488.609375, 359503.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(129030.484375, 361793.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(128504.8203125, 359167.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(129145.5625, 362285.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(129016.8828125, 361803.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(128465.7578125, 359325.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(128520.4375, 359538.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(128576.59375, 360018, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(129223.6484375, 362184.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(128486.8515625, 359319.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(128667.375, 362041.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(128436.703125, 363645.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(128887.640625, 359219.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(129230.1953125, 362210.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(126420.625, 362841.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(126433.1953125, 362891.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(128459.375, 359141.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(128543.8671875, 363548.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(127144.25, 363666.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(128724.4296875, 360234.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(129236.671875, 362237, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(128612.203125, 359961.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(126864.9296875, 362556.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(127170.3984375, 364006.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(128640.2578125, 362060.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(128330.484375, 363668.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(129295.328125, 362497.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='112', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(128694.640625, 362023.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(128454.59375, 359205.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(126967.8203125, 363844, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(129576.5078125, 361797.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(127086.78125, 363432.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(128500.25, 363629.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(128418.609375, 359117.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(126907.5390625, 362720.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(128494.59375, 359599.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(127101.296875, 363487.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(128427.5859375, 363746.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(129044.3203125, 361785.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))


class Ramon_Airbase(Airport):
    id = 9
    name = "Ramon Airbase"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4875000, vhf_low_hz=40650000, vhf_high_hz=119800000, uhf_hz=252250000)

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
                crossroad_idx=53, position=mapping.Point(79587.715611107, 327247.34537155, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(79548.578125, 327219.37894967, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(79508.689846148, 327191.19751641, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(79669.638640059, 327230.61469351, self._terrain), large=False, heli=False,
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
                crossroad_idx=68, position=mapping.Point(79532.802698871, 328025.67669192, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(79562.04511483, 328063.55123491, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(79622.4140625, 328036.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(79503.627540489, 328268.96607058, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(79527.301353935, 328329.19243708, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(79486.976066353, 328356.35286734, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(79445.828401588, 328386.00292306, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(79277.999541852, 327680.13515865, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(79161.482965822, 327798.87232058, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(79206.812326333, 327778.12105033, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(79251.709354655, 327757.55199071, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(80167.123943898, 329572.48620292, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(80200.445295133, 329607.69850349, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(80234.91090624, 329642.71247221, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(80316.921875, 329639.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(80224.41716666, 329862.29056248, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(80199.171205026, 329944.40558003, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(80244.564558292, 329921.69060416, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(80287.916620355, 329903.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(80490.842410289, 330188.10793109, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(80522.717163187, 330224.74054859, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(80554.447922456, 330261.27596062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(80605.7265625, 330224.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(80461.4375, 330497.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(80461.837765005, 330580.38630002, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(80498.930058815, 330549.10983315, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(80535.703478011, 330516.22248814, self._terrain), large=False, heli=False,
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
                crossroad_idx=110, position=mapping.Point(81035.684378473, 330571.08592013, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(80497.9296875, 330465.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(80534.8359375, 330432.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(80637.223228935, 330261.34995898, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(80573.2421875, 330188.33178001, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(80268.407784713, 329842.46712845, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(80313.107805553, 329821.95464235, self._terrain), large=False, heli=False,
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
                crossroad_idx=124, position=mapping.Point(79188.634100111, 327719.45873359, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(79333.704870759, 327462.7137418, self._terrain), large=False, heli=False,
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
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(79797.54030578, 328824.77904476, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(79816.232737762, 328816.48538504, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(79836.389220683, 328807.4348257, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(79856.952817645, 328798.54614041, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(79879.671490587, 328788.22925702, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(79919.55321186, 328772.3493685, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(79935.167022402, 328765.47431479, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(79951.009803766, 328758.57066579, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(79967.553045633, 328751.36830599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand09', length=21.0, width=15.0, height=8.0, shelter=False))


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
                crossroad_idx=10, position=mapping.Point(-13443.318359375, 355696.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-13494.997070312, 355768.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-13448.2578125, 355766.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-13399.369140625, 355761, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-13466.990234375, 356110.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-13419.837890625, 356118, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-13371.00390625, 356123.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-13261.71484375, 356286.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-13235.107421875, 356456.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-13222.94140625, 356410.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-13211.475585938, 356363.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-12877.584960938, 356340.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-12873.05078125, 356404.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-12826.515625, 356397.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-12778.5234375, 356386.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-12424.8515625, 356468.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-12390.90234375, 356502.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-12356.327148438, 356535.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-12447.771484375, 356537.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-11862.40234375, 356622.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-11873.599609375, 356649.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-11883.848632812, 356676.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-11894.767578125, 356704.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-11925.56640625, 356783.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-11895.16015625, 356795.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-11860.782226562, 356808.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-11833.40625, 356819.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-11806.34765625, 356829.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-11778.922851562, 356840.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-11818.291992188, 356711.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-11791.323242188, 356721.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-11763.821289062, 356731.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-11736.40234375, 356742.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-11214.426757812, 356934.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-11218.883789062, 356996.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-11171.200195312, 356996.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-11122.82421875, 356994.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-10816.41796875, 356631.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-10829.5390625, 356657.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-10841.040039062, 356687.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-10851.951171875, 356718.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-10863.3671875, 356748.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-10874.952148438, 356777.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-10845.02734375, 357213, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-10807.18359375, 357151.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-10782.8984375, 357191.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-10758.264648438, 357233.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-10543.947265625, 357344.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-10492.725585938, 357383.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-10468.040039062, 357343.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-10443.8984375, 357301.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-10304.133789062, 357283.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-10140.760742188, 357321.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-10179.247070312, 357293.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-10218.346679688, 357265.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-10039.358398438, 357022.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-10006.081054688, 357058.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-9973.3330078125, 357094.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-9922.033203125, 357058.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-9954.09765625, 357022.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-9986.7216796875, 356986.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-10240.881835938, 356845.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-10259.946289062, 356887.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-10277.198242188, 356932.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-10295.98046875, 356974.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-10309.79296875, 356439.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-10321.577148438, 356467.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-10332.900390625, 356497.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-10344.4765625, 356526.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-10355.96875, 356556.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-10366.762695312, 356587.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-10305.711914062, 356088.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-10376.810546875, 356022.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-10337.262695312, 355967.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-10271.11328125, 355981.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-10263.731445312, 357311.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-10224.3125, 357339.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-10519.561523438, 357302.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-10494.326171875, 357259.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-10871.38671875, 357171.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-10896.467773438, 357129.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-11166.80078125, 356934.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-11117.146484375, 356932.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-12482.659179688, 356503.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-12517.62109375, 356469.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-12830.38671875, 356332.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-12782.1328125, 356324, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-13273.1796875, 356334.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-13284.280273438, 356382.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-13352.866210938, 356057.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-13394.202148438, 355691.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-13345.431640625, 355686.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-13400.881835938, 356050.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-13450.778320312, 356044.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))


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
                crossroad_idx=4, position=mapping.Point(21507.287064173, 119066.46583599, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(21450.9214492, 119172.49812531, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(21348.034433528, 119131.23745359, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(21313.893690008, 119268.10089092, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(20840.1966832, 119746.60400414, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(20725.714618864, 119810.95546245, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(19572.236529927, 120901.67963458, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(19474.936223089, 120917.754811, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(19507.782532735, 121015.25036258, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(19383.326024191, 121016.04707304, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(19398.131870609, 121118.38371873, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(20036.189298405, 121379.20835614, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(20015.544768362, 121477.63866102, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(19920.71579129, 121445.77637103, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(19907.946404046, 121541.28647345, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(19812.76895884, 121536.16695012, self._terrain), large=False, heli=False,
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
        super().__init__(mapping.Point(134332.039063, 325363.625, terrain), terrain)

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

        self.runways.append(Runway(id=1, name='01R-19L', main=RunwayApproach(name='01R', heading=10, beacons=[]), opposite=RunwayApproach(name='19L', heading=190, beacons=[])))
        self.runways.append(Runway(id=2, name='01L-19R', main=RunwayApproach(name='01L', heading=10, beacons=[RunwayBeacon(id='airfield13_1', runway_name='01L-19R', runway_id=2, runway_side='01L'), RunwayBeacon(id='airfield13_0', runway_name='01L-19R', runway_id=2, runway_side='01L')]), opposite=RunwayApproach(name='19R', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-2021.1150231321, 56508.436476241, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-2145.3559570312, 56472.83203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-2311.8850464133, 56993.038365579, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-2170.3251085004, 57039.25008559, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-2096.6587636882, 57101.506773795, self._terrain), large=False, heli=False,
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
                crossroad_idx=38, position=mapping.Point(499.62514429923, 58265.604181108, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(630.4141225294, 58289.937426093, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(624.97958886748, 58045.616308424, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(697.30502330511, 58139.365277225, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(823.77111816406, 58231.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-1844.7791687867, 56561.159251028, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-1763.1457212243, 56588.014143922, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-1696.2959630401, 56634.451012107, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-1613.4058807728, 56661.766273913, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-1568.1045500883, 56665.811389447, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-2080.0724161562, 57289.361282649, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-2102.3047165653, 57376.825353601, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-1975.7395072754, 57413.379706407, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-1811.2416903195, 57411.494891236, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-737.7733057098, 57630.124030799, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-924.197795942, 57566.526436983, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=57, position=mapping.Point(876.25159608466, 57286.108035374, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(961.03619186018, 57359.224391097, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(1125.6517150139, 57339.820301008, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(1206.7453568978, 57366.341230047, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(1254.9566928774, 57426.223003842, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(1324.3480568989, 57461.42355727, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(1221.2189871338, 57912.44170599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(1274.3841786777, 58060.53325268, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(1140.6815405859, 58347.589445629, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(905.0303788763, 58320.215273441, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=12.5, height=5.5, shelter=False))
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

        self.runways.append(Runway(id=2, name='35-17', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='17', heading=170, beacons=[])))
        self.runways.append(Runway(id=1, name='32-14', main=RunwayApproach(name='32', heading=320, beacons=[]), opposite=RunwayApproach(name='14', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(100267.15420466, 20077.255584189, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(100190.87863376, 20101.334628181, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(100187.81251737, 20167.209597789, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(100224.03367878, 19961.419785787, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(100331.81160759, 19910.026441558, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(100377.16892273, 20551.13974188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(100458.01778749, 20491.406863177, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(100630.31291114, 20417.816967697, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(100759.32352086, 20494.291608348, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(100865.82500347, 20432.476265655, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(100983.65233507, 20441.729224556, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(100667.0546875, 19855.517578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(100655.39053817, 19804.829991291, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(100714.140625, 19689.572265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(100708.359375, 19736.865234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(100881.96509499, 19438.69518688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(100893.27654166, 19330.117710434, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(101017.59136719, 19437.697203466, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(101187.9727865, 19243.663235107, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(101255.2256462, 19232.897617756, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(101348.68672594, 19152.339308487, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(101373.01682054, 19098.150969305, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(101491.91694652, 18995.081892768, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(101800.81192359, 18778.270611495, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(101874.77631815, 18661.373617648, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(101999.6300082, 18565.263149939, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(102067.84626102, 18547.262602385, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(102591.63983523, 18172.136037523, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(102627.640625, 18702.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=39, position=mapping.Point(103186.62583747, 19178.379659971, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(103311.90192502, 19196.071463535, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(103411.140625, 19720.79296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(103313.63148748, 19717.010113604, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(103239.95412996, 19839.959597552, self._terrain), large=False, heli=False,
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

        self.runways.append(Runway(id=2, name='36R-18L', main=RunwayApproach(name='36R', heading=360, beacons=[]), opposite=RunwayApproach(name='18L', heading=180, beacons=[])))
        self.runways.append(Runway(id=1, name='36L-18R', main=RunwayApproach(name='36L', heading=360, beacons=[]), opposite=RunwayApproach(name='18R', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(61826.114800753, 41083.843864541, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(61715.00973998, 41070.583630209, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(61604.445800781, 40997.91897583, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(61518.881085472, 41074.950724806, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(60918.097900391, 41579.110443115, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(61024.177734174, 41624.404361693, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(61141.740112305, 41468.940437317, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(60819.323682705, 41660.864416139, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(60712.324077134, 41486.26659923, self._terrain), large=False, heli=False,
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
                crossroad_idx=17, position=mapping.Point(60033.87173702, 41476.124492726, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(59849.133443983, 41518.141403915, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(58955.041285819, 40956.688303437, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(58774.828745738, 41041.478002677, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(58645.912056764, 41036.448433473, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(58800.776034732, 40932.931284208, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(58738.125065731, 40858.902338043, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(58628.547546387, 40859.839161977, self._terrain), large=False, heli=False,
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

        self.runways.append(Runway(id=3, name='27L-09R', main=RunwayApproach(name='27L', heading=270, beacons=[]), opposite=RunwayApproach(name='09R', heading=90, beacons=[])))
        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.runways.append(Runway(id=2, name='35R-17L', main=RunwayApproach(name='35R', heading=350, beacons=[RunwayBeacon(id='airfield16_1', runway_name='35R-17L', runway_id=2, runway_side='35R'), RunwayBeacon(id='airfield16_0', runway_name='35R-17L', runway_id=2, runway_side='35R')]), opposite=RunwayApproach(name='17L', heading=170, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(40208.126204883, 35040.568836613, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(40253.978184047, 35095.044486096, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(40293.463482704, 35139.96003121, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(39714.725075172, 35744.880532512, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(39595.79296875, 35761.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(39541.049839582, 35843.815916761, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(39427.444071222, 35905.050012605, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(39273.419312429, 35831.448066105, self._terrain), large=False, heli=False,
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
                crossroad_idx=23, position=mapping.Point(39954.19996874, 35696.036621496, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(39988.96013541, 35731.417724972, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(40026.876702342, 35771.482127676, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(40068.091828691, 35809.278437847, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(40097.917522592, 35352.655359893, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(40146.373254241, 35398.680058815, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(40186.622442374, 35451.167777855, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(36639.161445897, 35714.493931258, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(36687.622243819, 35587.08503121, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(36735.428360543, 35536.59995832, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(36786.883787613, 35507.128766672, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(36834.857352086, 35471.971470804, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(36886.09885179, 35439.43751199, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(36921.05263369, 35400.746040226, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(36969.29227086, 35358.99058332, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(37026.05934642, 35319.832602316, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(37079.604198506, 35294.764137672, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(37124.17578125, 35247.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(37148.853407083, 33896.455924058, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(37094.193721708, 33772.568382952, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(37131.408065113, 33666.524309057, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(37159.476639876, 33539.479793518, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(37104.570414127, 33173.481138943, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(37148.264479629, 33117.893800611, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(37045.139034208, 33062.902946191, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(37139.890581583, 33014.534512444, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(37779.679041711, 33213.737340226, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(37827.252670739, 33253.395697294, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(37868.147809077, 33294.962454846, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=38, position=mapping.Point(6706.8056195091, 14882.826772696, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(6641.6169433547, 14896.838558163, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(6572.6733536734, 14917.986873395, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(6505.5032511801, 14930.146979883, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(6627.9034044031, 14567.74334927, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(6558.3151159593, 14584.741686874, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(6492.7374605433, 14600.010718155, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(6421.5291249262, 14614.608060425, self._terrain), large=False, heli=True,
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
                crossroad_idx=59, position=mapping.Point(6545.8380639594, 14762.249710931, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(6614.7701058852, 14745.353646398, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(6680.7443300208, 14728.426573334, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(6626.8806204908, 15073.037841352, self._terrain), large=False, heli=True,
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
                crossroad_idx=69, position=mapping.Point(7043.6507336965, 15215.559231599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(7012.4613628962, 15289.681377941, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(6989.6734347536, 15359.78897922, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(6929.4163290639, 15462.716081768, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(6829.0264145645, 15526.09343115, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(6852.8934339879, 15151.67478157, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(6831.5389588541, 15220.091858959, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(6809.5185359665, 15284.389709388, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(6773.2943388646, 15411.716624744, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=131200000, uhf_hz=250450000)

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
                crossroad_idx=39, position=mapping.Point(7217.0024051587, -31016.518772089, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(7042.5873674493, -30869.015311433, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(7044.5240041903, -31007.403872425, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(6893.65234375, -30899.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(6897.0670472473, -31044.343062778, self._terrain), large=False, heli=True,
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
                crossroad_idx=50, position=mapping.Point(7381.234375, -28822.669921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(7421.5688476562, -28868.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(7446.185546875, -28930.982421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(7473.0014648438, -29018.90234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(7510.2241210938, -29073.80078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(7515.6518554688, -29138.88671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(7546.0590820312, -29236.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(7741.7438263331, -29550.451869765, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(7771.3675994232, -29611.196158433, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(7812.0083007812, -29712.115234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(7830.4033203125, -29764.736328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(7854.8769704917, -29810.271440958, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(7886.2622070312, -29889.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(7922.5869140625, -29977.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(7950.1254882812, -30040.517578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(8010.9111328125, -30066.01953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(8087.9409179688, -30139.310546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=70, position=mapping.Point(9274.4847368375, -32212.375595641, self._terrain), large=False, heli=False,
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
                crossroad_idx=74, position=mapping.Point(9695.564332593, -32212.746617023, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(9804.19921875, -32233.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(9971.2734375, -32431.341796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(10039.5546875, -31910.267578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(9933.5908203125, -31873.470703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(9851.7713215619, -31785.470747299, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(9782.3761747273, -31743.643217589, self._terrain), large=False, heli=False,
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
                crossroad_idx=84, position=mapping.Point(10439.723801621, -31636.187205801, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(10561.519798503, -31463.120215633, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(10669.498098975, -31349.332679397, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(10639.568024388, -31162.649023727, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(10342.020768518, -31336.813224665, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=95, position=mapping.Point(9798.4950183639, -30455.717124773, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(9869.8109995372, -30172.52964582, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(10316.733360258, -30101.542848218, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(9886.0080415741, -29742.487288595, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(8767.304731674, -30246.965294431, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(8518.5661455441, -30363.247786169, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.0, width=12.5, height=5.5, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118400000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(31044.584961, 20003.525391, terrain), terrain)

        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[RunwayBeacon(id='airfield19_1', runway_name='04-22', runway_id=1, runway_side='22'), RunwayBeacon(id='airfield19_0', runway_name='04-22', runway_id=1, runway_side='22')])))
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
                crossroad_idx=21, position=mapping.Point(31232.16320831, 18726.969168412, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(31260.220703125, 18635.82421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(30908.23046875, 18556.033203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(30783.546989537, 18604.311730425, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(30704.248876338, 18605.77242238, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(30654.041659431, 18693.655070931, self._terrain), large=False, heli=False,
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
                crossroad_idx=31, position=mapping.Point(29973.490234375, 19912.763671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(29911.150390625, 19938.90234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(30072.76953125, 20521.490234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(30141.482421875, 20501.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(30215.814453125, 20491.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(30272.746638739, 20476.519463499, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(30300.921875, 20524.134765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(30357.767240509, 20589.006508418, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(30373.016532246, 20660.191538282, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(30350.421875, 20731.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(30714.147719886, 20910.727850111, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(30778.8777227, 20982.441329892, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
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
                crossroad_idx=47, position=mapping.Point(31616.266793402, 20846.844517357, self._terrain), large=False, heli=False,
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
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=118550000, uhf_hz=250600000)

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


class Palmachim(Airport):
    id = 21
    name = "Palmachim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=118600000, uhf_hz=250650000)

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
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=118650000, uhf_hz=250700000)

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
                crossroad_idx=43, position=mapping.Point(228277.880077, 337689.63896341, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))


class Tel_Nof(Airport):
    id = 23
    name = "Tel Nof"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4125000, vhf_low_hz=39150000, vhf_high_hz=118700000, uhf_hz=250750000)

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
                crossroad_idx=8, position=mapping.Point(199205.3260128, 340963.24763327, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(199179.09375, 340992.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(199074.98035421, 340938.14199944, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(199035.90625, 340937.78817166, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(198997.23680798, 340870.30643326, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(198969.58843149, 340897.9822628, self._terrain), large=False, heli=False,
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
                crossroad_idx=49, position=mapping.Point(198757.55622221, 340303.67487496, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(198744.58851016, 340340.61500539, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(198665.41256252, 340249.46407511, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(198678.60870503, 340212.68483503, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(198613.35398265, 340126.45607784, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(198605.97478465, 340164.22057995, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(198495.22274, 340201.21542998, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(198482.13919578, 340237.93394173, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(197912.515625, 340051.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(197913.140625, 340100.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(197913.95658583, 340148.70236142, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(197707.65996535, 340465.89375531, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(197756.62204823, 340471.00025526, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(197806.16826219, 340475.03211613, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(197573.17744803, 340686.16317166, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(197609.26319202, 340719.31264224, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(197648.18996157, 340752.01545828, self._terrain), large=False, heli=False,
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
                crossroad_idx=12, position=mapping.Point(217193.0057339, 345943.64675584, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(217275.453125, 345921.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(217353.79014764, 345926.97854691, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(217374.984375, 345998.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(217371.8279173, 346068.44590864, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(217373.734375, 346211.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(217383.54073184, 346289.75147444, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(217333.74669499, 346343.55240452, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(217218.04599194, 346321.46321332, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(217135.65625, 346450.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(217156.15106878, 346387.1407134, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(216995.05721715, 346357.38692906, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(216787.92241273, 346325.7756093, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(216850.90625, 346173.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(216750.35114212, 346258.98552524, self._terrain), large=False, heli=True,
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
                crossroad_idx=76, position=mapping.Point(217418.82971181, 348306.70781597, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=39350000, vhf_high_hz=118750000, uhf_hz=250950000)

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
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=118800000, uhf_hz=251000000)

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


class Al_Khatatbah(Airport):
    id = 31
    name = "Al Khatatbah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4350000, vhf_low_hz=39600000, vhf_high_hz=118950000, uhf_hz=251200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(30000.823242, -35160.732422, terrain), terrain)

        self.runways.append(Runway(id=2, name='20R-02L', main=RunwayApproach(name='20R', heading=200, beacons=[]), opposite=RunwayApproach(name='02L', heading=20, beacons=[])))
        self.runways.append(Runway(id=3, name='20L-02R', main=RunwayApproach(name='20L', heading=200, beacons=[]), opposite=RunwayApproach(name='02R', heading=20, beacons=[])))
        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(30659.828125, -35938.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30779.666015625, -35874.87890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(30848.79296875, -35746.75390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30800.35546875, -35633.7578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(30718.341796875, -35791.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(30659.73828125, -35650.765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(30675.1015625, -35528.90234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30542.34765625, -35577.24609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(30599.205078125, -35425.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(30506.068359375, -35479.33984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(30478.361328125, -35377.8359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(30536.302734375, -35723.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(30552.865234375, -35304.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(30417.125, -35259.10546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(30347.01953125, -35383.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(30396.275390625, -35700.52734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(30375.828125, -35559.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(30308.033203125, -35463.3203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H40', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(30252.03515625, -35289.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(30296.9296875, -35211.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(30212.951171875, -35111.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(30177.591796875, -35060.3515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(30118.439453125, -34971.58984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(30116.65625, -34844.48828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(30218.236328125, -34784.50390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(29966.626953125, -34859.42578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(30014.900390625, -35672.4296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(29928.66015625, -35514.12109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H32', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(29850.759765625, -35608.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H29', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(29735.8828125, -35506.58203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H30', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(29827.51953125, -35442.73828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H31', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(29721.193359375, -35440.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H33', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(29757.708984375, -35398.66796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H34', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(29711.462890625, -35184.9140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H35', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(29572.46484375, -35212.6484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(29578.669921875, -35094.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(29492.154296875, -35155.74609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(29470.671875, -35026.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(30292.865234375, -35096.62890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(30416.228515625, -35063.79296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=20.0, width=17.0, height=8.0, shelter=False))


class Al_Rahmaniyah_Air_Base(Airport):
    id = 32
    name = "Al Rahmaniyah Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4375000, vhf_low_hz=39650000, vhf_high_hz=119050000, uhf_hz=251250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(111444.902344, -53678.824219, terrain), terrain)

        self.runways.append(Runway(id=1, name='34-16', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='16', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(111917.38785611, -54062.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(110002.2578125, -53291.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(112866.6328125, -54292.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(112062.390625, -54017.04296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(112805.4609375, -54310.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(109939.6328125, -53241.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(111972.16372374, -54141.892635578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(112442.90134144, -53813.282177239, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(112732.734375, -54250.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(110078.875, -53301.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(110159.1171875, -53326.93359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(111895.6628098, -54105.649898477, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(110067.921875, -53002.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(113004.9609375, -54080.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(111939.4453125, -53960.01953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand02', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(111431.8125, -53767.9921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(112898.5703125, -53992.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(110292.875, -53071.88671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(112992.0078125, -54012.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(112355.18636287, -53764.062033061, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(111993.10940518, -54098.944307173, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(111576.62682151, -53827.582982333, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))


class Beni_Suef(Airport):
    id = 33
    name = "Beni Suef"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4400000, vhf_low_hz=39700000, vhf_high_hz=127100000, uhf_hz=251300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-93775.957031, -23378.751953, terrain), terrain)

        self.runways.append(Runway(id=2, name='36L-18R', main=RunwayApproach(name='36L', heading=360, beacons=[]), opposite=RunwayApproach(name='18R', heading=180, beacons=[])))
        self.runways.append(Runway(id=3, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.runways.append(Runway(id=1, name='36R-18L', main=RunwayApproach(name='36R', heading=360, beacons=[RunwayBeacon(id='airfield33_1', runway_name='36R-18L', runway_id=1, runway_side='36R'), RunwayBeacon(id='airfield33_0', runway_name='36R-18L', runway_id=1, runway_side='36R')]), opposite=RunwayApproach(name='18L', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-95732.9375, -24234.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-95504.21875, -24203.20703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-95068.334517048, -24137.387158585, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-94652.833010917, -24063.835979718, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-94522.049848112, -24040.274105687, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-91627.921875, -22638.470703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-91427.078125, -22722.451171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-91238.8359375, -22691.40234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-95539.625, -24494.498046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-95370.40625, -24216.642578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-95308.782355457, -24094.141830953, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-95149.55603319, -24013.869130022, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-94999.714651959, -24078.52169631, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-94805.892392918, -23971.438733403, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-95669.429888492, -23401.258164236, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-95429.3828125, -23384.656281459, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-95232.030746469, -23379.166327846, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-93379.571254168, -24048.299316648, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-93163.852969446, -23923.737282838, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-93107.641629961, -23841.502581226, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-93141.967927456, -23741.131194362, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-93013.903076373, -23739.034651005, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-92546.041321814, -23663.122796092, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-92373.21308258, -23676.027905242, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-92343.9863143, -23556.796385603, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-92232.397001242, -23598.679472223, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-92155.767196064, -23508.793099161, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-92378.113695475, -22752.208952916, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-92239.814446576, -22788.089341269, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-92069.773158344, -22660.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-91979.215420073, -22783.282435768, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-91843.84214582, -22751.070696178, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-95520.33959251, -23486.349148768, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-92955.512572967, -24256.609726736, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-92811.2890625, -24262.619140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-93511.277691729, -24030.505893786, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-92931.578125, -24293.541015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-95341.1171875, -23342.216796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-95572.015625, -23357.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-92659.578125, -23787.869140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-93949.4609375, -23937.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-93924.3984375, -23933.736328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-93898.96875, -23928.873046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-93874.3359375, -23925.052734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-93850.1328125, -23920.259765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-93826.296875, -23917.408203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-93800.9375, -23912.251953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-93776.796875, -23908.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-93752.5859375, -23903.759765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-93727.78125, -23899.564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-93703.484375, -23895.275390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-93678.953125, -23891.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-93654.8984375, -23886.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-93630.3828125, -23882.130859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-93605.359375, -23878.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-93581.140625, -23874.294921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-93556.3203125, -23870.654296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-93532.0546875, -23866.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-93507.2890625, -23862.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-92738.2421875, -23809.634765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-92303.8828125, -24828.607421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-92314.6328125, -24845.544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-92325.4921875, -24862.275390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-92336.5546875, -24879.259765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-92348.8359375, -24896.927734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-95092.171875, -24477.193359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-95118.53125, -24457.26171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-92650.6171875, -22868.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))


class Birma_Air_Base(Airport):
    id = 34
    name = "Birma Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4425000, vhf_low_hz=39750000, vhf_high_hz=119150000, uhf_hz=251350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(88051.835938, -28172.807617, terrain), terrain)

        self.runways.append(Runway(id=2, name='32L-14R', main=RunwayApproach(name='32L', heading=320, beacons=[]), opposite=RunwayApproach(name='14R', heading=140, beacons=[])))
        self.runways.append(Runway(id=1, name='32R-14L', main=RunwayApproach(name='32R', heading=320, beacons=[]), opposite=RunwayApproach(name='14L', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(88772.013421092, -29412.904089509, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(88769.097718705, -29348.992577136, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(88765.368129168, -29293.981967764, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(88763.620775591, -29227.83027108, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(88757.718018922, -29155.478945482, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(88862.767141685, -29251.893057982, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(88987.948128772, -29275.679051183, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(88961.020027577, -29149.637558688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(88817.909127233, -29033.160105399, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(89100.019345593, -29425.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(89098.685612, -29357.527758481, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(89094.9765625, -29304.033203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(89085.296238683, -29180.313442117, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(89363.62038664, -28915.780888816, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(89444.115475411, -29011.902564147, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(89306.103853241, -28874.139734156, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(88318.442153584, -28616.951019011, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(88269.020461821, -28675.510093387, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(88225.215950942, -28575.017272693, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(87583.019951219, -28118.997817801, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(87424.0078125, -28057.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(87015.48080538, -27742.44240227, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(86693.13650766, -27447.944743778, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(86663.541118236, -27404.231444112, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(86545.472781481, -27344.409428986, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(86767.894446492, -27178.23802498, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(86945.79555595, -27228.879368953, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(87549.9296875, -28065.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(87528.34375, -28050.568359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(87487.140625, -28021.806640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(87508.625, -28036.26953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(87466.140625, -28005.826171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))


class Borg_El_Arab_International_Airport(Airport):
    id = 35
    name = "Borg El Arab International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4450000, vhf_low_hz=39800000, vhf_high_hz=119100000, uhf_hz=251400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(99766.792969, -146755.710938, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield35_1'))
        self.runways.append(Runway(id=1, name='14L-32R', main=RunwayApproach(name='14L', heading=140, beacons=[]), opposite=RunwayApproach(name='32R', heading=320, beacons=[RunwayBeacon(id='airfield35_2', runway_name='14L-32R', runway_id=1, runway_side='32R'), RunwayBeacon(id='airfield35_0', runway_name='14L-32R', runway_id=1, runway_side='32R')])))
        self.runways.append(Runway(id=4, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.runways.append(Runway(id=3, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.runways.append(Runway(id=2, name='14R-32L', main=RunwayApproach(name='14R', heading=140, beacons=[]), opposite=RunwayApproach(name='32L', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(98761.7890625, -145492.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(98821.8984375, -145577.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(98920.171875, -145604.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(98981.25, -145701.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(99067.1796875, -145783.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(98694.375, -146165.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(98599.15625, -146157.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(98544.15625, -146070.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(98389.96875, -146015.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(98331.765625, -145934.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(100594.9765625, -147518.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(100630.71875, -147607.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(100736.2734375, -147623.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(100833.8125, -147755, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(100929.8671875, -147778.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(102079.8203125, -147041.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(102043.3359375, -147015.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(100649.1328125, -146057.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(100687.9453125, -146081.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(100723.6875, -146109.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(100763.078125, -146137.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(100801.21875, -146164.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(100842.7109375, -146192.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(100881.9453125, -146220.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(100920.09375, -146248.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(100954.5234375, -146274.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(100991.3125, -146301.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(101031.6640625, -146328.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(101068.640625, -146356.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(99960.828125, -147122.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(99918.0703125, -147091.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(99872.4765625, -147058.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(99772.9453125, -146986.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(99711.6171875, -146942.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(99652.296875, -146899.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(99118.71875, -146571.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(99079.1015625, -146542.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(98512.484375, -146157.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(98336.6953125, -146619.484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(98424.484375, -146499.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(98472.3671875, -146652.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(98371.8984375, -146816.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(98491.8671875, -146906.328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(98523.109375, -146768.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(98690.7890625, -146876.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(98779.484375, -146751.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(98642.953125, -146719.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(98742.6171875, -146552.765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(98587.109375, -146604.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(98620.4765625, -146464.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(99847.3203125, -147903.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H33', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(99722.796875, -147814.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H32', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(99690.75, -147619.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H31', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(99777.2578125, -147497.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H30', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(99853.9609375, -147614.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H29', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(99974.8671875, -147461.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(99975.4609375, -147626.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(100096.765625, -147549.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(99842.703125, -147739.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(99968.296875, -147750.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(100042.3515625, -147870.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(100127.34375, -147747.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(99987.7421875, -147950.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(99019.1875, -146494, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(98992.9140625, -146476.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(98970.140625, -146459.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(98945.234375, -146440.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(98923.09375, -146424.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(98901.5859375, -146408.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(98877.3125, -146393.109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(98852.0234375, -146374.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(101536.8671875, -146635.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(101470.0234375, -146590.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(101400.90625, -146543.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(101332.21875, -146496.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(99565.703125, -148097.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H35', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(99546.40625, -148083.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H36', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(99521.46875, -148067.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H37', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(99499.203125, -148051.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H38', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(99477.1953125, -148034.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H39', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(99455.6796875, -148019.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H40', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(100609.09375, -146028.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(100570.4921875, -146000.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(100533.7109375, -145974.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=36.0, width=36.0, height=15.0, shelter=False))


class El_Minya(Airport):
    id = 36
    name = "El Minya"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4475000, vhf_low_hz=39850000, vhf_high_hz=119200000, uhf_hz=251450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-214834.804688, -53828.40625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield36_3'))
        self.runways.append(Runway(id=1, name='34R-16L', main=RunwayApproach(name='34R', heading=340, beacons=[]), opposite=RunwayApproach(name='16L', heading=160, beacons=[RunwayBeacon(id='airfield36_1', runway_name='34R-16L', runway_id=1, runway_side='16L'), RunwayBeacon(id='airfield36_2', runway_name='34R-16L', runway_id=1, runway_side='16L')])))
        self.runways.append(Runway(id=2, name='34L-16R', main=RunwayApproach(name='34L', heading=340, beacons=[RunwayBeacon(id='airfield36_4', runway_name='34L-16R', runway_id=2, runway_side='34L'), RunwayBeacon(id='airfield36_0', runway_name='34L-16R', runway_id=2, runway_side='34L')]), opposite=RunwayApproach(name='16R', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-213455.59375, -54584.17578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-214729.65625, -53593.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-216003.15625, -52982.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-214766.59375, -53578.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-214787.046875, -53489.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-215497.921875, -53132.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-214710.875, -53600.43359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-215988.15625, -52988.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-214673.609375, -53615.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-214748.09375, -53585.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-214794.484375, -53507.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-215467.796875, -53144.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-215482.921875, -53138.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-216358.09375, -53466.33984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-213556.28125, -54568.72265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-215392.421875, -53175.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-214779.46875, -53470.88671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-216033.296875, -52970.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-216018.28125, -52976.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-215558.359375, -53108.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-216388.1875, -53386.39453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-215437.5625, -53156.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-216051.140625, -52963.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-215543.359375, -53114.16796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-216265.125, -53504.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-216154.578125, -53503.5546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-214783.4375, -53570.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-215407.4375, -53169.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-215528.234375, -53120.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-215452.796875, -53150.76953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-213751.078125, -54479.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-215513.234375, -53126.40234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-213651.890625, -54499.6796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-214655.40625, -53622.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-214692.09375, -53608.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-216066.140625, -52956.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-215422.546875, -53162.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))


class Gebel_El_Basur_Air_Base(Airport):
    id = 37
    name = "Gebel El Basur Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4500000, vhf_low_hz=39900000, vhf_high_hz=119250000, uhf_hz=251500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(55664.166016, -65567.445313, terrain), terrain)

        self.runways.append(Runway(id=2, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[]), opposite=RunwayApproach(name='36', heading=360, beacons=[])))
        self.runways.append(Runway(id=1, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[RunwayBeacon(id='airfield37_1', runway_name='15-33', runway_id=1, runway_side='33'), RunwayBeacon(id='airfield37_0', runway_name='15-33', runway_id=1, runway_side='33')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(57061.78125, -66506.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='1', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(56992.96484375, -66507.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='2', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(56894.18359375, -66523.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='3', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(56819.953125, -66424.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='4', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(57351.86328125, -66021.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='5', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(57296.73046875, -65916.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='6', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(57204.8515625, -65851.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='7', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(57180.30078125, -65780.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='8', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(56270.9453125, -64758.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(56351.22265625, -64566.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(56331.38671875, -64414.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(56062.7890625, -64635.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(55961.51171875, -64507.75390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(55782.22265625, -64577.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(55840.2890625, -64763.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(57581.03125, -64304.26171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(57632.5390625, -64237.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(57925.87109375, -63729.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(57844.87109375, -63718.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(57724.265625, -63779.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(57667.5, -63737.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(55082.08984375, -63998.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(55027.140625, -64077.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(54953.29296875, -64100.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(54880.8046875, -64107.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(54649.88671875, -64134.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(54543.72265625, -64106.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(54460.43359375, -64121.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(54407.17578125, -64176.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(54000.03125, -65016.58984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(54055.62109375, -65100, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(54153.984375, -65118.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(54218.578125, -65217.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(54229.53125, -65458.22265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(54111.36328125, -65552.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(53967.78125, -65744.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(53908.25390625, -65944.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(53996.7734375, -66059.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(54242.26171875, -65978.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(54401.07421875, -66175.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(54576.88671875, -66115.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(54700.54296875, -65950.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(54750.359375, -65784.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='9', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(54539.375, -65743.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(54377.71875, -65688.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(54556.03515625, -65318.0546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(54544.98046875, -65224.64453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(54516.45703125, -64732.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(54637.70703125, -64721.76171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(54831.6875, -64768.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(54779.578125, -64546.14453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(54920.6015625, -64582.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(54510.1328125, -63911.87109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(54453.41015625, -63804.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(54440.9765625, -63701.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(54376.640625, -63610.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(54280.87109375, -63511.07421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(54199.58984375, -63350.49609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(54424.33203125, -63332.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(55943.621839225, -65069.355600296, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(55950.562598092, -65047.388373526, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(55959.258277407, -65025.166260152, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(55967.554666268, -65003.056145555, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(55974.428301107, -64983.375636259, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(55981.102735833, -64962.974986776, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(55989.189615808, -64937.646965676, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(55999.288227803, -64905.34202457, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(54616.58984375, -64572.46484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(55224.73828125, -64766.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(55202.1796875, -64759.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(55240.8125, -64712.4453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(55218.296875, -64705.421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(55344.46484375, -64794.33984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(55392.9140625, -64809.80859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(55405.73828125, -64760.37890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(55358.08984375, -64746.6484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))


class Hurghada_International_Airport(Airport):
    id = 38
    name = "Hurghada International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4525000, vhf_low_hz=39950000, vhf_high_hz=119600000, uhf_hz=251550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-319084.890625, 247648.25, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield38_0'))
        self.runways.append(Runway(id=1, name='16L-34R', main=RunwayApproach(name='16L', heading=160, beacons=[]), opposite=RunwayApproach(name='34R', heading=340, beacons=[RunwayBeacon(id='airfield38_1', runway_name='16L-34R', runway_id=1, runway_side='34R'), RunwayBeacon(id='airfield38_2', runway_name='16L-34R', runway_id=1, runway_side='34R')])))
        self.runways.append(Runway(id=2, name='16R-34L', main=RunwayApproach(name='16R', heading=160, beacons=[]), opposite=RunwayApproach(name='34L', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-319009.1875, 249112.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-318672.875, 249023.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-316075.09375, 246079.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-317875.03125, 248740.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-319516.25, 249078.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-317860.3125, 248897.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-317517.4375, 248804.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-319252.25, 249209.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-318852.59375, 249079.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-319618.0625, 249427.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-320505.5625, 249476.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-318593.28125, 249010.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-316436.375, 248463.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-317562.53125, 248655.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-319607.21875, 249470.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-318993.6875, 248941.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-317618.65625, 248832.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-318934.5625, 249097.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-317074.09375, 248491.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-316811.71875, 247847.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-317405.375, 248612.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-317823.53125, 248726.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-319337.0625, 249233.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-319645.09375, 249331.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-319629.3125, 249385.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-318343.21875, 248248.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-320409.21875, 249475.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-316604.6875, 245816.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-317771.09375, 248711.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-319173.59375, 248981.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-317565.6875, 248817.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-319656.6875, 249289.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-320639.125, 249536.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-319548.78125, 249364.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-318124.5, 247938.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-316055.34375, 246397.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-317612.65625, 248668.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-318559.65625, 248814.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-319039.9375, 248953.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-317908.125, 248910.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-319704.15625, 249405.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-316579.5625, 248394.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-316402.875, 245613.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-315976.875, 246241.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-317328.0625, 248753.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-317716.53125, 248858.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-319574.96875, 249267.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-319380.6875, 249042, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-317004.03125, 247845.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-317454.40625, 248625.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-318617.4375, 248830.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-318671.53125, 248844.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-317763.9375, 248871.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-317425.125, 248779.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-317984.5, 249076.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-319338.25, 249030.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-319526.5625, 249449.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-320738.34375, 249530.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-318492.6875, 248986.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-316402.0625, 248542.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-316756.8125, 245858.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-317812.75, 248885.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-319425.6875, 249054.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-319717.3125, 249350.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-319563.96875, 249310.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-319537.875, 249406.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-318139, 248027.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-318531.09375, 249021.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-317508.40625, 248640.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-318734.875, 248861.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-319119.46875, 248967, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-317370.84375, 248764.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-317976, 249107.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-319170.8125, 249158.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-318756.375, 249035.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-316706.6875, 248274.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-316555.40625, 245668.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-318081.78125, 247817.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-317721.625, 248698.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-317475.1875, 248793.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-319418.09375, 249254.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-319090, 249136.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-316002.1875, 245920.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-317666.71875, 248683.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-319471.46875, 249066.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-317670, 248846.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-317968.5, 249135, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))


class Jiyanklis_Air_Base(Airport):
    id = 39
    name = "Jiyanklis Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4550000, vhf_low_hz=40000000, vhf_high_hz=119300000, uhf_hz=251600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(87971.730469, -99355.671875, terrain), terrain)

        self.runways.append(Runway(id=2, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.runways.append(Runway(id=1, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[RunwayBeacon(id='airfield39_1', runway_name='12-30', runway_id=1, runway_side='30'), RunwayBeacon(id='airfield39_0', runway_name='12-30', runway_id=1, runway_side='30')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(87923.9921875, -98685.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(87833.734375, -98558.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(89114, -100354.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(87351.1484375, -97511.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(87129.171875, -97359.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(87288.953125, -99966.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(87747.6875, -98096.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(87673.4921875, -97823.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(88879.3125, -100049.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(87856.2578125, -98590.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(86841.6640625, -99105.5078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(87596.7109375, -101004.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(88413.3515625, -100530.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(88262.8359375, -100309.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(86613.984375, -98333.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(87946.125, -98716.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(87867.5390625, -98605.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(88542.2265625, -100901.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(87818.1328125, -98325.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(89236.0078125, -100155.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(87555.890625, -97904.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(87901.4609375, -98653.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(88819.2578125, -99867.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(87890.2265625, -98637.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(87248.53125, -97352.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(87480.59375, -100396.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(88104.0625, -100726.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(87390.296875, -97693.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(87286.4765625, -97656.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(87878.859375, -98621.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(87206.34375, -97753.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(87994.609375, -100493.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(89270.5234375, -100204.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(86511.0390625, -98233.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(86517.5390625, -98124.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(87248.9375, -97556.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(87935.453125, -98701.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(87844.921875, -98574.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(88604.8671875, -100834.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(87367.3828125, -100209.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(87966.40625, -100249.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(88058.0859375, -100348.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(89198.0546875, -100106.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(86620.109375, -98437.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(86987.03125, -99296.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(86759.8515625, -98840.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(87166.4453125, -97533.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(89364.8984375, -100224.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(87350.734375, -97656.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(89307.796875, -100267.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(87912.6953125, -98669.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(89010.9921875, -100079.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(87783.921875, -98040.5078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(87535.5546875, -100760.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(88119.046875, -100581.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(89156.890625, -100006.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(89451.328125, -100315.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(88389.6953125, -100327.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(89394.5703125, -100353.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(88435.0546875, -100945.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(86595.2578125, -98682.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(88535.921875, -100555.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(87430.9375, -97741.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(88463.3828125, -100864.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(89452.9921875, -100157.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(88265.9453125, -100064.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))


class Kom_Awshim(Airport):
    id = 40
    name = "Kom Awshim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4600000, vhf_low_hz=40100000, vhf_high_hz=119400000, uhf_hz=251700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-54134.808594, -34871.597656, terrain), terrain)

        self.runways.append(Runway(id=2, name='34-16', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='16', heading=160, beacons=[])))
        self.runways.append(Runway(id=1, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-54577.96875, -33258.68359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-54976.84375, -33842.68359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-54962.28125, -33535.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-54740.98046875, -33503.37890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-54840.8671875, -33172.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-54671.85546875, -34169.14453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-54751.25, -34052.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-52736.21875, -34730.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-55015.08984375, -34633.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-52818.28515625, -35264.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-54844.29296875, -33661.0078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-55574.1015625, -34293.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-54557.875, -33054.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-54798.08203125, -33868.42578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-54494.41796875, -33187.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-54466.44921875, -33237.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-55007.66796875, -33635.22265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-54803.98046875, -33555.01171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-54444.4375, -33287.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-55289.3125, -34063.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-54881.5625, -34699.484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-54607.86328125, -33192.39453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-54788.2265625, -33367.6484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-54764.62109375, -33435.40234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-54714.99609375, -34731.5703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-54581.64453125, -33832.57421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-54773.08203125, -33770.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-55477.64453125, -34036.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-54461.9453125, -33420.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-55548.390625, -34369.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-55385.8671875, -34027.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-54637.98046875, -33126.87890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-54956.71875, -33309.67578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-55438.8984375, -34403.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-54506.89453125, -33106.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-55146.89453125, -33646.16796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-54814.77734375, -34139.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-54929.9375, -33744.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-54700.90625, -33253.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-52721.61328125, -35262.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-54434.421875, -33348.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-54620.52734375, -33877.87109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))


class Ramon_International_Airport(Airport):
    id = 41
    name = "Ramon International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4625000, vhf_low_hz=40150000, vhf_high_hz=119000000, uhf_hz=251750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-35075.113281, 364019.84375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield41_4'))
        self.runways.append(Runway(id=1, name='19-01', main=RunwayApproach(name='19', heading=190, beacons=[RunwayBeacon(id='airfield41_1', runway_name='19-01', runway_id=1, runway_side='19'), RunwayBeacon(id='airfield41_0', runway_name='19-01', runway_id=1, runway_side='19')]), opposite=RunwayApproach(name='01', heading=10, beacons=[RunwayBeacon(id='airfield41_2', runway_name='19-01', runway_id=1, runway_side='01'), RunwayBeacon(id='airfield41_3', runway_name='19-01', runway_id=1, runway_side='01')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-34434.47265625, 363660.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-35110.67578125, 363478.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-35321.765625, 363595.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-35365.7265625, 363420.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-35198.6640625, 363458.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-35686.63671875, 363403.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-35615.2265625, 363383.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-34641.9296875, 363725.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-34525.0703125, 363752.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-35530.82421875, 363436.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-35508.03515625, 363535.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-34853.8828125, 363521.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-35046.0390625, 363492.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-35761.734375, 363369.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-35755.85546875, 363343.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-34470.75390625, 363764.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-35723.82421875, 363488.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-35685.17578125, 363496.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-34358.81640625, 363677.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-35767.7734375, 363396.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-35470.75390625, 363543.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-34279.98046875, 363695.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-34590.5234375, 363625.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-34670.03125, 363607.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-34394.8359375, 363783.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-35006.2421875, 363666.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-35670.7734375, 363333, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-35647.89453125, 363504.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-34879.4609375, 363515.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-35544.6640625, 363528.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-35621.68359375, 363412, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-35516.0546875, 363373.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-34630.3125, 363616.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-34958.8671875, 363516.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-34737.8125, 363587.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-35276.74609375, 363440.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-35678.69140625, 363367.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-35247.43359375, 363612.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-34584.05859375, 363738.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-35475.16015625, 363392.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-34904.2265625, 363509.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-35750.08984375, 363318.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-35159.36328125, 363632.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-34512.13671875, 363642.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-34551.11328125, 363633.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-34695.3671875, 363713.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-35773.84375, 363423.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-35482.77734375, 363441.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-34319.26171875, 363686.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-34472.484375, 363651.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-34778.09375, 363578.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-35607.61328125, 363349.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-35081.5859375, 363649.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))


class Sharm_El_Sheikh_International_Airport(Airport):
    id = 42
    name = "Sharm El Sheikh International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4650000, vhf_low_hz=40200000, vhf_high_hz=118900000, uhf_hz=251800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-229684.5625, 306246.96875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield42_2'))
        self.runways.append(Runway(id=1, name='04R-22L', main=RunwayApproach(name='04R', heading=40, beacons=[]), opposite=RunwayApproach(name='22L', heading=220, beacons=[])))
        self.runways.append(Runway(id=2, name='04L-22R', main=RunwayApproach(name='04L', heading=40, beacons=[RunwayBeacon(id='airfield42_1', runway_name='04L-22R', runway_id=2, runway_side='04L'), RunwayBeacon(id='airfield42_0', runway_name='04L-22R', runway_id=2, runway_side='04L')]), opposite=RunwayApproach(name='22R', heading=220, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-230748.546875, 304488.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-230767.84375, 304471.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-230795.546875, 304448.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-230112.33096912, 305275.0684081, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-230156.10385399, 305234.97366063, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-230202.89442935, 305192.62826642, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-230248.95866095, 305152.02928072, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-230295.07057488, 305109.95131577, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-230341.19714397, 305067.87573576, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-230387.17221956, 305026.47332338, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-230403.265625, 305201.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-230341.796875, 305257.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-230285.53125, 305308.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-230234.703125, 305354.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-229873.85511977, 305530.69322213, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-229904.66730233, 305501.07421872, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-229935.91521551, 305472.31515422, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-229967.52042663, 305443.30313008, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-229999.04777351, 305414.32300014, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-229639.18036706, 305740.61923969, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-229671.51761994, 305710.73205277, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-229735.59755122, 305652.83134127, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-229704.42456759, 305681.12052254, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-229797.51129158, 305597.10930348, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-229766.46643607, 305624.63974582, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-230086.203125, 305481.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-230040.59375, 305522.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-229989.09375, 305568.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-229933.390625, 305619.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-229878.1875, 305669.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-229822.90625, 305719.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-229766.375, 305770.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-229711.234375, 305820.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-229841.82873414, 305559.39740674, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-230466.625, 305138.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-229544.796875, 305825.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-229501.640625, 305864.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-229458.890625, 305903.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-229415.078125, 305943.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-229327.25, 306036, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-229276.109375, 306082.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-229225.53125, 306127.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-229174.421875, 306172.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-228700.875, 306647.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-228721.265625, 306668.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-228625.3125, 306715.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-228645.09375, 306736.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-228258.046875, 307050.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))


class Wadi_Abu_Rish(Airport):
    id = 43
    name = "Wadi Abu Rish"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4675000, vhf_low_hz=40250000, vhf_high_hz=119450000, uhf_hz=251850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-119840.890625, 42431.076172, terrain), terrain)

        self.runways.append(Runway(id=2, name='19R-01L', main=RunwayApproach(name='19R', heading=190, beacons=[]), opposite=RunwayApproach(name='01L', heading=10, beacons=[RunwayBeacon(id='airfield43_1', runway_name='19R-01L', runway_id=2, runway_side='01L'), RunwayBeacon(id='airfield43_0', runway_name='19R-01L', runway_id=2, runway_side='01L')])))
        self.runways.append(Runway(id=1, name='19L-01R', main=RunwayApproach(name='19L', heading=190, beacons=[]), opposite=RunwayApproach(name='01R', heading=10, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-121889.703125, 42152.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-118980.9765625, 42941.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-121030.234375, 41452.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-118767.0078125, 43002.06640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-121631.0625, 42272.16796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-119506.0625, 42734.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-118260.9921875, 42176.98828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-119646.765625, 42698.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-119553.3203125, 42722.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-117874.703125, 43146.83203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-121428.296875, 41487.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-117909.5234375, 42383.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-120279.0625, 42536.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-119480.984375, 42740.86328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-121097.296875, 41573.92578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-117929.96875, 42261.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-119692.7734375, 42686.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-120124.78125, 42576.24609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-121896.015625, 42176.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-118193.5546875, 43112.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-119457.9921875, 42747.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-120325.40625, 42524.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-119600.5859375, 42710.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-119529.6015625, 42728.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-118427.203125, 42132.97265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-117880.78125, 43172.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-120544.9140625, 41701.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-121629, 42412.49609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-121194.78125, 41411.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-119577, 42716.24609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-120100.6484375, 42582.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-120655.5390625, 42506.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-121358.375, 41370.5078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-120370.6640625, 42512.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-118092.6875, 42358.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-120930.25, 41613.91015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-117887.5078125, 43196.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-118655.875, 43030.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-121463.875, 42452.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-121261.5859375, 41534.17578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-121901.7421875, 42198.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-119670.234375, 42692.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-121299.6328125, 42495.95703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-120822.109375, 42431.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-119434.6328125, 42753.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-118094.734375, 42219.9609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-117893.2734375, 43219.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-118430.78125, 43087.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-118546.1640625, 43060.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-121298.78125, 42356.88671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-118031.203125, 43169.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-121132.2265625, 42402.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-120348.21875, 42518.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-120393.984375, 42506.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-118258.828125, 42315.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-120168.65625, 42564.87109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-118879.3515625, 42971.26953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-120302.671875, 42530.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-120189.890625, 42559.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-120865.765625, 41496.77734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-121906.9921875, 42219.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-120147.390625, 42570.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-118322.109375, 43113.94140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-117797.671875, 42487.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-121134.1953125, 42539.30078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-121464.3671875, 42315.2890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-118424.9765625, 42270.36328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-119623.828125, 42704.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-120076.2109375, 42588.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))


class Al_Bahr_al_Ahmar(Airport):
    id = 44
    name = "Al Bahr al Ahmar"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4700000, vhf_low_hz=40300000, vhf_high_hz=119500000, uhf_hz=251900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-387890.744647, 181451.05889, terrain), terrain)

        self.runways.append(Runway(id=2, name='32L-14R', main=RunwayApproach(name='32L', heading=320, beacons=[]), opposite=RunwayApproach(name='14R', heading=140, beacons=[])))
        self.runways.append(Runway(id=1, name='32R-14L', main=RunwayApproach(name='32R', heading=320, beacons=[]), opposite=RunwayApproach(name='14L', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-387375.6875, 181263.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-388978.375, 182382.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-387707.46875, 181640.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-386459.40625, 180694.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-386947.9375, 181117.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-389172.75, 182482.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-387035.34375, 180341, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-386559.46875, 180780.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-389085.84375, 182503.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-389012.03125, 181667.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-386698.25, 180985.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-389533.3125, 182067, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-388868.28125, 182257.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-389290.5, 181871.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-386397.90625, 180614.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-387462.6875, 181323.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-386675.4375, 180224.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-388856.1875, 182391.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-389387.59375, 181916.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-386917.65625, 180298.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-386521.125, 180753.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-389505.0625, 181980.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-389185.5, 181849.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-386771.28125, 180242.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-386642.4375, 180869.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-388248.59375, 182012.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-387816.03125, 181656.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-387007, 181037.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-387002.03125, 180268.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-388512.375, 182186.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-388756.9375, 182208.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-389072.25, 181771.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-386866.9375, 180265.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))


class Quwaysina(Airport):
    id = 45
    name = "Quwaysina"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4725000, vhf_low_hz=40350000, vhf_high_hz=119550000, uhf_hz=251950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(59123.898438, -10186.813477, terrain), terrain)

        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(58410.3046875, -9865.103515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(58508.796875, -9886.787109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(58457.80078125, -9876.142578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(58938.453125, -9977.3310546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(58229.15234375, -9787.2470703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(58763.14453125, -9938.0380859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(58833.35546875, -9954.1611328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(58693.55859375, -9922.4404296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(58623, -9906.623046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(58903.6484375, -9969.5400390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(58363.11328125, -9853.3173828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(58868.6484375, -9961.685546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(58658.59375, -9914.5859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(58728.62109375, -9930.2978515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(58798.5703125, -9946.6455078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))


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
    Palmachim,
    Sde_Dov,
    Tel_Nof,
    Ben_Gurion,
    St_Catherine,
    Abu_Rudeis,
    Baluza,
    Bir_Hasanah,
    El_Arish,
    El_Gora,
    Al_Khatatbah,
    Al_Rahmaniyah_Air_Base,
    Beni_Suef,
    Birma_Air_Base,
    Borg_El_Arab_International_Airport,
    El_Minya,
    Gebel_El_Basur_Air_Base,
    Hurghada_International_Airport,
    Jiyanklis_Air_Base,
    Kom_Awshim,
    Ramon_International_Airport,
    Sharm_El_Sheikh_International_Airport,
    Wadi_Abu_Rish,
    Al_Bahr_al_Ahmar,
    Quwaysina,
]

