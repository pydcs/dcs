# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Rota_Intl(Airport):
    id = 1
    name = "Rota Intl"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3750000, vhf_low_hz=38400000, vhf_high_hz=123600000, uhf_hz=250000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(75884.859375, 48589.876953, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield1_0'))
        self.runways.append(Runway(id=None, name='9-27', main=RunwayApproach(name='9', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(75707.6015625, 49014.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(75630.046875, 49112.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(75629.2890625, 49162.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(75628.1328125, 49214.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(75621.208201164, 49052.942823717, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(75708.328125, 48871.59765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(75682.515625, 48870.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(75656.5390625, 48870.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(75630.5546875, 48870.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=21.0, width=15.0, height=8.0, shelter=False))


class Saipan_Intl(Airport):
    id = 2
    name = "Saipan Intl"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=125700000, uhf_hz=256900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(180035.4375, 101855.960938, terrain), terrain)

        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(180180.15625, 101120.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(180207.171875, 101187.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(180234.25, 101254.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(180261.25, 101322.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(180288.28125, 101389.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(180161.78125, 101053.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(180819.109375, 101515.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(180779.625, 101512.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(180737.5, 101510.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(180690.703125, 101510.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(180648.296875, 101509.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(180602.6875, 101508.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(180553.9375, 101506.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(180509.453125, 101506.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(180446.546875, 101489.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(180392.984375, 101485.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(180564.6875, 101586.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(180522.9375, 101585.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(180471.484375, 101585.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))


class Tinian_Intl(Airport):
    id = 3
    name = "Tinian Intl"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=123650000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(166859.859375, 89956.625, terrain), terrain)

        self.runways.append(Runway(id=2, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(166417.98813301, 90821.756445869, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(166400.99670044, 90761.885857966, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(166384.48702628, 90680.742496358, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(166395.7764307, 90734.518646327, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))


class Antonio_B__Won_Pat_Intl(Airport):
    id = 4
    name = "Antonio B. Won Pat Intl"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=118100000, uhf_hz=340200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-23.656158, -77.940308, terrain), terrain)

        self.runways.append(Runway(id=2, name='06R-24L', main=RunwayApproach(name='06R', heading=60, beacons=[]), opposite=RunwayApproach(name='24L', heading=240, beacons=[])))
        self.runways.append(Runway(id=1, name='06L-24R', main=RunwayApproach(name='06L', heading=60, beacons=[]), opposite=RunwayApproach(name='24R', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(624.08526611328, 668.80841064453, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(903.26086425781, 1196.6584472656, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(877.47869873047, 1147.7442626953, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(831.55505371094, 1061.0874023438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(785.39916992188, 973.69891357422, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(752.67144775391, 911.82092285156, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(719.86956787109, 849.861328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(686.99957275391, 788.45050048828, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(656.14630126953, 729.50567626953, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(964.23852539062, 1304.1909179687, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(1021.7053222656, 1303.4621582031, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(1061.9135742188, 1264.2581787109, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(1057.2142333984, 1206.6239013672, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(1030.521484375, 1165.5142822266, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(1009.8323364258, 1124.9478759766, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(987.93524169922, 1084.8646240234, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-357.14587402344, 570.22686767578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-387.22058105469, 503.13943481445, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-419.94061279297, 429.78918457031, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-449.54592895508, 364.64956665039, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-478.32592773438, 300.09509277344, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-508.40155029297, 233.57110595703, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(930.90014648438, 1247.4781494141, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))


class Olf_Orote(Airport):
    id = 5
    name = "Olf Orote"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-5023.305023, -16869.435119, terrain), terrain)

        self.runways.append(Runway(id=None, name='25-7', main=RunwayApproach(name='25', heading=250, beacons=[]), opposite=RunwayApproach(name='7', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-4995.8515625, -17498.607421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-4957.580078125, -17589.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-5037.1059570312, -17404.8046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-5470.4145507812, -16340.846679688, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Andersen_AFB(Airport):
    id = 6
    name = "Andersen AFB"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=126200000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(10574.989746, 14548.833496, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield6_0'))
        self.runways.append(Runway(id=1, name='06L-24R', main=RunwayApproach(name='06L', heading=60, beacons=[]), opposite=RunwayApproach(name='24R', heading=240, beacons=[])))
        self.runways.append(Runway(id=2, name='06R-24L', main=RunwayApproach(name='06R', heading=60, beacons=[]), opposite=RunwayApproach(name='24L', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(9766.2216796875, 13546.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(9825.9228515625, 13681.387695312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(9885.3564453125, 13817.124023438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(9693.576171875, 13361.888671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(9702.2646484375, 13382.290039062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(9711.2919921875, 13402.705078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(9663.95703125, 13294.158203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(9672.7333984375, 13314.536132812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(9681.7265625, 13334.771484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(9634.0908203125, 13226.369140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(9643.0224609375, 13246.771484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(9651.8623046875, 13267.126953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(9622.4833984375, 13199.209960938, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(9613.4248046875, 13178.915039062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(9604.552734375, 13158.62890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(9753.2021484375, 13208.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(9790.140625, 13277.35546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(9815.87890625, 13352.154296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(9852.8388671875, 13420.676757812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(9878.421875, 13495.098632812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(9915.744140625, 13564.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(9941.212890625, 13638.620117188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(9978.53515625, 13707.966796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(10029.017578125, 13839.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(10066.16796875, 13908.280273438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(10091.541015625, 13982.23046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(10128.40234375, 14050.508789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(10191.364257812, 14194.41796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(10153.958984375, 14124.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(10216.71875, 14268.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(10310.13671875, 14465.899414063, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(10273.583007812, 14398.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(10460.98046875, 14826.629882812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(10548.072265625, 15016.462890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(10554.439453125, 14938.446289062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(10585.73828125, 15095.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(10782.951171875, 15546.571289063, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(10812.133789062, 15613.290039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(10842.310546875, 15682.249023438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(10871.631835938, 15749.26171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(10901.703125, 15818, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(10931.232421875, 15885.491210938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(10961.026367188, 15953.583984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(10991.408203125, 16023.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(9742.9072265625, 13839.302734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(9908.3916015625, 13976.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(9984.599609375, 14028.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(10247.48828125, 14664.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(10322.262695312, 14770.915039062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(10377.077148438, 14611.384765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(10405.989257813, 14677.46484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(10434.4296875, 14742.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(10423.344726563, 15081.461914062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(10514.0390625, 15226.326171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(10531.203125, 15265.549804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(10562.173828125, 15351.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(10574.465820312, 15444.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(10611.69140625, 15528.14453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(10671.243164063, 15601.162109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(10690.805664062, 15645.865234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(10705.193359375, 15741.854492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(10767.278320313, 15820.668945313, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(10818.395507812, 15937.499023438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(10832.09375, 16031.907226563, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(10892.9375, 16107.874023437, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(9762.8203125, 13930.732421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(9688.3173828125, 13762.889648438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(9644.7392578125, 13657.630859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(9621.640625, 13564.205078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(9566.8642578125, 13490.555664063, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(9522.326171875, 13393.377929688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(9502.8681640625, 13294.806640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(9446.4287109375, 13220.162109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(10284.294921875, 13059.826171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='136', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(10347.38671875, 13203.798828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='134', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(10333.17578125, 13125.755859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='135', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(10427.630859375, 13341.822265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='133', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(10458.077148438, 13411.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='132', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(10490.060546875, 13484.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='131', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(10546.52734375, 13612.943359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='130', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(10577.766601562, 13684.096679687, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='129', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(10609.443359375, 13755.674804687, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='128', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(10640.864257812, 13827.466796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='127', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(10672.130859375, 13898.932617188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='126', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(10703.748046875, 13971.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='125', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(10735.200195312, 14043.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='124', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(10791.09765625, 14170.854492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='123', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(10822.0703125, 14241.646484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='122', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(10885.318359375, 14386.215820312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='120', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(10916.907226562, 14458.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='119', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(10948.34375, 14530.267578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='118', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(11034.15625, 14726.412109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(10962.837890625, 14609.01953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(11064.259765625, 14795.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(11094.572265625, 14864.490234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(11126.666015625, 14937.849609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(11161.450195312, 15017.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(11197.697265625, 15100.197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(11227.0625, 15167.314453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(11329.126953125, 15400.583007812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(11358.500976562, 15467.737304688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(11402.189453125, 15567.608398438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(11431.791992188, 15635.25390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(11475.595703125, 15735.373046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(11505.087890625, 15802.783203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(10238.58203125, 13251.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(10270.0859375, 13322.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(10301.798828125, 13396.702148438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(10332.951171875, 13467.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(10364.151367187, 13539.486328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(10420.53125, 13667.924804688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(10451.880859375, 13739.342773438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(10482.88671875, 13811.041992188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(10514.297851563, 13882.836914062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(10545.56640625, 13954.302734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(10665.935546875, 14229.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(10695.5078125, 14297.017578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(10758.76171875, 14441.580078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(10790.338867188, 14513.780273438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(10821.78125, 14585.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(10853.03125, 14657.057617188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(10937.697265625, 14850.579101562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(10914.969726562, 14778.560546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(10968.014648438, 14919.86328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(10998.080078125, 14988.591796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(11036.654296875, 15056.693359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(11065.430664063, 15142.534179688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(11184.155273438, 15440.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(11214.022460938, 15508.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(11244.372070312, 15578.077148437, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(10745.487304688, 13064.887695312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='137', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(10858.82421875, 13323.940429688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='138', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(10914.08984375, 13450.256835938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='139', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(10943.72265625, 13517.987304688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='140', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(10989.685546875, 13623.038085937, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='141', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(11040.87109375, 13704.485351562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='142', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(11071.96484375, 13811.096679688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='143', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(11115.321289062, 13874.647460938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='144', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(11172.234375, 14004.740234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='145', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(11189.588867188, 14079.947265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='146', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(11285.173828125, 14262.872070312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='147', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(11302.337890625, 14337.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='148', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(11332.2109375, 14405.934570312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='149', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(10825.497070312, 12947.146484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='150', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(10861.384765625, 13029.173828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='151', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(10897.189453125, 13111.008789062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='152', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(10933.05078125, 13192.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='153', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(10968.853515625, 13274.797851563, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='154', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(11004.639648438, 13356.599609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='155', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(11040.517578125, 13438.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='156', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(10968.982421875, 12870.936523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='157', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(11005.0234375, 12953.311523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='158', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(11040.334960937, 13034.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='159', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(11182.65625, 13387.244140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='169', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(11170.426757812, 13359.096679688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='168', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(11158.060546875, 13331.217773438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='167', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(11145.911132813, 13303.262695313, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='166', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(11133.774414063, 13275.104492188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='165', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(11121.518554688, 13247.12109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='164', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(11109.154296875, 13219.349609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='163', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(11096.975585938, 13191.374023437, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='162', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(11084.74609375, 13163.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='161', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(11072.4296875, 13135.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='160', length=21.0, width=15.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(11360.338867188, 13791.580078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='171', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(11395.466796875, 13776.208984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='170', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(11290.008789062, 13822.349609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='173', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(11325.028320312, 13807.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='172', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(11254.23046875, 13838.000976563, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='174', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(11321.28515625, 13893.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='178', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(11285.4296875, 13909.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='179', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(11391.52734375, 13862.935546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='176', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(11356.236328125, 13878.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='177', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(11426.666015625, 13847.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='175', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(11418.205078125, 13923.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='181', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(11453.278320312, 13908.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='180', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(11347.819335937, 13954.475585937, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='183', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(11382.837890625, 13939.154296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='182', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(11312.037109375, 13970.130859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='184', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(11379.061523438, 14025.768554688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='188', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(11343.239257812, 14041.438476562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='189', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(11449.36328125, 13994.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='186', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(11414.111328125, 14010.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='187', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(11484.473632812, 13979.642578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='185', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=187, position=mapping.Point(11476.442382812, 14057.137695312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='191', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=188, position=mapping.Point(11511.658203125, 14041.780273437, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='190', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=189, position=mapping.Point(11406.203125, 14087.919921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='193', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=190, position=mapping.Point(11441.21875, 14072.595703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='192', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=191, position=mapping.Point(11370.419921875, 14103.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='194', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=192, position=mapping.Point(9796.1572265625, 13614.776367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=193, position=mapping.Point(9856.1298828125, 13749.405273438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=194, position=mapping.Point(9735.939453125, 13477.642578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=195, position=mapping.Point(10576.22265625, 14027.25390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=196, position=mapping.Point(10607.504882812, 14098.822265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=60.0, width=60.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=197, position=mapping.Point(10854.17578125, 14314.244140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='121', length=60.0, width=60.0, height=18.0, shelter=False))


class Pagan_Airstrip(Airport):
    id = 7
    name = "Pagan Airstrip"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(512410.262497, 107564.608564, terrain), terrain)

        self.runways.append(Runway(id=None, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(512388.125, 107380.7734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(512369.53125, 107434.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(512351.28125, 107486.7109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))


class North_West_Field(Airport):
    id = 8
    name = "North West Field"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(15909.476563, 7619.561523, terrain), terrain)

        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(15829.838867188, 7461.5131835938, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(15853.114257812, 7510.591796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(15899.426757812, 7599.4477539062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(15877.509765625, 7556.2036132812, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(15922.694335938, 7644.7153320312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(15944.021484375, 7690.5483398438, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(15989.036132812, 7777.4575195312, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(15966.470703125, 7734.8623046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=42.0, width=34.0, height=14.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Rota_Intl,
    Saipan_Intl,
    Tinian_Intl,
    Antonio_B__Won_Pat_Intl,
    Olf_Orote,
    Andersen_AFB,
    Pagan_Airstrip,
    North_West_Field,
]

