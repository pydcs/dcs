# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Abu_al_Duhur(Airport):
    id = 1
    name = "Abu al-Duhur"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=122200000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(76048.957031, 111344.925781, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(76278.421875, 112793.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(76280.484375, 112763.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(76282.2890625, 112736.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(76284.1953125, 112705.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(76400.609375, 110599.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(76402.859375, 110567.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(76404.890625, 110536.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(76406.9296875, 110499.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(76409.6328125, 110467.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(76411.3984375, 110436.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(76414.28125, 110395.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(76416.4609375, 110362.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(76418.4140625, 110331.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(76420.359375, 110301.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(76422.5078125, 110268.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(76424.5234375, 110237.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(75966.7890625, 109730.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(75991.09375, 109711.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(75803.5078125, 109767.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(75787.90625, 109793.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(76501.0859375, 109760.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(76490.6953125, 110072.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(76508.8671875, 110095.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(76616.0625, 109895.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(75492.9453125, 113106.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(75527.59375, 113285.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(75745.9296875, 113080.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(75771.4453125, 113096.8046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(75780.125, 112892.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(75761.453125, 112869.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(76338.578125, 112682.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(76358.4140625, 112659.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(76308.984375, 112864.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(76307.375, 112894.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(76437.9453125, 113020.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(76293.3046875, 113035.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Adana_Sakirpasa(Airport):
    id = 2
    name = "Adana Sakirpasa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4275000, vhf_low_hz=39450000, vhf_high_hz=121100000, uhf_hz=251000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(219468.65625, -48332.732422, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield2_2'))
        self.beacons.append(AirportBeacon(id='airfield2_3'))
        self.runways.append(Runway(id=1, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[RunwayBeacon(id='airfield2_1', runway_name='05-23', runway_id=1, runway_side='05'), RunwayBeacon(id='airfield2_0', runway_name='05-23', runway_id=1, runway_side='05')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(219900.59375, -46846.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(219858.125, -46855.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(219815.28125, -46864.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(219762.140625, -47053.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(219807.296875, -47023.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(219849.4375, -47014.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(219890.671875, -47003.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(219488.75, -47186.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(219525.84375, -47211.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(219562.8125, -47237.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(219600.015625, -47262.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(219741.6875, -47087.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(219719.5, -47122.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(219697.0625, -47157.50390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(219574.21875, -47078.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(219602.96875, -47017.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(219634.609375, -46966.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(219662.421875, -46926.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(219941.34375, -46837.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(220287.77815769, -47549.613779849, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(220298.08078805, -47535.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(220308.31747279, -47520.545482388, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(220318.04250221, -47505.952248737, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(220327.78853253, -47491.575842504, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(220337.4146874, -47476.807670023, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(220347.80395363, -47461.503186422, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(220357.56706499, -47446.366909314, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(220321.72861964, -47572.590342349, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(220332.09375, -47558.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(220342.11168474, -47543.377513638, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(220351.83671415, -47528.784279987, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(220361.72336948, -47514.681311254, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(220373.03631772, -47500.554653657, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(220383.47245895, -47485.433763806, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(220393.76682031, -47470.852174198, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(220403.75350505, -47455.861345467, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(219772.828125, -46873.66015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(219518.03125, -47376.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(219730.96875, -46882.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=40.0, width=40.0, height=12.0, shelter=False))


class Al_Qusayr(Airport):
    id = 3
    name = "Al Qusayr"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4550000, vhf_low_hz=40000000, vhf_high_hz=119200000, uhf_hz=251550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-51906.964844, 60013.205078, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-52056.5390625, 61770.86328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-52566.94921875, 61464.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-52500.484375, 61317.16796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-51948.35546875, 61612.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-51972.328125, 61593.85546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-52038.29296875, 61746.96484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-52766.8828125, 60728.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-52640.1328125, 60846.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-52501.90234375, 60966.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-52605.703125, 61212.45703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-52790.546875, 61230.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-52867.08984375, 60932.19921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-52081.63671875, 61509.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-52087.23046875, 61538.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-52094.327218542, 61568.020229028, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-52075.676479028, 61479.684058935, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-52069.45703125, 61451.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-51863.296875, 61428.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-51812.81640625, 61198.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-51989.81640625, 61405.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-51782.390625, 60877.16015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-51936.0390625, 61043.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-51870.59765625, 60628.65234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-51317.875, 58704.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-51364.1015625, 58951.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-51407.0625, 59198.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-52663.64453125, 60956.81640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-52700.69140625, 60924.24609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-52644.203125, 60973.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-52553.6171875, 61054.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-52531.56640625, 61073.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-52576.43359375, 61034.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-52619.29296875, 60995.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-52597.859375, 61015.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))


class An_Nasiriyah(Airport):
    id = 4
    name = "An Nasiriyah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4800000, vhf_low_hz=40500000, vhf_high_hz=122300000, uhf_hz=252050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-124683.738281, 85510.820313, terrain), terrain)

        self.runways.append(Runway(id=None, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-123598.528425, 86827.54997916, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-123275.3125, 86664.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-123568.15032084, 86826.044712508, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-123106.7578125, 86653.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-125356.28967813, 84393.999041165, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-123721.31623194, 86703.438075678, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-123700.90154166, 86681.189662492, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-125474.28623003, 84044.472070023, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-123542.22020336, 86164.727872353, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-123564.58178001, 86185.526891517, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-123924.45345999, 86558.751019885, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-123895.75809166, 86568.98116664, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-125594.50803873, 84157.523822276, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-122879.5625, 86506.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-123152.28125, 86265.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-123062.1640625, 86384.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-123047.25, 86024.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-122640.78125, 86333.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-125131.63538496, 84655.385573636, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-122956.109375, 86242.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))


class Tha_lah(Airport):
    id = 5
    name = "Tha'lah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5000000, vhf_low_hz=40900000, vhf_high_hz=122400000, uhf_hz=252450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-258434.929688, 40368.677734, terrain), terrain)

        self.runways.append(Runway(id=1, name='05R-23L', main=RunwayApproach(name='05R', heading=50, beacons=[]), opposite=RunwayApproach(name='23L', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-259523.38051049, 39014.499141368, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-259335.2066851, 39263.243670698, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-259343.38633973, 39296.482166636, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-258937.33887103, 38642.081586503, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='1', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-258970.98292467, 38643.080169036, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='2', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-259510.15536746, 38984.027528517, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-257082.08635486, 41580.370427856, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='7', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-257099.957737, 41608.083691283, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='8', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-257264.2155963, 41296.279129277, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='5', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-257270.379351, 41328.530107474, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='6', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-257816.70954194, 41666.75760382, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-257847.56252391, 41656.104955738, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-257638.03122609, 41946.18338507, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='9', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-257669.47519086, 41949.76662711, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-258795.28937031, 38934.541155834, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='4', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-258763.07075377, 38944.221565026, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='3', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Beirut_Rafic_Hariri(Airport):
    id = 6
    name = "Beirut-Rafic Hariri"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5075000, vhf_low_hz=41050000, vhf_high_hz=118900000, uhf_hz=252600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-131310.8125, -42286.496094, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield6_7'))
        self.beacons.append(AirportBeacon(id='airfield6_0'))
        self.runways.append(Runway(id=3, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[RunwayBeacon(id='airfield6_1', runway_name='16-34', runway_id=1, runway_side='16'), RunwayBeacon(id='airfield6_4', runway_name='16-34', runway_id=1, runway_side='16')]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.runways.append(Runway(id=2, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-131575.125, -41971.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G20', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-131642.984375, -41980.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-131692.421875, -41993.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-131786.734375, -41945.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-131951.234375, -41991.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S3', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-131964.4375, -41914.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S2', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-131979.609375, -41838.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S1', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-131758.71875, -41885.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-131771.546875, -41667.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G7', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-131725.765625, -41648.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G6', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-131488.5625, -41470.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G1', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-131557.375, -41523.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G2', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-131393.5625, -41979.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-131620.078125, -41581.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G3', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-131674.96875, -41628.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G5', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-131595.9375, -41841.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-131650.390625, -41857.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-131706.84375, -41870.35546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-131682.609375, -41763.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-131632.984375, -41746.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-131836.875, -41722.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G8', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-131794.03125, -41787.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G9', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-131735.5, -41775.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-131499.8125, -41955.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-131443.296875, -41976.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-131341.1875, -41978.55078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-130282.5390625, -42027.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N1A', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-130291.90818934, -41831.401465533, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N3', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-130463.98674812, -42011.352994067, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='N8', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-130462.5206683, -41856.745003668, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='N5', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-130463.61827504, -41959.881672907, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='N7', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-130463.0753558, -41908.486498868, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='N6', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-130462.05706062, -41805.584847418, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='N4', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-130541.8125, -41898.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='N9', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-130609.5, -41896.37109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='N10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-130282.5546875, -41982.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N1B', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-130282.578125, -41938.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N2A', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-130282.34375, -41894.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='N2B', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-131153.453125, -41968.49609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-131094.75, -41968.39453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-131036.6953125, -41967.3046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=42.0, width=34.0, height=14.0, shelter=False))


class Damascus(Airport):
    id = 7
    name = "Damascus"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5100000, vhf_low_hz=41100000, vhf_high_hz=118500000, uhf_hz=252650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-178652.320313, 52081.296875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_2'))
        self.beacons.append(AirportBeacon(id='airfield7_4'))
        self.beacons.append(AirportBeacon(id='airfield7_5'))
        self.runways.append(Runway(id=2, name='05R-23L', main=RunwayApproach(name='05R', heading=50, beacons=[RunwayBeacon(id='airfield7_3', runway_name='05R-23L', runway_id=2, runway_side='05R'), RunwayBeacon(id='airfield7_6', runway_name='05R-23L', runway_id=2, runway_side='05R')]), opposite=RunwayApproach(name='23L', heading=230, beacons=[])))
        self.runways.append(Runway(id=1, name='05L-23R', main=RunwayApproach(name='05L', heading=50, beacons=[]), opposite=RunwayApproach(name='23R', heading=230, beacons=[RunwayBeacon(id='airfield7_1', runway_name='05L-23R', runway_id=1, runway_side='23R'), RunwayBeacon(id='airfield7_0', runway_name='05L-23R', runway_id=1, runway_side='23R')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-182103.921875, 50133.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='027', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-182079.9375, 50162.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='028', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-182151.59375, 50076.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='025', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-182127.9375, 50105.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='026', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-182597.125, 49554.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='020', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-182576.625, 49579.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='021', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-182618, 49528.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='019', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-182638.34375, 49502.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='018', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-182534.421875, 49631.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='023', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-182658.859375, 49476.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='017', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-182555.703125, 49605.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='022', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-182171.78125, 50052.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='024', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-180549.03125, 52349.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='605', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-180023.578125, 51576.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-180034.046875, 51822.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-180121.078125, 51656.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-180216.625, 51742.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-179968.0625, 51721.75390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-180071.171875, 51613.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-180179.84375, 51706.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-180093.234375, 51938.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-180503.359375, 52077.76953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='405', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-180508.796875, 51856.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='402', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-180476.796875, 52054.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='403', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-180572.671875, 51942.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='406', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-180451.734375, 52033.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='401', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-180545.109375, 51920.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='404', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-179810.96875, 51569.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='201', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-179976.46875, 51775.23046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-179954.453125, 51551.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-179840.0625, 51725.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-179999.09375, 51471.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='205', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-179926.27465564, 51484.920570022, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='204', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-180440.125, 52258.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='603', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-180491.015625, 52300.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='604', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-180378.5625, 52206.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='602', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-180325.46875, 52162, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='601', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-182418.078125, 50021.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='030', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-182505.875, 49926.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='031', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-182591.890625, 49820.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='032', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-182434.578125, 49777.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='033', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-182357.765625, 49878.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='034', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-180319.75, 51928.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='302', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-180304.625, 51797.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='305', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-180325.234375, 51866.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='303', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-181032.0625, 53098.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='003', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-181048.265625, 53005.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='004', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-182336.234375, 50118.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='029', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-179802, 51497.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='202', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-179854.0625, 51491.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='203', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-180239.546875, 51845.08984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-180241.75, 51945.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='301', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-181462.96875, 52711.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='007', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-181522.421875, 52640.15234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='008', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-181364.140625, 52643.0546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='006', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-181336.390625, 52654.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='005', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-180913.796875, 53041.88671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='002', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-180883.6875, 53046.20703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='001', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-183196.75, 50492.57421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='009', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-183275.21875, 50455.08203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='010', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-183207.46875, 50352.9140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='011', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-183209.59375, 50323.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='012', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-183540.765625, 50043.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='013', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-183629.3125, 50000.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='014', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-183553.53125, 49894.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='015', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-183554.109375, 49864.30078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='016', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-180308.046875, 51844.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='304', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-180530.953125, 52101.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='407', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-180561.375, 52125.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='409', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-180597.59375, 51963.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='408', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-180626.328125, 51986.86328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='410', length=26.0, width=24.0, height=11.0, shelter=False))


class Marj_as_Sultan_South(Airport):
    id = 8
    name = "Marj as Sultan South"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5125000, vhf_low_hz=41150000, vhf_high_hz=122900000, uhf_hz=252700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-171711.336701, 48243.74032, terrain), terrain)

        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-171652.453125, 48101.5703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-171651.875, 48367.8515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-171771.4375, 48372.2265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-171773.296875, 48102.4765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-171779.828125, 48248.85546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-171767.15625, 48195.12109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-171767, 48305.7265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-171654.703125, 48291.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-171646.5625, 48235.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-171656.25, 48179.6640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-171852.984375, 48086.94921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-171904.359375, 48083.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-171956.9375, 48100.26171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-172016.921875, 48085.01953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-172074.390625, 48100.44921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-171934.328125, 48309.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-171918.421875, 48256.94921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-172001.609375, 48264.4140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-171981.046875, 48210.8515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-171953.5625, 48166.6171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))


class Al_Dumayr(Airport):
    id = 9
    name = "Al-Dumayr"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5150000, vhf_low_hz=41200000, vhf_high_hz=120300000, uhf_hz=252750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-158713.039063, 73973.316406, terrain), terrain)

        self.runways.append(Runway(id=None, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-158242.609375, 75715.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-158232.625, 75689.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-158761.46875, 72028.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-157710.171875, 75231.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-157622.96875, 75800.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-157653.734375, 75803.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-157471.734375, 75794.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-157449.46875, 75771.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-158137.6875, 76126.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-158431.625, 75707.9609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-158785.5625, 75609.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-158814.5625, 75600.6015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-158554.96875, 75493.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-158565.078125, 75465.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-158538.359375, 75180.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-158523.875, 75154.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-158921.203125, 75350.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-158948.625, 75362.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-159469.859375, 72838.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-159440.78125, 72832.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-158889.359375, 72559.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-158870.78125, 72584.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-158174.84375, 72182.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-158177.671875, 72212.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-158556.40625, 72571.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-158541.5625, 72597.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-158377.15625, 72713.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-158359.90625, 72737.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-158488.328125, 72776.9140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-158707.703125, 72821.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-158722.96875, 72847.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-157680.28125, 75131.9609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-157650.09375, 75128.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-157690.15625, 75229.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-157670.25, 75227.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-157649.921875, 75224.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-157630.546875, 75222.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-157610.3125, 75220.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-157591.046875, 75218.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-157570.15625, 75215.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-157747.671875, 75288.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-157630.234375, 75404.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-157627.921875, 75434.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-159437, 73087.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-159448.609375, 73116.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-158510.40625, 73433.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-158459.078125, 73546.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-158183.984375, 75940.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-158419.015625, 75930.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-158339.34375, 75523.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-158363.0625, 75542.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-157734.453125, 74958.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-157770.046875, 74842.5546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-157912.953125, 74982.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-157874.734375, 75070.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-157859.15625, 75102.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-157901.890625, 75007.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))


class Eyn_Shemer(Airport):
    id = 10
    name = "Eyn Shemer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3750000, vhf_low_hz=38400000, vhf_high_hz=123400000, uhf_hz=250000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-283538.6875, -92619.707031, terrain), terrain)

        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-283520.1875, -92408.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-283534, -92333.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-283482.875, -92456.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-283477.09375, -92496.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-283486.0625, -92572.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))


class Gaziantep(Airport):
    id = 11
    name = "Gaziantep"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=120100000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(210314.796875, 147379.28125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield11_2'))
        self.beacons.append(AirportBeacon(id='airfield11_3'))
        self.runways.append(Runway(id=None, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(210293.453125, 146533.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(210303.140625, 146500.015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(210105.25, 146995.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(210172.421875, 146758.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(210094.03125, 147035.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(210070.890625, 147113.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(210082.9375, 147074.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(210127.386769, 146917.80824201, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(210116.46875, 146956.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(210138.859375, 146877.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(210161.15625, 146798.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(210150.109375, 146837.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))


class H4(Airport):
    id = 12
    name = "H4"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=122600000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-279366.765625, 207219.265625, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-279326.53125, 205884.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-279186.875, 205786.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-278896.125, 205856.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-278810.15625, 205996.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-278954.28125, 206120.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-279252.4375, 206049.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-279479.375, 208377.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-279396.5625, 208544.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-279539.03125, 208625.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-279828.03125, 208563.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-279914.625, 208422.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-279743.53125, 208323.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Haifa(Airport):
    id = 13
    name = "Haifa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=127800000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-242620.8125, -87704.417969, terrain), terrain)

        self.runways.append(Runway(id=1, name='34-16', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='16', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-242230.96875, -87918.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G5', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-242256.46875, -87909.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G4', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-242303.03125, -87894.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G2', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-242326.328125, -87887.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G1', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-242570.578125, -88062.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A4', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-242545.734375, -88004.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-242533.3125, -87969.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A2', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-242520.9375, -87929.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A1', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-242438.140625, -87631.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z1', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-242420.984375, -87576.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z2', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-242401.984375, -87516.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z3', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-242382.6875, -87455.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z4', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-242365.09375, -87399.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z5', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-242347.703125, -87345.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z6', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-242328.328125, -87283.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Z7', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-242279.71875, -87902.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G3', length=26.0, width=22.0, height=11.0, shelter=False))


class Hama(Airport):
    id = 14
    name = "Hama"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=118050000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(8662.594238, 74333.1875, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(8969.19140625, 73061.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(8987.0947265625, 73065.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(9003.8330078125, 73069.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(9021.369140625, 73074.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(9038.6923828125, 73077.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(9096.544921875, 73140.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(9087.6318359375, 73188.2421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(9080.4033203125, 73239.0703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(9070.2822265625, 73292.5078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(9063.8837890625, 73341.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(8982.041015625, 73805.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(8960.087890625, 73925.203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(8924.4296875, 74126.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(8878.3486328125, 74368.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(8806.32421875, 74738.8671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(9109.76171875, 73521.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(8805.6953125, 72709.8046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(8773.591796875, 72623.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(9226.1826171875, 72544.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(9243.23046875, 72845.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(9294.3466796875, 72885.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(9209.2319367427, 73030.804909862, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(9192.7968205551, 73005.340178898, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(9091.3388671875, 74045.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(8979.2412109375, 74404.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(9073.3447265625, 74481.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(8909.4150390625, 74607.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(8864.17578125, 74566.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(8875.3984375, 74498.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(8918.9296875, 74538.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(8858.369140625, 74960.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(8849.240234375, 74935.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(8932.3183460386, 75197.143783636, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(8873.484375, 75257.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(8987.3818359375, 75374.9140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(8896.9404296875, 75458.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(8868.0625, 75585.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(8974.4609375, 75647.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(8708.390625, 75648.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(8694.986328125, 75675.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(8590.401775226, 75614.573147434, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(8572.729900226, 75610.955959934, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(8555.5225464125, 75608.148287913, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(8537.9745679939, 75604.929970746, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(8520.6149129591, 75601.607851616, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(8503.1652804099, 75597.994353716, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))


class Hatay(Airport):
    id = 15
    name = "Hatay"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=128500000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(147687.484375, 39418.742188, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield15_3'))
        self.beacons.append(AirportBeacon(id='airfield15_0'))
        self.runways.append(Runway(id=None, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(147685.390625, 38910.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(147745.34375, 38967.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(147655.046875, 38881.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(147595.453125, 38823.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(147625, 38852.58984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(147866.75, 39084.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(147836.515625, 39055.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(147715.125, 38939.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(147775.15625, 38996.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(147805.625, 39025.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))


class Incirlik(Airport):
    id = 16
    name = "Incirlik"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=122100000, uhf_hz=360100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(221207.773438, -35240.347656, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield16_0'))
        self.runways.append(Runway(id=1, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[RunwayBeacon(id='airfield16_1', runway_name='05-23', runway_id=1, runway_side='05'), RunwayBeacon(id='airfield16_2', runway_name='05-23', runway_id=1, runway_side='05')]), opposite=RunwayApproach(name='23', heading=230, beacons=[RunwayBeacon(id='airfield16_3', runway_name='05-23', runway_id=1, runway_side='23'), RunwayBeacon(id='airfield16_4', runway_name='05-23', runway_id=1, runway_side='23')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(221611.203125, -35769.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(221592.640625, -35796.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(220781.78125, -36704.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(220757.921875, -36711.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(220734.65625, -36719.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(220541.75, -35443.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(220563.140625, -35410.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(220585.9375, -35378.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(220609.28125, -35345.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(220631.921875, -35312.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(220654.5, -35279.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(220677.1875, -35246.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(220699.875, -35213.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(220723.4375, -35181.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(220746.421875, -35148.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(220807.734375, -35045.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(220853.53125, -35075.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(220899.078125, -35108.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(220965.453125, -35013.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(220919.4375, -34981.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(220874.34375, -34950.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(220936.609375, -34861.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(220982.375, -34891.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(221027.9375, -34923.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(221118.625, -34820.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(221240.765625, -34645.94921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(221362.15625, -34472.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(221415.515625, -34336.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='84', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(221455.84375, -34365.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='83', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(221369.703125, -34261.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(222286.5625, -34268.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(222337.203125, -34308.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(221782.99739004, -34998.778596628, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(221769.46875, -35121.08984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(221663.296875, -35173.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(221352.046875, -35618.01953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(221334.578125, -35740.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(221218, -35794.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(221660.515625, -33924.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(220193.0625, -37450.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(220107.609375, -37415.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(220112.9375, -37340.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(220493.671875, -36634.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(220474.953125, -36622.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(220456.390625, -36609.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(220437.625, -36597.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(220419.0625, -36585.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(220400.546875, -36573.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(220381.1875, -36562.66796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(220028.5, -36234.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(220075.265625, -36168.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(220121.96875, -36102.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(220425.25, -35753.20703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(221190.96875, -36151.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(221186.828125, -36175.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(221183.5625, -36200.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(222191.265625, -34015.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(222208.96875, -34028.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(222227.15625, -34040.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(222244.640625, -34054.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(222263.453125, -34067.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(222281.28125, -34080.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(222300.21875, -34093.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(220883.296875, -36797.2890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(221647.140625, -34034.67578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(221546.765625, -33983.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(221638.859375, -33963.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(221703.78125, -33826.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(221740.65625, -33861.44140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(221865.40625, -33788.88671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(220146.359375, -37479.9609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(220263, -37561.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(220273.125, -37497.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(220411.9375, -37532.73046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(220813.578125, -37058.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(220785.890625, -36909.69921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(220851.234375, -36981.62890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(220944.015625, -36643.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(221090.375, -36728.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(221281.09375, -36368.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(221103.953125, -36012.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(221231.484375, -35897.04296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(221333.359375, -36098.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(221358.125, -35922.47265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(220594.484375, -37063.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(220542.53125, -35204.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(220626.15625, -35085.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(221444.453125, -36079.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(221607.375, -35987.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(221495.671875, -35839.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(221678.046875, -35889.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(221789.21875, -35596.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(221767.9375, -35481.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='122', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(221609.671875, -35574.5703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='121', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(221532.921875, -35468.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='123', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(221602.734375, -35303.77734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='124', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(222195.578125, -34587.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(220663.578125, -37135.55859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(220743.9375, -36856.68359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(220743.34375, -37255.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(220661.97924712, -37218.764512415, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(220536.703125, -37350.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(220638.140625, -37388.09765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(220543.375, -37464.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(220440.71026711, -37414.02554391, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(220337.79854444, -37396.673783156, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(220275.67836757, -37364.858882014, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(220228.29463165, -37307.941758408, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(220313.53125, -37559.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(220630.8125, -36798.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(220606.484375, -36725.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(221706.234375, -33958.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(221578.46875, -33891.15234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(221590.03125, -34123.97265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(221569.984375, -34066.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(221567.359375, -34039.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(221564.40625, -34012.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(220917.125, -36237.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(220784.6875, -36414.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(220896.90625, -36357.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(221233.84375, -36436.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(221148.0625, -36306.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(221300.203125, -36216.76953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(221157.3125, -36127.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(220697.234375, -34954.21484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='125', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(220739.34375, -34893.79296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='126', length=26.0, width=24.0, height=11.0, shelter=False))


class Jirah(Airport):
    id = 17
    name = "Jirah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=118100000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(115359.652344, 187020.734375, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(115251.65625, 188431.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(115247.0625, 188456.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(115256.4296875, 188406.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(115233.203125, 188529.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(115237.7109375, 188505.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(115242.3671875, 188480.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(115261.1953125, 188381.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(115274.96875, 188308.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(115269.9921875, 188332.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(115265.5078125, 188356.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(115500.3046875, 187918.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(115610.015625, 188144.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(115387.28125, 187936.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(114840.78125, 188132.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(114820.4765625, 188414.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(115033.0234375, 187674.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(114965.78125, 188002.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(114899.359375, 187879.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(114886.15625, 188621.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(115390.9375, 188318.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(115488.7109375, 187471.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(115476.65625, 188641.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(115598.4921875, 188546.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(115666.921875, 187660.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(115360.2109375, 188654.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(114970.328125, 188493.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(114916.1015625, 188617.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(115201.296875, 188650.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Khalkhalah(Airport):
    id = 18
    name = "Khalkhalah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=122500000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-218620.25, 56161.078125, terrain), terrain)

        self.runways.append(Runway(id=2, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-216011.40625, 52803.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-216074.609375, 52836.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-216043.53125, 52819.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-216101.6875, 52853.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-215989.515625, 52790.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-217979.421875, 57278.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-218040, 57041.01171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-218062.15625, 57020.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-217744.34375, 57152.82421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-217986.484375, 57307.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-216192.8125, 52301.66015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-215750.25, 52284.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-216059.515625, 52221, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-215903.734375, 52357.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-215875.40625, 52365.62109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-215613.0625, 52575.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-215737.375, 52689.80078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-215851.78125, 52713.32421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-218599.375, 53658.76953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-215883.9375, 52822.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-218481.53125, 53551.31640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-218571.828125, 53842.35546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-218350.890625, 54182.41796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-218107.90625, 54165.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-218107.5625, 54195.2109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-218563.625, 53813.66796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-217911.8125, 57665.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-218393.625, 54069.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-215878.125, 52726.46484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-217932.609375, 57684.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-217847.1875, 57492.35546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-217858.8125, 57466.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-217719.53125, 57668.93359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-217712.921875, 57641.23828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-217772.625, 57164.00390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-218299.40625, 55644.5234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-218171.015625, 55612.8515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-218243.9375, 55867.2578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-218116.484375, 55835.3203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-218050.8125, 56036.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-217920.90625, 56003.7734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-217996.21875, 56259.5703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-217864.5, 56225.8515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-217750.171875, 56622.94140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-217622.03125, 56589.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-217696.828125, 56844.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-217564.34375, 56809.984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-218250.84375, 53425.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-218151.328125, 53375.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-217982.984375, 53285.57421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-217891.921875, 53233.8828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-217712.625, 53168.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-217634.546875, 53101.13671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-217539.90625, 53069.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-217461.09375, 53000.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))


class King_Hussein_Air_College(Airport):
    id = 19
    name = "King Hussein Air College"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=118300000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-296592.405413, 24944.355658, terrain), terrain)

        self.runways.append(Runway(id=None, name='31-13', main=RunwayApproach(name='31', heading=310, beacons=[]), opposite=RunwayApproach(name='13', heading=130, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-296640.80960449, 24183.058325481, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-296678.90585077, 24226.843733705, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-296652.95668629, 24196.812040901, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-296666.00562723, 24212.346557418, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-296578.87714877, 24116.257915181, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-296538.76722989, 24073.167061635, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-296552.66796941, 24088.352492213, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-296565.92531672, 24102.7458605, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-296604.0114239, 24142.95477655, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-296590.72863258, 24130.309058278, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-296628.71539229, 24170.205390752, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-296616.69625101, 24156.516224996, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-295961.59375, 23764.876953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-296035.96875, 23715.93359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-295883.3125, 23814.978515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-296011.34375, 23732.806640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-295910.46875, 23798.123046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-295936.6875, 23781.3671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-295986.1875, 23748.37109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-297933.97112481, 26085.39973119, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-297853.62104594, 26005.231704819, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-298013.19758872, 26176.240044867, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-298008.27544296, 25395.875449027, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-296136.49667777, 23596.228672641, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-297987.45798596, 25471.236730109, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-297767.44966778, 25543.556640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-297782.50243281, 25428.64625618, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-297730.53761074, 25658.870143357, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-297910.5241298, 25715.468414813, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-297873.90625, 25830.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-297924.45798596, 25307.497537845, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-297806.40862481, 25935.712099303, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-297840.4375, 25211.94921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-297704.46208011, 25338.725111856, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-297761.89352852, 25122.497545509, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-297952.63080704, 25587.055690232, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-295941.34375, 23674.439453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-295819.07191023, 23633.595176932, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-296122.25, 23996.90234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-296159.15486711, 23884.298015472, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-295690.30251845, 23596.532376325, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-295737.98838044, 23716.448777959, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-296008.6324709, 23558.024963619, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-297113.83953047, 26250.561767147, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-296317.5625, 24213.353515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-297239.13984637, 26143.442253059, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-297232.85658389, 26258.429971188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-295341.53125, 24280.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-295459.44976252, 24166.80340192, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-295347.96875, 24161.236328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-297119.25181292, 26136.364902449, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-295451.09918875, 24286.377999792, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))


class Kiryat_Shmona(Airport):
    id = 20
    name = "Kiryat Shmona"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=118400000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-199486.164063, -34500.691406, terrain), terrain)

        self.runways.append(Runway(id=None, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-199734.375, -34826.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-199700.21875, -34799.95703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-199716.375, -34813.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-199751.5, -34841.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-199866.359375, -35206.71484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))


class Bassel_Al_Assad(Airport):
    id = 21
    name = "Bassel Al-Assad"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=118100000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(41994.498047, 5841.909424, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield21_2'))
        self.beacons.append(AirportBeacon(id='airfield21_3'))
        self.runways.append(Runway(id=1, name='17L-35R', main=RunwayApproach(name='17L', heading=170, beacons=[]), opposite=RunwayApproach(name='35R', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(43002.09375, 5465.603515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(43025.140625, 5465.9360351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(43048.53515625, 5463.6826171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(43071.828125, 5463.5791015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(42752.359375, 5383.3271484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(43095.1484375, 5463.3076171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(43118.21875, 5462.6240234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(43142.09765625, 5462.0419921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(43164.859375, 5461.5791015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(42843.66015625, 5142.7290039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(43093.89453125, 5384.1088867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(43113.34765625, 5383.8696289063, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(43154.3046875, 5383.3173828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(43174.3125, 5382.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(43194.15625, 5381.4697265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(43214.78125, 5381.2548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(43234.0078125, 5380.5200195312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(43254.4765625, 5379.2236328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(42929.24609375, 6348.849609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='44', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(42810.33984375, 6375.1801757812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(42809.375, 6338.126953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(42807.4296875, 6298.9243164062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(42807.046875, 6260.06640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(42805.54296875, 6219.314453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(42804.9765625, 6179.294921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(42803.91015625, 6138.037109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(42803.0859375, 6099.0439453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(43279.66015625, 5898.326171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(43303.921875, 5897.8823242188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(43328.3046875, 5897.4594726563, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(42633.26953125, 5365.3383789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(42596.25390625, 6145.3608398438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(42672.98046875, 6143.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(42518.5859375, 6146.2915039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(42439.484375, 6146.9443359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(42360.3203125, 6147.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(43133.53125, 5383.82421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(42518.8515625, 5371.0561523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(42633.4140625, 5406.3588867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(42520.203125, 5418.8837890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(42927.828125, 6270.6611328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='43', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(42925.5703125, 6191.8510742188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(42923.68359375, 6111.470703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(43098.953125, 6175.123046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='50', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(43100.8359375, 6255.427734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='51', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(43102.62890625, 6336.0502929688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='52', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(43123.36328125, 6467.470703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='53', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(42987.23046875, 6474.1064453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='49', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(43004.6953125, 6373.3154296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(43003.1875, 6297.880859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='47', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(43002.00390625, 6219.2954101563, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='46', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(42998.890625, 6141.4541015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(43255.43359375, 5898.8120117188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))


class Marj_as_Sultan_North(Airport):
    id = 22
    name = "Marj as Sultan North"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=122700000, uhf_hz=250600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-170244.028992, 47506.718825, terrain), terrain)

        self.runways.append(Runway(id=None, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-170310.71875, 47426.27734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-170281.296875, 47602.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-170234.984375, 47371.68359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-170108.171875, 47430.20703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-170153.375, 47438.53515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-170197.75, 47446.05078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-170167.578125, 47621.31640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-170180.875, 47544.80859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-170136.359375, 47536.38671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-170188.890625, 47496.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-170302.75, 47470.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-170295.5, 47514.87890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-170288.609375, 47557.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-170091.296875, 47529.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))


class Marj_Ruhayyil(Airport):
    id = 23
    name = "Marj Ruhayyil"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=120800000, uhf_hz=250650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-194233.6875, 46043.976563, terrain), terrain)

        self.runways.append(Runway(id=1, name='06L-24R', main=RunwayApproach(name='06L', heading=60, beacons=[]), opposite=RunwayApproach(name='24R', heading=240, beacons=[])))
        self.runways.append(Runway(id=2, name='06R-24L', main=RunwayApproach(name='06R', heading=60, beacons=[]), opposite=RunwayApproach(name='24L', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-194252.21875, 44232.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-194282.171875, 44230.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-194587.84375, 44375.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-194605.65625, 44400.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-194124.59375, 44277.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-194099.359375, 44293.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-194128.546875, 44531.37109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-194100.28125, 44540.37109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-194480.828125, 44791.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-194556.609375, 44841.98046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-194976.140625, 44896, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-194908.765625, 45020.35546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-195966.96875, 44616.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-195829.359375, 44794.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-195804, 44903.04296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-193736.6875, 47613.01171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-193710.59375, 47741.51953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-193616.84375, 47589.70703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-193603.171875, 47617.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-193324.21875, 47615.76171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-193352.5, 47604.83203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-193307, 47385.18359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-193221.015625, 47472.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-192887.96875, 47039.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-192876.484375, 47011.20703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-192748.21875, 47334.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-192731.890625, 47309.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-193775.953125, 47133.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-193754.9375, 47177.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-193735, 47218.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-193714.84375, 47261.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-193694.71875, 47301.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-193676.015625, 47342.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-193145.046875, 45821.81640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-193091.640625, 45756.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-193046.234375, 45800.98046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-193058.59375, 45855.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-193030.953125, 45971.74609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-192985.5625, 46058.47265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-192934.234375, 46148.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-192870.375, 46173.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-192853.8125, 46237.57421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-192938.984375, 46233.91796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-192575.625, 46483.01953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-192509.140625, 46455.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-192536.6875, 46555.109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-192516.875, 46622.80859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-192445.21875, 46657.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-192450.46875, 46732.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-192425.90625, 46791.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-192350.171875, 46765.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-192323.75, 46823.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-192397.734375, 46858.17578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))


class Megiddo(Airport):
    id = 24
    name = "Megiddo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4125000, vhf_low_hz=39150000, vhf_high_hz=119900000, uhf_hz=250700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-266965.015625, -71068.832031, terrain), terrain)

        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-266855.78894767, -70709.252965942, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-266836.47678221, -70719.901446102, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-266818.89077816, -70729.664412194, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-266800.95949932, -70740.563451847, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-266782.85354739, -70750.956968896, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-266765.6865152, -70760.230776548, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-266966.90625, -72310.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-266966.875, -72279.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-267257.4375, -70506.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))


class Mezzeh(Airport):
    id = 25
    name = "Mezzeh"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4150000, vhf_low_hz=39200000, vhf_high_hz=120700000, uhf_hz=250750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-172160.453125, 24865.682617, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield25_0'))
        self.runways.append(Runway(id=None, name='24-06', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='06', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-171953.078125, 25448.814453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-171989.59375, 25521.22265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-172004.625, 25550.388671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-172004.765625, 24883.302734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-171606.046875, 26258.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-171359.1875, 26056.25390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-171343.9375, 26082.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-171956.25, 26037.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-171618.53125, 25034.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-171582.265625, 25078.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-172922.15625, 23871.599609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-172891.4375, 23873.232421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-172511.28125, 23612.505859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-172528.015625, 23638.708984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-171630.90625, 26241.94921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-172090.21875, 24730.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-172219.59375, 24488.287109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-172321.125, 24304.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-172387.5, 24179.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-172467.09375, 24034.341796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-172558.390625, 23857.439453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-171426.296875, 25749.833984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-172339.21875, 24013.982421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-172214.40625, 24238.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-171956.796875, 25702.974609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-171904.296875, 25872.267578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-172171.921875, 26050.841796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-171705.78125, 26361.802734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-172635.484375, 24848.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-172608.5625, 24787.755859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-172643.75, 24899.298828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-172618.59375, 24960.681640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-172593.421875, 24736.400390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-172529.3125, 24713.166015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-172412.15625, 24750.208984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-172383.453125, 24812.70703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-172389.671875, 24866.978515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-172420.4375, 24927.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-172430.765625, 24968.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-172490.828125, 24998.720703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))


class Minakh(Airport):
    id = 26
    name = "Minakh"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4175000, vhf_low_hz=39250000, vhf_high_hz=120600000, uhf_hz=250800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(163697.53125, 107430.609375, terrain), terrain)

        self.runways.append(Runway(id=2, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.runways.append(Runway(id=1, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(163441.59375, 107169.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(163441.5625, 107195.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(163441.953125, 107221.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(163442.640625, 107245.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(163443.390625, 107271.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(163443.890625, 107297.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(163444.09375, 107322.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(163823.421875, 107561.6640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(164023.671875, 107455.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(164209.640625, 107547.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(163979.53125, 107607.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(163788.203125, 107747.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(163994.65625, 106824.8671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(164045.59375, 106890.5859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(164059, 106980.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(164090.359375, 107040.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(164161.640625, 107118.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(164225.234375, 107165.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(164255.453125, 107237.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(164248.9375, 107324.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))


class Aleppo(Airport):
    id = 27
    name = "Aleppo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4200000, vhf_low_hz=39300000, vhf_high_hz=119100000, uhf_hz=250850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(125576.863281, 123125.304688, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield27_1'))
        self.beacons.append(AirportBeacon(id='airfield27_2'))
        self.beacons.append(AirportBeacon(id='airfield27_0'))
        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(125126.828125, 124845.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(125262.703125, 124155, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(125252.3125, 124267.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(125223.34375, 124425.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(125429.6640625, 122696.0234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(125324.71875, 122681.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(125937.7890625, 123365.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(125904.6328125, 123406.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(125902.96875, 123620.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(125833.09375, 123609.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(125913.09375, 123507.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(125908.5859375, 123454.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(125924.7734375, 123291.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(125960.640625, 123249.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(125219.8203125, 124455.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(125211.1640625, 124628.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(125318.1875, 122730.7421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(125311.09375, 122779.3359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(125305.0703125, 122828.0234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(125422.765625, 122744.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(125416.109375, 122793.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(125409.2890625, 122841.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))


class Palmyra(Airport):
    id = 28
    name = "Palmyra"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=39350000, vhf_high_hz=121900000, uhf_hz=250900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-55704.023438, 220114.742188, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield28_1'))
        self.beacons.append(AirportBeacon(id='airfield28_0'))
        self.runways.append(Runway(id=None, name='26-08', main=RunwayApproach(name='26', heading=260, beacons=[]), opposite=RunwayApproach(name='08', heading=80, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-55613.91796875, 218666.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-55610.5625, 218694.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-55602.03515625, 218886.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-55601.4453125, 219086.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-55406.643602879, 219267.6243113, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-55401.72273061, 219312.63537167, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-55398.016148388, 219356.34084648, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-55393.799852879, 219402.17768204, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-55316.3671875, 220228.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-55119.5234375, 220463.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-55069.37109375, 220724.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-55214.5703125, 221011.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-55395.75, 221064.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-55380.3359375, 221201.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-55315.9765625, 221317.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-55092.93359375, 221375.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-55338.85546875, 221494.04272633, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-55336.21875, 221523.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-55402.53515625, 221434.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-55398.62109375, 221469.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-55155.953125, 221746.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-55353.92578125, 221646.18611711, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Qabr_as_Sitt(Airport):
    id = 29
    name = "Qabr as Sitt"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=122600000, uhf_hz=250950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-174597.761535, 37221.970678, terrain), terrain)

        self.runways.append(Runway(id=1, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-174752.078125, 37094.52734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-174729.96875, 37178.1953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-174711.9375, 37236.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-174572.125, 37409.44921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-174493.796875, 37202.12109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-174534.34375, 37068.04296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-174553.125, 36989.43359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-174627.015625, 36981.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-174636.09375, 37033.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))


class Ramat_David(Airport):
    id = 30
    name = "Ramat David"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4300000, vhf_low_hz=39500000, vhf_high_hz=118600000, uhf_hz=251050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-259102.132813, -75789.410156, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield30_1'))
        self.beacons.append(AirportBeacon(id='airfield30_0'))
        self.runways.append(Runway(id=3, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[RunwayBeacon(id='airfield30_2', runway_name='15-33', runway_id=3, runway_side='33'), RunwayBeacon(id='airfield30_3', runway_name='15-33', runway_id=3, runway_side='33')])))
        self.runways.append(Runway(id=2, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-258930.734375, -75766.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-258932.171875, -75743.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-258930.84375, -75719.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-258929.875, -75696.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-258928.6875, -75672.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-258684.97202576, -74703.004812078, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-258826.5625, -74570.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-258841.953125, -74549.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-258858.09375, -74527.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-258874.171875, -74506.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-258823.6875, -76847.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-258840.78125, -76822.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-258360.25, -75909.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-259885.6875, -74320.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-259533.484375, -74288.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-259300.5, -74383.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-259876.1875, -74352.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-259535.546875, -74323.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-259322.9375, -74411.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-258892.796875, -74483.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-258909.03125, -74462.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-258390.296875, -76228.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-258415.015625, -76203.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-258394.875, -75913.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-259974.390625, -74785.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-259999.78125, -74810.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-259545.140625, -75441.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-259567.296875, -75468.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-259785.734375, -75052.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-259802.6875, -75081.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-259277.3125, -75543.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-259269.84375, -75576.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-258770.765625, -75185.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-258769.078125, -75158.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-258767.265625, -75132.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-258765.28125, -75105.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-258763.28125, -75079.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-259959.875, -74257.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-259939.59375, -74245.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-259919.453125, -74234.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-259878.71875, -74210.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-259899.4375, -74221.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))


class Kuweires(Airport):
    id = 31
    name = "Kuweires"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4325000, vhf_low_hz=39550000, vhf_high_hz=120500000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(125810.890625, 155253.8125, terrain), terrain)

        self.runways.append(Runway(id=None, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(125533.8359375, 154375.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(125528.4296875, 154402.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(125523.1640625, 154429.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(125518.0078125, 154456.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(125512.703125, 154483.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(125507.5078125, 154510.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(125502.1328125, 154537.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(125496.78125, 154565.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(125491.609375, 154592.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(125486.3984375, 154619.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(125438.953125, 154863.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(125433.6484375, 154890.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(125454.75, 154782.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(125449.40625, 154809.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(125444.171875, 154836.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(125470.640625, 154700.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(125465.4296875, 154728.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(125460.0859375, 154755.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(125475.7734375, 154673.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(125481.0625, 154646.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(125868.921875, 154054.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(125887.0234375, 154058.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(125904.7578125, 154062.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(125923.171875, 154066.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(125941.09375, 154069.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(125959.3984375, 154072.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(125225.8125, 156555.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(125226.9375, 156585.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(125679.140625, 156731.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(125792.4375, 156752.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(125922.671875, 156113.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(126393.15625, 155059.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(126338.3984375, 154689.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(126128.96875, 154563.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(126182.2421875, 154301.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(126242.4140625, 154137.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(126275.84375, 154017.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Rayak(Airport):
    id = 32
    name = "Rayak"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4350000, vhf_low_hz=39600000, vhf_high_hz=124400000, uhf_hz=251150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-130132.492188, 4053.336304, terrain), terrain)

        self.runways.append(Runway(id=None, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-129373.9453125, 5490.4599609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-129356.2734375, 5509.322265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-129338.859375, 5527.9926757812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-129321.265625, 5546.7426757813, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-129275.3125, 5484.6723632813, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-129291.9921875, 5465.0029296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-129309.4140625, 5445.9350585937, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-129326.6015625, 5427.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-129417.609375, 5385.3833007813, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-129437.25, 5364.3862304688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-129412.0078125, 5439.1123046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-129477.21884565, 5330.181085508, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))


class Rene_Mouawad(Airport):
    id = 33
    name = "Rene Mouawad"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4375000, vhf_low_hz=39650000, vhf_high_hz=121000000, uhf_hz=251200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-48306.007813, 8690.693604, terrain), terrain)

        self.runways.append(Runway(id=None, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-47948.4140625, 8702.654296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-47964.61328125, 8671.2744140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-47900.51171875, 8797.40234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-47917.640625, 8766.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-47933.48828125, 8734.7802734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-47979.92578125, 8642.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-47885.35546875, 8829.9736328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-47869.05859375, 8861.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-47852.80078125, 8893.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-48921.453125, 7167.7524414062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-48860.46875, 7303.2216796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-47529.86328125, 9976.3935546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-47367.125, 9996.330078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Rosh_Pina(Airport):
    id = 34
    name = "Rosh Pina"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4400000, vhf_low_hz=39700000, vhf_high_hz=118450000, uhf_hz=251250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-225277.733943, -37687.536255, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield34_0'))
        self.runways.append(Runway(id=None, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-225774.390625, -37479.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-225566.578125, -37380.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-225881.96875, -37448.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-225557.140625, -37365.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-225654.921875, -37340.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-225646.0625, -37326.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-225802.21875, -37510.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-225811.171875, -37454.41796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-225839.921875, -37494.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Sayqal(Airport):
    id = 35
    name = "Sayqal"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4425000, vhf_low_hz=39750000, vhf_high_hz=120400000, uhf_hz=251300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-151781.367188, 117529.734375, terrain), terrain)

        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-150767.75, 118082.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-150739.515625, 118091.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-150798.984375, 118305.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-151046.015625, 118636.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-151022.375, 118619.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-150998.53125, 118601.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-150975, 118583.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-150951.09375, 118565.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-150927.4375, 118547.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-150903.859375, 118529.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-150879.984375, 118512.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-150856.53125, 118494.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-150832.6875, 118476.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-150479.15625, 117962.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-150099.796875, 117949.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-150324.015625, 117944.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-150766.59375, 119312.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-150749.796875, 119337.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-151193.84375, 119589.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-151220.5625, 119574.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-151370.84375, 119406.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-151341.875, 119398.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-151195.84375, 119228.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-151202.609375, 119257.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-151422.828125, 118999.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-151531.390625, 119188.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-151551.046875, 119211.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-152064.046875, 119173.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-152042.515625, 119194.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-152175.796875, 118990.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-152401.625, 118990.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-152402.375, 119020.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-152172.625, 119326.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-152202.546875, 119326.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-152123.21875, 115658.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-152134.8125, 115686.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-152011.03125, 115887.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-152113.375, 115979.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-151930.796875, 115975.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-152039.40625, 116061.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-152031.0625, 116090.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-152022.65625, 116314.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-152033.6875, 116286.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-151596.25, 115428.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-151622.953125, 115413.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-151465.375, 115627.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-151477.640625, 115600.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-151363.53125, 115745.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-151366.15625, 115775.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-151514.671875, 115949.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-151530.21875, 115923.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-151255.6875, 116011.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-151259.8125, 115981.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-151389.6875, 116162.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-151373.53125, 116187.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-151354.78125, 117107.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-151366.453125, 117421.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-151254.8125, 117628.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-150980.53125, 117776.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))


class Shayrat(Airport):
    id = 36
    name = "Shayrat"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4450000, vhf_low_hz=39800000, vhf_high_hz=120200000, uhf_hz=251350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-61368.207031, 90675.136719, terrain), terrain)

        self.runways.append(Runway(id=None, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-62254.8671875, 92263.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-62243.515625, 92291.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-62432.48046875, 92339.7734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-62408.37890625, 92358.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-62489.69140625, 92151.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-62490.40625, 92181.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-62269.2734375, 92023.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-62280.4921875, 92051.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-62128.73046875, 91946.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-62127.12890625, 91976.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-61852.84375, 92503.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-61882.9296875, 92506.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-61719.49609375, 92322.5703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-61738.234375, 92346.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-61565.9296875, 92100.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-61538.53125, 92088.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-60538.8828125, 89953.0546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-60562.1953125, 89972.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-60230.67578125, 90324.6796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-60244.2734375, 90297.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-60372.7890625, 89819.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-60148.73828125, 89517, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-59998.8203125, 90024.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-59999.33203125, 90054.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-59789.515625, 89731.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-59787.9921875, 89761.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-59633.95703125, 89851.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-59638.38671875, 89821.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-60384.8359375, 89189.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-60373.36328125, 89217.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-60472.2578125, 89326.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-60535.4296875, 89182.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-61114.6796875, 89430.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-61090.44921875, 89412.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-60954.0078125, 89082.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-60981.7109375, 89094.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-61179.85546875, 89020.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-61198.25390625, 89045.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-61077.80078125, 88972.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-61047.8828125, 88976.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-60592.5703125, 90579.6484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-60491.921875, 90793.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-60506.36328125, 90812.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-60523.12890625, 90833.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-60536.85546875, 90852.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-61742.02734375, 92066.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-61762.4375, 92093.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-61782.7265625, 92119.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-61802.92578125, 92146.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-61823.31640625, 92173.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-60235, 89908.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-60214.390625, 89882.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-60193.92578125, 89855.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-60173.5859375, 89829.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-60153, 89802.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-60255.52734375, 89936.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-60275.6796875, 89962.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))


class Tabqa(Airport):
    id = 37
    name = "Tabqa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4475000, vhf_low_hz=39850000, vhf_high_hz=118500000, uhf_hz=251400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(76964.6875, 243605.210938, terrain), terrain)

        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(77222.4375, 244747.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(77359.6015625, 245047.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(77244.8515625, 244727.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(77246.140625, 245090.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(77246.4921875, 245120.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(77351.421875, 242655.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(77196.5703125, 245305.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(77352.109375, 242625.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(77350.015625, 245283.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(77607.140625, 242237.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(77463.578125, 242046.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(77408.875, 245447.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(77385.1875, 241958.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(77285.9609375, 245521.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(77370.3828125, 241932.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(76687.828125, 245209.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(76707.078125, 245232.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(77407.8046875, 242174.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(77406.078125, 242210.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(77404.4140625, 242244.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(77428.390625, 244914.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(77402.2109375, 242277.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(77400.1640625, 242313.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(77169.5625, 244860.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(77167.7109375, 244890.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(77165.5859375, 244920.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(77163.515625, 244951.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(77162.453125, 244980.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(77161.1328125, 245007.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))


class Taftanaz(Airport):
    id = 38
    name = "Taftanaz"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4500000, vhf_low_hz=39900000, vhf_high_hz=122800000, uhf_hz=251450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(103485.980469, 82766.671875, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(103153.3359375, 82645.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(103122.875, 82555.2109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(103196.78125, 82495.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(103244.46875, 82597.109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(103101.71875, 82386.3828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(103078.609375, 82484, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(102969.3671875, 82480.1484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(103028.59375, 82565.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(102883.828125, 82596.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(102966.203125, 82670.109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(102878.859375, 82433.8828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(102944.8984375, 82367.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(102970.359375, 82271.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(102860.5, 82323.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(102818.1875, 82664.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(102868.484375, 82738.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(103050.6875, 82879.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(103139.8359375, 82959.328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(103128.59375, 82819.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(103203.859375, 82889.1640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(103301.671875, 82724.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(103337.5078125, 82817.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(103414.609375, 82785.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(103384.9296875, 82692.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(103351.03125, 82567.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(103338.921875, 82465.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(103417.484375, 82449.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='27', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(103455.71875, 82541.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='28', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(103318.25, 82286.5078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(103391.140625, 82343.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(103473.765625, 82275.6953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='32', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(103481.1875, 82380.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='29', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(103377.71875, 82049.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(103472.1484375, 82072.2421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(103492.921875, 82195.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(103558.6171875, 82118.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(103687.8203125, 82244.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(103650.734375, 82344.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(103750.734375, 82325.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(103766.1875, 82232.3515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(103633.375, 82499.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(103724.3984375, 82534.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(103673.21875, 82638.1015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='43', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(103593.5625, 82591.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='44', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(103575.0703125, 82708.328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(103555.078125, 82804.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(103649.9453125, 82860.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='47', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(103681.734375, 82764.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='46', length=30.0, width=23.0, height=10.0, shelter=False))


class Tiyas(Airport):
    id = 39
    name = "Tiyas"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4525000, vhf_low_hz=39950000, vhf_high_hz=120500000, uhf_hz=251500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-58907.53125, 157071.484375, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-58583.79296875, 154749.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-58446.546875, 154804.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-58195.171875, 154864.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-57997.5, 154854.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-58090.74609375, 154982.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-58493.53515625, 155889.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-58463.66796875, 155889.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-59847.71875, 156032.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-59819.33984375, 156040.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-59592.7421875, 156127.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-59564.25, 156119.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-59263.98046875, 155144.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-59241.86328125, 155123.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-59515.265625, 155222, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-59515.88671875, 155252.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-59640.06640625, 155499.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-59665.328125, 155483.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-59174.60546875, 155429.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-59201.37109375, 155415.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-59426.9453125, 155924.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-59419.42578125, 155895, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-58491.66796875, 158067.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-58491.64453125, 158105.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-58491.85546875, 158141.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-58492.15625, 158179.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-58492.2890625, 158216.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-58492.0703125, 158253.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-58492.26171875, 158290.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-58492.1875, 158328.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-58492.21875, 158365.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-58492.3359375, 158402.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-58492.453125, 158440.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-58492.34765625, 158477.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-58492.3515625, 158514, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-59549.390625, 158353.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-59568.4765625, 158376.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-60571.08984375, 159149.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-60542.9140625, 159139.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-60350.7578125, 158494.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-60375.8515625, 158510.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-60040.97265625, 158316.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-60046.0078125, 158345.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-60341.9375, 158858.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-60360.6171875, 158879.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-60013.5078125, 158770.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-60043.57421875, 158768.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-60206.19140625, 159380.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-60199.15625, 159410.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-60019.640625, 159001.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-60003.875, 159027.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-59589.76953125, 159177.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-59589.33203125, 159146.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-59835.60546875, 159451.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-59860.90625, 159436.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-59266.8125, 158980.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-59245.953125, 159001.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-57791.265625, 158564.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-57788.53515625, 158377.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-57790.8828125, 158228.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-58123.0234375, 158242.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-58380.08984375, 158848.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-58400.64453125, 158870.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-58053.375, 158988.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-58216.74609375, 158992.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-59867.73828125, 158455.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-59843.78125, 158474.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-58703.1484375, 155529.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-58732, 155529.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-58759.515625, 155529.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-58434.25390625, 154618.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-58453.59765625, 154612.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-58471.8125, 154605.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-58489.25390625, 154599.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-58507.77734375, 154592.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-58786.37890625, 155529.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-59595.51953125, 158705.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-58671.96484375, 156564.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-59543.53125, 158705.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-59494.61328125, 158705.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-59444.80078125, 158705.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-59395.19140625, 158705.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-59345.84765625, 158705.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=40.0, width=40.0, height=12.0, shelter=False))


class Wujah_Al_Hajar(Airport):
    id = 40
    name = "Wujah Al Hajar"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4575000, vhf_low_hz=40050000, vhf_high_hz=121500000, uhf_hz=251600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-81524.375, -22832.533203, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield40_0'))
        self.runways.append(Runway(id=None, name='20-02', main=RunwayApproach(name='20', heading=200, beacons=[]), opposite=RunwayApproach(name='02', heading=20, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-81061.453125, -22970.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-81145.108149116, -22963.7440216, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-81132.4885273, -22987.625568982, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-81113.930704375, -23006.491492389, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-81073.328125, -22949.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-81086.0234375, -22926.443359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))


class Gazipasa(Airport):
    id = 41
    name = "Gazipasa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4600000, vhf_low_hz=40100000, vhf_high_hz=119250000, uhf_hz=251650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(158144.617188, -319392.546875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield41_1'))
        self.beacons.append(AirportBeacon(id='airfield41_2'))
        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[RunwayBeacon(id='airfield41_0', runway_name='08-26', runway_id=1, runway_side='08')]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(158006.0625, -318795.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(158000.46875, -318877.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(157993.921875, -318959.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(157997.203125, -318918.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(158003.1875, -318836.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(158016.9375, -319061.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))


class Deir_ez_Zor(Airport):
    id = 42
    name = "Deir ez-Zor"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4625000, vhf_low_hz=40150000, vhf_high_hz=118100000, uhf_hz=251700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(25465.167969, 389747.03125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield42_1'))
        self.beacons.append(AirportBeacon(id='airfield42_0'))
        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(25592.66796875, 390510.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(25635.443359375, 390708.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(25566.087890625, 390685.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(25648.478515625, 390531, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(25701.109375, 390548.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(25198.212890625, 391118.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(25192.853515625, 391134.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(25187.35546875, 391149.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(25182.232421875, 391164.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(25176.703125, 391180.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(25171.083984375, 391196.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(25165.837890625, 391211.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(25206.853956897, 391276.21510026, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(25180.160946411, 391290.17831586, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(26161.213288282, 388408.19267497, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(26151.639295155, 388436.53977469, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Akrotiri(Airport):
    id = 44
    name = "Akrotiri"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4650000, vhf_low_hz=40200000, vhf_high_hz=128000000, uhf_hz=251750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-35778.628906, -268906.125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield44_2'))
        self.beacons.append(AirportBeacon(id='airfield44_3'))
        self.runways.append(Runway(id=1, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[RunwayBeacon(id='airfield44_1', runway_name='10-28', runway_id=1, runway_side='28'), RunwayBeacon(id='airfield44_0', runway_name='10-28', runway_id=1, runway_side='28')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-36358.76953125, -268523, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C1', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-36311.9140625, -268418.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C2', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-36463.01171875, -268475.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C3', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-36415.34375, -268371.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C4', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-36517.71875, -268123.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E2', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-36463.98828125, -268079.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E1', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-36546.91796875, -267976.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E3', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-36599.19921875, -268016.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E4', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-36802.859375, -267884.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F1', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-36867.51953125, -267791.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F2', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-36896.84375, -267950.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F4', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-36961.92578125, -267856.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F3', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-36835.4609375, -267695.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F7', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-36719.609375, -267636.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-36672.859375, -267659.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-36613.4140625, -267683.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-36566.1484375, -267705.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G9', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-36518.046875, -267725.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G7', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-36541.75, -267715.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G8', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-36591.25, -267694.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-36641.578125, -267672.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-36696.8046875, -267647.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-36742.90625, -267627.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-36686.03125, -267530.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G6', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-36652.2578125, -267547.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G5', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-36619.0546875, -267563.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G4', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-36585.44140625, -267579.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-36549.484375, -267595.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G2', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-35993.66796875, -269122.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-36118.73828125, -269053.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-35896.09765625, -269326.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-35850.76953125, -269570.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-35856.09765625, -269529.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-35829.125, -269466.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-35799.9375, -269506.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-35930.82421875, -269264.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-37085.125, -267803.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F5', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-37057.3359375, -267543.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F6', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-35626.7265625, -270167.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B2', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-35731.87890625, -270189.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B1', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-35430.03515625, -270624.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A3', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-35434.07421875, -270485.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A1', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-35555.16796875, -270636.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A4', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-35565.3203125, -270496.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A2', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-36525.8671875, -267610.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G1', length=21.0, width=15.0, height=8.0, shelter=False))


class Kingsfield(Airport):
    id = 45
    name = "Kingsfield"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4675000, vhf_low_hz=40250000, vhf_high_hz=121000000, uhf_hz=251800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(7596.761963, -199426.492188, terrain), terrain)

        self.runways.append(Runway(id=None, name='24-06', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='06', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(7760.2595443036, -198874.52124089, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(7775.0039815814, -198916.77351947, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))


class Paphos(Airport):
    id = 46
    name = "Paphos"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4700000, vhf_low_hz=40300000, vhf_high_hz=119900000, uhf_hz=251850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-18696.34668, -314208.375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield46_3'))
        self.beacons.append(AirportBeacon(id='airfield46_4'))
        self.beacons.append(AirportBeacon(id='airfield46_5'))
        self.beacons.append(AirportBeacon(id='airfield46_0'))
        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[RunwayBeacon(id='airfield46_1', runway_name='11-29', runway_id=1, runway_side='29'), RunwayBeacon(id='airfield46_2', runway_name='11-29', runway_id=1, runway_side='29')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-18519.71875, -313559.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-18484.078125, -313542.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-18448.640625, -313526.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-18512.640625, -313366.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-18540.3671875, -313379.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-18568.51953125, -313391.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-18595.5078125, -313403.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-18623.134765625, -313416, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-18510.9296875, -313446.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-18539.00390625, -313458.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-18565.427734375, -313470.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-18593.2578125, -313483.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-18751.837890625, -313158.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-18829.986328125, -312978.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-18613.177734375, -313067.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-18664.841796875, -312947.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-18738.138671875, -312821.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-18877.330078125, -312826.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-18936.056640625, -312781.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-18953.400390625, -312788.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-18970.025390625, -312796.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-18987.009765625, -312803.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-19186.84375, -313738.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-19177.86328125, -313836.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-19205.9375, -313910.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-19242.21875, -314004.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-19278.923828125, -314099.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-19285.03515625, -314309.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-19239.32421875, -314411.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-19200.6875, -314523.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-19101.015625, -314609.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-19307.25, -314174.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-19119.83203125, -314153.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-19071.787109375, -314017.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-19151.34765625, -314255.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-19043.912109375, -312697.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-19007.61328125, -312682.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-18972.251953125, -312666.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-18936.779296875, -312650.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-19021.2578125, -312748.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-18985.845703125, -312732.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-18950.16015625, -312716.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-18914.673828125, -312700.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))


class Larnaca(Airport):
    id = 47
    name = "Larnaca"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4725000, vhf_low_hz=40350000, vhf_high_hz=121200000, uhf_hz=251900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-7674.737061, -208843.625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield47_1'))
        self.beacons.append(AirportBeacon(id='airfield47_3'))
        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[RunwayBeacon(id='airfield47_2', runway_name='1#04-22', runway_id=1, runway_side='22'), RunwayBeacon(id='airfield47_0', runway_name='1#04-22', runway_id=1, runway_side='22')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-7843.2055664062, -210062.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-7895.5390625, -210020, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-7938.2109375, -209982.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-7985.0146484375, -209937.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-8104.6875, -209945.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-8157.6640625, -209997.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-8380.060546875, -210250.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-8336.611328125, -210288.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-8292.435546875, -210326.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-8247.189453125, -210365.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-8195.0927734375, -210405.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-8067.0766601563, -210408.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-8120.91796875, -210428.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-8030.1235351563, -210316.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-8185.2456054687, -210069.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-8141.5102539062, -210105.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-8090.4340820312, -210147.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-8035.900390625, -210192.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-6523.8901367188, -208028.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-6464.4912109375, -208077.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-6379.6342773438, -208149.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-6653.2021484375, -208187.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-6584.078125, -208244.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-6505.8618164062, -208312.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-6379.9711914063, -207813.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-6315.1684570312, -207872.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-6347.9721679687, -207843.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-6175.6899414062, -207999.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-6243.2578125, -208073.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-6323.8002929688, -208011.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-6365.2827148437, -207976.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-6402.2626953125, -207943.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-8131.8579101563, -209971.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-8204.5087890625, -210028.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-8079.0903320313, -209904.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-8018.7875976563, -209908.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-6200.3994140625, -208045.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-6290.712890625, -208041.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-6437.2817382812, -207913.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-6275.7880859375, -208117.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-6304.7729492187, -208148.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-6450.3911627919, -208421.86412191, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-6433.0324634475, -208402.4133702, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-6416.0255037334, -208382.6222308, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-6399.0373501031, -208363.41488626, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=11.0, shelter=False))


class Lakatamia(Airport):
    id = 48
    name = "Lakatamia"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4750000, vhf_low_hz=40400000, vhf_high_hz=120200000, uhf_hz=251950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(19561.164063, -234985.75, terrain), terrain)

        self.runways.append(Runway(id=None, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(19755.73828125, -234857.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H5', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(19771.982421875, -234896.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H6', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(19788.00390625, -234935.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H7', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(19803.666015625, -234974.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H8', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(19700.041015625, -234890.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(19720.837890625, -234940.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(19731.197265625, -234968.109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(19710.439453125, -234915.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=30.0, width=23.0, height=10.0, shelter=False))


class Ercan(Airport):
    id = 49
    name = "Ercan"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4775000, vhf_low_hz=40450000, vhf_high_hz=120200000, uhf_hz=252000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(24250.327148, -218240.28125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield49_0'))
        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[RunwayBeacon(id='airfield49_1', runway_name='11-29', runway_id=1, runway_side='29')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(24540.85546875, -218264.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(24418.74609375, -218001.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(24522.02734375, -218224.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(24503.546875, -218185.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(24484.994140625, -218145.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(24466.78515625, -218106.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(24437.859375, -218042.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))


class Gecitkale(Airport):
    id = 50
    name = "Gecitkale"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4825000, vhf_low_hz=40550000, vhf_high_hz=120000000, uhf_hz=252100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(32144.729634, -197767.51907, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield50_1'))
        self.beacons.append(AirportBeacon(id='airfield50_0'))
        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(31787.678962334, -196740.64115297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(31782.799899441, -196670.25006573, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(31778.895009085, -196592.03361997, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))


class Pinarbashi(Airport):
    id = 51
    name = "Pinarbashi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4850000, vhf_low_hz=40600000, vhf_high_hz=121000000, uhf_hz=252150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(38639.882813, -238774.6875, terrain), terrain)

        self.runways.append(Runway(id=None, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(39076.5546875, -238808.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(39123.921875, -238819.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(39100.58203125, -238814.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(39061.0546875, -238777.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(39259.328125, -238818.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Naqoura(Airport):
    id = 52
    name = "Naqoura"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4875000, vhf_low_hz=40650000, vhf_high_hz=122000000, uhf_hz=252200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-209938.1875, -78642.609375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-209818.171875, -78489.2578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-209946.015625, -78453.2109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-209981.640625, -78541.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-210024.25, -78626.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-210058.65625, -78711.3203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-209858.875, -78579.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-209899.1875, -78671.0703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-209930.640625, -78770.2109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-209957.484375, -78831.2421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=42.0, width=34.0, height=14.0, shelter=False))


class H3(Airport):
    id = 53
    name = "H3"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4900000, vhf_low_hz=40700000, vhf_high_hz=122000000, uhf_hz=252250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-235405.664063, 352522.65625, terrain), terrain)

        self.runways.append(Runway(id=2, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-236204.984375, 353533.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-236060.953125, 353596.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-236117.78125, 353860.93830397, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-236093.796875, 353976.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-235912.546875, 354091.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-234657.34375, 351574.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-234702.96875, 351678.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-234654.859375, 351339.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-234699.984375, 351402.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-234725.203125, 351392.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-234733.296875, 351488.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-234757.90625, 351479.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-234750.15625, 351382.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-234782.484375, 351470.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-234879.28125, 351982.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-234756.96875, 352010.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-235700.796875, 354045.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-235601.515625, 354081.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-235055.28125, 351289.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-235046.828125, 351181.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-234934.23604606, 350975.56001456, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-234616.81939311, 351082.96161875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-234844.40625, 352219.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-234890.953125, 352333.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-234975.453125, 352411.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-235067.796875, 352486.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-235894.328125, 353069.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-235823.875, 352906.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-235899.046875, 352854.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-235927.20681035, 352909.50537931, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-235963.7257712, 353000.11151802, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-235615.57884385, 353895.9704032, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-237994.71875, 351788.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-237906.703125, 351852.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-238015.9375, 351613.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-237872.140625, 351644.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-237785.5, 351748.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-237629.75, 351764.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-237585.703125, 351878.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-237473.578125, 351877.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-237538.34375, 350994.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-237492.453125, 351146.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-237374.125, 351190.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-237226, 351423.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-237044.296875, 351410, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-236897.4375, 351436.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-237371, 351315.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-237353, 351354.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-237335.0625, 351392.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-237317.21875, 351430.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-235199.359375, 353386.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-235493.34375, 353549.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-235503.96875, 353576.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-235514.671875, 353603.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-235525.171875, 353629.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-235535.53125, 353656.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-235545.78125, 353681.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-235555.84375, 353707.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-235566.21875, 353733.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-235576.34375, 353759.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-235230.234375, 353423.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-235240.5625, 353449.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-235251.15625, 353475.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-235261.671875, 353502.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-235277.0625, 353603.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-235305.234375, 353591.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-235333.5625, 353579.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-235360.3125, 353568.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))


class H3_Northwest(Airport):
    id = 54
    name = "H3 Northwest"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-220000.35156, 338483.561903, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-220580.53125, 338708.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-220565.3125, 338684.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-220550.53125, 338660, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-220535.859375, 338635.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-220520.84375, 338610.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-220505.796875, 338586.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-220490.9375, 338561.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-220475.46875, 338536.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-220460.625, 338511.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-220417.21875, 338572.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-220432.25, 338596.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-220446.8125, 338621.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-220461.28125, 338645.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-220476.09375, 338670.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-220490.9375, 338695.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-220505.59375, 338719.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-220520.84375, 338745.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-220467.06516497, 339750.119015, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-220621.56555203, 339790.43324201, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-220895.36765434, 339639.54727977, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-220938.17646707, 339461.11671036, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-219549.32873545, 337230.45870543, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-219383.88293833, 337189.65486839, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-219121.97410222, 337355.96923385, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-219084.2906963, 337516.60061388, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-221212.625, 339357.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-221050.203125, 339371.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-220334.34375, 339750.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-220336.09375, 339583.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))


class H3_Southwest(Airport):
    id = 55
    name = "H3 Southwest"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-256859.445313, 339219.1875, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-256947.3125, 339964.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-256962.6875, 339988.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-256977.625, 340013.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-256992.453125, 340037.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-257007.625, 340061.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-257022.84375, 340086.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-257037.859375, 340110.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-257081.59375, 340051.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-257066.96875, 340026.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-257051.984375, 340001.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-257036.984375, 339977.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-257022.171875, 339952.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-257006.75, 339927.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-257053.5, 340136.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-257111.5, 340100, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-257096.328125, 340075.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-257037.03125, 340798.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-257125.015625, 340646.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-257309.37862583, 340495.28859731, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-257467.59844968, 340538.65627391, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-257691.671875, 339967.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-257815.21875, 340040.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-257758.94375851, 340235.12660666, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-257727.01595999, 340388.81513512, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-255956.56798657, 338243.79415563, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-255994.5719956, 338088.14657875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-256289.19186905, 337925.63505971, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-256447.83882114, 337965.15482313, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-256979.046875, 340322.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-257040.640625, 340425.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))


class Ruwayshid(Airport):
    id = 57
    name = "Ruwayshid"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4925000, vhf_low_hz=40750000, vhf_high_hz=122100000, uhf_hz=252300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-294533.859375, 295074.640625, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-294232.71875, 293663.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-294395.71875, 296409.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-294550.21875, 293628.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-294932.75, 296355.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-294517.5, 296512.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-294834.34375, 296480.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-294674.125, 293732.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-294132.125, 293784.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-295168.625, 295229.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-295172.34375, 295269.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-295176.09375, 295309.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-295179.75183683, 295349.74448951, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-295184.21875, 295389.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-295188.40625, 295429.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-295192.25, 295469.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-295196.0625, 295509.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-295119.9375, 295516.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-295116.28125, 295477.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-295111.53125, 295437.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-295107.90625, 295397.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-295102.75, 295357.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-295098.84375, 295317.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-295095.1875, 295277.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-295091.03125, 295237.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))


class Sanliurfa(Airport):
    id = 58
    name = "Sanliurfa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4950000, vhf_low_hz=40800000, vhf_high_hz=118400000, uhf_hz=252350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(264719.125, 273812.4375, terrain), terrain)

        self.runways.append(Runway(id=None, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(264257.1139012, 274104.38323455, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(264224.7880478, 274075.39126774, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(264193.11898774, 274031.42177725, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(264288.85452552, 274134.14664353, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(264352.7764853, 274193.61695712, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(264384.77633455, 274223.55200428, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(264448.58228723, 274281.74945693, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(264525.51512884, 274337.86286121, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(264480.55062396, 274310.28425574, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(264321.19591808, 274163.97244661, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(264416.45122735, 274252.52918335, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))


class Kharab_Ishk(Airport):
    id = 59
    name = "Kharab Ishk"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4975000, vhf_low_hz=40850000, vhf_high_hz=122200000, uhf_hz=252400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(164825.84375, 245883.84375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(164830.796875, 246057.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(164866.21875, 246043.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(164928.34375, 246065.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(164928.421875, 246119.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(164928.578125, 246093.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(164917.3125, 245663.328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(164875.671875, 245662.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(164837.046875, 245660.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(164798.203125, 245658.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(164759.546875, 245653.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(164719.984375, 245651.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))


class Tal_Siman(Airport):
    id = 60
    name = "Tal Siman"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5025000, vhf_low_hz=40950000, vhf_high_hz=121900000, uhf_hz=252500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(133191.875, 276361.453125, terrain), terrain)

        self.runways.append(Runway(id=1, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(133191.78125, 276637.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(133185.90625, 276691.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(133169.171875, 276687.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(133152.140625, 276683.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))


class At_Tanf(Airport):
    id = 63
    name = "At Tanf"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5050000, vhf_low_hz=41000000, vhf_high_hz=121100000, uhf_hz=252550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-172365.28125, 247031.90625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-172390.890625, 247005.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-172339.65625, 247058.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Abu_al_Duhur,
    Adana_Sakirpasa,
    Al_Qusayr,
    An_Nasiriyah,
    Tha_lah,
    Beirut_Rafic_Hariri,
    Damascus,
    Marj_as_Sultan_South,
    Al_Dumayr,
    Eyn_Shemer,
    Gaziantep,
    H4,
    Haifa,
    Hama,
    Hatay,
    Incirlik,
    Jirah,
    Khalkhalah,
    King_Hussein_Air_College,
    Kiryat_Shmona,
    Bassel_Al_Assad,
    Marj_as_Sultan_North,
    Marj_Ruhayyil,
    Megiddo,
    Mezzeh,
    Minakh,
    Aleppo,
    Palmyra,
    Qabr_as_Sitt,
    Ramat_David,
    Kuweires,
    Rayak,
    Rene_Mouawad,
    Rosh_Pina,
    Sayqal,
    Shayrat,
    Tabqa,
    Taftanaz,
    Tiyas,
    Wujah_Al_Hajar,
    Gazipasa,
    Deir_ez_Zor,
    Akrotiri,
    Kingsfield,
    Paphos,
    Larnaca,
    Lakatamia,
    Ercan,
    Gecitkale,
    Pinarbashi,
    Naqoura,
    H3,
    H3_Northwest,
    H3_Southwest,
    Ruwayshid,
    Sanliurfa,
    Kharab_Ishk,
    Tal_Siman,
    At_Tanf,
]

