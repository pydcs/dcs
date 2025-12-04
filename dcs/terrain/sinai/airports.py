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
                crossroad_idx=0, position=mapping.Point(58384.940515907, 81352.07683942, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(58412.687240262, 81449.716939678, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(58306.571999159, 81555.26424849, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(58335.324394108, 81661.605623096, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(57512.73053431, 83563.045414748, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(57659.504631416, 83710.443862168, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=9, position=mapping.Point(57468.599671076, 84047.749563805, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(57377.218929103, 84037.805800959, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=24, position=mapping.Point(56523.161504645, 84147.899864045, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(56541.289425635, 84290.102796029, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(56374.917045215, 83195.398585751, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(56207.87890625, 83126.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(56236.810596873, 83049.518775067, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(56472.453125848, 82424.419699925, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(56430.556912933, 82492.418710561, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(56251.021797942, 82378.808245771, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(56293.000169378, 82311.174603151, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=39, position=mapping.Point(56581.159123277, 81432.174720889, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(56612.055610012, 81264.838702019, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(56468.58984375, 81199.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(56653.66507691, 81136.859299105, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(57261.324780879, 81318.501419069, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(57399.206807001, 81353.783784007, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(57470.371370181, 81371.479445277, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(57588.7255915, 81386.038801884, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(57666.847196893, 81486.098683624, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=14.0, height=6.0, shelter=False))


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
                crossroad_idx=30, position=mapping.Point(83085.991979099, 79014.337398778, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(83187.2890625, 78947.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(83257.964143801, 79053.665004617, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(83333.9921875, 78989.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(83415.508066702, 79026.353675815, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(83568.879996228, 78564.936511649, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(83445.604183758, 78542.935769586, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=62, position=mapping.Point(80714.527883809, 78245.742538807, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=14.0, height=6.0, shelter=False))
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
                airplanes=True, slot_name='05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(59614.311216298, 96788.677748161, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(59577.694028798, 96834.474623161, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=41.0, width=41.0, height=18.0, shelter=False))
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
                crossroad_idx=0, position=mapping.Point(30427.841796875, 100348.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(29875.7109375, 100300.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(29990.724609375, 97656.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30952.787109375, 98976.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(30898.4375, 98838.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30794.85546875, 99455.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(29925.1171875, 100066.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(31045.828125, 98810.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(29765.341796875, 99157.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30547.625, 99639.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(30451.6640625, 97446.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(30889.55078125, 99457.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(29974.46484375, 97849.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(30782.0703125, 99088.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(29867.111328125, 99101.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(29959.1171875, 97425.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(29977.376953125, 97573.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(30547.962890625, 99915.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(30613.12109375, 97974.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(30611.734375, 97872.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(30938.52734375, 99457.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(30841.73046875, 99457.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(29879.421875, 100155.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(29875.873046875, 99960.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(29886.67578125, 99567.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(31282.82421875, 99154.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(31093.134765625, 99092.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(29958.392578125, 97748.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(30640.23046875, 97778.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(30550.78515625, 99767.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(29895.0234375, 100444.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(30615.0859375, 97597.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(30985.19140625, 99457.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(30575.935546875, 100048.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(29756.080078125, 99580.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(30670.80078125, 97683.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(29987.822265625, 99567.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(30366.603515625, 100349.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(30563.16796875, 100148.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(30629.4453125, 99057.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(29963.845703125, 99121.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))


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
                crossroad_idx=0, position=mapping.Point(131218.265625, 328186.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='124', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(131115.4375, 328835.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='139', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(132316.421875, 326812.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(132258.171875, 327568.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(132632.46875, 326385.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(132085.828125, 328335.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(132537.859375, 326361.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(131443.75, 328336.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(130669.8046875, 328939.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='162', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(130602.0859375, 328957.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='165', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(132192.75, 327550.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(131952.21875, 328024.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(132077.8125, 328366.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(132474.796875, 326345.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(130738.6015625, 328924.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='159', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(130624.7109375, 328951.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='164', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(132479.21875, 326705.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(132210.90625, 327556.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(132260.8125, 327450.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(132443.0625, 326843.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(131967.96875, 328028.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(132522.109375, 326357.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(130847.3359375, 328875.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='154', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(132463.421875, 326701.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(132269.109375, 326800.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(131229.671875, 328541.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(132411.734375, 326328.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(132518.140625, 326511.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(131176.609375, 328211.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(130773.9375, 328790.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='147', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(130626.25, 329237.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='172', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(131163.609375, 328917.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='145', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(131419, 328281.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(132173.359375, 327545.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(132395.203125, 326832.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(131478.375, 328347.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(131255.84375, 328229.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(130646.703125, 328945.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='163', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(131131.390625, 328863.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='141', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(130687.046875, 328877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='156', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(132115.21875, 327531, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(132289.78125, 327576.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(132347.953125, 326820.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(132252.21875, 328414.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(132265.46875, 325993, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(132569.40625, 326369.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(132549.703125, 326519.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(131213.9375, 328254.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(131123.3125, 328849.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='140', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(130712.234375, 328882.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='155', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(132363.75, 326824.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(132226.078125, 328431.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(131513.5, 328358.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(132506.3125, 326353.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(132565.453125, 326523.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(131139.390625, 328876.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='142', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(132353.078125, 326672.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(132401.75, 326992.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(132273.9375, 327572.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(132338.671875, 326976.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(132273.09375, 328399, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(132342, 326014.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(131528.53125, 328306.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(132459.046875, 326341.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(132486.765625, 326502.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(131147.46875, 328890.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='143', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(130831.265625, 328848.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='152', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(130640.2421875, 329229.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='171', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(132426.8125, 326840.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(131712.5, 328389.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(132228.3125, 326948.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(132241.4375, 327445.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(132284.890625, 326804.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(131454.40625, 328287.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(132443.28125, 326336.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(132423.59375, 326486.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(130823.0625, 328834.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='151', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(131155.5625, 328904.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='144', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(132384.578125, 326680.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(132357.734375, 327474.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(132229.796875, 328572.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='106', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(131270.0625, 328610.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='136', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(132427.5, 326332.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(132376.28125, 326474.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(130839.1953125, 328861.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='153', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(130807.046875, 328807.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='149', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(132410.984375, 326836.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(132344.75, 326466.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(132291.375, 326964.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(132239.796875, 328590.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(132470.984375, 326498.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(132502.390625, 326507.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(131152.25, 328938.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='146', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(132305.765625, 326660.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(132321.21875, 327584.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(132219.6875, 328547.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(132392.03125, 326478.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(132416.15625, 326688.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(132318.96875, 327464.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(132386, 326988.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(131261.21875, 326484.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(132596.96875, 326531.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(130798.953125, 328793.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='148', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(132081.75, 328351.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(132076.453125, 327521.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(132338.34375, 327469.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(132275.578125, 326960.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(131251.609375, 326521.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(132015.28125, 328040.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(131245.890625, 328569.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='133', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(132407.796875, 326482.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(130667.640625, 329213.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='170', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(132455.078125, 326494.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(132280.203125, 327455, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(132163.90625, 327425.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(132322.921875, 326972.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(132204.59375, 328520.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(130569.3828125, 329314.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='174', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(132097.640625, 328289.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(130681.34375, 329205.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='169', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(130814.9921875, 328820.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='150', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(130692.0625, 328933.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='161', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(132431.90625, 326693.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(132134.59375, 327535.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(132299.578125, 327459.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(132144.515625, 327420.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(132370.234375, 326984.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(132290.21875, 328388.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(131270.765625, 326447.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(130695.0859375, 329197.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='168', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(131171.71875, 328279.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(132332.1875, 326816.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(131983.6875, 328032.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(132226.640625, 327560.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(132354.453125, 326980.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(131280.390625, 326409.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(132292.1875, 326000.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(132585.1875, 326373.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(132093.734375, 328305.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(130716.15625, 328929.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='160', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(132183.28125, 327430.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(132305.515625, 327580.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(132244.109375, 326952.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(131134.546875, 328236.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(132316.96875, 326007.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(131245.515625, 328528.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(131237.765625, 328555.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(132581.203125, 326527.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(130612.4375, 329244.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='173', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(130663.5078125, 328868.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='157', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(132105.75, 327410.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(132153.984375, 327540.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(131686.671875, 328383.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(131253.953125, 328582.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(132368.828125, 326676.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(132202.671875, 327435.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(132616.671875, 326381.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(131262.015625, 328596.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(132073.9375, 328382.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(130579.8046875, 328962.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='166', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(132447.65625, 326697.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(132222.046875, 327440.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(130640.796875, 328859.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='158', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(131278.1875, 328623.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='137', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(132089.765625, 328320.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(132600.921875, 326377.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(132337.3125, 326668.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(132125.140625, 327415.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(132095.828125, 327526.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(131491.25, 328296.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(131289.6875, 326372.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(131205.375, 328540.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='138', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(130719.0234375, 329212.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='167', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(132380.21875, 326320.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))


class Nevatim(Airport):
    id = 8
    name = "Nevatim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4850000, vhf_low_hz=40600000, vhf_high_hz=132400000, uhf_hz=252200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(129123.308594, 360906.375, terrain), terrain)

        self.runways.append(Runway(id=1, name='08L-26R', main=RunwayApproach(name='08L', heading=80, beacons=[]), opposite=RunwayApproach(name='26R', heading=260, beacons=[RunwayBeacon(id='airfield8_2', runway_name='08L-26R', runway_id=1, runway_side='26R'), RunwayBeacon(id='airfield8_0', runway_name='08L-26R', runway_id=1, runway_side='26R')])))
        self.runways.append(Runway(id=3, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield8_1', runway_name='07-25', runway_id=3, runway_side='25'), RunwayBeacon(id='airfield8_3', runway_name='07-25', runway_id=3, runway_side='25')])))
        self.runways.append(Runway(id=2, name='08R-26L', main=RunwayApproach(name='08R', heading=80, beacons=[]), opposite=RunwayApproach(name='26L', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(128522.6953125, 363723.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(128468.3359375, 363636.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(128491.171875, 363731.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(128442.2109375, 359331.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(128471.5625, 361753.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(128732.921875, 360180.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(128441.96875, 361239.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='146', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(128717.2265625, 360282.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(126433.1953125, 362891.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(128459.375, 359141.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(128465.7578125, 359325.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(129360.921875, 362749.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(128590.34375, 361810.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(129285.2109375, 362498.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(128819.921875, 359236.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(128855.125, 359228.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(126864.9296875, 362556.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(128436.703125, 363645.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(129223.6484375, 362184.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(128322.5390625, 363636.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(128346.125, 363731.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(127033.6875, 363207.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(129466.53125, 361874.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(128366.5, 359153.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(128454.59375, 359205.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(128503.0234375, 361471.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='136', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(128556.25, 359301.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(128488.609375, 359503.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(129192.578125, 362468.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(128628.796875, 360023.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(128500.25, 363629.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(129612.484375, 361772.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(128543.8671875, 363548.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(128569.734375, 361731.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(126878.9921875, 363866.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(128724.4296875, 360234.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(128479.296875, 361779.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(127013.8125, 363832.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(126894.28125, 362665.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(128576.28125, 361757.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(128494.59375, 359599.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(127129.8828125, 363605.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(126907.5390625, 362720.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(127046.875, 363260.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(129230.1953125, 362210.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(129098.3515625, 361748.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(129135.71875, 361723.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(129133.2109375, 362232.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='124', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(128405.046875, 363652.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(128422.1328125, 361546.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='142', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(128347.2578125, 361261.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='150', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(128491.6484375, 361832.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(128427.5859375, 363746.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(126981.3515625, 362993.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(129044.3203125, 361785.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(128428.140625, 361186.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='144', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(127060.7265625, 363315.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(127144.25, 363666.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(128407.734375, 359177.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(128520.4375, 359538.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(126922, 362774.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(129447.609375, 361887, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(129576.5078125, 361797.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(128408.4140625, 361493.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='140', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(129145.5625, 362285.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(126967.46875, 362937.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(128576.59375, 360018, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(127020.7578125, 363154.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(128557.9609375, 363605.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(128557.4609375, 359955.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(129244.2578125, 362263.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(128338.8828125, 363699.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(128533.2890625, 359308.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(128694.640625, 362023.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(129236.671875, 362237, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(129557.765625, 361811.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(129224.65625, 362532.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(129520.703125, 361837.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(128486.8515625, 359319.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(129341.3671875, 362794.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(128495.78125, 361445.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(129376.3046875, 362840.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(129593.921875, 361785.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(129190.15625, 361687.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(128557.3828125, 359578.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(128508.9609375, 359312.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(127115.6015625, 363550.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(129503.2890625, 361849.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(128956.2734375, 359201.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(128330.484375, 363668.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(126834.375, 363879.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(128613.5625, 362078.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(126936.59375, 362830.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(129321.3046875, 362838.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(128887.640625, 359219.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(128582.7578125, 361783.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(129178.2734375, 362516.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(128669.53125, 360198.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(126879.921875, 362611.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(128667.375, 362041.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(128679.3046875, 360146.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(128400.6796875, 361466.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='139', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(128790.5078125, 359247.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(128509.09375, 361497.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='137', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(129162.640625, 361705.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(128463.390625, 359563.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(128528.15625, 359637.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(128504.8203125, 359167.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(129630.015625, 361760.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(127007.90625, 363101.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(129270.6484375, 362548.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(128339.8125, 361234.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='149', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(126967.8203125, 363844, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(129483.875, 361863.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(128662.3046875, 360245.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(129396.4140625, 362796.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(129030.484375, 361793.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(126463.1015625, 362973.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='105', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(126476.5, 363031.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(129125.4765625, 362206.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(128612.203125, 359961.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(129540.4765625, 361823.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(128923.46875, 359210.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(128459.4453125, 363738.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(128537.265625, 363519.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(128484.640625, 361806.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='133', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(128414.6953125, 361519.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='141', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(128532.2109375, 360009.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(126994.578125, 363046.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(128516.8515625, 361524.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='138', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(128434.2109375, 361212.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='145', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(126923.65625, 363853.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(128551.6484375, 363576.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(127101.296875, 363487.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(128420.8984375, 361160.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='143', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(127174.8984375, 363780.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(128333.5390625, 361208.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='148', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(129416.421875, 362751.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(128640.2578125, 362060.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(128510.3046875, 359950.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(126420.625, 362841.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(129239.0234375, 362483.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(128325.8046875, 361181.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='147', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(127170.3984375, 364006.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='151', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(129138.5546875, 362259.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(127086.78125, 363432.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(128419.59375, 359339.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(126850.265625, 362500.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(127159.546875, 363720.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(128418.609375, 359117.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(129016.8828125, 361803.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))


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
                crossroad_idx=0, position=mapping.Point(79399.84375, 328344.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(79640.7890625, 330307.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(79528.640625, 328322.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(80286.71875, 329838.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(81099.6015625, 330491.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(79911.65625, 328644.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(79483.3203125, 330184.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(79515.140625, 329132.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(79986.78125, 328850.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(80246.4921875, 329916.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(79569.96875, 328064.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(79613.9140625, 330189.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(79447.5078125, 328377.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(79545.71875, 327948.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(79365.59375, 330091.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(80530.9921875, 330225.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(79576.390625, 327986.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(79663.5390625, 327231.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(79509.2109375, 327988.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(79424.515625, 330137.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(79589.53125, 330170.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(79454.8359375, 330063.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(79562.09375, 330245.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(79818.375, 328714.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(81315.2890625, 329121, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(81320.484375, 329316.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(79607.3984375, 327256.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(80900.6015625, 330283.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(79919.5546875, 328772.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(79426, 328965.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(79783.7421875, 328947.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(81326.6875, 329145.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(81277.5390625, 329211, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(79477.046875, 328942.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(79750.015625, 328745.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(79440.4453125, 328317.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(80258.6796875, 329584.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(79568.2109375, 327228.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(79162.671875, 327735.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(79787.9765625, 327454.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(79478.9609375, 330083.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(79722.8984375, 327484.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(79715.1953125, 328978.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(80441.953125, 330520.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(80969.7421875, 330253.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(81303.2734375, 329200.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(80536.3671875, 330506.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(79281.4296875, 330049.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(79306.9296875, 327438.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(79452.328125, 328953.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(79773.4296875, 328735.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(79338.53125, 327475.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(79369.953125, 327513, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(80933.75, 330273.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(79963.46875, 328860.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(79463.6640625, 330168.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(80478.84375, 330488.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(79252.2578125, 327697.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(79624.453125, 327202.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(79879.671875, 328788.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(79684.5625, 330367.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(79373.203125, 328985.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(79698.6484375, 327493.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(80498.8203125, 330188.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(79848.7421875, 328909.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(79207.6796875, 327716.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(80242.46875, 329858.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(79528.6328125, 327199.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(79581.7578125, 330261.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(79404.9296875, 330122.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(80173.2265625, 329572.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(79468.921875, 329151.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(81046.5859375, 330505.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(80499.5625, 330538.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(79480.78125, 328290.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(80614.1953125, 330241.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(79797.375, 328824.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(81040.9375, 330221.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(79488.2578125, 328349.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(79744.0390625, 327474.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(79503.0703125, 330199.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(79444.203125, 330152.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(81094.6953125, 330539.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(79686.078125, 330246.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(80197.65625, 329878.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(79816.3203125, 328816.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(79867.6875, 328663.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(79940.3203125, 328869.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(79935.1640625, 328765.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(79836.390625, 328807.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(80207.3359375, 329607.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(79209.2265625, 327771.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(80009.703125, 328840.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(79542.46875, 330230.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(80290.7421875, 329896.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(79284.765625, 327491.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(80462.6328125, 330570.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(79253.65625, 327752.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(79164.265625, 327791.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(79385.5078125, 330106.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(79253.328125, 327453.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(79888.65625, 328654.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(79760.734375, 328957.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(79637.2109375, 330208.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(79606.640625, 328024.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(79856.953125, 328798.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(79502.625, 330102.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(79681.609375, 327505.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(79871.1640625, 328898.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(79315.796875, 327528.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(79398.5390625, 328975.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(81004.6015625, 330237.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(80549.328125, 330168.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(80292.2421875, 329619.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(80581.7421875, 330204.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(79764.21875, 327463.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(79894.1640625, 328888.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(80241.0625, 329642.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(80562.78125, 330261.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(80202.0078125, 329936.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(79806.5859375, 328937.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(79662.234375, 330227.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(79539.7890625, 328026.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(79967.5546875, 328751.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(81089.9140625, 330588.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(81037.21875, 330602.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(81309.125, 329291.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(79345.796875, 330075.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(79620.8203125, 330292.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(79795.34375, 328724.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(79522.78125, 330215.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(81042.140625, 330553.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(80515.5, 330456.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(79584.8984375, 327173.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(79845.90625, 328674.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(79951.0078125, 328758.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(79737.9375, 328967.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(80224.890625, 329548.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(79917.2421875, 328878.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(79601.421875, 330276.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))


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
                crossroad_idx=0, position=mapping.Point(-10277.198242188, 356932.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-10531.686523438, 357330.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-10276.572265625, 357297.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-11895.16015625, 356795.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-11925.56640625, 356783.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-12492.563476562, 356488.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-13285.514648438, 356412.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-13460.950195312, 356105.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-10841.040039062, 356687.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-10337.262695312, 355967.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-10355.96875, 356556.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-12435.408203125, 356468.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-10321.577148438, 356467.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-13112.072265625, 355814.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-10236.669921875, 357325.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-12859.301757812, 356341.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-10790.404296875, 357190.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-13122.634765625, 355844.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-10344.4765625, 356526.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-9994.9697265625, 356986.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-13089.150390625, 355755.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-11806.34765625, 356829.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-11860.782226562, 356808.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-11197.30078125, 356938.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-10147.611328125, 357322.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-11118.0546875, 356989.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-13412.354492188, 356112.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-10305.711914062, 356088.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-12400.231445312, 356502.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-10187.731445312, 357294.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-12907.547851562, 356350.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-10825.734375, 357236.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-13274.64453125, 356364.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-13434.841796875, 356054.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-10470.771484375, 357333.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-13135.317382812, 355874.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-10271.11328125, 355981.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-9982.658203125, 357078.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-11778.922851562, 356840.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-12422.728515625, 356556.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-12457.771484375, 356521.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-13483.469726562, 356048.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-10764.3828125, 357231.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-13364.16015625, 356118.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-13377.84765625, 355695.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-10332.900390625, 356497.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-12364.587890625, 356535.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-13228.696289062, 356401.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-10227.610351562, 357267.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-10295.98046875, 356974.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-10556.4140625, 357373.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-11833.40625, 356819.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-11873.599609375, 356649.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-10015.893554688, 357042.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-11148.803710938, 356937.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-13474.987304688, 355704.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-10816.329101562, 357149, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-11763.821289062, 356731.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-11791.323242188, 356721.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-13239.95703125, 356448.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-10851.5546875, 357195.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-9949.01953125, 357113.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-13099.053710938, 355784.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-12811.594726562, 356333.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-13386.65625, 356060.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-10851.951171875, 356718.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-11818.291992188, 356711.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-10495.100585938, 357376.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-11862.40234375, 356622.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-12773.791992188, 356380.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-9962.0693359375, 357022.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-10259.946289062, 356887.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-10507.250976562, 357288.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-11883.848632812, 356676.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-11246.315429688, 356939.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-13426.129882812, 355699.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-10446.712890625, 357291.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-10816.41796875, 356631.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-13442.424804688, 355759.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-13147.985351562, 355905.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-11215.447265625, 356993.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-10376.810546875, 356022.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-12869.478515625, 356399.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-13217.524414062, 356354.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-10240.881835938, 356845.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-10874.952148438, 356777.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-13491.260742188, 355763.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-9928.7197265625, 357058.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-11894.767578125, 356704.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-10829.5390625, 356657.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-13394.114257812, 355754.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-11166.623046875, 356991.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-10309.79296875, 356439.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-12821.431640625, 356389.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-10877.154296875, 357153.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-10196.427734375, 357353.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-13263.83203125, 356317.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-10863.3671875, 356748.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-11736.40234375, 356742.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-10366.762695312, 356587.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))


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
                crossroad_idx=4, position=mapping.Point(21507.287064173, 119066.46583599, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(21450.9214492, 119172.49812531, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(21348.034433528, 119131.23745359, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(21313.893690008, 119268.10089092, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(20840.1966832, 119746.60400414, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(20725.714618864, 119810.95546245, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(19572.236529927, 120901.67963458, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(19474.936223089, 120917.754811, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(19507.782532735, 121015.25036258, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(19383.326024191, 121016.04707304, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(19398.131870609, 121118.38371873, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(20036.189298405, 121379.20835614, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(20015.544768362, 121477.63866102, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(19920.71579129, 121445.77637103, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(19907.946404046, 121541.28647345, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(19812.76895884, 121536.16695012, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))


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
                crossroad_idx=4, position=mapping.Point(-2021.1150231321, 56508.436476241, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-2145.3559570312, 56472.83203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-2311.8850464133, 56993.038365579, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-2170.3251085004, 57039.25008559, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-2096.6587636882, 57101.506773795, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-1996.1820374537, 57107.301961397, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=38, position=mapping.Point(499.62514429923, 58265.604181108, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(630.4141225294, 58289.937426093, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(624.97958886748, 58045.616308424, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(697.30502330511, 58139.365277225, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=57, position=mapping.Point(876.25159608466, 57286.108035374, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(961.03619186018, 57359.224391097, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=3, position=mapping.Point(100224.03367878, 19961.419785787, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(100331.81160759, 19910.026441558, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=9, position=mapping.Point(100865.82500347, 20432.476265655, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(100983.65233507, 20441.729224556, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=39, position=mapping.Point(103186.62583747, 19178.379659971, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(103311.90192502, 19196.071463535, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(103411.140625, 19720.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(103313.63148748, 19717.010113604, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(103239.95412996, 19839.959597552, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))


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
                crossroad_idx=0, position=mapping.Point(61826.114800753, 41083.843864541, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(61715.00973998, 41070.583630209, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(61604.445800781, 40997.91897583, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(61518.881085472, 41074.950724806, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(60918.097900391, 41579.110443115, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(61024.177734174, 41624.404361693, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(61141.740112305, 41468.940437317, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(60819.323682705, 41660.864416139, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(60712.324077134, 41486.26659923, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=22, position=mapping.Point(58800.776034732, 40932.931284208, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(58738.125065731, 40858.902338043, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(58628.547546387, 40859.839161977, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(58503.356811523, 40924.164428711, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=6, position=mapping.Point(40208.126204883, 35040.568836613, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(40253.978184047, 35095.044486096, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(40293.463482704, 35139.96003121, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(39714.725075172, 35744.880532512, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(39595.79296875, 35761.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(39541.049839582, 35843.815916761, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(39427.444071222, 35905.050012605, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(39273.419312429, 35831.448066105, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=41, position=mapping.Point(37148.853407083, 33896.455924058, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(37094.193721708, 33772.568382952, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(37131.408065113, 33666.524309057, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(37159.476639876, 33539.479793518, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=14.0, height=6.0, shelter=False))
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

        self.runways.append(Runway(id=2, name='05C-23C', main=RunwayApproach(name='05C', heading=50, beacons=[RunwayBeacon(id='airfield17_1', runway_name='05C-23C', runway_id=2, runway_side='05C'), RunwayBeacon(id='airfield17_2', runway_name='05C-23C', runway_id=2, runway_side='05C')]), opposite=RunwayApproach(name='23C', heading=230, beacons=[RunwayBeacon(id='airfield17_3', runway_name='05C-23C', runway_id=2, runway_side='23C'), RunwayBeacon(id='airfield17_9', runway_name='05C-23C', runway_id=2, runway_side='23C')])))
        self.runways.append(Runway(id=3, name='05L-23R', main=RunwayApproach(name='05L', heading=50, beacons=[RunwayBeacon(id='airfield17_7', runway_name='05L-23R', runway_id=3, runway_side='05L'), RunwayBeacon(id='airfield17_0', runway_name='05L-23R', runway_id=3, runway_side='05L')]), opposite=RunwayApproach(name='23R', heading=230, beacons=[RunwayBeacon(id='airfield17_5', runway_name='05L-23R', runway_id=3, runway_side='23R'), RunwayBeacon(id='airfield17_11', runway_name='05L-23R', runway_id=3, runway_side='23R')])))
        self.runways.append(Runway(id=1, name='05R-23L', main=RunwayApproach(name='05R', heading=50, beacons=[RunwayBeacon(id='airfield17_6', runway_name='05R-23L', runway_id=1, runway_side='05R'), RunwayBeacon(id='airfield17_8', runway_name='05R-23L', runway_id=1, runway_side='05R')]), opposite=RunwayApproach(name='23L', heading=230, beacons=[RunwayBeacon(id='airfield17_4', runway_name='05L-23L', runway_id=1, runway_side='23L'), RunwayBeacon(id='airfield17_10', runway_name='05R-23L', runway_id=1, runway_side='23L')])))
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
                airplanes=True, slot_name='76', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(7042.5873674493, -30869.015311433, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(7044.5240041903, -31007.403872425, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(6893.65234375, -30899.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(6897.0670472473, -31044.343062778, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=78, position=mapping.Point(9933.5908203125, -31873.470703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(9851.7713215619, -31785.470747299, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(9782.3761747273, -31743.643217589, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
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
        super().__init__(mapping.Point(31533.311523, 19893.730469, terrain), terrain)

        self.runways.append(Runway(id=2, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[RunwayBeacon(id='airfield19_1', runway_name='04-22', runway_id=1, runway_side='22'), RunwayBeacon(id='airfield19_0', runway_name='04-22', runway_id=1, runway_side='22')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(32444.36328125, 20552.439453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(32322.3046875, 20535.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(30357.767578125, 20589.005859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30072.76953125, 20521.490234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(31596.244140625, 19513.482421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30393.4140625, 21476.232421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(31616.267578125, 20846.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(31858.73828125, 21010.904296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30783.546875, 18604.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(30531.326171875, 18978.55078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(31566.033203125, 19349.197265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(31365.7265625, 19317.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(30525.169921875, 21383.564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(30350.421875, 20731.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(30284.296875, 19051.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(31296.125, 18885.458984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(30360.9375, 21498.876953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(32095.251953125, 21085.134765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(30426.201171875, 21453.267578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(30300.921875, 20524.134765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(30520.23046875, 19335.900390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(30654.041015625, 18693.654296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(31301.494140625, 19231.892578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(31558.873046875, 19453.314453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(31405.625, 19361.470703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(31923.478515625, 20800.728515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(30373.015625, 20660.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(30141.482421875, 20501.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(30295.19140625, 21545.556640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(31260.220703125, 18635.82421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(31346.162109375, 19295.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(32180.93359375, 21070.654296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(30409.47265625, 19278.708984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(31232.1640625, 18726.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(31445.25390625, 19409.251953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(30594.619140625, 21334.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(32449.369140625, 20678.076171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(31735.021484375, 20867.134765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(30714.1484375, 20910.728515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(31310.109375, 18790.927734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(30388.140625, 19129.841796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(31023.123046875, 18554.244140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(30458.390625, 21430.533203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(30950.70703125, 18622.638671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(30986.990234375, 18590.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(32332.67578125, 21246.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(32261.298828125, 21130.666015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(31846.75, 20711.095703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(31266.564453125, 19191.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(31385.62109375, 19339.650390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(30215.814453125, 20491.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(30327.734375, 21522.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(30559.111328125, 21358.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(30491.62890625, 21406.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(32320.185546875, 20420.119140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(32184.021484375, 21206.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(30272.74609375, 20476.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(29911.150390625, 19938.90234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(30704.248046875, 18605.771484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(31607.521484375, 19398.189453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(30778.876953125, 20982.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(30908.23046875, 18556.033203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(29973.490234375, 19912.763671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=12.5, height=5.5, shelter=False))


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
        self.beacons.append(AirportBeacon(id='airfield20_2'))
        self.runways.append(Runway(id=3, name='29R-11L', main=RunwayApproach(name='29R', heading=290, beacons=[]), opposite=RunwayApproach(name='11L', heading=110, beacons=[])))
        self.runways.append(Runway(id=2, name='29L-11R', main=RunwayApproach(name='29L', heading=290, beacons=[]), opposite=RunwayApproach(name='11R', heading=110, beacons=[])))
        self.runways.append(Runway(id=1, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[RunwayBeacon(id='airfield20_3', runway_name='05-23', runway_id=1, runway_side='05'), RunwayBeacon(id='airfield20_0', runway_name='05-23', runway_id=1, runway_side='05')]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(188941.90625, 334075.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(189215, 331952.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(190232.796875, 333806.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(190527.03125, 332507.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(189341.6875, 332683.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(189085.171875, 334470.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(190393.4375, 333635.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(189368.65625, 332357.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(189115.171875, 334537.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(188968.765625, 334226.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(190259.4375, 333824.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(189092.625, 334486.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(190340.84375, 333553.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(189458.328125, 333373.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(189812.421875, 332120.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(190191.140625, 333447.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(190193.265625, 333815.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(189258.6875, 334007.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(189251.421875, 332960.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(190771.71875, 333473.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(190469.421875, 333653.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(189266.28125, 333962.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(190255.015625, 333570.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(190310.671875, 333577.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(189236.625, 332953.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(190508.15625, 333683.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(189126.109375, 333868.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(189266.140625, 332967.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(189442.4375, 333369.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(189568.953125, 333385.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(190476.078125, 332491.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(190052.21875, 334349.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(189322.890625, 334109.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(190495.21875, 333673.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(189381.59375, 332347.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(189433.71875, 332309.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(189666.71875, 334589, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(190278.671875, 333575.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(189114.15625, 333948.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(190231.578125, 333565, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(189221.828125, 332947.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(189334.9375, 334028.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(189119.09375, 333916.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(189196.625, 332151.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(189101.140625, 334051.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(189385.921875, 332703.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(190396.5625, 333515.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(189200.578125, 332962.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(189103.390625, 334035.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(189337.390625, 333921.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(189280.953125, 332973.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(190092.671875, 334106.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(189829.71875, 332150, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(189109.140625, 333981.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(189096.421875, 334084.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(189107.671875, 334520.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(190507.5, 332483.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(189310.59375, 332986.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(189317.953125, 334141.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(189123.734375, 333884.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(189295.78125, 332980.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(190803.484375, 333457.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(189209.53125, 332141.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(190743.3125, 333458.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(189356.34375, 332690.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(190369.71875, 333532.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(189320.546875, 334125.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(189341.234375, 333898.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(189116.78125, 333932.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(189489.953125, 333380.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(189570.203125, 333495.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(189156.390625, 332179.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(189235.59375, 332122.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(190515.109375, 333611.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(189430.375, 332723.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(189446.734375, 332299.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(189394.765625, 332338.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(189327.75, 334077.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(189170.578125, 332170.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(189337.28125, 334012.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(189098.734375, 334068.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(190065.71875, 334089.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(189111.84375, 333965.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(189183.546875, 332160.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(190422.765625, 333500.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(190530.328125, 333632.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(190062.296875, 334051, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(189332.46875, 334045.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(189325.40625, 334093.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(189474.171875, 333377, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(190068.140625, 334398.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(189407.671875, 332328.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(189400.703125, 332710.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(189420.75, 332318.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(189415.59375, 332716.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(189222.59375, 332131.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(189100.125, 334503.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(190028.84375, 334328.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(189330.125, 334061.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(189136.90625, 332225.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(189234.8125, 331978.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(190205.484375, 333559.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(189369.4375, 332384.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(189105.75, 334019.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(189621.953125, 333398.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(189333.625, 333945.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(190157.765625, 333464.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(189128.53125, 333851.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(189108.171875, 334003.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(189371.203125, 332697, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(189121.484375, 333900.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(188946.921875, 334037.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(189194.75, 331925.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(190152.90625, 333496.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(189320.234375, 332698.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(189122.734375, 334553.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(189143.28125, 332188.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(188952.171875, 334191.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(189659.96875, 334558.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(190384.734375, 333616.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(190482.203125, 333663.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))


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
                crossroad_idx=0, position=mapping.Point(198236.4375, 341364.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(197325.90625, 342481.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(199613.1875, 341006.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(197711.453125, 340734.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(199187.515625, 341531.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(198648.796875, 340890.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(199656.3125, 341027.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(198011.109375, 342098.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(198394.5, 342013.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(197384.0625, 342686.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(197119.125, 340954.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(199189.734375, 341466.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(198613.359375, 340126.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(198408.8125, 342005.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(198495.59375, 341494.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(197978.03125, 342062.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(198482.140625, 340237.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(198959.28125, 341459.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(197130.5, 340943.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(198282.078125, 341412.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H29', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(198021.890625, 342111.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(197688.109375, 340712.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(199670.8125, 341034.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(198470.90625, 341437.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(198785.5, 341526.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(199179.09375, 340992.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(198450.015625, 341458.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(198665.40625, 340249.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(196930.71875, 340935.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(197407.015625, 342593.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(197643.0625, 340708.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(198495.21875, 340201.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(198744.59375, 340340.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(197020.96875, 342451.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(199205.328125, 340963.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(198474.015625, 341515.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(199188.671875, 341499, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(197775.78125, 340469.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(197164.796875, 340908.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(198450.65625, 341980.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(197000.59375, 342476.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(197842.296875, 340779.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(198452.1875, 341537.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(198170.0625, 340061.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(198805.1875, 341482.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(198619.015625, 340753.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(197848.015625, 340764.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(197521.21875, 342515.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(196945.546875, 340922.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(198827.03125, 341332.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(198822.59375, 341451.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(198639.84375, 340730.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(199627.3125, 341014.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(198428.171875, 341480.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(197870.734375, 340703.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(198492.421875, 341416.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(198228.8125, 341464, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(197080.265625, 340870.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(196959.359375, 342527.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(197528.40625, 342450.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(198728.578125, 340806.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(197966.84375, 342051.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(198161.65625, 341391.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(197804.859375, 340471.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(198561.171875, 341433.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(199598.265625, 341001.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(198541.171875, 340986.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(198212.90625, 341341.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H32', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(198757.5625, 340303.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(197337.078125, 342493.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(198688.171875, 340848.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(197348.640625, 342631.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(196969.671875, 342514.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(198517.359375, 341474.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(197141.953125, 340931.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(197516.125, 342561.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(198865, 341331.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(197348.21875, 342505.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(198669.171875, 340868.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(198605.96875, 340164.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(198957.359375, 341525.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(197865.09375, 340718.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(198436.59375, 341988.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(198957.1875, 341541.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(197523.65625, 342493.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(198958.4375, 341492.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(199685.390625, 341041.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(197518.640625, 342540.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(198251.140625, 341486.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(198184.359375, 341415.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(199190.0625, 341450.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(197966.65625, 340067.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(197153.453125, 340920.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(196980.0625, 342501.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(197281.484375, 342434.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(197525.984375, 342471.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(196915.765625, 340950.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(198958.859375, 341476.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(199189.0625, 341482.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(197966.765625, 340098.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(198798.515625, 341497.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(198422.65625, 341997, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(198959.734375, 341443.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(198497.203125, 340946.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(199187.390625, 341548, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(198464.953125, 341972.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(197314.859375, 342469.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(197853.703125, 340749, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(198000.265625, 342086.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(197292.53125, 342446.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(198206.53125, 341439.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(197956, 342039.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(197303.53125, 342458.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(198599.484375, 340774.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(197040.015625, 340869.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(198579, 340795.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(197265.15625, 342681.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(198678.609375, 340212.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(197836.53125, 340794.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(199035.90625, 340937.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(197010.796875, 342464.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(196990.28125, 342489.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(198169.484375, 340093.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(198475.5625, 340927.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(198997.234375, 340870.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(198792.140625, 341512.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(198380.140625, 342020.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(198707.421875, 340827.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(198969.59375, 340897.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(197859.421875, 340733.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(198558.75, 340817.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(197244.03125, 342692.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(198259.5, 341388.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(197988.953125, 342074.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(198958.03125, 341508.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(197327.53125, 342642.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(198519.84375, 340966.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(198583.265625, 341412.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(197060.171875, 340869.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(197436.359375, 342660.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(199188.34375, 341515.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(198303.796875, 341435.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(199074.984375, 340938.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(198660.671875, 340708.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))


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

        self.runways.append(Runway(id=3, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[RunwayBeacon(id='airfield24_2', runway_name='08-26', runway_id=3, runway_side='08'), RunwayBeacon(id='airfield24_7', runway_name='08-26', runway_id=3, runway_side='08')]), opposite=RunwayApproach(name='26', heading=260, beacons=[RunwayBeacon(id='airfield24_8', runway_name='08-26', runway_id=3, runway_side='26'), RunwayBeacon(id='airfield24_0', runway_name='08-26', runway_id=3, runway_side='26')])))
        self.runways.append(Runway(id=2, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[RunwayBeacon(id='airfield24_1', runway_name='30-12', runway_id=2, runway_side='30'), RunwayBeacon(id='airfield24_6', runway_name='30-12', runway_id=2, runway_side='30')]), opposite=RunwayApproach(name='12', heading=120, beacons=[RunwayBeacon(id='airfield24_5', runway_name='30-12', runway_id=2, runway_side='12'), RunwayBeacon(id='airfield24_9', runway_name='30-12', runway_id=2, runway_side='12')])))
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
    atc_radio = AtcRadio(hf_hz=4175000, vhf_low_hz=39250000, vhf_high_hz=124500000, uhf_hz=250850000)

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
                airplanes=True, slot_name='10', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(109849.1015625, 247478.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(109803.7109375, 247498.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(109757.375, 247518.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=41.0, width=41.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='16', length=60.0, width=60.0, height=18.0, shelter=False))


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
                crossroad_idx=1, position=mapping.Point(110292.875, -53071.88671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(112732.734375, -54250.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(111993.109375, -54098.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(109939.6328125, -53241.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(110067.921875, -53002.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(111917.390625, -54062.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(112992.0078125, -54012.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(113004.9609375, -54080.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(111576.625, -53827.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(112442.8984375, -53813.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(112866.6328125, -54292.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(110159.1171875, -53326.93359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(110078.875, -53301.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(111431.8125, -53767.9921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(112898.5703125, -53992.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(111939.4453125, -53960.01953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(110002.2578125, -53291.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(111972.1640625, -54141.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(112355.1875, -53764.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(111895.6640625, -54105.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(112805.4609375, -54310.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(112062.390625, -54017.04296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=18.0, width=15.0, height=8.0, shelter=False))


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

        self.runways.append(Runway(id=3, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.runways.append(Runway(id=2, name='36L-18R', main=RunwayApproach(name='36L', heading=360, beacons=[]), opposite=RunwayApproach(name='18R', heading=180, beacons=[])))
        self.runways.append(Runway(id=1, name='36R-18L', main=RunwayApproach(name='36R', heading=360, beacons=[RunwayBeacon(id='airfield33_1', runway_name='36R-18L', runway_id=1, runway_side='36R'), RunwayBeacon(id='airfield33_0', runway_name='36R-18L', runway_id=1, runway_side='36R')]), opposite=RunwayApproach(name='18L', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-93605.359375, -23878.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-93654.8984375, -23886.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-93874.3359375, -23925.052734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-93511.28125, -24030.505859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-93328.28125, -23911.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-92303.8828125, -24828.607421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-93163.8515625, -23923.736328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-95308.78125, -24094.142578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-93949.4609375, -23937.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-95732.9375, -24234.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-92155.765625, -23508.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-93379.5703125, -24048.298828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-93507.2890625, -23862.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-93581.140625, -23874.294921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-92931.578125, -24293.541015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-95504.21875, -24203.20703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-92239.8125, -22788.08984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-93013.90625, -23739.03515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-95092.171875, -24477.193359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-95149.5546875, -24013.869140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-93752.5859375, -23903.759765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-93898.96875, -23928.873046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-93924.3984375, -23933.736328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-94652.8359375, -24063.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-92373.2109375, -23676.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-91979.21875, -22783.283203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-92811.2890625, -24262.619140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-92546.0390625, -23663.123046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-92650.6171875, -22868.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-92348.8359375, -24896.927734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-92314.6328125, -24845.544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-95429.3828125, -23384.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-94805.890625, -23971.439453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-93556.3203125, -23870.654296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-93850.1328125, -23920.259765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-92955.515625, -24256.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-91427.078125, -22722.451171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-92378.1171875, -22752.208984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-93107.640625, -23841.501953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-93826.296875, -23917.408203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-91627.921875, -22638.470703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-94522.046875, -24040.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-95520.3359375, -23486.349609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-95341.1171875, -23342.216796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-93703.484375, -23895.275390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-92069.7734375, -22660.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-92336.5546875, -24879.259765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-94999.7109375, -24078.521484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-93532.0546875, -23866.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-93800.9375, -23912.251953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-91238.8359375, -22691.40234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-93141.96875, -23741.130859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-92738.2421875, -23809.634765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-93630.3828125, -23882.130859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-93678.953125, -23891.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-93776.796875, -23908.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-95539.625, -24494.498046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-91843.84375, -22751.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-92343.984375, -23556.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-95232.03125, -23379.166015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-95370.40625, -24216.642578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-93727.78125, -23899.564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-92659.578125, -23787.869140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-95572.015625, -23357.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-95068.3359375, -24137.38671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-92232.3984375, -23598.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-95118.53125, -24457.26171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-92325.4921875, -24862.275390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-93386.2265625, -23920.236328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-95669.4296875, -23401.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=14.0, height=6.0, shelter=False))


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
                crossroad_idx=9, position=mapping.Point(88862.767141685, -29251.893057982, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(88987.948128772, -29275.679051183, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(88961.020027577, -29149.637558688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(88817.909127233, -29033.160105399, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=23, position=mapping.Point(87583.019951219, -28118.997817801, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(87424.0078125, -28057.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=8, position=mapping.Point(98761.7890625, -145492.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(98821.8984375, -145577.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(98920.171875, -145604.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(98981.25, -145701.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(99067.1796875, -145783.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(98694.375, -146165.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(98599.15625, -146157.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(98544.15625, -146070.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(98389.96875, -146015.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(98331.765625, -145934.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(100594.9765625, -147518.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(100630.71875, -147607.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(100736.2734375, -147623.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(100833.8125, -147755, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(100929.8671875, -147778.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=0, position=mapping.Point(-213455.59375, -54584.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=15, position=mapping.Point(-216358.09375, -53466.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-213556.28125, -54568.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=24, position=mapping.Point(-216388.1875, -53386.39453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=28, position=mapping.Point(-216265.125, -53504.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-216154.578125, -53503.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=34, position=mapping.Point(-213751.078125, -54479.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-215513.234375, -53126.40234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-213651.890625, -54499.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=45, position=mapping.Point(54556.03515625, -65318.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(54544.98046875, -65224.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(54516.45703125, -64732.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(54637.70703125, -64721.76171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(54831.6875, -64768.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(54779.578125, -64546.14453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(54920.6015625, -64582.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(54510.1328125, -63911.87109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(54453.41015625, -63804.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(54440.9765625, -63701.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(54376.640625, -63610.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=67, position=mapping.Point(54616.58984375, -64572.46484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
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
                airplanes=True, slot_name='71', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-318672.875, 249023.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=60.0, width=52.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='74', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-318852.59375, 249079.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-319618.0625, 249427.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-320505.5625, 249476.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=14.0, height=6.0, shelter=False))
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
                airplanes=True, slot_name='86', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-318993.6875, 248941.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-317618.65625, 248832.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-318934.5625, 249097.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=60.0, width=52.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='75', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-319645.09375, 249331.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-319629.3125, 249385.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-318343.21875, 248248.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-320409.21875, 249475.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=14.0, height=6.0, shelter=False))
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
                airplanes=True, slot_name='82', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-320639.125, 249536.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-319548.78125, 249364.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=40.0, width=38.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='51', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-319039.9375, 248953.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-317908.125, 248910.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-319704.00530062, 249405.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=40.0, width=38.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='77', length=40.0, width=38.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='52', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-318671.53125, 248844.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=60.0, width=52.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='81', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-320738.34375, 249530.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.0, width=14.0, height=6.0, shelter=False))
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
                airplanes=True, slot_name='87', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-319563.96875, 249310.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-319537.875, 249406.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=40.0, width=38.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='54', length=60.0, width=52.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='73', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-318756.375, 249035.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=60.0, width=52.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='76', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-319090, 249136.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=60.0, width=52.0, height=18.0, shelter=False))
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
                crossroad_idx=29, position=mapping.Point(87390.296875, -97693.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(87286.4765625, -97656.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=51, position=mapping.Point(87350.734375, -97656.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=66, position=mapping.Point(87430.9375, -97741.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=14.0, height=6.0, shelter=False))
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
                crossroad_idx=0, position=mapping.Point(-34470.75390625, 363764.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-34778.09375, 363578.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-34512.13671875, 363642.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-35544.6640625, 363528.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-34394.8359375, 363783.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-34904.2265625, 363509.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-35198.6640625, 363458.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-35276.74609375, 363440.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-35647.89453125, 363504.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-34279.98046875, 363695.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-35470.75390625, 363543.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-35475.16015625, 363392.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-35607.61328125, 363349.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-34319.26171875, 363686.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-35530.82421875, 363436.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-34737.8125, 363587.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-35006.2421875, 363666.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-35081.5859375, 363649.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-34525.0703125, 363752.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-35247.43359375, 363612.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-35678.69140625, 363367.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-34590.5234375, 363625.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-35046.0390625, 363492.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-35508.03515625, 363535.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-34434.47265625, 363660.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-35159.36328125, 363632.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-34853.8828125, 363521.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-35686.63671875, 363403.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-34584.05859375, 363738.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-34630.3125, 363616.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-35516.0546875, 363373.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-35723.82421875, 363488.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-35755.85546875, 363343.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-35670.7734375, 363333, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-35767.7734375, 363396.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-34879.4609375, 363515.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-35761.734375, 363369.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-34472.484375, 363651.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-35482.77734375, 363441.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-34695.3671875, 363713.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-34551.11328125, 363633.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-35615.2265625, 363383.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-35365.7265625, 363420.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-35110.67578125, 363478.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-34358.81640625, 363677.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-35750.08984375, 363318.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-35321.765625, 363595.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-35621.68359375, 363412, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-34670.03125, 363607.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-35685.17578125, 363496.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-35773.84375, 363423.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-34641.9296875, 363725.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-34958.8671875, 363516.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=60.0, width=52.0, height=18.0, shelter=False))


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
                crossroad_idx=0, position=mapping.Point(-118430.78125, 43087.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-119692.7734375, 42686.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-117880.78125, 43172.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-120393.984375, 42506.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-121298.78125, 42356.88671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-120147.390625, 42570.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-118767.0078125, 43002.06640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-117874.703125, 43146.83203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-118879.3515625, 42971.26953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-117893.2734375, 43219.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-121897.0703125, 42215.01953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-120189.890625, 42559.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-119529.6015625, 42728.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-118193.5546875, 43112.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-119457.9921875, 42747.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-118655.875, 43030.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-121261.5859375, 41534.17578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-117797.671875, 42487.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-119646.765625, 42698.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-118094.734375, 42219.9609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-119506.0625, 42734.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-118260.9921875, 42176.98828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-120100.6484375, 42582.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-121097.296875, 41573.92578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-119670.234375, 42692.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-120655.5390625, 42506.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-121358.375, 41370.5078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-120348.21875, 42518.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-121886.1015625, 42150.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-120822.109375, 42431.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-118092.6875, 42358.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-120076.2109375, 42588.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-121629, 42412.49609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-119600.5859375, 42710.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-120168.65625, 42564.87109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-121132.2265625, 42402.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-118546.1640625, 43060.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-117929.96875, 42261.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-120325.40625, 42524.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-121134.1953125, 42539.30078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-120302.671875, 42530.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-119480.984375, 42740.86328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-120279.0625, 42536.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-119434.6328125, 42753.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-121463.875, 42452.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-117887.5078125, 43196.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-118424.9765625, 42270.36328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-121631.0625, 42272.16796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-121194.78125, 41411.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-121428.296875, 41487.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-118980.9765625, 42941.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-119623.828125, 42704.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-120370.6640625, 42512.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-121464.3671875, 42315.2890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-118322.109375, 43113.94140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-121030.234375, 41452.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-117909.5234375, 42383.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-120544.9140625, 41701.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-118427.203125, 42132.97265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-120124.78125, 42576.24609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-121299.6328125, 42495.95703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-120930.25, 41613.91015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-120865.765625, 41496.77734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-119577, 42716.24609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-119553.3203125, 42722.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-118258.828125, 42315.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-118031.203125, 43169.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))


class Al_Bahr_al_Ahmar(Airport):
    id = 44
    name = "Al Bahr al Ahmar"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4700000, vhf_low_hz=40300000, vhf_high_hz=119500000, uhf_hz=251900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-388005.78125, 181276.859375, terrain), terrain)

        self.runways.append(Runway(id=1, name='32R-14L', main=RunwayApproach(name='32R', heading=320, beacons=[]), opposite=RunwayApproach(name='14L', heading=140, beacons=[])))
        self.runways.append(Runway(id=2, name='32L-14R', main=RunwayApproach(name='32L', heading=320, beacons=[]), opposite=RunwayApproach(name='14R', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-386771.28125, 180242.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-386559.46875, 180780.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-389533.3125, 182067, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-386866.9375, 180265.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-387375.6875, 181263.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-388478.125, 181980.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-389185.5, 181849.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-388856.1875, 182391.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-387035.34375, 180341, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-389085.84375, 182503.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-387816.03125, 181656.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-386947.9375, 181117.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-388756.9375, 182208.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-386642.4375, 180869.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-386521.125, 180753.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-388978.375, 182382.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-386397.90625, 180614.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-386917.65625, 180298.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-387007, 181037.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-387707.46875, 181640.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-389072.25, 181771.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-386817.625, 180921.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-387002.03125, 180268.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-388868.28125, 182257.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-388248.59375, 182012.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-389387.59375, 181916.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-388380.375, 182099.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-387462.6875, 181323.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-386698.25, 180985.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-389290.5, 181871.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-389012.03125, 181667.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-386876.90625, 180960.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-389505.0625, 181980.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-386459.40625, 180694.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-386675.4375, 180224.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-389172.75, 182482.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-388512.375, 182186.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=12.5, height=5.5, shelter=False))


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


class Rafic_Hariri_Intl(Airport):
    id = 46
    name = "Rafic Hariri Intl"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(420154.5625, 399041.296875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield46_2'))
        self.beacons.append(AirportBeacon(id='airfield46_5'))
        self.beacons.append(AirportBeacon(id='airfield46_0'))
        self.runways.append(Runway(id=1, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[RunwayBeacon(id='airfield46_3', runway_name='03-21', runway_id=1, runway_side='03')]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.runways.append(Runway(id=2, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[RunwayBeacon(id='airfield46_1', runway_name='16-34', runway_id=2, runway_side='16'), RunwayBeacon(id='airfield46_4', runway_name='16-34', runway_id=2, runway_side='16')]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(420174.53443762, 399745.03320639, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(419842.8125, 399790.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(421386.65625, 399706.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(420593.15625, 400418.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(420133.24818708, 399960.65501877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(420224.00337564, 400151.5953794, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(420303.0520269, 400203.81852974, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(421532.75, 399804.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(420838.84375, 400581.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(419831.25, 399857.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(419961.9375, 400011.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(420080.42776957, 399866.91597853, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(421252.21875, 399707.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(420017.53370921, 399835.14138442, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(421111.84375, 399715.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(419819.75, 399922.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(420393.96875, 399734.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(420239.125, 399739.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(419972.53125, 399949.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(421395.40625, 399800.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(420073.89694945, 399946.21360683, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(420730.9375, 399740.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(420169.87124571, 399872.24352, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(420940.53125, 399735.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(421524.65625, 399708.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(420355.4227864, 400240.06852974, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(419990.51367469, 399786.41034087, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(420422.15625, 399739.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(421530.0625, 399772.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(420081.87725113, 399725.8795701, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(421535.21875, 399836.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(420084.5625, 400088.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(421527.625, 399740.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(420321.72310185, 399734.49485497, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(420656.9375, 400462.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(420146.125, 400102.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(421522.1875, 399676.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(421025.34375, 399725, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(420518.5, 399740.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(421190.375, 399713.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(420473.5625, 399734.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(420812.65625, 399733.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(420894.53125, 400618.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(420044.28125, 400060.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(421398.84375, 399846.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(421391.375, 399752.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(421519.6875, 399644.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(421383, 399658.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(420029.46116355, 399733.69673197, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=36.0, width=36.0, height=15.0, shelter=False))


class Tabuk(Airport):
    id = 47
    name = "Tabuk"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=42150000, vhf_high_hz=125900000, uhf_hz=229400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-181719.304688, 522694.640625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield47_1'))
        self.runways.append(Runway(id=2, name='24R-06L', main=RunwayApproach(name='24R', heading=240, beacons=[RunwayBeacon(id='airfield47_2', runway_name='24R-06L', runway_id=2, runway_side='24R')]), opposite=RunwayApproach(name='06L', heading=60, beacons=[])))
        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[RunwayBeacon(id='airfield47_3', runway_name='13-31', runway_id=1, runway_side='31'), RunwayBeacon(id='airfield47_0', runway_name='13-31', runway_id=1, runway_side='31')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-181663.515625, 522132.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-181105.6875, 524840.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-181226.9375, 522797.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-180604.96875, 527616.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='161', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-181114.421875, 524704.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-181290.546875, 524221.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-181290.125, 524358.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-181310.828125, 524157, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-181274.46875, 523976.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-181234.28125, 527271.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='142', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-181265.84375, 527194.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='140', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-180625.71875, 527105.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='151', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-180553.609375, 527241.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='156', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-181595.46875, 523719.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-181783.625, 522272.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-181337.265625, 523934.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-179689.703125, 527366.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='171', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-179725.796875, 527351.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='170', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-180938.59375, 527045.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='147', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-181298.28125, 522880.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-181522.046875, 523747, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-181429.703125, 523930.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-181463.296875, 526954.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='139', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-180988.53125, 525072.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='86', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-181253.03125, 524505.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-180792.625, 527062.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='149', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-181300.484375, 523989.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-180787.015625, 527489.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='158', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-182800.09375, 524363.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-181547.890625, 523695.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-182428.734375, 524554.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-180979.09375, 527721.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='159', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-182054.34375, 524515.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-181390.921875, 524007.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-181457.421875, 523875.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-182198.640625, 524396.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-181451.390625, 524005.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-181477.25, 523954.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-182302.125, 524649.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-181218.484375, 527307.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='143', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-181468.875, 521905.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-182339.859375, 525170.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-181127.4375, 524679.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-182407.765625, 524119.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-182605.09375, 524619.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-181729.234375, 523212.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-181139.375, 524655.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-181186.03125, 524675.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-179647.75, 527382.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='172', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-181041.109375, 524969.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-182533.34375, 524034.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-182102.90625, 524643.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-181015.25, 525020.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-181337.75, 523857.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-182186.09375, 524359.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-181234.4375, 521373.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-182392.125, 524123.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-181534.96875, 523721.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-181560.828125, 523669.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-180641.90625, 527732.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='164', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-181154.0625, 524738.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-182138.65625, 524039.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-180635.109375, 521913.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-180664.40625, 527813.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='166', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-181014.4375, 526869.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='146', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-180947.046875, 524931.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-181624.890625, 522087.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-181249.921875, 527235.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='141', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-181259.765625, 522836, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-182519.25, 524155.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-181079.875, 524891.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-181277.203125, 524384.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-181425.5625, 524057.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-181438.484375, 524031.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-182262.625, 525140.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-181403.859375, 523981.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-181230.34375, 524583.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-182044.515625, 524489.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-181275.90625, 524561.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-182512.9375, 524052.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-182524.109375, 524184.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-181131.96875, 527579.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='160', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-181584.984375, 522040.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-181470.34375, 523850.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-182411.171875, 524537.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-181236.75, 524028.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-182528.71875, 524212.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-180671.125, 521955.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-180619.515625, 527657.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='162', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-179837.203125, 527301.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='167', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-182317.359375, 524021.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-182423.71875, 524115.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-181250.640625, 523963.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-181164.8125, 524716.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-182515.078125, 524130.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-181651.015625, 523121.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-180743.75, 522040.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-181702.21875, 522177.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-181744.90625, 522227.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-181202.390625, 524570.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-181257.921875, 524266.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-181569.640625, 523770.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-180189.28125, 526988.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-180630.6875, 527694.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='163', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-181176.078125, 524556.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-181621.34375, 523667.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-182609.03125, 524541.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-180652.109375, 527097.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='150', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-182154.6875, 524283, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-180538.03125, 527188.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='154', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-182074.671875, 524567.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-182602.828125, 524658.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-182117.21875, 524029.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-182064.296875, 524541.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-180653.390625, 521934.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-182412, 525200.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='136', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-182084.453125, 524593.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-181303.15625, 521597.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-181054.03125, 524943.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-181496.1875, 523798.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-181225.546875, 524492.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-181193.640625, 524521.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-182554.9375, 524988.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-181361.6875, 523870.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-180741.84375, 521123.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-181182.9375, 527383.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='145', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-181690.515625, 523167.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-181102.125, 524729.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-181175.5, 524696.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-180708.703125, 521998.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-182492.84375, 524069.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-182452.859375, 525218.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='137', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-181151.03125, 524632.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-182093.75, 524618.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-180615.96875, 521892.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-181066.953125, 524917.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-181311.625, 523845.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-182095.90625, 524019.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-182610, 524497.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-180600.59375, 527113.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='152', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-181768.28125, 523258.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(-181464.34375, 523979.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-180562.625, 527267.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='157', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-181378, 524033.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-181416.78125, 523956.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-180864.171875, 521253.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-180690.546875, 521976.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-181257.4375, 524597.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-180900.765625, 524989.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='88', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-182376.0625, 525185.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-181221.671875, 524532.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-181336.59375, 522925.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-181582.5625, 523745.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(-181202.78125, 527343.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='144', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(-180816.53125, 527055.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='148', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(-182598.15625, 524702.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(-182212.703125, 524433.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(-182257.765625, 524935.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(-182303.71875, 525155.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='133', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(-182282.609375, 524671.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(-181002.328125, 525046.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='85', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(-182227.9375, 524475.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(-181028.1875, 524994.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(-182510.453125, 524102.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(-182172.15625, 524323.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(-182205.375, 524184.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(-182034.640625, 524463.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(-182606.8125, 524580.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(-181507.625, 521950.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(-181546.25, 521995.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(-181483.265625, 523824.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(-181573.75, 523643.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(-179797.078125, 527319.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='168', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(-180651.5625, 527770.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='165', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(-180544.875, 527215.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='155', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(-180725.75, 522019.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(-181248.296875, 524547.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(-180573.8125, 527121.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='153', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(-181092.765625, 524866.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(-181608.421875, 523693.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(-181509.125, 523772.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(-179761.75, 527336.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='169', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(-181473.921875, 526931.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='138', length=26.0, width=22.0, height=11.0, shelter=False))


class Damascus_Intl(Airport):
    id = 48
    name = "Damascus Intl"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=40950000, vhf_high_hz=118500000, uhf_hz=226100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(375326.765625, 495740.890625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield48_3'))
        self.beacons.append(AirportBeacon(id='airfield48_5'))
        self.beacons.append(AirportBeacon(id='airfield48_6'))
        self.runways.append(Runway(id=2, name='05L-23R', main=RunwayApproach(name='05L', heading=50, beacons=[]), opposite=RunwayApproach(name='23R', heading=230, beacons=[RunwayBeacon(id='airfield48_4', runway_name='05L-23R', runway_id=2, runway_side='23R'), RunwayBeacon(id='airfield48_0', runway_name='05L-23R', runway_id=2, runway_side='23R')])))
        self.runways.append(Runway(id=1, name='05R-23L', main=RunwayApproach(name='05R', heading=50, beacons=[RunwayBeacon(id='airfield48_1', runway_name='05R-23L', runway_id=1, runway_side='05R'), RunwayBeacon(id='airfield48_2', runway_name='05R-23L', runway_id=1, runway_side='05R')]), opposite=RunwayApproach(name='23L', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(377305.90625, 496216.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(376734.84375, 496392.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(375162.59375, 494677.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(376831.125, 496504.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(376541.09375, 497468.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(377112.59375, 496142.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(377480.46875, 495965.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(377362.90625, 496147.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(377265.90625, 496016.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(374108.9375, 495111.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(377162.6875, 496107.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(375947.65625, 497175.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(377206.84375, 496056.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(376976.40625, 496621.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(377463.125, 496115, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(376055.9375, 497122.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(376370.09375, 497433.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(376821.0625, 496767.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(377252.15625, 496310.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(377015.78125, 496215.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(376780.96875, 496552.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(374593.90625, 494071.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(374033.59375, 494930.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(376293.03125, 495975.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(377031.375, 496569.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(376084.71875, 497131.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(377042.34375, 496267.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(373699.53125, 494593.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(376883.3125, 496454.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(377375.46875, 495944.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(377481.375, 495915.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(374040.40625, 494959.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(373664.96875, 494727.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(377308.90625, 495965.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(377007.75, 496328.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(376510.90625, 497466.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(376345.1875, 496031.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(375075.53125, 494585.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(374637.875, 494117.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(376871.78125, 496720.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(377433.21875, 495795.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(376924.40625, 496669.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(376389.34375, 497536.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(373692.3125, 494564.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(374571.9375, 494048.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(375119.40625, 494632.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(373763.4375, 494744.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(375877.375, 497098, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(376954.78125, 496207.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(375097.34375, 494608.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(374010.9375, 495091.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(377096.8125, 496253.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(374682.03125, 494164.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(376786.9375, 496343.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(376837.03125, 496295.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(376221.8125, 496035.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(375141.5625, 494655.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(374549.875, 494025, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(376620.09375, 496443.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(377080.90625, 496318.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(377384.84375, 495794.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=36.0, width=36.0, height=15.0, shelter=False))


class Mezzeh_Air_Base(Airport):
    id = 49
    name = "Mezzeh Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4450000, vhf_low_hz=41350000, vhf_high_hz=126000000, uhf_hz=227200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(383579.703125, 468789.203125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield49_0'))
        self.runways.append(Runway(id=1, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(382787.625, 467889.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(383947.34375, 469844.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(383964.125, 469172.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H29', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(383779.28125, 469485.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(383348.3125, 468959.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H46', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(383998.375, 468999.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(383841.21875, 469346.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(383170.3125, 468964.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H48', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(384024.375, 469043.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(384291.34375, 469237.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(384157.59375, 469088.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H32', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(383973.90625, 469151.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H28', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(382816.84375, 467888.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(383737.78125, 469576.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(383259.5, 467852.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(383142.21875, 468859.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H50', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(384267.71875, 470193.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(384015.03125, 469062.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(383181.90625, 467609.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(384033.5, 469021.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(384495.34375, 469982.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(383861.875, 470017.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(383518.9375, 468213.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(383173.6875, 468747.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H52', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(384371.65625, 469424.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H41', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(383373.375, 468851.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H44', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(383386.90625, 467993.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(384307.34375, 469274.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(383164.9375, 468803.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H51', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(384160.40625, 470317.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(383874.21875, 469683.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(383945.125, 469123.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(384341.28125, 469351.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(384103.8125, 469037.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(384275.40625, 469201.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(383390.25, 468796.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H43', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(383692, 469680.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(383470.1875, 469936.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(383818.8125, 469396.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(384005.375, 469080.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(383760.1875, 469526.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(383666.78125, 470032.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(383657.9375, 469758.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(383935.4375, 469145.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(384507.375, 470010.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(383168.15625, 467635.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(383359.4375, 468906.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H45', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(384323.09375, 469311.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(383801.6875, 469435.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(384096.15625, 469954.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(384007.9375, 468979.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(384187.5, 468991.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(383989.53125, 469019.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(383367.28125, 467859.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(383231.28125, 468716.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H53', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(383983.90625, 469131.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(383298.6875, 468992.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H47', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(384356.53125, 469388.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H40', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(384399.78125, 469673.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(383646.15625, 469783.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(383703.78125, 469654.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(383668.5625, 469733.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(383136.375, 468914.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H49', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(383830.59375, 469371.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(384209.6875, 469017.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(383714.375, 469630.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(383955.65625, 469100.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(384131.40625, 469063.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(383505.09375, 468099.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(383791.0625, 469460.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(383749.5625, 469551.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(383979.6875, 469039.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(383351.03125, 468745.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H42', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(384241.125, 470179.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))


class Ramat_David(Airport):
    id = 50
    name = "Ramat David"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3750000, vhf_low_hz=38400000, vhf_high_hz=118000000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(291107.234375, 374035.84375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield50_0'))
        self.runways.append(Runway(id=2, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.runways.append(Runway(id=3, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(290144.03125, 374487.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(291969.25, 372951.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(291951.75, 373006.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(290720.625, 374846.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(291083.4375, 372090.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(291253.71875, 372333.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(290154.71875, 374518.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(290122.78125, 374426.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(291806.9375, 373207.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(291919.875, 373042.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(291940.875, 373244.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(290326.96875, 374926.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(291286.53125, 372277.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(291772.46875, 373205.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(291928.9375, 373253.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(290802.34375, 372067.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(290921.28125, 373613.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(291378.53125, 373441.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(291930.4375, 373030.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(290730.09375, 374880.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(290772.34375, 372058.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(290292.65625, 374401.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(291941.15625, 373018.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(291259.25, 373467, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(290696.875, 374822.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(290448.65625, 374123.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(291410.84375, 373451.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(290956.875, 374774.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='104', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(290806.96875, 373932.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(290768.125, 373880.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(291361.75, 373011.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(291384.09375, 374612.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(291979.5, 373038.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(290399.46875, 374962.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(290185.8125, 374529.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(290826.4375, 373958.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(290662.03125, 373729.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(291411.3125, 373023.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(291427.875, 374540.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(291880.6875, 373289.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(291259.4375, 373444.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(291092.5, 374788.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(290392, 374828.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(290853.21875, 373960.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(290388.375, 374083.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(291464.28125, 373942.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(291065.8125, 374807.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(290021.09375, 374476.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(290252.78125, 374412, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(291468.9375, 373994.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(291916.78125, 373262.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(290415.03125, 374967.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(290278.28125, 374897.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(290787.875, 373906.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(290638.34375, 373706.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(291475.375, 374073.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(291464.0625, 374209.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(291336.6875, 374681.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(290061.375, 374595.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(290816.6875, 373945.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(290428.21875, 374097.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(290924.59375, 373580.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(291472.8125, 374112.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(291260.8125, 373418.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(290149.34375, 374503.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(290231.75, 374387.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(291468.4375, 374177.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(291952.9375, 373235.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(291461.21875, 374232.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(290011.0625, 374451.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(290778.125, 373893.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(291330.125, 373020.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(291473.0625, 374044.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(291957.9375, 373062.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(291269.21875, 373298.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(291868.625, 373297.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(291107.25, 372087.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(290031.375, 374504.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(291470.90625, 374146, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(291264.34375, 373360.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(291457.03125, 374253.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(290186.5, 374387.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(290743.34375, 372049.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(290043.5, 374533.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(291453.25, 373436.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(291263.4375, 373379.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(291450.625, 374276.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(291744.1875, 372915.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(291302.75, 372249.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(290053.40625, 374569.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(291909.125, 373054.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(291262, 373399.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(291444.1875, 374299.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(291767.8125, 372888.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(291267.15625, 372366.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(290069.5625, 374623.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(290797.4375, 373919.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(292004.5625, 372982, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(291359.9375, 374646.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(291968.75, 373050.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(291856.53125, 373307.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(290937.90625, 374746.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='103', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(290831.875, 372076.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(291270.25, 372305.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(290078.8125, 374649.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(290897.8125, 373550.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(291406.40625, 374577.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(291973.09375, 372981.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(291904.75, 373271.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(290301.96875, 374912.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(291278.65625, 372292.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(290378.6875, 374861.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(290128.03125, 374442, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(291738.75, 373167.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(291892.75, 373280.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(291294.78125, 372263.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(291262.15625, 372320.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(290419.78125, 374799.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(290138.625, 374472.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(291466.34375, 373968.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(291764.3125, 372838.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(290860.3125, 372086.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(290133.4375, 374457.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(291471.1875, 374018.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(291962.5, 372993.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=12.5, height=5.5, shelter=False))


class Megiddo(Airport):
    id = 51
    name = "Megiddo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4975000, vhf_low_hz=41150000, vhf_high_hz=123000000, uhf_hz=225900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(283509.78125, 378523.125, terrain), terrain)

        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(283236.5625, 379203.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(283311.1875, 379240.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(283660.53125, 379536.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(283254.78125, 379284.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(283628.34375, 378899.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(283394.46875, 379013.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(283436.125, 378943.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(283285, 379188.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(283291.8125, 379201.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(283699.0625, 379521.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(283364.84375, 379031.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(283397.5625, 378967.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(283605.125, 378941.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(283411.28125, 379497.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(283391.625, 377857.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(283718.90625, 379513.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(283273.78125, 379164.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(283353.1875, 379469.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(283568.125, 378832.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(283335.96875, 379049.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(283552.34375, 378847.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(283266.71875, 379150.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(283254.125, 379058.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(283445.1875, 377290.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(283239.59375, 379066.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(283329.40625, 379279.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(283377.25, 378981.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(283428.90625, 377290.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(283379.46875, 379023.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(283268.09375, 379049.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(283245.09375, 379270, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(283322.25, 379264.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(283281.9375, 377924.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(283755.09375, 379499.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(283774.25, 379491.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(283587.125, 378823, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(283319.3125, 379015.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(283679.5625, 379528.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(283338.8125, 379004.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(283019.3125, 378393.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(283060.3125, 378679, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(283367.65625, 379487.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(283412.625, 377290.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(283264.21875, 379298.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(283292.96875, 379074.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(283322.25, 379057.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(283282.09375, 379041.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(283417.03125, 378955.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(283396.3125, 377290.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(283307.03125, 379066.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(283181.75, 379127.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(283350.28125, 379040.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(283550.53125, 378966.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(283097.375, 378128.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(283298.75, 379214.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(283358.15625, 378992.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(283191.5625, 379145.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(283576.5, 378872.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(283336.5625, 379294, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(283619.25, 378921.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(283737.3125, 379506.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(283582.4375, 378954.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=14.0, height=6.0, shelter=False))


class Ein_Shamer(Airport):
    id = 52
    name = "Ein Shamer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=41450000, vhf_high_hz=124550000, uhf_hz=227850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(265763.1875, 357945.765625, terrain), terrain)

        self.runways.append(Runway(id=1, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(265827.3125, 358249.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(265832.09375, 358207.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(265839.96875, 358000.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(265842.59375, 357978.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(265813.90625, 357880.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(265785.625, 358153.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(265847.09375, 358097.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(265849.78125, 358075.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(265873.125, 357896.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(265834.84375, 358185.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=18.0, height=8.0, shelter=False))


class Taba_International_Airport(Airport):
    id = 53
    name = "Taba International Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=42200000, vhf_high_hz=121900000, uhf_hz=227150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-50856.566406, 341451.765625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield53_2'))
        self.runways.append(Runway(id=1, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[RunwayBeacon(id='airfield53_1', runway_name='22-04', runway_id=1, runway_side='04'), RunwayBeacon(id='airfield53_0', runway_name='22-04', runway_id=1, runway_side='04')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-50467.16796875, 341271.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-50515.35546875, 341231.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-50060.8515625, 341340.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-50667.43359375, 341105.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-50564.39453125, 341190.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-50109.55859375, 341333.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-50160.7109375, 341326.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-50313.14453125, 341304.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-50612.859375, 341149.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-50009.69140625, 341347.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-50211.7265625, 341319.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-50262.953125, 341311.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=41.0, width=41.0, height=18.0, shelter=False))


class King_Feisal_Air_Base(Airport):
    id = 54
    name = "King Feisal Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4950000, vhf_low_hz=40750000, vhf_high_hz=129200000, uhf_hz=227950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(35757.6875, 471805.875, terrain), terrain)

        self.runways.append(Runway(id=1, name='29-11', main=RunwayApproach(name='29', heading=290, beacons=[RunwayBeacon(id='airfield54_1', runway_name='29-11', runway_id=1, runway_side='29'), RunwayBeacon(id='airfield54_0', runway_name='29-11', runway_id=1, runway_side='29')]), opposite=RunwayApproach(name='11', heading=110, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(34463.5625, 472915.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(35711.89453125, 469925.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(34080.69140625, 473448.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(35690.87109375, 469743.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(34969.1875, 473219.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(35752.2890625, 469605.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(35937.97265625, 470068.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(34455.4453125, 473132, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(35851.00390625, 470612.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(35393.328125, 471901.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(35789.2109375, 470586.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(34468.08984375, 473122.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(34347.6015625, 473100.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(36357.796875, 470093.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(34503.296875, 473223.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(34340.3828125, 473946.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(34722.8671875, 473047.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(34162.125, 473532.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(36093.93359375, 469479.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(35657.75, 470137.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(34626.875, 472831.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(34512.82421875, 472809.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(34901.1875, 473449.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(34200.1015625, 473211.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(36307.94921875, 470046.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(35630.4296875, 469843.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(35780.94140625, 469492.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(35404.28125, 471706.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(35354.81640625, 471991.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(36271.8203125, 470249.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(34912.95703125, 473347.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(35384.24609375, 471922.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(36216.3671875, 470375.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(35364.8125, 471967.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(34805.98046875, 473129.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(34263.08984375, 471412.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(34389.84765625, 473736.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(35383.625, 471699.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(34533.8515625, 473335.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(35932.5390625, 470234.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(34230.9296875, 473098.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(35898.19140625, 469493.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(35708.9453125, 470314.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(34480.1875, 473113.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(35672.18359375, 470703.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(34518.359375, 473085.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(35266.90625, 471641.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(34141.79296875, 473350.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(35725.92578125, 470559.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(36049.2109375, 470238.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(36027.96875, 469576.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(34966.12890625, 473283.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(35403.8359375, 471877.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(36345.65234375, 470081.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(35318.26953125, 471670.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(35615.04296875, 470247.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(34285.3515625, 473683.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(34781.84375, 472947.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(36011.03515625, 469899.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(35646.66015625, 470764.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(35907.89453125, 469956.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(35900.453125, 470346.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(35770.75, 470794.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(36281.11328125, 470166.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(34493.92578125, 473103.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(36333.08203125, 470070, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(34865.69921875, 473449, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(36226.8984375, 470295.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(35021.3203125, 473156.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(36320.0546875, 470057.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(34505.9453125, 473094.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(35374.59375, 471945.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(34833.953125, 473448.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(36203.05859375, 469520.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(34311.421875, 473569.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(34606.45703125, 473166.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(35339.1328125, 471679.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(34882.34765625, 473449.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))


class Khalkhalah_Air_Base(Airport):
    id = 55
    name = "Khalkhalah Air Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4925000, vhf_low_hz=40700000, vhf_high_hz=128400000, uhf_hz=227900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(340303.703125, 499770.65625, terrain), terrain)

        self.runways.append(Runway(id=2, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.runways.append(Runway(id=1, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(339709.84375, 503885.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(339750.875, 502796.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(341532.46875, 499182.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(339625.65625, 502833.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(339974.3125, 499552.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(341518.40625, 498818.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(339410.90625, 502204.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(341791.9375, 499018.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(339898.6875, 503729.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(339951.6875, 503396.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(338908.78125, 500452.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(339285.65625, 502242, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(341326.21875, 498689.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(339587.90625, 504209.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(339925.78125, 503716.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(341558.90625, 499166.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(339558.21875, 502617.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(340010.5, 503141.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(339553.90625, 499809.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(341638.5625, 498735.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(339101.09375, 500667.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(339684.5, 502579.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(339627.875, 503615.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(339834.4375, 504030.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(339148.0625, 500774.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(339896.34375, 499622.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(339714.375, 503856.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(338859.53125, 500271.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(339477.9375, 502421.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(339976.375, 504197.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(341193.40625, 498777.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(341670.75, 499139.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(339533.875, 504225.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(339970.375, 504226.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(339806.1875, 499660.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(339352.40625, 502459.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(339208.84375, 500019.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(339788.625, 504237.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(339464.625, 499864.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(338915, 500423, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(339605.1875, 503595.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(341540.78125, 499289.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(339884.21875, 503179.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(339401.0625, 500780.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(339300.1875, 499966.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(339730.46875, 499734.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(339847.59375, 504057.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(339400.28125, 500750.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(341489.28125, 498812.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(339767.6875, 504258.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(340076.8125, 503357.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(338979.15625, 500150.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.0, width=12.5, height=5.5, shelter=False))


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
    Rafic_Hariri_Intl,
    Tabuk,
    Damascus_Intl,
    Mezzeh_Air_Base,
    Ramat_David,
    Megiddo,
    Ein_Shamer,
    Taba_International_Airport,
    King_Feisal_Air_Base,
    Khalkhalah_Air_Base,
]

