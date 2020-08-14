from dcs.terrain import Terrain, Airport, Runway, ParkingSlot, MapView, Graph
import dcs.mapping as mapping
import os
from typing import List


class Creech_AFB(Airport):
    id = 1
    name = "Creech AFB"
    position = mapping.Point(-360507.203125, -75590.070313)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Creech_AFB, self).__init__()

        self.runways.append(Runway(80))
        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-359540.25, -74552.5390625), large=False, heli=False,
                airplanes=True, slot_name='D15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-359619.3125, -74497.2734375), large=False, heli=False,
                airplanes=True, slot_name='D17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-360846.28125, -74698.109375), large=False, heli=False,
                airplanes=True, slot_name='A28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-360846.40625, -74766.1171875), large=False, heli=False,
                airplanes=True, slot_name='A27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-359427.8125, -74622), large=False, heli=False,
                airplanes=True, slot_name='D11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-359510.3125, -74570.046875), large=False, heli=False,
                airplanes=True, slot_name='D13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-360688.40625, -75605.421875), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-360691.9375, -75478.2578125), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-360690.71875, -75525.859375), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-360689.9375, -75566.609375), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-360684.0625, -75825.4765625), large=False, heli=True,
                airplanes=False, slot_name='H11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-360683.21875, -75852.0078125), large=False, heli=True,
                airplanes=False, slot_name='H12', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-360682.34375, -75879), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-360684.5625, -75799.6015625), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-360687.90625, -75691.5625), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-360804.03125, -75881.7109375), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-360687, -75718.4296875), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-360685.25, -75772.0234375), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-360686.21875, -75744.875), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-360100.0625, -75474.5234375), large=False, heli=False,
                airplanes=True, slot_name='B04', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-360083.625, -75450.6484375), large=False, heli=False,
                airplanes=True, slot_name='B05', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-360116.21875, -75497.96875), large=False, heli=False,
                airplanes=True, slot_name='B03', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-360148.25, -75542.3359375), large=False, heli=False,
                airplanes=True, slot_name='B01', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-360132.5, -75522.765625), large=False, heli=False,
                airplanes=True, slot_name='B02', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-360036.59375, -75377.625), large=False, heli=False,
                airplanes=True, slot_name='B08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-360052.375, -75401.453125), large=False, heli=False,
                airplanes=True, slot_name='B07', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-360068.09375, -75424.2734375), large=False, heli=False,
                airplanes=True, slot_name='B06', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-359596.21875, -74579.7421875), large=False, heli=False,
                airplanes=True, slot_name='D14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-359508.78125, -74632.1640625), large=False, heli=False,
                airplanes=True, slot_name='D12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-359622.34375, -74561.484375), large=False, heli=False,
                airplanes=True, slot_name='D16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-359681.5625, -74639.53125), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-359703.03125, -74625.03125), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-359482.65625, -74649.734375), large=False, heli=False,
                airplanes=True, slot_name='D10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-359427.34375, -74809.3984375), large=False, heli=False,
                airplanes=True, slot_name='D09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-360726.9375, -75298.4765625), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-359453.6875, -74792.4296875), large=False, heli=False,
                airplanes=True, slot_name='D08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-359506.28125, -74757.234375), large=False, heli=False,
                airplanes=True, slot_name='D06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-359479.5, -74773.4375), large=False, heli=False,
                airplanes=True, slot_name='D07', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-359747.6875, -75579.015625), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-360733.96875, -75144.9375), large=False, heli=False,
                airplanes=True, slot_name='A07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-359756.09375, -75618.3125), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-359790.25, -75833.625), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-359786.09375, -75793.578125), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-360732.125, -75178.484375), large=False, heli=False,
                airplanes=True, slot_name='A06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-359638.9375, -74666.234375), large=False, heli=False,
                airplanes=True, slot_name='D04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-359660.5625, -74653.3046875), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-360728.3125, -75268.6640625), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-360731.09375, -75207.7109375), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-360729.75, -75237.9765625), large=False, heli=False,
                airplanes=True, slot_name='A04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-360725.46875, -75329.1015625), large=False, heli=False,
                airplanes=True, slot_name='A01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-359619.25, -74679.2265625), large=False, heli=False,
                airplanes=True, slot_name='D05', length=22.726997, width=18.0, height=6.0, shelter=False))


class Groom_Lake_AFB(Airport):
    id = 2
    name = "Groom Lake AFB"
    position = mapping.Point(-288604.671875, -86870.445313)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Groom_Lake_AFB, self).__init__()

        self.runways.append(Runway(320))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-287726.5625, -88658.625), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-287269.25, -88479.9921875), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-286989.0625, -88658.0546875), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-287685.03125, -88662.265625), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-287320.15625, -88763.3203125), large=False, heli=False,
                airplanes=True, slot_name='C15', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-287298.84375, -88764.78125), large=False, heli=False,
                airplanes=True, slot_name='C16', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-287376.3125, -89030.9921875), large=False, heli=False,
                airplanes=True, slot_name='C11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-287289.15625, -89037.109375), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-287363.0625, -88761.0859375), large=False, heli=False,
                airplanes=True, slot_name='C13', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-287337.40625, -89039.1875), large=False, heli=False,
                airplanes=True, slot_name='C09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-287341.125, -88761.953125), large=False, heli=False,
                airplanes=True, slot_name='C14', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-287210.9375, -88766.6484375), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-287206.8125, -88704.890625), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-287208.1875, -88725.328125), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-287205.40625, -88684.5234375), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-287209.59375, -88746.3125), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-287285, -88883.7421875), large=False, heli=False,
                airplanes=True, slot_name='C17', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-287204.03125, -88664.140625), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-287811.21875, -88663.1640625), large=False, heli=False,
                airplanes=True, slot_name='B12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-287973.0625, -88633.6796875), large=False, heli=False,
                airplanes=True, slot_name='B06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-289152.6875, -88598.171875), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-288705.46875, -88614.53125), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-288542.21875, -88724.4453125), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-288147.5, -88618.203125), large=False, heli=False,
                airplanes=True, slot_name='B02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-288060.5625, -88628.9921875), large=False, heli=False,
                airplanes=True, slot_name='B04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-288702.4375, -88564.4375), large=False, heli=False,
                airplanes=True, slot_name='A04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-287807.78125, -88620.5859375), large=False, heli=False,
                airplanes=True, slot_name='B10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-287809.5, -88641.59375), large=False, heli=False,
                airplanes=True, slot_name='B11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-288535.34375, -88644.375), large=False, heli=False,
                airplanes=True, slot_name='A01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-287085.59375, -87639.703125), large=False, heli=False,
                airplanes=True, slot_name='05', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-287078.96875, -87617.921875), large=False, heli=False,
                airplanes=True, slot_name='04', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-290292.78125, -86213.3671875), large=False, heli=False,
                airplanes=True, slot_name='10', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-290298.6875, -86235.484375), large=False, heli=False,
                airplanes=True, slot_name='11', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-287091.875, -87661.1171875), large=False, heli=False,
                airplanes=True, slot_name='06', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-287029.5625, -87687.4609375), large=False, heli=False,
                airplanes=True, slot_name='03', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-287006.5, -87651.6328125), large=False, heli=False,
                airplanes=True, slot_name='01', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-287018.875, -87668.265625), large=False, heli=False,
                airplanes=True, slot_name='02', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-287860.875, -88624.703125), large=False, heli=False,
                airplanes=True, slot_name='B07', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-287863.1875, -88659.5859375), large=False, heli=False,
                airplanes=True, slot_name='B09', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-287862.09375, -88642.796875), large=False, heli=False,
                airplanes=True, slot_name='B08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-287352.21875, -89027.96875), large=False, heli=False,
                airplanes=True, slot_name='C10', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-287311.46875, -89033.671875), large=False, heli=False,
                airplanes=True, slot_name='C08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-287395, -89025.0390625), large=False, heli=False,
                airplanes=True, slot_name='C12', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-290222.4375, -86246.6484375), large=False, heli=False,
                airplanes=True, slot_name='07', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-290306.0625, -86258.6796875), large=False, heli=False,
                airplanes=True, slot_name='12', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-290244.4375, -86286.4765625), large=False, heli=False,
                airplanes=True, slot_name='09', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-290233.375, -86265.4140625), large=False, heli=False,
                airplanes=True, slot_name='08', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-288102.78125, -88625.734375), large=False, heli=True,
                airplanes=True, slot_name='B03', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-288193.125, -88619.78125), large=False, heli=True,
                airplanes=True, slot_name='B01', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-288018.21875, -88631.15625), large=False, heli=True,
                airplanes=True, slot_name='B05', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-288407.28125, -88792.3203125), large=False, heli=True,
                airplanes=True, slot_name='A07', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-288402.28125, -88720.9453125), large=False, heli=True,
                airplanes=True, slot_name='A06', length=39.857483, width=40.0, height=18.0, shelter=False))


class McCarran_International_Airport(Airport):
    id = 3
    name = "McCarran International Airport"
    position = mapping.Point(-416011.359375, -26929.336914)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(McCarran_International_Airport, self).__init__()

        self.runways.append(Runway(70))
        self.runways.append(Runway(70))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-415461.59375, -25559.572265625), large=False, heli=True,
                airplanes=True, slot_name='04', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-415379.09375, -27106.3515625), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-415520.09375, -25553.193359375), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-415393.625, -25562.69921875), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-415257.59375, -25235.619140625), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-415299.8125, -25565.33984375), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-415320.8125, -27463.15625), large=False, heli=False,
                airplanes=True, slot_name='07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-414753.46875, -28874.76953125), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-414777.9375, -28885.521484375), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-414695.3125, -28865.498046875), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-414967.5, -29016.703125), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-414695.21875, -28945.541015625), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-415002.8125, -29033.88671875), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-415041.9375, -29051.591796875), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-414803.375, -28895.8671875), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))


class Nellis_AFB(Airport):
    id = 4
    name = "Nellis AFB"
    position = mapping.Point(-398195.359375, -17233.242188)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Nellis_AFB, self).__init__()

        self.runways.append(Runway(30))
        self.runways.append(Runway(30))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-399382, -19269.25390625), large=False, heli=False,
                airplanes=True, slot_name='F164', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-399571.9375, -19235.65234375), large=False, heli=False,
                airplanes=True, slot_name='F163', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-399499.8125, -19155.458984375), large=False, heli=False,
                airplanes=True, slot_name='F162', length=23.076286, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-399113.96875, -18563.66015625), large=False, heli=False,
                airplanes=True, slot_name='F174', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-399131.5625, -18578.541015625), large=False, heli=False,
                airplanes=True, slot_name='F173', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-399148.83161652, -18593.524975894), large=False, heli=False,
                airplanes=True, slot_name='F172', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-399165.80036652, -18607.878284153), large=False, heli=False,
                airplanes=True, slot_name='F171', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-399183.3125, -18622.458984375), large=False, heli=False,
                airplanes=True, slot_name='F170', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-399200.53125, -18636.875), large=False, heli=False,
                airplanes=True, slot_name='F168', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-399217.34375, -18651.2890625), large=False, heli=False,
                airplanes=True, slot_name='F167', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-399234.65625, -18665.939453125), large=False, heli=False,
                airplanes=True, slot_name='F166', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-399251.93644146, -18680.544299778), large=False, heli=False,
                airplanes=True, slot_name='F165', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-399282.875, -18894.181640625), large=False, heli=True,
                airplanes=True, slot_name='F161', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-399231.28125, -18848.50390625), large=False, heli=True,
                airplanes=True, slot_name='F160', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-399181.75, -18801.109375), large=False, heli=True,
                airplanes=True, slot_name='F159', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-399130.1875, -18755.640625), large=False, heli=True,
                airplanes=True, slot_name='F158', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-399073.71875, -18716.119140625), large=False, heli=True,
                airplanes=True, slot_name='F157', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-399016.21875, -18668.330078125), large=False, heli=True,
                airplanes=True, slot_name='F156', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-398958.28125, -18614.935546875), large=False, heli=True,
                airplanes=True, slot_name='F155', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-398900, -18561.501953125), large=False, heli=True,
                airplanes=True, slot_name='F154', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-398853.46875, -18461.2421875), large=False, heli=False,
                airplanes=True, slot_name='F147', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-398843.03125, -18473.52734375), large=False, heli=False,
                airplanes=True, slot_name='F148', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-398832.875, -18485.669921875), large=False, heli=False,
                airplanes=True, slot_name='F149', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-398822.53125, -18497.85546875), large=False, heli=False,
                airplanes=True, slot_name='F150', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-398805.8125, -18517.787109375), large=False, heli=False,
                airplanes=True, slot_name='F151', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-398793.28125, -18532.5546875), large=False, heli=False,
                airplanes=True, slot_name='F152', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-398780.15625, -18548.28515625), large=False, heli=False,
                airplanes=True, slot_name='F153', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-398801.9375, -18417.126953125), large=False, heli=False,
                airplanes=True, slot_name='F140', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-398791.59375, -18429.427734375), large=False, heli=False,
                airplanes=True, slot_name='F141', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-398781.0625, -18442.248046875), large=False, heli=False,
                airplanes=True, slot_name='F142', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-398770.625, -18454.72265625), large=False, heli=False,
                airplanes=True, slot_name='F143', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-398754.28125, -18474.0078125), large=False, heli=False,
                airplanes=True, slot_name='F144', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-398741.59375, -18489.076171875), large=False, heli=False,
                airplanes=True, slot_name='F145', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-398728.53125, -18504.76953125), large=False, heli=False,
                airplanes=True, slot_name='F146', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-398741.53125, -18366.09765625), large=False, heli=False,
                airplanes=True, slot_name='F133', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-398731, -18378.435546875), large=False, heli=False,
                airplanes=True, slot_name='F134', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-398720.78125, -18390.5), large=False, heli=False,
                airplanes=True, slot_name='F135', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-398709.9375, -18403.255859375), large=False, heli=False,
                airplanes=True, slot_name='F136', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-398693.75, -18422.7265625), large=False, heli=False,
                airplanes=True, slot_name='F137', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-398680.9375, -18437.912109375), large=False, heli=False,
                airplanes=True, slot_name='F138', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-398667.75, -18453.587890625), large=False, heli=False,
                airplanes=True, slot_name='F139', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-398683.4375, -18316.5078125), large=False, heli=False,
                airplanes=True, slot_name='F126', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-398672.6875, -18329.474609375), large=False, heli=False,
                airplanes=True, slot_name='F127', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-398662.25, -18342.001953125), large=False, heli=False,
                airplanes=True, slot_name='F128', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-398651.8125, -18354.1015625), large=False, heli=False,
                airplanes=True, slot_name='F129', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-398635.4375, -18373.701171875), large=False, heli=False,
                airplanes=True, slot_name='F130', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-398622.8125, -18389.06640625), large=False, heli=False,
                airplanes=True, slot_name='F131', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-398609.71875, -18404.734375), large=False, heli=False,
                airplanes=True, slot_name='F132', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-398618.65625, -18262.603515625), large=False, heli=False,
                airplanes=True, slot_name='F119', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-398608.3125, -18275.24609375), large=False, heli=False,
                airplanes=True, slot_name='F120', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-398598.09375, -18287.20703125), large=False, heli=False,
                airplanes=True, slot_name='F121', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-398587.5, -18300.044921875), large=False, heli=False,
                airplanes=True, slot_name='F122', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-398571.25, -18319.50390625), large=False, heli=False,
                airplanes=True, slot_name='F123', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-398558.4375, -18334.962890625), large=False, heli=False,
                airplanes=True, slot_name='F124', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-398545.40625, -18350.48046875), large=False, heli=False,
                airplanes=True, slot_name='F125', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-398566.25, -18218.412109375), large=False, heli=False,
                airplanes=True, slot_name='F112', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-398555.71875, -18230.923828125), large=False, heli=False,
                airplanes=True, slot_name='F113', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-398545.78125, -18243.076171875), large=False, heli=False,
                airplanes=True, slot_name='F114', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-398534.8125, -18255.908203125), large=False, heli=False,
                airplanes=True, slot_name='F115', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-398518.6875, -18275.21875), large=False, heli=False,
                airplanes=True, slot_name='F116', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-398505.90625, -18290.611328125), large=False, heli=False,
                airplanes=True, slot_name='F117', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-398492.75, -18306.1328125), large=False, heli=False,
                airplanes=True, slot_name='F118', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-398512.96875, -18175.263671875), large=False, heli=False,
                airplanes=True, slot_name='F104', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-398502.4375, -18187.634765625), large=False, heli=False,
                airplanes=True, slot_name='F105', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-398491.9375, -18200.2734375), large=False, heli=False,
                airplanes=True, slot_name='F106', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-398481.59375, -18212.677734375), large=False, heli=False,
                airplanes=True, slot_name='F107', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-398471.5, -18224.810546875), large=False, heli=False,
                airplanes=True, slot_name='F108', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-398460.96875, -18237.28515625), large=False, heli=False,
                airplanes=True, slot_name='F109', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-398450.875, -18249.431640625), large=False, heli=False,
                airplanes=True, slot_name='F110', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-398440.375, -18262.123046875), large=False, heli=False,
                airplanes=True, slot_name='F111', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-398458.96875, -18140.611328125), large=False, heli=False,
                airplanes=True, slot_name='F98', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-398447.84375, -18154.552734375), large=False, heli=False,
                airplanes=True, slot_name='F99', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-398437.21875, -18168.05859375), large=False, heli=False,
                airplanes=True, slot_name='F100', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-398394.46875, -18219.5), large=False, heli=False,
                airplanes=True, slot_name='F103', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-398409.375, -18201.705078125), large=False, heli=False,
                airplanes=True, slot_name='F102', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-398415.34375, -18105.625), large=False, heli=False,
                airplanes=True, slot_name='F92', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-398404.75, -18118.541015625), large=False, heli=False,
                airplanes=True, slot_name='F93', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-398393.875, -18131.4609375), large=False, heli=False,
                airplanes=True, slot_name='F94', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-398366.3125, -18164.302734375), large=False, heli=False,
                airplanes=True, slot_name='F96', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-398350.96875, -18182.9140625), large=False, heli=False,
                airplanes=True, slot_name='F97', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-398365.96875, -18063.005859375), large=False, heli=False,
                airplanes=True, slot_name='F86', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-398354.875, -18076.26171875), large=False, heli=False,
                airplanes=True, slot_name='F87', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-398343.9375, -18089.767578125), large=False, heli=False,
                airplanes=True, slot_name='F88', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-398319.34375, -18124.572265625), large=False, heli=False,
                airplanes=True, slot_name='F90', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-398303.78125, -18143.228515625), large=False, heli=False,
                airplanes=True, slot_name='F91', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-398274.9375, -18027.333984375), large=False, heli=True,
                airplanes=True, slot_name='F85', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-398226.78125, -17986.38671875), large=False, heli=True,
                airplanes=True, slot_name='F84', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-398200.25, -17963.787109375), large=False, heli=False,
                airplanes=True, slot_name='F83', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-398162.75, -17932.62890625), large=False, heli=True,
                airplanes=True, slot_name='F82', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-398128.125, -17903.56640625), large=False, heli=True,
                airplanes=True, slot_name='F81', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-398083.71875, -17865.68359375), large=False, heli=True,
                airplanes=True, slot_name='F80', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-398032.875, -17823.26953125), large=False, heli=True,
                airplanes=True, slot_name='F79', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-397982.25, -17780.150390625), large=False, heli=True,
                airplanes=True, slot_name='F78', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-397918.875, -17689.5703125), large=False, heli=False,
                airplanes=True, slot_name='F72', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-397907.5625, -17703.119140625), large=False, heli=False,
                airplanes=True, slot_name='F73', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-397896.9375, -17715.75390625), large=False, heli=False,
                airplanes=True, slot_name='F74', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-397880.28125, -17735.869140625), large=False, heli=False,
                airplanes=True, slot_name='F75', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-397867.15625, -17751.037109375), large=False, heli=False,
                airplanes=True, slot_name='F76', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-397855.34375, -17765.38671875), large=False, heli=False,
                airplanes=True, slot_name='F77', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-397801.96875, -17720.576171875), large=False, heli=False,
                airplanes=True, slot_name='F71', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-397815.1875, -17704.84375), large=False, heli=False,
                airplanes=True, slot_name='F70', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-397827.375, -17690.3984375), large=False, heli=False,
                airplanes=True, slot_name='F68', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-397843.65625, -17670.828125), large=False, heli=False,
                airplanes=True, slot_name='F67', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-397854.125, -17658.095703125), large=False, heli=False,
                airplanes=True, slot_name='F66', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-397865.28125, -17644.509765625), large=False, heli=False,
                airplanes=True, slot_name='F65', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-397811.42141685, -17599.092691463), large=False, heli=False,
                airplanes=True, slot_name='F59', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-397800.40625, -17613.208984375), large=False, heli=False,
                airplanes=True, slot_name='F60', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-397788.46875, -17626.9296875), large=False, heli=False,
                airplanes=True, slot_name='F61', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-397772.40625, -17645.55078125), large=False, heli=False,
                airplanes=True, slot_name='F62', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-397759.6875, -17660.8671875), large=False, heli=False,
                airplanes=True, slot_name='F63', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-397747.53125, -17674.748046875), large=False, heli=False,
                airplanes=True, slot_name='F64', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-397716.34375, -17577.095703125), large=False, heli=True,
                airplanes=True, slot_name='F58', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-397667.28125, -17531.349609375), large=False, heli=True,
                airplanes=True, slot_name='F57', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-397559.28125, -17439.671875), large=False, heli=True,
                airplanes=True, slot_name='F55', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-397615.3125, -17489.3984375), large=False, heli=True,
                airplanes=True, slot_name='F56', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-397510.15625, -17340.060546875), large=False, heli=False,
                airplanes=True, slot_name='F46', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-397493.6875, -17359.908203125), large=False, heli=False,
                airplanes=True, slot_name='F48', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-397477.375, -17378.7265625), large=False, heli=False,
                airplanes=True, slot_name='F50', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-397464.75, -17393.5546875), large=False, heli=False,
                airplanes=True, slot_name='F52', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-397452.03125, -17409.046875), large=False, heli=False,
                airplanes=True, slot_name='F53', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-397440.375, -17422.556640625), large=False, heli=False,
                airplanes=True, slot_name='F54', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-397462, -17299.53515625), large=False, heli=False,
                airplanes=True, slot_name='F37', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-397444.65625, -17318.537109375), large=False, heli=False,
                airplanes=True, slot_name='F39', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-397427.6875, -17336.939453125), large=False, heli=False,
                airplanes=True, slot_name='F41', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-397413.3125, -17351.5546875), large=False, heli=False,
                airplanes=True, slot_name='F43', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-397401.125, -17366.33984375), large=False, heli=False,
                airplanes=True, slot_name='F44', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-397389.8125, -17379.462890625), large=False, heli=False,
                airplanes=True, slot_name='F45', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-397407.21875, -17253.296875), large=False, heli=False,
                airplanes=True, slot_name='F28', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-397390.625, -17273.12109375), large=False, heli=False,
                airplanes=True, slot_name='F30', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-397375.375, -17290.033203125), large=False, heli=False,
                airplanes=True, slot_name='F32', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-397362, -17306.87109375), large=False, heli=False,
                airplanes=True, slot_name='F34', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-397349.03125, -17322.46875), large=False, heli=False,
                airplanes=True, slot_name='F35', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-397337.6875, -17335.587890625), large=False, heli=False,
                airplanes=True, slot_name='F36', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-397334.1875, -17196.00390625), large=False, heli=False,
                airplanes=True, slot_name='F25', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-397353.84375, -17213.466796875), large=False, heli=False,
                airplanes=True, slot_name='F27', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-397279, -17160.373046875), large=False, heli=False,
                airplanes=True, slot_name='F24', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-397278.90625, -17186.26953125), large=False, heli=False,
                airplanes=True, slot_name='F22', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-397278.5, -17212.77734375), large=False, heli=False,
                airplanes=True, slot_name='F20', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-397277.84375, -17238.4921875), large=False, heli=False,
                airplanes=True, slot_name='F18', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-397276.90625, -17269.40234375), large=False, heli=False,
                airplanes=True, slot_name='F15', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-397276.1875, -17305.73046875), large=False, heli=False,
                airplanes=True, slot_name='F13', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-397276.5625, -17287.1953125), large=False, heli=False,
                airplanes=True, slot_name='F14', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-397229.875, -17159.55078125), large=False, heli=False,
                airplanes=True, slot_name='F01', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-397229.46875, -17185.43359375), large=False, heli=False,
                airplanes=True, slot_name='F03', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-397229.40625, -17212.083984375), large=False, heli=False,
                airplanes=True, slot_name='F05', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(-397228.84375, -17237.8125), large=False, heli=False,
                airplanes=True, slot_name='F07', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-397228.53125, -17268.98828125), large=False, heli=False,
                airplanes=True, slot_name='F10', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-397228.1875, -17286.427734375), large=False, heli=False,
                airplanes=True, slot_name='F11', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-397228.03125, -17305.197265625), large=False, heli=False,
                airplanes=True, slot_name='F12', length=22.922363, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-397002.625, -17428.95703125), large=False, heli=True,
                airplanes=True, slot_name='11', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-397004.78125, -17372.9375), large=False, heli=True,
                airplanes=True, slot_name='10', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-396877.375, -17320.220703125), large=False, heli=True,
                airplanes=True, slot_name='07', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-396876.71875, -17366.47265625), large=False, heli=True,
                airplanes=True, slot_name='08', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-396874.6875, -17426.908203125), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-396904.21875, -17205.234375), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-396434.90625, -17126.658203125), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-396433.78125, -17159.294921875), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(-396433.0625, -17196.578125), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(-396347.34375, -17127.369140625), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(-396346.90625, -17159.03125), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(-396346.71875, -17191.53515625), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(-396407.0625, -17269.4296875), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(-396542.75, -17053.296875), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(-396515.4375, -17052.734375), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(-396488.15625, -17052.220703125), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(-396587.6875, -17139.623046875), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(-396541.40625, -17138.61328125), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(-396495.21875, -17137.720703125), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(-397010.15625, -16819.60546875), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(-397007.625, -16843.59375), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(-397005.15625, -16866.923828125), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(-396810.375, -16814.14453125), large=False, heli=False,
                airplanes=True, slot_name='E06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(-396805.96875, -16836.791015625), large=False, heli=False,
                airplanes=True, slot_name='E05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(-396805.1875, -16863.359375), large=False, heli=False,
                airplanes=True, slot_name='E04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(-396804.1875, -16888.568359375), large=False, heli=False,
                airplanes=True, slot_name='E03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(-396802.25, -16913.80859375), large=False, heli=False,
                airplanes=True, slot_name='E02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(-396802.40625, -16939.462890625), large=False, heli=False,
                airplanes=True, slot_name='E01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(-397132.9375, -16205.690429688), large=False, heli=False,
                airplanes=True, slot_name='E07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(-397146.53125, -16189.5859375), large=False, heli=False,
                airplanes=True, slot_name='E08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(-397160.25, -16173.016601563), large=False, heli=False,
                airplanes=True, slot_name='E09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(-397173.9375, -16156.876953125), large=False, heli=False,
                airplanes=True, slot_name='E10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(-397187.75, -16140.875), large=False, heli=False,
                airplanes=True, slot_name='E11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(-396939.1875, -15793.793945313), large=False, heli=True,
                airplanes=True, slot_name='E13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(-397428.4375, -16102.076171875), large=False, heli=True,
                airplanes=True, slot_name='G38', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(-397392.71875, -16146.020507813), large=False, heli=True,
                airplanes=True, slot_name='G39', length=39.827835, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(-397538.1875, -16194.704101563), large=False, heli=True,
                airplanes=True, slot_name='G36', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(-397501.71875, -16237.975585938), large=False, heli=True,
                airplanes=True, slot_name='G37', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=187, position=mapping.Point(-397707.75, -16375.091796875), large=False, heli=True,
                airplanes=True, slot_name='G35', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=188, position=mapping.Point(-397601.46875, -16317.440429688), large=False, heli=True,
                airplanes=True, slot_name='G34', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=189, position=mapping.Point(-397639.15625, -16350.895507813), large=False, heli=True,
                airplanes=True, slot_name='G33', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=190, position=mapping.Point(-397758.65625, -16418.9609375), large=False, heli=True,
                airplanes=True, slot_name='G32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=191, position=mapping.Point(-397796.25, -16451.12890625), large=False, heli=False,
                airplanes=True, slot_name='G31', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=192, position=mapping.Point(-397833.71875, -16483.876953125), large=False, heli=True,
                airplanes=True, slot_name='G30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=193, position=mapping.Point(-397871.1875, -16515.486328125), large=False, heli=False,
                airplanes=True, slot_name='G29', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=194, position=mapping.Point(-398494.02017026, -16288.001990565), large=False, heli=False,
                airplanes=True, slot_name='C12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=195, position=mapping.Point(-398518.20718608, -16331.263962037), large=False, heli=False,
                airplanes=True, slot_name='C11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=196, position=mapping.Point(-398541.9982293, -16374.340412734), large=False, heli=False,
                airplanes=True, slot_name='C10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=197, position=mapping.Point(-398566.28760781, -16418.142836288), large=False, heli=False,
                airplanes=True, slot_name='C09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=198, position=mapping.Point(-398590.51859035, -16460.125371273), large=False, heli=False,
                airplanes=True, slot_name='C08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=199, position=mapping.Point(-398614.27883819, -16502.418372804), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=200, position=mapping.Point(-398900.16711083, -16287.246047106), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=201, position=mapping.Point(-398875.05353195, -16330.576252544), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=202, position=mapping.Point(-398850.2408698, -16372.370055509), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=203, position=mapping.Point(-398825.06803034, -16414.82240857), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=204, position=mapping.Point(-398799.877116, -16457.836131296), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=205, position=mapping.Point(-398775.20668444, -16498.818654669), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=206, position=mapping.Point(-398865.625, -17143.28515625), large=False, heli=True,
                airplanes=True, slot_name='G28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=207, position=mapping.Point(-398913.71875, -17187.099609375), large=False, heli=True,
                airplanes=True, slot_name='G27', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=208, position=mapping.Point(-398964.1875, -17228.3359375), large=False, heli=True,
                airplanes=True, slot_name='G26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=209, position=mapping.Point(-399055.21875, -17318.3359375), large=False, heli=False,
                airplanes=True, slot_name='G25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=210, position=mapping.Point(-399080, -17339.37109375), large=False, heli=False,
                airplanes=True, slot_name='G24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=211, position=mapping.Point(-399104.9375, -17359.998046875), large=False, heli=False,
                airplanes=True, slot_name='G23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=212, position=mapping.Point(-399129.5, -17380.666015625), large=False, heli=False,
                airplanes=True, slot_name='G22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=213, position=mapping.Point(-399154.28125, -17401.962890625), large=False, heli=False,
                airplanes=True, slot_name='G21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=214, position=mapping.Point(-399179.375, -17422.201171875), large=False, heli=False,
                airplanes=True, slot_name='G20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=215, position=mapping.Point(-399203.84375, -17443.55859375), large=False, heli=False,
                airplanes=True, slot_name='G19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=216, position=mapping.Point(-399228.40625, -17463.712890625), large=False, heli=False,
                airplanes=True, slot_name='G18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=217, position=mapping.Point(-399253.03125, -17484.89453125), large=False, heli=False,
                airplanes=True, slot_name='G17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=218, position=mapping.Point(-399277.84375, -17505.71484375), large=False, heli=False,
                airplanes=True, slot_name='G16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=219, position=mapping.Point(-399302.46875, -17526.42578125), large=False, heli=False,
                airplanes=True, slot_name='G15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=220, position=mapping.Point(-399327.28125, -17547.18359375), large=False, heli=False,
                airplanes=True, slot_name='G14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=221, position=mapping.Point(-399352.375, -17568.51953125), large=False, heli=False,
                airplanes=True, slot_name='G13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=222, position=mapping.Point(-399376.03125, -17588.59765625), large=False, heli=False,
                airplanes=True, slot_name='G12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=223, position=mapping.Point(-399399.875, -17608.30078125), large=False, heli=False,
                airplanes=True, slot_name='G11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=224, position=mapping.Point(-399422.9375, -17627.716796875), large=False, heli=False,
                airplanes=True, slot_name='G10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=225, position=mapping.Point(-399446.1875, -17647.3203125), large=False, heli=False,
                airplanes=True, slot_name='G09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=226, position=mapping.Point(-399469.25, -17666.794921875), large=False, heli=False,
                airplanes=True, slot_name='G08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=227, position=mapping.Point(-399493, -17686.3359375), large=False, heli=False,
                airplanes=True, slot_name='G07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=228, position=mapping.Point(-399516.0625, -17706.298828125), large=False, heli=False,
                airplanes=True, slot_name='G06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=229, position=mapping.Point(-399539.46875, -17726.119140625), large=False, heli=False,
                airplanes=True, slot_name='G05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=230, position=mapping.Point(-399562.875, -17745.650390625), large=False, heli=False,
                airplanes=True, slot_name='G04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=231, position=mapping.Point(-399585.90625, -17765.37109375), large=False, heli=False,
                airplanes=True, slot_name='G03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=232, position=mapping.Point(-399609.21875, -17784.76953125), large=False, heli=False,
                airplanes=True, slot_name='G02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=233, position=mapping.Point(-399632.90625, -17804.19921875), large=False, heli=False,
                airplanes=True, slot_name='G01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=234, position=mapping.Point(-399250.125, -18395.14453125), large=False, heli=False,
                airplanes=True, slot_name='A01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=235, position=mapping.Point(-399263.46875, -18373.666015625), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=236, position=mapping.Point(-399279.5625, -18352.32421875), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=237, position=mapping.Point(-399297.375, -18331.2578125), large=False, heli=False,
                airplanes=True, slot_name='A04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=238, position=mapping.Point(-399589.0625, -18011.1953125), large=False, heli=False,
                airplanes=True, slot_name='A13', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=239, position=mapping.Point(-399575.1875, -18027.861328125), large=False, heli=False,
                airplanes=True, slot_name='A12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=240, position=mapping.Point(-399561.96875, -18043.88671875), large=False, heli=False,
                airplanes=True, slot_name='A11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=241, position=mapping.Point(-399548.3125, -18060.47265625), large=False, heli=False,
                airplanes=True, slot_name='A10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=242, position=mapping.Point(-399534.15625, -18076.705078125), large=False, heli=False,
                airplanes=True, slot_name='A09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=243, position=mapping.Point(-399519.9375, -18092.3984375), large=False, heli=False,
                airplanes=True, slot_name='A08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=244, position=mapping.Point(-399506.34375, -18108.94140625), large=False, heli=False,
                airplanes=True, slot_name='A07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=245, position=mapping.Point(-399493.375, -18125.486328125), large=False, heli=False,
                airplanes=True, slot_name='A06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=246, position=mapping.Point(-399479.5625, -18142.439453125), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.727446, width=18.0, height=6.0, shelter=False))


class Beatty_Airport(Airport):
    id = 5
    name = "Beatty Airport"
    position = mapping.Point(-330553.625, -174958.53125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Beatty_Airport, self).__init__()

        self.runways.append(Runway(160))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-329737.78125, -174776.515625), large=False, heli=True,
                airplanes=True, slot_name='01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-329765.3125, -174776.484375), large=False, heli=True,
                airplanes=True, slot_name='02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-329812.75, -174776.625), large=False, heli=True,
                airplanes=True, slot_name='03', length=30.5, width=20.5, height=6.0, shelter=False))


class Boulder_City_Airport(Airport):
    id = 6
    name = "Boulder City Airport"
    position = mapping.Point(-429660.09375, -1148.724518)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Boulder_City_Airport, self).__init__()

        self.runways.append(Runway(330))
        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-429671, -475.66937255859), large=False, heli=True,
                airplanes=True, slot_name='B03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-429641.46941251, -521.85439625786), large=False, heli=True,
                airplanes=True, slot_name='B02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-429587.875, -367.20352172852), large=False, heli=False,
                airplanes=True, slot_name='D08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-429584.78125, -389.08340454102), large=False, heli=False,
                airplanes=True, slot_name='D07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-429581.6875, -410.40881347656), large=False, heli=False,
                airplanes=True, slot_name='D06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-429578.0625, -431.21661376953), large=False, heli=False,
                airplanes=True, slot_name='D05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-429575.03125, -451.87316894531), large=False, heli=False,
                airplanes=True, slot_name='D04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-429571.875, -472.59674072266), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-429568.65625, -493.09997558594), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-429565.34375, -514.28686523438), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-429753.4375, -360.10110473633), large=False, heli=True,
                airplanes=True, slot_name='B06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-429741.6875, -409.41787719727), large=False, heli=True,
                airplanes=True, slot_name='B05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-429734.90625, -453.82467651367), large=False, heli=True,
                airplanes=True, slot_name='B04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-429757.5625, -387.72048950195), large=False, heli=True,
                airplanes=True, slot_name='B08', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-429751.90625, -433.58285522461), large=False, heli=True,
                airplanes=True, slot_name='B07', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-429726.21875, -518.19439697266), large=False, heli=False,
                airplanes=True, slot_name='B01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-429631.8125, -835.08251953125), large=False, heli=True,
                airplanes=True, slot_name='C01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-429676.75, -816.31884765625), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-429702.65625, -819.10211181641), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-429665.625, -956.45343017578), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-429682, -886.85943603516), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-429653.53125, -703.56359863281), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-429650.65625, -764.11791992188), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-429722, -629.05236816406), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-429727.84375, -594.33264160156), large=False, heli=True,
                airplanes=False, slot_name='H09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-429734.25, -556.65533447266), large=False, heli=True,
                airplanes=False, slot_name='H10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-429656.83592013, -650.40435801079), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-429709.53125, -716.01586914063), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-429704.125, -746.65289306641), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-429699.15625, -776.27526855469), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-429630.34769967, -645.73404377412), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-429643.875, -1040.2800292969), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-429644.09375, -990.54827880859), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-429549.40625, -1073.4930419922), large=False, heli=True,
                airplanes=True, slot_name='A01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-429549.09375, -1024.9760742188), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-429671, -923.56829833984), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-429655.5, -732.88134765625), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.727446, width=18.0, height=6.0, shelter=False))


class Echo_Bay(Airport):
    id = 7
    name = "Echo Bay"
    position = mapping.Point(-388592.34375, 33697.310547)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Echo_Bay, self).__init__()

        self.runways.append(Runway(60))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-388552.3125, 33604.30078125), large=False, heli=True,
                airplanes=True, slot_name='H02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-388566.15625, 33543.640625), large=False, heli=True,
                airplanes=True, slot_name='H01', length=16.0, width=16.0, height=6.0, shelter=False))


class Henderson_Executive_Airport(Airport):
    id = 8
    name = "Henderson Executive Airport"
    position = mapping.Point(-427352.71875, -25668.716797)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Henderson_Executive_Airport, self).__init__()

        self.runways.append(Runway(350))
        self.runways.append(Runway(350))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-428026.78125, -26065.75), large=False, heli=True,
                airplanes=True, slot_name='H02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-427979.9375, -26078.1484375), large=False, heli=True,
                airplanes=True, slot_name='H01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-427554.625, -26066.544921875), large=False, heli=True,
                airplanes=True, slot_name='B12', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-427554.65625, -26089.80078125), large=False, heli=True,
                airplanes=True, slot_name='B11', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-427555.0625, -26114.921875), large=False, heli=True,
                airplanes=True, slot_name='B10', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-427407.125, -26140.626953125), large=False, heli=True,
                airplanes=True, slot_name='B05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-427407.1875, -26116.669921875), large=False, heli=True,
                airplanes=True, slot_name='B06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-427405.75, -26079.99609375), large=False, heli=True,
                airplanes=True, slot_name='B07', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-427405.71875, -26056.078125), large=False, heli=True,
                airplanes=True, slot_name='B08', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-427339.3125, -26086.208984375), large=False, heli=False,
                airplanes=True, slot_name='B03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-427338.96875, -26113.87890625), large=False, heli=False,
                airplanes=True, slot_name='B02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-427339.125, -26058.41015625), large=False, heli=False,
                airplanes=True, slot_name='B04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-427338.5625, -26140.412109375), large=False, heli=False,
                airplanes=True, slot_name='B01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-427214.4375, -26142.978515625), large=False, heli=True,
                airplanes=True, slot_name='A25', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-427214.5625, -26118.896484375), large=False, heli=True,
                airplanes=True, slot_name='A26', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-426943.1875, -26067.935546875), large=False, heli=False,
                airplanes=True, slot_name='A10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-426876, -26068.4765625), large=False, heli=True,
                airplanes=True, slot_name='A06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-426876.125, -26092.037109375), large=False, heli=True,
                airplanes=True, slot_name='A05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-426821.4375, -26071.060546875), large=False, heli=True,
                airplanes=True, slot_name='A02', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-426821.625, -26129.708984375), large=False, heli=True,
                airplanes=True, slot_name='A01', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-427212.03125, -26082.5), large=False, heli=True,
                airplanes=True, slot_name='A27', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-427212, -26058.517578125), large=False, heli=True,
                airplanes=True, slot_name='A28', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-427554.75, -26144.6484375), large=False, heli=True,
                airplanes=True, slot_name='B09', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-426876.1875, -26140.025390625), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-426875.96875, -26116.658203125), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-426943.75, -26139.68359375), large=False, heli=False,
                airplanes=True, slot_name='A07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-426943.8125, -26115.65234375), large=False, heli=False,
                airplanes=True, slot_name='A08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-426943.9375, -26092.0234375), large=False, heli=False,
                airplanes=True, slot_name='A09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-426993.90625, -26138.951171875), large=False, heli=False,
                airplanes=True, slot_name='A11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-426993.59375, -26116.001953125), large=False, heli=False,
                airplanes=True, slot_name='A12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-426993.75, -26092.720703125), large=False, heli=False,
                airplanes=True, slot_name='A13', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-426994, -26068.947265625), large=False, heli=False,
                airplanes=True, slot_name='A14', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-427052.0625, -26136.19921875), large=False, heli=True,
                airplanes=True, slot_name='A16', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-427126.65625, -26145.291015625), large=False, heli=True,
                airplanes=True, slot_name='A17', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-427126.4375, -26119.8984375), large=False, heli=True,
                airplanes=True, slot_name='A18', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-427126.875, -26093.212890625), large=False, heli=True,
                airplanes=True, slot_name='A19', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-427126.34375, -26059.703125), large=False, heli=True,
                airplanes=True, slot_name='A20', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-427155.90625, -26144.94921875), large=False, heli=False,
                airplanes=True, slot_name='A21', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-427155.15625, -26119.26953125), large=False, heli=False,
                airplanes=True, slot_name='A22', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-427155.09375, -26083.5), large=False, heli=False,
                airplanes=True, slot_name='A23', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-427155.5625, -26059.17578125), large=False, heli=False,
                airplanes=True, slot_name='A24', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-427277, -26060.08984375), large=False, heli=False,
                airplanes=True, slot_name='A29', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-427054.84375, -26064.26953125), large=False, heli=True,
                airplanes=True, slot_name='A15', length=39.857483, width=40.0, height=18.0, shelter=False))


class Jean_Airport(Airport):
    id = 9
    name = "Jean Airport"
    position = mapping.Point(-450392.859375, -43000.460938)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Jean_Airport, self).__init__()

        self.runways.append(Runway(200))
        self.runways.append(Runway(200))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-450104.78125, -42994.28515625), large=False, heli=True,
                airplanes=True, slot_name='A01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-450083.875, -42980.6875), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-450062.40625, -42967.71875), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-450039.75, -42953.65625), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))


class Laughlin_Airport(Airport):
    id = 10
    name = "Laughlin Airport"
    position = mapping.Point(-516946.421875, 28306.30957)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Laughlin_Airport, self).__init__()

        self.runways.append(Runway(160))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-516446.90625, 28580.93359375), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-516483.625, 28584.234375), large=False, heli=True,
                airplanes=True, slot_name='A03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-516520.3125, 28587.455078125), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-516557.25, 28590.7109375), large=False, heli=True,
                airplanes=True, slot_name='A05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-516807.34375, 28610.177734375), large=False, heli=True,
                airplanes=True, slot_name='C02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-516843.625, 28614.28125), large=False, heli=True,
                airplanes=True, slot_name='C03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-516881.03125, 28616.73046875), large=False, heli=True,
                airplanes=True, slot_name='C04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-516916.59375, 28621.19921875), large=False, heli=True,
                airplanes=True, slot_name='C05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-516770.625, 28607.046875), large=False, heli=True,
                airplanes=True, slot_name='C01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-516616.71875, 28600.787109375), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-516647.1875, 28603.6953125), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-516674.90625, 28606.09375), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-515958.03125, 28557.603515625), large=False, heli=True,
                airplanes=True, slot_name='G01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-516032.9375, 28569.548828125), large=False, heli=True,
                airplanes=True, slot_name='G02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-516413.78125, 28461.2890625), large=False, heli=True,
                airplanes=True, slot_name='A01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-516701.28125, 28608.578125), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))


class Lincoln_County(Airport):
    id = 11
    name = "Lincoln County"
    position = mapping.Point(-224670.351563, 33199.935547)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lincoln_County, self).__init__()

        self.runways.append(Runway(170))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-224143.265625, 33338.26953125), large=False, heli=True,
                airplanes=True, slot_name='02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-224167.59375, 33337.65625), large=False, heli=True,
                airplanes=True, slot_name='03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-224191.8125, 33337.16015625), large=False, heli=True,
                airplanes=True, slot_name='04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-224216.578125, 33337.0703125), large=False, heli=True,
                airplanes=True, slot_name='05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-224240.3125, 33337.046875), large=False, heli=True,
                airplanes=True, slot_name='06', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-224091.5, 33328.6328125), large=False, heli=True,
                airplanes=True, slot_name='01', length=30.5, width=20.5, height=6.0, shelter=False))


class Mesquite(Airport):
    id = 13
    name = "Mesquite"
    position = mapping.Point(-329622.09375, 68561.148438)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Mesquite, self).__init__()

        self.runways.append(Runway(10))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-329683.28125, 68345.796875), large=False, heli=False,
                airplanes=True, slot_name='A10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-329665.15625, 68355.09375), large=False, heli=False,
                airplanes=True, slot_name='A09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-329364.5, 68547.8203125), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-329569.78125, 68409.25), large=False, heli=False,
                airplanes=True, slot_name='A08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-329708.84375, 68396.125), large=False, heli=False,
                airplanes=True, slot_name='A01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-329690.875, 68406.25), large=False, heli=False,
                airplanes=True, slot_name='A02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-329673.125, 68416.078125), large=False, heli=False,
                airplanes=True, slot_name='A03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-329655.21875, 68425.796875), large=False, heli=False,
                airplanes=True, slot_name='A04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-329630.625, 68437.484375), large=False, heli=False,
                airplanes=True, slot_name='A05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-329612.1875, 68448.375), large=False, heli=False,
                airplanes=True, slot_name='A06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-329590.25, 68459.6875), large=False, heli=False,
                airplanes=True, slot_name='A07', length=22.727446, width=18.0, height=6.0, shelter=False))


class Mina_Airport_3Q0(Airport):
    id = 14
    name = "Mina Airport 3Q0"
    position = mapping.Point(-161504.46875, -289784.765625)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Mina_Airport_3Q0, self).__init__()

        self.runways.append(Runway(130))


class North_Las_Vegas(Airport):
    id = 15
    name = "North Las Vegas"
    position = mapping.Point(-400891.484375, -31726.952148)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(North_Las_Vegas, self).__init__()

        self.runways.append(Runway(250))
        self.runways.append(Runway(300))
        self.runways.append(Runway(120))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-401630.4375, -32211.359375), large=False, heli=False,
                airplanes=True, slot_name='B17', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-401616.6875, -32228.7421875), large=False, heli=False,
                airplanes=True, slot_name='B16', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-401717.4375, -31595.21875), large=False, heli=True,
                airplanes=True, slot_name='B18', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-401453.5625, -31027.25), large=False, heli=True,
                airplanes=True, slot_name='M01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-401751.5625, -31576.97265625), large=False, heli=True,
                airplanes=True, slot_name='B19', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-401354.4375, -31032.263671875), large=False, heli=True,
                airplanes=True, slot_name='M02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-401489.6875, -30933.9453125), large=False, heli=False,
                airplanes=True, slot_name='W10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-401440.71875, -30933.94140625), large=False, heli=False,
                airplanes=True, slot_name='W09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-401390.96875, -30933.29296875), large=False, heli=False,
                airplanes=True, slot_name='W08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-401352.0625, -30935.35546875), large=False, heli=False,
                airplanes=True, slot_name='W07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-401325.71875, -30933.8828125), large=False, heli=False,
                airplanes=True, slot_name='W06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-401296.5, -30933.76953125), large=False, heli=False,
                airplanes=True, slot_name='W05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-401270.59375, -30985.921875), large=False, heli=False,
                airplanes=True, slot_name='W04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-401270.96875, -31018.4609375), large=False, heli=False,
                airplanes=True, slot_name='W03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-401270.875, -31066.826171875), large=False, heli=False,
                airplanes=True, slot_name='W02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-401277.34375, -31097.29296875), large=False, heli=False,
                airplanes=True, slot_name='W01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-401577.625, -32188.427734375), large=False, heli=False,
                airplanes=True, slot_name='B14', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-401562.65625, -32206.3984375), large=False, heli=False,
                airplanes=True, slot_name='B13', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-401602.6875, -32245.6875), large=False, heli=False,
                airplanes=True, slot_name='B15', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-401334.46875, -32438.099609375), large=False, heli=False,
                airplanes=True, slot_name='R03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-401350.59375, -32458.09765625), large=False, heli=False,
                airplanes=True, slot_name='R02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-401366.125, -32478.998046875), large=False, heli=False,
                airplanes=True, slot_name='R01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-401803.5625, -31493.84375), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-401858.03125, -31452.5390625), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-401822.5625, -31472.845703125), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-401498.875, -32041.6484375), large=False, heli=False,
                airplanes=True, slot_name='B06', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-401498.4375, -32020.84375), large=False, heli=False,
                airplanes=True, slot_name='B07', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-401497.90625, -31999.55859375), large=False, heli=False,
                airplanes=True, slot_name='B08', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-401496.96875, -31978.71875), large=False, heli=False,
                airplanes=True, slot_name='B09', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-401495.875, -31957.3671875), large=False, heli=False,
                airplanes=True, slot_name='B10', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-401495.46875, -31936.4296875), large=False, heli=False,
                airplanes=True, slot_name='B11', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-401495.15625, -31914.193359375), large=False, heli=False,
                airplanes=True, slot_name='B12', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-401433.25, -31965.734375), large=False, heli=False,
                airplanes=True, slot_name='B05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-401434, -31987.259765625), large=False, heli=False,
                airplanes=True, slot_name='B04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-401434.4375, -32007.994140625), large=False, heli=False,
                airplanes=True, slot_name='B03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-401434.71875, -32028.744140625), large=False, heli=False,
                airplanes=True, slot_name='B02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-401435.3125, -32049.84765625), large=False, heli=False,
                airplanes=True, slot_name='B01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-401349.125, -32043.392578125), large=False, heli=True,
                airplanes=True, slot_name='C04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-401371.96875, -32066.841796875), large=False, heli=True,
                airplanes=True, slot_name='C05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-401286.9375, -32101.779296875), large=False, heli=True,
                airplanes=True, slot_name='C01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-401242.15625, -32165.65625), large=False, heli=True,
                airplanes=True, slot_name='C02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-401309.96875, -32122.806640625), large=False, heli=True,
                airplanes=True, slot_name='C03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-401266.5625, -32363.90234375), large=False, heli=False,
                airplanes=True, slot_name='R05', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-401280.53125, -32383.21875), large=False, heli=False,
                airplanes=True, slot_name='R04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-400996.53125, -32766.830078125), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-400997.6875, -32797.9609375), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-400998.5, -32828.859375), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))


class Pahute_Mesa_Airstrip(Airport):
    id = 16
    name = "Pahute Mesa Airstrip"
    position = mapping.Point(-303620, -132937.929688)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Pahute_Mesa_Airstrip, self).__init__()

        self.runways.append(Runway(360))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-303524.92167696, -133026.1164952), large=False, heli=True,
                airplanes=True, slot_name='05', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-303622.72626628, -133052.93433556), large=False, heli=True,
                airplanes=True, slot_name='01', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-303596.62381344, -133045.59117884), large=False, heli=True,
                airplanes=True, slot_name='02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-303572.4616298, -133039.13607596), large=False, heli=True,
                airplanes=True, slot_name='03', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-303548.5625, -133032.90625), large=False, heli=True,
                airplanes=True, slot_name='04', length=30.5, width=20.5, height=6.0, shelter=False))


class Tonopah_Airport(Airport):
    id = 17
    name = "Tonopah Airport"
    position = mapping.Point(-197282.898438, -201302.882813)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tonopah_Airport, self).__init__()

        self.runways.append(Runway(290))
        self.runways.append(Runway(330))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-198277.78125, -202084.4375), large=False, heli=True,
                airplanes=True, slot_name='A01', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-198234.625, -202096.203125), large=False, heli=True,
                airplanes=True, slot_name='A02', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-198191.3125, -202108.109375), large=False, heli=True,
                airplanes=True, slot_name='A03', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-198147.96875, -202119.859375), large=False, heli=True,
                airplanes=True, slot_name='A04', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-198104.5625, -202131.625), large=False, heli=True,
                airplanes=True, slot_name='A05', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-198061.28125, -202143.40625), large=False, heli=True,
                airplanes=True, slot_name='A06', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-198017.90625, -202155.34375), large=False, heli=True,
                airplanes=True, slot_name='A07', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-197974.59375, -202167), large=False, heli=True,
                airplanes=True, slot_name='A08', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-197931.203125, -202178.84375), large=False, heli=True,
                airplanes=True, slot_name='A09', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-197888.296875, -202191.09375), large=False, heli=True,
                airplanes=True, slot_name='A10', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-197844.96875, -202203), large=False, heli=True,
                airplanes=True, slot_name='A11', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-197801.65625, -202214.71875), large=False, heli=True,
                airplanes=True, slot_name='A12', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-197758.28125, -202226.53125), large=False, heli=True,
                airplanes=True, slot_name='A13', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-197714.96875, -202238.265625), large=False, heli=True,
                airplanes=True, slot_name='A14', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-197671.609375, -202250.1875), large=False, heli=True,
                airplanes=True, slot_name='A15', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-197628.296875, -202261.90625), large=False, heli=True,
                airplanes=True, slot_name='A16', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-197584.890625, -202273.671875), large=False, heli=True,
                airplanes=True, slot_name='A17', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-197541.734375, -202285.421875), large=False, heli=True,
                airplanes=True, slot_name='A18', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-197498.34375, -202297.328125), large=False, heli=True,
                airplanes=True, slot_name='A19', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-197455.0625, -202309.078125), large=False, heli=True,
                airplanes=True, slot_name='A20', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-197411.65625, -202320.828125), large=False, heli=True,
                airplanes=True, slot_name='A21', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-197368.34375, -202332.625), large=False, heli=True,
                airplanes=True, slot_name='A22', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-197325.015625, -202344.578125), large=False, heli=True,
                airplanes=True, slot_name='A23', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-197281.703125, -202356.25), large=False, heli=True,
                airplanes=True, slot_name='A24', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-197238.3125, -202368.0625), large=False, heli=True,
                airplanes=True, slot_name='A25', length=39.857483, width=40.0, height=18.0, shelter=False))


class Tonopah_Test_Range_Airfield(Airport):
    id = 18
    name = "Tonopah Test Range Airfield"
    position = mapping.Point(-226505.273438, -174698.484375)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tonopah_Test_Range_Airfield, self).__init__()

        self.runways.append(Runway(320))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-225679.28125, -174488.90625), large=False, heli=True,
                airplanes=True, slot_name='D14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-225566.109375, -174497.4375), large=False, heli=True,
                airplanes=True, slot_name='D13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-225334.95388725, -174677.29806156), large=False, heli=False,
                airplanes=True, slot_name='D01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-225305.27862034, -174607.56103651), large=False, heli=False,
                airplanes=True, slot_name='D02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-225336.69549492, -174594.64793502), large=False, heli=False,
                airplanes=True, slot_name='D04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-225366.11437447, -174663.87932047), large=False, heli=False,
                airplanes=True, slot_name='D03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-225368.05984995, -174581.47129585), large=False, heli=False,
                airplanes=True, slot_name='D06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-225397.43520077, -174650.9141146), large=False, heli=False,
                airplanes=True, slot_name='D05', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-225434.3677049, -174635.32878005), large=False, heli=False,
                airplanes=True, slot_name='D07', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-225404.6040749, -174565.07406801), large=False, heli=False,
                airplanes=True, slot_name='D08', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-225436.13971854, -174552.33086829), large=False, heli=False,
                airplanes=True, slot_name='D10', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-225467.44159797, -174538.94416997), large=False, heli=False,
                airplanes=True, slot_name='D12', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-225465.54811448, -174621.86886115), large=False, heli=False,
                airplanes=True, slot_name='D09', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-225497.0551549, -174608.87690051), large=False, heli=False,
                airplanes=True, slot_name='D11', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-225784.66016626, -174485.6993844), large=False, heli=False,
                airplanes=True, slot_name='D16', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-225756.17207304, -174418.12183539), large=False, heli=False,
                airplanes=True, slot_name='D17', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-225787.37365922, -174405.15371192), large=False, heli=False,
                airplanes=True, slot_name='D19', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-225815.85834898, -174472.03034354), large=False, heli=False,
                airplanes=True, slot_name='D18', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-226023.079914, -174305.06717577), large=False, heli=False,
                airplanes=True, slot_name='D33', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-226051.430065, -174372.145237), large=False, heli=False,
                airplanes=True, slot_name='D32', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-225818.57253879, -174391.47521078), large=False, heli=False,
                airplanes=True, slot_name='D21', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-225847.2409015, -174459.02059161), large=False, heli=False,
                airplanes=True, slot_name='D20', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-225858.328125, -174374.9375), large=False, heli=False,
                airplanes=True, slot_name='D23', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-225888.265625, -174443.359375), large=False, heli=False,
                airplanes=True, slot_name='D22', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-225917.87402489, -174428.56350496), large=False, heli=False,
                airplanes=True, slot_name='D24', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-225889.47406502, -174361.36936492), large=False, heli=False,
                airplanes=True, slot_name='D25', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-225920.92177536, -174348.26105286), large=False, heli=False,
                airplanes=True, slot_name='D27', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-225949.39733376, -174415.98412333), large=False, heli=False,
                airplanes=True, slot_name='D26', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-225960.40173764, -174331.51832843), large=False, heli=False,
                airplanes=True, slot_name='D29', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-225988.76580065, -174398.56491191), large=False, heli=False,
                airplanes=True, slot_name='D28', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-225991.92642722, -174318.48805264), large=False, heli=False,
                airplanes=True, slot_name='D31', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-226020.14143581, -174385.54689891), large=False, heli=False,
                airplanes=True, slot_name='D30', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-226349.08826391, -174167.6341884), large=False, heli=False,
                airplanes=True, slot_name='C02', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-226380.33108749, -174154.16114983), large=False, heli=False,
                airplanes=True, slot_name='C04', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-226411.72351514, -174141.06076098), large=False, heli=False,
                airplanes=True, slot_name='C06', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-226451.26140048, -174124.29973919), large=False, heli=False,
                airplanes=True, slot_name='C08', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-226482.53119996, -174110.99479694), large=False, heli=False,
                airplanes=True, slot_name='C10', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-226513.92184931, -174097.78370771), large=False, heli=False,
                airplanes=True, slot_name='C12', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-226606.10651026, -174057.5304521), large=False, heli=False,
                airplanes=True, slot_name='C14', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-226637.52436533, -174044.59019056), large=False, heli=False,
                airplanes=True, slot_name='C16', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-226376.4150904, -174231.81486009), large=False, heli=False,
                airplanes=True, slot_name='C01', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-226407.58818546, -174218.50625769), large=False, heli=False,
                airplanes=True, slot_name='C03', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-226438.90190801, -174205.27253551), large=False, heli=False,
                airplanes=True, slot_name='C05', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-226478.45647197, -174188.35840596), large=False, heli=False,
                airplanes=True, slot_name='C07', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-226509.6703714, -174175.10336315), large=False, heli=False,
                airplanes=True, slot_name='C09', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-226541.01059472, -174161.75745093), large=False, heli=False,
                airplanes=True, slot_name='C11', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-226633.67607466, -174122.56833442), large=False, heli=False,
                airplanes=True, slot_name='C13', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-226665.11597856, -174109.49366358), large=False, heli=False,
                airplanes=True, slot_name='C15', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-226668.99905254, -174031.51725982), large=False, heli=False,
                airplanes=True, slot_name='C18', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-226708.41810205, -174014.4719288), large=False, heli=False,
                airplanes=True, slot_name='C20', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-226739.67786257, -174001.36779802), large=False, heli=False,
                airplanes=True, slot_name='C22', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-226771.49263453, -173988.0099171), large=False, heli=False,
                airplanes=True, slot_name='C24', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-226696.44328202, -174096.27250661), large=False, heli=False,
                airplanes=True, slot_name='C17', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-226736.08705702, -174079.60198763), large=False, heli=False,
                airplanes=True, slot_name='C19', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-226767.1764298, -174066.22197129), large=False, heli=False,
                airplanes=True, slot_name='C21', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-226798.65727271, -174053.07863275), large=False, heli=False,
                airplanes=True, slot_name='C23', length=22.726997, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-226927.875, -173894.078125), large=False, heli=False,
                airplanes=True, slot_name='F01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-226956.390625, -173881.984375), large=False, heli=False,
                airplanes=True, slot_name='F02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-226984.34375, -173870.203125), large=False, heli=False,
                airplanes=True, slot_name='F03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-227012.8125, -173858.890625), large=False, heli=False,
                airplanes=True, slot_name='F04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-227606.4425991, -173705.90072357), large=False, heli=False,
                airplanes=True, slot_name='G01', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-227633.84375, -173694.46875), large=False, heli=False,
                airplanes=True, slot_name='G02', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-227661.33808507, -173682.64142897), large=False, heli=False,
                airplanes=True, slot_name='G03', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-227688.73477698, -173670.98031801), large=False, heli=False,
                airplanes=True, slot_name='G04', length=22.727446, width=18.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-228133, -173442.140625), large=False, heli=True,
                airplanes=True, slot_name='A04', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-228068.0625, -173471.71875), large=False, heli=True,
                airplanes=True, slot_name='A02', length=30.5, width=20.5, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-228098.96875, -173452.59375), large=False, heli=True,
                airplanes=True, slot_name='A03', length=39.857483, width=40.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-228030.828125, -173478.921875), large=False, heli=True,
                airplanes=True, slot_name='A01', length=39.857483, width=40.0, height=18.0, shelter=False))


class Nevada(Terrain):
    center = {"lat": 39.81806, "long": -114.73333}
    bounds = mapping.Rectangle(-166934.953125, -329334.875000, -497177.656250, 209836.890625)
    map_view_default = MapView(mapping.Point(-340928.57142857, -55928.571428568), 1000000)
    city_graph = Graph.from_pickle(os.path.join(os.path.dirname(__file__), 'nevada.p'))
    temperature = [
        (0, 10),
        (2, 16),
        (6, 22),
        (10, 24),
        (14, 28),
        (19, 35),
        (23, 40),
        (22, 38),
        (18, 33),
        (11, 26),
        (5, 19),
        (1, 13)
    ]
    assert(len(temperature) == 12)

    def __init__(self):
        super(Nevada, self).__init__("Nevada")
        # nttr center MGRS
        # 11SPE9400410022
        self.bullseye_blue = {"x": -409931.344, "y": -14024.097}
        self.bullseye_red = {"x": -288293.969, "y": -88022.641}

        self.airports['Creech AFB'] = Creech_AFB()
        self.airports['Groom Lake AFB'] = Groom_Lake_AFB()
        self.airports['McCarran International Airport'] = McCarran_International_Airport()
        self.airports['Nellis AFB'] = Nellis_AFB()
        self.airports['Beatty Airport'] = Beatty_Airport()
        self.airports['Boulder City Airport'] = Boulder_City_Airport()
        self.airports['Echo Bay'] = Echo_Bay()
        self.airports['Henderson Executive Airport'] = Henderson_Executive_Airport()
        self.airports['Jean Airport'] = Jean_Airport()
        self.airports['Laughlin Airport'] = Laughlin_Airport()
        self.airports['Lincoln County'] = Lincoln_County()
        self.airports['Mesquite'] = Mesquite()
        self.airports['Mina Airport 3Q0'] = Mina_Airport_3Q0()
        self.airports['North Las Vegas'] = North_Las_Vegas()
        self.airports['Pahute Mesa Airstrip'] = Pahute_Mesa_Airstrip()
        self.airports['Tonopah Airport'] = Tonopah_Airport()
        self.airports['Tonopah Test Range Airfield'] = Tonopah_Test_Range_Airfield()

    def creech_afb(self) -> Airport:
        return self.airports["Creech AFB"]

    def groom_lake_afb(self) -> Airport:
        return self.airports["Groom Lake AFB"]

    def mccarran_international_airport(self) -> Airport:
        return self.airports["McCarran International Airport"]

    def nellis_afb(self) -> Airport:
        return self.airports["Nellis AFB"]

    def beatty_airport(self) -> Airport:
        return self.airports["Beatty Airport"]

    def boulder_city_airport(self) -> Airport:
        return self.airports["Boulder City Airport"]

    def echo_bay(self) -> Airport:
        return self.airports["Echo Bay"]

    def henderson_executive_airport(self) -> Airport:
        return self.airports["Henderson Executive Airport"]

    def jean_airport(self) -> Airport:
        return self.airports["Jean Airport"]

    def laughlin_airport(self) -> Airport:
        return self.airports["Laughlin Airport"]

    def lincoln_county(self) -> Airport:
        return self.airports["Lincoln County"]

    def mesquite(self) -> Airport:
        return self.airports["Mesquite"]

    def mina_airport_3q0(self) -> Airport:
        return self.airports["Mina Airport 3Q0"]

    def north_las_vegas(self) -> Airport:
        return self.airports["North Las Vegas"]

    def pahute_mesa_airstrip(self) -> Airport:
        return self.airports["Pahute Mesa Airstrip"]

    def tonopah_airport(self) -> Airport:
        return self.airports["Tonopah Airport"]

    def tonopah_test_range_airfield(self) -> Airport:
        return self.airports["Tonopah Test Range Airfield"]

    def default_red_airports(self) -> List[Airport]:
        return []

    def default_blue_airports(self) -> List[Airport]:
        return list(self.airport_list())
