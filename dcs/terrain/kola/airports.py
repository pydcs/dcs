# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Banak(Airport):
    id = 1
    name = "Banak"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=118050000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(234850.039063, 88378.335938, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield1_2'))
        self.beacons.append(AirportBeacon(id='airfield1_3'))
        self.runways.append(Runway(id=1, name='34-16', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='16', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(233864.84375, 88349.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(233847.78125, 88352.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(233830.71875, 88354.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(233813.59375, 88357.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(233796.28125, 88359.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(233779.109375, 88362.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(233762.171875, 88364.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(233745.09375, 88367.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(233728.203125, 88369.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(233710.984375, 88371.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(233694.109375, 88374.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(233677.1875, 88376.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(233660.0625, 88379.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(233642.328125, 88381.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(233625.125, 88384.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(233607.953125, 88386.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(233590.71875, 88389.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(233635.8125, 88251.3671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HC1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(233698.5625, 88078.9140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HC4', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(233680.34375, 88110.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HC3', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(233661.15625, 88141.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HC2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(234597.75, 88657.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='CIV02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(234642.9375, 88650.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='CIV03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(234552.1875, 88664.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='CIV01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(233592.84375, 88164.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(233566.046875, 88208.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M18', length=21.0, width=15.0, height=8.0, shelter=False))


class Rovaniemi(Airport):
    id = 2
    name = "Rovaniemi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=118700000, uhf_hz=250950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-152462.09375, 151503.710938, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield2_1'))
        self.runways.append(Runway(id=1, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[RunwayBeacon(id='airfield2_2', runway_name='21-03', runway_id=1, runway_side='21'), RunwayBeacon(id='airfield2_0', runway_name='21-03', runway_id=1, runway_side='21')]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-153437.71875, 151265.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-153182.484375, 151354.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S07', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-153086.90625, 151560.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-153075.078125, 151602.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-153061.28125, 151652.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-153317.03125, 151282.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-153343.46875, 151265.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-153048.734375, 151698.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-152931.765625, 151583.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S09', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-152185.390625, 151334.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-152169.875, 151346.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-152152.578125, 151357.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-152135.5, 151368.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-152118.203125, 151379.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-152100.796875, 151390.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-152083.921875, 151401.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-152067.671875, 151412.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-151928.9375, 151535.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-151908.953125, 151530.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-151887.15625, 151525.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-151866.40625, 151520.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-151844.28125, 151515.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-151822.0625, 151511.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-151800.46875, 151506.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-151779.1875, 151501.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-151757.171875, 151496.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-151679.625, 151459.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-151557.296875, 151431.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-151284.296875, 151913.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-151302.453125, 151935.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-153665.640625, 150507.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q1', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-153634.703125, 150504.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q2', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-152962.140625, 151502.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S10', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-153099.875, 151516.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-153827.546875, 150911.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Q4', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-153727.453125, 150993.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Q3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-153122.359375, 151410.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-151191.953125, 151831.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-151138, 151805.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-151166.375, 151890.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-151111.96875, 151862.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-153250.078125, 151307.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S08', length=60.0, width=60.0, height=18.0, shelter=False))


class Kemi_Tornio(Airport):
    id = 3
    name = "Kemi Tornio"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4275000, vhf_low_hz=39450000, vhf_high_hz=119400000, uhf_hz=251000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-243395.968891, 101204.631625, terrain), terrain)

        self.runways.append(Runway(id=1, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[]), opposite=RunwayApproach(name='36', heading=360, beacons=[RunwayBeacon(id='airfield3_1', runway_name='36-18', runway_id=1, runway_side='36'), RunwayBeacon(id='airfield3_0', runway_name='36-18', runway_id=1, runway_side='36')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-243722.24928481, 100891.70359519, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-243609.99166752, 100949.13069256, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-243575.53261063, 100950.33763344, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-243476.02836943, 100968.10209483, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-243387.4555893, 100970.34995285, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-243862.19937994, 100771.02116804, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D01', length=26.0, width=24.0, height=11.0, shelter=False))


class Vuojarvi(Airport):
    id = 4
    name = "Vuojarvi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4300000, vhf_low_hz=39500000, vhf_high_hz=118400000, uhf_hz=257100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-93814.804688, 177899.304688, terrain), terrain)

        self.runways.append(Runway(id=None, name='22-4', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='4', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-95322.140625, 176289.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-95337.90625, 176321.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-95310.84375, 176141.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-95292.1640625, 176177.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-95273.28125, 176223.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-95382.65625, 176094.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-95349.2421875, 176098.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-91853.3046875, 179754.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-91846.890625, 179666.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-91868.9453125, 179614.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N01', length=26.0, width=24.0, height=11.0, shelter=False))


class Kiruna(Airport):
    id = 5
    name = "Kiruna"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4325000, vhf_low_hz=39550000, vhf_high_hz=130150000, uhf_hz=251050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-20455.625, -90638.921875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield5_2'))
        self.beacons.append(AirportBeacon(id='airfield5_0'))
        self.runways.append(Runway(id=1, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[RunwayBeacon(id='airfield5_1', runway_name='21-03', runway_id=1, runway_side='21'), RunwayBeacon(id='airfield5_3', runway_name='03-21', runway_id=1, runway_side='21')]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-20098.654296875, -90651.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B5', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-20166.421875, -90807.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B3', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-20297.822265625, -90813.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F1', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-20283.078125, -90804.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F2', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-20268.76171875, -90794.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-20254.142578125, -90784.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F4', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-20240.12890625, -90775.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F5', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-20226.115234375, -90765.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F6', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-20237.404296875, -90748.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F7', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-20463.375, -91018.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H1', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-20114.484375, -90725.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B4', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-20419.1484375, -90913.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B1', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-20322.97265625, -90901.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B2', length=41.0, width=41.0, height=18.0, shelter=False))


class Severomorsk_3(Airport):
    id = 6
    name = "Severomorsk-3"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4350000, vhf_low_hz=39600000, vhf_high_hz=124300000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(148839.246577, 445897.988931, terrain), terrain)

        self.runways.append(Runway(id=1, name='35-17', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='17', heading=170, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(149944.75, 445795.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(148285.84375, 446432.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(148218.046875, 446411.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(147728.71875, 446163.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(147756.203125, 446158.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(147783.671875, 446154.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(147840.984375, 446129.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(147031.5, 445491.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(146912.25, 445510.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(147143.625, 445465.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(147262.65625, 445428.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(147355.375, 445467.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(147702.671875, 446167.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(146714.171875, 445278.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(146954.046875, 445226, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(147052.21875, 445258.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(147156.578125, 445291.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(146527.1875, 445336.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(148150.78125, 446391.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(147897.65625, 446122.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(147953.703125, 446112.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(147875.734375, 446400.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(147822.96875, 446403.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(147770.265625, 446406.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(147715.859375, 446409.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(146475.81548242, 445689.70594003, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(146652.90625, 445730.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(146269.03125, 445745.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(146751.625, 445756.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(147129.453125, 445855.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(147543.546875, 446424.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B50', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(147161.625, 445864.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(147193.484375, 445872.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(147224.625, 445881.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(147256.546875, 445889.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(148349.15625, 446350.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(148378.34375, 446339.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(148408.125, 446329.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(148437.046875, 446319.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(148466.21875, 446309.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(148496.171875, 446301.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(149875.71875, 446126.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(150134.484375, 446025.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(150211.859375, 446047.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(149881.59375, 445805.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(149819.265625, 445815.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(149755.359375, 445825.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(148526.296875, 446290.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(148556.859375, 446279.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(148586.984375, 446268.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(148617.3125, 446258.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(148739.609375, 446222.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(149904, 446121.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(149932.8125, 446117.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(149961.109375, 446112.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(148183.03125, 446401.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(148250, 446422.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(147900.265625, 446332.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(147938.5625, 446330.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(147977.671875, 446328.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(148015.96875, 446326.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(147743.1875, 446407.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(147796.65625, 446405.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(147849.578125, 446401.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(148835.203125, 446189.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(148930.5625, 446155.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(149565.3125, 446101.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(149464.28125, 446106.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(149727.15625, 446078.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(149827.1875, 446062.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(149930.25, 446046.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(149061.515625, 446126.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(149162.46875, 446121.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(149263.28125, 446116.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(149363.953125, 446111.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=26.0, width=24.0, height=11.0, shelter=False))


class Bodo(Airport):
    id = 7
    name = "Bodo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4375000, vhf_low_hz=39650000, vhf_high_hz=118450000, uhf_hz=251150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-66958.882813, -348337.328125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_1'))
        self.beacons.append(AirportBeacon(id='airfield7_3'))
        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[RunwayBeacon(id='airfield7_4', runway_name='07-25', runway_id=1, runway_side='07'), RunwayBeacon(id='airfield7_0', runway_name='07-25', runway_id=1, runway_side='07')]), opposite=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield7_2', runway_name='25-07', runway_id=1, runway_side='25'), RunwayBeacon(id='airfield7_5', runway_name='25-07', runway_id=1, runway_side='25')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-66660.3515625, -348583.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-66653.4296875, -348694.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-66674.0625, -348553.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-66695.0703125, -348550.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-66721.546875, -348603.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-66694.2734375, -348607.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-66715.3125, -348548.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-66734.6953125, -348546.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-66753.109375, -348544.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='GA31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-67271.1015625, -348928.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-67477.546875, -350441.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-67597.625, -350495.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-66772.0859375, -349400.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-66783.171875, -348878.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-66627.5078125, -348101, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-66609.53125, -348032.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-67267.9453125, -348902.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-67264.90625, -348875.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-67329.984375, -348867.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-67333.0703125, -348894.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-67336.046875, -348921.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-67315.75, -348734.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-67318.84375, -348760.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-67321.8125, -348787.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-67256.875, -348795.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-67253.71875, -348768.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-67250.6796875, -348741.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-66607.7265625, -348479.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-66617.1484375, -348364.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-66732.75, -348155.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-67666.8515625, -350574.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-67804.375, -350472.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-67884.359375, -350571.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-67751.6953125, -350349.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-67633.9375, -350352.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-66819.578125, -349141.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-66803.171875, -349032.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-67944.6015625, -350469.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-67956.4453125, -350319.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-67925.4375, -350198.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-67405.4296875, -349966.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-67538.0390625, -349932.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-67528.234375, -350082, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-67594.78125, -349830.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-67797.2109375, -350119.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-67685.6015625, -350164.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-67774.328125, -349929.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='L13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-67668.3671875, -349954.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-67656.125, -349734.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-67399.1875, -349812.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K06', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-67459.2734375, -349735.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-66747.3671875, -348788.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-67603.84375, -349309.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-67412.8828125, -349484.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-67419, -349401.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-67388.5546875, -349319.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-67499.625, -349661.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-67482.28125, -349301.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-67655.9765625, -349559.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-67588.84375, -349652, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-67540.2421875, -349313.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-67339.0078125, -349134.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-67625.671875, -349195.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-67630.7265625, -349093.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-67544.40625, -349225.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-67732.1875, -349335.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-67764.234375, -349233.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-67840.6171875, -348929.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-67139.9765625, -347530.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-67775.2109375, -348824.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-67677.7734375, -348855.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='K26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-67655.3359375, -348760.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-67820.21875, -348757.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-67618.5546875, -348461.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-67438.65625, -348359.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-67190.9296875, -347457, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-67207.8984375, -347366.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-67106.6640625, -347275.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-67061.5546875, -347353.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-66974.8359375, -346630.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-66936.796875, -346466.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-67102.5703125, -346793.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-67174.6015625, -346865.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-67073.921875, -346880.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-67152.9375, -346973.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-67239.5625, -346929.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-67295.921875, -347008.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-67342.0859375, -347096.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-67307.75, -347198.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-67206.1875, -347045.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-67180.5546875, -347167.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-66877.4609375, -349750.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-66936.671875, -349819.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Z01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-66860.5234375, -349641.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W02', length=21.0, width=15.0, height=8.0, shelter=False))


class Severomorsk_1(Airport):
    id = 8
    name = "Severomorsk-1"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4400000, vhf_low_hz=39700000, vhf_high_hz=127800000, uhf_hz=251200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(164318.273438, 430555.578125, terrain), terrain)

        self.runways.append(Runway(id=1, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(166292.328125, 429242.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(166298.75, 429125.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(166284.34375, 429144.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(166270.9375, 429163.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(166257.015625, 429181.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(166171.703125, 429372.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(166243.203125, 429086.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(166228.625, 429104.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(166214.875, 429123.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(166201.4375, 429142.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(166187.5625, 429161.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(166227.53125, 429332.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(166100.71875, 429260.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(166139.03125, 429404.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(166105.09375, 429436.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(166072.296875, 429468.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(166006.5, 429532.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(166039.921875, 429501.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(165764.796875, 429578.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(165726.453125, 429581.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(165688.59375, 429585.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(165651.484375, 429589.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(165551.078125, 429595.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(163802.0625, 430311.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H6', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(163815.375, 430292.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H7', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(163828.546875, 430273.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H8', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(163842, 430254.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H9', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(163876.4375, 430363.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(163890.546875, 430344.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(163903.8125, 430325.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(163916.734375, 430305.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(163775.09375, 430350.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(163788.109375, 430330.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H5', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(163849.171875, 430400.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(163863.28125, 430382.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(164025.765625, 430314.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A19', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(164185.546875, 430233.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A18', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(165921.484375, 429631.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(165919.828125, 429669.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(165918.078125, 429709.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(165916.25, 429748.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(165852.875, 429746.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(165853.734375, 429706.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(165855.40625, 429666.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(165857.765625, 429628.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='W02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(166062.078125, 429320.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(166031.046875, 429349.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(165983.453125, 429361.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(165936.40625, 429445.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(165873.78125, 429458.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(164060.296875, 431391.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(164489.125, 431488.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(164571.296875, 431547.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(164669.203125, 431571.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(164631.234375, 431704.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(164728.3125, 431679.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(164772.703125, 431554.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(164388.15625, 431352.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(164541.609375, 431760.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(164446.625, 431803.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(164640.6875, 429660.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(164565.28125, 429695.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C07', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(164486.125, 429728.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C08', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(164608.109375, 430040.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(163684.734375, 430533.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(163712.53125, 430491.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(163744.5, 430444.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=42.0, width=34.0, height=14.0, shelter=False))


class Olenya(Airport):
    id = 9
    name = "Olenya"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4425000, vhf_low_hz=39750000, vhf_high_hz=131400000, uhf_hz=251250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(68386.710938, 451986.390625, terrain), terrain)

        self.runways.append(Runway(id=1, name='19-01', main=RunwayApproach(name='19', heading=190, beacons=[]), opposite=RunwayApproach(name='01', heading=10, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(66987.6875, 451434.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(67069.234375, 451445.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(67733.1875, 451562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(67656.65625, 451551.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(67582.140625, 451540.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(67507.3359375, 451530.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(67428.921875, 451519.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(67355.3828125, 451508.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(67284.25, 451499.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(67816.7890625, 451606.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(67860.0234375, 451612.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(67903.15625, 451618.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(67946.390625, 451624.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(67988.5546875, 451630.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(68031.7890625, 451636.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(68074.921875, 451642.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(68118.15625, 451648.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(68160.921875, 451654.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(68204.15625, 451660.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(68247.2890625, 451666.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(68290.5234375, 451672.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(68332.6875, 451679.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(68375.9296875, 451685.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(68419.0546875, 451691.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(68462.296875, 451697.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(68505.5, 451702.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(68548.734375, 451708.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(68590.8984375, 451715.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(68634.140625, 451721.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(68677.265625, 451727.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(68720.5078125, 451733.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(68761.296875, 451739.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(68804.4296875, 451745.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(68887.2890625, 451699.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(68943.2421875, 451707.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(68995.6953125, 451715.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(69052.046875, 451723.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(69205.9140625, 451757.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(69251.9453125, 451765.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B13', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(69300.2421875, 451771.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(69347.484375, 451777.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B16', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(69393.8203125, 451784.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B17', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(69193.921875, 451642.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(69207.2734375, 451545.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(70262.65625, 451478.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(70168.59375, 451438.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(70054.4765625, 451432.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(69946.796875, 451430.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(69851.0546875, 451428.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(69728.5625, 451461.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(69680.59375, 451550.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(69623.0078125, 451656.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(69578.421875, 451738.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(69292.5234375, 451220.53014259, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(69284.445589352, 451277.43528518, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(69276.237163735, 451334.02484197, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(69268.31026497, 451390.6280858, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(69260.604628087, 451447.22017468, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(69699.953125, 450826.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(69787.0546875, 450728.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D13', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(69631.4296875, 450904.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(69520.4140625, 450958.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(69417.8046875, 450965.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(69316.8828125, 450972.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(69662.9140625, 451842.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(69793.3984375, 451861.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B19', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(69870.4921875, 451871.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=60.0, width=52.0, height=18.0, shelter=False))


class Monchegorsk(Airport):
    id = 10
    name = "Monchegorsk"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=118250000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(46867.561851, 437312.674304, terrain), terrain)

        self.runways.append(Runway(id=1, name='01-19', main=RunwayApproach(name='01', heading=10, beacons=[]), opposite=RunwayApproach(name='19', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(46124.52734375, 436935.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(46142.1015625, 436937.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(46106.88671875, 436934.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(46177.171875, 436939.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(46194.73828125, 436941.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(46159.42578125, 436938.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(46212.3125, 436942.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(46229.65625, 436943.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(46264.7109375, 436945.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(46247.07421875, 436944.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='K02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(45864.591392535, 437242.44888839, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(46736.31640625, 436790.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(46765.0703125, 436807, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(46707.96484375, 436774.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(46794.51953125, 436824.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(46823.29296875, 436840.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(46857.22265625, 436858.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(47731.046875, 437289.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(47725.20703125, 437308.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(47718.65234375, 437329.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(47712.453125, 437350.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(47706.06640625, 437369.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(47700.15234375, 437390.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(47693.25390625, 437412.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(47687.1328125, 437432.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(47829.71875, 437203.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(47793.59375, 437279.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(48064.234375, 437398.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(48050.82421875, 437382.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(46053.23046875, 436738.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(46024.15625, 436738.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(46911.05078125, 436996.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(46992.6015625, 437044.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(47628.09765625, 437281.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(46914.52734375, 436902.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(46944.18359375, 436919.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(46972.08984375, 436935.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(47002.4921875, 436953.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(47030.703125, 436969.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(47060.3046875, 436986.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(47088.01953125, 437004.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(47116.1953125, 437020.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(47145.0078125, 437037.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(46886.28125, 436885.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(45849.109375, 436660.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(45799.615872456, 436749.71764212, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(46131.99609375, 437271.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(45779.300244836, 436819.83314653, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(45132.1015625, 436312.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(45696.217604629, 436873.66622598, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(45704.534276165, 436845.67919332, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(46451.4375, 436793.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(45685.40625, 437180.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(47317.82421875, 437213.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(47498.2109375, 437104.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(47411.765625, 437233.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(47491.046875, 437256.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(47181.8671875, 437166.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(47251.84765625, 437188.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(47747.87890625, 437211.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(47557.0234375, 437133.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(47933.1796875, 437185.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(47972.66015625, 437224.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(47998.0546875, 437284.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(48042.68359375, 437318.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(47960.27734375, 437397.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(47241.19140625, 437025.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(47302.22265625, 437040.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(47366.73828125, 437062.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(45548.55859375, 437202.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(45522.1796875, 437261.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(45624.0234375, 437301.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(45653.640625, 437242.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(46562.69921875, 436896.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(46486.3671875, 436874.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(46256.0078125, 436760.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(46365.62890625, 436775.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(46161.69921875, 436760.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(46099.4453125, 436755.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(45350.19921875, 436406.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(45402.11328125, 436431, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(45320.21484375, 436524.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(45411.3984375, 436578.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(45460.7734375, 436652.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(45519.41796875, 436683.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(45591.078125, 436681.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='I02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(46258.95703125, 436664.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(46162.6875, 436653.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(45994.78125, 436799.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(45916.9453125, 436800.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(45844.51953125, 436756.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(45983.125, 436644.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(45931.42578125, 436640.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(45792.858298527, 436773.20814653, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(45786.143994836, 436796.33176492, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(45705.42578125, 436711.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='I01', length=20.0, width=14.0, height=6.0, shelter=False))


class Jokkmokk(Airport):
    id = 11
    name = "Jokkmokk"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=123300000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-168129.9375, -100661.414063, terrain), terrain)

        self.runways.append(Runway(id=1, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-166550.140625, -100963.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-166216.609375, -100355.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand02', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-165785.125, -99880.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand03', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-165729.4375, -99852.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand04', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-165615.3125, -99804.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-165557.859375, -99779.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-165497.5625, -99762, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-165438, -99751.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand08', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-165373.609375, -99741.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand09', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-165315.765625, -99735.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand10', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-165257.390625, -99732.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand11', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-165196.703125, -99728.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand12', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-164877.265625, -99514.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand13', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-164852.078125, -99463.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand14', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-164826.96875, -99408.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand15', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-164797.203125, -99348.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand16', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-164710.90625, -99257.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand17', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-164657.484375, -99221.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand18', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-164599.015625, -99194.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand19', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-164532.859375, -99185.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand20', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-164464.359375, -99189.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand21', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-167866.890625, -100746.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-167890.8125, -100730.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-167913.671875, -100714.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-167936.890625, -100697.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-167960.6875, -100681.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-167984.359375, -100664.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-168008.234375, -100647.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-168031.453125, -100631.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-168230.140625, -100492.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-168206.859375, -100508.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-168182.859375, -100525.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-168159.078125, -100541.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-168135.265625, -100558.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-168111.6875, -100575.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-168445.078125, -100342.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-168421.40625, -100358.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-168397.53125, -100374.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-168373.875, -100391.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-168350.0625, -100408.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-168326.546875, -100424.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q15', length=26.0, width=24.0, height=11.0, shelter=False))


class Murmansk_International(Airport):
    id = 12
    name = "Murmansk International"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=127300000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(131730.496094, 409479, terrain), terrain)

        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[RunwayBeacon(id='airfield12_1', runway_name='13-31', runway_id=1, runway_side='13'), RunwayBeacon(id='airfield12_3', runway_name='13-31', runway_id=1, runway_side='13')]), opposite=RunwayApproach(name='31', heading=310, beacons=[RunwayBeacon(id='airfield12_2', runway_name='31-13', runway_id=1, runway_side='31'), RunwayBeacon(id='airfield12_0', runway_name='31-13', runway_id=1, runway_side='31')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(131927.1875, 409564.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A9', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(131957.546875, 409593.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A7', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(131987.890625, 409622.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A5', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(132018.484375, 409652.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A3', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(132048.953125, 409681.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A1', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(132146.90625, 409576.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A2', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(132112.15625, 409543.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A4', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(132074.78125, 409507.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A6', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(132036.453125, 409467.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A8', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(132377.46875, 409181.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B5', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(132422.46875, 409229.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B6', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(132388.234375, 409265.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B4', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(132343.03125, 409309.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(132307.265625, 409251.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(132260.28125, 409241.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='PP', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(132341.640625, 409217.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='B3', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(132233.46875, 409303.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C1', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(132251.890625, 409323.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C2', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(132270.40625, 409342.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C3', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(132289.078125, 409361.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C4', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(132307.625, 409380.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C5', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(132325.734375, 409399.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C6', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(132344.171875, 409417.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C7', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(132189.875, 409346.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(132209, 409365.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(132227.515625, 409384.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(132245.953125, 409404.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='C10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(131094.046875, 410512.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(131225.296875, 410377.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=61.0, width=61.0, height=20.0, shelter=False))


class Kalixfors(Airport):
    id = 13
    name = "Kalixfors"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118300000, uhf_hz=301100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-26773.458984, -94330.128906, terrain), terrain)

        self.runways.append(Runway(id=1, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-26574.47265625, -93873.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-26558.90234375, -93920.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-26543.853515625, -93964.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-26528.845703125, -94010.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-26513.2734375, -94057.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-26498.265625, -94103.1640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-26483.26953125, -94147.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-26468.259765625, -94193.0703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-26452.689453125, -94239.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-26986.921875, -93969.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-26954.1484375, -93922.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-26923.169921875, -93876.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-26891.169921875, -93831.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-27116.623046875, -94154.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-27083.849609375, -94107.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-27052.87109375, -94061.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-27020.87109375, -94016.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='P04', length=42.0, width=34.0, height=14.0, shelter=False))


class Kirkenes(Airport):
    id = 14
    name = "Kirkenes"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=120350000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(216627.87565, 280054.90785, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield14_0'))
        self.runways.append(Runway(id=1, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(216198.375, 280298.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(216148.265625, 279965.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y20', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(216183.625, 279946.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y21', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(216219.8125, 279925.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y22', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(216224.421875, 279872.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y23', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(216180.421875, 279790.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y25', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(216203.6875, 279830.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y24', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(216439.546875, 280225.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(216029.421875, 279384.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(216049.90625, 279422.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))


class Kallax(Airport):
    id = 15
    name = "Kallax"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=128200000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-274102.5, -10878.522949, terrain), terrain)

        self.runways.append(Runway(id=None, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-274815.1875, -10584.447265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-274828.90625, -10570.303710938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-273989.125, -11813.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-273973.21875, -11797.055664062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-273957.3125, -11780.379882812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-273941.34375, -11763.583007812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-273925.1875, -11746.590820312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-273923.125, -11498.45703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='U06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-273952.3125, -11483.748046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='U07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-273987.3125, -11466.176757812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='U08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-274016.4375, -11451.221679688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='U09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-274051.40625, -11433.528320312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='U10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-273867.53125, -11667.065429688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-274842.71875, -10555.932617188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-274856.6875, -10541.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-274870.90625, -10527.833007812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-274884.75, -10513.677734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-274898.8125, -10499.607421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-274912.65625, -10485.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-274473.96875, -10924.014648438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-274487.78125, -10909.90234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-274501.9375, -10896.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-274515.84375, -10881.76171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-274529.78125, -10867.564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-274543.71875, -10853.452148438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-274557.75, -10839.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-274571.5, -10825.142578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-273825.8125, -11623.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-273788.1875, -11584.235351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='U13', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-273472.875, -10963.077148438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-273536.28125, -10922.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='3', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-273571.3125, -10885.215820312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='4', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-273609.875, -10848.211914062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='5', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-273617.28125, -10795.81640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='7', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-273636.28125, -10754.869140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='8', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-273817.71875, -10602.616210938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-273843.8125, -10628.200195312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='102', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-273396.5, -11014.509765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='112', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-273416.28125, -11100.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-274531.8125, -11017.05078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='U15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-274548.75, -11032.303710938, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='U14', length=21.0, width=15.0, height=8.0, shelter=False))


class Kuusamo(Airport):
    id = 16
    name = "Kuusamo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=118650000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-200527.164063, 310573.234375, terrain), terrain)

        self.runways.append(Runway(id=1, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-199686.53125, 309760.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-199724.921875, 309826.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-199755.8125, 309889.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-199798.84375, 309950.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-199852.953125, 309930.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=36.0, width=36.0, height=15.0, shelter=False))


class Vidsel(Airport):
    id = 17
    name = "Vidsel"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=119200000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-237355.53125, -101474.101563, terrain), terrain)

        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-237200.46875, -102211.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-236817.671875, -102753.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='H01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-236890.6875, -102714.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='H02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-236950.140625, -102571.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='H04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-236897.796875, -102621.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='H03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-237191.34375, -102229.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-237182.109375, -102246.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-237172.953125, -102264.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-237163.71875, -102282.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-237154.640625, -102300.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-237247.109375, -102122.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-236483.609375, -102519.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-237342.9375, -100920.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-237330.765625, -100571.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-235449.84375, -104586.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-235486.53125, -104526.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-235521.703125, -104473.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-235557.734375, -104416.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-235593.625, -104364.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-235204.046875, -104935.9140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='E01', length=30.0, width=23.0, height=10.0, shelter=False))


class Ivalo(Airport):
    id = 18
    name = "Ivalo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118000000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(80495.585938, 197621.367188, terrain), terrain)

        self.runways.append(Runway(id=1, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(80505.1328125, 198340.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(80639.4375, 198100.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(80797.890625, 198206.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(80509.6484375, 198414.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(80515.125, 198489.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(80520.234375, 198564.484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(80525.1328125, 198639.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(80530.2265625, 198714.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(80535.4140625, 198788.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(80540.90625, 198863.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(80609.1875, 198091.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(80584.921875, 198122.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(80555.3828125, 198157.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(80523.4921875, 198191.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(80674.5, 198131.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D04', length=26.0, width=24.0, height=11.0, shelter=False))


class Alakurtti(Airport):
    id = 19
    name = "Alakurtti"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=118350000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-84651.667969, 344113.5, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-84031.1875, 343547.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-84011.6875, 343517.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-83992.09375, 343487.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-83971.367087004, 343457.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-83951.027576343, 343428.09558683, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-83913.596825256, 343366.59189375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-83932.236211829, 343397.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-84881.595145556, 344887.54778146, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-84902.601381208, 344920.55072995, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-84923.112520053, 344953.73863932, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-84860.751395556, 344854.70917936, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-84839.860407973, 344821.48013356, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-84819.302874584, 344788.63674614, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-84798.477051598, 344755.65438926, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-84777.595298112, 344722.7732812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-84756.65625, 344693.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-84737.2265625, 344663.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-84718.015625, 344632.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-84698.5546875, 344602.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-84679.2109375, 344572.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-84659.953125, 344541.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-84640.484375, 344511.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P15', length=26.0, width=24.0, height=11.0, shelter=False))


class Andoya(Airport):
    id = 20
    name = "Andoya"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=118200000, uhf_hz=250600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(151539.578125, -254451.789063, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield20_1'))
        self.beacons.append(AirportBeacon(id='airfield20_0'))
        self.runways.append(Runway(id=1, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(150204.375, -254196.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(149771.640625, -254071.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(149461.828125, -254392.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(149429.515625, -254845.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(149838.484375, -254665.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(150211.203125, -253548.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(150157.859375, -253417.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(152749.46875, -254760.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(152841.046875, -254698.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(152953.96875, -254624.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(152871.5, -254534.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(152756.921875, -254513.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(152738.890625, -254660.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(152649.203125, -254563.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(152645.359375, -254727.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(152517.640625, -254649.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(152476.546875, -254638.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(152438.84375, -254628.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(150048.46875, -253416.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(150044.046875, -253211.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(150118.859375, -253151.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(149945.84375, -253304.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(149852.375, -253308.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(149786.640625, -253212.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(149841.078125, -253132.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(149847.765625, -253021.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(149968.46875, -252994.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(149946.578125, -253140.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(149999.203125, -253045.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(150105.796875, -253015.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(150232.375, -253208.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(150224.84375, -253325.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(150322.4375, -253262.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(150329.40625, -253454.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(150467.359375, -253419.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(150650.671875, -253733.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(150753.796875, -253743.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(150773.609375, -253837.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(150892.5, -253850.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(150961.1875, -253941.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(151048.8125, -253888.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(151561.453125, -254874.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(151572.9375, -255024.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(151750.1875, -255032.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(151771.65625, -255200.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(151774.953125, -255315.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(151882.84375, -255034.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(151924.4375, -255183.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(152066.59375, -255122.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(152075.515625, -255227.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(152159.296875, -255240.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(152157.546875, -255301.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(152174.40625, -255539.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(152303, -255605.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(152358.765625, -255452.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(152405.828125, -255461.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(152422.34375, -255365.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(152416.8125, -255297.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(152542.078125, -255371, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(152480.390625, -255541.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(152400.359375, -255576.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(151897.578125, -255404.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(151758.546875, -254173, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(151643.515625, -254195.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(151937.203125, -254330.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(151812.359375, -254276.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='A23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(152044.3125, -254438.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(152222.171875, -255198.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C23', length=21.0, width=15.0, height=8.0, shelter=False))


class Bardufoss(Airport):
    id = 21
    name = "Bardufoss"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=118100000, uhf_hz=250650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(118870.59375, -160678.242188, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield21_1'))
        self.runways.append(Runway(id=1, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[RunwayBeacon(id='airfield21_2', runway_name='28-10', runway_id=1, runway_side='28'), RunwayBeacon(id='airfield21_0', runway_name='28-10', runway_id=1, runway_side='28')]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(118656.765625, -161458.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(118678.6484375, -161816.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(118754.03125, -161684.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(118107.34375, -159904.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='R13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(118515.5, -160414.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='X01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(118246.984375, -159656.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='R16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(118546.3046875, -161757.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(118498.9921875, -161707.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(118833.4921875, -161368.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(118946.2734375, -161392.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(118638.7578125, -161818.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(119341.7890625, -160954.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(119465.953125, -161680.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(119169.515625, -160546.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(118298.2109375, -160220.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(119390.9296875, -161498.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(118857.984375, -161448.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(119201.9453125, -160701.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(119350.515625, -160992.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(118383.3359375, -159999.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='X04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(118308.5703125, -159904.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='X05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(118116.5703125, -159967.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='R11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(119370.53125, -161443.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(118473.515625, -161680.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(118795.4140625, -161476.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(118880.0078125, -161341.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='J02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(119328.875, -161303.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(119455.46875, -161655.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(119476.9921875, -161707.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(119176.703125, -160571.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(119380.15625, -161471.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(118902.90625, -161281.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(119198.1015625, -160661.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(118121.65746038, -160343.04854745, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(119488.234375, -161734.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(119184.703125, -160600.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(119444.765625, -161629.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(119321.078125, -161275.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(119305.75, -161221.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(118721.53125, -161504.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(118087.78125, -160100.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(118719.203125, -161814.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(119204.3671875, -160726.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(118715.3671875, -161578.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(118111.8515625, -159935.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='R12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(118229.29467376, -160077.9214574, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(119434.1953125, -161603.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(118570.0859375, -161782.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(119313.453125, -161248.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(118191.7734375, -160447.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(119163.296875, -160527.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(119275.0546875, -160793.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(118635.171875, -161680.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(118103.7265625, -159709.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(119156.296875, -160509.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(119412.5390625, -161550.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(119423.40625, -161577.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(118122.1796875, -160180.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(119344.5859375, -161358.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(118213.71875, -159953.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='R10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(119352.65625, -161386.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(118580.703125, -160608.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(118382.65625, -160185.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='X03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(119192.4921875, -160630.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='P15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(118598.7109375, -161811.796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(118522.9453125, -161732.484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='I07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(119336.7109375, -161330.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(119304.9140625, -160873.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='L02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(118294.92944758, -160485.80831031, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(118102.578125, -159872.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='R14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(118472.2734375, -160241.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='X02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(118331.63482351, -160344.00563428, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(119401.625, -161524.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Y09', length=26.0, width=22.0, height=11.0, shelter=False))


class Kittila(Airport):
    id = 22
    name = "Kittila"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4125000, vhf_low_hz=39150000, vhf_high_hz=118950000, uhf_hz=250700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-29037.706055, 100101.597656, terrain), terrain)

        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[RunwayBeacon(id='airfield22_1', runway_name='34-16', runway_id=1, runway_side='34'), RunwayBeacon(id='airfield22_0', runway_name='34-16', runway_id=1, runway_side='34')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-29580.435546875, 100552.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-29390.44140625, 100500.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-29808.169921875, 100630.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-29480.77734375, 100529.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-29346.59765625, 100486.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-29436.970703125, 100515.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-29852.1953125, 100643.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-29702.62890625, 100587.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-29632.015625, 100565.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-29764.609375, 100616.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-29530.0703125, 100540.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=40.0, width=40.0, height=12.0, shelter=False))


class Hosio(Airport):
    id = 23
    name = "Hosio"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-227262.609375, 151497.34375, terrain), terrain)

        self.runways.append(Runway(id=None, name='24-6', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='6', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-226654.640625, 152562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-226678.734375, 152534.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-227828.875, 150499.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-227805.078125, 150530.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N01', length=26.0, width=24.0, height=11.0, shelter=False))


class Alta(Airport):
    id = 24
    name = "Alta"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4150000, vhf_low_hz=39200000, vhf_high_hz=120400000, uhf_hz=250750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(221465.984375, 27686.098633, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield24_2'))
        self.runways.append(Runway(id=1, name='29-11', main=RunwayApproach(name='29', heading=290, beacons=[RunwayBeacon(id='airfield24_1', runway_name='11-29', runway_id=1, runway_side='29'), RunwayBeacon(id='airfield24_0', runway_name='11-29', runway_id=1, runway_side='29')]), opposite=RunwayApproach(name='11', heading=110, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(221437.78125, 27290.884765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(221425.359375, 27317.90234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(221356.90625, 27309.84765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(221624.09375, 26862.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(221604.46875, 26897.990234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(221584.984375, 26933.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(221565.578125, 26968.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(221545.984375, 27004.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(221526.171875, 27039.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(221392.390625, 27353.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))


class Evenes(Airport):
    id = 25
    name = "Evenes"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4175000, vhf_low_hz=39250000, vhf_high_hz=118000000, uhf_hz=250800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(60208.767578, -239417.101563, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield25_2'))
        self.beacons.append(AirportBeacon(id='airfield25_3'))
        self.runways.append(Runway(id=1, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[RunwayBeacon(id='airfield25_1', runway_name='17-35', runway_id=1, runway_side='17'), RunwayBeacon(id='airfield25_0', runway_name='17-35', runway_id=1, runway_side='17')]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(60355.4453125, -239202.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(60300.84765625, -239204.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(60226.48828125, -239206.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(60150.99609375, -239209.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(60109.14453125, -239189.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(60068.91796875, -239184.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(60018.484375, -239191.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26B', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(60034.09765625, -239142.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(60032.84765625, -239101.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(60031.3828125, -239061.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(60030.16796875, -239021.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(58456.32421875, -239934.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Mil_05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(58481.828125, -239884.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Mil_04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(58507.00390625, -239835.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Mil_03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(58532.6640625, -239786.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Mil_02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(58557.375, -239736.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Mil_01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(58830.453125, -239208.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(58807.3984375, -239093.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(58729.06640625, -239157.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(58715.5234375, -239009.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(58694.66796875, -238876.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(58792.4375, -238914.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(58562.203125, -239107.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(58580.3828125, -238947.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(58574.3984375, -238835.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(58559.76953125, -238726.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(58604.33984375, -238576.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(58697.49609375, -238554.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(58745.08984375, -238662.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(58807.9609375, -238560.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(58914.578125, -238634.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(58846.88671875, -238720.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(58896.375, -238805.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M310', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(58886.32421875, -238946.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M311', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(58940.1796875, -239172.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(59030.5625, -239084.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(59054.984375, -239012.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(59033.921875, -238724.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(59152.47265625, -238829.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(59175.47265625, -239069.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(59147.03125, -239200.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(59247.41015625, -239172.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(59295.04296875, -239007.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(59369.1171875, -239206.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(59456.015625, -239141.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(59433.00390625, -239045.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(59343.50390625, -239122.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(59300.06640625, -238817.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(59395.01953125, -238896.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(59566.2890625, -239012.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(59576.1484375, -238916.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(59623.51171875, -238762.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(58730.19921875, -238765.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='M38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(58786.6796875, -239290.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF_02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(58745.96484375, -239283.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF_01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(59904.94140625, -238928.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(59866.7890625, -238839.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='J02', length=26.0, width=22.0, height=11.0, shelter=False))


class Enontekio(Airport):
    id = 26
    name = "Enontekio"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4200000, vhf_low_hz=39300000, vhf_high_hz=119700000, uhf_hz=250850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(41616.833984, 37027.746094, terrain), terrain)

        self.runways.append(Runway(id=1, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[RunwayBeacon(id='airfield26_1', runway_name='03-21', runway_id=1, runway_side='21'), RunwayBeacon(id='airfield26_0', runway_name='03-21', runway_id=1, runway_side='21')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(41126.58203125, 37026.15234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='A04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(41233.94921875, 37038.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(41294.7109375, 37089.35546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(41362.6640625, 37132.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=36.0, width=36.0, height=15.0, shelter=False))


class Sodankyla(Airport):
    id = 27
    name = "Sodankyla"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=39350000, vhf_high_hz=123400000, uhf_hz=250900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-57296.550781, 178052.148438, terrain), terrain)

        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-57312.56640625, 177822.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='A01', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-57338.41015625, 177810.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='A02', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-57354.55078125, 177816.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='A03', length=18.0, width=15.0, height=8.0, shelter=False))


class Kilpyavr(Airport):
    id = 28
    name = "Kilpyavr"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=119100000, uhf_hz=250950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(163480.617188, 389049.8125, terrain), terrain)

        self.runways.append(Runway(id=1, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(163919.421875, 389545.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(163946.078125, 389563.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(163975.4375, 389582.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(164002.09375, 389600.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(164031.46875, 389619.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(164058.125, 389637.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(164087.5, 389656.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(164114.15625, 389673.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(164143.515625, 389693.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(164170.171875, 389710.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(164199.546875, 389730.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(164226.203125, 389747.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(164255.578125, 389767, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(164282.234375, 389784.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(164311.59375, 389803.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(164338.25, 389821.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(162312.1875, 388438.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(162519.328125, 388598.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(162539.21875, 388612, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(162559.3125, 388625.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(162579.609375, 388639, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(162599.5, 388652.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(162619.578125, 388665.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(162639.296875, 388679.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(162659.1875, 388692.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(162679.28125, 388706.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(162698.921875, 388719.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(162379.25, 388482.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(162334.265625, 388453.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(162356.59375, 388467.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(164577.140625, 390049.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(164531.84375, 390106.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(164526.703125, 390080.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(164517.671875, 390030.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(164522.15625, 390055.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(164513.375, 390006.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(164563.484375, 389975.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(164568.09375, 390000.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(164572.625, 390024.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(164508.453125, 389979.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(164558.3125, 390228.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(164554.203125, 390204.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(164550.109375, 390179.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(162824.109375, 388289.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(162772.234375, 388237.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(162780.859375, 388255.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(162789.21875, 388271.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(162935.734375, 388409.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(162916.171875, 388413.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(162439.609375, 388624.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(162467.421875, 388683.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(162513.15625, 388711.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(162794.3125, 388812.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S04', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(162850.640625, 388860.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S05', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(163170.875, 389132.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S07', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(163305.765625, 389249.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S08', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(162990.703125, 388965.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S06', length=20.0, width=14.0, height=6.0, shelter=False))


class Luostari_Pechenga(Airport):
    id = 29
    name = "Luostari Pechenga"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4450000, vhf_low_hz=41200000, vhf_high_hz=119350000, uhf_hz=281300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(187599.09375, 328063.921875, terrain), terrain)

        self.runways.append(Runway(id=1, name='20-02', main=RunwayApproach(name='20', heading=200, beacons=[]), opposite=RunwayApproach(name='02', heading=20, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(188060.40625, 328581.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(187994.8125, 328552.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(187952.328125, 328536.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(187909.78125, 328519.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(187867.15625, 328503.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(187827.125, 328489.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(187778.15625, 328470.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(187729.1875, 328452.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(187680.71875, 328434.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(187635.4375, 328417.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(187589.15625, 328400, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(187540.59375, 328381.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(187496.59375, 328365.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(187446.53125, 328346.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(187398.90625, 328328.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(187346.21875, 328309.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(187308.703125, 328294.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(187275.640625, 328282.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(187243.671875, 328270.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(187212.15625, 328258.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(187179.5, 328246.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(187145.90625, 328234.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(187112.984375, 328222.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(187050.84375, 328198.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(187083.5, 328210.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(187113.515625, 328342.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(187212.140625, 328378.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=42.0, width=34.0, height=14.0, shelter=False))


class Koshka_Yavr(Airport):
    id = 30
    name = "Koshka Yavr"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4850000, vhf_low_hz=38450000, vhf_high_hz=123800000, uhf_hz=225500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(172272.046875, 338839, terrain), terrain)

        self.runways.append(Runway(id=1, name='19-01', main=RunwayApproach(name='19', heading=190, beacons=[]), opposite=RunwayApproach(name='01', heading=10, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(171334.796875, 338997.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(171378.4375, 339000.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C07', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(171426.890625, 339002.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C08', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(171471.1875, 339004.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C09', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(171514.828125, 339007.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C10', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(171556.140625, 339009.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C11', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(171598.0625, 339011.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C12', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(171639.734375, 339013.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C13', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(171681.53125, 339016.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C14', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(171723.453125, 339018.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C15', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(171765.921875, 339020.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C16', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(171808.890625, 339022.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C17', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(171853.90625, 339025, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C18', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(171898.78125, 339027.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C19', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(171944, 339029.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C20', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(171989.234375, 339032.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C21', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(170861.078125, 338812.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(170902.875, 338824.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(170943.796875, 338836.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(170985.453125, 338848.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(171027.71875, 338861.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=40.0, width=38.0, height=18.0, shelter=False))


class Poduzhemye(Airport):
    id = 31
    name = "Poduzhemye"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38450000, vhf_high_hz=120100000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-278453.125, 561022.4375, terrain), terrain)

        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-278142.28125, 562129.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-278144.09375, 562083.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-278146.3125, 562036.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-278148.125, 561990.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-278149.96875, 561944.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-278152.1875, 561897.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-278154.40625, 561852.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-278156.25, 561805.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-278158.4375, 561759.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-278160.28125, 561713.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-278162.125, 561666.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-278306.375, 560029.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-278307.59375, 560001.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-278308.75, 559974.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-278309.96875, 559946.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-278311.28125, 559919.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-278312.5, 559891.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-278313.65625, 559864.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-278677.59375, 562203.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-278683.875, 562118.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-278674.6875, 561887.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='T01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-278698.90625, 561845.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='T02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-278668.03125, 561794.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='T02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-278483.40625, 562279.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='Q01', length=21.0, width=15.0, height=8.0, shelter=False))


class Kalevala(Airport):
    id = 32
    name = "Kalevala"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38400000, vhf_high_hz=119300000, uhf_hz=301000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-273728.015625, 409821.859375, terrain), terrain)

        self.runways.append(Runway(id=1, name='20-02', main=RunwayApproach(name='20', heading=200, beacons=[]), opposite=RunwayApproach(name='02', heading=20, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-273488.625, 410088.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-273578.4375, 410040.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=26.0, width=24.0, height=11.0, shelter=False))


class Afrikanda(Airport):
    id = 33
    name = "Afrikanda"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4775000, vhf_low_hz=39900000, vhf_high_hz=121300000, uhf_hz=311000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-13402.855469, 438922.3125, terrain), terrain)

        self.runways.append(Runway(id=1, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-13724.593471216, 440245.54236662, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-13702.937221216, 440247.33831125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-13681.256557153, 440249.36405077, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-13711.449080175, 440100.84742366, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-13713.301619238, 440119.78492366, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-13714.609236425, 440138.62867366, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-13658.51953125, 440079.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Q01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-13840.060546875, 440097.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-13866.350585938, 440012.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-13894.047851562, 439924.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-13875.341796875, 439852.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-13835.818359375, 439764.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-13799.23828125, 439678.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-13776.78515625, 439535.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-13782.6171875, 439442.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-13795.78515625, 439332, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-13807.190429688, 439222.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-13818.529296875, 439113.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-13799.366210938, 439033.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-13739.11328125, 438953.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-13691.322265625, 438872.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-13647.321289062, 438734.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-13621.377929688, 438641.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-13594.74609375, 438551.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-13566.598632812, 438459.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-13677.462890625, 438366.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-13744.459960938, 438379.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-13755.38671875, 438445.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-13696.939453125, 438466.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-13812.681640625, 438817.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-13865.125, 438909.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-13917.561523438, 438967.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-13891.58203125, 439636.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-13929.0625, 439723.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-13972.12890625, 439809.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-14033.091796875, 439947.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-13952.1171875, 440319.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-13901.71484375, 440444, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14041.209960938, 440468.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-13926.228515625, 439324.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-13920.607421875, 439372.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-13757.803627139, 440240.7163554, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-13799.368080264, 440237.4038554, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-13840.949134951, 440234.6226054, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-13917.4765625, 439280.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-13923.884765625, 439213.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-13928.162109375, 439169.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-13934.577148438, 439104.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-13924.485351562, 438608.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-13952.624023438, 438498.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-13449.612304688, 438193, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-13466.077148438, 438209.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-13480.974609375, 438225.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-13496.553710938, 438241, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-13511.049804688, 438256.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=20.0, width=17.0, height=8.0, shelter=False))


class Boden_Heli_Base(Airport):
    id = 34
    name = "Boden Heli Base"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4475000, vhf_low_hz=40150000, vhf_high_hz=118750000, uhf_hz=252250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-244792.210938, -30945.338867, terrain), terrain)

        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-244852.046875, -31079.60546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-244883.03125, -31040.10546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-244901.6875, -31057.96484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-244920.390625, -31075.880859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-244939.203125, -31093.888671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-244957.890625, -31111.74609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-244976.734375, -31129.720703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-244995.5, -31147.693359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-245014.234375, -31165.65234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-245033.125, -31183.67578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-244878.671875, -31105.05859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-244905.359375, -31130.552734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-244931.90625, -31156.00390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-244958.734375, -31181.607421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-244985.453125, -31207.146484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-244747.71875, -31185.240234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-244778.6875, -31145.7421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-244797.359375, -31163.599609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-244816.0625, -31181.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-244834.875, -31199.5234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-244853.5625, -31217.380859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL11', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-244872.40625, -31235.35546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-244891.171875, -31253.330078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-244909.90625, -31271.287109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-244928.78125, -31289.310546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-244774.34375, -31210.693359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-244801.03125, -31236.189453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-244827.578125, -31261.638671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-244854.40625, -31287.2421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-244881.125, -31312.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HL06', length=30.0, width=23.0, height=10.0, shelter=False))


class Hemavan(Airport):
    id = 35
    name = "Hemavan"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4625000, vhf_low_hz=39950000, vhf_high_hz=122900000, uhf_hz=251500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-232656.234375, -332951.640625, terrain), terrain)

        self.runways.append(Runway(id=1, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-231956.75, -332908.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='S01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-231906.546875, -333045.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-231920.03125, -333000.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=26.0, width=24.0, height=11.0, shelter=False))


class Arvidsjaur(Airport):
    id = 36
    name = "Arvidsjaur"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-268159.331616, -142107.057546, terrain), terrain)

        self.runways.append(Runway(id=1, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[RunwayBeacon(id='airfield36_1', runway_name='12-30', runway_id=1, runway_side='12'), RunwayBeacon(id='airfield36_3', runway_name='12-30', runway_id=1, runway_side='12')]), opposite=RunwayApproach(name='30', heading=300, beacons=[RunwayBeacon(id='airfield36_2', runway_name='30-12', runway_id=1, runway_side='30'), RunwayBeacon(id='airfield36_0', runway_name='30-12', runway_id=1, runway_side='30')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-267901.3125, -142868.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-267944.53125, -142816.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-267987.375, -142764.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-268030.59375, -142712.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S04', length=40.0, width=38.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-268075.40625, -142659.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H01', length=60.0, width=52.0, height=18.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Banak,
    Rovaniemi,
    Kemi_Tornio,
    Vuojarvi,
    Kiruna,
    Severomorsk_3,
    Bodo,
    Severomorsk_1,
    Olenya,
    Monchegorsk,
    Jokkmokk,
    Murmansk_International,
    Kalixfors,
    Kirkenes,
    Kallax,
    Kuusamo,
    Vidsel,
    Ivalo,
    Alakurtti,
    Andoya,
    Bardufoss,
    Kittila,
    Hosio,
    Alta,
    Evenes,
    Enontekio,
    Sodankyla,
    Kilpyavr,
    Luostari_Pechenga,
    Koshka_Yavr,
    Poduzhemye,
    Kalevala,
    Afrikanda,
    Boden_Heli_Base,
    Hemavan,
    Arvidsjaur,
]

