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
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=122200000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(76048.957031, 111344.925781, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(76271.684679983, 112805.5380375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(76276.650781432, 112764.25817787, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(76279.27455726, 112725.42722994, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(76282.937400979, 112691.84266077, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=4400000, vhf_low_hz=39700000, vhf_high_hz=121100000, uhf_hz=251250000)

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
                airplanes=True, slot_name='A03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(219815.28125, -46864.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(219762.140625, -47053.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A18', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(219807.296875, -47023.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A19', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(219849.4375, -47014.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A20', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(219893.08035903, -47003.57555583, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(219488.75, -47186.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A11', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(219525.84375, -47211.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A12', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(219562.8125, -47237.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A13', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(219600.07628817, -47262.740350671, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A14', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(219739.8530457, -47085.899195532, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A17', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(219717.84025563, -47121.067510432, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A16', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(219694.79127086, -47155.756806915, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A15', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(219569.15216193, -47074.543446363, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(219602.96875, -47017.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A09', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(219634.609375, -46966.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A08', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(219662.421875, -46926.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=41.0, width=41.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='A05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(219518.03125, -47376.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D09', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(219730.00784537, -46883.067098551, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=41.0, width=41.0, height=18.0, shelter=False))


class Al_Qusayr(Airport):
    id = 3
    name = "Al Qusayr"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4675000, vhf_low_hz=40250000, vhf_high_hz=119200000, uhf_hz=251800000)

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
                crossroad_idx=10, position=mapping.Point(-52510.928888841, 60964.632030876, self._terrain), large=False, heli=False,
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
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-51989.81640625, 61405.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=36.0, width=36.0, height=15.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=4925000, vhf_low_hz=40750000, vhf_high_hz=122300000, uhf_hz=252300000)

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
    atc_radio = AtcRadio(hf_hz=5175000, vhf_low_hz=41250000, vhf_high_hz=118000000, uhf_hz=252800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-258434.929688, 40368.673828, terrain), terrain)

        self.runways.append(Runway(id=1, name='05R-23L', main=RunwayApproach(name='05R', heading=50, beacons=[]), opposite=RunwayApproach(name='23L', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-257744.859375, 41773.9140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H24', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-257741.6875, 41840.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H25', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-257738.75, 41900.48828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H26', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-257736.125, 41959.5234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H27', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-259539.015625, 39077.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-259479.375, 39108.67578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-259420.046875, 39139.62109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-259367.78125, 39167.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-257191.125, 41447.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H21', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-257129.421875, 41480.83203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H22', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-257072.59375, 41510.94140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H23', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-259510.171875, 38984.03515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-258971, 38643.08203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='2', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-257099.953125, 41608.09765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='8', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-257082.09375, 41580.37109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='7', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-259335.203125, 39263.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-259523.390625, 39014.4921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-258937.359375, 38642.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='1', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-259343.40625, 39296.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-257264.21875, 41296.27734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='5', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-257669.515625, 41949.76171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-257638.015625, 41946.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='9', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-258763.09375, 38944.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-258795.265625, 38934.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='4', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-257816.6875, 41666.76171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-257847.5625, 41656.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-257270.375, 41328.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='6', length=21.0, width=15.0, height=8.0, shelter=False))


class Beirut_Rafic_Hariri(Airport):
    id = 6
    name = "Beirut-Rafic Hariri"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5375000, vhf_low_hz=41650000, vhf_high_hz=118900000, uhf_hz=253200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-131310.8125, -42286.496094, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield6_7'))
        self.beacons.append(AirportBeacon(id='airfield6_0'))
        self.runways.append(Runway(id=3, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[RunwayBeacon(id='airfield6_1', runway_name='16-34', runway_id=1, runway_side='16'), RunwayBeacon(id='airfield6_4', runway_name='16-34', runway_id=1, runway_side='16')]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.runways.append(Runway(id=2, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-131572.95132889, -41980.701114046, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G20', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-131640.75636211, -41997.389934053, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G19', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-131693.50871055, -42002.417098267, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G18', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-131786.734375, -41945.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G17', length=41.0, width=41.0, height=18.0, shelter=False))
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
                crossroad_idx=13, position=mapping.Point(-131762.86985802, -41881.316059676, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G16', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-131775.64766656, -41655.835184735, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G7', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-131729.4256742, -41634.840623576, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G6', length=41.0, width=41.0, height=18.0, shelter=False))
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
                crossroad_idx=20, position=mapping.Point(-131676.96044324, -41623.474831325, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G5', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-131595.9375, -41841.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G13', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-131650.879134, -41854.334568999, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G14', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-131702.98196163, -41864.615199175, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G15', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-131681.85462809, -41765.822834488, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G11', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-131631.92772932, -41750.768433946, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G12', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-131839.48340533, -41732.609644989, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G8', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-131794.03125, -41787.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G9', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-131733.61313272, -41780.594146085, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G10', length=41.0, width=41.0, height=18.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=5400000, vhf_low_hz=41700000, vhf_high_hz=118500000, uhf_hz=253250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-178652.320313, 52081.296875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_2'))
        self.beacons.append(AirportBeacon(id='airfield7_4'))
        self.beacons.append(AirportBeacon(id='airfield7_5'))
        self.runways.append(Runway(id=2, name='05R-23L', main=RunwayApproach(name='05R', heading=50, beacons=[RunwayBeacon(id='airfield7_3', runway_name='05R-23L', runway_id=2, runway_side='05R'), RunwayBeacon(id='airfield7_6', runway_name='05R-23L', runway_id=2, runway_side='05R')]), opposite=RunwayApproach(name='23L', heading=230, beacons=[])))
        self.runways.append(Runway(id=1, name='05L-23R', main=RunwayApproach(name='05L', heading=50, beacons=[]), opposite=RunwayApproach(name='23R', heading=230, beacons=[RunwayBeacon(id='airfield7_1', runway_name='05L-23R', runway_id=1, runway_side='23R'), RunwayBeacon(id='airfield7_0', runway_name='05L-23R', runway_id=1, runway_side='23R')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-182109.68730281, 50138.411195125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='027', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-182090.50745098, 50170.371308862, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='028', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-182157.35917781, 50081.567445125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='025', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-182133.70292781, 50109.954163875, self._terrain), large=False, heli=True,
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
                crossroad_idx=13, position=mapping.Point(-182177.54667781, 50057.739320125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='024', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-180549.03125, 52349.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='605', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-180023.578125, 51576.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-180034.046875, 51822.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-180113.07301291, 51653.008890767, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-180208.52040031, 51742.390573699, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-179969.98563706, 51708.728721635, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-180062.67223673, 51614.085432075, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-180167.58493633, 51704.408799037, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-180093.234375, 51938.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-180503.359375, 52077.76953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='405', length=36.0, width=36.0, height=15.0, shelter=False))
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
                crossroad_idx=29, position=mapping.Point(-180451.55323574, 52033.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='401', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-180545.109375, 51920.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='404', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-179813.5348895, 51569.600168133, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='201', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-179976.46875, 51775.23046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-179954.453125, 51551.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-179840.0625, 51725.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-179999.09375, 51471.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='205', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-179927.68689427, 51509.265913951, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='204', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-180440.125, 52258.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='603', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-180491.015625, 52300.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='604', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-180378.5625, 52206.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='602', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-180325.46875, 52162, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='601', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-182418.078125, 50021.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='030', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-182505.875, 49926.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='031', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-182591.890625, 49820.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='032', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-182434.578125, 49777.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='033', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-182357.765625, 49878.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='034', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-180319.75, 51928.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='302', length=41.0, width=41.0, height=18.0, shelter=False))
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
                crossroad_idx=52, position=mapping.Point(-179800.18860741, 51498.278184413, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='202', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-179854.6385495, 51510.113618267, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='203', length=41.0, width=41.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='409', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-180597.59375, 51963.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='408', length=36.0, width=36.0, height=15.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=5425000, vhf_low_hz=41750000, vhf_high_hz=122900000, uhf_hz=253300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-171711.042484, 48237.622439, terrain), terrain)

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
                crossroad_idx=5, position=mapping.Point(-171773.43274176, 48101.956435524, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=5450000, vhf_low_hz=41800000, vhf_high_hz=120300000, uhf_hz=253350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-158713.039063, 73973.316406, terrain), terrain)

        self.runways.append(Runway(id=None, name='24-06', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='06', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-158232.625, 75689.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-158510.39200927, 73433.454503081, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-158870.78125, 72584.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-158795.01213063, 73083.441785266, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-157630.546875, 75222.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-158201.234375, 74386.796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-158736.40625, 73216.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-158459.09215775, 73546.827188693, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-157449.46875, 75771.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-157649.921875, 75224.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-157874.71572384, 75070.081541057, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-158183.984375, 75940.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-158565.07776575, 75465.532158081, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-158137.6875, 76126.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-159469.859375, 72838.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-158177.671875, 72212.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-158523.87522646, 75154.314342813, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-158756.796875, 73170.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-157610.3125, 75220.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-158184.4375, 74424.3671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='61', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-157770.046875, 74842.5546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-159448.609375, 73116.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-158554.98292005, 75493.991031118, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-158921.203125, 75350.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-158541.5625, 72597.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-157670.25, 75227.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-157591.046875, 75218.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-157859.14238948, 75102.313033751, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-159437, 73087.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-158538.359375, 75180.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-158174.84375, 72182.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-158761.46875, 72028.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-158419.015625, 75930.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-158722.96875, 72847.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-158556.40412279, 72571.901713744, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-157570.15625, 75215.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-157912.9645902, 74982.028251152, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-158948.625, 75362.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-157710.171875, 75231.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-157747.66974212, 75288.515921786, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-157627.93699891, 75434.466475257, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-157734.43702442, 74958.093336988, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-157680.2971749, 75131.958529829, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-158339.34375, 75523.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-158431.63233876, 75707.951801216, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-158889.359375, 72559.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-157622.96875, 75800.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-158149.359375, 74504.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='59', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-158775.24650563, 73127.230847766, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-158242.609375, 75715.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-158814.5723439, 75600.606579272, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-158377.15412279, 72713.182963744, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-157471.734375, 75794.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-158132.5, 74540.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='58', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-158717.8125, 73261.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-158707.703125, 72821.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-157650.10971987, 75128.638536287, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-158488.328125, 72776.9140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-157630.23520172, 75404.140668864, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-158166.375, 74464.6796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='60', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-157898.93926448, 75013.680221251, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-158363.05764243, 75542.013931252, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-158785.56993033, 75609.825711438, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-158359.90412279, 72737.479838744, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-157690.15625, 75229.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-159440.78125, 72832.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-157653.75041842, 75803.321212356, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))


class Eyn_Shemer(Airport):
    id = 10
    name = "Eyn Shemer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=123400000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-283529.25, -92673.230469, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-282995.65625, -92976.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-283142.84375, -93232.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-283992.8125, -92122.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-283139.125, -92764.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-283140.40625, -92985.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-283478.9375, -92496.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-283100.9375, -93110.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-283533.75, -92335.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-283443.8125, -92651.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-283484.6875, -92572.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-283520.09375, -92411.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-283483.90625, -92391.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-283482.875, -92456.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-283263.46875, -93215.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-283295.84375, -93085.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))


class Gaziantep(Airport):
    id = 11
    name = "Gaziantep"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=120100000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(210333.625365, 147313.672429, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield11_2'))
        self.beacons.append(AirportBeacon(id='airfield11_3'))
        self.runways.append(Runway(id=None, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(210293.7151899, 146534.1732596, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(210303.140625, 146500.015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(210091.69474545, 146991.82531605, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
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
                crossroad_idx=7, position=mapping.Point(210066.03116915, 147069.54461976, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(210127.386769, 146917.80824201, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(210116.46875, 146956.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(210125.57582934, 146873.20031605, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(210147.87270434, 146794.82001544, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=122600000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-279366.758024, 207219.267431, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-279252.4375, 206049.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-279193.1875, 205773.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-278882.15625, 205852.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-279847.09375, 208566.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-279210.96875, 206236.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-279743.84375, 208032.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-279479.375, 208377.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-279928.84375, 208431.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-279673.875, 207975.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-279692.46875, 208047.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-278800.1875, 206001, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-279536.375, 208624.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-279334.625, 205872.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-279706.78125, 207967.796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-279397.1875, 208544.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-279743.54494318, 208323.88309921, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-279736.21875, 207961.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-278954.28125, 206120.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))


class Haifa(Airport):
    id = 13
    name = "Haifa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=127800000, uhf_hz=250200000)

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
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118050000, uhf_hz=250250000)

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
                crossroad_idx=7, position=mapping.Point(9098.4317891569, 73141.129746913, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(9089.5187032194, 73189.122725565, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(9082.2901875944, 73239.321894804, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(9072.6722584529, 73293.262559413, self._terrain), large=False, heli=True,
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
                crossroad_idx=15, position=mapping.Point(8881.2166710809, 74369.44754753, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(8812.8246511148, 74740.344830882, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=128500000, uhf_hz=250300000)

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
                airplanes=True, slot_name='03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(147595.453125, 38823.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(147625, 38852.58984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(147866.75, 39084.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(147836.515625, 39055.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(147715.125, 38939.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(147775.15625, 38996.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=41.0, width=41.0, height=18.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=122100000, uhf_hz=360100000)

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
                crossroad_idx=2, position=mapping.Point(220781.8302372, -36704.158362204, self._terrain), large=False, heli=True,
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
                crossroad_idx=7, position=mapping.Point(220586.12372976, -35377.907520244, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(220609.52390269, -35345.298944421, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(220631.921875, -35312.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(220654.57054157, -35279.649010185, self._terrain), large=False, heli=True,
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
                crossroad_idx=14, position=mapping.Point(220746.54038484, -35148.352884845, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(220807.734375, -35045.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(220853.48249166, -35075.721993738, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(220899.078125, -35108.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(220965.453125, -35013.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(220919.37871535, -34981.464576497, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(220874.29499166, -34950.044991664, self._terrain), large=False, heli=True,
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
                crossroad_idx=24, position=mapping.Point(221118.88626509, -34820.367323002, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(221240.765625, -34645.94921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(221362.25030543, -34472.867225679, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(221415.515625, -34336.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='84', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(221455.80847921, -34365.070159784, self._terrain), large=False, heli=True,
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
                crossroad_idx=35, position=mapping.Point(221352.39794996, -35618.01953125, self._terrain), large=False, heli=True,
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
                crossroad_idx=43, position=mapping.Point(220474.90436666, -36622.637241684, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=118100000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(115350.483441, 187069.20336, terrain), terrain)

        self.runways.append(Runway(id=None, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(114840.78125, 188132.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(115237.09864806, 188509.82785079, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(115251.04978944, 188435.65652421, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(115610.015625, 188144.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(115229.53125, 188533.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(114970.328125, 188493.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(115387.28125, 187936.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(114899.421875, 187879.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(114820.4765625, 188414.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(115275.9140625, 188302.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(115264.91378829, 188360.42478944, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(115246.45021056, 188460.62472579, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(115666.921875, 187660.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(115201.296875, 188650.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(114886.16398448, 188621.90514866, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(114916.10926987, 188617.35809764, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(115360.2109375, 188654.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(115255.82322694, 188410.65652421, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(115598.4921875, 188546.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(114965.78125, 188002.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(115500.3046875, 187918.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(115390.9375, 188318.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(115476.6471309, 188641.26112233, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(115260.60420272, 188385.78443865, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(115033.0859375, 187674.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(115241.77024885, 188484.92451523, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(115158.53125, 188437.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(115488.72413042, 187471.1654883, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(115269.38572694, 188336.73464921, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))


class Khalkhalah(Airport):
    id = 18
    name = "Khalkhalah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=122500000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-217201.976563, 53275.345703, terrain), terrain)

        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.runways.append(Runway(id=2, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-217622.046875, 56589.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-217564.34375, 56810, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-217996.234375, 56259.5703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-217696.828125, 56844.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-218116.46875, 55835.30859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-218050.796875, 56036.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-218171.03125, 55612.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-218243.96875, 55867.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-217864.5, 56225.85546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-217750.171875, 56622.94140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-217920.921875, 56003.77734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-218299.40625, 55644.52734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-218250.828125, 53425.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-217634.5625, 53101.14453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-217539.90625, 53069.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-217461.125, 53000.921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-217712.625, 53168.7265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-217982.96875, 53285.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-218151.328125, 53375.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-217891.9375, 53233.8828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-215987.015625, 52789.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-216101.65625, 52853.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-216043.546875, 52819.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-216011.40625, 52803.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-216074.609375, 52836.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-217986.484375, 57307.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-218481.53125, 53551.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-215883.9375, 52822.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-218599.34375, 53658.78515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-218571.8125, 53842.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-218107.578125, 54195.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-218107.90625, 54165.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-216192.8125, 52301.66015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-215903.734375, 52357.25390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-216059.53125, 52221.00390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-215750.25, 52284.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-215875.390625, 52365.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-215851.765625, 52713.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-215737.375, 52689.80078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-215613.0625, 52575.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-218563.625, 53813.66796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-217744.34375, 57152.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-217772.625, 57164.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-217712.90625, 57641.22265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-218062.171875, 57020.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-218350.90625, 54182.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-217979.421875, 57278.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-218040, 57041.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-215878.125, 52726.46484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-218393.625, 54069.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-217911.828125, 57664.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-217932.609375, 57684.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-217719.515625, 57668.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-217858.8125, 57466.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-217847.171875, 57492.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))


class King_Hussein_Air_College(Airport):
    id = 19
    name = "King Hussein Air College"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118300000, uhf_hz=250450000)

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
                airplanes=True, slot_name='21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-296317.5625, 24213.353515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-297239.13984637, 26143.442253059, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-297232.85658389, 26258.429971188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-295341.53125, 24280.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-295459.44976252, 24166.80340192, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-295347.96875, 24161.236328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-297119.25181292, 26136.364902449, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-295451.09918875, 24286.377999792, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=41.0, width=41.0, height=18.0, shelter=False))


class Kiryat_Shmona(Airport):
    id = 20
    name = "Kiryat Shmona"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=118400000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-199486.164063, -34500.691406, terrain), terrain)

        self.runways.append(Runway(id=None, name='03-21', main=RunwayApproach(name='03', heading=30, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-199732.59635582, -34827.335558484, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-199697.39911786, -34795.046338193, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-199716.51126095, -34812.609113838, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-199754.34243356, -34844.651769012, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-199866.359375, -35206.71484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))


class Bassel_Al_Assad(Airport):
    id = 21
    name = "Bassel Al-Assad"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=118100000, uhf_hz=250600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(41994.498047, 5841.909424, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield21_2'))
        self.beacons.append(AirportBeacon(id='airfield21_3'))
        self.runways.append(Runway(id=None, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(43255.4453125, 5898.8120117188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(43002.00390625, 6219.2875976562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='46', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(42998.89453125, 6141.4541015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(43279.65625, 5898.3256835938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(42803.0859375, 6099.0439453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(42633.26953125, 5365.3383789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(43328.1697488, 5897.4594726562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(43303.921875, 5897.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(42596.24609375, 6145.3603515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(42803.91015625, 6138.033203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(42804.98046875, 6179.291015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(42805.54296875, 6219.310546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(42807.046875, 6260.06640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(42807.4296875, 6298.9165039062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(42809.375, 6338.119140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(43174.31640625, 5382.1723632812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(43154.30859375, 5383.3178710938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(42929.24609375, 6348.845703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='44', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(43254.48046875, 5379.2241210938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(43214.78125, 5381.2548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(42810.33984375, 6375.1801757812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(43234.01171875, 5380.5200195312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(43194.15625, 5381.4697265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(43093.8984375, 5384.1088867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(43141.911760486, 5457.2491133691, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(43118.036760486, 5457.8316329003, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(43164.673479236, 5456.7867110253, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(43094.966447986, 5458.5157149316, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(42843.66015625, 5142.7290039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(43071.646135486, 5458.7867110253, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(42752.510324383, 5376.2320391764, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(43113.3515625, 5383.8706054688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(43048.353166736, 5458.8907149316, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(43024.962541736, 5461.1436446191, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(42987.23046875, 6474.1064453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='49', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(43123.36328125, 6467.470703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='53', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(42925.5703125, 6191.8510742188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(42923.68359375, 6111.470703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(43004.6953125, 6373.3154296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(42927.828125, 6270.6650390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='43', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(43003.1875, 6297.880859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='47', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(43098.953125, 6175.123046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='50', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(43102.6328125, 6336.0502929688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='52', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(43100.8359375, 6255.427734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='51', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(42518.8515625, 5371.0561523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(42633.4140625, 5406.3588867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(42520.2109375, 5418.8876953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(42360.31640625, 6147.6088867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(42518.5859375, 6146.2915039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(42672.98828125, 6143.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(43133.53125, 5383.8251953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(42439.484375, 6146.9443359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(43001.911760486, 5460.8121016503, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))


class Marj_as_Sultan_North(Airport):
    id = 22
    name = "Marj as Sultan North"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4200000, vhf_low_hz=39300000, vhf_high_hz=122700000, uhf_hz=250850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-170244.028992, 47506.718825, terrain), terrain)

        self.runways.append(Runway(id=None, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-170310.00453579, 47426.078873266, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-170282.3996441, 47602.275949383, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-170234.984375, 47371.68359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-170108.171875, 47430.20703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-170152.8508702, 47439.932835718, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-170197.40058013, 47447.099040851, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-170167.34167256, 47623.259376855, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-170180.87622437, 47543.061494415, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-170136.09853447, 47536.38671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-170188.890625, 47496.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-170302.03578579, 47470.754654516, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-170294.78578579, 47514.680435766, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-170287.89516079, 47557.676529516, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-170091.03603447, 47529.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=42.0, width=34.0, height=14.0, shelter=False))


class Marj_Ruhayyil(Airport):
    id = 23
    name = "Marj Ruhayyil"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=39350000, vhf_high_hz=120800000, uhf_hz=250900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-193677.15625, 45844.763672, terrain), terrain)

        self.runways.append(Runway(id=1, name='06L-24R', main=RunwayApproach(name='06L', heading=60, beacons=[]), opposite=RunwayApproach(name='24R', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-194252.21875, 44232.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-194282.171875, 44230.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-194587.84375, 44375.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-194605.65625, 44400.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-194124.59375, 44277.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-194099.359375, 44293.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-194128.546875, 44531.37109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-194100.28125, 44540.37109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-194481.13144086, 44800.930833088, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-194557.22085977, 44856.044618397, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-194976.140625, 44896, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-194908.765625, 45020.35546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-195966.96875, 44616.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-195829.359375, 44794.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-195804, 44903.04296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-193736.6875, 47613.01171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-193710.59375, 47741.51953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-193616.84375, 47589.70703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-193603.171875, 47617.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-193324.21875, 47615.76171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-193352.5, 47604.83203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-193307, 47385.18359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-193221.015625, 47472.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-192887.96875, 47039.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-192876.484375, 47011.20703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-192748.21875, 47334.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-192731.890625, 47309.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-193781.50890089, 47134.854924981, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-193755.44707064, 47176.747544082, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-193735.73378172, 47216.709503388, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-193717.56083889, 47256.392552861, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-193698.4421681, 47295.187934472, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-193674.89189071, 47343.662073311, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-193145.046875, 45821.81640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-193091.640625, 45756.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-193046.234375, 45800.98046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-193058.59375, 45855.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-193030.953125, 45971.74609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-192985.5625, 46058.47265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-192934.234375, 46148.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-192870.375, 46173.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-192853.8125, 46237.57421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-192938.984375, 46233.91796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-192575.625, 46483.01953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-192509.140625, 46455.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-192536.6875, 46555.109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-192516.875, 46622.80859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-192445.21875, 46657.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-192450.46875, 46732.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-192425.90625, 46791.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-192350.171875, 46765.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-192323.75, 46823.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-192397.734375, 46858.17578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.0, width=23.0, height=10.0, shelter=False))


class Megiddo(Airport):
    id = 24
    name = "Megiddo"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=119900000, uhf_hz=250950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-266965.0625, -71068.835938, terrain), terrain)

        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-266610.71875, -70120.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-266648.78860529, -70108.405812713, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-267191.78125, -70296.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-267245.28125, -70415.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-267232.3125, -70387.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-267218.96875, -70356.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-267204.59375, -70325.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-266686.0625, -70094.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-266721.9375, -70082.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-266756.28125, -70070.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-266791.84375, -70058.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-267223.5625, -70472.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-267202.84375, -70483.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-267181.90625, -70493.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-267160.96875, -70504.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-267140.15625, -70514.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-266539.21875, -70104.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-266836.46875, -70719.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-266800.9375, -70740.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-266855.75, -70709.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-266966.875, -72279.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-266782.8125, -70750.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-266818.9375, -70729.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-266765.65625, -70760.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-266966.9375, -72310.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-267308.81360741, -70483.504355277, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=41.0, width=41.0, height=18.0, shelter=False))


class Mezzeh(Airport):
    id = 25
    name = "Mezzeh"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4275000, vhf_low_hz=39450000, vhf_high_hz=120700000, uhf_hz=251000000)

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
    atc_radio = AtcRadio(hf_hz=4300000, vhf_low_hz=39500000, vhf_high_hz=120600000, uhf_hz=251050000)

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
    atc_radio = AtcRadio(hf_hz=4325000, vhf_low_hz=39550000, vhf_high_hz=119100000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(125576.863281, 123125.304688, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield27_1'))
        self.beacons.append(AirportBeacon(id='airfield27_2'))
        self.beacons.append(AirportBeacon(id='airfield27_0'))
        self.runways.append(Runway(id=None, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(125937.7890625, 123365.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(125318.32396954, 122730.73241458, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(125262.703125, 124155, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(125908.5859375, 123454.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(125324.70325696, 122681.63859861, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(125409.44001188, 122841.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(125126.828125, 124845.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(125961.3984375, 123244.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(125422.765625, 122744.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(125223.34375, 124425.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(125252.3125, 124267.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(125305.20576884, 122828.02141111, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(125917.8732185, 123289.60916917, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(125843.4921875, 123610.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(125903.2265625, 123620.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(125429.66523042, 122696.01571279, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(125893.68898227, 123405.12755129, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(125219.81985313, 124455.78904898, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(125416.11054292, 122793.13290029, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(125311.25917923, 122779.34571042, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(125913.09375, 123507.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(126003.78939612, 122585.93053248, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(125211.1640625, 124628.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))


class Palmyra(Airport):
    id = 28
    name = "Palmyra"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4350000, vhf_low_hz=39600000, vhf_high_hz=121900000, uhf_hz=251150000)

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
                airplanes=True, slot_name='05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-55401.72273061, 219312.63537167, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-55398.016148388, 219356.34084648, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-55393.799852879, 219402.17768204, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=41.0, width=41.0, height=18.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=4375000, vhf_low_hz=39650000, vhf_high_hz=122600000, uhf_hz=251200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-174598.3671, 37220.91243, terrain), terrain)

        self.runways.append(Runway(id=1, name='05-23', main=RunwayApproach(name='05', heading=50, beacons=[]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-174493.796875, 37202.12109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-174683.109375, 37353.74609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-174685.25, 36926.73046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-174638.828125, 37272.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-174697.859375, 37295.046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-174647.078125, 36918.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-174572.15625, 37154.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-174636.09375, 37033.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-174534.34498818, 37068.039263929, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-174721.15625, 36936.94921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-174553.1388612, 36989.442302916, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-174589.609375, 36893.73046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-174466.921875, 37296.1484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-174752.078125, 37094.52734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-174591.8125, 37098.48046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-174630.65625, 36982.3046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-174729.96875, 37178.1953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-174711.9375, 37236.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-174626.328125, 37320.60546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-174572.13917197, 37409.456082461, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))


class Ramat_David(Airport):
    id = 30
    name = "Ramat David"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4425000, vhf_low_hz=39750000, vhf_high_hz=118600000, uhf_hz=251300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-259121.195313, -75104.90625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield30_1'))
        self.beacons.append(AirportBeacon(id='airfield30_0'))
        self.runways.append(Runway(id=2, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.runways.append(Runway(id=3, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[RunwayBeacon(id='airfield30_2', runway_name='15-33', runway_id=3, runway_side='33'), RunwayBeacon(id='airfield30_3', runway_name='15-33', runway_id=3, runway_side='33')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-258762.6058149, -74992.201232293, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-258797.125, -74842.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-258925.328125, -75696.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-258823.671875, -76847.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-259843.515625, -74197.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-259785.734375, -75052.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-259802.703125, -75081.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-258788.359375, -74869.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-258807.84375, -75692.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-259322.921875, -74411.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-259688.05719938, -74168.296024232, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-258858.09375, -74527.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-258926.203125, -75766.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-258390.296875, -76228.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-258767.296875, -74957.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-259300.484375, -74383.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-259939.59375, -74245.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-258765.265625, -75105.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-258926.328125, -75719.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-259885.6875, -74320.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-259269.828125, -75576.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-259150.109375, -74365.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-258770.765625, -75185.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-258841.953125, -74549.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-258394.875, -75913.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-258360.25, -75909.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-259535.546875, -74323.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-258927.65625, -75743.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-258874.1875, -74506.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-259959.890625, -74257.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-258774.203125, -75680.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-258840.78125, -76822.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-258909.046875, -74462.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-258684.953125, -74703, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-258781.375, -74895.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-259803.140625, -74181.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-259999.796875, -74810.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-259533.5, -74288.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-258769.078125, -75158.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-259919.37069199, -74234.368146342, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-258415.015625, -76203.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-259758.796875, -74174.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-259545.140625, -75441.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-259193.84375, -74335.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-258763.296875, -75079.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-258892.75, -74483.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-258767.28125, -75132.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-258828.09375, -75527.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-259277.3125, -75543.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-259171.8125, -74350.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-258774.265625, -74923.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-259567.3125, -75468.4921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-258924.109375, -75672.6015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-259974.40625, -74785.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-259823.4375, -74189, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-259782.125, -74177.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-258826.5625, -74570.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-259899.4375, -74221.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-259878.6875, -74210.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-259876.203125, -74352.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-259710.43219938, -74168.436649232, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-260147.90625, -74661.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-260158.484375, -74706.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-260169.4375, -74752.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=41.0, width=41.0, height=18.0, shelter=False))


class Kuweires(Airport):
    id = 31
    name = "Kuweires"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4450000, vhf_low_hz=39800000, vhf_high_hz=120500000, uhf_hz=251350000)

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
    atc_radio = AtcRadio(hf_hz=4475000, vhf_low_hz=39850000, vhf_high_hz=124400000, uhf_hz=251400000)

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
    atc_radio = AtcRadio(hf_hz=4500000, vhf_low_hz=39900000, vhf_high_hz=121000000, uhf_hz=251450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-48306.007813, 8690.693604, terrain), terrain)

        self.runways.append(Runway(id=None, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-47956.825485573, 8694.6518830807, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-47976.463578181, 8655.0955753801, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-47898.8030556, 8813.579784753, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-47917.8159173, 8774.4503777071, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-47937.219891308, 8734.1802224648, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-47996.851353483, 8614.5082787788, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-47879.657595452, 8853.5354803384, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-47860.202838404, 8892.7932473889, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-47840.570374123, 8932.833761474, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-48921.453125, 7167.7524414062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-48855.646755835, 7306.2616325305, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-47528.072939409, 9967.7753203718, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-47367.125, 9996.330078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))


class Rosh_Pina(Airport):
    id = 34
    name = "Rosh Pina"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4525000, vhf_low_hz=39950000, vhf_high_hz=118450000, uhf_hz=251500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-225277.734375, -37687.537109, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield34_0'))
        self.runways.append(Runway(id=None, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-225408.34375, -37271.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-225793.734375, -37523.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-225771.515625, -37487.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-225504.75, -37272.84765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-225558.36128333, -37359.413732886, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-225837.84375, -37477.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-225651.078125, -37340.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-225459.4375, -37271.60546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-225571.03125, -37382.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-225854.0625, -37514.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-225636.96875, -37317.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-225907.34375, -37448.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=36.0, width=36.0, height=15.0, shelter=False))


class Sayqal(Airport):
    id = 35
    name = "Sayqal"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4550000, vhf_low_hz=40000000, vhf_high_hz=120400000, uhf_hz=251550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-151781.375, 117529.734375, terrain), terrain)

        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-150951.09375, 118565.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-150832.671875, 118476.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-151048.81463219, 118638.71496446, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-150856.53125, 118494.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-150927.4375, 118547.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-150903.859375, 118529.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-150879.984375, 118512.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-151020.61576803, 118617.24627852, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-150998.53125, 118601.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-150974.984375, 118583.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-151354.78125, 117107.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-151373.53125, 116187.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-150980.53125, 117776.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-151254.8125, 117628.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-151366.453125, 117421.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-151389.6875, 116162.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-150099.796875, 117949.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-150800.52987548, 118307.31113914, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-151220.5625, 119574.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-151193.859375, 119589.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-150479.125, 117962.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-150749.828125, 119337.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-150766.59375, 119312.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-150767.71875, 118082.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-150739.515625, 118091.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-150324, 117944.5703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-152022.65625, 116314.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-152033.6875, 116286.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-152031.046875, 116090.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-152402.375, 119020.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-151622.953125, 115413.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-152175.796875, 118990.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-152401.625, 118990.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-151596.25, 115428.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-152011.03125, 115887.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-152202.546875, 119326.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-152123.21875, 115658.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-152134.8125, 115686.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-151930.796875, 115975.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-152039.40625, 116061.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-152113.390625, 115979.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-152172.625, 119326.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-151465.375, 115627.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-151531.375, 119188.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-151422.828125, 118999.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-151255.6875, 116011.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-151259.828125, 115981.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-151341.875, 119398.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-151370.828125, 119406.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-151202.609375, 119257.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-151195.84375, 119228.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-151363.53125, 115745.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-151366.15625, 115775.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-151477.640625, 115600.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-152042.5, 119194.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-151530.21875, 115923.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-151551.015625, 119211.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-152064.046875, 119173.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-151514.6875, 115949.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))


class Shayrat(Airport):
    id = 36
    name = "Shayrat"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4575000, vhf_low_hz=40050000, vhf_high_hz=120200000, uhf_hz=251600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-61368.207031, 90675.136719, terrain), terrain)

        self.runways.append(Runway(id=None, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-62254.8671875, 92263.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-62243.515625, 92291.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-62432.48046875, 92339.7734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-62408.37890625, 92358.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-62489.69140625, 92151.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-62490.40625, 92181.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-62269.2734375, 92023.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-62280.4921875, 92051.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-62128.73046875, 91946.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-62127.12890625, 91976.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-61852.84375, 92503.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-61882.9296875, 92506.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-61719.49609375, 92322.5703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-61738.234375, 92346.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-61565.9296875, 92100.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-61538.53125, 92088.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-60538.8828125, 89953.0546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-60562.1953125, 89972.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-60230.67578125, 90324.6796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-60244.2734375, 90297.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-60372.7890625, 89819.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-60148.73828125, 89517, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-59998.8203125, 90024.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-59999.33203125, 90054.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-59789.515625, 89731.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-59787.9921875, 89761.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-59633.95703125, 89851.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-59638.38671875, 89821.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-60384.8359375, 89189.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-60373.36328125, 89217.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-60472.2578125, 89326.713449383, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-60535.4296875, 89182.408761883, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-61114.6796875, 89430.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-61090.44921875, 89412.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-60954.0078125, 89082.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-60981.7109375, 89094.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-61179.85546875, 89020.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-61198.25390625, 89045.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-61077.80078125, 88972.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-61047.8828125, 88976.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-60592.5703125, 90579.6484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
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
                crossroad_idx=47, position=mapping.Point(-61739.293622478, 92063.309660787, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-61765.418051466, 92098.116759482, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-61787.201078019, 92125.689139634, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-61803.659562971, 92147.577531721, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-61822.355501616, 92178.631923005, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-60233.200487685, 89906.714991858, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-60210.365308132, 89877.357396611, self._terrain), large=False, heli=True,
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
                crossroad_idx=57, position=mapping.Point(-60260.681286788, 89942.89039494, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-60287.752143905, 89978.856838403, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=41.0, width=41.0, height=18.0, shelter=False))


class Tabqa(Airport):
    id = 37
    name = "Tabqa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4600000, vhf_low_hz=40100000, vhf_high_hz=118500000, uhf_hz=251650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(76964.6875, 243605.210938, terrain), terrain)

        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(77222.4375, 244747.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(77359.6015625, 245047.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(77244.8515625, 244727.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(77246.140625, 245090.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(77246.4921875, 245120.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(77351.421875, 242655.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(77196.5703125, 245305.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(77352.109375, 242625.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(77350.015625, 245283.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(77607.140625, 242237.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(77469.926949921, 242046.73467653, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(77408.875, 245447.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(77385.1875, 241958.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(77285.9609375, 245521.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(77370.3828125, 241932.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(76687.828125, 245209.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(76707.078125, 245232.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(77404.634750466, 242174.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(77403.117839887, 242200.32278379, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(77406.799901352, 242232.72567131, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(77428.390625, 244914.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(77405.313087079, 242273.06493885, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(77403.643114235, 242313.36628679, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(77176.334257023, 244848.0664544, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(77173.409975531, 244893.69903778, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(77165.372791381, 244928.01377977, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(77163.075355968, 244959.49584738, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(77162.012855968, 244984.90051474, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(77161.007021348, 245010.1431965, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))


class Taftanaz(Airport):
    id = 38
    name = "Taftanaz"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4625000, vhf_low_hz=40150000, vhf_high_hz=122800000, uhf_hz=251700000)

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
                crossroad_idx=14, position=mapping.Point(102818.21187917, 82664.875, self._terrain), large=False, heli=True,
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
                crossroad_idx=25, position=mapping.Point(103338.94219097, 82465.551565973, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=4650000, vhf_low_hz=40200000, vhf_high_hz=120500000, uhf_hz=251750000)

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
                crossroad_idx=78, position=mapping.Point(-58664.948245203, 156564.56471092, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=4700000, vhf_low_hz=40300000, vhf_high_hz=120500000, uhf_hz=251850000)

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
    atc_radio = AtcRadio(hf_hz=4725000, vhf_low_hz=40350000, vhf_high_hz=119250000, uhf_hz=251900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(158144.617188, -319392.546875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield41_2'))
        self.beacons.append(AirportBeacon(id='airfield41_3'))
        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[RunwayBeacon(id='airfield41_1', runway_name='08-26', runway_id=1, runway_side='08'), RunwayBeacon(id='airfield41_0', runway_name='08-26', runway_id=1, runway_side='08')]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
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
    atc_radio = AtcRadio(hf_hz=4750000, vhf_low_hz=40400000, vhf_high_hz=118100000, uhf_hz=251950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(25465.162934, 389747.046042, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield42_1'))
        self.beacons.append(AirportBeacon(id='airfield42_0'))
        self.runways.append(Runway(id=None, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(26161.202661455, 388408.2170284, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(25198.46484375, 391117.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(25636.1015625, 390525.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(25624.423828125, 390705.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(25171.208984375, 391195.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(25187.607421875, 391148.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(25570.91015625, 390686.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(25193.09070455, 391132.65113541, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(25165.837890625, 391211.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(25176.80313163, 391179.58691381, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(26151.628442705, 388436.5607784, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(26140.980106054, 388492.11755578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(25581.6484375, 390506.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(25180.174212673, 391290.18067669, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(25701.69140625, 390549.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(25206.867572048, 391276.21192669, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(25182.332428505, 391163.71191381, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Akrotiri(Airport):
    id = 44
    name = "Akrotiri"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4775000, vhf_low_hz=40450000, vhf_high_hz=128000000, uhf_hz=252000000)

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
                airplanes=True, slot_name='E2', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-36447.692993505, -268066.08583095, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E1', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-36529.832199155, -267962.15104425, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E3', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-36605.176814299, -268021.18473148, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E4', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-36802.859375, -267884.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F1', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-36867.51953125, -267791.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F2', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-36901.483269345, -267956.63491732, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F4', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-36965.286520943, -267859.75154598, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F3', length=60.0, width=52.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='G8', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-36591.25, -267694.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-36641.578125, -267672.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-36696.8046875, -267647.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-36742.90625, -267627.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G16', length=26.0, width=24.0, height=11.0, shelter=False))
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
                crossroad_idx=32, position=mapping.Point(-35903.24329253, -269329.53454675, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-35850.552164139, -269570.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=42.0, width=34.0, height=14.0, shelter=False))
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
                airplanes=True, slot_name='02', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-37085.125, -267803.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F5', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-37057.3359375, -267543.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F6', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-35626.7265625, -270167.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B2', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-35731.87890625, -270189.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B1', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-35430.03515625, -270624.23676756, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A3', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-35434.07421875, -270484.61176756, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A1', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-35555.16796875, -270636.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A4', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-35565.3203125, -270496.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A2', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-36525.8671875, -267610.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G1', length=26.0, width=24.0, height=11.0, shelter=False))


class Kingsfield(Airport):
    id = 45
    name = "Kingsfield"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4800000, vhf_low_hz=40500000, vhf_high_hz=121000000, uhf_hz=252050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(7596.761963, -199426.492188, terrain), terrain)

        self.runways.append(Runway(id=None, name='24-06', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='06', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(7760.2595443036, -198874.52124089, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(7775.0039815814, -198916.77351947, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))


class Paphos(Airport):
    id = 46
    name = "Paphos"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4825000, vhf_low_hz=40550000, vhf_high_hz=119900000, uhf_hz=252100000)

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
                crossroad_idx=37, position=mapping.Point(-19043.912109375, -312697.46947517, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-19008.195647695, -312682.28233775, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-18972.251953125, -312666.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-18936.779296875, -312650.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-19023.447549158, -312743.92204412, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-18986.14760189, -312731.04770556, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-18950.462055015, -312715.01645556, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=4850000, vhf_low_hz=40600000, vhf_high_hz=121200000, uhf_hz=252150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-7674.737061, -208843.625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield47_1'))
        self.beacons.append(AirportBeacon(id='airfield47_3'))
        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[RunwayBeacon(id='airfield47_2', runway_name='1#04-22', runway_id=1, runway_side='22'), RunwayBeacon(id='airfield47_0', runway_name='1#04-22', runway_id=1, runway_side='22')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-7843.2055664062, -210062.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-7895.5390625, -210020, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-7938.2109375, -209982.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-7985.0146484375, -209937.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-8104.6875, -209945.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-8157.6640625, -209997.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-8380.060546875, -210250.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-8336.611328125, -210288.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-8292.435546875, -210326.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-8247.189453125, -210365.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-8195.0927734375, -210405.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-8067.0766601563, -210408.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-8120.91796875, -210428.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-8030.1235351563, -210316.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-8185.2456054687, -210069.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-8141.5102539062, -210105.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-8090.4340820312, -210147.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-8035.900390625, -210192.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=41.0, width=41.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='91', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-6315.1684570312, -207872.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-6347.9721679687, -207843.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-6175.6899414062, -207999.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-6243.2578125, -208073.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-6323.8002929688, -208011.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-6365.2827148437, -207976.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-6402.2626953125, -207943.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=41.0, width=41.0, height=18.0, shelter=False))
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
                airplanes=True, slot_name='47', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-6200.3994140625, -208045.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-6290.9176756363, -208041.67885003, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-6437.2817382812, -207913.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=41.0, width=41.0, height=18.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=4875000, vhf_low_hz=40650000, vhf_high_hz=120200000, uhf_hz=252200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(19561.164063, -234985.75, terrain), terrain)

        self.runways.append(Runway(id=None, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(19757.101018731, -234856.62559328, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H5', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(19774.132053436, -234895.68993797, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H6', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(19790.629812727, -234934.90686505, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H7', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(19809.004918246, -234972.75048105, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H8', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(19700.041015625, -234890.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(19720.837890625, -234940.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(19730.321693852, -234967.38141694, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=4900000, vhf_low_hz=40700000, vhf_high_hz=120200000, uhf_hz=252250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(24250.327148, -218240.28125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield49_1'))
        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[RunwayBeacon(id='airfield49_2', runway_name='11-29', runway_id=1, runway_side='29'), RunwayBeacon(id='airfield49_0', runway_name='11-29', runway_id=1, runway_side='29')])))
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
    atc_radio = AtcRadio(hf_hz=4950000, vhf_low_hz=40800000, vhf_high_hz=120000000, uhf_hz=252350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(32144.729634, -197767.51907, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield50_1'))
        self.beacons.append(AirportBeacon(id='airfield50_0'))
        self.runways.append(Runway(id=None, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(31788.727221935, -196741.07792781, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(31782.904725402, -196670.25006573, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(31778.895009085, -196592.03361997, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))


class Pinarbashi(Airport):
    id = 51
    name = "Pinarbashi"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4975000, vhf_low_hz=40850000, vhf_high_hz=121000000, uhf_hz=252400000)

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
    atc_radio = AtcRadio(hf_hz=5000000, vhf_low_hz=40900000, vhf_high_hz=122000000, uhf_hz=252450000)

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
    atc_radio = AtcRadio(hf_hz=5025000, vhf_low_hz=40950000, vhf_high_hz=122000000, uhf_hz=252500000)

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
                crossroad_idx=22, position=mapping.Point(-235051.21681752, 351291.1673188, self._terrain), large=False, heli=True,
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
                crossroad_idx=47, position=mapping.Point(-237224.35703911, 351421.07837667, self._terrain), large=False, heli=True,
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
    atc_radio = AtcRadio(hf_hz=5050000, vhf_low_hz=41000000, vhf_high_hz=122100000, uhf_hz=252550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-220000.35156, 338483.561903, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-220596.01725509, 338732.40531432, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-220565.3125, 338684.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-220551.28599691, 338660.9056963, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-220536.70804597, 338636.77892417, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-220522.29966611, 338613.17321578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-220508.10723916, 338589.59913011, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-220493.87262688, 338566.07911436, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-220479.24248456, 338542.05775377, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-220460.01351523, 338510.15203047, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-220420.8876586, 338578.02650377, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-220433.92721536, 338601.96914608, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-220448.4939084, 338625.41558587, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-220462.73716611, 338648.14196578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-220477.57137673, 338672.57520589, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-220491.69224691, 338696.4681963, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-220505.59375, 338719.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-220519.41816547, 338744.88968666, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-220467.06516497, 339750.119015, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-220621.56555203, 339790.43324201, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-220895.36765434, 339639.54727977, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-220938.17646707, 339461.11671036, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-219545.11226143, 337227.00391661, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-219383.88293833, 337189.65486839, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-219121.97410222, 337355.96923385, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-219084.2906963, 337516.60061388, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=5075000, vhf_low_hz=41050000, vhf_high_hz=122400000, uhf_hz=252600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-256859.445313, 339219.1875, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-255994.578125, 338088.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-257758.9375, 340235.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-257467.59375, 340538.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-257096.328125, 340075.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-256962.43473679, 339988.48497798, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-257007.20497379, 339927.75093436, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-257815.21875, 340040.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-257021.1165347, 340087.45069317, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-257125.015625, 340646.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-256445.36822972, 337965.26081183, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-255956.5625, 338243.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-257035.4817157, 340111.34422116, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-257309.375, 340495.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-257691.671875, 339967.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-257040.640625, 340425.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-256977.625, 340013.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-257037.03125, 340798.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-257051.0229205, 340137.4053555, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-257727.015625, 340388.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-257111.98530537, 340101.51657928, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-256291.69075297, 337926.41390988, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-257006.93551812, 340062.35351178, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-257022.37408557, 339952.95221057, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-257066.96875, 340026.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-256992.453125, 340037.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-256979.046875, 340322.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-257081.663962, 340051.48762803, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-257037.32139262, 339977.65228083, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-257052.27692502, 340001.99002501, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-256926.06300435, 339931.97137278, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-256946.97548238, 339963.59633756, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))


class Ruwayshid(Airport):
    id = 57
    name = "Ruwayshid"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5100000, vhf_low_hz=41100000, vhf_high_hz=122100000, uhf_hz=252650000)

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
    atc_radio = AtcRadio(hf_hz=5125000, vhf_low_hz=41150000, vhf_high_hz=118400000, uhf_hz=252700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(264719.125, 273812.4375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield58_1'))
        self.beacons.append(AirportBeacon(id='airfield58_2'))
        self.beacons.append(AirportBeacon(id='airfield58_3'))
        self.beacons.append(AirportBeacon(id='airfield58_0'))
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
    atc_radio = AtcRadio(hf_hz=5150000, vhf_low_hz=41200000, vhf_high_hz=122200000, uhf_hz=252750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(164820.140625, 245880.46875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(164830.796875, 246057.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(164866.21875, 246043.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
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
                crossroad_idx=5, position=mapping.Point(164920.66613623, 245663.32278414, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(164878.0082365, 245660.6101447, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(164836.24561995, 245658.51382871, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(164795.93917044, 245655.14146898, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(164755.83561733, 245652.76039633, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(164715.10897693, 245651.61403031, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=42.0, width=34.0, height=14.0, shelter=False))


class Tal_Siman(Airport):
    id = 60
    name = "Tal Siman"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5200000, vhf_low_hz=41300000, vhf_high_hz=121900000, uhf_hz=252850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(133191.875, 276361.453125, terrain), terrain)

        self.runways.append(Runway(id=1, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(133192.08597208, 276637.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=36.0, width=36.0, height=15.0, shelter=False))
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
    atc_radio = AtcRadio(hf_hz=5225000, vhf_low_hz=41350000, vhf_high_hz=121100000, uhf_hz=252900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-172365.28125, 247031.90625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-172390.890625, 247005.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-172339.65625, 247058.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Prince_Hassan(Airport):
    id = 64
    name = "Prince Hassan"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5250000, vhf_low_hz=41400000, vhf_high_hz=122600000, uhf_hz=252950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-320113.40625, 108294.582031, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield64_1'))
        self.beacons.append(AirportBeacon(id='airfield64_2'))
        self.beacons.append(AirportBeacon(id='airfield64_0'))
        self.runways.append(Runway(id=None, name='31-13', main=RunwayApproach(name='31', heading=310, beacons=[]), opposite=RunwayApproach(name='13', heading=130, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-318801.25, 107549.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-320291.03125, 108949.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-319317.8125, 107900.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-320999.75, 109701.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-319824.46875, 108367.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-319935.59375, 108490.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-319061.5, 107338.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-319621.0625, 108142.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-318848.40625, 107607.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-320418.875, 109453.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-319866.9375, 108413.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-320819.65625, 109841.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-319095.25, 107294.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-321234.4375, 109312.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-320521.375, 109605.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-320599.34375, 109588.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-318955.65625, 107285.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-320235.65625, 108892.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-320907.53125, 109813.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-320387.75, 109378.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-319852.875, 108397.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-319894.3125, 108444.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-320690.40625, 109624.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-320851.59375, 109775.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-320898.28125, 109393.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-319086.6875, 107624.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-318983.3125, 107260.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-320507.9375, 109185.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-320389.59375, 109095.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-320532.1875, 109426.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-319288.625, 107967.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-319838.625, 108381.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-319921.84375, 108474.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-320646.46875, 109809.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-318862.40625, 107509.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-320219.40625, 109446.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-321079.4375, 109546.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-319949.34375, 108505.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-320279.5625, 109703.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-320728.8125, 109800.3359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-321251.65625, 109399.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-320367.71875, 109416.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-319908.3125, 108459.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-318953.15625, 107221.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-320352.21875, 109577.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-321036.375, 109560.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-320425.84375, 109574.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-318969.40625, 107272.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-320184, 108840.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-318920.5, 107157.3046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-319394.625, 107882, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-320661.96875, 109691.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-318913.1875, 107667.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-319880.65625, 108428.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-318996.125, 107248.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-320433.21875, 109372.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-320938.4375, 109439.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-318774, 107476.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-319770.25, 108383.9140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-320220.15625, 109519.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))


class King_Abdullah_II(Airport):
    id = 65
    name = "King Abdullah II"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5275000, vhf_low_hz=41450000, vhf_high_hz=118400000, uhf_hz=253000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-335450.1875, 20534.525391, terrain), terrain)

        self.runways.append(Runway(id=None, name='31-13', main=RunwayApproach(name='31', heading=310, beacons=[]), opposite=RunwayApproach(name='13', heading=130, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-336101.03125, 20353.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='56', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-336341.0625, 20706.451171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='106', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-336253.09375, 20604.505859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='89', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-335036.6875, 20342.31640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-335595.16998327, 20150.56132126, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='32', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-336189.73978671, 20469.54728348, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-336140.89237843, 20460.40327454, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-335675.117984, 20290.21028891, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-336017, 20467.748046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='51', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-336067.5, 20399.052734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='54', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-335392.06275882, 20077.659798649, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-335350.16996049, 20049.039928846, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-335553.32490458, 20209.715067407, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='31', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-335999.125, 20491.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='50', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-336289.65625, 20557.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-335307.0625, 19868.017578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-335574.0043128, 20224.45864005, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-336176.5625, 20487.404296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-335205.54990387, 19942.56043438, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-336150.1875, 20389.361328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='64', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-335472.50438648, 20135.564811285, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='27', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-336085, 20376.486328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='55', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-335675.65387888, 20209.262510336, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='40', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-334989.5, 20290.20703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-335506.04904146, 20088.988716646, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='28', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-336142.90625, 20751.30078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='84', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-336498.875, 20664.615234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-336450.625, 20588.091796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-336294.96875, 20707.806640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='101', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-335774.12920534, 20362.042254551, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='47', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-336359.5, 20682.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='107', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-336096.1875, 20575.17578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='74', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-336099.75, 20458.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='61', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-336116.28125, 20435.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-336163.11605955, 20505.020652283, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-336082.84375, 20481.412109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='60', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-336807.1875, 20823.14453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='117', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-335636.23283477, 20182.102699574, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-336203.23444989, 20451.495655816, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-336270.875, 20384.56640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-334943.125, 20238.736328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-335741.66958329, 20337.673542283, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='45', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-336114.31812173, 20497.20369288, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-336304.125, 20642.576171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='96', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-336127.6733825, 20478.441060823, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-336050.84375, 20422.068359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='53', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-334820.6875, 20061.205078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-336235.875, 20628.662109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='88', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-336377.1875, 20657.93359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='108', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-336329.40625, 20661.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='103', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-336167.34314572, 20424.068923183, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-336339.1875, 20592.97265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-335276.93631941, 19929.490124864, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-335574.23752205, 20136.658488481, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-336379.3125, 20537.521484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-336271.75, 20580.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='90', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-335743.0214142, 20265.015782249, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='44', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-335657.30766531, 20196.606851638, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-335285.76422026, 20002.362490426, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-336324.15625, 20729.568359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='105', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-335464.96324115, 20060.012237212, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='26', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-335532.77843403, 20194.131318873, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='29', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-336180.15625, 20779.34765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='86', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-335707.26119656, 20315.802394393, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='43', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-336071.8125, 20557.31640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='66', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-335245.31950622, 19972.254006093, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-336312.125, 20684.685546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='102', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-336100.8125, 20517.517578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='67', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-336143.90625, 20281.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-336199, 20792.326171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='87', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-336525.75, 20723.556640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='113', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-336180.87228618, 20406.53558278, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-334736.59375, 20225.345703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-336348.5, 20636.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='104', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-336733.0625, 20769.98828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='116', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-334850.5625, 20097.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-336065.6875, 20504.068359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='59', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-335384.7280739, 20001.050221223, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-335615.67075316, 20166.789555914, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-335595.38075946, 20239.151335326, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-335166.19934256, 19912.194703359, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-336154.29093721, 20442.266389064, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-335775.69160586, 20290.37030806, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='46', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-336358.8125, 20566.017578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-335425.36857297, 20030.416353656, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='24', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-336250.65625, 20370.044921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-336285.9375, 20666.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='95', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-334789.59375, 20025.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-336048.8125, 20527.927734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='58', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-336034.1875, 20445.03515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='52', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-335844.95482836, 20332.580300499, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='49', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-335235.90332804, 19900.09326215, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-336661.03125, 20719.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='115', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-336322.21875, 20618.11328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='97', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-336538.78125, 20705.41015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='114', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-336161.3125, 20765.42578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='85', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-335430.70915152, 20107.549687351, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='25', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-336402.15625, 20457.330078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-336329.5, 20501.669921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-336150.05632084, 20522.788101741, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-334758.4375, 19989.541015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-335385.8125, 19925.763671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-336481.375, 20688.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-334895.53125, 20186.52734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-335633.02075316, 20267.804632236, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='39', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-335808.91790114, 20314.165432956, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='48', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-336209.46875, 20329.876953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-336309.21875, 20529.818359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-336133.5625, 20412.42578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='63', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-335195.55142869, 19872.147449298, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-336125.3125, 20535.376953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='75', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-334754.84375, 20165.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-335710.4593918, 20241.491561434, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-335316.6754369, 19958.485842502, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-336216.78128092, 20433.985669637, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-335615.57939208, 20254.35900718, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-336541.28125, 20640.794921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='112', length=26.0, width=24.0, height=11.0, shelter=False))


class Herzliya(Airport):
    id = 66
    name = "Herzliya"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5300000, vhf_low_hz=41500000, vhf_high_hz=122200000, uhf_hz=253050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-311947.078125, -109710.855469, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-311989.53125, -109793.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-311594.09375, -110581.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-311975.46875, -109838.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-311706.9375, -110531.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-311777.9375, -110537.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-311754.5625, -110535.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-311956.40625, -109503.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-311728.59375, -110533.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-311864, -110113.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-311831.84375, -110201.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-312087.28125, -109569.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-312071.84375, -109612.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-311840.28125, -110179.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-312094.4375, -109549.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-311808.25, -110665.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-312102.28125, -109528.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-312063.75, -109635.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-312003.03125, -109752.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-311794.96875, -110472.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-311855.90625, -110136.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-312040.125, -109697.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-311888.6875, -110049.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-311615.5, -110590.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-311819.71875, -110471.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-311939.90625, -109531.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-311658.78125, -110607.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-311614.59375, -110525.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-311635.90625, -110597.765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-311823.71875, -110220.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-311735.65625, -110632.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-311763.03125, -110465.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-311871.375, -110091.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-311996.40625, -109773.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-311717.84375, -110624.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-311982.25, -109815.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-312056.40625, -109655.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-311808.09375, -110263.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-311786.84375, -110656.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-311762.96875, -110443.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-311799.65625, -110285.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-311754.625, -110639.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-311847.28125, -110157.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-312048.5625, -109675.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-312080.28125, -109590.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-311636.625, -110534.8828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-311967.875, -109860.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-311880.0625, -110070.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-311859.96875, -110496.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-311815.09375, -110242.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))


class Marka(Airport):
    id = 67
    name = "Marka"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5325000, vhf_low_hz=41550000, vhf_high_hz=118100000, uhf_hz=253100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-338495.244804, -1486.426628, terrain), terrain)

        self.runways.append(Runway(id=None, name='24-06', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='06', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-338420.84375, -1904.3911132812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-338417.09375, -2113.7124023438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-338256.79179841, -2208.7158612038, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-338799.15625, -2704.2653808594, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-338346.5625, -2370.1545410156, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-339050.28125, -3081.2856445312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-338772.21875, -2642.3059082031, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='25', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-339011.34375, -3105.3718261719, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-338968.90625, -3083.9470214844, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-338578.71875, -977.59124755859, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-338468.6875, -2189.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-338955.09375, -3051.8801269531, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-338981.1875, -3039.8872070312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-338840.09375, -2850.2849121094, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-338844.1875, -2797.9489746094, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-338384.625, -2127.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-338371.21875, -2358.2407226562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-338426.28125, -2482.283203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-338241.84375, -2152.0788574219, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-338764.6875, -2626.0666503906, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='26', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-338561.15625, -850.57403564453, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-338995.40625, -3073.205078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-338378.6875, -2506.3959960938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-338757.375, -2609.5109863281, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='27', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-338472.625, -2022.3472900391, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-338586.03125, -2225.9096679688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-338887.65625, -2887.4438476562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-338780.53125, -2658.6696777344, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='24', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-338916.34375, -3069.525390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-338551.5, -993.55535888672, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-338396, -2344.5073242188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-338513.375, -2002.0499267578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-338861.96875, -2899.7561035156, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-338464.1875, -1885.7858886719, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-338833.0625, -2774.6401367188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-338485.9375, -2015.2358398438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-338884.9375, -2950.3366699219, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-339035, -3049.3000488281, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-338912.09375, -2939.0490722656, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-338442.9375, -2101.7199707031, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-338455.34375, -1981.6468505859, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-338306.6875, -2397.7497558594, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-338449.6875, -1892.2349853516, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-338895.15625, -3029.6149902344, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-338262.28125, -2140.6694335938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-338463.5625, -1928.5439453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-338481.4375, -1968.1663818359, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-338468.28125, -1974.9326171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-338330.03125, -2129.5847167969, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-338295.96942035, -2284.5790985741, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-338448.6875, -1935.5897216797, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-338943.9375, -3128.1762695312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-338346.09375, -2156.8415527344, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-338517.9375, -1011.0361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-338440.6875, -2202.1999511719, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-338750.03125, -2592.2878417969, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='28', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-338221.78125, -2162.4799804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-338498.90625, -2009.2371826172, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-338477.96875, -1921.4151611328, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-338584, -2432.6408691406, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-338435.03125, -1898.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-338276.0504351, -2246.4971031782, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-338496.375, -1960.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-338449.65625, -2471.2529296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-338473.875, -890.93682861328, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-338610.0625, -962.55883789062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='74', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-338538.125, -2247.5717773438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-338401.90625, -2494.7514648438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-338627.84375, -955.54821777344, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='75', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-338645.9375, -946.69030761719, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='76', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-338436.8125, -1941.4488525391, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-338361.21875, -2184.9143066406, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-338624.46875, -2414.3063964844, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-338822.28125, -2751.0397949219, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-338984.8125, -3116.7121582031, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-338867.125, -2839.2666015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-338788.40625, -2679.0661621094, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-338810, -2727.9050292969, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='21', length=30.0, width=23.0, height=10.0, shelter=False))


class Muwaffaq_Salti(Airport):
    id = 68
    name = "Muwaffaq Salti"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5350000, vhf_low_hz=41600000, vhf_high_hz=120500000, uhf_hz=253150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-357496.34375, 72548.183594, terrain), terrain)

        self.runways.append(Runway(id=1, name='31-13', main=RunwayApproach(name='31', heading=310, beacons=[RunwayBeacon(id='airfield68_2', runway_name='13-31', runway_id=1, runway_side='31'), RunwayBeacon(id='airfield68_3', runway_name='13-31', runway_id=1, runway_side='31')]), opposite=RunwayApproach(name='13', heading=130, beacons=[])))
        self.runways.append(Runway(id=2, name='26-08', main=RunwayApproach(name='26', heading=260, beacons=[RunwayBeacon(id='airfield68_1', runway_name='08-26', runway_id=2, runway_side='26'), RunwayBeacon(id='airfield68_0', runway_name='08-26', runway_id=2, runway_side='26')]), opposite=RunwayApproach(name='08', heading=80, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-356000.3125, 74456.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-356006.59375, 73982.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-356597.1875, 74240.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-355606.125, 73322.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-354664.25, 72361.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-356017.90625, 74437.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-356448.4375, 74357.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-354482.375, 72682.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-355864.84375, 73656.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-356067.03125, 73901.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-356359.03125, 74379.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-354176.46875, 71903.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-356488.46875, 74281.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-356281.375, 74084.1328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-355720.90625, 73508.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-357174.0625, 74045.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-357162.8125, 73800.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='120', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-356709.4375, 73872.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-356628.53125, 74151.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-356415.75, 74618.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-354226.34375, 72370.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-356916.28125, 74111.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='114', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-354919.0625, 72786.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-356417, 74365.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-354164.21875, 71889.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-355625.75, 73342.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-356012.25, 74512.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-357121.5, 73905.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='122', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-355703.5, 73489.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-356085.25, 73981.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-353995.90625, 71667.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-355778.25, 73681.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-354097.71875, 71672.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-356289.21875, 74651.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-356383.21875, 74547.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-354848.28125, 71845.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-354298.125, 72422.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-354694.65625, 72499.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-356826.53125, 73861.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-356280.1875, 74703.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-356430.125, 74293.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-356274.625, 74193.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-355961.21875, 73669.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-355667.28125, 73380.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-354413.75, 72328.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-354109.90625, 71834.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-355945.375, 73765.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='63', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-356046.5, 73763.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-354332.875, 72431.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-355010, 72741.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-355703, 73419.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-354188.75, 71917.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-355889.875, 73667.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-354876.90625, 72694.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-356618.5625, 74182.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-356478.3125, 74351.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-356002.71875, 73714.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-356421.34375, 74509.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-357114, 73857.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='121', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-355837.84375, 73524.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-355854.28125, 73602.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-356325.25, 74292.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-356259.59375, 74246, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-354263.03125, 72410.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-355981.75, 73690.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-354608.9375, 72445.2109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-354316, 72427.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-355585.34375, 73302.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-356703.4375, 74279.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='111', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-354281.125, 72416.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-357101.625, 74054.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='124', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-354643.3125, 72032.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-355721.5, 73595.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-355450.84375, 73305.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-356941.8125, 73848.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-357072.5, 73964.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='123', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-355995.40625, 73927.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-355773, 73562.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-356274, 74106.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-356884.21875, 73854.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-355866, 73724.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-354719.78125, 72135.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-355531.5, 73201.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-355940.125, 73806.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-355647.15625, 73363.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-356070.4375, 74422.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-356761.40625, 74349.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='112', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-355817.3125, 73642.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-354310.71875, 72326.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-355756, 73547.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-354096.71875, 71820.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-356384.84375, 74372.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-356606.71875, 74211.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-356272.46875, 74580.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-356040.03125, 74523.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-356379.21875, 74575.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-354588.375, 71973.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-355906.75, 73602.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-356024.8125, 73738.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-356035.5625, 73992.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-357150.21875, 74048.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-354393.0625, 72728.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-356013.15625, 73902.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-355678.9375, 73392.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-356975.03125, 74181.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='113', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-354246.5625, 72404.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-354800.34375, 71782.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-355518.5, 73385.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-353992.6875, 71767.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-354785.1875, 72122.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-356094.4375, 74513.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-354752.75, 72128.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-356281.09375, 74616.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-356273.3125, 74276.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-355691.03125, 73406.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-356767.34375, 73866.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-356266.5625, 74130.1953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=18.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-355834.40625, 73582.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-356535.1875, 74338.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-356457.21875, 74287.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-354319.0625, 72225.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-354349.75, 72637.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-356509.09375, 74345.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-357126.0625, 74051.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-354122.5625, 71848.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-355738.5, 73527.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-356355.78125, 74276.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-356367.84375, 74225.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-356444.96875, 74616.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-356483.84375, 74579.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=20.0, width=14.0, height=6.0, shelter=False))


class Helipad_69(Airport):
    id = 69
    name = "Helipad_69"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-1909.417969, -210324.59375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-1907.6511230469, -210375.984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-1909.1923828125, -210324.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-1911.1475830078, -210273.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_70(Airport):
    id = 70
    name = "Helipad_70"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-11651.873047, -222381.390625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-11651.609375, -222381.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-11649.276367188, -222342.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-11654.470703125, -222420.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_71(Airport):
    id = 71
    name = "Helipad_71"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(42759.042969, -236540.65625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(42759.04296875, -236540.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_72(Airport):
    id = 72
    name = "Helipad_72"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(36725.941406, -218077.875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(36736.1953125, -218096.421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(36715.6875, -218059.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_73(Airport):
    id = 73
    name = "Helipad_73"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(15571.533203, -183557.703125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(15586.24609375, -183568.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(15556.821289062, -183546.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_74(Airport):
    id = 74
    name = "Helipad_74"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(14422.808594, -182572.46875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(14422.80859375, -182572.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_76(Airport):
    id = 76
    name = "Helipad_76"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-227518.71875, -39695.945313, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-227537.6875, -39542.29296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-227499.875, -39620.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-227537.21875, -39738.67578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-227551.40625, -39847.79296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-227578.203125, -39661.50390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-227476.078125, -39806.13671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-227459.28125, -39697.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_77(Airport):
    id = 77
    name = "Helipad_77"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-225166.0625, -42928.195313, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-225271.0625, -42889.04296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-225128.390625, -42942.56640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-225059.8125, -42968.06640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_78(Airport):
    id = 78
    name = "Helipad_78"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-225271.0625, -42889.042969, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-225271.0625, -42889.04296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_79(Airport):
    id = 79
    name = "Helipad_79"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-236859.625, -24173.347656, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-236859.765625, -24195.58203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-236859.484375, -24151.11328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_80(Airport):
    id = 80
    name = "Helipad_80"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-230260.71875, -38038.21875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-230227.828125, -38224.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-230246.234375, -38131.32421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-230275.8125, -37945.20703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-230293.625, -37852.33203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_82(Airport):
    id = 82
    name = "Helipad_82"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-244391.609375, -54174.597656, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-244392.59375, -54156.80078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-244390.9375, -54193.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-244389.109375, -54231.0234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-244394.109375, -54118.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_83(Airport):
    id = 83
    name = "Helipad_83"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-244187.40625, -51945.539063, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-244187.40625, -51945.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_84(Airport):
    id = 84
    name = "Helipad_84"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-265064.4375, -95176.210938, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-265064.4375, -95176.2109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_85(Airport):
    id = 85
    name = "Helipad_85"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-242563.15625, -50868.386719, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-242510.75, -50873.1640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-242615.5625, -50863.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_86(Airport):
    id = 86
    name = "Helipad_86"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-223660.78125, -45746.117188, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-223641.25, -45782.57421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-223680.609375, -45709.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_87(Airport):
    id = 87
    name = "Helipad_87"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-221855.96875, -25060.3125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-221830.890625, -25093.271484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-221883.734375, -25092.14453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-221828.34375, -25029.392578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-221880.875, -25027.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_89(Airport):
    id = 89
    name = "Helipad_89"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(34650.914063, 16892.472656, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(34647.21875, 16871.43359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(34654.609375, 16913.509765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_92(Airport):
    id = 92
    name = "Helipad_92"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(81444.421875, 167560.6875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(81443.2578125, 167533.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(81440.7734375, 167475.796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(81445.6796875, 167590.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(81448.0703125, 167645.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_93(Airport):
    id = 93
    name = "Helipad_93"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-193853.15625, 11337.087891, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-193852.5625, 11337.865234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-193903.0625, 11304.533203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-193803.234375, 11369.643554688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_94(Airport):
    id = 94
    name = "Helipad_94"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-43893.3125, 75999.921875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-43895.01171875, 75999.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-43967.84765625, 75999.3359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-43818.7734375, 76000.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_95(Airport):
    id = 95
    name = "Helipad_95"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(112046.929688, 133579.46875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(112054.6875, 133602.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(112039.1796875, 133556.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_96(Airport):
    id = 96
    name = "Helipad_96"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(110991.648438, 132585.96875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(110979.9375, 132553.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(111027.421875, 132561.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(111002.53125, 132618.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(110955.703125, 132611.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_97(Airport):
    id = 97
    name = "Helipad_97"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-182424.109375, 29107.121094, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-182433.203125, 29135.24609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-182415.140625, 29079.076171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_98(Airport):
    id = 98
    name = "Helipad_98"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-179190.84375, 30290.609375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-179144.5, 30343.560546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-179130.796875, 30275.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-179236.109375, 30289.560546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-179224.78125, 30234.65234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-179247.609375, 30346.576171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_99(Airport):
    id = 99
    name = "Helipad_99"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-49713.671875, 214312.96875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-49787.78125, 214389, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-49697.59765625, 214360.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-49818.8359375, 214295.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-49728.58984375, 214266.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-49639.4765625, 214236.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-49608.2890625, 214332.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_100(Airport):
    id = 100
    name = "Helipad_100"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-47920.046875, 213406.125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-47900.68359375, 213478.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-47939.578125, 213333.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-47920.48828125, 213406.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_101(Airport):
    id = 101
    name = "Helipad_101"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(103896.304688, 139855.5, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(103866.578125, 139823.109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(103926.71875, 139840.015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(103926.1015625, 139887.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(103865.703125, 139870.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_102(Airport):
    id = 102
    name = "Helipad_102"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-181717.15625, 37228, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-181699.453125, 37267.17578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-181755.84375, 37206.05078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-181678.6875, 37189.01953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_103(Airport):
    id = 103
    name = "Helipad_103"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-174294.78125, 12049.615234, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-174257.265625, 12027.4921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-174332.390625, 12071.784179688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-174295.3125, 12050.478515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_104(Airport):
    id = 104
    name = "Helipad_104"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-143739.78125, 79341.257813, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-143772.15625, 79382.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-143708.578125, 79383.765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-143708.046875, 79341.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-143771.703125, 79298.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-143771.984375, 79341.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-143707.453125, 79299.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_105(Airport):
    id = 105
    name = "Helipad_105"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-177248.84375, 14913.109375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-177207.5625, 14882.491210938, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-177269.140625, 14865.655273438, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-177280.0625, 14904.895507812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-177290.125, 14943.549804688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-177229.65625, 14960.592773438, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-177218.421875, 14921.297851562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_106(Airport):
    id = 106
    name = "Helipad_106"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-174162.625, 16124.533203, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-174140.59375, 16078.762695312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-174176.875, 16095.7578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-174212.359375, 16112.262695312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-174186.421875, 16170.311523438, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-174112.6875, 16136.791015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-174148.640625, 16153.762695312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_107(Airport):
    id = 107
    name = "Helipad_107"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-176031.203125, 32733.699219, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-175996.609375, 32679.162109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-176040.15625, 32688.0703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-176084.015625, 32696.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-176066.140625, 32788.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-175978.125, 32770.4921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-176020.671875, 32778.8828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_108(Airport):
    id = 108
    name = "Helipad_108"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-205780.78125, 56427.867188, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-205790.9375, 56493.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-205784.4375, 56450.18359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-205776.90625, 56404.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-205770.65625, 56362.71484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_109(Airport):
    id = 109
    name = "Helipad_109"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-147659.90625, 67139.390625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-147575.40625, 67176.2109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-147606.8125, 67131.296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-147712.375, 67147.2890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-147683.5625, 67186.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-147635.328125, 67091.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-147744.4375, 67103.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-147667.546875, 67047.2109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-147652.578125, 67231.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_110(Airport):
    id = 110
    name = "Helipad_110"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-179414.84375, 21648.0625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-179363.421875, 21655.94921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-179466.25, 21678.80078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-179401.859375, 21702.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-179429.859375, 21636.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-179394.546875, 21594.1640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_111(Airport):
    id = 111
    name = "Helipad_111"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-186567.25, 48755.1875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-186610.3125, 48740.35546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-186523.140625, 48771.66015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-186564.8125, 48799.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-186563.5, 48710.11328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_112(Airport):
    id = 112
    name = "Helipad_112"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-264467.53125, -56972.355469, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-264874.5, -56795.55078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-265019.09375, -56880.5546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-263909.5, -57137.03515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-264945.96875, -56838.15234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-263991.84375, -57144.52734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-264074.53125, -57153.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_113(Airport):
    id = 113
    name = "Helipad_113"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-228217.921875, -72069.8125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-228194.09375, -72051.0078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-228209.71875, -72222.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-228241.765625, -71915.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_114(Airport):
    id = 114
    name = "Helipad_114"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-222468.65625, -28966.998047, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-222480.953125, -28927.791015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-222456.375, -29006.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-222468.578125, -28966.947265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_115(Airport):
    id = 115
    name = "Helipad_115"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-248813.5, -63606.941406, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-248836, -63576.80078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-248793.21875, -63575.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-248791.046875, -63637.70703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-248835.140625, -63638.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_116(Airport):
    id = 116
    name = "Helipad_116"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-225668.78125, -23064.505859, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-225658.75, -23040.169921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-225678.8125, -23088.830078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_117(Airport):
    id = 117
    name = "Helipad_117"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(206722.03125, -98750.054688, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(206746.484375, -98746.1953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(206697.78125, -98753.7734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_119(Airport):
    id = 119
    name = "Helipad_119"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-200345.203125, -36831.859375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-200345.203125, -36831.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_120(Airport):
    id = 120
    name = "Helipad_120"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(4824.811035, -168230.28125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(4824.8110351562, -168230.28125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_121(Airport):
    id = 121
    name = "Helipad_121"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(46821.480469, -245006.640625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(46821.48046875, -245006.640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_122(Airport):
    id = 122
    name = "Helipad_122"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(44949.476563, -233284.140625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(44949.4765625, -233284.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_123(Airport):
    id = 123
    name = "Helipad_123"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(11737.285156, 78141.3125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(11737.28515625, 78141.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_124(Airport):
    id = 124
    name = "Helipad_124"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(23805.400391, -231792.9375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(23805.400390625, -231792.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_125(Airport):
    id = 125
    name = "Helipad_125"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(227359.75, -48127.035156, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(227359.75, -48127.03515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_126(Airport):
    id = 126
    name = "Helipad_126"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(55216.226563, -8201.401367, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(55216.2265625, -8201.4013671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_127(Airport):
    id = 127
    name = "Helipad_127"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(99196.703125, 281832.71875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(99196.703125, 281832.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_128(Airport):
    id = 128
    name = "Helipad_128"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(2549.282959, -187689.4375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(2549.2829589844, -187689.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_129(Airport):
    id = 129
    name = "Helipad_129"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(171643.171875, 32166.269531, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(171643.171875, 32166.26953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_130(Airport):
    id = 130
    name = "Helipad_130"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-271792.21875, -13300.441406, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-271792.21875, -13300.44140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_131(Airport):
    id = 131
    name = "Helipad_131"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-124129.28125, -38767.148438, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-124129.28125, -38767.1484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_132(Airport):
    id = 132
    name = "Helipad_132"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-239898.125, -92927.015625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-239898.125, -92927.015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_133(Airport):
    id = 133
    name = "Helipad_133"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(21866.267578, -229639.953125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(21866.267578125, -229639.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_134(Airport):
    id = 134
    name = "Helipad_134"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-245195.828125, -93708.75, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-245195.828125, -93708.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_135(Airport):
    id = 135
    name = "Helipad_135"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-22678.439453, -268661.5, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-22678.439453125, -268661.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_136(Airport):
    id = 136
    name = "Helipad_136"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-2219.406006, -210290.96875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-2219.4060058594, -210290.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_137(Airport):
    id = 137
    name = "Helipad_137"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-10698.604492, -317325.8125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-10698.604492188, -317325.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_138(Airport):
    id = 138
    name = "Helipad_138"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(222517.078125, -41742.527344, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(222517.078125, -41742.52734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_139(Airport):
    id = 139
    name = "Helipad_139"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-166748.0625, 31892.707031, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-166748.0625, 31892.70703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_140(Airport):
    id = 140
    name = "Helipad_140"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(8419.079102, 78839.515625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(8419.0791015625, 78839.515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_141(Airport):
    id = 141
    name = "Helipad_141"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(60216.75, -12288.379883, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(60216.75, -12288.379882812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_142(Airport):
    id = 142
    name = "Helipad_142"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(129617.632813, 117115.390625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(129617.6328125, 117115.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_143(Airport):
    id = 143
    name = "Helipad_143"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(24209.625, -235411.40625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(24209.625, -235411.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_144(Airport):
    id = 144
    name = "Helipad_144"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(221203.9375, -43846.519531, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(221203.9375, -43846.51953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_145(Airport):
    id = 145
    name = "Helipad_145"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-223220.4375, 339599.875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-223211.69203833, 339580.56842874, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-223229.20738205, 339619.21117796, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_146(Airport):
    id = 146
    name = "Helipad_146"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-252415.78125, -9587.150391, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-252413.0625, -9611.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-252418.546875, -9562.98828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_147(Airport):
    id = 147
    name = "Helipad_147"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-207813.390625, -43302.433594, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-207820, -43279.02734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-207806.84375, -43325.765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_148(Airport):
    id = 148
    name = "Helipad_148"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-203136.6875, -64559.292969, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-203136.6875, -64559.29296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_149(Airport):
    id = 149
    name = "Helipad_149"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-251153.53125, -7836.765137, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-251153.53125, -7836.7651367188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_150(Airport):
    id = 150
    name = "Helipad_150"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-135772.71875, 18951.167969, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-135753.09375, 18965.396484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-135792.390625, 18936.935546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_151(Airport):
    id = 151
    name = "Helipad_151"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-145744.890625, 1682.621582, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-145744.890625, 1682.6215820312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_152(Airport):
    id = 152
    name = "Helipad_152"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-85532.171875, 51076.960938, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-85532.171875, 51076.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_153(Airport):
    id = 153
    name = "Helipad_153"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-74410.96875, 54011.53125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-74391.265625, 54025.77734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-74430.59375, 53997.30078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_154(Airport):
    id = 154
    name = "Helipad_154"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-200058.703125, -57188.457031, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-200058.703125, -57188.45703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_155(Airport):
    id = 155
    name = "Helipad_155"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-193789.125, -50862.128906, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-193789.125, -50862.12890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_156(Airport):
    id = 156
    name = "Helipad_156"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-176976.984375, -2193.785645, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-176976.984375, -2193.7856445312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_157(Airport):
    id = 157
    name = "Helipad_157"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-189325.96875, -39286.421875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-189325.96875, -39286.421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_158(Airport):
    id = 158
    name = "Helipad_158"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(221842.484375, 139624.34375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(221842.484375, 139624.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_159(Airport):
    id = 159
    name = "Helipad_159"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(31334.716797, 385438.6875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(31334.716796875, 385438.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_160(Airport):
    id = 160
    name = "Helipad_160"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-55594.832031, 216633.0625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-55594.83203125, 216633.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_161(Airport):
    id = 161
    name = "Helipad_161"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(100143.203125, 196394.390625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(100143.203125, 196394.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_162(Airport):
    id = 162
    name = "Helipad_162"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(127277.054688, 111782.953125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(127277.0546875, 111782.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_163(Airport):
    id = 163
    name = "Helipad_163"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-366070.90625, -20651.453125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-366070.90625, -20651.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_164(Airport):
    id = 164
    name = "Helipad_164"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-124216.078125, -34665.90625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-124216.078125, -34665.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_165(Airport):
    id = 165
    name = "Helipad_165"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-24323.556641, -270753.96875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-24323.556640625, -270753.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_166(Airport):
    id = 166
    name = "Helipad_166"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-348647.8125, -60.603279, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-348647.8125, -60.603275299072, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_167(Airport):
    id = 167
    name = "Helipad_167"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-174607.421875, 25824.818359, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-174607.421875, 25824.818359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_168(Airport):
    id = 168
    name = "Helipad_168"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-313531.53125, -109070.703125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-313531.53125, -109070.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_169(Airport):
    id = 169
    name = "Helipad_169"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-241290.59375, -92618.023438, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-241290.59375, -92618.0234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_170(Airport):
    id = 170
    name = "Helipad_170"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-254881.078125, -63877.308594, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-254881.078125, -63877.30859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_171(Airport):
    id = 171
    name = "Helipad_171"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-167396.859375, 37139.230469, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-167396.859375, 37139.23046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_172(Airport):
    id = 172
    name = "Helipad_172"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-35451.175781, 75210.96875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-35451.17578125, 75210.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_173(Airport):
    id = 173
    name = "Helipad_173"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(130717.890625, 26791.4375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(130717.890625, 26791.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_174(Airport):
    id = 174
    name = "Helipad_174"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-15288.266602, -1718.334473, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-15288.266601562, -1718.3344726562, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_175(Airport):
    id = 175
    name = "Helipad_175"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-312183.625, -96410.125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-312183.625, -96410.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_176(Airport):
    id = 176
    name = "Helipad_176"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-335957.4375, -11038.44043, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-335957.4375, -11038.440429688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_177(Airport):
    id = 177
    name = "Helipad_177"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(30205.117188, 383272.96875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(30205.1171875, 383272.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_178(Airport):
    id = 178
    name = "Helipad_178"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(15238.806641, 381282.0625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(15238.806640625, 381282.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_179(Airport):
    id = 179
    name = "Helipad_179"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(14742.870117, 365007.65625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(14742.870117188, 365007.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_180(Airport):
    id = 180
    name = "Helipad_180"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(30904.890625, 351943.03125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(30904.890625, 351943.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_181(Airport):
    id = 181
    name = "Helipad_181"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-50325.945313, 182096.609375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-50325.9453125, 182096.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_182(Airport):
    id = 182
    name = "Helipad_182"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(224352.53125, -41733.660156, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(224352.53125, -41733.66015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_184(Airport):
    id = 184
    name = "Helipad_184"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(81654.710938, 167697.421875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(81654.7109375, 167697.421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_185(Airport):
    id = 185
    name = "Helipad_185"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-44554.09375, 217666.21875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-44512.9296875, 217686.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-44595.25390625, 217645.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_186(Airport):
    id = 186
    name = "Helipad_186"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-280598.5, -91036.359375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-280568.28125, -91007.7734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-280628.75, -91064.9453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_187(Airport):
    id = 187
    name = "Helipad_187"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-43227.71875, 218511.390625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-43230.05859375, 218558.234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-43225.21875, 218464.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_189(Airport):
    id = 189
    name = "Helipad_189"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-194770.515625, 28548.925781, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-194770.515625, 28548.92578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_190(Airport):
    id = 190
    name = "Helipad_190"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-197349.5, 28554.351563, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-197336.234375, 28511.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-197362.78125, 28597.427734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_191(Airport):
    id = 191
    name = "Helipad_191"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-194069.359375, 28007.244141, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-194069.359375, 28007.244140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_192(Airport):
    id = 192
    name = "Helipad_192"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(223448.421875, -42507.359375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(223398.328125, -42536.6796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(223498.53125, -42478.03125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_193(Airport):
    id = 193
    name = "Helipad_193"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-222915.4375, -52884.019531, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-222915.4375, -52884.01953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_194(Airport):
    id = 194
    name = "Helipad_194"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-322235.25, -115473.703125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-322235.25, -115473.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_195(Airport):
    id = 195
    name = "Helipad_195"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-201979.78125, -68354.03125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-201946.765625, -68313.1328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-202009.09375, -68398.484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_196(Airport):
    id = 196
    name = "Helipad_196"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-315846.625, -112004.65625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-315801.59375, -112024.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-315817.125, -111964.7265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-315891.65625, -111986.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-315873.5, -112044.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_197(Airport):
    id = 197
    name = "Helipad_197"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-360223.125, -102285.273438, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-360185, -102275.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-360228.0625, -102209.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-360276.875, -102336.078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-360200.34375, -102318.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-360216.4375, -102360.8515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-360244.46875, -102252.40625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-360260.28125, -102293.890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-360169.25, -102233.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_198(Airport):
    id = 198
    name = "Helipad_198"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-322427.25, -102375.296875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-322437.75, -102329.3828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-322473, -102383.421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-322381.5, -102366.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-322417.3125, -102421.2109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_199(Airport):
    id = 199
    name = "Helipad_199"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-249323.640625, -54436.375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-249344.890625, -54425.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-249296.953125, -54490.91796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-249346.46875, -54376.7109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-249343.390625, -54492.1640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_200(Airport):
    id = 200
    name = "Helipad_200"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-282810.03125, 6809.364746, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-282810.03125, 6809.3647460938, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_201(Airport):
    id = 201
    name = "Helipad_201"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-281967.4375, 7073.218262, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-281967.4375, 7073.2182617188, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_202(Airport):
    id = 202
    name = "Helipad_202"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-270217.375, -5879.893555, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-270234.96875, -5837.5112304688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-270199.78125, -5922.2763671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_203(Airport):
    id = 203
    name = "Helipad_203"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-193745.6875, 255127.96875, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-193697.84375, 255055.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-193837.0625, 255154.671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-193836.96875, 255105.140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-193649.0625, 255055.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-193834.859375, 255203.828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-193745.9375, 255055.953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-193838.265625, 255055.171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_204(Airport):
    id = 204
    name = "Helipad_204"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-205086.9375, -71998.890625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-205087.03125, -71998.71875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-205138.578125, -72004.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-205035.28125, -71993.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_205(Airport):
    id = 205
    name = "Helipad_205"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-208089.21875, -53706.59375, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-208089.078125, -53706.22265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-208103.234375, -53753.80859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-208075.21875, -53659.37890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_206(Airport):
    id = 206
    name = "Helipad_206"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-202835.875, -43949.472656, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-202841.203125, -43995.83203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-202830.703125, -43903.11328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-202875.859375, -43925.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-202795.890625, -43974.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_207(Airport):
    id = 207
    name = "Helipad_207"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-203320.53125, -72816.695313, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-203360.53125, -72835.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-203280.53125, -72797.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-203321.75, -72816.3515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_208(Airport):
    id = 208
    name = "Helipad_208"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-192752.328125, -69701.320313, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-192752.328125, -69701.3203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_209(Airport):
    id = 209
    name = "Helipad_209"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-327453.5, 13265.248047, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-327409.5625, 13285.690429688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-327497.40625, 13244.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_210(Airport):
    id = 210
    name = "Helipad_210"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-144529.75, 52020.828125, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-144529.765625, 52021.07421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-144529.75, 52072.7578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-144529.765625, 51968.89453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_211(Airport):
    id = 211
    name = "Helipad_211"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-323127.75, 9754.041016, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-323127.75, 9754.041015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_212(Airport):
    id = 212
    name = "Helipad_212"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-243956.65625, 1595.556763, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-243987.25, 1640.8037109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-243926.0625, 1550.3098144531, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_213(Airport):
    id = 213
    name = "Helipad_213"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-268636.0625, -55162.117188, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-268686.125, -55147.14453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-268585.90625, -55177.17578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_214(Airport):
    id = 214
    name = "Helipad_214"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-286938.03125, 2538.717773, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-286989.1875, 2517.0080566406, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-286886.875, 2560.427734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_215(Airport):
    id = 215
    name = "Helipad_215"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-164441.6875, 45795.5, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-164404.03125, 45756.72265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-164479.328125, 45834.2734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_216(Airport):
    id = 216
    name = "Helipad_216"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-198932.3125, 17115.625, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-198966.515625, 17156.896484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-198898.125, 17074.3515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Helipad_219(Airport):
    id = 219
    name = "Helipad_219"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-218041.421875, -77878.648438, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-218050.015625, -77825.4296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-218032.828125, -77931.8671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))


class Tel_Nof(Airport):
    id = 220
    name = "Tel Nof"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=128100000, uhf_hz=250650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-349771.3125, -111673.332031, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield220_0'))
        self.runways.append(Runway(id=1, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[]), opposite=RunwayApproach(name='36', heading=360, beacons=[RunwayBeacon(id='airfield220_1', runway_name='18-36', runway_id=1, runway_side='36'), RunwayBeacon(id='airfield220_2', runway_name='18-36', runway_id=1, runway_side='36')])))
        self.runways.append(Runway(id=2, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.runways.append(Runway(id=3, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-349562.875, -112837.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-349612.15625, -113499.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-349681.82061399, -114186.54092125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-349362.07078964, -113405.94315226, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-349543.79227097, -113993.1906537, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-349694, -114159.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-349540.73716611, -112873.57078464, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-349551.34193708, -112854.0068343, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-351113.53125, -111741.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-351113.2942621, -111911.07410516, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-349899.70416511, -112796.79943438, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='57', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-350432.85716409, -112285.2590556, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-349687.15625, -112560.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-350459.40625, -113639.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-349958.00536628, -112854.01963813, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='62', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-349853.81307294, -112837.31669134, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='55', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-351189.59375, -111689.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-349924.3050387, -112778.4369647, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='58', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-349896.98525754, -112363.26564891, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-349923.64998209, -112349.00911895, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-349822.5, -113332.8828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='18', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-350316.34375, -112576.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-349185.35186399, -112740.33076238, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-350489.46875, -113570.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-349795.59375, -113305.0390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='19', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-349414.26968199, -112826.39907763, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-350367.71460518, -112210.93672137, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-349647.59375, -113627.546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-350468.6875, -113617.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-349640.125, -113528.96875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-351457.48064566, -111890.20819654, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-349905.6875, -112494.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-349698.28125, -112540.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-348655.18010486, -113225.81661493, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-349416.39042401, -112795.62405839, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-348682.92925021, -113239.19670407, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-349825.34375, -114092.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-350909.45021432, -111870.36762877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-351381.03411878, -113484.31578318, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-349872.71875, -113679.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-350916.66896432, -111823.05512877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-349960.21875, -112524.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-350479.875, -113591.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-349985.44855286, -112319.44315226, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-349623.61305264, -114062.20817429, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-350659.625, -113628.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-350412.58764593, -112262.18555342, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-349877.90743622, -112818.23625335, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='56', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-349962.875, -112501.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-349848.28125, -113360.7578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='17', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-349920, -112512.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-349146.76560507, -113308.04780936, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-349187.4483772, -112709.71827286, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-350906.04396432, -111893.71137877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-351001.03125, -111704.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-350101.375, -112915.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='66', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-350388.04546805, -112234.01767207, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-349419.42593199, -112758.45111508, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-349912.40878209, -112895.7801628, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='60', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-349958.35445155, -112333.81358012, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-350103.09375, -114230.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-350167.78125, -112995.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='63', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-349611.2711315, -114089.16730286, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-349813.12223679, -114119.54092125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-350122.59375, -112940.8828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='65', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-350167.59375, -112904.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='70', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-351172.65625, -113407.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-349662.96875, -113507.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-350515.9375, -113911.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-351392.62010189, -111964.80883232, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-349935.84402066, -112875.83545328, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='61', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-349679.34375, -113434.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-349556.41618322, -113965.67544605, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-349715.25, -113562.390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-351284.21185592, -113527.2091561, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-350144.34375, -112966.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='64', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-348743.99818708, -113269.39018373, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-350188.75, -112931.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='69', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-349180.22334207, -112807.7380925, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-350912.98146432, -111846.16450377, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-350360.78125, -114228.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-351432.10767164, -113439.50326325, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-349685.03125, -113486.984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-351138.12858801, -111939.75913752, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-350674.75, -113512.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-349168.35203964, -113287.64336829, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-349708.59375, -113464.8671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-349585.90625, -112790.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-349676.03125, -112581.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-349421.476462, -112727.39628993, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-349182.35110529, -112777.66861472, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-349870.5, -113608.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-349578.625, -112805.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-349782.53125, -113498.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-349791.29509465, -112895.83257485, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='53', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-349874.65625, -113388.3203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='16', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-349653.90625, -112622.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-349628.375, -112669.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-349806.5, -113901.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='133', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-349569.875, -112822.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-350209.85694647, -112960.85968281, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='68', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-349957.59375, -112455.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-349812.62333668, -112872.86880125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='54', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-349738, -113541.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-351056.75, -111780.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-351093.67275882, -111887.60496798, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-351061.57445654, -111668.34770145, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-349655.78125, -113455.1796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-351403.83701438, -113463.68000301, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-350144.15625, -112881.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='71', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-348716.40161807, -113255.83591757, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-349340.08843498, -113426.34524252, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-351036.53125, -111792.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-349884.31697015, -112909.72730075, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='59', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-351254.60567943, -113526.61050457, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-350121.59375, -112853.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='72', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-349639.53125, -112649.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-349670.4375, -113605.78125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-351437.28210465, -111913.32018667, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-349296.41758973, -113339.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-349266.55365453, -113336.47407919, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-349665.03125, -112602.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-350436.03125, -112879.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-349760.59375, -113520.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-350447.90625, -113663.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-349575.625, -112717.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-349692.4375, -113583.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-351412.70618821, -111941.55390693, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-349351.75, -113536.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-349634.34375, -113477.59375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='14', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-350020.1875, -114191.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='124', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-350078.65625, -112887.0859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='67', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-351158.09841588, -111962.83368042, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-350438.09375, -113685.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-351321.06889503, -113528.2060914, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=21.0, width=15.0, height=8.0, shelter=False))


class Ben_Gurion(Airport):
    id = 221
    name = "Ben Gurion"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4125000, vhf_low_hz=39150000, vhf_high_hz=134600000, uhf_hz=250700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-331339.375, -106248.296875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield221_2'))
        self.runways.append(Runway(id=None, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.runways.append(Runway(id=None, name='26-08', main=RunwayApproach(name='26', heading=260, beacons=[]), opposite=RunwayApproach(name='08', heading=80, beacons=[])))
        self.runways.append(Runway(id=None, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-330917.09375, -104801.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='159', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-331707.40081125, -104827.50867113, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-332159.96875, -104144.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='121', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-331324.28125, -107656.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-332004.34375, -106799.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-332585.65625, -105382.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-330482.03125, -104533.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='171', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-331967.1875, -106774.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-331639.34375, -106562.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-332737.9375, -104726.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-332824.34375, -105307.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-331246.1875, -104809.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='138', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-330327.25, -104442.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='175', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-332719.90625, -105427.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-331481.125, -107302.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-332212.4375, -103797.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-332634.34375, -104775.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-331043.75, -107458.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-330969.34375, -104705.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='154', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-330887.53125, -104783.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='160', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-332743.03125, -105544.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-331825.60403498, -104867.81942233, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-331062.09375, -104805.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='151', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-331963.5, -106174.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-331914.5625, -106087.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-331886.84375, -106124.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-332257.0625, -104579.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-332312.46875, -103806.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='125', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-331259.5625, -107215.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-331319.09375, -104843.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='136', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-331284.21875, -104824.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='137', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-332252.3125, -104651.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-331371.65625, -107167.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-331940.8125, -106048.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-332370.34375, -105312.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-332156.71875, -103986.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='129', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-332347, -105581.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-331208.28125, -104891.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='148', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-332269.65625, -104694.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-332263.875, -104162.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='122', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-331639.53125, -106839.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-331580.375, -106818.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-332199.25, -104537.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-330447.40625, -104512.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='172', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-332758.125, -105280.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-331967.0625, -106010.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-331377.5, -107690.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-331001.8125, -107429.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-331998.9375, -104211.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='119', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-331927.90625, -106751.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-332804.21875, -104579.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-332043.875, -106058.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-331111.09375, -104728.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='142', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-332794.125, -104701.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-331603.03125, -106530.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-332850.5625, -104676.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-330576.59375, -104589.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='168', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-332872.34375, -104548.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-331093.65625, -104823.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='150', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-331078.59375, -107482.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-332061.09375, -104428.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='117', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-332018.5625, -106098.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-331799.09375, -106950.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-331478.15625, -107012.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-330998.96875, -104722.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='153', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-332442.375, -105335.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-331272.78125, -104930.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='146', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-330411.1875, -104490.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='173', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-331212.40625, -104788.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='139', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-332599.875, -105491.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-331410.53125, -107339.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-331175.75, -104872.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='149', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-332727, -104578.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-330783.875, -104722.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='163', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-332372.0625, -103854.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='124', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-331279.03125, -107006.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-331306.40625, -107091.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-330512.1875, -104553.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='170', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-332894.71875, -105288.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-332529.90625, -105466.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-331145.125, -104749.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='141', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-332895.3125, -105341.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-332083.84375, -104179.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='120', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-331639.15625, -104820.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='133', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-332096.90625, -106860.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-331891.3125, -106725.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-332195.34375, -103834.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-330647.4375, -104632.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='166', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-332672.03125, -105519.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-332499.65625, -105635.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-331422.8125, -107712.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-331030.28125, -104785.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='152', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-331991.4375, -106137.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-331281.28125, -107627.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-331078.3125, -104709.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='143', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-331674.34375, -106587.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-332128.875, -104399.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='116', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-331991, -104457.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='118', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-331177.65625, -104769.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='140', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-331895.4375, -107083.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-331803.5625, -106660.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-331856.9375, -106968.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-332723.53125, -105715.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-331338.34375, -104966.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='144', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-330708.03125, -104670, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='164', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-332304.28125, -105382.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-331241.15625, -104911, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='147', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-331258.0625, -107278.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-330860.5, -104637.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='158', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-331241.21875, -107603.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-331660.68552161, -106959.63030062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-332324.28125, -104584.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-331340.65625, -107365.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-331325.5, -107195.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-332437.90625, -105608.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-331503.5625, -107762.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-331793, -107148.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-331718.1875, -106613.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-331740.4723895, -106995.08848981, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-331695.25, -107023.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-331196.875, -107576.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-332778.8125, -105174.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-330916.5, -104675.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='156', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-330542.625, -104571.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='169', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-331751.28125, -107184.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-331426.96875, -106963.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-331461.9375, -107742.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-329760.625, -104695.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='176', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-331120.59375, -107515.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-332384.25, -105415.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-331764.5027692, -104850.79338063, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-332897.8125, -104652.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-330940.34375, -104689.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='155', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-329772.1875, -104767.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='177', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-332217.21875, -104575.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-332942.125, -104624.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-332543.0625, -105364.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-332662.09375, -105684.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-331497.09375, -106884.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-332280.9375, -104579.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-330677.84375, -104652.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='165', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-332656.6875, -104603.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-332669.8125, -105412.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-331306.03125, -104948.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='145', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-331758.5, -106324.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-331385.8125, -104882.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-332126.03125, -103781.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-331938.84375, -106216.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-332452.59375, -105442.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-331514.07713564, -106978.24258274, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-331377.21875, -106917.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-332451.28125, -103896.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='123', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-332592.53125, -104630.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(-332829.3125, -105685.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(-332792.40625, -105248.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(-331156.5, -107544.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(-330367.71875, -104466.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='174', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(-329783.75, -104844.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='178', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(-331282.125, -107339.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(-330612.8125, -104610.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='167', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(-331352.09375, -104862.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(-331759.34375, -106642.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(-332302.71875, -104581.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(-331513.125, -106837.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(-330821.5, -104742.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='162', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(-330886.625, -104655.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='157', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(-331823.28125, -106369.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(-332198.46875, -104368.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='115', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(-332046.78125, -106828.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=36.0, width=36.0, height=15.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(-330855.65625, -104765.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='161', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(-331678.875, -106883.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(-332627.84375, -105398.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(-332685.75, -104750.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=36.0, width=36.0, height=15.0, shelter=False))


class Hatzor(Airport):
    id = 222
    name = "Hatzor"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4150000, vhf_low_hz=39200000, vhf_high_hz=125750000, uhf_hz=250750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-358026.625, -122186.695313, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield222_1'))
        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.runways.append(Runway(id=2, name='29-11', main=RunwayApproach(name='29', heading=290, beacons=[]), opposite=RunwayApproach(name='11', heading=110, beacons=[])))
        self.runways.append(Runway(id=3, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-358623.71875, -120884.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-358616.53125, -121832.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-358691.5, -122690.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-358649.0625, -120726.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-357662.09375, -121210.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-358460.75, -122078.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-358636.53125, -121844.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-358632.375, -120794.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-357586.9375, -121153.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-357542.34375, -121248.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-358464.375, -122480.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-358711.5, -122678.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-358743.15625, -122658.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-358592.375, -121300.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-358691.75, -120874.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-357731.5625, -121237.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-357710.875, -121224.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-357548.875, -121089.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-358764.96875, -123086.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-358634.15625, -122879.0703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='81', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-357749.96875, -121313.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-358299.625, -121409.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-358651.65625, -122716.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-358484.59375, -122468.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-358694.21875, -120425.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-358837.0625, -120937.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-358842.5625, -120909.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-357569.125, -121234.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-357233.22236786, -121405.14238154, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-358670.90625, -122702.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-357621.21875, -121202.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-358598.0625, -122740.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-358869.125, -120781.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-358832.28125, -120966.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-358886.21875, -120360.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-358643.96875, -120748.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-357511.625, -121276.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-359016.65625, -120629.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-358866.03125, -120299.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-358629.46875, -120860.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-358616.75493269, -121202.13007616, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-357597.59375, -121215.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-358462.86897957, -121459.90329456, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-358501.875, -122100.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-357447.15625, -121167.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-358522.5625, -122111.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-358419.01493376, -121444.99952786, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-359028.28125, -120660.6640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-358637.53125, -120771.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-358543.78125, -122120.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-358630.3125, -120826.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-358595.875, -121822.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-357489.40625, -121064.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-358653.9375, -120703.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-359033.34635376, -120764.53485313, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-358687.8125, -120899, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-357434.46875, -121148.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-358350.5, -121428.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-358503.40625, -122455.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-358750.90625, -123063.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-358733.875, -123040.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-357551.9375, -121153.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-358612.25, -120929.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-359025.28018203, -120797.72308803, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-357420.125, -121129.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-358873.5625, -120757.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-358672.125, -120415.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-358682.1875, -120920.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-358857.625, -120829.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-358503.34375, -121251.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-357518.28125, -121079.9609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.0, width=18.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-358717.21875, -120435.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-358674.5, -120943.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-358648.875, -121141.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-357686.5625, -121217.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-358722.0625, -123016.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-358618.03125, -120906.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-358444.21875, -122493.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-358632.78125, -122729.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-358677.96875, -121866.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-358851.53125, -120853.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-358657.78125, -121854.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-358481.53125, -122088.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.0, width=14.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-358424.59375, -122506.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.0, width=14.0, height=6.0, shelter=False))


class Palmachim(Airport):
    id = 223
    name = "Palmachim"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4175000, vhf_low_hz=39250000, vhf_high_hz=118250000, uhf_hz=250800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-342360.6875, -124708.273438, terrain), terrain)

        self.runways.append(Runway(id=2, name='03L-21R', main=RunwayApproach(name='03L', heading=30, beacons=[]), opposite=RunwayApproach(name='21R', heading=210, beacons=[])))
        self.runways.append(Runway(id=1, name='03R-21L', main=RunwayApproach(name='03R', heading=30, beacons=[]), opposite=RunwayApproach(name='21L', heading=210, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-341758.0625, -124729.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-341747.75, -124750.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-341727.3125, -124788.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-341716.59375, -124809.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-341705.8125, -124833.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-341695.65625, -124854.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-341640.96875, -124827.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-341651.6875, -124805.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-341662.46875, -124782.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-341672.625, -124760.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-341694.03125, -124723, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-341704.1875, -124701.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-341802, -124149.6015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='77', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-341779.28125, -124138.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='78', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-341758.3125, -124124.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='79', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-341736.21875, -124112.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='80', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-341713.71875, -124102.1484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='81', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-341691.375, -124090.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='82', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-341668.4375, -124079.9765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='83', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-341646.4375, -124068.65625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='84', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-341624.4375, -124056.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='85', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-341601.40625, -124046.984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='86', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-341579.15625, -124035.1953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='87', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-341556.9375, -124023.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='88', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-341535.125, -124011.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='89', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-341510.875, -124002.3828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='90', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-341490.375, -123988.3828125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='91', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-341467.375, -123978.0078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='92', length=20.0, width=17.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-341232.0625, -123833.2421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='109', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-341210.78125, -123820.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='110', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-341188.5, -123809.6015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='111', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-341166.25, -123798.1328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='112', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-341143, -123788.2265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='113', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-341120.75, -123776.5859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='114', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-341099.375, -123763.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='115', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-341076.84375, -123753.359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='116', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-341054.3125, -123741.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='117', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-341031.8125, -123730.3359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='118', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-341009.71875, -123718.7265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='119', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-340987.0625, -123708.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='120', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-340964.0625, -123698.3359375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='121', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-340941.3125, -123686.8671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='122', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-340919.875, -123673.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='123', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-340898, -123661.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='124', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-341093.875, -123842.203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='103', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-341127.59375, -123859.53125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='102', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-341161.625, -123877.0703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='101', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-340905.4375, -123746.9453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='108', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-340937.90625, -123763.6328125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='107', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-340971.90625, -123781.15625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='106', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-341015.5625, -123802.6015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='105', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-341050.46875, -123820.4765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='104', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-341664.03125, -124157.46875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='73', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-341691.0625, -124170.7890625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='72', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-341717.9375, -124184.4140625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='71', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-341488.71875, -124068.8984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='76', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-341515.84375, -124082.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='75', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-341542.15625, -124095.6015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='74', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-341801.69015005, -124274.14438051, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-341793.62805203, -124288.97941354, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-342073.6875, -124392.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-342064.90625, -124411.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-342097.28125, -124342.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-342088.5, -124361.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-342035.1875, -124333.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-342044, -124314.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-342011.3125, -124381, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-342020.03125, -124362.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-342116.0625, -124379.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-342126.5625, -124356.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-342090.125, -124424.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-342101.53125, -124401.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-342223.90625, -124470.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-342215.125, -124488.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-342248.03125, -124423.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-342239.25, -124442.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-342191.4375, -124416.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-342200.25, -124398.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-342167.71875, -124462.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-342176.4375, -124444.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-342361.0625, -124580.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-342339.78125, -124569.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-342404.1875, -124603.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-342381.46875, -124592.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-342424.5625, -124613.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-342935.28125, -124906.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-342914, -124895.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-342978.40625, -124928.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-342955.6875, -124917.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-342998.78125, -124938.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-343070.57298481, -124945.38814792, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-342889.3125, -124763.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-342873.96875, -124794.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-342904.5625, -124732.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-342897.15625, -124748.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-342635.125, -124510.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-342625.34375, -124530.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-342655.375, -124470.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-342644.8125, -124490.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-342675.6875, -124529.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-342667.71875, -124544.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-342698.03125, -124485.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-342683.0625, -124514.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-341961.40625, -124802.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-342004.53125, -124824.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-341982.84375, -124813.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-342025.96875, -124835.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-341900.15625, -124830.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-341907.53125, -124815.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-341915, -124800.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=15.25, width=10.25, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-341853.625, -124033.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-341843.71875, -124053.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-341768, -123991.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-341758.09375, -124011.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-341666.8125, -123939.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-341656.90625, -123959.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-341579.84375, -123899.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-341569.9375, -123919.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-341286.75, -123719.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-341276.84375, -123740.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-341198.84375, -123675.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-341188.9375, -123695.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-341097.96875, -123624.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-341088.0625, -123645.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-341008.96875, -123580.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-340999.0625, -123600.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-340846.8125, -123611.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='133', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-341882.4375, -124160.3984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='70', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-342797.21875, -124649.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-342417.125, -125094.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=61.0, width=61.0, height=20.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-342885.0625, -124682.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-342896.09375, -124662.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-342905.90625, -124642.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-342916.3125, -124621.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=18.5, width=12.5, height=5.5, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-342881.34375, -124779.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=18.5, width=12.5, height=5.5, shelter=False))


class Helipad_224(Airport):
    id = 224
    name = "Helipad_224"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-10727.029297, 8033.193848, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-10747.880859375, 8044.8515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-10706.178710938, 8021.5361328125, self._terrain), large=False, heli=True,
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
    Prince_Hassan,
    King_Abdullah_II,
    Herzliya,
    Marka,
    Muwaffaq_Salti,
    Helipad_69,
    Helipad_70,
    Helipad_71,
    Helipad_72,
    Helipad_73,
    Helipad_74,
    Helipad_76,
    Helipad_77,
    Helipad_78,
    Helipad_79,
    Helipad_80,
    Helipad_82,
    Helipad_83,
    Helipad_84,
    Helipad_85,
    Helipad_86,
    Helipad_87,
    Helipad_89,
    Helipad_92,
    Helipad_93,
    Helipad_94,
    Helipad_95,
    Helipad_96,
    Helipad_97,
    Helipad_98,
    Helipad_99,
    Helipad_100,
    Helipad_101,
    Helipad_102,
    Helipad_103,
    Helipad_104,
    Helipad_105,
    Helipad_106,
    Helipad_107,
    Helipad_108,
    Helipad_109,
    Helipad_110,
    Helipad_111,
    Helipad_112,
    Helipad_113,
    Helipad_114,
    Helipad_115,
    Helipad_116,
    Helipad_117,
    Helipad_119,
    Helipad_120,
    Helipad_121,
    Helipad_122,
    Helipad_123,
    Helipad_124,
    Helipad_125,
    Helipad_126,
    Helipad_127,
    Helipad_128,
    Helipad_129,
    Helipad_130,
    Helipad_131,
    Helipad_132,
    Helipad_133,
    Helipad_134,
    Helipad_135,
    Helipad_136,
    Helipad_137,
    Helipad_138,
    Helipad_139,
    Helipad_140,
    Helipad_141,
    Helipad_142,
    Helipad_143,
    Helipad_144,
    Helipad_145,
    Helipad_146,
    Helipad_147,
    Helipad_148,
    Helipad_149,
    Helipad_150,
    Helipad_151,
    Helipad_152,
    Helipad_153,
    Helipad_154,
    Helipad_155,
    Helipad_156,
    Helipad_157,
    Helipad_158,
    Helipad_159,
    Helipad_160,
    Helipad_161,
    Helipad_162,
    Helipad_163,
    Helipad_164,
    Helipad_165,
    Helipad_166,
    Helipad_167,
    Helipad_168,
    Helipad_169,
    Helipad_170,
    Helipad_171,
    Helipad_172,
    Helipad_173,
    Helipad_174,
    Helipad_175,
    Helipad_176,
    Helipad_177,
    Helipad_178,
    Helipad_179,
    Helipad_180,
    Helipad_181,
    Helipad_182,
    Helipad_184,
    Helipad_185,
    Helipad_186,
    Helipad_187,
    Helipad_189,
    Helipad_190,
    Helipad_191,
    Helipad_192,
    Helipad_193,
    Helipad_194,
    Helipad_195,
    Helipad_196,
    Helipad_197,
    Helipad_198,
    Helipad_199,
    Helipad_200,
    Helipad_201,
    Helipad_202,
    Helipad_203,
    Helipad_204,
    Helipad_205,
    Helipad_206,
    Helipad_207,
    Helipad_208,
    Helipad_209,
    Helipad_210,
    Helipad_211,
    Helipad_212,
    Helipad_213,
    Helipad_214,
    Helipad_215,
    Helipad_216,
    Helipad_219,
    Tel_Nof,
    Ben_Gurion,
    Hatzor,
    Palmachim,
    Helipad_224,
]

