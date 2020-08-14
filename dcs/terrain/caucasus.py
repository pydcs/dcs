import os
from typing import List

from dcs.terrain.terrain import Terrain, Airport, Runway, ParkingSlot, MapView, Graph
import dcs.mapping as mapping


class Anapa_Vityazevo(Airport):
    id = 12
    name = "Anapa-Vityazevo"
    position = mapping.Point(-5412.409668, 243128.820313)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Anapa_Vityazevo, self).__init__()

        self.runways.append(Runway(220))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-4829.5249882422, 244622.06661236), large=False, heli=True,
                airplanes=True, slot_name='40', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-5155.0776367188, 244536.28125), large=False, heli=False,
                airplanes=True, slot_name='90', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-4696.5478288993, 243274.37815978), large=False, heli=True,
                airplanes=True, slot_name='32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-5305.7182736723, 241653.99465964), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-5388.4541015625, 241652.23378172), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-5551.3579101563, 242507.421875), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-5536.3608398438, 242520.671875), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-5566.2290039063, 242494.109375), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-5581.0903320313, 242480.671875), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-5506.6323242188, 242547.34375), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-5491.6909179688, 242560.734375), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-5476.833984375, 242574.125), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-5521.3090820313, 242533.859375), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-5446.7998046875, 242601.125), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-5431.9287109375, 242614.484375), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-5417.0126953125, 242627.859375), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-5401.8798828125, 242640.953125), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-5387.0405273438, 242654.359375), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-5372.220703125, 242667.828125), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-5357.4453125, 242681.21875), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-5461.9453125, 242587.453125), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-5327.6533203125, 242707.96875), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-5312.7817382813, 242721.296875), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-5297.7846679688, 242734.53125), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-5282.7329101563, 242747.71875), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-5268.0561523438, 242761.203125), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-5253.1147460938, 242774.59375), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-5238.2578125, 242787.984375), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-5342.5141601563, 242694.53125), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-4741.4052507743, 243234.59690978), large=False, heli=True,
                airplanes=True, slot_name='31', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-4830.7929460868, 243154.56565978), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-4785.9355242118, 243194.33128478), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-4922.2558367118, 243073.53440978), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-4875.5019304618, 243114.48753478), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-4967.1420671805, 243033.73753478), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-5011.9448015555, 242993.84690978), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-4790.3916874609, 244576.50411236), large=False, heli=True,
                airplanes=True, slot_name='39', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-4751.6978398047, 244530.70723736), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-4712.8706913672, 244485.00411236), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-4674.0435429297, 244439.22286236), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-4635.1949101172, 244393.51973736), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-4596.4380741797, 244347.69161236), large=False, heli=True,
                airplanes=True, slot_name='34', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-4557.5967655859, 244301.94161236), large=False, heli=True,
                airplanes=True, slot_name='33', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-5436.5092773438, 241690.79034808), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-5413.4798547706, 241545.64098758), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-5319.2125073418, 241730.30735768), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-5450.540836361, 241767.296875), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-5496.1748046875, 241543.984375), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-5518.6357421875, 241688.34302483), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-5482.233249469, 241466.25205966), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-5783.3602568085, 241659.6704904), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-5714.2987024269, 241738.58950855), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-5736.34765625, 241883.515625), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-5845.3850444094, 241776.54227097), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-5913.7447381715, 241698.10297997), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-5796.9307114395, 241737.20239983), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-5927.2530718185, 241774.6576346), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-5819.0512695313, 241880.71875), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-5751.3354492188, 241960.765625), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-5875.41796875, 242068.25), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-5742.6792411181, 242093.13989983), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-5828.84375, 242005.625), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-5695.7739257813, 242030.703125), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-5802.478515625, 242106.84375), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-5669.6904296875, 242131.43713742), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-5136.349609375, 244639.625), large=False, heli=False,
                airplanes=True, slot_name='92', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-5206.4555664063, 244595.46875), large=False, heli=False,
                airplanes=True, slot_name='91', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-5116.3564453125, 244752.328125), large=False, heli=False,
                airplanes=True, slot_name='83', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-5045.9018554688, 244796.109375), large=False, heli=False,
                airplanes=True, slot_name='82', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-5098.1450195313, 244854.828125), large=False, heli=False,
                airplanes=True, slot_name='81', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-4926.8896484375, 244382.046875), large=False, heli=False,
                airplanes=True, slot_name='69', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-4891.9521484375, 244234.578125), large=False, heli=False,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-4792.0336914063, 244326.671875), large=False, heli=False,
                airplanes=True, slot_name='73', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-4858.4965820313, 244134.140625), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-4758.4594726563, 244227.4375), large=False, heli=False,
                airplanes=True, slot_name='71', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-4833.2495117188, 244254.3125), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-4932.529296875, 244162.890625), large=False, heli=False,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-4968.3100585938, 244309.828125), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-4999.859375, 244409.109375), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-4719.0668945313, 244710.125), large=False, heli=False,
                airplanes=True, slot_name='74', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-4751.1293945313, 244810.375), large=False, heli=False,
                airplanes=True, slot_name='75', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-4806.8271484375, 244941.375), large=False, heli=False,
                airplanes=True, slot_name='77', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-4931.6782226563, 244826.203125), large=False, heli=False,
                airplanes=True, slot_name='80', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-4847.0278320313, 244870.671875), large=False, heli=False,
                airplanes=True, slot_name='78', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-4880.447265625, 244968.734375), large=False, heli=False,
                airplanes=True, slot_name='76', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-5004.98046875, 244854.046875), large=False, heli=False,
                airplanes=True, slot_name='79', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-5211.3549804688, 244762.734375), large=False, heli=False,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-5273.0068359375, 244631.796875), large=False, heli=False,
                airplanes=True, slot_name='89', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-5239.4360351563, 244835.453125), large=False, heli=False,
                airplanes=True, slot_name='84', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-5292.3120117188, 244747.203125), large=False, heli=False,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-5354.6943833145, 244615.9928798), large=False, heli=False,
                airplanes=True, slot_name='88', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-5326.7529197075, 244542.60565741), large=False, heli=False,
                airplanes=True, slot_name='87', length=26.0, width=22.0, height=8.0, shelter=False))


class Krasnodar_Center(Airport):
    id = 13
    name = "Krasnodar-Center"
    position = mapping.Point(11685.205078, 367933.515625)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Krasnodar_Center, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(10890.094726563, 368483.28125), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(10816.975585938, 368480.78125), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(10828.625, 368562.46875), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(10964.021484375, 368612.8125), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(10890.548828125, 368610.5), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(10902.284179688, 368691.96875), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(11036.436523438, 368740.28125), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(10963.412109375, 368737.71875), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(10974.916015625, 368819.40625), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(11107.930664063, 368865.5), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(11034.784179688, 368863.125), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(11046.223632813, 368944.84375), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(11178.272460938, 368989), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(11105.057617188, 368986.625), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(11116.887695313, 369068.1875), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(11250.354492188, 369040.15625), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(11214.475585938, 369104.75), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(11293.036132813, 369131.375), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(11285.462890625, 369308.6875), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(11333.448242188, 369240.78125), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(11348.0546875, 369339.34375), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(11435.4140625, 369297.28125), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(11509.239257813, 369260.40625), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(11476.19921875, 369354.34375), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(11558.979492188, 369291.34375), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(11634.052734375, 369254.15625), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(11599.92578125, 369348.375), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(11687.473632813, 369546.84375), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(11613.020507813, 369584.90625), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(11646.333007813, 369490.375), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(11533.930664063, 369554.75), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(11459.388671875, 369592.84375), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(11492.416015625, 369498.5), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(11221.29895066, 367130), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(11223.147583472, 367149.875), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(11224.277466285, 367169.96875), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(11225.272583472, 367189.875), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(11226.208130347, 367209.8125), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(11227.437622535, 367229.78125), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(11228.38879441, 367249.78125), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(11229.686645972, 367269.71875), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(11230.66223191, 367289.65625), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(11231.44738816, 367309.65625), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(11232.25988816, 367329.625), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(11233.032349097, 367349.65625), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(11234.26770066, 367369.59375), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(11235.262817847, 367389.59375), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(11236.44348191, 367409.5625), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(11237.496216285, 367429.5), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(11238.256958472, 367449.53125), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(11266.885152755, 368273.59222408), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(11270.491598068, 368333.74847408), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(11273.925191818, 368393.71722408), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(11276.546285568, 368453.59222408), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(11279.530660568, 368513.59222408), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(11282.865621505, 368573.43597408), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Novorossiysk(Airport):
    id = 14
    name = "Novorossiysk"
    position = mapping.Point(-40917.535156, 279256.0625)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Novorossiysk, self).__init__()

        self.runways.append(Runway(220))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-40106.0234375, 279575.75), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-40104.6796875, 279615.6875), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-40103.375, 279655.71875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-40102.11328125, 279695.65625), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-40105.41796875, 279595.6875), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-40104.03515625, 279635.6875), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-40102.78515625, 279675.65625), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-40101.39453125, 279715.59375), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-41416.58984375, 278570.15625), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-41318.96484375, 278640), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-41219.26171875, 278710.53125), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-41121.76171875, 278780.46875), large=False, heli=True,
                airplanes=True, slot_name='07', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-41072.97265625, 278815.34375), large=False, heli=True,
                airplanes=True, slot_name='08', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-41170.57421875, 278745.5), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-41268.16796875, 278675.78125), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-41367.76171875, 278605.09375), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-40872.625, 278800.34375), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-40950.88671875, 278911.46875), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-40587.84375, 279004.53125), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-40665.9453125, 279115.75), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-40619.13671875, 278841.59375), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-40769.328125, 278822.59375), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-40847.50390625, 278933.875), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-40697.3046875, 278952.71875), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-40562.71875, 279138.03125), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-40484.59375, 279027), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-40334.1328125, 279045.71875), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-40412.1015625, 279156.53125), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-40686.68359375, 278888.875), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-40836.859375, 278869.875), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-40764.8515625, 278999.96875), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-40552.1796875, 279074.15625), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-40401.765625, 279092.96875), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-40479.5390625, 279203.875), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-40583.38671875, 278911.34375), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-40661.52734375, 279022.34375), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-40298.3671875, 279115.375), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-40376.36328125, 279226.15625), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=8.0, shelter=False))


class Krymsk(Airport):
    id = 15
    name = "Krymsk"
    position = mapping.Point(-6576.524658, 294388.125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Krymsk, self).__init__()

        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-6138.9926757813, 295188.6875), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-6097.5327148438, 295259.875), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-6170.1665039063, 295289.59375), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-6317.9501953125, 295041.53125), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-6276.6088867188, 295112.65625), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-6349.3403320313, 295142.46875), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-6532.59375, 295051.09375), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-6467.80859375, 295101.34375), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-6523.60546875, 295156.1875), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-6698.37890625, 294999.09375), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-6633.3872070313, 295049.28125), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-6689.0551757813, 295104.1875), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-7035.1518554688, 294749.6875), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-6978.9584960938, 294810), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-7042.8793945313, 294855.15625), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-7759.7709960938, 294398.21875), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-7767.87890625, 294477.625), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-7842.916015625, 294460.0625), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-7794.2456054688, 294270.46875), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-7802.0161132813, 294350.375), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-7877.3930664063, 294333.8125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-8101.458984375, 293986.15625), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-8061.2060546875, 294058.125), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-8133.9609375, 294086.8125), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-5757.481319782, 295140.78536236), large=False, heli=True,
                airplanes=True, slot_name='57', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-5798.7357143133, 295184.31661236), large=False, heli=True,
                airplanes=True, slot_name='56', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-5837.6092494695, 295230.06661236), large=False, heli=True,
                airplanes=True, slot_name='55', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-5875.707882282, 295276.44161236), large=False, heli=True,
                airplanes=True, slot_name='54', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-7521.655918735, 293786.75525333), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-7483.4381452975, 293740.47400333), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-7496.21255936, 293755.88025333), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-7508.9005476413, 293771.41150333), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-7534.3282820163, 293802.19275333), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-7546.8487898288, 293817.84900333), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-7559.39224686, 293833.41150333), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-7572.2545515475, 293848.69275333), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-7997.2153320313, 294137), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-7956.2280273438, 293896.25), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-7885.65234375, 293957.59375), large=False, heli=True,
                airplanes=True, slot_name='14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-7789.0859375, 294061.625), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-7730.9223632813, 293991.65625), large=False, heli=True,
                airplanes=True, slot_name='12', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-7876.2900390625, 294240.34375), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-7640.392578125, 294218.375), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-7617.5151367188, 294310.03125), large=False, heli=True,
                airplanes=True, slot_name='31', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-7561.830078125, 294082), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-7488.0541992188, 294142.71875), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-7392.68359375, 294221.28125), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-7310.68359375, 294292.0625), large=False, heli=True,
                airplanes=True, slot_name='32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-7514.4228515625, 294397.1875), large=False, heli=True,
                airplanes=True, slot_name='34', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-7423.8745117188, 294414.96875), large=False, heli=True,
                airplanes=True, slot_name='33', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-7183.6884765625, 294468.15625), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-7052.5170898438, 294497.75), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-7263.6923828125, 294690.0625), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-7178.9565429688, 294729.28125), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-7676.2456054688, 293953.5625), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-7604.6469726563, 293912.65625), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-7705.3676757813, 293880.78125), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=8.0, shelter=False))


class Maykop_Khanskaya(Airport):
    id = 16
    name = "Maykop-Khanskaya"
    position = mapping.Point(-26437.275391, 458048.84375)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Maykop_Khanskaya, self).__init__()

        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-26260.4609375, 459009.125), large=False, heli=True,
                airplanes=True, slot_name='53', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-26161.666015625, 459066.25), large=False, heli=True,
                airplanes=True, slot_name='55', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-26161.541015625, 458825.40625), large=False, heli=True,
                airplanes=True, slot_name='54', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-25956.638671875, 458904.375), large=False, heli=True,
                airplanes=True, slot_name='57', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-25982.900390625, 459108.40625), large=False, heli=True,
                airplanes=True, slot_name='56', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-26820.943359375, 458524.90625), large=False, heli=True,
                airplanes=True, slot_name='24', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-26968.1484375, 458456.71875), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-26732.99609375, 458333.46875), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-26952.458984375, 458206.90625), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-27182.22265625, 458288.0625), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-27294.580078125, 458158.09375), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-27368.205078125, 458046.21875), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-27190.376953125, 457932.21875), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-27121.5078125, 458048.03125), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-27552.341796875, 457640.28125), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-26421.903075371, 458658.14455129), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-26415.012450371, 458676.89455129), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-26407.873778496, 458695.42580129), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-26400.619872246, 458714.05080129), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-26393.481200371, 458732.70705129), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-26386.459715996, 458751.61330129), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-26379.256590996, 458770.26955129), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-26372.237059746, 458788.95705129), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-26365.285887871, 458807.70705129), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-26357.951903496, 458826.36330129), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-26350.744872246, 458844.98830129), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-26343.785887871, 458863.80080129), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-26469.258416733, 458516.897708), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-26487.317010483, 458508.366458), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-26505.412713608, 458500.147708), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-26523.633416733, 458491.960208), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-26541.811151108, 458483.647708), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-26560.068963608, 458475.116458), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-26578.303338608, 458466.835208), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-26596.406854233, 458458.460208), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-26614.508416733, 458449.960208), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-26632.811151108, 458441.803958), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-26651.020135483, 458433.585208), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-26669.170526108, 458425.053958), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-26415.248651108, 458542.085208), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-26433.307244858, 458533.553958), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-26451.402947983, 458525.335208), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-27578.401310777, 457789.92452263), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-27558.769558638, 457793.69475166), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-27539.098576402, 457796.62413136), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-27519.367577471, 457800.04067716), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-27499.430440054, 457802.79212749), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-27479.697487999, 457805.98035266), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-27438.662215658, 457832.07759703), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-27426.876210466, 457848.43486226), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-27416.169179216, 457865.36596723), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-27405.025373132, 457881.92279736), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-27981.550375433, 457441.01886459), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-27959.298422308, 457496.76886459), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-27936.554281683, 457552.30011459), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-27890.812094183, 457663.20636459), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-27914.026937933, 457607.89386459), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Gelendzhik(Airport):
    id = 17
    name = "Gelendzhik"
    position = mapping.Point(-50378.611328, 298406.15625)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Gelendzhik, self).__init__()

        self.runways.append(Runway(10))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-50574.20703125, 298005.59375), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-50558.77734375, 298018.34375), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-50543.48046875, 298031.21875), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-50528.09765625, 298044), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-50512.8359375, 298056.875), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-50497.5, 298069.75), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-50482.16015625, 298082.53125), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-50466.90625, 298095.40625), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-50451.66015625, 298108.4375), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-50435.83203125, 298121.25), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-50104.984375, 298390.25), large=False, heli=True,
                airplanes=True, slot_name='11', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-50059.01171875, 298428.78125), large=False, heli=True,
                airplanes=True, slot_name='12', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-50012.703125, 298466.9375), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Sochi_Adler(Airport):
    id = 18
    name = "Sochi-Adler"
    position = mapping.Point(-164496.46875, 462218.921875)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Sochi_Adler, self).__init__()

        self.runways.append(Runway(60))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-164362.125, 463237.3125), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-164427.8125, 463280), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-164374.0625, 463342.34375), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-164464.296875, 463181.65625), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-164530.078125, 463224.46875), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-164476.078125, 463286.875), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-164564.53125, 463127.21875), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-164630.328125, 463169.90625), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-164576.5, 463232.1875), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-164664.9375, 463072.6875), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-164730.75, 463115.3125), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-164676.828125, 463177.5625), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-164765.984375, 463017.71875), large=False, heli=False,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-164777.875, 463122.84375), large=False, heli=False,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-164998.828125, 460827.84375), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-164989.53125, 460845.5), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-164980.25, 460863.1875), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-164969.421875, 460882.53125), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-164960.125, 460900.25), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-164950.796875, 460917.875), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-164941.484375, 460935.625), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-164932.125, 460953.28125), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-164922.859375, 460971), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-164913.5, 460988.71875), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-164904.203125, 461006.375), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-164894.84375, 461024.09375), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-164885.484375, 461041.75), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-164876.1875, 461059.46875), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-164866.828125, 461077.15625), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-164857.5, 461094.875), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-164848.15625, 461112.53125), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-164838.84375, 461130.21875), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-164512.015625, 461704.5625), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-164483.671875, 461757.5625), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-164455.65625, 461810.34375), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-164398.9375, 461916.71875), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-164342.546875, 462022.6875), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-164267.171875, 462163.78125), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-164238.921875, 462216.71875), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-164182.15625, 462322.875), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-164125.859375, 462428.84375), large=False, heli=True,
                airplanes=True, slot_name='32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-164069.140625, 462534.5625), large=False, heli=True,
                airplanes=True, slot_name='34', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-164012.8125, 462640.625), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-163956.21875, 462746.34375), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-163899.703125, 462852.25), large=False, heli=True,
                airplanes=True, slot_name='40', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-164427.0625, 461863.75), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-164370.75, 461969.6875), large=False, heli=True,
                airplanes=True, slot_name='24', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-164295.296875, 462110.75), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-164210.390625, 462269.9375), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-164154, 462375.84375), large=False, heli=True,
                airplanes=True, slot_name='31', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-164097.640625, 462481.78125), large=False, heli=True,
                airplanes=True, slot_name='33', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-164040.96875, 462587.59375), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-163984.375, 462693.40625), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-163928.046875, 462799.40625), large=False, heli=True,
                airplanes=True, slot_name='39', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-163871.5, 462905.28125), large=False, heli=True,
                airplanes=True, slot_name='41', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-164831.75, 463060.25), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-164273.75, 463397), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-164327.609375, 463334.6875), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-164261.765625, 463291.90625), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-164226.859375, 463389.71875), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-164127.1875, 463443.5), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-164025.6875, 463498.3125), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-164161.859375, 463346.375), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-164061.3125, 463400.9375), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-163959.875, 463455.90625), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-164172.953125, 463450.96875), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-164073.40625, 463505.71875), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-163972.140625, 463561.0625), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=8.0, shelter=False))


class Krasnodar_Pashkovsky(Airport):
    id = 19
    name = "Krasnodar-Pashkovsky"
    position = mapping.Point(7717.637452, 387878.803876)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Krasnodar_Pashkovsky, self).__init__()

        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(8852.1181640625, 388779.3125), large=False, heli=True,
                airplanes=True, slot_name='19', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(8811.3408203125, 388735.3125), large=False, heli=True,
                airplanes=True, slot_name='18', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(8770.4775390625, 388691.34375), large=False, heli=True,
                airplanes=True, slot_name='17', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(8729.6845703125, 388647.40625), large=False, heli=True,
                airplanes=True, slot_name='16', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(8689.171875, 388603.03125), large=False, heli=True,
                airplanes=True, slot_name='15', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(8648.1572265625, 388559.3125), large=False, heli=True,
                airplanes=True, slot_name='14', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(8116.8237304688, 387990.71875), large=False, heli=True,
                airplanes=True, slot_name='12', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(8076.0463867188, 387946.71875), large=False, heli=True,
                airplanes=True, slot_name='11', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(8035.1831054688, 387902.75), large=False, heli=True,
                airplanes=True, slot_name='10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(7994.3901367188, 387858.8125), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(7953.8774414063, 387814.4375), large=False, heli=True,
                airplanes=True, slot_name='08', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(7912.8627929688, 387770.71875), large=False, heli=True,
                airplanes=True, slot_name='07', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(8158.8012695313, 388037.375), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(7036.2416992188, 386835.375), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(6995.46484375, 386791.375), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(6954.724609375, 386747.53125), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(6913.8081054688, 386703.46875), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(6873.2958984375, 386659.09375), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(7078.2197265625, 386882.03125), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))


class Sukhumi_Babushara(Airport):
    id = 20
    name = "Sukhumi-Babushara"
    position = mapping.Point(-220592.328125, 564391.96875)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Sukhumi_Babushara, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-219883.625, 563502.8125), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-219907.546875, 563580.25), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-219930.921875, 563648.6875), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-219791.34375, 563716.5), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-219720.76802519, 563720.41216012), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-219701.33316499, 563868.44392188), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-219729.47262868, 563926.47644348), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-219773.703125, 563977.125), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-219769.515625, 564016.9375), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-219765.375, 564056.5625), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-219761.21875, 564096.375), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-219757.046875, 564136.1875), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-219753.375, 564175.3125), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-219730.484375, 564199.875), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-219726.53125, 564236.8125), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-219722.40625, 564276.625), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-219718.203125, 564316.375), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-219819.8125, 564130.125), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-219815.625, 564169.9375), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-219811.421875, 564209.75), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-219807.1875, 564249.4375), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-219803.046875, 564289.25), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-219798.890625, 564328.875), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=18.0, height=11.0, shelter=False))


class Gudauta(Airport):
    id = 21
    name = "Gudauta"
    position = mapping.Point(-196710.085938, 516451.6875)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Gudauta, self).__init__()

        self.runways.append(Runway(150))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-196497.375, 515476.09375), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-196599.296875, 515489.78125), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-196587.828125, 515571.71875), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-196532.328125, 515672.59375), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-196543.90625, 515590.65625), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-196441.921875, 515576.96875), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-196477.46875, 515772.8125), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-196488.9375, 515690.8125), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-196386.765625, 515677.09375), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-196422.203125, 515873.25), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-196433.703125, 515791.28125), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-196331.578125, 515777.59375), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-196686.8125, 515606.90625), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-196675.53125, 515688.8125), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-196777.375, 515702.40625), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-196620.359375, 515789), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-196631.859375, 515707.09375), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-196722.5, 515802.6875), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-196565.125, 515889.5), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-196576.625, 515807.625), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-196667.28125, 515903.15625), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-197659.23757596, 516240.61614072), large=False, heli=True,
                airplanes=True, slot_name='10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-197684.61257596, 516294.83489072), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-197736.15945096, 516403.14739072), large=False, heli=True,
                airplanes=True, slot_name='07', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-197762.09695096, 516457.36614072), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-197787.23757596, 516511.80364072), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-197812.95632596, 516565.99114072), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-197838.50320096, 516620.27239072), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-197864.01882596, 516674.61614072), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-197889.87820096, 516728.77239072), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-197711.09695096, 516348.74114072), large=False, heli=True,
                airplanes=True, slot_name='08', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Batumi(Airport):
    id = 22
    name = "Batumi"
    position = mapping.Point(-355810.6875, 617386.1875)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Batumi, self).__init__()

        self.runways.append(Runway(310))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-356069.625, 618234.9375), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-356101.71875, 618304.8125), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-356168.27327001, 618351.087765), large=False, heli=True,
                airplanes=True, slot_name='10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-356142.96875, 618264.4375), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-355962.5625, 618097.125), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-356108.25, 618207.8125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-355977.71875, 618118.6875), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-355990.90625, 618136.9375), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-356004.4375, 618154.375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-356017.875, 618172.25), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))


class Senaki_Kolkhi(Airport):
    id = 23
    name = "Senaki-Kolkhi"
    position = mapping.Point(-281782.46875, 647279.46875)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Senaki_Kolkhi, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-281607.28417614, 646373.17498617), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-281456.22003117, 646561.96463955), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-281562.28044481, 646425.05699916), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-281489.89862041, 646523.67344853), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-281518.00576771, 646476.77560265), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-281358.9375, 646600.375), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-281336.65625, 646693.125), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-281277.9375, 646757.9375), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-281191.59375, 646756.25), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-281190.3125, 646854.125), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-281111, 646869.625), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-281016.25, 646954.125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-281475.84375, 646396.1875), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-281398.75, 646179.875), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-281357.5625, 646097.1875), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-281292, 646183.8125), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-281233.125, 646211.1875), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-281215.90625, 646252), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-281211.28125, 646333.3125), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-281276.8125, 646357.125), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-281385.53125, 646762.5), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-281504.625, 646733.0625), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-281386.5625, 646840.8125), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-281348.375, 646881.0625), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-281383.84375, 646924.6875), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-281335.5, 646973.75), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-281289.875, 646985), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-281245.78125, 646916.6875), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-281204.125, 646986.75), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-281169.84375, 647061.625), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-281153.875, 647160), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-281129.0625, 647207), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-281200.53125, 647119.125), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-281271.09375, 647118.25), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-281263.3125, 647204.125), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-281254.53125, 647279.8125), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-281098.84375, 647314.0625), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-281148.03125, 647346.5), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-281245.1875, 647435.4375), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-281289.8125, 647459.125), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-281335.40625, 647508), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-281387.4375, 647558.4375), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-281437.53125, 647454.6875), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-281395.34375, 647403.5), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-281330.28125, 647251.8125), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-281393.65625, 647266.5), large=False, heli=False,
                airplanes=True, slot_name='69', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-281378.125, 647356.5625), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-281347.375, 647393.625), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-281427.59375, 647634.8125), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-281573.3125, 647673), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-281460.28125, 647672.6875), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-281612.625, 647714.25), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-281615.09375, 647805.375), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-281442.4375, 647819), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-281477.1875, 647863.5625), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-281588.625, 647856.375), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-281634.53125, 647900.125), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-281618.375, 647993.375), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-281482.78125, 648004.625), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-281522.625, 648102.4375), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-281414.65625, 648104.5), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-281724.8125, 648062.625), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-281693.125, 648065.125), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-281665.125, 648068.125), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-281636.34375, 648071.5), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-281616, 648119.1875), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-281500.21875, 648225), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-281610.28125, 648369.0625), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=8.0, shelter=False))


class Kobuleti(Airport):
    id = 24
    name = "Kobuleti"
    position = mapping.Point(-317962.296875, 635632.96875)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Kobuleti, self).__init__()

        self.runways.append(Runway(250))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-317882.375, 635012.9375), large=False, heli=True,
                airplanes=True, slot_name='42', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-317748.375, 635096.5625), large=False, heli=True,
                airplanes=True, slot_name='41', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-317776.65625, 635293), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-317652.375, 635288.25), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-317595.0625, 635445.9375), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-317557.5, 635549.25), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-317519.875, 635652.875), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-317482.28125, 635756.375), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-317686.46875, 635541.1875), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-317648.90625, 635645), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-317611.21875, 635748.0625), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-317573.625, 635851.75), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-317854.40625, 636854.6875), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-317688.125, 636897.0625), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-317884.25, 636664.5625), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-317935.9375, 636407.875), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-317940.40625, 636490.1875), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-318001.09375, 636473.125), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-318022.46875, 636169.375), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-318026.90625, 636253), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-318087.625, 636235.9375), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-318165.3125, 635727.5), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-318144.15625, 635783.6875), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-318123.4375, 635840.125), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-318103.28125, 635896.625), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-318082.6875, 635952.875), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-318328.25, 635190.875), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-318321, 635219.9375), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-318314.625, 635249.25), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-318307.96875, 635278.5), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-318301.125, 635307.875), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-318294.4375, 635337.25), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-318287.8125, 635366.25), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-318280.78125, 635395.375), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-318274.21875, 635424.6875), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-318253.21875, 635494.1875), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-318242.875, 635522.3125), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-318232.625, 635550.5625), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-318222.53125, 635578.75), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-318212.28125, 635607.0625), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-318202, 635635.125), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-318191.53125, 635663.3125), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))


class Kutaisi(Airport):
    id = 25
    name = "Kutaisi"
    position = mapping.Point(-284887.375, 683858.8125)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Kutaisi, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-284604.78125, 682356.25), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-284566.03125, 682401.25), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-284525.5, 682446), large=False, heli=True,
                airplanes=True, slot_name='14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-284488.46875, 682491.0625), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-284107.0625, 685163.0625), large=False, heli=True,
                airplanes=True, slot_name='57', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-284206.90625, 685057.3125), large=False, heli=True,
                airplanes=True, slot_name='55', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-283996.8125, 684974.1875), large=False, heli=True,
                airplanes=True, slot_name='56', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-283964.28125, 685176.3125), large=False, heli=True,
                airplanes=True, slot_name='58', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-284717.0625, 682696.75), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-284684, 682812.125), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-284650.90625, 682927.4375), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-284605.75, 683031.3125), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-284526.21875, 683121.1875), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-284446.71875, 683211.0625), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-284244.25, 683742.375), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-284211.1875, 683857.75), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-284178.09375, 683973.0625), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-284171.1875, 684152.0625), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-284191, 684270.4375), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-284210.8125, 684388.75), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-284200.65625, 684497.6875), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-284167.59375, 684613.0625), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-284134.5, 684728.375), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-284386.84375, 683374.25), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-284378.0625, 683402.75), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-284369.90625, 683431.625), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-284361.53125, 683460.4375), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-284353.34375, 683489.3125), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-284345.09375, 683518.3125), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-284337, 683547.0625), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-284328.46875, 683575.875), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-284320.46875, 683604.6875), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-284312.1875, 683633.6875), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-284303.90625, 683662.5), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-284295.4375, 683691.25), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-284890.53125, 682746.0625), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-284857.4375, 682861.375), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-284824.375, 682976.75), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-284741.09375, 683150.375), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-284661.5625, 683240.25), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-284582.0625, 683330.125), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-284525.6875, 683413.8125), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-284492.59375, 683529.125), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-284459.53125, 683644.5), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-284417.71875, 683791.6875), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-284384.625, 683907), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-284351.5625, 684022.375), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-284348.90625, 684121.8125), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-284368.71875, 684240.1875), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-284388.53125, 684358.5), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-284374.125, 684546.9375), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-284341.03125, 684662.3125), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-284307.96875, 684777.6875), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-286045.8125, 682836.875), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-285900.25, 682753.5625), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-286147.875, 683066.25), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-285950.75, 683030), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-285763.875, 682928.1875), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Mineralnye_Vody(Airport):
    id = 26
    name = "Mineralnye Vody"
    position = mapping.Point(-51259.983985, 705734.026899)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Mineralnye_Vody, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-52132.26171875, 706676.875), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-52107.890625, 706621.875), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-52081.31640625, 706568.25), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-52055.515625, 706514), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-52029.734375, 706459.75), large=False, heli=True,
                airplanes=True, slot_name='24', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-52004.15625, 706405.5625), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-51978.3984375, 706351.25), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-51952.8828125, 706296.875), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-51927.08203125, 706242.75), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-51900.98046875, 706188.8125), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-51875.1171875, 706134.5625), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-51849.5859375, 706080.3125), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-51823.8046875, 706026.1875), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-51798.19140625, 705971.875), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-51772.2421875, 705917.75), large=False, heli=True,
                airplanes=True, slot_name='14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-51590.734375, 705539.3125), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-51603.890625, 705566.125), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-51616.52734375, 705593.375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-51629.58984375, 705620.25), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-51642.30859375, 705647.5), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-51655.30859375, 705674.8125), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-51668.23828125, 705701.75), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-51680.92578125, 705728.75), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-51694.10546875, 705755.8125), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-51706.63671875, 705783.0625), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-51719.61328125, 705810.0625), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-51732.4609375, 705837.125), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-51745.375, 705864.25), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))


class Nalchik(Airport):
    id = 27
    name = "Nalchik"
    position = mapping.Point(-124912.453125, 760449.59375)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Nalchik, self).__init__()

        self.runways.append(Runway(60))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-125432.2109375, 760324.1875), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-125415.2265625, 760348.875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-125398.1953125, 760373.625), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-125381.203125, 760398.375), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-125364.265625, 760423.0625), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-125347.265625, 760447.8125), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-125330.2734375, 760472.5625), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-125313.25, 760497.25), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-125296.2890625, 760521.9375), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-125279.2734375, 760546.6875), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-125148.34375, 760748), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-125214.2734375, 760647.625), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-125181.859375, 760698.25), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-125116.8515625, 760798.75), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-125245.3515625, 760596.3125), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Mozdok(Airport):
    id = 28
    name = "Mozdok"
    position = mapping.Point(-83450.417969, 834461.78125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Mozdok, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-84047.34375, 833973.125), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-85129.6015625, 832223.8125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-85226.8046875, 832297.1875), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-85269.125, 832171), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-85213.28125, 831977.8125), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-85246.7734375, 831859.625), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-85116.234375, 831784.6875), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-85087.8515625, 831900.375), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-85074.921875, 832018.5625), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-83973.453125, 832792.5625), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-83952.578125, 833011.75), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-83941.125, 833133.6875), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-83930.3125, 833278.375), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-83959.7578125, 833464.9375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-84067.1640625, 833603.9375), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-84060.8046875, 833868.9375), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-84034.0390625, 834077.1875), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-84020.65625, 834181.3125), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-83993.78125, 834389.625), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-83980.2890625, 834493.75), large=False, heli=True,
                airplanes=True, slot_name='07', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-83966.6796875, 834597.8125), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-83953.3984375, 834702), large=False, heli=True,
                airplanes=True, slot_name='11', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-83940.0078125, 834806.125), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-83926.640625, 834910.25), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-83913.234375, 835014.375), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-83899.8359375, 835118.5625), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-83886.328125, 835222.6875), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-83873.859375, 835326.125), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-83987.2578125, 834443.625), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-83973.8359375, 834548.8125), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-83960.6328125, 834654.125), large=False, heli=True,
                airplanes=True, slot_name='10', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-83947.3046875, 834754.375), large=False, heli=True,
                airplanes=True, slot_name='12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-83934.8984375, 834858.75), large=False, heli=True,
                airplanes=True, slot_name='14', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-83920.671875, 834962.125), large=False, heli=True,
                airplanes=True, slot_name='16', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-83893.7734375, 835169.1875), large=False, heli=True,
                airplanes=True, slot_name='19', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-83880.1015625, 835277.3125), large=False, heli=True,
                airplanes=True, slot_name='21', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-83765.015625, 835046.6875), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-83717, 835330.4375), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-83760.5703125, 835549.6875), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))


class Tbilisi_Lochini(Airport):
    id = 29
    name = "Tbilisi-Lochini"
    position = mapping.Point(-315671.09375, 896629.90625)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Tbilisi_Lochini, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-315166.34375, 897212.4375), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-315196.28125, 897192.5), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-315225.46875, 897171.9375), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-315254.8125, 897151.1875), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-315227.9375, 897048.6875), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-315198.625, 897069.375), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-315169.28125, 897089.9375), large=False, heli=False,
                airplanes=True, slot_name='34', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-315139.5625, 897109.875), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-315109.96875, 897130.125), large=False, heli=False,
                airplanes=True, slot_name='31', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-315056.875, 897054.5), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-315083.09375, 897027.5), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-315116.1875, 897014.3125), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-315142.15625, 896987), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-315171.46875, 896966.3125), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-314944.46875, 896889.8125), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-314970.3125, 896862.8125), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-315003.78125, 896849.625), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-315029.375, 896822.3125), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-315058.6875, 896801.625), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-315085.84375, 896904.6875), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-315115.15625, 896884), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-315026.78125, 896945.1875), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-315056.5, 896925.25), large=False, heli=False,
                airplanes=True, slot_name='24', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-314997.1875, 896965.4375), large=False, heli=False,
                airplanes=True, slot_name='21', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-314830.6875, 896723.1875), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-314857.25, 896697.75), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-314890, 896683), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-314916.3125, 896657.25), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-314945.625, 896636.5625), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-314972.78125, 896739.625), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-315002.09375, 896718.9375), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-314913.71875, 896780.125), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-314943.4375, 896760.1875), large=False, heli=False,
                airplanes=True, slot_name='14', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-314884.125, 896800.375), large=False, heli=False,
                airplanes=True, slot_name='11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-314770.875, 896635.125), large=False, heli=False,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-314800.46875, 896614.875), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-314830.1875, 896594.9375), large=False, heli=False,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-314859.53125, 896574.375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-314888.84375, 896553.6875), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-314709.1875, 896537.375), large=False, heli=True,
                airplanes=True, slot_name='51', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-314742.75, 896524.0625), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-314768.0625, 896496.5), large=False, heli=True,
                airplanes=True, slot_name='49', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-314991, 896554.9375), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-315015.78125, 896539), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-315041.1875, 896523.875), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-314979.09375, 896460.9375), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-314950.57799001, 896480.9850637), large=False, heli=True,
                airplanes=True, slot_name='45', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-314940.5, 896390.125), large=False, heli=False,
                airplanes=True, slot_name='46', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-314901.25, 896415.875), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-314404.625, 895930), large=False, heli=False,
                airplanes=True, slot_name='77', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-314372.65625, 895962), large=False, heli=False,
                airplanes=True, slot_name='78', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-314337.75, 895990.25), large=False, heli=False,
                airplanes=True, slot_name='74', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-314242.25, 895946.375), large=False, heli=False,
                airplanes=True, slot_name='73', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-314273.53125, 895919.875), large=False, heli=False,
                airplanes=True, slot_name='53', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-314310.125, 895892.625), large=False, heli=False,
                airplanes=True, slot_name='54', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-314342.09375, 895861.9375), large=False, heli=False,
                airplanes=True, slot_name='55', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-314384.9375, 895827.25), large=False, heli=False,
                airplanes=True, slot_name='56', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-314256.78125, 896018), large=False, heli=False,
                airplanes=True, slot_name='52', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-314421.9375, 895757.125), large=False, heli=False,
                airplanes=True, slot_name='57', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-314481.625, 895824.125), large=False, heli=False,
                airplanes=True, slot_name='58', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-314325.0625, 895744.9375), large=False, heli=False,
                airplanes=True, slot_name='70', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-314299.75, 895768.125), large=False, heli=False,
                airplanes=True, slot_name='71', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-314266.53125, 895797.875), large=False, heli=False,
                airplanes=True, slot_name='72', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-314553.34375, 895809.125), large=False, heli=True,
                airplanes=False, slot_name='H04', length=28.510406, width=21.5, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-314522.71875, 895758.125), large=False, heli=True,
                airplanes=False, slot_name='H03', length=28.510406, width=21.5, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-314492.875, 895709.4375), large=False, heli=True,
                airplanes=False, slot_name='H02', length=28.510406, width=21.5, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-314461.46875, 895661.875), large=False, heli=True,
                airplanes=False, slot_name='H01', length=28.510406, width=21.5, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-314422.8125, 895567.9375), large=False, heli=False,
                airplanes=True, slot_name='66', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-314395.3125, 895589.75), large=False, heli=False,
                airplanes=True, slot_name='65', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-314367.28125, 895611.25), large=False, heli=False,
                airplanes=True, slot_name='64', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-314338.9375, 895633.3125), large=False, heli=False,
                airplanes=True, slot_name='63', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-314370.03125, 895537.375), large=False, heli=False,
                airplanes=True, slot_name='67', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-314326.0625, 895514.625), large=False, heli=False,
                airplanes=True, slot_name='68', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-314249.40625, 895478.125), large=False, heli=False,
                airplanes=True, slot_name='69', length=43.057953, width=40.0, height=None, shelter=False))


class Soganlug(Airport):
    id = 30
    name = "Soganlug"
    position = mapping.Point(-317828.046875, 895407.1875)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Soganlug, self).__init__()

        self.runways.append(Runway(140))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-318023.51732654, 895394.57452592), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-317995.3125, 895361.3125), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-318524.40625, 895803.625), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-318054.09375, 895426.1875), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-317122.75, 894202.5625), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Vaziani(Airport):
    id = 31
    name = "Vaziani"
    position = mapping.Point(-319064.875, 903148.53125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Vaziani, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-318059.6875, 902639.0625), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-317991.90625, 902709.9375), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-317935.34375, 902716.625), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-317921.375, 902608.3125), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-317868.84375, 902585.875), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-317883.03125, 902815.6875), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-317837.375, 902898), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-317877.96875, 902913.3125), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-317949.65625, 902877.8125), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-317737.875, 902814.25), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-317698.0625, 902899.9375), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-317696, 902801.75), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-317627.3125, 902842.75), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-317627.75, 903180.25), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-317586.0625, 903167.9375), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-317588.25, 903266.125), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-317517.3125, 903209), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-317767.78125, 903282), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-317772.59375, 903187.5), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-317815.375, 903196.375), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-317856.90625, 903264.5625), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-318176.5, 902711.5), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-318160.09375, 902843.5), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-318249.46875, 902735.625), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-318237.0625, 902905), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-318318.90625, 902844), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-318372.5625, 902882.875), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-318306.375, 902973.3125), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-318468.3125, 902994.375), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-318389.40625, 903089.3125), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-318377.9375, 903160.8125), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-318517.40625, 903106.9375), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-318461.6875, 903209.875), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-318595.1875, 903209.125), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-318626.25, 903245.5625), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-318593.40625, 903322.75), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-318477.34375, 903285.5), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-318485.09375, 903378.375), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-318604.0625, 903415.75), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-318488, 903509.5625), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-318569.03125, 903563.625), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-318710.625, 903551.125), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-318751.6875, 903512), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-318834.5625, 903551.625), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-318799.96875, 903598.625), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-318823.4375, 903642.9375), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-318648.4375, 903680.3125), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-318777.9375, 903751.3125), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-318912.125, 903689.75), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-318846.4375, 903816.25), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-318953.78125, 903771.1875), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-319009.6875, 903764.875), large=False, heli=False,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-319074.125, 903772.375), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-319027.125, 903912.3125), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-319135.46875, 903787.5), large=False, heli=False,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-319125, 903882.875), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-319190.8125, 903806.875), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-319025, 903982.625), large=False, heli=False,
                airplanes=True, slot_name='80', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-319119.71875, 904039.6875), large=False, heli=False,
                airplanes=True, slot_name='81', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-319164.5, 904037.0625), large=False, heli=False,
                airplanes=True, slot_name='82', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-319216.0625, 904052.625), large=False, heli=False,
                airplanes=True, slot_name='83', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-319132.625, 904130.375), large=False, heli=False,
                airplanes=True, slot_name='87', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-319120.84375, 904181.375), large=False, heli=False,
                airplanes=True, slot_name='88', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-319098.15625, 904228.25), large=False, heli=False,
                airplanes=True, slot_name='89', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-319044.25, 904305.125), large=False, heli=False,
                airplanes=True, slot_name='90', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-318992.5, 904258.625), large=False, heli=False,
                airplanes=True, slot_name='91', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-319183.96875, 904159.9375), large=False, heli=False,
                airplanes=True, slot_name='86', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-319250.71875, 904141.8125), large=False, heli=False,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-319292.71875, 904101.5625), large=False, heli=False,
                airplanes=True, slot_name='84', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-319285.65625, 903837.4375), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-319340.84375, 903865.75), large=False, heli=False,
                airplanes=True, slot_name='71', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-319389.46875, 903909.75), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-319429.34375, 903957.25), large=False, heli=False,
                airplanes=True, slot_name='73', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-319487.34375, 904034), large=False, heli=False,
                airplanes=True, slot_name='75', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-319560.8125, 904094.0625), large=False, heli=False,
                airplanes=True, slot_name='74', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-319512.03125, 904151.5625), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-319442.21875, 904088.3125), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-318912.1875, 903856.25), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-318695.125, 903248.3125), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-319222.5625, 903907.375), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-319295.4375, 903965.75), large=False, heli=True,
                airplanes=True, slot_name='92', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-319783.8125, 904239.75), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-319752.375, 904274.6875), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-319819.53125, 904208.5625), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-319857.5, 904158.4375), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-319838.15625, 904184.4375), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-319622.5625, 904241.8125), large=False, heli=True,
                airplanes=True, slot_name='79', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-318047.53125, 902476.8125), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-318089.125, 902515.25), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-318125.34375, 902550.0625), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-318166.6875, 902592.875), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-319596, 904221.8125), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.5, width=18.0, height=11.0, shelter=False))


class Beslan(Airport):
    id = 32
    name = "Beslan"
    position = mapping.Point(-148590.171875, 843668.625)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Beslan, self).__init__()

        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-148875.828125, 844108.375), large=False, heli=True,
                airplanes=True, slot_name='15', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-148873.3125, 844068.4375), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-148870.78125, 844028.625), large=False, heli=True,
                airplanes=True, slot_name='13', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-148868.515625, 843988.625), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-148863.796875, 843906.8125), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-148857.65625, 843824.125), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-148852.15625, 843744.0625), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-148866.078125, 843948.625), large=False, heli=True,
                airplanes=True, slot_name='11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-148860.890625, 843863.75), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-148855.875, 843785.0625), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-148838.5, 843498.125), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-148868.453125, 843496.375), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-148815.359375, 843611.0625), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-148845.28125, 843609.3125), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-148875.21875, 843607.4375), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))


class Caucasus(Terrain):
    center = {"lat": 43.69666, "long": 32.96}
    bounds = mapping.Rectangle(380*1000, -560*1000, -600*1000, 1130*1000)
    map_view_default = MapView(mapping.Point(-255714.28571428, 680571.42857143), 1000000)
    city_graph = Graph.from_pickle(os.path.join(os.path.dirname(__file__), 'caucasus.p'))  # type: Graph
    temperature = [
        (-4, 14),
        (-8, 14),
        (-6, 16),
        (0, 19),
        (1, 24),
        (8, 30),
        (12, 33),
        (12, 32),
        (10, 28),
        (2, 22),
        (-2, 14),
        (-4, 12)
    ]
    assert(len(temperature) == 12)

    def __init__(self):
        super(Caucasus, self).__init__("Caucasus")
        # caucasus center MGRS
        # 36TWQ9949898109
        self.bullseye_blue = {"x": -291014, "y": 617414}
        self.bullseye_red = {"x": 11557, "y": 371700}

        self.airports['Anapa-Vityazevo'] = Anapa_Vityazevo()
        self.airports['Krasnodar-Center'] = Krasnodar_Center()
        self.airports['Novorossiysk'] = Novorossiysk()
        self.airports['Krymsk'] = Krymsk()
        self.airports['Maykop-Khanskaya'] = Maykop_Khanskaya()
        self.airports['Gelendzhik'] = Gelendzhik()
        self.airports['Sochi-Adler'] = Sochi_Adler()
        self.airports['Krasnodar-Pashkovsky'] = Krasnodar_Pashkovsky()
        self.airports['Sukhumi-Babushara'] = Sukhumi_Babushara()
        self.airports['Gudauta'] = Gudauta()
        self.airports['Batumi'] = Batumi()
        self.airports['Senaki-Kolkhi'] = Senaki_Kolkhi()
        self.airports['Kobuleti'] = Kobuleti()
        self.airports['Kutaisi'] = Kutaisi()
        self.airports['Mineralnye Vody'] = Mineralnye_Vody()
        self.airports['Nalchik'] = Nalchik()
        self.airports['Mozdok'] = Mozdok()
        self.airports['Tbilisi-Lochini'] = Tbilisi_Lochini()
        self.airports['Soganlug'] = Soganlug()
        self.airports['Vaziani'] = Vaziani()
        self.airports['Beslan'] = Beslan()

        self.anapa_vityazevo().unit_zones.append(mapping.Rectangle(-5802.857142854, 242768.57142857, -7402.857142854, 244368.57142857))
        self.anapa_vityazevo().unit_zones.append(mapping.Rectangle(-4217.1428571397, 239325.71428572, -5417.1428571397, 240525.71428572))
        self.anapa_vityazevo().unit_zones.append(mapping.Rectangle(-5759.9999999969, 239132.85714286, -7159.9999999969, 240532.85714286))
        self.anapa_vityazevo().unit_zones.append(mapping.Rectangle(-3967.1428571397, 245318.57142857, -6767.1428571397, 248118.57142857))

        self.krasnodar_center().unit_zones.append(mapping.Rectangle(13360.857142856, 366714.28571429, 12360.857142856, 367714.28571429))
        self.krasnodar_center().unit_zones.append(mapping.Rectangle(13375.142857142, 367717.14285714, 12375.142857142, 368717.14285714))
        self.krasnodar_center().unit_zones.append(mapping.Rectangle(11072.285714285, 366687.14285714, 10372.285714285, 367387.14285714))
        self.krasnodar_center().unit_zones.append(mapping.Rectangle(15490.857142856, 361865.71428571, 12490.857142856, 364865.71428571))

        self.novorossiysk().unit_zones.append(mapping.Rectangle(-39022.285714285, 277836.85714285, -40122.285714285, 278936.85714285))
        self.novorossiysk().unit_zones.append(mapping.Rectangle(-40290.857142857, 279953.99999999, -40790.857142857, 280453.99999999))
        self.novorossiysk().unit_zones.append(mapping.Rectangle(-40255.142857142, 276589.71428571, -41155.142857142, 277489.71428571))

        self.krymsk().unit_zones.append(mapping.Rectangle(-6292.8571428566, 295422.85714286, -7292.8571428566, 296422.85714286))
        self.krymsk().unit_zones.append(mapping.Rectangle(-5878.5714285709, 292315.71428571, -6878.5714285709, 293315.71428571))
        self.krymsk().unit_zones.append(mapping.Rectangle(-4885.7142857137, 293180, -5885.7142857137, 294180))
        self.krymsk().unit_zones.append(mapping.Rectangle(-5414.2857142852, 295651.42857143, -6214.2857142852, 296451.42857143))

        self.maykop_khanskaya().unit_zones.append(mapping.Rectangle(-24574.285714285, 455938.57142857, -26574.285714285, 457938.57142857))
        self.maykop_khanskaya().unit_zones.append(mapping.Rectangle(-26888.571428571, 459010, -29088.571428571, 461210))
        self.maykop_khanskaya().unit_zones.append(mapping.Rectangle(-24917.142857142, 459945.71428572, -26717.142857142, 461745.71428572))
        self.maykop_khanskaya().unit_zones.append(mapping.Rectangle(-29138.57142857, 457451.42857144, -30738.57142857, 459051.42857144))

        self.gelendzhik().unit_zones.append(mapping.Rectangle(-50072.857142857, 296894.28571429, -50972.857142857, 297794.28571429))
        self.gelendzhik().unit_zones.append(mapping.Rectangle(-49435.714285714, 296528.57142857, -50135.714285714, 297228.57142857))
        self.gelendzhik().unit_zones.append(mapping.Rectangle(-50470, 298271.42857143, -51170, 298971.42857143))
        self.gelendzhik().unit_zones.append(mapping.Rectangle(-48665.714285714, 297704.28571428, -49265.714285714, 298304.28571428))

        self.krasnodar_pashkovsky().unit_zones.append(mapping.Rectangle(8105.7142857243, 388292.85714286, 6705.7142857243, 389692.85714286))
        self.krasnodar_pashkovsky().unit_zones.append(mapping.Rectangle(7184.2857142957, 384857.14285715, 6184.2857142957, 385857.14285715))
        self.krasnodar_pashkovsky().unit_zones.append(mapping.Rectangle(8848.5714285814, 386628.57142858, 7948.571428581399, 387528.57142858))
        self.krasnodar_pashkovsky().unit_zones.append(mapping.Rectangle(9570.0000000098, 383164.28571429, 8570.0000000098, 384164.28571429))

        self.sukhumi_babushara().unit_zones.append(mapping.Rectangle(-220484.28571428, 563282.85714286, -221084.28571428, 563882.85714286))
        self.sukhumi_babushara().unit_zones.append(mapping.Rectangle(-220081.42857143, 562380.00000001, -220681.42857143, 562980.00000001))
        self.sukhumi_babushara().unit_zones.append(mapping.Rectangle(-218804.28571429, 564057.14285715, -219404.28571429, 564657.14285715))
        self.sukhumi_babushara().unit_zones.append(mapping.Rectangle(-218895.71428571, 563268.57142858, -219495.71428571, 563868.57142858))
        self.sukhumi_babushara().unit_zones.append(mapping.Rectangle(-221415.71428571, 565074.28571429, -222015.71428571, 565674.28571429))

        self.gudauta().unit_zones.append(mapping.Rectangle(-196705.71428572, 516900, -197405.71428572, 517600))
        self.gudauta().unit_zones.append(mapping.Rectangle(-195732.85714286, 514945.71428571, -196332.85714286, 515545.71428571))
        self.gudauta().unit_zones.append(mapping.Rectangle(-195075.71428572, 516880, -195875.71428572, 517680))

        self.batumi().unit_zones.append(mapping.Rectangle(-356160, 616688.00000003, -356960, 617488.00000003))
        self.batumi().unit_zones.append(mapping.Rectangle(-357551.42857143, 614990.85714289, -358551.42857143, 615990.85714289))
        self.batumi().unit_zones.append(mapping.Rectangle(-355574.28571429, 615740.85714289, -356474.28571429, 616640.85714289))

        self.senaki_kolkhi().unit_zones.append(mapping.Rectangle(-281829.99999999, 646374.2857143, -282629.99999999, 647174.2857143))
        self.senaki_kolkhi().unit_zones.append(mapping.Rectangle(-280231.42857142, 645832.85714287, -280931.42857142, 646532.85714287))
        self.senaki_kolkhi().unit_zones.append(mapping.Rectangle(-282110, 645288.57142859, -282910, 646088.57142859))
        self.senaki_kolkhi().unit_zones.append(mapping.Rectangle(-281052.85714285, 648450.00000002, -281452.85714285, 648850.00000002))

        self.kobuleti().unit_zones.append(mapping.Rectangle(-319184.85714285, 636121.14285715, -320584.85714285, 637521.14285715))
        self.kobuleti().unit_zones.append(mapping.Rectangle(-317053.42857142, 634509.71428572, -317553.42857142, 635009.71428572))
        self.kobuleti().unit_zones.append(mapping.Rectangle(-317776.28571428, 634158.28571429, -318276.28571428, 634658.28571429))

        self.kutaisi().unit_zones.append(mapping.Rectangle(-285691.42857142, 683870.00000001, -286691.42857142, 684870.00000001))
        self.kutaisi().unit_zones.append(mapping.Rectangle(-285131.42857142, 685257.14285716, -286131.42857142, 686257.14285716))
        self.kutaisi().unit_zones.append(mapping.Rectangle(-283062.85714285, 682065.71428573, -283762.85714285, 682765.71428573))
        self.kutaisi().unit_zones.append(mapping.Rectangle(-283252.85714285, 685130.00000001, -283752.85714285, 685630.00000001))

        self.mineralnye_vody().unit_zones.append(mapping.Rectangle(-50675.714285712, 706205.71428572, -51275.714285712, 706805.71428572))
        self.mineralnye_vody().unit_zones.append(mapping.Rectangle(-52302.857142855, 704720, -53002.857142855, 705420))
        self.mineralnye_vody().unit_zones.append(mapping.Rectangle(-51194.285714284, 701500, -52594.285714284, 702900))
        self.mineralnye_vody().unit_zones.append(mapping.Rectangle(-48049.999999998, 706642.85714286, -48849.999999998, 707442.85714286))

        self.tbilisi_lochini().unit_zones.append(mapping.Rectangle(-315025.71428571, 894574.28571429, -316225.71428571, 895774.28571429))
        self.tbilisi_lochini().unit_zones.append(mapping.Rectangle(-316225.71428571, 896138.57142857, -317425.71428571, 897338.57142857))
        self.tbilisi_lochini().unit_zones.append(mapping.Rectangle(-314582.85714286, 897795.71428571, -315982.85714286, 899195.71428571))

        self.soganlug().unit_zones.append(mapping.Rectangle(-318431.42857142, 894650.00000001, -318931.42857142, 895150.00000001))
        self.soganlug().unit_zones.append(mapping.Rectangle(-318949.99999999, 894894.28571429, -319549.99999999, 895494.28571429))
        self.soganlug().unit_zones.append(mapping.Rectangle(-318215.7142857, 897200.00000001, -319215.7142857, 898200.00000001))

        self.vaziani().unit_zones.append(mapping.Rectangle(-318605.71428571, 901664.28571429, -319605.71428571, 902664.28571429))
        self.vaziani().unit_zones.append(mapping.Rectangle(-319434.28571428, 902484.28571429, -320434.28571428, 903484.28571429))
        self.vaziani().unit_zones.append(mapping.Rectangle(-318435.71428571, 904565.71428572, -319435.71428571, 905565.71428572))
        self.vaziani().unit_zones.append(mapping.Rectangle(-316582.85714285, 903304.28571429, -317582.85714285, 904304.28571429))

        self.sochi_adler().unit_zones.append(mapping.Rectangle(-164637.14285714, 461964.28571428, -165237.14285714, 462564.28571428))
        self.sochi_adler().unit_zones.append(mapping.Rectangle(-162801.42857142, 460978.57142857, -163601.42857142, 461778.57142857))
        self.sochi_adler().unit_zones.append(mapping.Rectangle(-165514.28571428, 461815.71428571, -165914.28571428, 462215.71428571))

        # for x in sorted(self.airports, key=lambda x: self.airports[x].id):
        #     airport = self.airports[x]
        #     print("airports[{id}] = {{'id': {id}, 'name': '{name}', 'tacan':{tacan}, 'runways': []}}".format(
        #         id=airport.id, name=x, tacan=airport.tacan if airport.tacan else None
        #     ))
        #     for r in self.airports[x].runways:
        #         print("airports[{id}]['runways'].append({hdg})".format(id=airport.id, hdg=r.heading))

    def anapa_vityazevo(self) -> Airport:
        return self.airports["Anapa-Vityazevo"]

    def krasnodar_center(self) -> Airport:
        return self.airports["Krasnodar-Center"]

    def novorossiysk(self) -> Airport:
        return self.airports["Novorossiysk"]

    def krymsk(self) -> Airport:
        return self.airports["Krymsk"]

    def maykop_khanskaya(self) -> Airport:
        return self.airports["Maykop-Khanskaya"]

    def gelendzhik(self) -> Airport:
        return self.airports["Gelendzhik"]

    def sochi_adler(self) -> Airport:
        return self.airports["Sochi-Adler"]

    def krasnodar_pashkovsky(self) -> Airport:
        return self.airports["Krasnodar-Pashkovsky"]

    def sukhumi_babushara(self) -> Airport:
        return self.airports["Sukhumi-Babushara"]

    def gudauta(self) -> Airport:
        return self.airports["Gudauta"]

    def batumi(self) -> Airport:
        return self.airports["Batumi"]

    def senaki_kolkhi(self) -> Airport:
        return self.airports["Senaki-Kolkhi"]

    def kobuleti(self) -> Airport:
        return self.airports["Kobuleti"]

    def kutaisi(self) -> Airport:
        return self.airports["Kutaisi"]

    def mineralnye_vody(self) -> Airport:
        return self.airports["Mineralnye Vody"]

    def nalchik(self) -> Airport:
        return self.airports["Nalchik"]

    def mozdok(self) -> Airport:
        return self.airports["Mozdok"]

    def tbilisi_lochini(self) -> Airport:
        return self.airports["Tbilisi-Lochini"]

    def soganlug(self) -> Airport:
        return self.airports["Soganlug"]

    def vaziani(self) -> Airport:
        return self.airports["Vaziani"]

    def beslan(self) -> Airport:
        return self.airports["Beslan"]

    def default_red_airports(self) -> List[Airport]:
        return [
            self.anapa_vityazevo(),
            self.krymsk(),
            self.novorossiysk(),
            self.krasnodar_center(),
            self.krasnodar_pashkovsky(),
            self.maykop_khanskaya(),
            self.gelendzhik(),
            self.mineralnye_vody(),
            self.mozdok(),
            self.beslan(),
            self.nalchik(),
            self.sochi_adler()
        ]

    def default_blue_airports(self) -> List[Airport]:
        return [
            self.batumi(),
            self.vaziani(),
            self.soganlug(),
            self.kobuleti(),
            self.senaki_kolkhi(),
            self.tbilisi_lochini(),
            self.kutaisi()
        ]