# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Port_Stanley(Airport):
    id = 1
    name = "Port Stanley"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=118100000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(89025.222656, 93868.265625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield1_1'))
        self.beacons.append(AirportBeacon(id='airfield1_0'))
        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(88872.890625, 93596.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(88874.15625, 93617.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(88874.7890625, 93638.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(88875.390625, 93658.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(88862.609375, 93952.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(88843.453125, 93952.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(88821.21875, 93953.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(88793.125, 94016.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(88774.0390625, 94032.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(88752.515625, 94042.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(89159.5546875, 94720.1171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(89159, 94768.34375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(89198.03125, 94767.4296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(89198.0859375, 94721.453125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(88880.53125, 94599.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T2', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(88906.8203125, 94705.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T1', length=60.0, width=52.0, height=18.0, shelter=False))


class Mount_Pleasant(Airport):
    id = 2
    name = "Mount Pleasant"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4150000, vhf_low_hz=39200000, vhf_high_hz=133350000, uhf_hz=250800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(73318.320312, 47168.748047, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield2_1'))
        self.beacons.append(AirportBeacon(id='airfield2_2'))
        self.beacons.append(AirportBeacon(id='airfield2_3'))
        self.runways.append(Runway(id=2, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[])))
        self.runways.append(Runway(id=1, name='10-28', main=RunwayApproach(name='10', heading=100, beacons=[]), opposite=RunwayApproach(name='28', heading=280, beacons=[RunwayBeacon(id='airfield2_4', runway_name='28-10', runway_id=1, runway_side='28'), RunwayBeacon(id='airfield2_0', runway_name='28-10', runway_id=1, runway_side='28')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(73289.8359375, 46269.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(73243.7578125, 46258.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(73279.296875, 46320.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(73232.9609375, 46309.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(73239.171875, 46472.59765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(73194.4140625, 46462.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(73182.453125, 46508.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(73227.1171875, 46519.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(73191.5625, 48786.3046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(73187.1015625, 48920.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(73346.71875, 49144.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(73463.3125, 48975.88671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(73649.9375, 48974.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(73262.4296875, 48492.83984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(73351.9375, 48674.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(73188.0703125, 45901.59765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(73075.234375, 45856.75390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(73868.8359375, 46166.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(73649.953125, 46719.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(73155.828125, 48683.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(73852.671875, 48685.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(73894.515625, 48481.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(74119.4921875, 48826.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(73994.3515625, 48923.6953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(74058.265625, 48605.08984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(73844.46875, 48107.10546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(73781.890625, 48319.76953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(73203.796875, 45833.40234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(73188.28125, 45697.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(73456.4453125, 45520.0234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(73431.203125, 45845.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(73393.3671875, 45868.8515625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(73346.703125, 45895.765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(74065.7890625, 48260.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(74074.21875, 48439.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(74072.9140625, 48465.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(74071, 48491.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C11', length=26.0, width=22.0, height=11.0, shelter=False))


class San_Carlos_FOB(Airport):
    id = 3
    name = "San Carlos FOB"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4175000, vhf_low_hz=39250000, vhf_high_hz=134350000, uhf_hz=250850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(107939.375, 8484.390625, terrain), terrain)

        self.runways.append(Runway(id=1, name='11-27', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(107926.41685133, 8629.698241451, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(107933.27846005, 8604.9788338942, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(107940.60865135, 8581.3065269883, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(107947.49858877, 8558.5784727169, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(107954.27057294, 8535.8026067306, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(107960.02069688, 8513.5235026695, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(107966.30666034, 8492.7303812665, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(107793.3359375, 8489.1826171875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H6', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(107782.015625, 8520.2099609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H5', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(107770.6796875, 8550.7177734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H4', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(107802.2734375, 8602.6025390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(107824.6640625, 8643.431640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(107781.7265625, 8653.3583984375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=42.0, width=34.0, height=14.0, shelter=False))


class Rio_Gallegos(Airport):
    id = 5
    name = "Rio Gallegos"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4200000, vhf_low_hz=39300000, vhf_high_hz=119100000, uhf_hz=250900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(25718.329375, -703408.191242, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield5_0'))
        self.runways.append(Runway(id=1, name='25-07', main=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield5_1', runway_name='25-07', runway_id=1, runway_side='25'), RunwayBeacon(id='airfield5_2', runway_name='25-07', runway_id=1, runway_side='25')]), opposite=RunwayApproach(name='07', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(26473.5, -701737.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(26535.212890625, -701657.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(26615, -701722.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(26682.455078125, -701642.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(26471.986328125, -701515.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(25492.90234375, -702755, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(25504.27734375, -702772.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(25524.75390625, -702806.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(25514.3671875, -702789.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(25535.208984375, -702822.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(25545.5546875, -702839.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(25555.93359375, -702856.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(25645.353515625, -702559.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(25662.34375, -702489.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='T02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(25722.125, -702180.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='S08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(26078.0625, -703388.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(26049.160921968, -703351.15427127, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(26828.753627094, -701285.89937917, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(26817.02734375, -701313.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(26806.5703125, -701339.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(26747.341796875, -701310.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(26769.150390625, -701260.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(26758.2890625, -701285.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(26165.015625, -702249.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))


class Rio_Grande(Airport):
    id = 6
    name = "Rio Grande"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=39350000, vhf_high_hz=118300000, uhf_hz=250950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-197144.468784, -559487.57478, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield6_1'))
        self.beacons.append(AirportBeacon(id='airfield6_3'))
        self.beacons.append(AirportBeacon(id='airfield6_4'))
        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[RunwayBeacon(id='airfield6_2', runway_name='26-08', runway_id=1, runway_side='26'), RunwayBeacon(id='airfield6_0', runway_name='26-08', runway_id=1, runway_side='26')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-197547.51280997, -559618.60822941, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-197579.3125, -559850.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-197572.796875, -559820.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-197567.6875, -559791, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-197597.0625, -559748.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-197628.375, -559741.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-197662.546875, -559734.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=26.0, width=22.0, height=11.0, shelter=False))


class Ushuaia(Airport):
    id = 7
    name = "Ushuaia"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=118100000, uhf_hz=251000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-320586.703125, -576144.78125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield7_2'))
        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield7_1', runway_name='25-07', runway_id=1, runway_side='25'), RunwayBeacon(id='airfield7_0', runway_name='25-07', runway_id=1, runway_side='25')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-320280.0625, -576962.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-320413.3125, -577172.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-320384.28125, -577117.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-320416.21875, -576783.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-320453.9375, -576739.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-320422.40625, -576811.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-320428.6875, -576838.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-320434.5625, -576865.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))


class Ushuaia_Helo_Port(Airport):
    id = 8
    name = "Ushuaia Helo Port"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4275000, vhf_low_hz=39450000, vhf_high_hz=118500000, uhf_hz=251050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-318409.578125, -577046.9375, terrain), terrain)

        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-317890.73417401, -577297.15930203, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-317930.90625, -577290.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-318009.49206167, -577277.57116457, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-317970.15625, -577284.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-317850.25, -577306.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-318246.89442221, -577232.60760593, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-318190.28190537, -577242.35305371, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-317622.27429472, -577307.19234744, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.0, width=23.0, height=10.0, shelter=False))


class Punta_Arenas(Airport):
    id = 9
    name = "Punta Arenas"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4300000, vhf_low_hz=39500000, vhf_high_hz=118700000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-147785.300936, -779608.568689, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield9_2'))
        self.beacons.append(AirportBeacon(id='airfield9_3'))
        self.runways.append(Runway(id=1, name='25-07', main=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield9_1', runway_name='25-07', runway_id=1, runway_side='25'), RunwayBeacon(id='airfield9_0', runway_name='25-07', runway_id=1, runway_side='25')]), opposite=RunwayApproach(name='07', heading=70, beacons=[])))
        self.runways.append(Runway(id=3, name='19-01', main=RunwayApproach(name='19', heading=190, beacons=[]), opposite=RunwayApproach(name='01', heading=10, beacons=[])))
        self.runways.append(Runway(id=2, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-148739.765625, -778607, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-148729.6875, -778586.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-148516.578125, -778462.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-148488.859375, -778460.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-147084.5, -779895.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-146753.96875, -779604.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-146318.34375, -778615.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-146759.2491324, -777761.12476919, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-146778.84375, -777748.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-147013.13021562, -777685.94998149, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-147034.19101438, -777693.53297319, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-147304.390625, -777816.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F3', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-146720.359375, -778080.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-146665.953125, -778283.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-146755.59375, -778445.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-146768.515625, -778432.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-146780.76684582, -778419.11879168, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-147340.515625, -777927.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F1', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-147393.890625, -777916.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F2', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-147299.796875, -777795.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F4', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-147295.0625, -777774.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F5', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-147290.640625, -777753.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F6', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-147285.765625, -777732.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F7', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-147368.1875, -777790.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H1', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-147360.6875, -777756.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H2', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-147353.328125, -777722.3125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H3', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-147389.953125, -777713.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-147412.796875, -777708, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-147435.953125, -777702.4375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-146274.1875, -779004.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='QRF12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-148167.34375, -778812.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='QRF05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-147525.03125, -778883.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A1', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-147487.90625, -778790.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A2', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-147463.140625, -778687.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A3', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-147399.828125, -779058.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-147439.546875, -779049.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='HR02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-146558.875, -778592.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-146548.953125, -778610.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-146538.796875, -778627.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-146528.53125, -778644.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-146518.421875, -778661.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-146508.375, -778678.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-146759.46875, -778685.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-146762.90625, -778666.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-146745.671875, -778764.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-146749.109375, -778745, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-146752.578125, -778725.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_09', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-146756.046875, -778705.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='HAS_10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-146742.84375, -778458.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-147472.625, -777959.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F8', length=26.0, width=24.0, height=11.0, shelter=False))


class Pampa_Guanaco(Airport):
    id = 10
    name = "Pampa Guanaco"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3750000, vhf_low_hz=38400000, vhf_high_hz=118000000, uhf_hz=250000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-238408.351562, -623774.96875, terrain), terrain)

        self.runways.append(Runway(id=1, name='26-08', main=RunwayApproach(name='26', heading=260, beacons=[]), opposite=RunwayApproach(name='08', heading=80, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-238432.22280699, -623479.90424008, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-238426.91882297, -623448.58780978, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))


class San_Julian(Airport):
    id = 11
    name = "San Julian"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=118050000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(297477.765625, -636918.15625, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield11_0'))
        self.runways.append(Runway(id=1, name='25-07', main=RunwayApproach(name='25', heading=250, beacons=[]), opposite=RunwayApproach(name='07', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(298061.05416072, -636079.75084617, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(298060.8838024, -636063.38008032, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F06', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(298010.33392067, -636066.37467357, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F08', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(298019.34017558, -636051.7834765, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F07', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(297940.27299971, -636279.83705037, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(297941.27144763, -636262.56814754, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(297980.21692236, -636298.90390998, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(297991.02793975, -636286.43819467, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(297276.91575997, -636815.26432669, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=40.0, width=40.0, height=12.0, shelter=False))


class Puerto_Williams(Airport):
    id = 12
    name = "Puerto Williams"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=118500000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-323519.353789, -531926.173104, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield12_0'))
        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-323574.27915013, -531349.32468435, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-323566.83874946, -531295.27050397, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-323704.98344978, -532198.36674949, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-323709.43003312, -532235.68198951, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-323714.71863043, -532275.37674118, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=24.0, height=11.0, shelter=False))


class Puerto_Natales(Airport):
    id = 13
    name = "Puerto Natales"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=128100000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-24058.357422, -923008.125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield13_0'))
        self.runways.append(Runway(id=1, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-23851.2734375, -923026.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-23853.8828125, -923142.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-23804.03125, -923123.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-23831.548828125, -923135.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))


class El_Calafate(Airport):
    id = 14
    name = "El Calafate"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=119950000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(136356.9375, -922477.96875, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield14_2'))
        self.runways.append(Runway(id=1, name='25-07', main=RunwayApproach(name='25', heading=250, beacons=[RunwayBeacon(id='airfield14_1', runway_name='07-25', runway_id=1, runway_side='25'), RunwayBeacon(id='airfield14_0', runway_name='25-07', runway_id=1, runway_side='25')]), opposite=RunwayApproach(name='07', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(135948.5625, -922618.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(135970.63398495, -922546.28590997, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(136057.734375, -922362.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(136030.515625, -922354.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(136000.296875, -922346.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(136039.54371395, -922459.25157755, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(136117.53125, -921995.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H03', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(135986.35445062, -922493.94844388, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(136011.01087707, -922450.0427212, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(135984.80340107, -922441.06882888, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=24.0, height=11.0, shelter=False))


class Puerto_Santa_Cruz(Airport):
    id = 15
    name = "Puerto Santa Cruz"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118600000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(210340.710938, -680891.53125, terrain), terrain)

        self.runways.append(Runway(id=1, name='07-07', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='07', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(209873.90625, -680756.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(209891.46875, -680740.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(209905.734375, -680730, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(209919.765625, -680719.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(209990.9077879, -680673.06594889, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(210089.12741728, -680638.95849086, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(210068.05170269, -680613.67142594, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(210063.41324279, -680660.48460165, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand04', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(210043.68709301, -680675.79663137, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(210023.57633052, -680690.98850221, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand06', length=30.0, width=23.0, height=10.0, shelter=False))


class Comandante_Luis_Piedrabuena(Airport):
    id = 16
    name = "Comandante Luis Piedrabuena"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=122100000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(208540.984375, -707860.46875, terrain), terrain)

        self.runways.append(Runway(id=1, name='26-08', main=RunwayApproach(name='26', heading=260, beacons=[]), opposite=RunwayApproach(name='08', heading=80, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(208098.6875, -707718.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(208164.1875, -707636.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(208119.0625, -707632.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(208105.78125, -707684.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(208144.734375, -707780.6875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(208115.171875, -707775.5, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(208090.21875, -707770.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(208740.71875, -707317.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(208692.671875, -707247.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=21.0, width=15.0, height=8.0, shelter=False))


class Aerodromo_De_Tolhuin(Airport):
    id = 17
    name = "Aerodromo De Tolhuin"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=118150000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-271432.625, -510004.6875, terrain), terrain)

        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-271388.0625, -509369.90625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-271422.0625, -509430.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-271435.40625, -509531.8125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-271190.875, -509516.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-271215.21875, -509588.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-271210.75, -509832.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-271175.28125, -509800.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=22.0, height=11.0, shelter=False))


class Porvenir_Airfield(Airport):
    id = 18
    name = "Porvenir Airfield"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=126700000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-168264.273438, -738640.3125, terrain), terrain)

        self.runways.append(Runway(id=2, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.runways.append(Runway(id=1, name='09-27', main=RunwayApproach(name='09', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-168373.515625, -739012.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-168377.46875, -738989.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-168381.390625, -738966, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-168385.421875, -738942.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-168389.5, -738918.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-168360.953125, -738883.75, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-168391.875, -738888.1875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))


class Almirante_Schroeders(Airport):
    id = 19
    name = "Almirante Schroeders"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-209214.25, -741523.0625, terrain), terrain)

        self.runways.append(Runway(id=2, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.runways.append(Runway(id=1, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-209534.28125, -740958.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-209456.078125, -741610.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-209454.390625, -741583.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-209458.43538644, -741665.70166268, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-209839.90625, -740973.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-209452.609375, -741555.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-209446.421875, -741467.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-209417.5625, -741759.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-209873.234375, -740945.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-209834.109375, -740997.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-209450.734375, -741526.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-209877.359375, -741017, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='Stand04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-209457.640625, -741637.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-209448.53125, -741497.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=26.0, width=24.0, height=11.0, shelter=False))


class Rio_Turbio(Airport):
    id = 20
    name = "Rio Turbio"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118100000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-12261.766602, -903418.8125, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield20_0'))
        self.runways.append(Runway(id=None, name='24-6', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='6', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-12224.193915032, -903905.44177845, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=41.0, width=41.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-12269.675616921, -903917.22514503, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-12302.5859375, -903917.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=26.0, width=24.0, height=11.0, shelter=False))


class Rio_Chico(Airport):
    id = 21
    name = "Rio Chico"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=118200000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(19603.670898, -699092, terrain), terrain)

        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(19867.458984375, -698786.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(19883.187003973, -698743.33939205, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(19836.9921875, -698775, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))


class Caleta_Tortel_Airport(Airport):
    id = 22
    name = "Caleta Tortel Airport"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(388906, -1088761.6875, terrain), terrain)

        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(389126.125, -1088453.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(389127, -1088476, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(389128.03125, -1088498.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(389105.625, -1088519.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))


class Franco_Bianco(Airport):
    id = 23
    name = "Franco Bianco"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=128500000, uhf_hz=250600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-99216.238281, -683357.0625, terrain), terrain)

        self.runways.append(Runway(id=2, name='19-01', main=RunwayApproach(name='19', heading=190, beacons=[]), opposite=RunwayApproach(name='01', heading=10, beacons=[])))
        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-98902.2421875, -682769.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='S04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-98948.7265625, -682855.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-98890.890625, -682852.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-98884.1953125, -682821.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='S03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-99091.265625, -683143.125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-99045.890625, -683091.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-99004.921875, -683041.9375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-98953.7265625, -683937.25, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-98869.1796875, -683910.375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.0, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-98783.890625, -683886.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.0, width=23.0, height=10.0, shelter=False))


class Goose_Green(Airport):
    id = 24
    name = "Goose Green"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=126000000, uhf_hz=250650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(72564.992188, 11161.910645, terrain), terrain)

        self.runways.append(Runway(id=1, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(72692.828125, 11113.881835938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(72669.140625, 11127.302734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(72648.953125, 11141.979492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(72629.5078125, 11156.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(72612.5859375, 11170.282226562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(72594.2421875, 11184.521484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=21.0, width=15.0, height=8.0, shelter=False))


class Hipico_Flying_Club(Airport):
    id = 25
    name = "Hipico Flying Club"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(329967.3125, -823640.0625, terrain), terrain)

        self.runways.append(Runway(id=1, name='19-01', main=RunwayApproach(name='19', heading=190, beacons=[]), opposite=RunwayApproach(name='01', heading=10, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(330286.40625, -823671.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(330277.21875, -823652.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(330268.90625, -823634.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(330256.96875, -823615.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))


class Aeropuerto_de_Gobernador_Gregores(Airport):
    id = 26
    name = "Aeropuerto de Gobernador Gregores"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=118100000, uhf_hz=250700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(328115.09375, -817026.1875, terrain), terrain)

        self.runways.append(Runway(id=1, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(328016, -818027.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(327996.4375, -818011.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(327977.75, -817994.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(327958.1875, -817977.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(328125.4375, -818227.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(328124.28125, -818197.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))


class Aerodromo_O_Higgins(Airport):
    id = 27
    name = "Aerodromo O'Higgins"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4125000, vhf_low_hz=39150000, vhf_high_hz=118250000, uhf_hz=250750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(328843.03125, -1000893.75, terrain), terrain)

        self.runways.append(Runway(id=1, name='34-16', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='16', heading=160, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(329134.65625, -1000799.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(329162.46875, -1000858.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(329169.9375, -1000840.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(329157.15625, -1000808.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))


class Gull_Point(Airport):
    id = 29
    name = "Gull Point"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(32793.739258, 20419.773438, terrain), terrain)

        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.runways.append(Runway(id=2, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(32569.24609375, 20531.013671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Port_Stanley,
    Mount_Pleasant,
    San_Carlos_FOB,
    Rio_Gallegos,
    Rio_Grande,
    Ushuaia,
    Ushuaia_Helo_Port,
    Punta_Arenas,
    Pampa_Guanaco,
    San_Julian,
    Puerto_Williams,
    Puerto_Natales,
    El_Calafate,
    Puerto_Santa_Cruz,
    Comandante_Luis_Piedrabuena,
    Aerodromo_De_Tolhuin,
    Porvenir_Airfield,
    Almirante_Schroeders,
    Rio_Turbio,
    Rio_Chico,
    Caleta_Tortel_Airport,
    Franco_Bianco,
    Goose_Green,
    Hipico_Flying_Club,
    Aeropuerto_de_Gobernador_Gregores,
    Aerodromo_O_Higgins,
    Gull_Point,
]

