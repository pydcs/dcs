# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Creech(Airport):
    id = 1
    name = "Creech"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=118300000, uhf_hz=360600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-360507.203125, -75590.070313, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield1_4'))
        self.runways.append(Runway(id=2, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[RunwayBeacon(id='airfield1_2', runway_name='13-31', runway_id=2, runway_side='13'), RunwayBeacon(id='airfield1_3', runway_name='13-31', runway_id=2, runway_side='13')]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))
        self.runways.append(Runway(id=1, name='08-26', main=RunwayApproach(name='08', heading=80, beacons=[RunwayBeacon(id='airfield1_1', runway_name='08-26', runway_id=1, runway_side='08'), RunwayBeacon(id='airfield1_0', runway_name='08-26', runway_id=1, runway_side='08')]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-359540.25, -74552.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-359619.3125, -74497.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-360846.28125, -74698.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-360846.40625, -74766.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-359427.8125, -74622, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-359510.3125, -74570.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-360688.40625, -75605.421875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-360691.9375, -75478.2578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-360690.71875, -75525.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-360689.9375, -75566.609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-360684.0625, -75825.4765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-360683.21875, -75852.0078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-360682.34375, -75879, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-360684.5625, -75799.6015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-360687.90625, -75691.5625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-360804.03125, -75881.7109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-360687, -75718.4296875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-360685.25, -75772.0234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-360686.21875, -75744.875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-360100.0625, -75474.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B04', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-360083.625, -75450.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B05', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-360116.21875, -75497.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B03', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-360148.25, -75542.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B01', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-360132.5, -75522.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B02', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-360036.59375, -75377.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-360052.375, -75401.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B07', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-360068.09375, -75424.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B06', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-359596.21875, -74579.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-359508.78125, -74632.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-359622.34375, -74561.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-359681.5625, -74639.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-359703.03125, -74625.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-359482.65625, -74649.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-359427.34375, -74809.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-360726.9375, -75298.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-359453.6875, -74792.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-359506.28125, -74757.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-359479.5, -74773.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D07', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-359747.6875, -75579.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-360733.96875, -75144.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-359756.09375, -75618.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-359790.25, -75833.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-359786.09375, -75793.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-360732.125, -75178.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-359638.9375, -74666.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-359660.5625, -74653.3046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-360728.3125, -75268.6640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-360731.09375, -75207.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-360729.75, -75237.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-360725.46875, -75329.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-359619.25, -74679.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D05', length=22.726997, width=18.0, height=6.0, shelter=False))


class Groom_Lake(Airport):
    id = 2
    name = "Groom Lake"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=118000000, uhf_hz=250050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-288604.671875, -86870.445313, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield2_2'))
        self.runways.append(Runway(id=1, name='32-14', main=RunwayApproach(name='32', heading=320, beacons=[RunwayBeacon(id='airfield2_1', runway_name='32-14', runway_id=1, runway_side='32'), RunwayBeacon(id='airfield2_0', runway_name='32-14', runway_id=1, runway_side='32')]), opposite=RunwayApproach(name='14', heading=140, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-287726.5625, -88658.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-287269.25, -88479.9921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-286989.0625, -88658.0546875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-287685.03125, -88662.265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-287320.15625, -88763.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C15', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-287298.84375, -88764.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C16', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-287376.3125, -89030.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-287289.15625, -89037.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-287363.0625, -88761.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C13', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-287337.40625, -89039.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-287341.125, -88761.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C14', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-287210.9375, -88766.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-287206.8125, -88704.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-287208.1875, -88725.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-287205.40625, -88684.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-287209.59375, -88746.3125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-287285, -88883.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C17', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-287204.03125, -88664.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-287811.21875, -88663.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-287973.0625, -88633.6796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-289152.6875, -88598.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-288705.46875, -88614.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-288542.21875, -88724.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-288147.5, -88618.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-288060.5625, -88628.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-288702.4375, -88564.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-287807.78125, -88620.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-287809.5, -88641.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-288535.34375, -88644.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-287085.59375, -87639.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-287078.96875, -87617.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-290292.78125, -86213.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-290298.6875, -86235.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-287091.875, -87661.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-287029.5625, -87687.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-287006.5, -87651.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-287018.875, -87668.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-287860.875, -88624.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B07', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-287863.1875, -88659.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B09', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-287862.09375, -88642.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-287352.21875, -89027.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C10', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-287311.46875, -89033.671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-287395, -89025.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C12', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-290222.4375, -86246.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-290306.0625, -86258.6796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-290244.4375, -86286.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-290233.375, -86265.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-288102.78125, -88625.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-288193.125, -88619.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B01', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-288018.21875, -88631.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-288407.28125, -88792.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-288402.28125, -88720.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=39.857483, width=40.0, height=18.0, shelter=False))


class McCarran_International(Airport):
    id = 3
    name = "McCarran International"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=119900000, uhf_hz=257800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-416011.359375, -26929.336914, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield3_4'))
        self.runways.append(Runway(id=1, name='7R-25L', main=RunwayApproach(name='7R', heading=70, beacons=[]), opposite=RunwayApproach(name='25L', heading=250, beacons=[RunwayBeacon(id='airfield3_2', runway_name='7R-25L', runway_id=1, runway_side='25L'), RunwayBeacon(id='airfield3_0', runway_name='7R-25L', runway_id=1, runway_side='25L')])))
        self.runways.append(Runway(id=2, name='7L-25R', main=RunwayApproach(name='7L', heading=70, beacons=[]), opposite=RunwayApproach(name='25R', heading=250, beacons=[RunwayBeacon(id='airfield3_1', runway_name='7L-25R', runway_id=2, runway_side='25R'), RunwayBeacon(id='airfield3_3', runway_name='7L-25R', runway_id=2, runway_side='25R')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-415461.59375, -25559.572265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-415379.09375, -27106.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-415520.09375, -25553.193359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-415393.625, -25562.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-415257.59375, -25235.619140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-415299.8125, -25565.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-415320.8125, -27463.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-414753.46875, -28874.76953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-414777.9375, -28885.521484375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-414695.3125, -28865.498046875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-414967.5, -29016.703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-414695.21875, -28945.541015625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-415002.8125, -29033.88671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-415041.9375, -29051.591796875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-414803.375, -28895.8671875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))


class Nellis(Airport):
    id = 4
    name = "Nellis"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=132550000, uhf_hz=327000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-398195.375, -17233.236816, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield4_1'))
        self.runways.append(Runway(id=1, name='03L-21R', main=RunwayApproach(name='03L', heading=30, beacons=[]), opposite=RunwayApproach(name='21R', heading=210, beacons=[])))
        self.runways.append(Runway(id=2, name='03R-21L', main=RunwayApproach(name='03R', heading=30, beacons=[]), opposite=RunwayApproach(name='21L', heading=210, beacons=[RunwayBeacon(id='airfield4_2', runway_name='03R-21L', runway_id=2, runway_side='21L'), RunwayBeacon(id='airfield4_0', runway_name='03R-21L', runway_id=2, runway_side='21L')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-399382, -19269.263671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F164', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-399571.96875, -19235.677734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F163', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-399499.84375, -19155.423828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F162', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-399114.03907987, -18563.786478595, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F174', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-399131.5, -18578.552734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F173', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-399148.84375, -18593.533203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F172', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-399165.78125, -18607.830078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F171', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-399183.34375, -18622.427734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F170', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-399200.46875, -18636.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F168', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-399217.33000834, -18651.469482301, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F167', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-399234.625, -18665.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F166', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-399251.90625, -18680.568359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F165', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-399282.90625, -18894.193359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F161', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-399231.25, -18848.525390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F160', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-399181.75, -18801.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F159', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-399130.1875, -18755.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F158', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-399073.6875, -18716.103515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F157', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-399016.21875, -18668.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F156', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-398958.25, -18614.916015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F155', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-398900, -18561.48828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F154', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-398853.46875, -18461.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F147', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-398843.0625, -18473.505859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F148', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-398832.875, -18485.662109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F149', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-398822.53125, -18497.84765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F150', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-398805.84375, -18517.802734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F151', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-398793.28125, -18532.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F152', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-398780.15625, -18548.23828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F153', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-398801.9375, -18417.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F140', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-398791.59375, -18429.390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F141', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-398781.0625, -18442.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F142', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-398770.59375, -18454.69921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F143', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-398754.28125, -18474.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F144', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-398741.59375, -18489.04296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F145', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-398728.53125, -18504.732421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F146', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-398741.5625, -18366.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F133', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-398731, -18378.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F134', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-398720.8125, -18390.49609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F135', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-398709.9375, -18403.228515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F136', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-398693.75, -18422.720703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F137', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-398681.03125, -18437.900390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F138', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-398667.75, -18453.591796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F139', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-398683.4375, -18316.501953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F126', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-398672.65625, -18329.451171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F127', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-398662.25, -18342, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F128', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-398651.84375, -18354.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F129', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-398635.46875, -18373.732421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F130', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-398622.84375, -18389.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F131', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-398609.75, -18404.720703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F132', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-398618.6875, -18262.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F119', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-398608.375, -18275.220703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F120', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-398598.15625, -18287.2109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F121', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-398587.5, -18300.01171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F122', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-398571.28125, -18319.4765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F123', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-398558.46875, -18334.91796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F124', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-398545.40625, -18350.44921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F125', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-398566.25, -18218.408203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F112', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-398555.6875, -18230.869140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F113', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-398545.78125, -18243.04296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F114', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-398534.8125, -18255.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F115', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-398518.6875, -18275.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F116', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-398505.90625, -18290.619140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F117', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-398492.84375, -18306.119140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F118', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-398513, -18175.251953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F104', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-398502.4375, -18187.62890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F105', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-398491.9375, -18200.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F106', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-398481.59375, -18212.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F107', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-398471.53125, -18224.787109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F108', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-398461, -18237.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F109', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-398450.84375, -18249.439453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F110', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-398440.34375, -18262.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F111', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-398458.9375, -18140.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F98', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-398447.8125, -18154.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F99', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-398437.1875, -18168.06640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F100', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-398394.46875, -18219.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F103', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-398409.375, -18201.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F102', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-398415.34375, -18105.625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F92', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-398404.78125, -18118.5546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F93', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-398393.90625, -18131.44140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F94', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-398366.34375, -18164.28515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F96', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-398350.9375, -18182.93359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F97', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-398365.9375, -18063.025390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F86', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-398354.84375, -18076.322265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F87', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-398343.90625, -18089.736328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F88', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-398319.3125, -18124.58984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F90', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-398303.78125, -18143.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F91', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-398274.96875, -18027.361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F85', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-398226.78125, -17986.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F84', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-398200.25, -17963.783203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F83', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-398162.78125, -17932.646484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F82', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-398128.09375, -17903.587890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F81', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-398083.6875, -17865.666015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F80', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-398032.90625, -17823.318359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F79', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-397982.25, -17780.166015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F78', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-397918.90625, -17689.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F72', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-397907.59375, -17703.0546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F73', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-397896.9375, -17715.751953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F74', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-397880.3125, -17735.849609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F75', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-397867.15625, -17751.009765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F76', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-397855.34375, -17765.35546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F77', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-397801.96875, -17720.54296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F71', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-397815.1875, -17704.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F70', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-397827.375, -17690.404296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F68', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-397843.65625, -17670.837890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F67', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-397854.125, -17658.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F66', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-397865.34375, -17644.51953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F65', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-397811.4375, -17599.068359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F59', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-397800.4375, -17613.19140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F60', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-397788.46875, -17626.958984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F61', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-397772.40625, -17645.513671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F62', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-397759.6875, -17660.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F63', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-397747.53125, -17674.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F64', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-397716.375, -17577.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F58', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-397667.3125, -17531.376953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F57', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-397559.28125, -17439.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F55', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-397615.3125, -17489.380859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='F56', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-397510.15625, -17340.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F46', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-397493.6875, -17359.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F48', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-397477.40625, -17378.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F50', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-397464.75, -17393.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F52', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-397452.03125, -17409.013671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F53', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-397440.40625, -17422.537109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F54', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-397462, -17299.533203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F37', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-397444.625, -17318.513671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F39', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-397427.6875, -17336.89453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F41', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-397413.29499166, -17351.711600012, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F43', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-397401.1875, -17366.33984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F44', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-397389.8125, -17379.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F45', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-397407.1875, -17253.310546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F28', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-397390.625, -17273.080078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F30', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-397375.40625, -17290.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F32', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-397361.96875, -17306.853515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F34', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-397349, -17322.4921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F35', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-397337.71875, -17335.544921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F36', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-397334.1875, -17196, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F25', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-397353.84375, -17213.45703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F27', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-397278.96875, -17160.373046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F24', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-397278.84375, -17186.236328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F22', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-397278.46875, -17212.77734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F20', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-397277.8125, -17238.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F18', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-397276.90625, -17269.40234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F15', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-397276.1875, -17305.79296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F13', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-397276.59375, -17287.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F14', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-397229.875, -17159.55078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F01', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-397229.46875, -17185.43359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F03', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-397229.40625, -17212.083984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F05', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(-397228.84375, -17237.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F07', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-397228.5, -17268.95703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F10', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-397228.15625, -17286.427734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F11', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-397228.03125, -17305.197265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F12', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-397002.625, -17428.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-397004.8125, -17372.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-396877.34375, -17320.220703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-396876.6875, -17366.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-396874.65625, -17426.876953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-396904.1875, -17205.203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-396434.90625, -17126.658203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-396433.8125, -17159.294921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(-396433.0625, -17196.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(-396347.3125, -17127.400390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(-396346.875, -17159.0625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(-396346.65625, -17191.56640625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(-396407.03125, -17269.4609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(-396542.78125, -17053.294921875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(-396515.4375, -17052.734375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(-396488.15625, -17052.21875, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(-396587.71875, -17139.625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(-396541.4375, -17138.615234375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(-396495.25, -17137.72265625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(-397010.125, -16819.666015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(-397007.625, -16843.62109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(-397005.1875, -16866.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(-396810.375, -16814.138671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(-396805.96875, -16836.822265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(-396805.1875, -16863.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(-396804.1875, -16888.572265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(-396802.25, -16913.806640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(-396802.40625, -16939.501953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(-397132.90625, -16205.692382812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(-397146.5, -16189.594726563, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(-397160.25, -16173.005859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(-397173.90625, -16156.899414062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(-397187.71875, -16140.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='E11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(-396939.21875, -15793.793945312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='E13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(-397428.4375, -16102.064453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G38', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(-397392.6875, -16146.037109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G39', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(-397538.1875, -16194.713867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G36', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(-397501.71875, -16237.947265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G37', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=187, position=mapping.Point(-397707.84375, -16375.125976562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G35', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=188, position=mapping.Point(-397601.375, -16317.409179687, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G34', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=189, position=mapping.Point(-397639.15625, -16350.887695313, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G33', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=190, position=mapping.Point(-397758.625, -16418.935546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=191, position=mapping.Point(-397796.25, -16451.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G31', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=192, position=mapping.Point(-397833.6875, -16483.826171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=193, position=mapping.Point(-397871.27475984, -16515.491548036, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G29', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=194, position=mapping.Point(-398494.03125, -16288.00390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=195, position=mapping.Point(-398518.25, -16331.268554688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=196, position=mapping.Point(-398541.96875, -16374.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=197, position=mapping.Point(-398566.3125, -16418.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=198, position=mapping.Point(-398590.53125, -16460.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=199, position=mapping.Point(-398614.28125, -16502.412109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=200, position=mapping.Point(-398900.125, -16287.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=201, position=mapping.Point(-398875.03125, -16330.576171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=202, position=mapping.Point(-398850.25, -16372.369140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=203, position=mapping.Point(-398825.0625, -16414.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=204, position=mapping.Point(-398799.84375, -16457.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=205, position=mapping.Point(-398775.1875, -16498.822265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=206, position=mapping.Point(-398865.65625, -17143.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=207, position=mapping.Point(-398913.71875, -17187.091796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G27', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=208, position=mapping.Point(-398964.15625, -17228.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=209, position=mapping.Point(-399057.3125, -17315.94921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=210, position=mapping.Point(-399082.03125, -17336.82421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=211, position=mapping.Point(-399106.8125, -17357.80859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=212, position=mapping.Point(-399131.5, -17378.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=213, position=mapping.Point(-399156.5, -17399.515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=214, position=mapping.Point(-399181, -17420.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=215, position=mapping.Point(-399205.8125, -17441.16796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=216, position=mapping.Point(-399230.40625, -17461.654296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=217, position=mapping.Point(-399255.125, -17482.537109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=218, position=mapping.Point(-399279.9375, -17503.416015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=219, position=mapping.Point(-399304.4375, -17524.091796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=220, position=mapping.Point(-399329.125, -17545.025390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=221, position=mapping.Point(-399354.3125, -17566.173828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=222, position=mapping.Point(-399378.09375, -17586.23046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=223, position=mapping.Point(-399401.75, -17606.201171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=224, position=mapping.Point(-399424.84375, -17625.400390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=225, position=mapping.Point(-399448.03125, -17645.12109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=226, position=mapping.Point(-399471.625, -17664.087890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=227, position=mapping.Point(-399494.59375, -17684.279296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=228, position=mapping.Point(-399518.0625, -17704.013671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=229, position=mapping.Point(-399541.5, -17723.845703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=230, position=mapping.Point(-399564.9375, -17743.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=231, position=mapping.Point(-399588.15625, -17762.86328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=232, position=mapping.Point(-399611.125, -17782.404296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=233, position=mapping.Point(-399634.65625, -17802.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=234, position=mapping.Point(-399250.15625, -18395.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=235, position=mapping.Point(-399263.5, -18373.638671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=236, position=mapping.Point(-399279.5625, -18352.259765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=237, position=mapping.Point(-399297.375, -18331.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=238, position=mapping.Point(-399589.03125, -18011.23828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A13', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=239, position=mapping.Point(-399575.1875, -18027.849609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=240, position=mapping.Point(-399561.96875, -18043.966796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=241, position=mapping.Point(-399548.3125, -18060.470703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=242, position=mapping.Point(-399534.15625, -18076.693359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=243, position=mapping.Point(-399519.9375, -18092.404296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=244, position=mapping.Point(-399506.3125, -18108.962890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=245, position=mapping.Point(-399493.34375, -18125.455078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=246, position=mapping.Point(-399479.59375, -18142.458984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.727446, width=18.0, height=6.0, shelter=False))


class Beatty(Airport):
    id = 5
    name = "Beatty"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-330553.625, -174958.53125, terrain), terrain)

        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-329737.78125, -174776.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-329765.3125, -174776.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-329812.75, -174776.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=30.5, width=20.5, height=6.0, shelter=False))


class Boulder_City(Airport):
    id = 6
    name = "Boulder City"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=118050000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-429660.09375, -1148.724518, terrain), terrain)

        self.runways.append(Runway(id=1, name='27L-9', main=RunwayApproach(name='27L', heading=270, beacons=[]), opposite=RunwayApproach(name='9', heading=90, beacons=[])))
        self.runways.append(Runway(id=1, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-429671, -475.66937255859, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-429641.46941251, -521.85439625786, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-429587.875, -367.20352172852, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-429584.78125, -389.08340454102, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-429581.6875, -410.40881347656, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-429578.0625, -431.21661376953, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-429575.03125, -451.87316894531, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-429571.875, -472.59674072266, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-429568.65625, -493.09997558594, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-429565.34375, -514.28686523438, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-429753.4375, -360.10110473633, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-429741.6875, -409.41787719727, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-429734.90625, -453.82467651367, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-429757.5625, -387.72048950195, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-429751.90625, -433.58285522461, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-429726.21875, -518.19439697266, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-429631.8125, -835.08251953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-429676.75, -816.31884765625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-429702.65625, -819.10211181641, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-429665.625, -956.45343017578, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-429682, -886.85943603516, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-429653.53125, -703.56359863281, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-429650.65625, -764.11791992188, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-429722, -629.05236816406, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-429727.84375, -594.33264160156, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-429734.25, -556.65533447266, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-429656.83592013, -650.40435801079, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-429709.53125, -716.01586914062, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-429704.125, -746.65289306641, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-429699.15625, -776.27526855469, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-429630.34769967, -645.73404377412, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-429643.875, -1040.2800292969, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-429644.09375, -990.54827880859, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-429549.40625, -1073.4930419922, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-429549.09375, -1024.9760742188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-429671, -923.56829833984, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-429655.5, -732.88134765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.727446, width=18.0, height=6.0, shelter=False))


class Echo_Bay(Airport):
    id = 7
    name = "Echo Bay"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-388592.34375, 33697.310547, terrain), terrain)

        self.runways.append(Runway(id=1, name='6-24', main=RunwayApproach(name='6', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-388552.3125, 33604.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-388566.15625, 33543.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H01', length=16.0, width=16.0, height=6.0, shelter=False))


class Henderson_Executive(Airport):
    id = 8
    name = "Henderson Executive"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=125100000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-427352.71875, -25668.716797, terrain), terrain)

        self.runways.append(Runway(id=1, name='35L-17R', main=RunwayApproach(name='35L', heading=350, beacons=[]), opposite=RunwayApproach(name='17R', heading=170, beacons=[])))
        self.runways.append(Runway(id=2, name='35R-17L', main=RunwayApproach(name='35R', heading=350, beacons=[]), opposite=RunwayApproach(name='17L', heading=170, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-428026.78125, -26065.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-427979.9375, -26078.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='H01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-427554.625, -26066.544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B12', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-427554.65625, -26089.80078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B11', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-427555.0625, -26114.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B10', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-427407.125, -26140.626953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-427407.1875, -26116.669921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-427405.75, -26079.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B07', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-427405.71875, -26056.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B08', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-427339.3125, -26086.208984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-427338.96875, -26113.87890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-427339.125, -26058.41015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-427338.5625, -26140.412109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-427214.4375, -26142.978515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A25', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-427214.5625, -26118.896484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A26', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-426943.1875, -26067.935546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-426876, -26068.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-426876.125, -26092.037109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-426821.4375, -26071.060546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-426821.625, -26129.708984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-427212.03125, -26082.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A27', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-427212, -26058.517578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A28', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-427554.75, -26144.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B09', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-426876.1875, -26140.025390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-426875.96875, -26116.658203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-426943.75, -26139.68359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-426943.8125, -26115.65234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-426943.9375, -26092.0234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-426993.90625, -26138.951171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-426993.59375, -26116.001953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-426993.75, -26092.720703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A13', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-426994, -26068.947265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A14', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-427052.0625, -26136.19921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A16', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-427126.65625, -26145.291015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A17', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-427126.4375, -26119.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A18', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-427126.875, -26093.212890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A19', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-427126.34375, -26059.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A20', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-427155.90625, -26144.94921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A21', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-427155.15625, -26119.26953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A22', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-427155.09375, -26083.5, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A23', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-427155.5625, -26059.17578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A24', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-427277, -26060.08984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A29', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-427054.84375, -26064.26953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A15', length=39.857483, width=40.0, height=18.0, shelter=False))


class Jean(Airport):
    id = 9
    name = "Jean"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-450392.859375, -43000.460938, terrain), terrain)

        self.runways.append(Runway(id=1, name='20L-2R', main=RunwayApproach(name='20L', heading=200, beacons=[]), opposite=RunwayApproach(name='2R', heading=20, beacons=[])))
        self.runways.append(Runway(id=2, name='20R-2L', main=RunwayApproach(name='20R', heading=200, beacons=[]), opposite=RunwayApproach(name='2L', heading=20, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-450104.78125, -42994.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-450083.875, -42980.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-450062.40625, -42967.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-450039.75, -42953.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))


class Laughlin(Airport):
    id = 10
    name = "Laughlin"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3750000, vhf_low_hz=38400000, vhf_high_hz=123900000, uhf_hz=250000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-516946.421875, 28306.30957, terrain), terrain)

        self.runways.append(Runway(id=1, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-516446.90625, 28580.93359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-516483.625, 28584.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-516520.3125, 28587.455078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-516557.25, 28590.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-516807.34375, 28610.177734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-516843.625, 28614.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-516881.03125, 28616.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-516916.59375, 28621.19921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-516770.625, 28607.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-516616.71875, 28600.787109375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-516647.1875, 28603.6953125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-516674.90625, 28606.09375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-515958.03125, 28557.603515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-516032.9375, 28569.548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='G02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-516413.78125, 28461.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-516701.28125, 28608.578125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))


class Lincoln_County(Airport):
    id = 11
    name = "Lincoln County"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-224670.351563, 33199.935547, terrain), terrain)

        self.runways.append(Runway(id=1, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-224143.265625, 33338.26953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-224167.59375, 33337.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-224191.8125, 33337.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-224216.578125, 33337.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-224240.3125, 33337.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-224091.5, 33328.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=30.5, width=20.5, height=6.0, shelter=False))


class Mesquite(Airport):
    id = 13
    name = "Mesquite"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-329622.09375, 68561.148438, terrain), terrain)

        self.runways.append(Runway(id=1, name='1-19', main=RunwayApproach(name='1', heading=10, beacons=[]), opposite=RunwayApproach(name='19', heading=190, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-329683.28125, 68345.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-329665.15625, 68355.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-329364.5, 68547.8203125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-329569.78125, 68409.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-329708.84375, 68396.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-329690.875, 68406.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-329673.125, 68416.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-329655.21875, 68425.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-329630.625, 68437.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-329612.1875, 68448.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-329590.25, 68459.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='A07', length=22.727446, width=18.0, height=6.0, shelter=False))


class Mina(Airport):
    id = 14
    name = "Mina"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-161504.46875, -289784.765625, terrain), terrain)

        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))


class North_Las_Vegas(Airport):
    id = 15
    name = "North Las Vegas"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = True
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3775000, vhf_low_hz=38450000, vhf_high_hz=125700000, uhf_hz=360750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-400891.484375, -31726.952148, terrain), terrain)

        self.runways.append(Runway(id=1, name='30L-12R', main=RunwayApproach(name='30L', heading=300, beacons=[]), opposite=RunwayApproach(name='12R', heading=120, beacons=[])))
        self.runways.append(Runway(id=2, name='12L-30R', main=RunwayApproach(name='12L', heading=120, beacons=[RunwayBeacon(id='airfield15_1', runway_name='12L-30R', runway_id=2, runway_side='12L'), RunwayBeacon(id='airfield15_0', runway_name='12L-30R', runway_id=2, runway_side='12L')]), opposite=RunwayApproach(name='30R', heading=300, beacons=[])))
        self.runways.append(Runway(id=3, name='25-7', main=RunwayApproach(name='25', heading=250, beacons=[]), opposite=RunwayApproach(name='7', heading=70, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-401630.4375, -32211.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B17', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-401616.6875, -32228.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B16', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-401717.4375, -31595.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B18', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-401453.5625, -31027.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-401751.5625, -31576.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='B19', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-401354.4375, -31032.263671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='M02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-401489.6875, -30933.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-401440.71875, -30933.94140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-401390.96875, -30933.29296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-401352.0625, -30935.35546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-401325.71875, -30933.8828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-401296.5, -30933.76953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-401270.59375, -30985.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-401270.96875, -31018.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-401270.875, -31066.826171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-401277.34375, -31097.29296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='W01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-401577.625, -32188.427734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B14', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-401562.65625, -32206.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B13', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-401602.6875, -32245.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B15', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-401334.46875, -32438.099609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-401350.59375, -32458.09765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-401366.125, -32478.998046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-401803.5625, -31493.84375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-401858.03125, -31452.5390625, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-401822.5625, -31472.845703125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-401498.875, -32041.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-401498.4375, -32020.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-401497.90625, -31999.55859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-401496.96875, -31978.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-401495.875, -31957.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-401495.46875, -31936.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-401495.15625, -31914.193359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-401433.25, -31965.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-401434, -31987.259765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-401434.4375, -32007.994140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-401434.71875, -32028.744140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-401435.3125, -32049.84765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='B01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-401349.125, -32043.392578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-401371.96875, -32066.841796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-401286.9375, -32101.779296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-401242.15625, -32165.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-401309.96875, -32122.806640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='C03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-401266.5625, -32363.90234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-401280.53125, -32383.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='R04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-400996.53125, -32766.830078125, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-400997.6875, -32797.9609375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-400998.5, -32828.859375, self._terrain), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))


class Pahute_Mesa(Airport):
    id = 16
    name = "Pahute Mesa"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-303620, -132937.929688, terrain), terrain)

        self.runways.append(Runway(id=1, name='36-18', main=RunwayApproach(name='36', heading=360, beacons=[]), opposite=RunwayApproach(name='18', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-303524.92167696, -133026.1164952, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-303622.72626628, -133052.93433556, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-303596.62381344, -133045.59117884, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-303572.4616298, -133039.13607596, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-303548.5625, -133032.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=30.5, width=20.5, height=6.0, shelter=False))


class Tonopah(Airport):
    id = 17
    name = "Tonopah"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = None

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-197282.898438, -201302.882813, terrain), terrain)

        self.runways.append(Runway(id=1, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.runways.append(Runway(id=2, name='29-11', main=RunwayApproach(name='29', heading=290, beacons=[]), opposite=RunwayApproach(name='11', heading=110, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-198277.78125, -202084.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-198234.625, -202096.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-198191.3125, -202108.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-198147.96875, -202119.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-198104.5625, -202131.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A05', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-198061.28125, -202143.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A06', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-198017.90625, -202155.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A07', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-197974.59375, -202167, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A08', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-197931.203125, -202178.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A09', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-197888.296875, -202191.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A10', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-197844.96875, -202203, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A11', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-197801.65625, -202214.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A12', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-197758.28125, -202226.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A13', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-197714.96875, -202238.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A14', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-197671.609375, -202250.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A15', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-197628.296875, -202261.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A16', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-197584.890625, -202273.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A17', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-197541.734375, -202285.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A18', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-197498.34375, -202297.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A19', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-197455.0625, -202309.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A20', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-197411.65625, -202320.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A21', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-197368.34375, -202332.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A22', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-197325.015625, -202344.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A23', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-197281.703125, -202356.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A24', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-197238.3125, -202368.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A25', length=39.857483, width=40.0, height=18.0, shelter=False))


class Tonopah_Test_Range(Airport):
    id = 18
    name = "Tonopah Test Range"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=124750000, uhf_hz=257950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-226505.273438, -174698.484375, terrain), terrain)

        self.beacons.append(AirportBeacon(id='airfield18_4'))
        self.runways.append(Runway(id=1, name='32-14', main=RunwayApproach(name='32', heading=320, beacons=[]), opposite=RunwayApproach(name='14', heading=140, beacons=[RunwayBeacon(id='airfield18_3', runway_name='14-32', runway_id=1, runway_side='14'), RunwayBeacon(id='airfield18_0', runway_name='14-32', runway_id=1, runway_side='14')])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-225679.28125, -174488.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-225566.109375, -174497.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='D13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-225334.95388725, -174677.29806156, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-225305.27862034, -174607.56103651, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-225336.69549492, -174594.64793502, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-225366.11437447, -174663.87932047, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-225368.05984995, -174581.47129585, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-225397.43520077, -174650.9141146, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D05', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-225434.3677049, -174635.32878005, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D07', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-225404.6040749, -174565.07406801, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D08', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-225436.13971854, -174552.33086829, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D10', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-225467.44159797, -174538.94416997, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D12', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-225465.54811448, -174621.86886115, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D09', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-225497.0551549, -174608.87690051, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D11', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-225784.66016626, -174485.6993844, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D16', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-225756.17207304, -174418.12183539, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D17', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-225787.37365922, -174405.15371192, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D19', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-225815.85834898, -174472.03034354, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D18', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-226023.079914, -174305.06717577, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D33', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-226051.430065, -174372.145237, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D32', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-225818.57253879, -174391.47521078, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D21', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-225847.2409015, -174459.02059161, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D20', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-225858.328125, -174374.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D23', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-225888.265625, -174443.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D22', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-225917.87402489, -174428.56350496, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D24', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-225889.47406502, -174361.36936492, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D25', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-225920.92177536, -174348.26105286, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D27', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-225949.39733376, -174415.98412333, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D26', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-225960.40173764, -174331.51832843, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D29', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-225988.76580065, -174398.56491191, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D28', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-225991.92642722, -174318.48805264, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D31', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-226020.14143581, -174385.54689891, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='D30', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-226349.08826391, -174167.6341884, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-226380.33108749, -174154.16114983, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-226411.72351514, -174141.06076098, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-226451.26140048, -174124.29973919, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C08', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-226482.53119996, -174110.99479694, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C10', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-226513.92184931, -174097.78370771, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C12', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-226606.10651026, -174057.5304521, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C14', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-226637.52436533, -174044.59019056, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C16', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-226376.4150904, -174231.81486009, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-226407.58818546, -174218.50625769, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-226438.90190801, -174205.27253551, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-226478.45647197, -174188.35840596, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-226509.6703714, -174175.10336315, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C09', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-226541.01059472, -174161.75745093, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C11', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-226633.67607466, -174122.56833442, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C13', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-226665.11597856, -174109.49366358, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C15', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-226668.99905254, -174031.51725982, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C18', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-226708.41810205, -174014.4719288, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C20', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-226739.67786257, -174001.36779802, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C22', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-226771.49263453, -173988.0099171, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C24', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-226696.44328202, -174096.27250661, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C17', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-226736.08705702, -174079.60198763, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C19', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-226767.1764298, -174066.22197129, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C21', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-226798.65727271, -174053.07863275, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='C23', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-226927.875, -173894.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-226956.390625, -173881.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-226984.34375, -173870.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-227012.8125, -173858.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='F04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-227606.4425991, -173705.90072357, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-227633.84375, -173694.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-227661.33808507, -173682.64142897, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-227688.73477698, -173670.98031801, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='G04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-228133, -173442.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-228068.0625, -173471.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-228098.96875, -173452.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A03', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-228030.828125, -173478.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='A01', length=39.857483, width=40.0, height=18.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Creech,
    Groom_Lake,
    McCarran_International,
    Nellis,
    Beatty,
    Boulder_City,
    Echo_Bay,
    Henderson_Executive,
    Jean,
    Laughlin,
    Lincoln_County,
    Mesquite,
    Mina,
    North_Las_Vegas,
    Pahute_Mesa,
    Tonopah,
    Tonopah_Test_Range,
]

