from dcs.terrain.terrain import Terrain, Airport, Runway, ParkingSlot, MapView, Graph
import dcs.mapping as mapping
import random
from datetime import datetime


class Saint_Pierre_du_Mont(Airport):
    id = 1
    name = "Saint Pierre du Mont"
    position = mapping.Point(-11938.055664, -47277.988281)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Saint_Pierre_du_Mont, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-11861.235351563, -46465.25390625), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-11873.943184903, -46479.21794791), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-11898.822265625, -46507.36328125), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-11886.739257813, -46492.5), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-12039.180664063, -46515.12109375), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-12058.407226563, -46497.13671875), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-12037.9765625, -46804.5625), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-12129.071289063, -46484.23828125), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-12131.545898438, -46550.19140625), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-12134.2421875, -46619.4375), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-12137.01171875, -46693.15625), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-12186.439453125, -46857.2734375), large=False, heli=True,
                airplanes=True, slot_name='78', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-12124.87890625, -46938.7734375), large=False, heli=True,
                airplanes=True, slot_name='81', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-12019.78515625, -47078.625), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-12001.478515625, -47019.37109375), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-12117.408203125, -46866.7109375), large=False, heli=True,
                airplanes=True, slot_name='79', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-12046.608398438, -47984.5625), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-12027.291992188, -47962.453125), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-12007.661132813, -47941.08984375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-12082.845703125, -48027.05859375), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-12065.557617188, -48006.5078125), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-11731.30078125, -48142.2109375), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-11689.122070313, -48092.28515625), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-11607.21484375, -48090.13671875), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-11485.78515625, -48099.5), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-11493.037109375, -48052.19921875), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-11505.822265625, -47971.53515625), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-11522.823242188, -47863.47265625), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-11543.275390625, -47727.5625), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-11546.611328125, -48018.2578125), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-11565.462890625, -47896.51171875), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-11583.840820313, -47787.68359375), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-11579.479492188, -47644.8046875), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-11519.467773438, -47477.08984375), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-11488.647460938, -47367.4375), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-11510.143554688, -47591.2265625), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-11457.013671875, -47441.32421875), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-11444.255859375, -47329.359375), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-11450.486328125, -47190.890625), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-11496.440429688, -47212.94921875), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-11453.455078125, -47132.046875), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-11497.38671875, -47072.8671875), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-11443.544921875, -47025.45703125), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-11432.590820313, -46933.72265625), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-11482.905273438, -46949.73046875), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-11464.669921875, -46793.51953125), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-11411.390625, -46765.30078125), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-11510.172851563, -46702.23828125), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-11603.045898438, -46734.75), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-11693.220703125, -46668.15625), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-11743.827148438, -48032.1171875), large=False, heli=True,
                airplanes=True, slot_name='117', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-11742.192382813, -47930.80078125), large=False, heli=True,
                airplanes=True, slot_name='113', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-11738.780273438, -47846.27734375), large=False, heli=True,
                airplanes=True, slot_name='111', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-11791.165039063, -47991.6875), large=False, heli=True,
                airplanes=True, slot_name='116', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-11768.6796875, -47652.5859375), large=False, heli=True,
                airplanes=True, slot_name='108', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-11764.453125, -47571.18359375), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-11742.244140625, -47427.82421875), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-11769.696289063, -47273.6171875), large=False, heli=True,
                airplanes=True, slot_name='98', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-11722.994140625, -47693.921875), large=False, heli=True,
                airplanes=True, slot_name='109', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-11703.243164063, -47521.046875), large=False, heli=True,
                airplanes=True, slot_name='104', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-11701.814453125, -47353.62109375), large=False, heli=True,
                airplanes=True, slot_name='100', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-11725.767578125, -47249.14453125), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-11833.3125, -46413.54296875), large=False, heli=True,
                airplanes=True, slot_name='61', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-11836.239257813, -47220.046875), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-11726.50390625, -47038.4375), large=False, heli=True,
                airplanes=True, slot_name='89', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-11725.782226563, -46914.33203125), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-11707.290039063, -46748.6328125), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-11518.412109375, -46987.10546875), large=False, heli=True,
                airplanes=True, slot_name='95', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-11593.666015625, -47070.2421875), large=False, heli=True,
                airplanes=True, slot_name='94', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-11773.306640625, -47067.875), large=False, heli=True,
                airplanes=True, slot_name='90', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-11651.00390625, -47687.70703125), large=False, heli=True,
                airplanes=True, slot_name='110', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-11509.331054688, -46558.09375), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-11563.271484375, -46585.95703125), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-11518.399414063, -46435.94140625), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-11579.274414063, -46446.08203125), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-11652.578125, -46399.91015625), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-11777.2734375, -46514.328125), large=False, heli=True,
                airplanes=True, slot_name='62', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-11794.124023438, -46463.8359375), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-11810.203125, -46957.5078125), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-11827.336914063, -46861.72265625), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-11802.4921875, -46798.109375), large=False, heli=True,
                airplanes=True, slot_name='93', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-11466.025390625, -47522.421875), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-11481.012695313, -47564.6640625), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-11450.46875, -47479.6875), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-11424.7890625, -47287.3671875), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-11426.75390625, -47230.921875), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-11431.197265625, -47100.2734375), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-11426.763671875, -47059.93359375), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-11416.50390625, -46981.125), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-11408.248046875, -46893.3046875), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-11403.66796875, -46850.73046875), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-11395.853515625, -46805.98828125), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-11716.645507813, -46377.0859375), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-11761.440429688, -46380.3671875), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-11722.368164063, -48000.62109375), large=False, heli=False,
                airplanes=True, slot_name='115', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-11720.6328125, -47963.28125), large=False, heli=False,
                airplanes=True, slot_name='114', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-11719.461914063, -47889.98828125), large=False, heli=False,
                airplanes=True, slot_name='112', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-11697.715820313, -47637.953125), large=False, heli=False,
                airplanes=True, slot_name='107', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-11695.588867188, -47595.81640625), large=False, heli=False,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-11669.390625, -47452.90625), large=False, heli=False,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-11670.260742188, -47410.08984375), large=False, heli=False,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-11690.357421875, -47295.484375), large=False, heli=False,
                airplanes=True, slot_name='99', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-12062.75, -47063.10546875), large=False, heli=False,
                airplanes=True, slot_name='84', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-12094.387695313, -47024.12109375), large=False, heli=False,
                airplanes=True, slot_name='83', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-12121.622070313, -46985.421875), large=False, heli=False,
                airplanes=True, slot_name='82', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-12174.390625, -46910.38671875), large=False, heli=False,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-12160.331054688, -46655.90234375), large=False, heli=False,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-12156.065429688, -46584.01171875), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-12151.716796875, -46515.1796875), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-11988.481445313, -47919.55859375), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-11984.814453125, -48054.07421875), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-11792.02734375, -48074.1015625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-11806.2421875, -48061.796875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-11819.955078125, -48049.546875), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-11834.15625, -48037.203125), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-12057.829101563, -46785.00390625), large=False, heli=True,
                airplanes=True, slot_name='76', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-12008.80078125, -48081.73828125), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))


class Lignerolles(Airport):
    id = 2
    name = "Lignerolles"
    position = mapping.Point(-35526.060547, -34407.238281)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lignerolles, self).__init__()

        self.runways.append(Runway(290))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-35437.69140625, -35072.56640625), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-35533.734375, -34914.5859375), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-35545.25, -34808.6484375), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-35583.09375, -34702.9375), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-35611.28125, -34626.1640625), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-35641.828125, -34546.3828125), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-35668.23828125, -34475.4375), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-35695.23828125, -34401.53515625), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-35719.58203125, -34336.12109375), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-35753.734375, -34272.54296875), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-35834.734375, -34201.00390625), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-35918.54296875, -34127.5234375), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-35951.19140625, -34223.8671875), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-35937.49609375, -34319.4921875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-35921.3203125, -34407.38671875), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-35836.9140625, -34567.953125), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-35793.9921875, -34631.75390625), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-35711.29296875, -34755.6875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-35651.09765625, -34857.5078125), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-35587.2109375, -34961.28125), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-35606.85546875, -35020.86328125), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-35657.9296875, -34938.12890625), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-35719.828125, -34835.2265625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-35773.26171875, -34747.58203125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-35805.203125, -34699.6328125), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-35855.1796875, -34624.9765625), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-35902.8125, -34553.9375), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-35935.82421875, -34498.52734375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-35102.33984375, -34855.7421875), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-35050.13671875, -34894.125), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-35065.109375, -34791.09765625), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-35247.71484375, -34535.34765625), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-35308.26171875, -34471.078125), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-35359.95703125, -34381.29296875), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-35389.15625, -34301.546875), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-35414.60546875, -34232.734375), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-35441.7421875, -34157.01953125), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-35479.6171875, -34052.66796875), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-35502.609375, -34128.00390625), large=False, heli=True,
                airplanes=True, slot_name='61', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-35507.71875, -33977.328125), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-35533.39453125, -33908.14453125), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-35557.3125, -33843.01171875), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-35180.4453125, -35159.98828125), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-35196.2109375, -35121.0078125), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-35211.74609375, -35081.6953125), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-35227.3125, -35042.55859375), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-35728.65625, -34895.4375), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-35823.390625, -34241.26953125), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-35874.6875, -34192.62109375), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-35904.046875, -34166.31640625), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-35441.09765625, -34105.60546875), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-35426.54296875, -35047.5859375), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-35415.1015625, -35022.5546875), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-35403.8984375, -34996.89453125), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-35392.83203125, -34970.84765625), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-35380.8828125, -34943.9375), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-35301.5546875, -34914.1953125), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-35284.15234375, -34922.390625), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-35267.5390625, -34930.05859375), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-35250.3125, -34937.8515625), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-35233.0625, -34946.03515625), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-35215.83203125, -34954.203125), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-35198.73046875, -34962.125), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-35181.11328125, -34970.1796875), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-35164.265625, -34978.46875), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-35147.6640625, -34986.28125), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))


class Cretteville(Airport):
    id = 3
    name = "Cretteville"
    position = mapping.Point(-18675.582031, -77791.164063)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Cretteville, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-19256.740234375, -77253.203125), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-19236.23046875, -77255.40625), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-18081.92578125, -78339.2265625), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-18100.044921875, -78337.8671875), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-19299.7265625, -77325.65625), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-19259.796875, -77383), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-19219.552734375, -77441.0703125), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-19097.205078125, -77645.21875), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-19056.87890625, -77656.5234375), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-18382.986328125, -77737.734375), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-18353.447265625, -77779.1015625), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-18123.4296875, -78148.8046875), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-18333.34765625, -77849.234375), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-18855.8046875, -77697.109375), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-18875.212890625, -77630.6328125), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-18721.369140625, -77382.1640625), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-19109.267578125, -77166.53125), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-19031.01171875, -77489.1875), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-19067.4609375, -77484.3671875), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-19049.123046875, -77486.6953125), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-19122.33984375, -77621.9921875), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-19024.6328125, -77651.0078125), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-18115.130859375, -78275.3671875), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-18305.9375, -77993.9140625), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-18351.392578125, -77926.4296875), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-18537.41796875, -77694.1875), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-18052.49609375, -78278.2109375), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-18112.76953125, -78196.515625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-18161.353515625, -78128.09375), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-18241.6953125, -77997.0859375), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-18434.375, -77715.09375), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-18516.58203125, -77647.0859375), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-18854.552734375, -77338.140625), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-18836.255859375, -77403.9296875), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-19060.23046875, -77581.9375), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-18761.44921875, -77469.1171875), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-19184.5390625, -77459.65625), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-19225.6796875, -77399.25), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-19303.953125, -77288.8046875), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-19265.904296875, -77342.7890625), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-19008.171875, -77098.7578125), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-18622.31640625, -77693.09375), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-18667.068359375, -77534.1953125), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-18645.56640625, -77480.0859375), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-18807.8828125, -77239.8828125), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-19108.0078125, -77145.546875), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-18233.6171875, -78511.296875), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-18225.890625, -78437.5703125), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-18227.91796875, -78455.984375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-18229.650390625, -78474.4140625), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-18231.5546875, -78492.7734375), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-18118.8046875, -78336.65625), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-19106.96875, -77125.8515625), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-19105.943359375, -77106.515625), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-19216.01953125, -77257.9140625), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-18420.499213946, -77798.911429215), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))


class Maupertus(Airport):
    id = 4
    name = "Maupertus"
    position = mapping.Point(16014.310059, -84882.660156)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Maupertus, self).__init__()

        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(15957.225585938, -84030.5546875), large=False, heli=True,
                airplanes=True, slot_name='01', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(16018.493164062, -84016.984375), large=False, heli=True,
                airplanes=True, slot_name='02', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(16237.17578125, -83995.703125), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(16196.150390625, -83987.4375), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(16115.506835938, -83983.5859375), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(16074.153320313, -83991.6328125), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(15994.185546875, -85262.78125), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))


class Brucheville(Airport):
    id = 5
    name = "Brucheville"
    position = mapping.Point(-14857.000488, -66027.34375)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Brucheville, self).__init__()

        self.runways.append(Runway(250))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-14501.358398438, -65514.94921875), large=False, heli=True,
                airplanes=True, slot_name='90', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-14517.989257813, -65507.62890625), large=False, heli=True,
                airplanes=True, slot_name='89', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-14534.658203125, -65500.1796875), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-14551.46875, -65492.34375), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-15255.484375, -66566.4921875), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-15218.252929688, -66387.6875), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-15152.118164063, -66305.09375), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-15106.09375, -66203.234375), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-15073.575195313, -66127.6875), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-15040.1796875, -66049.421875), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-15009.584960938, -65980.2109375), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14977.276367188, -65908.375), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14949.876953125, -65844.140625), large=False, heli=True,
                airplanes=True, slot_name='76', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14927.905273438, -65775.8046875), large=False, heli=True,
                airplanes=True, slot_name='77', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14938.030273438, -65667.796875), large=False, heli=True,
                airplanes=True, slot_name='80', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14946.461914063, -65557.3046875), large=False, heli=True,
                airplanes=True, slot_name='83', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-15034.13671875, -65603.4765625), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-15091.52734375, -65681.65625), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-15141.1953125, -65756.3984375), large=False, heli=True,
                airplanes=True, slot_name='93', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-15193.87890625, -65929.9375), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-15206.630859375, -66005.2578125), large=False, heli=True,
                airplanes=True, slot_name='100', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-15233.885742188, -66152.0078125), large=False, heli=True,
                airplanes=True, slot_name='104', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-15261.7734375, -66267.0625), large=False, heli=True,
                airplanes=True, slot_name='106', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15288.400390625, -66385.8359375), large=False, heli=True,
                airplanes=True, slot_name='108', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15344.825195313, -66414.8203125), large=False, heli=True,
                airplanes=True, slot_name='109', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15323.421875, -66319.625), large=False, heli=True,
                airplanes=True, slot_name='107', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15296.349609375, -66202.7890625), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-15273.4609375, -66103.375), large=False, heli=True,
                airplanes=True, slot_name='103', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-15262.833984375, -66046.34375), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-15246.717773438, -65957.546875), large=False, heli=True,
                airplanes=True, slot_name='99', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-15232.001953125, -65873.671875), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-15217.291015625, -65810.8359375), large=False, heli=True,
                airplanes=True, slot_name='94', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-14867.946289063, -66647.2890625), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-14857.071289063, -66711.109375), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-14793.830078125, -66628.4609375), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-14715.09375, -66501.90625), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-14739.391601563, -66435.5546875), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-14670.317382813, -66416.7421875), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14692.541992188, -66349.4765625), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-14624.703125, -66328.9921875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-14659.502929688, -66280.953125), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-14592.354492188, -66256.953125), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-14618.577148438, -66192.140625), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-14554.859375, -66174.7421875), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-14585.719726563, -66123.1484375), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-14523.669921875, -66105.265625), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-14545.145507813, -66033.828125), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-14458.555664063, -65957.6875), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-14488.490234375, -65892.578125), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-14436.583984375, -65881.4453125), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-14478.83203125, -65826.3671875), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-14429.744140625, -65808.953125), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-14473.884765625, -65754.6875), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-14421.282226563, -65718.9140625), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-14415.702148438, -65667.0625), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-14462.69921875, -65642.6171875), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-14419.032226563, -65578.015625), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-14748.681640625, -66316.8671875), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-14746.928710938, -66227.890625), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-14721.640625, -66127.9609375), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-14687.233398438, -66049.796875), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-14656.653320313, -65983.28125), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-14624.192382813, -65909.828125), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-14578.459960938, -65808.578125), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-14648.44921875, -65845.9375), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-14546.174804688, -65735.2109375), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-14515.787109375, -65667.703125), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-14487.78125, -65603.9296875), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-14663.276367188, -65443.4921875), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-14679.943359375, -65436.04296875), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-14696.75, -65428.2109375), large=False, heli=True,
                airplanes=True, slot_name='84', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-14676.118164063, -66470.203125), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-14638.977539063, -66399.1015625), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-14621.461914063, -66364.3046875), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-14591.599609375, -66301.3046875), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-14414.049804688, -65845.4296875), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-14404.415039063, -65765.578125), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-14394.783203125, -65619.7109375), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-14686.155273438, -66096.7109375), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-14652.928710938, -66025.1484375), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-14622.028320313, -65954.0078125), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-14591.83984375, -65887.2421875), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-14574.374023438, -65848.015625), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-15157.338867188, -66267.1875), large=False, heli=False,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-15139.759765625, -66227.703125), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-15107.727539063, -66156.9375), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-15075.030273438, -66081.0859375), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-14953.810546875, -65745.34375), large=False, heli=False,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-14957.19921875, -65702.28125), large=False, heli=False,
                airplanes=True, slot_name='79', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-14962.072265625, -65635.9140625), large=False, heli=False,
                airplanes=True, slot_name='81', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-14966.075195313, -65593.46875), large=False, heli=False,
                airplanes=True, slot_name='82', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-15274.353515625, -65996.59375), large=False, heli=False,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-15260.655273438, -65912.7265625), large=False, heli=False,
                airplanes=True, slot_name='98', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-15244.107421875, -65837.8203125), large=False, heli=False,
                airplanes=True, slot_name='95', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-15229.662109375, -66556.375), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-15204.504882813, -66546.40625), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-15179.133789063, -66536.671875), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-15154.333984375, -66526.015625), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-14992.06640625, -66702.9375), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-14998.623046875, -66686.140625), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-15005.604492188, -66668.90625), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-15012.447265625, -66651.6875), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-15019.56640625, -66634.625), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-15026.561523438, -66617.984375), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-15033.685546875, -66600.640625), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-15040.500976563, -66583.390625), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-15047.578125, -66566.375), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))


class Meautis(Airport):
    id = 6
    name = "Meautis"
    position = mapping.Point(-24484.185547, -71902.113281)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Meautis, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-24512.439453125, -71203.234375), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-24455.6015625, -71257.609375), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-24488.98046875, -71217.5), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-24222.326171875, -71235.40625), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-24237.43359375, -71246.21875), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-24207.40625, -71224.4453125), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-24469.798828125, -72625.875), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-24520.91015625, -72570.03125), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-24458.52734375, -72640.7578125), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-24753.8515625, -72582.4375), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-24738.1640625, -72572.71875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-24722.5234375, -72562.8125), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-24706.70703125, -72553.1484375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-24251.6875, -71528.109375), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-24241.32421875, -71476.25), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-24233.685546875, -71424.984375), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-24224.97265625, -71376.171875), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-24215.9609375, -71325.2109375), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-24432.71484375, -72550.5390625), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-24424.19921875, -72500.8203125), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-24415.59765625, -72449.15625), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-24532.384765625, -71210.2421875), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-24412.02734375, -72325.4296875), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-24406.2890625, -72293.8984375), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-24401.15625, -72264.3125), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-24395.71484375, -72235.328125), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-24390.3046875, -72205.4609375), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-24384.55859375, -72173.9296875), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-24379.42578125, -72144.3359375), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-24373.982421875, -72115.359375), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-24368.90625, -72085.9921875), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-24363.16796875, -72054.4609375), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-24358.03515625, -72024.8671875), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-24352.59375, -71995.890625), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-24347.275390625, -71966.0546875), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-24341.83984375, -71937.0703125), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-24336.7734375, -71907.7109375), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-24331.01171875, -71876.1875), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-24325.87109375, -71846.59375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-24320.455078125, -71817.6171875), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-24306.47265625, -71739.21875), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-24301.0390625, -71710.2421875), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-24295.970703125, -71680.875), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-24290.216796875, -71649.34375), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-24285.076171875, -71619.75), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-24279.650390625, -71590.7734375), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))


class Cricqueville_en_Bessin(Airport):
    id = 7
    name = "Cricqueville-en-Bessin"
    position = mapping.Point(-14917.461426, -50815.857422)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Cricqueville_en_Bessin, self).__init__()

        self.runways.append(Runway(350))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-15036.99609375, -51188.1875), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-15091.197265625, -51189.6875), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-15142.259765625, -51190.3359375), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-15281.184570313, -51137.03125), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-15298.483398438, -51091.53125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-15317.65625, -51047.0859375), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-15336.374023438, -51002.328125), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-15354.755859375, -50956.9296875), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-15418.361328125, -50414.19921875), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-15101.448242188, -50437.07421875), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-15140.26953125, -50467.3828125), large=False, heli=False,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-15179.002929688, -50500.98828125), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-14789.887695313, -50429.359375), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14785.345703125, -50480.71875), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14778.875976563, -50532.2890625), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14873.093679891, -50271.912260383), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14393.776367188, -50436.76953125), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14362.53515625, -50450.37109375), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-14330.71484375, -50463.71484375), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-15480.72265625, -50543.0390625), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-15456.775390625, -50455.05859375), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-15404.940429688, -50455.609375), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-15422.161132813, -50520.171875), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-15482.276367188, -50696.7109375), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-15475.487304688, -50678.74609375), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15532.52734375, -50821.71484375), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15526.719726563, -50803.74609375), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15556.122070313, -50900.8125), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15538.387695313, -50839.859375), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-15492.958984375, -50850.04296875), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-15317.954101563, -50832.0859375), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-15203.686523438, -50834.265625), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-14977.603515625, -50935.98046875), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-14829.362304688, -50973.69140625), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-15343.048828125, -50902.4375), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-15280.298828125, -50928.9609375), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-15245.411132813, -51016.99609375), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-15187.541992188, -51169.28125), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-14988.005859375, -51161.2421875), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-15062.760742188, -51115.62890625), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14834.578125, -51050.4609375), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-14740.361328125, -51063.00390625), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-14737.412109375, -51005.38671875), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-14481.265625, -51002.46484375), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-14534.053710938, -51029.69140625), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-14534.231445313, -50972.02734375), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-14433.102539063, -51086.09765625), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-14283.299804688, -51085.515625), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-14898.4296875, -50565.55078125), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-15205.576171875, -50580.7265625), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-15042.82421875, -50424.015625), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-14928.950195313, -50414.375), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-14831.16015625, -50282.3046875), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-14871.176757813, -50337.5625), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-14821.112304688, -50376.94921875), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-14852.219726563, -50551.953125), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-14220.969726563, -51007.28515625), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-14106.381835938, -51025.65625), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-14093.397460938, -51065.625), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-14138.702148438, -51079.06640625), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-14214.407226563, -51090.12890625), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-14495.455078125, -50471.9765625), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-14486.166992188, -50584.37109375), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-14371.833984375, -50654.5234375), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-14244.102539063, -50718.015625), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-14464.435546875, -50520.44921875), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-14730.510742188, -50690.265625), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-14806.484375, -50589.41015625), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-14266.1484375, -50823.421875), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-14251.94921875, -50811.6640625), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-14237.971679688, -50798.953125), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-14303.3828125, -51041.8125), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-14311.14453125, -51023.55859375), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))


class Lessay(Airport):
    id = 8
    name = "Lessay"
    position = mapping.Point(-33862.595703, -86418.007813)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lessay, self).__init__()

        self.runways.append(Runway(60))
        self.runways.append(Runway(120))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-33662.57421875, -86710.5703125), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-33433.50390625, -87110.734375), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-33482.44140625, -87000.0625), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-33684.90234375, -86676.8984375), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-33692.0078125, -86485.2109375), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-33598.76953125, -86289.0625), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-34212.1640625, -86446.484375), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-34181.9609375, -86422.921875), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-33818.0625, -87227.8359375), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-33699.921875, -87349.796875), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-33666.0390625, -87386.75), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-34258.4453125, -86497.6015625), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-34269.671875, -86482.6875), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-34302.3828125, -86437.90625), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-34291.44921875, -86452.9296875), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-34280.42578125, -86467.8125), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-34088.7421875, -86284.296875), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-33449.34765625, -85828.6484375), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-33433.03515625, -85836.90625), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-33664.3125, -85712.6328125), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-33647.8203125, -85721.1875), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-33631.27734375, -85729.4921875), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-33614.97265625, -85737.921875), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-33598.23828125, -85746.21875), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-33513.84765625, -87600.3828125), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-33776.38671875, -87132.734375), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-33691.08203125, -87216.8125), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-33597.89453125, -87308.9296875), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-33538.01953125, -87418.5703125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-33449.77734375, -86016.953125), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-33500.7578125, -86145.8203125), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-33607.65625, -86138.7265625), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-33679.51171875, -86230.21875), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-33785.83203125, -86456.2109375), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-33823.88671875, -86588.515625), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-33574.41796875, -86236.609375), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-33644.30078125, -86325.7265625), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-33685.91015625, -86421.7890625), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-33718.13671875, -86537.7578125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-33714.7890625, -86650.4921875), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-33754.078125, -86750.015625), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-33693.9765625, -86838.625), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-33649.79296875, -86745.40625), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-33621.7578125, -86944.375), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-33581.984375, -86843.9140625), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-33517.6015625, -86942.0546875), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-33565.828125, -87037.5390625), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-33520.64453125, -87147.375), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-33461.2734375, -87060.359375), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-33416.0390625, -87168.8203125), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-33353.05859375, -87262.25), large=False, heli=True,
                airplanes=True, slot_name='15', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-33272.55859375, -87342.828125), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-33385.7890625, -87356.1484375), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-33303.296875, -87432.875), large=False, heli=True,
                airplanes=True, slot_name='10', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-33278.5, -87511.9765625), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-33220.2890625, -87391.15625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-33247.94140625, -87366.6015625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))


class Sainte_Laurent_sur_Mer(Airport):
    id = 9
    name = "Sainte-Laurent-sur-Mer"
    position = mapping.Point(-14665.532227, -41130.955078)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sainte_Laurent_sur_Mer, self).__init__()

        self.runways.append(Runway(290))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-14792.571289063, -40413.9765625), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-14786.885742188, -40431.3671875), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-14780.911132813, -40449.0625), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-14775.3671875, -40466.57421875), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-14769.575195313, -40484.1484375), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-14763.927734375, -40501.84765625), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-14758.26953125, -40519.546875), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-14500.940429688, -41793.68359375), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-14506.548828125, -41776.21484375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-14512.370117188, -41758.85546875), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-14518.376953125, -41741.5546875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14524.096679688, -41724.0390625), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14716.283203125, -41543.76953125), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14729.244140625, -41490.97265625), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14741.564453125, -41439.4375), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14845.327148438, -41070.640625), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-14857.267578125, -41016.8515625), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-14868.475585938, -40965.5234375), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-14881.069335938, -40912.890625), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-14893.48046875, -40863.08984375), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-14932.262695313, -40735.390625), large=False, heli=True,
                airplanes=True, slot_name='19', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-14976.861328125, -40748.1015625), large=False, heli=True,
                airplanes=True, slot_name='20', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-15025.260742188, -40763.8671875), large=False, heli=True,
                airplanes=True, slot_name='21', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15079.633789063, -40779.78515625), large=False, heli=True,
                airplanes=True, slot_name='22', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15138.8046875, -40593.58984375), large=False, heli=True,
                airplanes=True, slot_name='32', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15092.795898438, -40578.37109375), large=False, heli=True,
                airplanes=True, slot_name='33', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15044.654296875, -40562.89453125), large=False, heli=True,
                airplanes=True, slot_name='34', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-14990.793945313, -40544.0703125), large=False, heli=True,
                airplanes=True, slot_name='35', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-14946.081054688, -40639.1953125), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-14964.600585938, -40645.234375), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-14982.981445313, -40651.38671875), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-15001.500976563, -40657.4296875), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-15019.73046875, -40663.4140625), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-15038.25, -40669.453125), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-15056.0390625, -40676.0546875), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-15074.408203125, -40682.09375), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-15093.846679688, -40688.37890625), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-14540.583984375, -41806.27734375), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14546.1875, -41788.8046875), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-14552.008789063, -41771.44921875), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-14558.014648438, -41754.1484375), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-14563.748046875, -41736.63671875), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))


class Biniville(Airport):
    id = 10
    name = "Biniville"
    position = mapping.Point(-7677.553223, -84529.835938)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Biniville, self).__init__()

        self.runways.append(Runway(320))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-8033.611328125, -84135.671875), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-8019.6059570313, -84147.4296875), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-8005.193359375, -84159.3203125), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-7991.2490234375, -84171.2734375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-7977.0590820313, -84183.1484375), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-7963.0268554688, -84195.2578125), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-7414.8676757813, -84869.8828125), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-7949.9409179688, -84208.34375), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-7943.2578125, -84462.4140625), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-7957.3520507813, -84450.75), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-7971.8725585938, -84439), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-7985.90234375, -84427.1484375), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-8000.1918945313, -84415.3984375), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-8014.328125, -84403.6484375), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-8028.1040039063, -84391.265625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-8042.5458984375, -84379.4765625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-8056.5776367188, -84367.6328125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-8070.8725585938, -84355.8984375), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-8085.4135742188, -84343.890625), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-7541.2006835938, -84882.4609375), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-7577.7485351563, -84846.140625), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-7811.5815429688, -84618.15625), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-7846.2333984375, -84581.015625), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-7882.6318359375, -84544.765625), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-7918.98828125, -84509.578125), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-7393.63671875, -84888.5546875), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-7373.1157226563, -84907.078125), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-7352.5859375, -84925.078125), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-7330.65625, -84897.21875), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-7351.8154296875, -84878.453125), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-7372.2724609375, -84859.859375), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-7392.73046875, -84841.78125), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Cardonville(Airport):
    id = 11
    name = "Cardonville"
    position = mapping.Point(-16508.699707, -53979.537109)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Cardonville, self).__init__()

        self.runways.append(Runway(150))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-15586.537109375, -54800.81640625), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-15641.615234375, -54743.21484375), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-15673.69140625, -54710.9765625), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-16080.328125, -53632.6796875), large=False, heli=False,
                airplanes=True, slot_name='90', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-16146.381835938, -53639.6328125), large=False, heli=False,
                airplanes=True, slot_name='93', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-16188.14453125, -53642.76171875), large=False, heli=False,
                airplanes=True, slot_name='94', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-16229.381835938, -53646.97265625), large=False, heli=False,
                airplanes=True, slot_name='95', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-16437.35546875, -53667.4375), large=False, heli=False,
                airplanes=True, slot_name='100', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-16477.451171875, -53656.6328125), large=False, heli=False,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-16555.625, -53639.40625), large=False, heli=False,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-17250.392578125, -53886.55859375), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-17221.244140625, -53918.51171875), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-17189.90234375, -53951.96484375), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-17159.515625, -53983.796875), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-17129.3671875, -54016.078125), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-16761.142578125, -54228.5703125), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-16751.130859375, -54273.7421875), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-16668.916015625, -54469.875), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-16649.916015625, -54509.546875), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-16629.091796875, -54548.6640625), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-16216.904296875, -54955.22265625), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-16185.349609375, -54985.09375), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-16114.564453125, -55053.5234375), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-16081.6015625, -55081.94921875), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-16011.588867188, -55136.2734375), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15978.251953125, -55164.328125), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15859.850585938, -54399.078125), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15853.694335938, -54416.64453125), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15848.7109375, -54434.12109375), large=False, heli=True,
                airplanes=True, slot_name='72', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-15843.506835938, -54452.1171875), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-15837.958984375, -54469.67578125), large=False, heli=True,
                airplanes=True, slot_name='70', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-15832.440429688, -54487.28125), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-16961.4765625, -53485.44921875), large=False, heli=True,
                airplanes=True, slot_name='112', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-16871.330078125, -53474.70703125), large=False, heli=True,
                airplanes=True, slot_name='111', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-16869.044921875, -53556.6796875), large=False, heli=True,
                airplanes=True, slot_name='110', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-16812.857421875, -53549.0390625), large=False, heli=True,
                airplanes=True, slot_name='109', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-16752.498046875, -53610.49609375), large=False, heli=True,
                airplanes=True, slot_name='108', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-16786.134765625, -53651.265625), large=False, heli=True,
                airplanes=True, slot_name='107', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-16673.2890625, -53679.98828125), large=False, heli=True,
                airplanes=True, slot_name='106', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-16637.556640625, -53637.48828125), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-16559.43359375, -53706.96484375), large=False, heli=True,
                airplanes=True, slot_name='103', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-16522.216796875, -53665.0859375), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-16455.0078125, -53732.2265625), large=False, heli=True,
                airplanes=True, slot_name='99', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-16386.693359375, -53681.63671875), large=False, heli=True,
                airplanes=True, slot_name='98', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-16303.830078125, -53723.234375), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-16139.215820313, -53706.2734375), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-16263.493164063, -53669.8203125), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-16110.779296875, -53652.99609375), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-16008.267578125, -53643.11328125), large=False, heli=True,
                airplanes=True, slot_name='89', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-15892.083007813, -53658.51171875), large=False, heli=True,
                airplanes=True, slot_name='84', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-15789.494140625, -53794.140625), large=False, heli=True,
                airplanes=True, slot_name='83', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-15714.548828125, -53896.33984375), large=False, heli=True,
                airplanes=True, slot_name='81', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-15674.037109375, -53988.1328125), large=False, heli=True,
                airplanes=True, slot_name='80', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-15804.512695313, -53856.78125), large=False, heli=True,
                airplanes=True, slot_name='82', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-15726.368164063, -54097.7890625), large=False, heli=True,
                airplanes=True, slot_name='79', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-15971.498046875, -53935.01171875), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-16027.420898438, -54086.30078125), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-15992.6640625, -53835.65234375), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-16054.048828125, -54018.81640625), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-16149.725585938, -54313.78125), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-16120.153320313, -54391.234375), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-16201.03125, -54494.71875), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-16183.944335938, -54610.84375), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-16261.133789063, -54701.5859375), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-15914.64453125, -54633.36328125), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-15931.873046875, -54696.7890625), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-16000.876953125, -54676.0703125), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-16028.017578125, -54743.8828125), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-16117.163085938, -54734.09375), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-16211.81640625, -54835.1796875), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-15795.741210938, -54606.796875), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-15769.395507813, -54719.52734375), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-15723.627929688, -54697.57421875), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-15681.915039063, -54808.4453125), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-15630.877929688, -54792.53125), large=False, heli=True,
                airplanes=True, slot_name='62', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-15623.0703125, -54869.3671875), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-15596.291015625, -54942.69921875), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-15655.248046875, -55020.32421875), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-15705.473632813, -55008.3671875), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-15718.486328125, -55104.3671875), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-15777.911132813, -55105.48828125), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-15822.833007813, -55227.52734375), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-15933.588867188, -55169.1484375), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-15925.166015625, -55110.2734375), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-16023.131835938, -55090.18359375), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-16010.935546875, -55035.97265625), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-16120.498046875, -54939.66796875), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-16341.719726563, -54749.56640625), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-16134.9140625, -54993.015625), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-16233.361328125, -54906.51171875), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-16324.620117188, -54827.58203125), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-16412.291015625, -54754.3671875), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-16479.880859375, -54696.234375), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-16476.26171875, -54636.1875), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-16584.130859375, -54578.2421875), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-16666.607421875, -54407.8828125), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-16709.921875, -54318.31640625), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-16748.45703125, -54177.6484375), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-16708.390625, -54139.7265625), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-16861.119140625, -54099.2265625), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-17005.7421875, -54058.671875), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-16895.994140625, -54037.984375), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-17079.923828125, -53953.79296875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-17158.5546875, -53871.328125), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-17258.25, -53838.3515625), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-17278.8203125, -53735.12890625), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-17260.72265625, -53730.9375), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-17242.7421875, -53726.578125), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-17152.638671875, -53555.58203125), large=False, heli=True,
                airplanes=True, slot_name='116', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-17158.3046875, -53537.8828125), large=False, heli=True,
                airplanes=True, slot_name='115', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-17163.9375, -53520.17578125), large=False, heli=True,
                airplanes=True, slot_name='114', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-17169.751953125, -53502.609375), large=False, heli=True,
                airplanes=True, slot_name='113', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-15758.708007813, -54239.625), large=False, heli=True,
                airplanes=True, slot_name='77', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-15794.997070313, -54245.63671875), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-15740.494140625, -54237.04296875), large=False, heli=True,
                airplanes=True, slot_name='78', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-15776.756835938, -54242.74609375), large=False, heli=True,
                airplanes=True, slot_name='76', length=16.0, width=16.0, height=6.0, shelter=False))


class Deux_Jumeaux(Airport):
    id = 12
    name = "Deux Jumeaux"
    position = mapping.Point(-16784.448242, -48871.496094)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Deux_Jumeaux, self).__init__()

        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-16293.255859375, -48417.40234375), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-16282.234375, -48455.4921875), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-16270.723632813, -48493.8984375), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-16658.90625, -49620.28515625), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-16648.599609375, -49604.79296875), large=False, heli=True,
                airplanes=True, slot_name='98', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-16354.609375, -49555.421875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-16349.532226563, -49637.859375), large=False, heli=True,
                airplanes=True, slot_name='106', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-16406.048828125, -49603.85546875), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-16432.744140625, -49660.66796875), large=False, heli=True,
                airplanes=True, slot_name='104', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-16531.4765625, -49571.76953125), large=False, heli=True,
                airplanes=True, slot_name='99', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-16514.380859375, -49578.84375), large=False, heli=True,
                airplanes=True, slot_name='100', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-16497.287109375, -49586.13671875), large=False, heli=True,
                airplanes=True, slot_name='101', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-16480.197265625, -49593.41015625), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-16463.14453125, -49600.67578125), large=False, heli=True,
                airplanes=True, slot_name='103', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-16352.766601563, -49500.05078125), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-16308.0703125, -49577.16015625), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-16303.395507813, -49463.12109375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-16299.439453125, -49373.93359375), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-16292.530273438, -49229.1953125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-16343.53125, -49295.99609375), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-16287.10546875, -49135.73046875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-16283.921875, -49056.0625), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-16278.91796875, -48952.46484375), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-16333.291015625, -49085.6484375), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-16329.033203125, -48992.03125), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-16323.532226563, -48866.50390625), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-16271.005859375, -48810.74609375), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-16280.390625, -48536.4375), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-16318.211914063, -48580.4765625), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-16361.840820313, -48427.1953125), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-16322.625976563, -48390.8203125), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-16342.681640625, -48321.328125), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-16385.189453125, -48345.83984375), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-16397.126953125, -48276.7890625), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-16505.462890625, -48287.98828125), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-16579.3203125, -48250.9765625), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-16678.544921875, -48288.61328125), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-16620.384765625, -48319.1953125), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-16316.899414063, -48630.18359375), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-16529.078125, -48626.875), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-16885.779296875, -48705.09765625), large=False, heli=True,
                airplanes=True, slot_name='83', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-16699.5390625, -48662.92578125), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-16626.1484375, -48698.90234375), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-16734.740234375, -48720.75), large=False, heli=True,
                airplanes=True, slot_name='84', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-16911.642578125, -48762.3515625), large=False, heli=True,
                airplanes=True, slot_name='82', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-16980.2734375, -48755.6484375), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-16410.884765625, -49173.01171875), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-16528.8203125, -49195.6484375), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-16615.6484375, -49211.4609375), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-16374.63671875, -49215.953125), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-16430.197265625, -49228.51953125), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-16565.91015625, -49253.1015625), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-16774.92578125, -49244.20703125), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-16744.666015625, -49286.765625), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-16756.822265625, -49364.69921875), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-16721.998046875, -49469.1796875), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-16687.62890625, -49574.08984375), large=False, heli=True,
                airplanes=True, slot_name='95', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-16790.95703125, -49416.30078125), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-16755.474609375, -49520.81640625), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-16721.2265625, -49625.67578125), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-16459.369140625, -49108.5078125), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-16524.884765625, -49018.4453125), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-16497.7421875, -48890.21484375), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-16552.59375, -48862.0703125), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-16513.443359375, -48801.44140625), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-16577.294921875, -48591.80859375), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-16798.439453125, -49213.26953125), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-16808.57421875, -49146.7421875), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-16866.265625, -49093.31640625), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-16874.853515625, -49053.796875), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-16847.708984375, -48969.96484375), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-16883.748046875, -48873.9765625), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-16911.826171875, -48939.36328125), large=False, heli=True,
                airplanes=True, slot_name='70', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-16951.494140625, -48833.3984375), large=False, heli=True,
                airplanes=True, slot_name='72', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-16992.060546875, -48671.12890625), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-16951.58984375, -48602.14453125), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-17006.361328125, -48545.4609375), large=False, heli=True,
                airplanes=True, slot_name='76', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-16646.740234375, -48572.83203125), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-16664.58984375, -48456.64453125), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-16737.638671875, -48433.82421875), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-16718.697265625, -48371.3515625), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-16947.78125, -48475.7734375), large=False, heli=True,
                airplanes=True, slot_name='78', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-16964.701171875, -48468.84765625), large=False, heli=True,
                airplanes=True, slot_name='77', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-16799.900390625, -48399.6953125), large=False, heli=True,
                airplanes=True, slot_name='81', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-16813.556640625, -48412.79296875), large=False, heli=True,
                airplanes=True, slot_name='80', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-16826.8359375, -48425.71484375), large=False, heli=True,
                airplanes=True, slot_name='79', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-16608.15234375, -48514.71484375), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-16628.984375, -48480.06640625), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-16584.869140625, -48547.328125), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-16487.88671875, -48844.7421875), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-16471.427734375, -48937.015625), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-16462.33984375, -48982.9921875), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-16454.626953125, -49029.05078125), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-16447.1015625, -49074.9609375), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-16362.614257813, -49354.015625), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-16364.236328125, -49400.04296875), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-16367.515625, -49446.78515625), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-16751.185546875, -49599.375), large=False, heli=False,
                airplanes=True, slot_name='94', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-16764.0625, -49560.30078125), large=False, heli=False,
                airplanes=True, slot_name='93', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-16785.099609375, -49494.2734375), large=False, heli=False,
                airplanes=True, slot_name='90', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-16797.408203125, -49455.4609375), large=False, heli=False,
                airplanes=True, slot_name='89', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-16866.474609375, -49213.26171875), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-16872.404296875, -49171.25390625), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-16877.357421875, -49129.58984375), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-16899.203125, -49023.30078125), large=False, heli=False,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-16915.587890625, -48978.65234375), large=False, heli=False,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=7.0, shelter=False))


class Chippelle(Airport):
    id = 13
    name = "Chippelle"
    position = mapping.Point(-28484.011719, -47891.75)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Chippelle, self).__init__()

        self.runways.append(Runway(240))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-27995.6875, -47895.3359375), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-27973.552734375, -47983.5390625), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-27959.81640625, -48073.33984375), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-27962.666015625, -47073.28125), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-27971.533203125, -47089.2734375), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-27980.431640625, -47105.703125), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-27989.498046875, -47121.671875), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-27998.423828125, -47137.8828125), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-28007.546875, -47154.0703125), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-28016.677734375, -47170.2578125), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-28025.763671875, -47186.2421875), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-28352.4375, -48438.46875), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-28320.48046875, -48429.46875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-28163.1328125, -48399.45703125), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-28129.833984375, -48398.9140625), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-27805.580078125, -47574.76171875), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-27773.833984375, -47524.2265625), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-27755.712890625, -47484.1953125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-27696.97265625, -47242.69140625), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-27717.705078125, -47202.5390625), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-27739.095703125, -47163.59375), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-28896.05859375, -47632.703125), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-28883.548828125, -47687.8515625), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-28870.4296875, -47743.6171875), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-28858.521484375, -47800.1171875), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-28975.806640625, -48118.0703125), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-28978.978515625, -48189.9375), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-28983.876953125, -48264.3984375), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-29006.0546875, -48346.3671875), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-29043.02734375, -48431.6953125), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-28095.26953125, -47146.3203125), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-28086.189453125, -47130.43359375), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-28077.08984375, -47114.125), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-28067.8203125, -47098.27734375), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-28058.701171875, -47082.17578125), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-28049.359375, -47066.10546875), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-28040.0390625, -47050.03515625), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-28030.740234375, -47034.16015625), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))


class Beuzeville(Airport):
    id = 14
    name = "Beuzeville"
    position = mapping.Point(-9213.708321, -72131.675455)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Beuzeville, self).__init__()

        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-9549.2371128719, -72743.202755871), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-9525.7830145649, -72749.92337805), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-8840.433696951, -72002.399976129), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-8873.6436439827, -72040.663541772), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-8969.4557823461, -71608.056965579), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-9001.412918534, -71643.432447979), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-9032.5198800264, -71678.077970203), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-9127.8546687363, -71778.728729793), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-9156.7521487452, -71811.634277487), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-9755.9261008704, -72561.004226378), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-9792.3576487029, -72563.908011363), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-8687.6023167638, -71690.318635498), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-8669.0404678861, -71690.169369297), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-8650.5332512783, -71689.711128952), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-8632.0775919186, -71689.466558893), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-8860.1156956263, -71478.991441075), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-8836.6006874024, -71578.605364839), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-8859.0806163038, -71497.751248665), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-8857.8338419296, -71516.247983147), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-9556.6817989323, -72720.691482349), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-9564.7540722959, -72668.103804183), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-9025.3471569783, -72224.373583967), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-8997.8093401864, -72191.687500426), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-9066.907608551, -72264.060043339), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-9098.0037873245, -72298.832740668), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-9200.2110714676, -72418.536901398), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-9233.308509396, -72457.295020326), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-9128.791702767, -72332.532934654), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-9171.2996548613, -72387.04981122), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-9364.3667604144, -72605.095733485), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-9394.7026873702, -72640.840351674), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-9265.5648999977, -72490.139731522), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-9334.6947025213, -72571.590497961), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-8933.0675495665, -72118.036237151), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-8966.1586209655, -72156.789724001), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-8904.1455170346, -72086.552208416), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))


class Azeville(Airport):
    id = 15
    name = "Azeville"
    position = mapping.Point(-2528.950195, -73675.082031)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Azeville, self).__init__()

        self.runways.append(Runway(250))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-2123.7131347656, -73153.453125), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-2081.9501953125, -73177.0390625), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-2040.4594726563, -73200.3046875), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-2012.9418945313, -73986.0625), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-2035.3203125, -74028.953125), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-2056.7839355469, -74071.578125), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-2106.0627441406, -73798.078125), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-2065.8771972656, -73822.609375), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-2212.58984375, -74123.0859375), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-2255.6872558594, -74098.9921875), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-2297.3012695313, -74074.2578125), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-2629.3388671875, -73137.828125), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-2652.0964355469, -73188.8671875), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-2673.8247070313, -73237.375), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-2764.1257324219, -73455.265625), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-2778.4426269531, -73504.078125), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-2788.1728515625, -73557.7734375), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-2445.6650390625, -73047.671875), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-2436.5981445313, -73063.890625), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-2427.4140625, -73079.953125), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-2418.4819335938, -73096.0078125), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-2802.3271484375, -74166.1484375), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-2820.349609375, -74172.1875), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-2838.0317382813, -74177.7578125), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-2605.4279785156, -74259.2265625), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-2614.9304199219, -74243.5), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-2624.9028320313, -74227.703125), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-2634.4953613281, -74212.1328125), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-2244.7939453125, -73155.4296875), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-2227.5087890625, -73148.7890625), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-2210.3583984375, -73141.78125), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))


class Picauville(Airport):
    id = 16
    name = "Picauville"
    position = mapping.Point(-12078.898926, -80241.097656)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Picauville, self).__init__()

        self.runways.append(Runway(290))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-11705.821289063, -80830.46875), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-11688.598632813, -80813.1875), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-11917.751953125, -79818.453125), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-11900.314453125, -79866.0234375), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-12441.276045877, -79710.022448305), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-12423.750910831, -79756.439806962), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-12404.504130258, -79805.557642941), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-12167.399414063, -80484.1875), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-12149.485351563, -80531.8984375), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-12008.892578125, -80901.1796875), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-12024.680664063, -80935.3203125), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-12210.875976563, -79567.1796875), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-12202.032226563, -79550.859375), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-12193.485351563, -79534.4375), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-12184.776367188, -79518.1640625), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-12479.26953125, -79616.015625), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-12380.703125, -79643.59375), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-12462.34765625, -79624.1796875), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-12445.553710938, -79632.03125), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-11729.125976563, -80826.1015625), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-11779.061523438, -80807.7421875), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-11897.059570313, -80148.6640625), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-11914.984375, -80100.953125), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-11883.475585938, -80189.1953125), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-11865.546875, -80236.8984375), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-11821.268554688, -80367.9765625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-11803.34375, -80415.6875), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-11852.78125, -80279.7421875), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-11834.852539063, -80327.4453125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-11757.323242188, -80552.0625), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-11739.396484375, -80599.78125), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-11788.8359375, -80463.828125), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-11770.909179688, -80511.5234375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-11948.153320313, -80008.671875), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-11930.229492188, -80056.375), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-11961.729492188, -79968.1328125), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))


class Le_Molay(Airport):
    id = 17
    name = "Le Molay"
    position = mapping.Point(-26123.464844, -41403.646484)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Le_Molay, self).__init__()

        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-25710.234375, -40841.69921875), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-25728.570386257, -40836.218305422), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-26573.366872787, -41502.122958808), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-26539.770757123, -41472.023371614), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-26430.628065989, -41885.641688014), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-26391.807753489, -41850.551844264), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-26354.493300364, -41816.047938014), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-26326.231749006, -41789.100753942), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-26288.302061506, -41755.049972692), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-25530.654057203, -41081.604719417), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-25493.111088453, -41083.889875667), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-26703.17578125, -41771.78125), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-26721.59375, -41769.48046875), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-26740.001953125, -41767.4921875), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-26758.326171875, -41765.30078125), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-26506.125038148, -41988.894540288), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-26572.024283216, -41902.315011883), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-26506.897335978, -41951.071161524), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-26456.679306329, -41909.747811724), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-25705.8203125, -40864.9921875), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-25704.75390625, -40918.19140625), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-26323.022490338, -41326.574364352), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-26360.940459088, -41360.621239352), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-26290.206084088, -41299.172020602), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-26252.293974713, -41265.105614352), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-26113.732890439, -41133.475159372), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-26066.966568244, -41090.416685048), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-26184.451640439, -41194.928284372), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-26147.996457636, -41165.047612331), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-25927.123391165, -40981.625870483), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-25835.392004404, -40913.864222727), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-26007.225154784, -41048.61795056), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-25967.173183639, -41015.960096668), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-26434.833037213, -41425.101708102), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-26396.911162213, -41391.050926852), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-26501.862918516, -41442.653566536), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))


class Longues_sur_Mer(Airport):
    id = 18
    name = "Longues-sur-Mer"
    position = mapping.Point(-16733.196289, -28909.375977)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Longues_sur_Mer, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-16807.962890625, -28363.375), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-16807.560546875, -28381.953125), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-16807.03125, -28400.830078125), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-16806.25390625, -28438.42578125), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-16930.123046875, -28211.51171875), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-16920.40625, -28227.01171875), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-16910.3125, -28242.736328125), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-16900.71484375, -28258.3828125), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-16890.833984375, -28274.029296875), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-16939.623046875, -28195.556640625), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-16949.123046875, -28179.33203125), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-16807.369140625, -28419.271484375), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-16805.587890625, -28475.853515625), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-16805.181640625, -28494.427734375), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-16804.646484375, -28513.302734375), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-16806.193359375, -28457.3515625), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-16803.90625, -28551.12890625), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-16804.998046875, -28531.74609375), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-16692.044921875, -28369.626953125), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-16776.28515625, -28436.703125), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-16747.720703125, -28171.970703125), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-17123.638671875, -28505.7578125), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-17105.720703125, -28509.447265625), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-17087.390625, -28513.02734375), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-17069.439453125, -28516.912109375), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-17051.3046875, -28520.59375), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-16893.796875, -29078.78125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-16801.8671875, -29157.962890625), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-16926.353515625, -29296.88671875), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-17134.45703125, -29145.544921875), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-17208.533203125, -29217.60546875), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-17219.412109375, -29309.48828125), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-17224.39453125, -28715.630859375), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-17024.671875, -29481.23046875), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-16978.853515625, -29471.9140625), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-16931.41796875, -29464.322265625), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-17135.447265625, -28976.498046875), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-17144.453125, -28927.85546875), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-17151.802734375, -28878.380859375), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-17168.888671875, -28779.4375), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-17176.681640625, -28738.08984375), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-16677.41015625, -28404.736328125), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-16657.23046875, -28443.82421875), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-16942.953125, -29224.666015625), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-17015.8125, -29212.169921875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-17024.232421875, -29148.724609375), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))


class Carpiquet(Airport):
    id = 19
    name = "Carpiquet"
    position = mapping.Point(-34782.396484, -9983.634766)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Carpiquet, self).__init__()

        self.runways.append(Runway(120))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-34197.03515625, -9833.6513671875), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-34212.44140625, -9804.1455078125), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-34134.3671875, -9956.640625), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-34149.7734375, -9927.1357421875), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-34069.6484375, -10074.700195313), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-34085.0546875, -10045.1953125), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-34017.34375, -10166.115234375), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-34001.8671875, -10196.345703125), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-34087.314132154, -10191.047501569), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-35223.62109375, -10048.220703125), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-35225.9921875, -10014.627929688), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-35212.45703125, -10184.047851563), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-35214.8359375, -10150.447265625), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-35202.72265625, -10321.732421875), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-35205.28125, -10287.767578125), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-34094.51953125, -9752.546875), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-33980.7890625, -9794.8310546875), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-33994.0078125, -9714.791015625), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-33947.72265625, -9616.6376953125), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-33908.58984375, -9757.107421875), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-33913.14453125, -9545.3740234375), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-33992.75, -9505.3828125), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-34080.3046875, -9445.015625), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-34298.2734375, -9760.3505859375), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-35416.671875, -10415.975585938), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-35409.21875, -10273.341796875), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-35403.3828125, -10136.973632813), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-34814.234375, -10790.25390625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-34754.29296875, -10794.409179688), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-35191.609375, -10458.305664063), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-35194.97265625, -10423.762695313), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-34296.46875, -9837.23828125), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-34270.0390625, -9886.0361328125), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-34287.34375, -9853.5361328125), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-34278.56640625, -9869.58984375), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-34229.359375, -9956.1015625), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-34202.9296875, -10004.895507813), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-34220.234375, -9972.3955078125), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-34211.45703125, -9988.453125), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-34060.880538404, -10240.125626569), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-34078.345382154, -10207.716446882), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-34069.728194654, -10224.117814069), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-34132.796875, -10122.698242188), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-34159.2265625, -10073.899414063), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-34150.09765625, -10090.197265625), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-34141.33203125, -10106.25390625), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-34694.890625, -10798.870117188), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))


class Bazenville(Airport):
    id = 20
    name = "Bazenville"
    position = mapping.Point(-20712.899414, -18498.402344)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Bazenville, self).__init__()

        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-20335.234375, -18316.857421875), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-20377.361328125, -18364.02734375), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-20772.580078125, -18210.572265625), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-20232.328125, -18036.72265625), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-20251.14453125, -18038.349609375), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-20288.55859375, -18041.60546875), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-20269.576171875, -18039.072265625), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-20390.791015625, -17800.55078125), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-20377.712890625, -17815.150390625), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-20403.771484375, -17786.548828125), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-20783.365234375, -18178.650390625), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-20763.3828125, -18237.361328125), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-20793.443359375, -18148.78515625), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-21005.6171875, -18443.46484375), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-21123.7421875, -18722.470703125), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-21025.310546875, -18592.7109375), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-21256.19140625, -18898.48046875), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-21390.876953125, -18569.59375), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-21296.03515625, -18453.11328125), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-21163.62890625, -18425.4453125), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-21025.4375, -18523.05078125), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-21286.15234375, -18517.451171875), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-21434.630859375, -18715.25), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-21404.08984375, -18926.802734375), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-21336.30859375, -18968.328125), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-21333.0546875, -18806.814453125), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-21329.564453125, -18746.94140625), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-21265.501953125, -18794.5546875), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-21135.96484375, -18822.828125), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-21050.67578125, -19086.5546875), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-21049.85546875, -19105.11328125), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-21048.91015625, -19123.978515625), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-21051.9453125, -19067.5078125), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-21247.4375, -18986.37109375), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-21229.001953125, -18985.681640625), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-21210.5, -18985.60546875), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-21192.05078125, -18984.431640625), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-21173.580078125, -18983.66796875), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-21155.0078125, -18983.361328125), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-20710.037109375, -18172.650390625), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-20631.10546875, -18066.431640625), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-20487.5625, -17876.705078125), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-20208.302734375, -18316.76953125), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-20752.998046875, -18720.3046875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-20799.13671875, -18809.6640625), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-20842.138671875, -18954.66015625), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-20922.423828125, -19034.49609375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-20621.189453125, -17747.060546875), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-20658.197265625, -17799.236328125), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-20956.408203125, -19134.3828125), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-20958.56640625, -19249.51953125), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-20899.78515625, -19300.826171875), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-20688.861328125, -18976.1015625), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-20748.201171875, -19039.2734375), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-20763.611328125, -19100.8046875), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-20674.0390625, -18873.73046875), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-20969.18359375, -18399.265625), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-20931.576171875, -18349.92578125), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-20879.84765625, -18277.759765625), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-20842.23828125, -18231.677734375), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))


class Sainte_Croix_sur_Mer(Airport):
    id = 21
    name = "Sainte-Croix-sur-Mer"
    position = mapping.Point(-18787.417239, -15106.744633)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sainte_Croix_sur_Mer, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-18935.797506538, -14425.181352241), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-18955.511437772, -14439.031926648), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-18974.197161471, -15448.867635729), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-18974.26685997, -15398.202103266), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-18627.901420484, -15635.443028885), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-18625.446984828, -15578.038079956), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-18624.606111946, -15530.53050971), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-18623.942170349, -15393.258895972), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-18624.077136593, -15346.543303123), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-18660.273262113, -14426.922800901), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-18634.698741977, -14400.814687899), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-18894.511294516, -15785.061840187), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-18908.414793946, -15797.360507503), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-18922.074238214, -15809.856372142), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-18935.835069109, -15822.157213982), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-18625.642936133, -15831.212190673), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-18706.996355159, -15769.622855667), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-18638.739748452, -15817.740914672), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-18651.823535069, -15804.60705916), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-18915.402945293, -14437.274435296), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-18874.789469465, -14471.642604775), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-18971.427683023, -15160.933043093), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-18970.741090512, -15203.667572476), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-18971.541400518, -15102.810529574), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-18970.913751285, -15056.165927846), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-18967.446331251, -14898.320173153), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-18967.925577219, -14847.35545493), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-18969.814518791, -15010.53271078), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-18968.58302001, -14941.052067526), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-18960.540161859, -14651.478445819), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-18959.621618603, -14603.097381752), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-18967.410678453, -14801.40347066), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-18960.925677996, -14696.232028966), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-18971.223915088, -15301.727630171), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-18971.704922417, -15250.770585699), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-18972.370621482, -15344.46418473), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))


class Beny_sur_Mer(Airport):
    id = 22
    name = "Beny-sur-Mer"
    position = mapping.Point(-21040.570313, -8437.482422)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Beny_sur_Mer, self).__init__()

        self.runways.append(Runway(170))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-20698.400390625, -8236.490234375), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-20759.39453125, -8227.58984375), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-20813.50390625, -8219.935546875), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-20881.3203125, -8210.1083984375), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-21031.484375, -8814.19140625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-20976.33203125, -8846.66796875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-20921.58203125, -8796.9970703125), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-20923.525390625, -8204.125), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-21368.75, -8089.3754882813), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-21444.09375, -8672.4375), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-21406.73046875, -8691.7880859375), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-21343.0078125, -8730.451171875), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-21297.421875, -8754.986328125), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-21252.34765625, -8778.4794921875), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-20885.06640625, -9083.87890625), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-20937.765625, -9082.919921875), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-20987.078125, -9081.455078125), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-21495.896484375, -8704.86328125), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-21025.19140625, -9066.9755859375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-21090.841796875, -9001.7724609375), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-21101.927734375, -8899.0302734375), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-20854.482421875, -8828.4404296875), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-20887.1484375, -8644.783203125), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-21006.1640625, -8668.3671875), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-21556.87109375, -8460.3544921875), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-21570.9921875, -8472.0986328125), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-21585.109375, -8484.32421875), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-21599.060546875, -8496.1630859375), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-21630.1953125, -7994.4057617188), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-21439.3359375, -8180.072265625), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-21509.98046875, -8070.0009765625), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-21382.193359375, -8261.265625), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-21366.26171875, -8272.353515625), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-21441.51171875, -8216.3515625), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-21396.501953125, -8249.6201171875), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-21411.693359375, -8238.40625), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-21426.572265625, -8227.2763671875), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-21472.224609375, -8193.802734375), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-21748.533203125, -8157.5395507813), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-21729.90234375, -8160.0571289063), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-21638.041015625, -8170.0068359375), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-21656.447265625, -8168.1430664063), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-21674.681640625, -8166.0581054688), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-21693.294921875, -8164.3134765625), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-21711.48828125, -8162.4111328125), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-21456.45703125, -8204.7333984375), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-21486.5390625, -8182.1708984375), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-21501.73046875, -8170.9536132813), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-21516.60546875, -8159.8193359375), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))


class Rucqueville(Airport):
    id = 23
    name = "Rucqueville"
    position = mapping.Point(-26589.313477, -19444.007813)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Rucqueville, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-26680.033203125, -20166.484375), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-26680.318359375, -20148.185546875), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-26680.7890625, -20129.515625), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-26680.90625, -20111.15234375), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-26681.240234375, -20092.650390625), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-26681.400390625, -20074.068359375), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-26681.5703125, -20055.486328125), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-26532.548742227, -18761.644249345), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-26532.369054727, -18779.987999345), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-26531.935460977, -18798.292686845), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-26531.312414102, -18816.597374345), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-26531.031164102, -18835.023155595), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-26426.551778491, -19064.36277261), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-26429.788106616, -19118.630350735), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-26433.262715991, -19171.50730386), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-26425.681147362, -19234.099614526), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-26429.030014925, -19276.537434649), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-26432.165091925, -19449.680094371), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-26435.75852053, -19493.251864466), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-26438.89167918, -19536.898076108), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-26448.663201849, -19811.302483006), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-26389.784123554, -19811.790194497), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-26323.667076539, -19810.377331253), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-26326.318216085, -20181.566246667), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-26388.137336106, -20181.054522865), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-26448.39529431, -20181.988278684), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-26466.771484375, -19996.744140625), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-26447.294921875, -19996.451171875), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-26427.91796875, -19996.013671875), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-26408.439453125, -19995.71875), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-26389.255859375, -19995.392578125), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-26369.77734375, -19995.103515625), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-26350.833984375, -19994.05859375), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-26331.498046875, -19993.724609375), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-26311.0703125, -19993.46875), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-26490.954992227, -18761.339561845), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-26490.771398477, -18779.683311845), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-26490.343664102, -18797.987999345), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-26489.728429727, -18816.292686845), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-26489.427648477, -18834.714561845), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))


class Sommervieu(Airport):
    id = 24
    name = "Sommervieu"
    position = mapping.Point(-21371.758789, -26206.679688)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sommervieu, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-21503.513671875, -25766.630859375), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-21186.708984375, -26337.33203125), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-21249.21484375, -26889.314453125), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-21497.822265625, -25668.73828125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-21499, -25717.818359375), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-21491.11328125, -25573.759765625), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-21189.107421875, -26383.232421875), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-21191.4453125, -26430.79296875), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-21203.11328125, -26565.4375), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-21207.599609375, -26617.955078125), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-21212.037109375, -26671.822265625), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-21220.759765625, -25535.435546875), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-21206.08203125, -25524.125), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-21191.595703125, -25512.58984375), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-21177.056640625, -25501.234375), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-21476.947265625, -25475.115234375), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-21407.296875, -25538.701171875), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-21464.1328125, -25488.689453125), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-21573.826171875, -26910.24609375), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-21546.328125, -26885.369140625), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-21560.177734375, -26897.7421875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-21293.14453125, -26886.78515625), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-21330.662109375, -26850.51171875), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-21268.29296875, -26898.4296875), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))


class Lantheuil(Airport):
    id = 25
    name = "Lantheuil"
    position = mapping.Point(-24264.160156, -16467.212402)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lantheuil, self).__init__()

        self.runways.append(Runway(240))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-24663.552734375, -16906.71875), large=False, heli=True,
                airplanes=True, slot_name='72', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-24647.7890625, -16916.2265625), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-24631.693359375, -16925.703125), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-24615.9765625, -16934.541015625), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-24470.34765625, -17017.083984375), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-24454.625, -17025.931640625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-24438.8984375, -17035.41796875), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-24384.876953125, -17095.078125), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-24496.875, -17132.98828125), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-24475.224609375, -17232.46875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-24653.60546875, -17477.984375), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-24409.47265625, -16983.439453125), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-24283.244140625, -16997.78515625), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-24338.453125, -16882.359375), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-24231.240234375, -16875.96875), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-24107.36328125, -16614.99609375), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-24204.287109375, -16632.62109375), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-24161.091796875, -16502.79296875), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-24040.953125, -16478.146484375), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-23691.98046875, -16509.95703125), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-23415.4765625, -16464.2734375), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-23535.109375, -16176.109375), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-24617.4140625, -16845.037109375), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-24629.162109375, -16737.638671875), large=False, heli=True,
                airplanes=True, slot_name='70', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-24533.12109375, -16698.734375), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-24707.142578125, -16403.763671875), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-24633.591796875, -16266.357421875), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-24566.673828125, -16136.291015625), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-24464.2265625, -15915.408203125), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-24388.7109375, -15793.330078125), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-24322.92578125, -15651.119140625), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-24353.671875, -15576.958007813), large=False, heli=True,
                airplanes=True, slot_name='Stand03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-24283.392578125, -15429.709960938), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-24209.513671875, -15349.244140625), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-24095.677734375, -15475.010742188), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-24162.7890625, -15644.055664063), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-24281.287109375, -16074.471679688), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-24354.265625, -16243.137695313), large=False, heli=True,
                airplanes=True, slot_name='62', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-24241.630859375, -16178.12109375), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-24166.390625, -16049.4140625), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-24284.19921875, -16312.561523438), large=False, heli=True,
                airplanes=True, slot_name='61', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-24643.9453125, -15412.844726563), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-24048.427734375, -15879.088867188), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-24050.986328125, -15860.905273438), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-24045.3671875, -15896.866210938), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-24042.5625, -15915.327148438), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-23892.515625, -16002.810546875), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-23874.03125, -15998.43359375), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-23855.80078125, -15994.41796875), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-23837.783203125, -15990.6484375), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-23819.765625, -15987.193359375), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-24066.755859375, -15779.571289063), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-24063.955078125, -15798.026367188), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-24365.591796875, -16468.89453125), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-24349.80078125, -16477.61328125), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-23492.82421875, -16352.380859375), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-23506.751953125, -16302.108398438), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-23561.73828125, -16104.012695313), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-23572.306640625, -16055.453125), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-23584.37890625, -16005.393554688), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-24289.115234375, -16945.453125), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-24263.6796875, -16901.72265625), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-24452.333984375, -15557.690429688), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-24427.677734375, -15512.467773438), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-24403.439453125, -15470.97265625), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-24377.525390625, -15428.096679688), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))


class Evreux(Airport):
    id = 26
    name = "Evreux"
    position = mapping.Point(-45898.339844, 112233.769531)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Evreux, self).__init__()

        self.runways.append(Runway(160))
        self.runways.append(Runway(30))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-46294.65234375, 112935.03125), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-46247.6796875, 112961.9921875), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-46084.17578125, 113050.125), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-46036.52734375, 113076.46875), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-45987.94921875, 113100.7421875), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-44986.59375, 112609.53125), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-44992.4921875, 112555.34375), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-46745.3359375, 111867.9375), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-46699.2421875, 111834.890625), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-46652.8046875, 111806.25), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-46350.63671875, 112760.375), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-45121.30078125, 112111.5234375), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-45126.21484375, 112093.875), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-45136.546875, 112236.3515625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-45115.94140625, 112148.625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-45116.5234375, 112129.5546875), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-45053.62890625, 112292.734375), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-46397.5234375, 112725.5703125), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-45058.38671875, 112258.2890625), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-45320.82421875, 112904.8046875), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-45346.4140625, 112905.4375), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-45373.71484375, 112907.3203125), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-46437.4140625, 112687.0703125), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-46481.66015625, 112655.5234375), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))


class Chailey(Airport):
    id = 27
    name = "Chailey"
    position = mapping.Point(163729.554688, 11866.79248)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Chailey, self).__init__()

        self.runways.append(Runway(170))
        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(163935.828125, 12154.985351562), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(164233.171875, 12507.352539063), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(164146.03125, 12423.440429688), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(163911.859375, 12122.442382812), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(163734.21875, 12050.0703125), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(163517.96875, 12070.427734375), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(163876.15625, 11548.159179687), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(163843.53125, 11568.692382812), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(164475.046875, 12186.220703125), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(164549.125, 12339.038085937), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(164572.203125, 12383.532226562), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(163940.03125, 11522.202148438), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(163929.859375, 11506.55078125), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(163899.03125, 11460.458984375), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(163909.375, 11475.895507812), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(163919.5625, 11491.345703125), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(163681.484375, 11608.47265625), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(163034.21875, 12052.96484375), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(163036.40625, 12071.107421875), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(162998.9375, 11811.239257812), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(163001.34375, 11829.653320312), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(163003.46875, 11848.056640625), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(163005.78125, 11866.276367187), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(163007.84375, 11884.825195313), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(164720.75, 12599.767578125), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(164371.421875, 12192.779296875), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(164421.15625, 12301.758789063), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(164475.75, 12420.885742188), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(164558.21875, 12514.727539063), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(163211.28125, 12117.11328125), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(163349.8125, 12113.37109375), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(163379.796875, 12010.55859375), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(163490.375, 11974.3984375), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(163739.140625, 11952.001953125), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(163876.453125, 11961.602539062), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(163460.390625, 12075.318359375), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(163568.046875, 12040.21484375), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(163672.515625, 12034.083984375), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(163792.53125, 12043.546875), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(163897.28125, 12085.333984375), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(164004.234375, 12082.552734375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(164066.875, 12169.396484375), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(163964.15625, 12178.965820312), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(164141.46875, 12273.471679687), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(164033.4375, 12276.400390625), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(164103.578125, 12370.510742188), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(164209.8125, 12357.971679687), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(164297.5, 12438.063476563), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(164195.390625, 12464.029296875), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(164281.796875, 12543.676757813), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(164347.96875, 12634.852539063), large=False, heli=True,
                airplanes=True, slot_name='15', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(164396.0625, 12738.103515625), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(164447.375, 12636.295898438), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(164491.171875, 12740.1171875), large=False, heli=True,
                airplanes=True, slot_name='10', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(164557, 12790.516601563), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(164423.515625, 12803.815429688), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(164409.953125, 12769.400390625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))


class Needs_Oar_Point(Airport):
    id = 28
    name = "Needs Oar Point"
    position = mapping.Point(141296.390625, -84372.234375)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Needs_Oar_Point, self).__init__()

        self.runways.append(Runway(340))
        self.runways.append(Runway(50))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(141049.53125, -84626.5390625), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(140703, -84930.71875), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(140801.703125, -84860.6875), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(141078.078125, -84597.890625), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(141264.5, -84552.8125), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(141475.3125, -84605.125), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(141199.09375, -84035.6875), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(141228.25, -84060.53125), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(140511.65625, -84577.1953125), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(140415.65625, -84717.234375), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(140386.1875, -84757.7890625), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(141139.484375, -84000.1640625), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(141151.921875, -83986.1875), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(141189.296875, -83945.2421875), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(141176.75, -83958.953125), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(141164.359375, -83972.6953125), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(141382.375, -84123.984375), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(141956.21875, -84659.8203125), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(141951.40625, -84677.4296875), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(142027.140625, -84426.0703125), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(142022.015625, -84443.9453125), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(142017.1875, -84461.7890625), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(142012.171875, -84479.46875), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(142007.359375, -84497.4765625), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(140207.15625, -84949.5), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(140613.140625, -84599.09375), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(140547.75, -84699.4375), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(140476.03125, -84809.109375), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(140380.515625, -84889.578125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(141771.625, -84696.90625), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(141635.21875, -84672.625), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(141620.84375, -84566.484375), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(141516.90625, -84514.2734375), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(141274.265625, -84455.109375), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(141137, -84444.140625), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(141531.53125, -84618.484375), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(141430.3125, -84567.765625), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(141327.875, -84546.140625), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(141207.796875, -84537.65625), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(141098, -84563.359375), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(140992.671875, -84544.734375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(140917.8125, -84621.2734375), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(141017.9375, -84645.9921875), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(140828.546875, -84713.1171875), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(140934.90625, -84732.046875), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(140851.546875, -84814.671875), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(140748.375, -84786.4921875), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(140649.75, -84852.6484375), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(140746.84375, -84893.4765625), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(140649.546875, -84959.3828125), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(140570.5625, -85039.703125), large=False, heli=True,
                airplanes=True, slot_name='15', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(140507.609375, -85134.6328125), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(140472.015625, -85026.328125), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(140413.25, -85122.4453125), large=False, heli=True,
                airplanes=True, slot_name='10', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(140340.65625, -85162.5390625), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(140470.65625, -85195.515625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(140489.21875, -85163.5078125), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))


class Funtington(Airport):
    id = 29
    name = "Funtington"
    position = mapping.Point(152367.835938, -45975.689453)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Funtington, self).__init__()

        self.runways.append(Runway(190))
        self.runways.append(Runway(250))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(152473.796875, -45637.49609375), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(152646.328125, -45209.890625), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(152589.671875, -45316.84375), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(152461.1875, -45675.89453125), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(152315.03125, -45800.109375), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(152103.265625, -45848.26171875), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(152606.5625, -46232.6171875), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(152976.3125, -45439.4453125), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(152998.96875, -45271.16015625), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(153007.046875, -45221.671875), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(152675.375, -46237.30859375), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(152670.609375, -46255.37890625), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(152655.671875, -46308.76953125), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(152660.6875, -46290.90234375), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(152665.578125, -46273.03515625), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(152402.796875, -46236.08203125), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(151649.140625, -46015.9296875), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(151645.5625, -45998), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(151691.09375, -46256.55859375), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(151687.59375, -46238.3046875), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(151683.890625, -46220.18359375), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(151680.40625, -46202.15234375), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(151676.578125, -46183.90234375), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(153080.640625, -44969.90625), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(152875.828125, -45465.578125), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(152889.0625, -45346.54296875), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(152903.703125, -45216.3046875), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(152952.765625, -45101.453125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(151797.328125, -45899.69140625), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(151930.09375, -45859.96875), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(151990.703125, -45948.3125), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(152107.03125, -45948.11328125), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(152350.296875, -45891.7265625), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(152477.765625, -45839.734375), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(152047.03125, -45861.640625), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(152160.234375, -45861.3671875), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(152261.4375, -45834.5703125), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(152372.46875, -45788.09375), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(152458.9375, -45715.703125), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(152561.4375, -45684.9921875), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(152593.8125, -45582.89453125), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(152493.234375, -45605.8828125), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(152632.15625, -45460.7265625), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(152528.640625, -45491.65625), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(152565.890625, -45380.375), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(152670.71875, -45359.11328125), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(152729.015625, -45255.63671875), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(152623.921875, -45262.8984375), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(152681.09375, -45160.20703125), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(152715.53125, -45052.94140625), large=False, heli=True,
                airplanes=True, slot_name='15', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(152728.984375, -44939.82421875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(152809.515625, -45020.53515625), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(152818.734375, -44908.25390625), large=False, heli=True,
                airplanes=True, slot_name='10', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(152865.53125, -44839.79296875), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(152734.578125, -44868.84765625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(152732.40625, -44905.75390625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))


class Tangmere(Airport):
    id = 30
    name = "Tangmere"
    position = mapping.Point(150158.65625, -33957.914063)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tangmere, self).__init__()

        self.runways.append(Runway(290))
        self.runways.append(Runway(60))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(149939.671875, -33095.33984375), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(149948.84375, -33069.546875), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(149956.359375, -33045.06640625), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(150649.671875, -32966.5078125), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(150617.78125, -32952.65625), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(150757.96875, -33057.1953125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(150739.765625, -33051.48828125), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(150649.734375, -33047.71484375), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(150789.71875, -33076.13671875), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(150774.046875, -33066.66015625), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(150656.828125, -34625.33203125), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(150615.34375, -34660.78125), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(150574.03125, -34696.14453125), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(150381.328125, -32823.0390625), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(150330.75, -32802.7265625), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(149587.9375, -33634.7421875), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(149598.21875, -33688.078125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(149610.75, -33741.0703125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(149648.15625, -33922.4140625), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(149659.515625, -33975.6953125), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))


class Ford_AF(Airport):
    id = 31
    name = "Ford_AF"
    position = mapping.Point(147498.585938, -25722.724609)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Ford_AF, self).__init__()

        self.runways.append(Runway(270))
        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(147609.515625, -24839.732421875), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(147627.484375, -24819.0625), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(147643.390625, -24799.025390625), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(148317.5625, -24978.9296875), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(148292.90625, -24954.373046875), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(148385.265625, -25102.876953125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(148370.40625, -25090.916015625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(148287.96875, -25054.529296875), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(148407.9375, -25132.09765625), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(148396.8125, -25117.541015625), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(147718.78125, -26525.919921875), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(147667.234375, -26543.78515625), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(147615.859375, -26561.64453125), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(148120.09375, -24747.404296875), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(148080.40625, -24710.046875), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(147085.15625, -25213.5546875), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(147075.28125, -25266.953125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(147067.59375, -25320.849609375), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(147036.234375, -25503.3671875), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(147027.359375, -25557.1171875), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))


class Argentan(Airport):
    id = 32
    name = "Argentan"
    position = mapping.Point(-78808.039063, 22665.379883)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Argentan, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-78984.9453125, 23166.23046875), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-78976.5390625, 23149.994140625), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-78967.8125, 23133.4765625), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-78959.5390625, 23117.064453125), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-78951.0234375, 23100.654296875), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-78942.7265625, 23084.06640625), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-78696.5, 22250.4296875), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-78935.6875, 23066.953125), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-79027.3203125, 22829.88671875), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-79035.8203125, 22846.068359375), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-79044.71875, 22862.521484375), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-79053.1015625, 22878.84765625), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-79061.765625, 22895.193359375), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-79070.28125, 22911.47265625), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-79078.2265625, 22928.205078125), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-79087.015625, 22944.654296875), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-79095.421875, 22960.9765625), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-79104.09375, 22977.30859375), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-79112.8984375, 22993.994140625), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-78817.9609375, 22287.451171875), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-78837.6953125, 22335.0390625), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-78965.734375, 22635.462890625), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-78983.4296875, 22683.083984375), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-79003.0703125, 22730.541015625), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-79023.0859375, 22777.0234375), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-78684.09375, 22224.99609375), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-78672.3125, 22200.0234375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-78660.2890625, 22175.509765625), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-78629.296875, 22192.763671875), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-78641.609375, 22218.23046875), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-78653.328125, 22243.2578125), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-78665.2421875, 22267.8203125), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Goulet(Airport):
    id = 33
    name = "Goulet"
    position = mapping.Point(-81156.757813, 16794.293945)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Goulet, self).__init__()

        self.runways.append(Runway(30))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-81659.4765625, 16622.775390625), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-81643.1484375, 16630.994140625), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-81626.5390625, 16639.55078125), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-81610.046875, 16647.634765625), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-81593.5234375, 16655.99609375), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-81576.8671875, 16664.10546875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-80740.625, 16901.3828125), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-81559.6796875, 16670.970703125), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-81323.609375, 16576.791015625), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-81339.875, 16568.44921875), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-81356.4296875, 16559.748046875), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-81372.84375, 16551.53125), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-81389.2734375, 16543.04296875), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-81405.65625, 16534.697265625), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-81422.46875, 16526.93359375), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-81439.0078125, 16518.322265625), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-81455.4296875, 16510.09765625), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-81471.8515625, 16501.595703125), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-81488.625, 16492.970703125), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-80778.9375, 16780.33203125), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-80826.7421875, 16761.1015625), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-81128.53125, 16636.283203125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-81176.34375, 16619.111328125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-81224, 16599.98046875), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-81270.6875, 16580.47265625), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-80715.078125, 16913.501953125), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-80689.96875, 16925.048828125), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-80665.328125, 16936.802734375), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-80682.2578125, 16967.955078125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-80707.8515625, 16955.9296875), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-80733.0078125, 16944.470703125), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-80757.703125, 16932.80859375), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Barville(Airport):
    id = 34
    name = "Barville"
    position = mapping.Point(-109934.785156, 49091.339844)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Barville, self).__init__()

        self.runways.append(Runway(100))
        self.runways.append(Runway(330))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-109506.859375, 49616.75390625), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-109469.828125, 49587.37890625), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-109350.109375, 49487.39453125), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-109314.2890625, 49457.921875), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-109280.5234375, 49426.16015625), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-109354.359375, 48494.078125), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-109397.5859375, 48480.06640625), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-110485.5859375, 49643.37890625), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-110497.359375, 49595.41015625), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-110505.2890625, 49549.78515625), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-109581.984375, 48438.61328125), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-109790.92840192, 48434.840190324), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-109812.64715192, 48433.148784074), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-109768.94402692, 48437.781596574), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-109636.859375, 48423.1015625), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-109677.578125, 49708.35546875), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-109627.6640625, 49682.44921875), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))


class Essay(Airport):
    id = 35
    name = "Essay"
    position = mapping.Point(-105527.957031, 45008.003906)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Essay, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-105499.4375, 45538.40234375), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-105497.90625, 45520.19140625), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-105496.171875, 45501.5859375), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-105494.8203125, 45483.2734375), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-105493.234375, 45464.828125), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-105491.9375, 45446.34375), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-105583.9375, 44581.9765625), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-105491.984375, 45427.83203125), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-105667.46875, 45243.9765625), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-105669.1328125, 45262.1875), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-105671.03125, 45280.78125), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-105672.53125, 45299.0859375), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-105674.2578125, 45317.5), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-105675.890625, 45335.80859375), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-105676.8203125, 45354.3046875), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-105678.6328125, 45372.86328125), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-105680.1328125, 45391.1640625), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-105681.8984375, 45409.58203125), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-105683.640625, 45428.35546875), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-105681.9375, 44662.70703125), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-105681.9296875, 44714.22265625), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-105685.0859375, 45040.7890625), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-105683.171875, 45091.55078125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-105683.125, 45142.9140625), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-105683.8046875, 45193.51171875), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-105582.2265625, 44553.75), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-105580.8828125, 44526.1484375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-105579.171875, 44498.89453125), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-105543.953125, 44502.9765625), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-105545.5625, 44531.20703125), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-105546.8046875, 44558.8203125), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-105548.40625, 44586.0859375), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Hauterive(Airport):
    id = 36
    name = "Hauterive"
    position = mapping.Point(-107997.585938, 40856.037109)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Hauterive, self).__init__()

        self.runways.append(Runway(140))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-107626.625, 40475.87109375), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-107641.0703125, 40487.0859375), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-107655.921875, 40498.40625), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-107670.328125, 40509.81640625), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-107684.9609375, 40521.13671875), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-107699.4453125, 40532.6875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-108273.1640625, 41185.73046875), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-107713.046875, 40545.26171875), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-107729.4921875, 40798.89453125), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-107714.9609375, 40787.78515625), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-107699.9921875, 40776.58984375), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-107685.5234375, 40765.296875), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-107670.7890625, 40754.109375), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-107656.2109375, 40742.90625), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-107641.96875, 40731.0625), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-107627.0859375, 40719.8359375), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-107612.609375, 40708.5390625), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-107597.8671875, 40697.36328125), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-107582.875, 40685.93359375), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-108147.3984375, 41203.16015625), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-108109.5, 41168.26953125), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-107867.0625, 40949.45703125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-107831.0078125, 40913.6640625), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-107793.234375, 40878.859375), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-107755.546875, 40845.08984375), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-108295.1015625, 41203.57421875), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-108316.296875, 41221.29296875), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-108337.5078125, 41238.4765625), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-108358.375, 41209.8125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-108336.515625, 41191.87109375), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-108315.359375, 41174.078125), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-108294.203125, 41156.8046875), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Vrigny(Airport):
    id = 38
    name = "Vrigny"
    position = mapping.Point(-89449.566406, 25165.529297)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Vrigny, self).__init__()

        self.runways.append(Runway(140))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-89126.6328125, 24743.80078125), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-89139.6328125, 24756.654296875), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-89153.0390625, 24769.66796875), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-89165.9609375, 24782.716796875), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-89179.1484375, 24795.705078125), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-89192.1484375, 24808.904296875), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-89683.8125, 25525.751953125), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-89204.140625, 24823.0078125), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-89190.203125, 25076.791015625), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-89177.09375, 25064.025390625), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-89163.5703125, 25051.125), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-89150.5546875, 25038.181640625), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-89137.265625, 25025.31640625), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-89124.125, 25012.45703125), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-89111.40625, 24998.998046875), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-89097.96875, 24986.0703125), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-89084.9375, 24973.1328125), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-89071.640625, 24960.275390625), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-89058.1171875, 24947.13671875), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.0, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-89556.8671875, 25528.056640625), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-89523.390625, 25488.888671875), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-89308.8203125, 25242.6953125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-89277.296875, 25202.861328125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-89243.953125, 25163.791015625), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-89210.5703125, 25125.765625), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-89703.4609375, 25546.09765625), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-89722.40625, 25566.212890625), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-89741.40625, 25585.81640625), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-89765.53125, 25559.83203125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-89745.96875, 25539.416015625), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-89727.0859375, 25519.228515625), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-89708.1484375, 25499.544921875), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Conches(Airport):
    id = 40
    name = "Conches"
    position = mapping.Point(-57019.595703, 94577.890625)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Conches, self).__init__()

        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-57231.17578125, 95025.9140625), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-57176.97265625, 95067.0078125), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-57011.6015625, 95182.7109375), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-57121.21484375, 95107.453125), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-56959.0859375, 95226.2734375), large=False, heli=True,
                airplanes=True, slot_name='01', length=24.0, width=33.0, height=7.0, shelter=False))

class Normandy(Terrain):
    center = {"lat": 41.3, "long": 0.18}
    bounds = mapping.Rectangle(-132707.843750, -389942.906250, 185756.156250, 165065.078125)
    map_view_default = MapView(bounds.center(), 1000000)
    city_graph = None
    temperature = [
        (-10, 10),
        (-9, 10),
        (-3, 12),
        (-1, 14),
        (0, 18),
        (2, 22),
        (7, 30),
        (8, 32),
        (3, 28),
        (0, 22),
        (-2, 16),
        (-8, 10)
    ]
    assert(len(temperature) == 12)

    def __init__(self):
        super(Normandy, self).__init__("Normandy")
        self.bullseye_blue = {"x": Normandy.bounds.center().x, "y": Normandy.bounds.center().y}
        self.bullseye_red = {"x": Normandy.bounds.center().x, "y": Normandy.bounds.center().y}

        self.airports['Saint Pierre du Mont'] = Saint_Pierre_du_Mont()
        self.airports['Lignerolles'] = Lignerolles()
        self.airports['Cretteville'] = Cretteville()
        self.airports['Maupertus'] = Maupertus()
        self.airports['Brucheville'] = Brucheville()
        self.airports['Meautis'] = Meautis()
        self.airports['Cricqueville-en-Bessin'] = Cricqueville_en_Bessin()
        self.airports['Lessay'] = Lessay()
        self.airports['Sainte-Laurent-sur-Mer'] = Sainte_Laurent_sur_Mer()
        self.airports['Biniville'] = Biniville()
        self.airports['Cardonville'] = Cardonville()
        self.airports['Deux Jumeaux'] = Deux_Jumeaux()
        self.airports['Chippelle'] = Chippelle()
        self.airports['Beuzeville'] = Beuzeville()
        self.airports['Azeville'] = Azeville()
        self.airports['Picauville'] = Picauville()
        self.airports['Le Molay'] = Le_Molay()
        self.airports['Longues-sur-Mer'] = Longues_sur_Mer()
        self.airports['Carpiquet'] = Carpiquet()
        self.airports['Bazenville'] = Bazenville()
        self.airports['Sainte-Croix-sur-Mer'] = Sainte_Croix_sur_Mer()
        self.airports['Beny-sur-Mer'] = Beny_sur_Mer()
        self.airports['Rucqueville'] = Rucqueville()
        self.airports['Sommervieu'] = Sommervieu()
        self.airports['Lantheuil'] = Lantheuil()
        self.airports['Evreux'] = Evreux()
        self.airports['Chailey'] = Chailey()
        self.airports['Needs Oar Point'] = Needs_Oar_Point()
        self.airports['Funtington'] = Funtington()
        self.airports['Tangmere'] = Tangmere()
        self.airports['Ford_AF'] = Ford_AF()
        self.airports['Argentan'] = Argentan()
        self.airports['Goulet'] = Goulet()
        self.airports['Barville'] = Barville()
        self.airports['Essay'] = Essay()
        self.airports['Hauterive'] = Hauterive()
        self.airports['Vrigny'] = Vrigny()
        self.airports['Conches'] = Conches()

    def saint_pierre_du_mont(self) -> Airport:
        return self.airports["Saint Pierre du Mont"]

    def lignerolles(self) -> Airport:
        return self.airports["Lignerolles"]

    def cretteville(self) -> Airport:
        return self.airports["Cretteville"]

    def maupertus(self) -> Airport:
        return self.airports["Maupertus"]

    def brucheville(self) -> Airport:
        return self.airports["Brucheville"]

    def meautis(self) -> Airport:
        return self.airports["Meautis"]

    def cricqueville_en_bessin(self) -> Airport:
        return self.airports["Cricqueville-en-Bessin"]

    def lessay(self) -> Airport:
        return self.airports["Lessay"]

    def sainte_laurent_sur_mer(self) -> Airport:
        return self.airports["Sainte-Laurent-sur-Mer"]

    def biniville(self) -> Airport:
        return self.airports["Biniville"]

    def cardonville(self) -> Airport:
        return self.airports["Cardonville"]

    def deux_jumeaux(self) -> Airport:
        return self.airports["Deux Jumeaux"]

    def chippelle(self) -> Airport:
        return self.airports["Chippelle"]

    def beuzeville(self) -> Airport:
        return self.airports["Beuzeville"]

    def azeville(self) -> Airport:
        return self.airports["Azeville"]

    def picauville(self) -> Airport:
        return self.airports["Picauville"]

    def le_molay(self) -> Airport:
        return self.airports["Le Molay"]

    def longues_sur_mer(self) -> Airport:
        return self.airports["Longues-sur-Mer"]

    def carpiquet(self) -> Airport:
        return self.airports["Carpiquet"]

    def bazenville(self) -> Airport:
        return self.airports["Bazenville"]

    def sainte_croix_sur_mer(self) -> Airport:
        return self.airports["Sainte-Croix-sur-Mer"]

    def beny_sur_mer(self) -> Airport:
        return self.airports["Beny-sur-Mer"]

    def rucqueville(self) -> Airport:
        return self.airports["Rucqueville"]

    def sommervieu(self) -> Airport:
        return self.airports["Sommervieu"]

    def lantheuil(self) -> Airport:
        return self.airports["Lantheuil"]

    def evreux(self) -> Airport:
        return self.airports["Evreux"]

    def chailey(self) -> Airport:
        return self.airports["Chailey"]

    def needs_oar_point(self) -> Airport:
        return self.airports["Needs Oar Point"]

    def funtington(self) -> Airport:
        return self.airports["Funtington"]

    def tangmere(self) -> Airport:
        return self.airports["Tangmere"]

    def ford_af(self) -> Airport:
        return self.airports["Ford_AF"]

    def argentan(self) -> Airport:
        return self.airports["Argentan"]

    def goulet(self) -> Airport:
        return self.airports["Goulet"]

    def barville(self) -> Airport:
        return self.airports["Barville"]

    def essay(self) -> Airport:
        return self.airports["Essay"]

    def hauterive(self) -> Airport:
        return self.airports["Hauterive"]

    def vrigny(self) -> Airport:
        return self.airports["Vrigny"]

    def conches(self) -> Airport:
        return self.airports["Conches"]