# flake8: noqa
from typing import List, Type

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


class Saint_Pierre_du_Mont(Airport):
    id = 1
    name = "Saint Pierre du Mont"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4050000, vhf_low_hz=39000000, vhf_high_hz=118600000, uhf_hz=250600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-11938.038996, -47277.673365, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-9', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='9', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-11861.235351562, -46465.25390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-11873.943184903, -46479.21794791, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-11898.822265625, -46507.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-11886.739257812, -46492.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-12039.180664062, -46515.12109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-12058.407226562, -46497.13671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-12037.9765625, -46804.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-12129.071289062, -46484.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-12131.545898438, -46550.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-12134.2421875, -46619.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-12137.01171875, -46693.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-12187.690107682, -46858.398011399, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-12126.041617034, -46939.481174499, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-12019.78515625, -47078.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-12001.478515625, -47019.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-12117.408203125, -46866.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-12046.608398438, -47984.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-12027.291992188, -47962.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-12007.661132812, -47941.08984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-12082.845703125, -48027.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-12065.557617188, -48006.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-11731.30078125, -48142.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-11689.122070312, -48092.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-11607.21484375, -48090.13671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-11485.78515625, -48099.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-11493.037109375, -48052.19921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-11505.822265625, -47971.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-11522.823242188, -47863.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-11543.275390625, -47727.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-11546.611328125, -48018.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-11565.462890625, -47896.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-11583.840820312, -47787.68359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-11579.479492188, -47644.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-11520.462443493, -47476.680273727, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-11488.647460938, -47367.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-11510.143554688, -47591.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-11457.013671875, -47441.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-11444.255859375, -47329.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-11450.486328125, -47190.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-11496.440429688, -47212.94921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-11453.455078125, -47132.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-11497.38671875, -47072.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-11443.544921875, -47025.45703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-11432.590820312, -46933.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-11482.905273438, -46949.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-11464.669921875, -46793.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-11411.390625, -46765.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-11510.172851562, -46702.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-11603.045898438, -46734.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-11693.220703125, -46668.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-11743.827148438, -48032.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='117', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-11742.192382812, -47930.80078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-11738.780273438, -47846.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-11791.165039062, -47991.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-11768.6796875, -47652.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-11764.453125, -47571.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-11742.244140625, -47427.82421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-11769.696289062, -47273.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-11722.994140625, -47693.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-11703.243164062, -47521.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-11701.814453125, -47353.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-11725.767578125, -47249.14453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-11833.3125, -46413.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-11836.239257812, -47220.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-11726.50390625, -47038.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-11725.782226562, -46914.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-11707.290039062, -46748.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-11518.412109375, -46987.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-11593.666015625, -47070.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-11773.306640625, -47067.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-11651.00390625, -47687.70703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-11509.331054688, -46558.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-11563.271484375, -46585.95703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-11518.399414062, -46435.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-11579.274414062, -46446.08203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-11652.578125, -46399.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-11777.2734375, -46514.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-11794.124023438, -46463.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-11810.203125, -46957.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-11827.336914062, -46861.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-11802.4921875, -46798.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-11466.025390625, -47522.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-11481.012695312, -47564.6640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-11450.46875, -47479.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-11424.7890625, -47287.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-11426.75390625, -47230.921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-11431.197265625, -47100.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-11426.763671875, -47059.93359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-11416.50390625, -46981.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-11408.248046875, -46893.3046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-11403.66796875, -46850.73046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-11395.853515625, -46805.98828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-11716.645507812, -46377.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-11761.440429688, -46380.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-11722.368164062, -48000.62109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='115', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-11720.6328125, -47963.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='114', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-11719.461914062, -47889.98828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='112', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-11697.715820312, -47637.953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='107', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-11695.588867188, -47595.81640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-11669.390625, -47452.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-11670.260742188, -47410.08984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-11690.357421875, -47295.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='99', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-12062.75, -47063.10546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='84', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-12094.387695312, -47024.12109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='83', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-12121.622070312, -46985.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-12174.390625, -46910.38671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='80', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-12160.331054688, -46655.90234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-12156.065429688, -46584.01171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-12151.716796875, -46515.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-11988.481445312, -47919.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-11985.307749254, -48054.906905204, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-11792.02734375, -48074.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-11806.2421875, -48061.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-11819.955078125, -48049.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-11834.15625, -48037.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-12057.829101562, -46785.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-12008.80078125, -48081.73828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))


class Lignerolles(Airport):
    id = 2
    name = "Lignerolles"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4325000, vhf_low_hz=39550000, vhf_high_hz=119150000, uhf_hz=251150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-35526.060547, -34407.238281, terrain), terrain)

        self.runways.append(Runway(id=None, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-35437.69140625, -35072.56640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-35533.44014624, -34914.341489796, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-35545.310663171, -34808.223795301, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-35583.09375, -34702.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-35611.28125, -34626.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-35641.625914429, -34546.635575714, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-35668.154026845, -34475.774517619, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-35695.23828125, -34401.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-35719.441607242, -34336.29662376, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-35753.734375, -34272.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-35834.734375, -34201.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-35918.54296875, -34127.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-35951.19140625, -34223.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-35937.638439175, -34319.499504146, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-35921.3203125, -34407.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-35836.9140625, -34567.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-35793.9921875, -34631.75390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-35711.29296875, -34755.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-35651.09765625, -34857.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-35587.2109375, -34961.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-35606.05494866, -35020.603139717, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-35657.9296875, -34938.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-35719.828125, -34835.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-35773.26171875, -34747.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-35805.203125, -34699.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-35854.983722669, -34624.906228268, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-35903.024356123, -34553.971837489, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-35935.82421875, -34498.52734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-35102.33984375, -34855.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-35050.13671875, -34894.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-35064.963600555, -34791.217772956, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-35247.627078745, -34535.464676256, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-35308.312271393, -34470.774809143, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-35359.95703125, -34381.29296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-35389.15625, -34301.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-35414.647595952, -34232.607993393, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-35441.7421875, -34157.054637252, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-35479.79271751, -34051.860530705, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-35504.0397034, -34128.546507005, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-35507.71875, -33977.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-35532.411563196, -33907.793471231, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-35557.3125, -33843.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-35179.673394365, -35160.57545339, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-35195.651202706, -35121.705207795, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-35210.863049331, -35082.320438971, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-35226.496051994, -35043.189897301, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-35730.673215219, -34896.144256922, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-35823.695267253, -34240.071237104, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-35875.428207858, -34191.767811538, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-35904.783613308, -34165.491027996, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-35440.760638631, -34105.731850357, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-35426.54296875, -35047.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-35415.1015625, -35022.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-35403.8984375, -34996.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-35392.83203125, -34970.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-35380.8828125, -34943.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-35301.5546875, -34914.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-35284.15234375, -34922.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-35267.5390625, -34930.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-35250.3125, -34937.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-35233.0625, -34946.03515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-35215.83203125, -34954.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-35198.73046875, -34962.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-35181.11328125, -34970.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-35164.265625, -34978.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-35147.6640625, -34986.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))


class Cretteville(Airport):
    id = 3
    name = "Cretteville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4600000, vhf_low_hz=40100000, vhf_high_hz=119700000, uhf_hz=251700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-18675.582031, -77791.164062, terrain), terrain)

        self.runways.append(Runway(id=None, name='31-13', main=RunwayApproach(name='31', heading=310, beacons=[]), opposite=RunwayApproach(name='13', heading=130, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-19256.740234375, -77253.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-19236.23046875, -77255.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-18081.92578125, -78339.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-18100.044921875, -78337.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-19299.7265625, -77325.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-19259.796875, -77383, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-19219.552734375, -77441.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-19097.205078125, -77645.21875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-19056.87890625, -77656.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-18382.986328125, -77737.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-18353.447265625, -77779.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-18123.4296875, -78148.8046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-18332.646240112, -77848.864231023, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-18855.8046875, -77697.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-18875.212890625, -77630.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-18720.312494947, -77381.409315587, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-19109.267578125, -77166.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-19031.01171875, -77489.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-19067.4609375, -77484.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-19049.123046875, -77486.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-19122.33984375, -77621.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-19024.6328125, -77651.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-18116.040806945, -78276.074924499, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-18305.9375, -77993.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-18351.392578125, -77926.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-18538.260512797, -77695.282807261, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-18051.622544082, -78277.555775249, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-18111.812540052, -78195.97888385, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-18161.395642827, -78127.967368393, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-18241.157944377, -77996.938044361, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-18432.102162107, -77712.820215624, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-18516.245013631, -77646.664665477, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-18854.552734375, -77338.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-18836.255859375, -77403.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-19060.23046875, -77581.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-18759.352699548, -77468.383405779, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-19183.700184082, -77460.009796964, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-19225.6796875, -77399.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-19303.953125, -77288.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-19265.904296875, -77342.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-19006.781677323, -77096.272307562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-18621.825432018, -77694.139032598, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-18668.837701873, -77535.669764582, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-18643.746511109, -77478.775612999, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-18807.8828125, -77239.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-19108.0078125, -77145.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-18233.6171875, -78511.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-18226.234013667, -78436.799980343, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-18227.91796875, -78455.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-18229.650390625, -78474.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-18231.5546875, -78492.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-18118.8046875, -78336.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-19106.96875, -77125.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-19105.943359375, -77106.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-19216.01953125, -77257.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-18420.499213946, -77798.911429215, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))


class Maupertus(Airport):
    id = 4
    name = "Maupertus"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4875000, vhf_low_hz=40650000, vhf_high_hz=120250000, uhf_hz=252250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(16010.684042, -84863.223212, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(15957.225585938, -84030.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(16018.493164062, -84016.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(16237.17578125, -83995.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(16196.150390625, -83987.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(16115.506835938, -83983.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(16074.153320312, -83991.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(15994.185546875, -85262.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))


class Brucheville(Airport):
    id = 5
    name = "Brucheville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5125000, vhf_low_hz=41150000, vhf_high_hz=120750000, uhf_hz=252750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-14857.000488, -66027.34375, terrain), terrain)

        self.runways.append(Runway(id=None, name='7-25', main=RunwayApproach(name='7', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-14501.358398438, -65514.94921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='90', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-14517.989257812, -65507.62890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-14534.658203125, -65500.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-14551.46875, -65492.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-15255.484375, -66566.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-15218.252929688, -66387.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-15152.118164062, -66305.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-15106.09375, -66203.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-15073.575195312, -66127.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-15040.1796875, -66049.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-15009.584960938, -65980.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14977.276367188, -65908.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14949.876953125, -65844.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14927.905273438, -65775.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14938.030273438, -65667.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14946.461914062, -65557.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-15034.13671875, -65603.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-15091.52734375, -65681.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-15141.300630506, -65756.363331498, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='93', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-15193.87890625, -65929.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-15206.630859375, -66005.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-15233.885742188, -66152.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-15260.15575293, -66267.517473785, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15288.400390625, -66385.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15344.825195312, -66414.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15323.421875, -66319.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15296.349609375, -66202.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-15273.232242477, -66103.247948019, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-15262.833984375, -66046.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-15246.717773438, -65957.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-15232.001953125, -65873.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-15217.291015625, -65810.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='94', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-14867.946289062, -66647.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-14857.071289062, -66711.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-14793.830078125, -66628.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-14715.09375, -66501.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-14739.391601562, -66435.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-14670.317382812, -66416.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14692.541992188, -66349.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-14624.703125, -66328.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-14659.502929688, -66280.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-14592.354492188, -66256.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-14618.577148438, -66192.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-14554.859375, -66174.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-14585.719726562, -66123.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-14523.669921875, -66105.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-14545.145507812, -66033.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-14457.186529987, -65958.600256051, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-14490.674108544, -65892.286941777, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-14436.583984375, -65881.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-14478.83203125, -65826.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-14429.744140625, -65808.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-14473.884765625, -65754.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-14421.282226562, -65718.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-14415.702148438, -65667.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-14462.69921875, -65642.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-14418.568827337, -65578.099879405, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-14748.681640625, -66316.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-14746.928710938, -66227.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-14721.640625, -66127.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-14687.233398438, -66049.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-14656.653320312, -65983.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-14624.192382812, -65909.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-14578.459960938, -65808.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-14648.44921875, -65845.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-14546.174804688, -65735.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-14515.787109375, -65667.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-14487.78125, -65603.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-14663.276367188, -65443.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-14679.943359375, -65436.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-14696.75, -65428.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-14676.118164062, -66470.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-14638.977539062, -66399.1015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-14621.461914062, -66364.3046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-14591.599609375, -66301.3046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-14413.962449721, -65845.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-14404.415039062, -65765.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-14394.783203125, -65619.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-14686.155273438, -66096.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-14652.928710938, -66025.1484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-14622.028320312, -65954.0078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-14591.83984375, -65887.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-14574.374023438, -65848.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-15157.338867188, -66267.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-15139.759765625, -66227.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-15107.727539062, -66156.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-15075.030273438, -66081.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-14953.810546875, -65745.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-14957.19921875, -65702.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='79', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-14962.072265625, -65635.9140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='81', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-14966.075195312, -65593.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='82', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-15274.353515625, -65996.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-15260.655273438, -65912.7265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='98', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-15244.107421875, -65837.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-15229.662109375, -66556.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-15204.504882812, -66546.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-15179.133789062, -66536.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-15154.333984375, -66526.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-14992.06640625, -66702.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-14998.623046875, -66686.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-15005.604492188, -66668.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-15012.447265625, -66651.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-15019.56640625, -66634.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-15025.469586353, -66617.438406458, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-15032.593609791, -66600.094656458, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-15039.409039478, -66582.844656458, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-15046.486187916, -66565.829031458, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))


class Meautis(Airport):
    id = 6
    name = "Meautis"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5400000, vhf_low_hz=41700000, vhf_high_hz=121300000, uhf_hz=253300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-24485.687154, -71910.215499, terrain), terrain)

        self.runways.append(Runway(id=None, name='8-26', main=RunwayApproach(name='8', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-24512.439453125, -71203.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-24455.6015625, -71257.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-24488.98046875, -71217.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-24222.326171875, -71235.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-24237.43359375, -71246.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-24207.40625, -71224.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-24449.250576067, -72574.258999437, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-24520.91015625, -72570.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-24425.862918865, -72602.891621554, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-24753.8515625, -72582.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-24738.1640625, -72572.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-24722.5234375, -72562.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-24706.70703125, -72553.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-24239.272146232, -71453.171043221, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-24233.211077682, -71421.363670832, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-24227.291163309, -71390.706286046, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-24221.827877447, -71358.770765623, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-24215.9609375, -71325.2109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-24439.576263565, -72518.182299794, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-24435.516661535, -72488.525467414, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-24430.979129193, -72459.973126853, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-24532.384765625, -71210.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-24425.917096311, -72431.163736959, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-24420.369054766, -72400.298325928, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-24415.236242266, -72370.712388428, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-24409.794836016, -72341.728013428, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-24404.384679766, -72311.860825928, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-24398.924411468, -72282.80463332, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-24394.141018835, -72255.132692588, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-24389.134434293, -72227.99058439, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-24383.868178011, -72200.402875799, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-24337.562493509, -71912.557230825, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-24332.429681009, -71882.963480825, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-24326.857081541, -71853.52724333, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-24321.538722166, -71823.69130583, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-24316.103175291, -71794.70693083, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-24311.036769041, -71765.34755583, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-24305.275050291, -71733.82411833, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-24300.155390483, -71703.957820833, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-24294.739374858, -71674.981258333, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-24288.904528835, -71640.67865297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-24283.470935085, -71611.70209047, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-24278.40257571, -71582.33490297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-24272.64866946, -71550.80365297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-24267.50804446, -71521.20990297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-24262.08226321, -71492.23334047, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))


class Cricqueville_en_Bessin(Airport):
    id = 7
    name = "Cricqueville-en-Bessin"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5450000, vhf_low_hz=41800000, vhf_high_hz=121400000, uhf_hz=253400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-14917.461426, -50815.857422, terrain), terrain)

        self.runways.append(Runway(id=None, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-15036.99609375, -51188.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-15091.197265625, -51189.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-15142.259765625, -51190.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-15281.184570312, -51137.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-15298.483398438, -51091.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-15317.65625, -51047.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-15336.374023438, -51002.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-15354.755859375, -50956.9296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-15418.361328125, -50414.19921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-15101.448242188, -50437.07421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-15140.26953125, -50467.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-15179.002929688, -50500.98828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-14789.887695312, -50429.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14785.345703125, -50480.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14778.875976562, -50532.2890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14873.093679891, -50271.912260383, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14393.776367188, -50436.76953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14362.53515625, -50450.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-14330.71484375, -50463.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-15480.72265625, -50543.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-15456.775390625, -50455.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-15404.940429688, -50455.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-15422.161132812, -50520.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-15482.276367188, -50696.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-15475.487304688, -50678.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15532.52734375, -50821.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15526.719726562, -50803.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15556.122070312, -50900.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15538.387695312, -50839.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-15492.958984375, -50850.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-15317.954101562, -50832.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-15203.686523438, -50834.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-14977.603515625, -50935.98046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-14829.362304688, -50973.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-15343.048828125, -50902.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-15280.298828125, -50928.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-15245.411132812, -51016.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-15187.541992188, -51169.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-14988.005859375, -51161.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-15062.760742188, -51115.62890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14834.578125, -51050.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-14740.361328125, -51063.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-14737.412109375, -51005.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-14481.265625, -51002.46484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-14534.053710938, -51029.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-14534.231445312, -50972.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-14433.102539062, -51086.09765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-14283.299804688, -51085.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-14898.4296875, -50565.55078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-15205.576171875, -50580.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-15042.82421875, -50424.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-14928.950195312, -50414.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-14831.16015625, -50282.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-14871.176757812, -50337.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-14821.112304688, -50376.94921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-14852.219726562, -50551.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-14220.969726562, -51007.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-14106.381835938, -51025.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-14093.397460938, -51065.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-14138.702148438, -51079.06640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-14214.407226562, -51090.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-14497.122613217, -50471.215932458, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-14486.166992188, -50584.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-14371.833984375, -50654.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-14244.102539062, -50718.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-14463.62670459, -50520.600876678, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-14729.752452546, -50692.0770947, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-14806.484375, -50589.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-14266.1484375, -50823.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-14251.94921875, -50811.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-14237.971679688, -50798.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-14303.3828125, -51041.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-14311.14453125, -51023.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))


class Lessay(Airport):
    id = 8
    name = "Lessay"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5475000, vhf_low_hz=41850000, vhf_high_hz=121450000, uhf_hz=253450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-33862.595703, -86418.007812, terrain), terrain)

        self.runways.append(Runway(id=None, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.runways.append(Runway(id=None, name='24-6', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='6', heading=60, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-33662.57421875, -86710.5703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-33433.50390625, -87110.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-33482.44140625, -87000.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-33684.90234375, -86676.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-33692.0078125, -86485.2109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-33598.76953125, -86289.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-34212.1640625, -86446.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-34181.9609375, -86422.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-33818.0625, -87227.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-33699.921875, -87349.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-33666.0390625, -87386.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-34258.4453125, -86497.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-34269.671875, -86482.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-34302.3828125, -86437.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-34291.44921875, -86452.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-34280.42578125, -86467.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-34088.7421875, -86284.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-33449.34765625, -85828.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-33433.03515625, -85836.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-33665.155044047, -85712.211540477, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-33648.199457321, -85721.018991191, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-33631.27734375, -85729.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-33614.467129822, -85738.132511012, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-33597.564246013, -85746.555767619, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-33513.84765625, -87600.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-33776.38671875, -87132.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-33691.08203125, -87216.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-33597.89453125, -87308.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-33538.01953125, -87418.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-33449.77734375, -86016.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-33500.7578125, -86145.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-33607.65625, -86138.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-33679.51171875, -86230.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-33785.83203125, -86456.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-33823.88671875, -86588.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-33574.41796875, -86236.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-33644.30078125, -86325.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-33685.91015625, -86421.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-33718.13671875, -86537.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-33714.7890625, -86650.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-33754.078125, -86750.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-33693.9765625, -86838.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-33649.79296875, -86745.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-33621.7578125, -86944.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-33581.984375, -86843.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-33517.6015625, -86942.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-33565.828125, -87037.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-33520.64453125, -87147.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-33461.2734375, -87060.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-33416.0390625, -87168.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-33353.05859375, -87262.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-33272.55859375, -87342.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-33385.7890625, -87356.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-33303.296875, -87432.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-33267.757199427, -87505.188563924, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-33220.2890625, -87391.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-33247.94140625, -87366.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))


class Sainte_Laurent_sur_Mer(Airport):
    id = 9
    name = "Sainte-Laurent-sur-Mer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5500000, vhf_low_hz=41900000, vhf_high_hz=121500000, uhf_hz=253500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-14665.532227, -41130.955078, terrain), terrain)

        self.runways.append(Runway(id=None, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-14792.571289062, -40413.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-14786.885742188, -40431.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-14780.911132812, -40449.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-14775.3671875, -40466.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-14769.575195312, -40484.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-14763.927734375, -40501.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-14758.26953125, -40519.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-14500.940429688, -41793.68359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-14506.548828125, -41776.21484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-14512.370117188, -41758.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-14518.376953125, -41741.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14524.096679688, -41724.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14716.283203125, -41543.76953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14729.244140625, -41490.97265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14741.564453125, -41439.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14845.327148438, -41070.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-14857.267578125, -41016.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-14868.475585938, -40965.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-14881.069335938, -40912.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-14893.48046875, -40863.08984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-14932.262695312, -40735.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-14976.861328125, -40748.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-15025.260742188, -40763.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15079.633789062, -40779.78515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15138.8046875, -40593.58984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15092.795898438, -40578.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15044.654296875, -40562.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-14990.793945312, -40544.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-14946.081054688, -40639.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-14964.600585938, -40645.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-14982.981445312, -40651.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-15001.500976562, -40657.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-15019.73046875, -40663.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-15038.25, -40669.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-15056.0390625, -40676.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-15074.408203125, -40682.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-15093.846679688, -40688.37890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-14540.583984375, -41806.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14546.1875, -41788.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-14552.008789062, -41771.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-14558.014648438, -41754.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-14563.748046875, -41736.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))


class Biniville(Airport):
    id = 10
    name = "Biniville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3800000, vhf_low_hz=38500000, vhf_high_hz=118100000, uhf_hz=250100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-7680.428545, -84526.999232, terrain), terrain)

        self.runways.append(Runway(id=None, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-8033.611328125, -84135.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-8019.6059570312, -84147.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-8005.193359375, -84159.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-7991.2490234375, -84171.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-7977.0590820312, -84183.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-7963.0268554688, -84195.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-7414.8676757812, -84869.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-7949.9409179688, -84208.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-7943.2578125, -84462.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-7957.3520507812, -84450.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-7971.8725585938, -84439, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-7985.90234375, -84427.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-8000.1918945312, -84415.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-8014.328125, -84403.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-8028.1040039062, -84391.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-8042.5458984375, -84379.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-8056.5776367188, -84367.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-8070.8725585938, -84355.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-8085.4135742188, -84343.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-7541.2006835938, -84882.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-7577.7485351562, -84846.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-7811.5815429688, -84618.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-7846.2333984375, -84581.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-7882.6318359375, -84544.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-7918.98828125, -84509.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-7393.63671875, -84888.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-7373.1157226562, -84907.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-7352.5859375, -84925.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-7330.65625, -84897.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-7351.8154296875, -84878.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-7372.2724609375, -84859.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-7392.73046875, -84841.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Cardonville(Airport):
    id = 11
    name = "Cardonville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3825000, vhf_low_hz=38550000, vhf_high_hz=118150000, uhf_hz=250150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-16508.699707, -53979.537109, terrain), terrain)

        self.runways.append(Runway(id=None, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-15586.537109375, -54800.81640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-15641.615234375, -54743.21484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-15673.69140625, -54710.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-16080.328125, -53632.6796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-16146.381835938, -53639.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-16188.14453125, -53642.76171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-16229.381835938, -53646.97265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='95', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-16437.35546875, -53667.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='100', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-16477.451171875, -53656.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='101', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-16555.625, -53639.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-17250.392578125, -53886.55859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-17221.244140625, -53918.51171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-17189.90234375, -53951.96484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-17159.515625, -53983.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-17129.3671875, -54016.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-16761.142578125, -54228.5703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-16751.130859375, -54273.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-16668.916015625, -54469.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-16649.916015625, -54509.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-16629.091796875, -54548.6640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-16216.904296875, -54955.22265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-16185.349609375, -54985.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-16114.564453125, -55053.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-16081.6015625, -55081.94921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-16011.588867188, -55136.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-15978.251953125, -55164.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-15859.850585938, -54399.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-15853.694335938, -54416.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-15848.7109375, -54434.12109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-15843.506835938, -54452.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-15837.958984375, -54469.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-15832.440429688, -54487.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-16961.4765625, -53485.44921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='112', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-16871.330078125, -53474.70703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='111', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-16869.044921875, -53556.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='110', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-16812.857421875, -53549.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='109', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-16752.498046875, -53610.49609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='108', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-16786.134765625, -53651.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='107', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-16673.2890625, -53679.98828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-16637.556640625, -53637.48828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-16559.43359375, -53706.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-16522.216796875, -53665.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-16455.0078125, -53732.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-16386.693359375, -53681.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-16303.830078125, -53723.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-16139.215820312, -53706.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-16263.493164062, -53669.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-16110.779296875, -53652.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-16008.267578125, -53643.11328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='89', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-15892.083007812, -53658.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-15789.494140625, -53794.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-15714.548828125, -53896.33984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-15674.037109375, -53988.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-15804.512695312, -53856.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-15726.368164062, -54097.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-15971.498046875, -53935.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-16027.420898438, -54086.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-15992.6640625, -53835.65234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-16054.048828125, -54018.81640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-16151.375568029, -54313.219553969, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-16120.153320312, -54391.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-16203.601009342, -54493.791951549, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-16183.944335938, -54610.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-16261.133789062, -54701.5859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-15914.191672766, -54633.648615494, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-15931.873046875, -54696.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-16001.69609317, -54673.963952383, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-16028.017578125, -54743.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-16119.55029407, -54729.494863746, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-16211.81640625, -54835.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-15795.741210938, -54606.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-15769.283143697, -54719.608187958, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-15723.627929688, -54697.57421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-15682.968219121, -54809.498492558, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-15630.574613831, -54792.1773815, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-15623.0703125, -54869.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-15596.291015625, -54942.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-15653.127059258, -55021.396902143, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-15706.948084894, -55007.693152263, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-15717.867230002, -55104.654127818, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-15778.290277633, -55105.193390834, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-15822.833007812, -55227.52734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-15933.588867188, -55169.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-15925.166015625, -55110.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-16023.131835938, -55090.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-16010.935546875, -55035.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-16120.498046875, -54939.66796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-16341.719726562, -54749.56640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-16134.9140625, -54993.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-16233.361328125, -54906.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-16324.620117188, -54827.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-16412.291015625, -54754.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-16480.267025396, -54696.796071031, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-16476.26171875, -54636.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-16584.341495387, -54578.06665749, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-16668.924418003, -54408.514720535, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-16709.921875, -54318.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-16748.637175346, -54177.358750208, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-16708.390625, -54139.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-16861.119140625, -54099.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-17005.7421875, -54058.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-16895.994140625, -54037.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-17079.923828125, -53953.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-17158.5546875, -53871.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-17258.072605531, -53838.422563443, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-17278.8203125, -53735.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-17260.72265625, -53730.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-17242.7421875, -53726.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-17152.638671875, -53555.58203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='116', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-17158.3046875, -53537.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='115', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-17163.9375, -53520.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='114', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-17169.751953125, -53502.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='113', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-15758.708007812, -54239.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-15794.997070312, -54245.63671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-15740.494140625, -54237.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-15776.756835938, -54242.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=16.0, width=16.900002, height=6.0, shelter=False))


class Deux_Jumeaux(Airport):
    id = 12
    name = "Deux Jumeaux"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3850000, vhf_low_hz=38600000, vhf_high_hz=118200000, uhf_hz=250200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-16784.448242, -48871.496094, terrain), terrain)

        self.runways.append(Runway(id=None, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-16293.255859375, -48417.40234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-16282.234375, -48455.4921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-16270.723632812, -48493.8984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-16658.90625, -49620.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='97', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-16648.599609375, -49604.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='98', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-16354.609375, -49555.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-16349.532226562, -49637.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='106', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-16406.048828125, -49603.85546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='105', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-16432.638822619, -49660.632862748, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='104', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-16531.4765625, -49571.76953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='99', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-16514.380859375, -49578.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='100', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-16497.287109375, -49586.13671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='101', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-16480.197265625, -49593.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='102', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-16463.14453125, -49600.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='103', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-16352.766601562, -49500.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-16308.0703125, -49577.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-16303.249916201, -49463.12109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-16298.580058197, -49374.034699036, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-16291.721431153, -49228.841444, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-16344.087329071, -49296.248856964, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-16287.10546875, -49135.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-16284.022980286, -49055.506420929, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-16277.451942109, -48952.161527893, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-16333.291015625, -49085.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-16329.033203125, -48992.132355286, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-16323.447972158, -48866.166888631, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-16271.005859375, -48810.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-16279.041150285, -48535.982526215, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-16317.489979723, -48580.188467786, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-16361.735626355, -48427.136506591, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-16322.674791657, -48390.436587235, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-16342.681640625, -48321.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-16385.27694618, -48345.772201621, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-16396.874189911, -48275.735882442, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-16504.999491399, -48287.98828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-16579.917114533, -48248.519142364, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-16678.650239881, -48287.981373215, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-16620.384765625, -48319.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-16316.899414062, -48630.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-16529.078125, -48626.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-16885.779296875, -48705.09765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='83', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-16699.5390625, -48662.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='85', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-16625.885142485, -48698.697558739, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='86', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-16734.740234375, -48720.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='84', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-16911.642578125, -48762.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='82', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-16982.25341601, -48756.153963928, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-16410.884765625, -49173.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-16528.8203125, -49195.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-16615.6484375, -49211.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-16374.63671875, -49215.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-16430.197265625, -49228.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-16565.91015625, -49253.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-16774.92578125, -49244.20703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-16744.666015625, -49286.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-16756.822265625, -49364.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='87', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-16721.998046875, -49469.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='91', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-16687.62890625, -49574.08984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='95', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-16790.95703125, -49416.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='88', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-16755.474609375, -49520.81640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='92', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-16721.2265625, -49625.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='96', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-16459.41919268, -49108.289698933, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-16524.520786597, -49018.263322986, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-16495.467318574, -48889.86097525, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-16552.59375, -48862.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-16511.842525686, -48801.357151845, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-16577.294921875, -48591.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-16796.164584199, -49212.974640834, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-16808.110819524, -49146.868569107, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-16868.32254107, -49093.585657439, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-16874.853515625, -49053.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-16847.708984375, -48969.96484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-16883.748046875, -48873.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-16911.447027054, -48939.36328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-16951.494140625, -48833.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-16992.060546875, -48671.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-16951.58984375, -48602.14453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-17006.058012268, -48545.400274329, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-16646.740234375, -48572.83203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-16664.58984375, -48456.64453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-16737.592705936, -48433.493876312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-16718.697265625, -48371.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-16947.78125, -48475.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-16964.701171875, -48468.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-16799.900390625, -48399.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='81', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-16813.556640625, -48412.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='80', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-16826.8359375, -48425.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='79', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-16608.15234375, -48514.71484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-16628.984375, -48480.06640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-16584.869140625, -48547.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-16487.88671875, -48844.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-16471.427734375, -48937.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-16462.33984375, -48982.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-16454.626953125, -49029.05078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-16447.1015625, -49074.9609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-16362.614257812, -49354.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-16364.236328125, -49400.04296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-16367.515625, -49446.78515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-16751.185546875, -49599.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='94', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-16764.0625, -49560.30078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='93', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-16785.099609375, -49494.2734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='90', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-16797.408203125, -49455.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='89', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-16866.474609375, -49213.26171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-16872.404296875, -49171.25390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-16877.357421875, -49129.58984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-16899.203125, -49023.30078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-16915.587890625, -48978.65234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=7.0, shelter=False))


class Chippelle(Airport):
    id = 13
    name = "Chippelle"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3875000, vhf_low_hz=38650000, vhf_high_hz=118250000, uhf_hz=250250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-28484.011719, -47891.75, terrain), terrain)

        self.runways.append(Runway(id=None, name='6-24', main=RunwayApproach(name='6', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-27995.6875, -47895.3359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-27973.552734375, -47983.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-27959.81640625, -48073.33984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-27962.666015625, -47073.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-27971.533203125, -47089.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-27980.431640625, -47105.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-27989.498046875, -47121.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-27998.423828125, -47137.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-28007.546875, -47154.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-28016.677734375, -47170.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-28025.763671875, -47186.2421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-28352.4375, -48438.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-28320.48046875, -48429.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-28163.1328125, -48399.45703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-28129.833984375, -48398.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-27805.580078125, -47574.76171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-27773.833984375, -47524.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-27755.712890625, -47484.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-27696.97265625, -47242.69140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-27717.705078125, -47202.5390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-27739.095703125, -47163.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-28896.05859375, -47632.703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-28883.548828125, -47687.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-28870.4296875, -47743.6171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-28858.521484375, -47800.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-28975.806640625, -48118.0703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-28978.978515625, -48189.9375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-28983.876953125, -48264.3984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-29006.0546875, -48346.3671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-29043.02734375, -48431.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-28095.26953125, -47146.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-28086.189453125, -47130.43359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-28077.08984375, -47114.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-28067.8203125, -47098.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-28058.701171875, -47082.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-28049.359375, -47066.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-28040.0390625, -47050.03515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-28030.740234375, -47034.16015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))


class Beuzeville(Airport):
    id = 14
    name = "Beuzeville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3900000, vhf_low_hz=38700000, vhf_high_hz=118300000, uhf_hz=250300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-9213.708321, -72131.675455, terrain), terrain)

        self.runways.append(Runway(id=None, name='5-23', main=RunwayApproach(name='5', heading=50, beacons=[]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-9549.2371128719, -72743.202755871, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-9525.7830145649, -72749.92337805, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-8782.3181846694, -71971.304403324, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-8812.5997136796, -72006.247082551, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-9027.2392059861, -71673.991655877, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-9056.5396330411, -71706.04625186, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-9087.6465945336, -71740.691774085, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-9120.8313294094, -71770.761956825, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-9149.7288094182, -71803.667504519, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-9755.9261008704, -72561.004226378, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-9792.3576487029, -72563.908011363, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-8687.6023167638, -71690.318635498, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-8669.0404678861, -71690.169369297, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-8650.5332512783, -71689.711128952, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-8632.0775919186, -71689.466558893, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-8912.1347782726, -71498.968954511, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-8836.6006874024, -71578.605364839, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-8905.5398592672, -71535.659105952, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-8943.3783126573, -71580.275636544, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-9556.6817989323, -72720.691482349, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-9564.7540722959, -72668.103804183, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-8980.5695321387, -72174.161781356, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-8953.0317153469, -72141.475697815, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-9023.141143577, -72215.132768449, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-9054.2373223506, -72249.905465778, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-9156.4932896598, -72364.133001189, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-9186.2753822444, -72398.642693397, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-9085.025237793, -72283.605659764, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-9124.7976775728, -72329.905068923, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-9314.5390680744, -72536.892469643, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-9347.5236442115, -72578.037418466, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-9226.7180933049, -72447.122458219, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-9280.7393831763, -72498.541479403, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-8888.2899247269, -72067.824434539, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-8921.380996126, -72106.57792139, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-8841.833611918, -72041.810811428, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))


class Azeville(Airport):
    id = 15
    name = "Azeville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3925000, vhf_low_hz=38750000, vhf_high_hz=118350000, uhf_hz=250350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-2525.192392, -73664.185534, terrain), terrain)

        self.runways.append(Runway(id=None, name='7-25', main=RunwayApproach(name='7', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-2123.7131347656, -73153.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-2081.9501953125, -73177.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-2040.4594726562, -73200.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-2012.9418945312, -73986.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-2035.3203125, -74028.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-2056.7839355469, -74071.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-2106.0627441406, -73798.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-2065.8771972656, -73822.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-2212.58984375, -74123.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-2255.6872558594, -74098.9921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-2297.3012695312, -74074.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-2629.3388671875, -73137.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-2652.0964355469, -73188.8671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-2673.8247070312, -73237.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-2764.1257324219, -73455.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-2778.4426269531, -73504.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-2788.1728515625, -73557.7734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-2445.6650390625, -73047.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-2436.5981445312, -73063.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-2427.4140625, -73079.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-2418.4819335938, -73096.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-2802.3271484375, -74166.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-2820.349609375, -74172.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-2838.0317382812, -74177.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-2605.4279785156, -74259.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-2614.9304199219, -74243.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-2624.9028320312, -74227.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-2634.4953613281, -74212.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-2244.7939453125, -73155.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-2227.5087890625, -73148.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-2210.3583984375, -73141.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))


class Picauville(Airport):
    id = 16
    name = "Picauville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3950000, vhf_low_hz=38800000, vhf_high_hz=118400000, uhf_hz=250400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-12078.898926, -80241.097656, terrain), terrain)

        self.runways.append(Runway(id=None, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-11705.821289062, -80830.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-11688.598632812, -80813.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-12008.790129538, -79785.056479807, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-11992.607046861, -79828.870528737, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-12364.773373001, -79921.35005031, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-12352.926310794, -79952.130869917, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-12341.037322597, -79980.936366073, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-12138.869980761, -80562.983077691, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-12120.955918261, -80610.694015191, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-12008.892578125, -80901.1796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-12024.680664062, -80935.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-12210.875976562, -79567.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-12202.032226562, -79550.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-12193.485351562, -79534.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-12184.776367188, -79518.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-12484.275606471, -79667.038180088, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-12380.703125, -79643.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-12449.084009163, -79678.748140559, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-12378.486774371, -79882.123577947, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-11729.125976562, -80826.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-11779.061523438, -80807.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-11897.059570312, -80148.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-11914.984375, -80100.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-11883.475585938, -80189.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-11858.645832626, -80256.990079853, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-11814.542222247, -80387.369365119, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-11800.11161623, -80425.209191376, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-11844.744593059, -80302.192413956, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-11828.73769139, -80345.353080684, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-11750.1950769, -80573.027692021, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-11726.817369163, -80636.365510076, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-11785.062202936, -80475.254154651, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-11766.925793204, -80523.263945032, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-11948.153320312, -80008.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-11930.229492188, -80056.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-11961.729492188, -79968.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))


class Le_Molay(Airport):
    id = 17
    name = "Le Molay"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=3975000, vhf_low_hz=38850000, vhf_high_hz=118450000, uhf_hz=250450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-26123.464844, -41403.646484, terrain), terrain)

        self.runways.append(Runway(id=None, name='22-4', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='4', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-25710.234375, -40841.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-25728.570386257, -40836.218305422, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-26573.366872787, -41502.122958808, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-26539.770757123, -41472.023371614, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-26430.628065989, -41885.641688014, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-26391.807753489, -41850.551844264, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-26354.493300364, -41816.047938014, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-26326.231749006, -41789.100753942, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-26288.302061506, -41755.049972692, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-25530.654057203, -41081.604719417, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-25493.111088453, -41083.889875667, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-26703.17578125, -41771.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-26721.59375, -41769.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-26740.001953125, -41767.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-26758.326171875, -41765.30078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-26506.125038148, -41988.894540288, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-26572.024283216, -41902.315011883, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-26506.897335978, -41951.071161524, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-26456.679306329, -41909.747811724, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-25705.8203125, -40864.9921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-25704.75390625, -40918.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-26323.022490338, -41326.574364352, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-26360.940459088, -41360.621239352, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-26290.206084088, -41299.172020602, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-26252.293974713, -41265.105614352, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-26113.732890439, -41133.475159372, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-26066.966568244, -41090.416685048, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-26184.451640439, -41194.928284372, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-26147.996457636, -41165.047612331, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-25927.123391165, -40981.625870483, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-25835.392004404, -40913.864222727, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-26007.225154784, -41048.61795056, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-25967.173183639, -41015.960096668, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-26434.833037213, -41425.101708102, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-26396.911162213, -41391.050926852, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-26501.862918516, -41442.653566536, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))


class Longues_sur_Mer(Airport):
    id = 18
    name = "Longues-sur-Mer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4000000, vhf_low_hz=38900000, vhf_high_hz=118500000, uhf_hz=250500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-16733.196289, -28909.375977, terrain), terrain)

        self.runways.append(Runway(id=None, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-16807.962890625, -28363.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-16807.560546875, -28381.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-16807.03125, -28400.830078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-16806.25390625, -28438.42578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-16930.123046875, -28211.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-16920.40625, -28227.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-16910.3125, -28242.736328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-16900.71484375, -28258.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-16890.833984375, -28274.029296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-16939.623046875, -28195.556640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-16949.123046875, -28179.33203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-16807.369140625, -28419.271484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-16805.587890625, -28475.853515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-16805.181640625, -28494.427734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-16804.646484375, -28513.302734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-16806.193359375, -28457.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-16803.90625, -28551.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-16804.998046875, -28531.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-16692.044921875, -28369.626953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-16776.28515625, -28436.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-16747.720703125, -28171.970703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-17123.638671875, -28505.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-17105.720703125, -28509.447265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-17087.390625, -28513.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-17069.439453125, -28516.912109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-17051.3046875, -28520.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-16893.796875, -29078.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-16801.8671875, -29157.962890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-16926.353515625, -29296.88671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-17134.45703125, -29145.544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-17208.533203125, -29217.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-17219.412109375, -29309.48828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-17224.39453125, -28715.630859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-17024.671875, -29481.23046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-16978.853515625, -29471.9140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-16931.41796875, -29464.322265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-17135.447265625, -28976.498046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-17144.453125, -28927.85546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-17151.802734375, -28878.380859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-17168.888671875, -28779.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-17176.681640625, -28738.08984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-16677.41015625, -28404.736328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-16657.23046875, -28443.82421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-16942.953125, -29224.666015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-17015.8125, -29212.169921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-17024.232421875, -29148.724609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))


class Carpiquet(Airport):
    id = 19
    name = "Carpiquet"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4025000, vhf_low_hz=38950000, vhf_high_hz=118550000, uhf_hz=250550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-34769.425958, -10001.304177, terrain), terrain)

        self.runways.append(Runway(id=None, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-34197.03515625, -9833.6513671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-34212.44140625, -9804.1455078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-34134.3671875, -9956.640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-34149.7734375, -9927.1357421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-34069.6484375, -10074.700195312, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-34085.0546875, -10045.1953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-34017.34375, -10166.115234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-34001.8671875, -10196.345703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-34087.314132154, -10191.047501569, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-35223.62109375, -10048.220703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-35225.9921875, -10014.627929688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-35212.45703125, -10184.047851562, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-35214.8359375, -10150.447265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-35202.72265625, -10321.732421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-35205.28125, -10287.767578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-34094.51953125, -9752.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-33980.7890625, -9794.8310546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-33994.0078125, -9714.791015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-33947.72265625, -9616.6376953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-33908.58984375, -9757.107421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-33913.14453125, -9545.3740234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-33992.75, -9505.3828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-34080.3046875, -9445.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-34298.2734375, -9760.3505859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-35416.671875, -10415.975585938, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-35409.21875, -10273.341796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-35403.3828125, -10136.973632812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-34814.234375, -10790.25390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-34754.29296875, -10794.409179688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-35191.609375, -10458.305664062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-35194.97265625, -10423.762695312, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-34296.46875, -9837.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-34270.0390625, -9886.0361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-34287.34375, -9853.5361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-34278.56640625, -9869.58984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-34229.359375, -9956.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-34202.9296875, -10004.895507812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-34220.234375, -9972.3955078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-34211.45703125, -9988.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-34060.880538404, -10240.125626569, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-34078.345382154, -10207.716446882, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-34069.728194654, -10224.117814069, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-34132.796875, -10122.698242188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-34159.2265625, -10073.899414062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-34150.09765625, -10090.197265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-34141.33203125, -10106.25390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-34694.890625, -10798.870117188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))


class Bazenville(Airport):
    id = 20
    name = "Bazenville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4075000, vhf_low_hz=39050000, vhf_high_hz=118650000, uhf_hz=250650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-20712.899414, -18498.402344, terrain), terrain)

        self.runways.append(Runway(id=None, name='5-23', main=RunwayApproach(name='5', heading=50, beacons=[]), opposite=RunwayApproach(name='23', heading=230, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-20335.234375, -18316.857421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-20377.361328125, -18364.02734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-20772.580078125, -18210.572265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-20232.328125, -18036.72265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-20251.14453125, -18038.349609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-20288.55859375, -18041.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-20269.576171875, -18039.072265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-20390.791015625, -17800.55078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-20377.712890625, -17815.150390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-20403.771484375, -17786.548828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-20783.365234375, -18178.650390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-20763.3828125, -18237.361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-20793.443359375, -18148.78515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-21005.6171875, -18443.46484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-21123.7421875, -18722.470703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-21026.334471932, -18591.716267445, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-21256.19140625, -18898.48046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-21391.382479553, -18569.04609637, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-21296.03515625, -18453.11328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-21163.62890625, -18425.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-21025.4375, -18523.05078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-21286.15234375, -18517.451171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-21434.883622589, -18715.452210571, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-21404.08984375, -18926.802734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-21336.30859375, -18968.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-21333.0546875, -18806.814453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-21329.564453125, -18746.94140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-21265.501953125, -18794.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-21135.96484375, -18822.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-21050.67578125, -19086.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-21049.85546875, -19105.11328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-21048.91015625, -19123.978515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-21050.125417359, -19067.325822986, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-21247.4375, -18986.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-21229.001953125, -18985.681640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-21210.5, -18985.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-21192.05078125, -18984.431640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-21173.580078125, -18983.66796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-21155.0078125, -18983.361328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-20710.037109375, -18172.650390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-20631.10546875, -18066.431640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-20487.5625, -17876.705078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-20208.302734375, -18316.76953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-20752.998046875, -18720.3046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-20799.13671875, -18809.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-20842.138671875, -18954.66015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-20922.423828125, -19034.49609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-20621.189453125, -17747.060546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-20658.197265625, -17799.236328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-20956.408203125, -19134.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-20958.56640625, -19249.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-20899.78515625, -19300.826171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-20688.861328125, -18976.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-20748.201171875, -19039.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-20763.611328125, -19100.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-20674.0390625, -18873.73046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-20969.18359375, -18399.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-20931.576171875, -18349.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-20879.84765625, -18277.759765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-20842.23828125, -18231.677734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))


class Sainte_Croix_sur_Mer(Airport):
    id = 21
    name = "Sainte-Croix-sur-Mer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4100000, vhf_low_hz=39100000, vhf_high_hz=118700000, uhf_hz=250700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-18787.417239, -15106.744633, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-9', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='9', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-18935.797506538, -14425.181352241, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-18955.511437772, -14439.031926648, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-19004.161748973, -15509.879780026, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-19002.948979736, -15463.206234381, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-18625.536546824, -15580.581314405, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-18624.591604994, -15532.300417044, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-18624.430004333, -15489.321328274, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-18624.123309608, -15443.79674925, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-18624.258275852, -15397.0811564, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-18660.273262113, -14426.922800901, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-18634.698741977, -14400.814687899, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-18894.511294516, -15785.061840187, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-18908.414793946, -15797.360507503, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-18922.074238214, -15809.856372142, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-18935.835069109, -15822.157213982, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-18604.928928455, -15787.163679697, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-18706.996355159, -15769.622855667, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-18633.394119163, -15763.015251065, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-18633.253833207, -15699.960061319, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-18915.402945293, -14437.274435296, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-18874.789469465, -14471.642604775, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-18978.721779393, -15211.964090865, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-18978.078864366, -15243.371592893, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-18979.532057033, -15179.365828343, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-18979.1664727, -15147.463250805, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-18973.733149895, -15015.081893174, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-18972.140783154, -14967.830332186, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-18978.097618427, -15114.449540438, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-18978.474348139, -15081.02730831, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-18965.774424294, -14733.46598852, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-18964.266333676, -14681.125704695, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-18970.434760511, -14922.291498259, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-18967.193450077, -14784.966957763, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-18978.128408307, -15309.68685567, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-18978.867986337, -15276.235746535, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-19002.222045455, -15417.341356434, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))


class Beny_sur_Mer(Airport):
    id = 22
    name = "Beny-sur-Mer"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4125000, vhf_low_hz=39150000, vhf_high_hz=118750000, uhf_hz=250750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-21040.570312, -8437.482422, terrain), terrain)

        self.runways.append(Runway(id=None, name='35-17', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='17', heading=170, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-20698.400390625, -8236.490234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-20759.39453125, -8227.58984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-20813.50390625, -8219.935546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-20881.3203125, -8210.1083984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-21031.484375, -8814.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-20972.368349414, -8874.5303204797, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-20921.58203125, -8796.9970703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-20923.525390625, -8204.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-21359.662249457, -8095.0095004467, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-21444.09375, -8672.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-21406.73046875, -8691.7880859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-21320.145075465, -8742.24067862, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-21276.696741217, -8765.6727252319, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-21231.379649805, -8788.5991864176, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-20727.151427711, -8936.9365878649, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-20752.788242779, -8977.2135728171, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-20776.555611616, -9017.8438543908, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-21495.896484375, -8704.86328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-21025.19140625, -9066.9755859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-21090.841796875, -9001.7724609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-21101.927734375, -8899.0302734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-20850.985055549, -8856.6991496008, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-20887.1484375, -8644.783203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-21006.1640625, -8668.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-21556.87109375, -8460.3544921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-21570.9921875, -8472.0986328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-21585.109375, -8484.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-21599.060546875, -8496.1630859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-21630.1953125, -7994.4057617188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-21439.3359375, -8180.072265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-21402.728246388, -8088.1496366985, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-21382.193359375, -8261.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-21366.26171875, -8272.353515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-21441.51171875, -8216.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-21396.501953125, -8249.6201171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-21411.693359375, -8238.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-21426.572265625, -8227.2763671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-21472.224609375, -8193.802734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-21748.533203125, -8157.5395507812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-21729.90234375, -8160.0571289062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-21638.041015625, -8170.0068359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-21656.447265625, -8168.1430664062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-21674.681640625, -8166.0581054688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-21693.294921875, -8164.3134765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-21711.48828125, -8162.4111328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-21456.45703125, -8204.7333984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-21486.5390625, -8182.1708984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-21501.73046875, -8170.9536132812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-21516.60546875, -8159.8193359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))


class Rucqueville(Airport):
    id = 23
    name = "Rucqueville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4150000, vhf_low_hz=39200000, vhf_high_hz=118800000, uhf_hz=250800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-26589.313477, -19444.007812, terrain), terrain)

        self.runways.append(Runway(id=None, name='27-9', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='9', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-26680.033203125, -20167.445279634, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-26680.318359375, -20148.919328596, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-26680.7890625, -20130.249406721, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-26680.90625, -20111.15234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-26681.135408415, -20092.021434864, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-26681.295564665, -20073.439403614, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-26681.46548654, -20053.913938723, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-26532.46138726, -18758.412115575, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-26532.369054727, -18777.716770209, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-26531.84810601, -18796.80765241, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-26531.225059135, -18815.811179644, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-26531.031164102, -18835.023155595, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-26422.91198821, -19060.795778135, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-26425.420358279, -19114.55378562, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-26428.822171848, -19167.212351328, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-26442.365466328, -19550.187396838, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-26446.442318597, -19604.708761064, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-26450.242406083, -19657.260450478, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-26453.687248082, -19710.451783754, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-26457.351071384, -19761.89664453, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-26448.059404319, -19854.624955797, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-26389.2035497, -19855.109102829, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-26323.063279008, -19853.699804045, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-26325.274853953, -20139.310080314, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-26387.093973974, -20138.798356511, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-26447.351932178, -20139.73211233, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-26466.771484375, -19996.744140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-26447.294921875, -19996.451171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-26427.91796875, -19996.013671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-26408.439453125, -19995.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-26389.255859375, -19995.392578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-26369.77734375, -19995.103515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-26350.833984375, -19994.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-26331.498046875, -19993.724609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-26311.0703125, -19993.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-26490.954992227, -18759.010096065, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-26490.771398477, -18778.300191538, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-26490.343664102, -18797.114449677, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-26489.728429727, -18815.783116205, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-26489.427648477, -18834.714561845, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))


class Sommervieu(Airport):
    id = 24
    name = "Sommervieu"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4175000, vhf_low_hz=39250000, vhf_high_hz=118850000, uhf_hz=250850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-21371.758789, -26206.679688, terrain), terrain)

        self.runways.append(Runway(id=None, name='9-27', main=RunwayApproach(name='9', heading=90, beacons=[]), opposite=RunwayApproach(name='27', heading=270, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-21507.245448101, -25821.626779038, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-21185.718670235, -26311.399777583, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-21249.21484375, -26889.314453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-21501.554041851, -25723.734200913, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-21502.731776226, -25772.814279038, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-21493.426893721, -25606.617123106, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-21190.173152469, -26358.545908271, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-21194.903113267, -26403.919183839, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-21211.586713025, -26540.191914608, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-21217.208655718, -26591.486523199, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-21221.908220618, -26643.69396633, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-21221.012528839, -25535.730437291, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-21206.08203125, -25524.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-21191.595703125, -25512.58984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-21176.593241399, -25500.770975774, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-21507.876986137, -25516.406925546, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-21406.750906458, -25539.125814074, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-21481.060089025, -25542.535399381, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-21573.826171875, -26910.24609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-21544.853672918, -26884.147451757, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-21559.082427114, -26896.731134644, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-21291.142646595, -26884.419292567, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-21330.662109375, -26850.51171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-21268.29296875, -26898.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))


class Lantheuil(Airport):
    id = 25
    name = "Lantheuil"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4200000, vhf_low_hz=39300000, vhf_high_hz=118900000, uhf_hz=250900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-24264.160156, -16467.212402, terrain), terrain)

        self.runways.append(Runway(id=None, name='6-24', main=RunwayApproach(name='6', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-24663.552734375, -16906.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-24647.7890625, -16916.2265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-24631.693359375, -16925.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-24615.9765625, -16934.541015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-24470.34765625, -17017.083984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-24454.625, -17025.931640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-24438.8984375, -17035.41796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-24384.876953125, -17095.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-24496.875, -17132.98828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-24475.224609375, -17232.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-24653.60546875, -17477.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-24409.47265625, -16983.439453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-24283.244140625, -16997.78515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-24338.453125, -16882.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-24231.240234375, -16875.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-24107.36328125, -16614.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-24204.287109375, -16632.62109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-24161.091796875, -16502.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-24040.953125, -16478.146484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-23691.98046875, -16509.95703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-23415.4765625, -16464.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-23535.109375, -16176.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-24617.4140625, -16845.037109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-24629.162109375, -16737.638671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-24533.12109375, -16698.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-24707.142578125, -16403.763671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-24633.591796875, -16266.357421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-24566.673828125, -16136.291015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-24464.2265625, -15915.408203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-24388.7109375, -15793.330078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-24322.92578125, -15651.119140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-24353.671875, -15576.958007812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='Stand03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-24283.392578125, -15429.709960938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-24209.513671875, -15349.244140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-24095.677734375, -15475.010742188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-24162.7890625, -15644.055664062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-24281.287109375, -16074.471679688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-24354.265625, -16243.137695312, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-24241.630859375, -16178.12109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-24166.390625, -16049.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-24284.19921875, -16312.561523438, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-24643.9453125, -15412.844726562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-24049.91276881, -15879.438287055, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-24052.47136256, -15861.254693305, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-24046.852221935, -15897.215630805, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-24044.047534435, -15915.676568305, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-23892.515625, -16002.810546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-23874.03125, -15998.43359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-23855.80078125, -15994.41796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-23837.783203125, -15990.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-23819.765625, -15987.193359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-24066.755859375, -15779.571289062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-24063.955078125, -15798.026367188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-24365.591796875, -16468.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-24349.80078125, -16477.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-23492.82421875, -16352.380859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-23506.751953125, -16302.108398438, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-23561.73828125, -16104.012695312, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-23572.306640625, -16055.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-23584.37890625, -16005.393554688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-24289.115234375, -16945.453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-24263.6796875, -16901.72265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-24452.333984375, -15557.690429688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-24427.677734375, -15512.467773438, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-24403.439453125, -15470.97265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-24377.525390625, -15428.096679688, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))


class Evreux(Airport):
    id = 26
    name = "Evreux"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4225000, vhf_low_hz=39350000, vhf_high_hz=118950000, uhf_hz=250950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-46154.649883, 112456.803572, terrain), terrain)

        self.runways.append(Runway(id=2, name='16-34', main=RunwayApproach(name='16', heading=160, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.runways.append(Runway(id=1, name='35-21', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-46476.053813378, 112649.05916996, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-46433.745153896, 112681.65430456, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-45373.7109375, 112907.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-45320.82421875, 112904.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-45346.40625, 112905.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-45058.37109375, 112258.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-45053.62890625, 112292.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-45121.518511765, 112151.5818704, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-45120.587869981, 112130.88927727, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-46391.309516111, 112716.55712592, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-45125.555015745, 112112.56252391, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-45136.515625, 112236.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-45131.083522459, 112092.79087542, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-46658.750046144, 111797.96287631, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-46704.556423573, 111828.30671636, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-46750.183978035, 111860.14016736, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-44986.56640625, 112609.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-46347.006121069, 112755.70338164, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-44992.4921875, 112555.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-45987.82276933, 113100.51957471, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-46036.791619646, 113076.39316091, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-46247.891123235, 112961.71737627, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-46294.94705397, 112935.16874025, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-46084.516769052, 113050.10369202, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))


class Chailey(Airport):
    id = 27
    name = "Chailey"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4250000, vhf_low_hz=39400000, vhf_high_hz=119000000, uhf_hz=251000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(163883.445537, 11849.153206, terrain), terrain)

        self.runways.append(Runway(id=1, name='07-02', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='02', heading=20, beacons=[])))
        self.runways.append(Runway(id=2, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(164077.81950654, 11594.470908193, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(164053.0965293, 11609.825875996, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(164027.72960123, 11624.936067476, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(164232.69553684, 12023.485237566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(164209.54237264, 12010.861344976, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(164230.69553684, 11911.657112566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(164215.38303684, 11858.602425066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(164193.07053684, 11822.532112566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(164074.50803684, 11885.578987566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(164028.19553684, 11972.469612566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(163996.07053684, 11957.352425066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(164022.82053684, 11921.032112566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(163932.74141558, 11954.275134294, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(163868.74573081, 11999.619877707, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(163831.44553684, 12004.313362566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(163794.25979733, 12024.539283688, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(163756.23454682, 12044.987084199, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(163722.89476869, 12127.087956201, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(163735.57053684, 12096.375862566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(163678.18069047, 12105.027364768, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(163511.8756417, 12224.450707355, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(163471.89222098, 12206.453570207, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(163530.22859976, 12200.025695622, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(163541.94553684, 11854.875862566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(163570.88303684, 11858.493050066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(163540.75803684, 11895.094612566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(163631.24669901, 11863.918534518, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(163666.02648484, 11841.796016317, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(163702.86308686, 11818.722750171, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(163736.45726271, 11735.808103907, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(163767.07053684, 11735.274300066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(163738.44553684, 11777.344612566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(163824.36363057, 11745.07163843, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(163861.02551063, 11719.553283922, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(163900.13252564, 11703.152071603, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(163929.57066765, 11614.740306304, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(163957.66431075, 11616.112026569, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(163935.57053684, 11660.711800066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(163999.44553684, 11343.094612566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(164021.76601367, 11359.926979011, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(164029.79922006, 11312.142410987, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(164032.56248633, 11253.169020068, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(164015.26952262, 11211.752646437, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(164003.75803684, 11172.703987566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(163933.19553684, 11126.196175066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(163953.50803684, 11139.586800066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(163964.82053684, 11092.993050066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(164522.28006284, 11847.942060136, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(164492.94553684, 11875.868050066, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(164502.57053684, 11829.469612566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(164539.44553684, 11979.016487566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(164526.57053684, 11954.703987566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(164495.63303684, 11986.953987566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(164448.69901919, 11675.488076505, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(164441.08585305, 11754.930033769, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(164449.87648937, 11781.670458129, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))


class Needs_Oar_Point(Airport):
    id = 28
    name = "Needs Oar Point"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4275000, vhf_low_hz=39450000, vhf_high_hz=119050000, uhf_hz=251050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(140788.828125, -85142.085938, terrain), terrain)

        self.runways.append(Runway(id=2, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.runways.append(Runway(id=1, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(140762.90625, -85568.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(140754.828125, -85540.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(140719.25, -85570.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(140974.296875, -85218.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(140992.703125, -85166.5859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(140994.5625, -85110.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(141025.84375, -85093.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(141101.46875, -84967.8203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(141076.546875, -84929.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(141073.59375, -84988.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(141162.484375, -84900.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(141207.03125, -84910.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(141248.59375, -84919.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(141298.359375, -84986.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(141278.875, -84961.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(141327.828125, -84948.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(141344.375, -85025.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(141427.171875, -85020.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(141652.546875, -85044.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(141627.5625, -85024.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(141759.4375, -85071.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(141741.3125, -85049.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(141786.109375, -85036.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(140578.6875, -84821.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(140605.625, -84838.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(140579.078125, -84783.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(140653.953125, -84857.875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(140682.984375, -84853.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(140713.359375, -84822.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(140759.53125, -84832.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(140732.171875, -84877.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(140778.609375, -84867.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(140728.546875, -84910.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(140750.171875, -84949.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(140727.0625, -84988.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(140661.671875, -85003.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(140614.25, -85073, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(140582.890625, -85140.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(140604.4375, -85174.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(140608.859375, -85118.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(140637.875, -85059.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(140689.703125, -84987.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(140590.984375, -85223.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(140493.09375, -85290.1328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(140535.59375, -85283.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(140495.84375, -85318.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(140498.484375, -85383.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(140437.265625, -85397.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(140437.359375, -85423.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(140456.5625, -85384.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(140458.71875, -85454.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(140423.78125, -85464.90625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(140404.63846084, -85499.223639872, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(140407.484375, -85540.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(140386.96875, -85575.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))


class Funtington(Airport):
    id = 29
    name = "Funtington"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4300000, vhf_low_hz=39500000, vhf_high_hz=119100000, uhf_hz=251100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(152518.3125, -45583.925781, terrain), terrain)

        self.runways.append(Runway(id=None, name='8-26', main=RunwayApproach(name='8', heading=80, beacons=[]), opposite=RunwayApproach(name='26', heading=260, beacons=[])))
        self.runways.append(Runway(id=None, name='15-33', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='33', heading=330, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(152380.5656709, -45166.837526687, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(152377.66502622, -45209.439238565, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(152385.53212098, -45123.543296131, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(152388.99026974, -45083.156834022, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(152392.56309413, -45042.162678238, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(152396.40807043, -45002.191949849, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(152122.23461621, -45842.889380017, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(152131.77516199, -45881.297359835, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(152112.943858, -45807.213945696, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(152145.10328699, -45927.059078585, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(152170.68141199, -46015.066891085, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(152157.80641199, -45972.023922335, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(152697.453125, -46422.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='1', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(152713.21875, -46388.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='2', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(152727.234375, -46357.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='3', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(152742.734375, -46325.2578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='4', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(152748.84375, -46272.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='5', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(152771.28125, -46224.55078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='6', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(153157.546875, -46044.30078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(152989, -46401.78515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='8', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(153046.78125, -46284.79296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='9', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(153104.578125, -46162.45703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(151842.734375, -45794.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(151884.96875, -45918.48828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(151928.671875, -46046.16796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(151969.078125, -46170.41796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(152790.57780624, -46179.335245199, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='7', length=24.0, width=33.0, height=7.0, shelter=False))


class Tangmere(Airport):
    id = 30
    name = "Tangmere"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4350000, vhf_low_hz=39600000, vhf_high_hz=119200000, uhf_hz=251200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(150376.648438, -33743.716797, terrain), terrain)

        self.runways.append(Runway(id=2, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.runways.append(Runway(id=1, name='21-03', main=RunwayApproach(name='21', heading=210, beacons=[]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(150079.515625, -33748.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(150088.453125, -33729.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(150777.609375, -34491.34765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(150794.375, -34442.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(150770.5, -34540.5625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(150417.40625, -33291.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(150394.484375, -33292.80859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(150441.609375, -33289.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(150799.6875, -34405.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(150805.03125, -34368.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(150801.40625, -34327.66796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(150808.96875, -34274.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(150392.78125, -33345.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(150421.71875, -33343.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(150451.625, -33341.23828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))


class Ford(Airport):
    id = 31
    name = "Ford"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4375000, vhf_low_hz=39650000, vhf_high_hz=119250000, uhf_hz=251250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(147549.78125, -25817.384766, terrain), terrain)

        self.runways.append(Runway(id=1, name='23-57', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='57', heading=570, beacons=[])))
        self.runways.append(Runway(id=2, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(148026.34375, -25819.291015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(146950.140625, -25687.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(147217.3125, -26499.962890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(147196.484375, -26514.994140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(147176.53125, -26530.19140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(147156.5, -26545.248046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(147736.859375, -26209.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(148082.1875, -26020.142578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(148011.953125, -25910.275390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(147901.8125, -25880.646484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(147919.515625, -25753.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(147938.90625, -25678.228515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(147963.109375, -25603.634765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(147962.65625, -25451.201171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(147990.53125, -25330.666015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(148002.609375, -25262.54296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(148019.421875, -25226.982421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(147937.8125, -25190.892578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(147925.90625, -25164.958984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(147913.953125, -25139.158203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))


class Argentan(Airport):
    id = 32
    name = "Argentan"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4400000, vhf_low_hz=39700000, vhf_high_hz=119300000, uhf_hz=251300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-78808.183184, 22665.733434, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-78983.1875, 22682.416015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-78840.8046875, 22332.53515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-79115.226157097, 22998.606494773, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-79002.5859375, 22729.517578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-78821.46875, 22284.7578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-79105.772097741, 22980.655178703, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-79087.804246228, 22946.284390002, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-79096.703614098, 22963.459846276, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-79022.84375, 22776.2421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-78965.375, 22634.556640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-79070.28125, 22911.46484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-79061.241495199, 22894.145099774, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-79043.393866338, 22860.162900273, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-79052.213453671, 22877.29763851, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-79025.194674976, 22825.991610229, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-78933.590980798, 23065.068210843, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-78950.499307699, 23099.815689194, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-78941.895767319, 23082.383331513, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-79078.764718542, 22929.11697882, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-79034.204245615, 22842.974004716, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-78696.515625, 22250.431640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-78653.328125, 22243.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-78641.609375, 22218.228515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-78629.2890625, 22192.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-78665.234375, 22267.82421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-78669.936444904, 22201.728848187, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-78657.978071594, 22177.157367896, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-78682.346650665, 22226.379214057, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-78986.315862481, 23169.171455008, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-78977.377670181, 23151.783994447, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-78968.441455761, 23134.734474021, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-78959.5390625, 23117.064453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))


class Goulet(Airport):
    id = 33
    name = "Goulet"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4425000, vhf_low_hz=39750000, vhf_high_hz=119350000, uhf_hz=251350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-81156.733307, 16794.329582, terrain), terrain)

        self.runways.append(Runway(id=1, name='35-21', main=RunwayApproach(name='35', heading=350, beacons=[]), opposite=RunwayApproach(name='21', heading=210, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-80682.2578125, 16967.95703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-80733.0078125, 16944.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-80757.703125, 16932.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-80666.966190832, 16939.155591618, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-80716.708378332, 16915.858716618, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-80692.132791625, 16928.584883669, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-81130.3515625, 16635.5546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-81224.8515625, 16599.55078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-80828.078125, 16760.494140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-81177.859375, 16618.3203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-81493.303876694, 16490.671361988, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-81459.202936758, 16508.192832669, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-81441.017509655, 16517.163805994, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-81476.457643389, 16499.393836947, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-80781.0390625, 16779.38671875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-81423.932478613, 16526.205635694, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-81406.452683728, 16534.327427222, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-81389.28125, 16543.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-81372.388776215, 16551.729554321, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-81321.437909388, 16577.763579492, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-81355.345562916, 16560.318487628, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-81338.378641773, 16569.173270556, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-81558.152936593, 16672.908148434, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-80742.247440832, 16903.741529118, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-81575.629658804, 16664.680022695, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-81592.787666944, 16656.356166528, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-81610.0234375, 16647.62890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-81627.024367871, 16639.308128565, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-81644.171898913, 16630.510788379, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-81661.766138012, 16621.509276527, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-81272.328125, 16579.8046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-80707.8515625, 16955.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))


class Barville(Airport):
    id = 34
    name = "Barville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4450000, vhf_low_hz=39800000, vhf_high_hz=119400000, uhf_hz=251400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-109839.684309, 49363.208809, terrain), terrain)

        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.runways.append(Runway(id=2, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-109594.0078125, 49671.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-109777.96875, 49765.55078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-109670.296875, 48414.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-109768.9296875, 48437.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-109790.9296875, 48434.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-109812.65625, 48433.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-109537.8416143, 48444.647080036, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-109353.734375, 48494.03515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-109398.65625, 48482.8515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-110496.59375, 49644.23046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-110517.7421875, 49553.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-109350.046875, 49487.64453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-109315.3359375, 49457.83203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-109470.984375, 49588.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-109280.375, 49426.27734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-109507.0390625, 49616.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-110507.1328125, 49597.7109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))


class Essay(Airport):
    id = 35
    name = "Essay"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4475000, vhf_low_hz=39850000, vhf_high_hz=119450000, uhf_hz=251450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-105528.050902, 45012.608083, terrain), terrain)

        self.runways.append(Runway(id=1, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-105546.7890625, 44558.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-105543.96875, 44502.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-105548.40625, 44586.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-105580.8828125, 44526.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-105582.2265625, 44553.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-105579.171875, 44498.89453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-105683.8125, 45193.51953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-105681.9296875, 44663.148973687, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-105683.82314743, 45432.532882154, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-105683.1328125, 45142.9140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-105681.9140625, 44714.21484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-105685.078125, 45040.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-105683.1796875, 45091.55078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-105680.56958733, 45393.602189069, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-105682.4225673, 45412.988874953, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-105678.99004487, 45374.427858152, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-105670.86328673, 45279.077828148, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-105675.82996183, 45336.293899121, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-105674.17045753, 45317.19911067, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-105677.25708733, 45355.265592134, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-105672.45170753, 45298.212387832, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-105668.96484923, 45259.954562375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-105667.32422423, 45240.4435394, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-105490.49689695, 45426.061103421, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-105583.9375, 44581.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-105491.76587984, 45445.07875302, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-105492.80999163, 45464.220312377, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-105493.84766256, 45483.431727019, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-105495.03975463, 45502.381466241, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-105496.77412963, 45521.239698205, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-105498.26325243, 45540.116858442, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-105545.5625, 44531.20703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))


class Hauterive(Airport):
    id = 36
    name = "Hauterive"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4500000, vhf_low_hz=39900000, vhf_high_hz=119500000, uhf_hz=251500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-107997.579966, 40856.027628, terrain), terrain)

        self.runways.append(Runway(id=1, name='15-32', main=RunwayApproach(name='15', heading=150, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-107701.21387637, 40777.432387797, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-107731.71711672, 40800.69757551, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-107716.58704751, 40788.973756296, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-107686.00874287, 40765.600190857, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-108275.04462081, 41183.425268238, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-107715.31810414, 40545.694587334, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-107685.21370071, 40521.48277475, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-107700.27429322, 40533.339121167, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-107670.12591443, 40509.610289429, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-107654.82993792, 40497.532700332, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-107639.56614177, 40485.905165726, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-107624.13836182, 40473.958457669, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-107755.546875, 40845.0859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-107578.45164376, 40682.529102861, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-107867.0625, 40949.45703125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-108147.390625, 41203.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-107831, 40913.65234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-107793.2265625, 40878.85546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-108109.4921875, 41168.26953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-107594.37966809, 40694.597056408, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-107610.1166705, 40706.7197803, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-107625.316595, 40718.411425121, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-107640.57073982, 40729.921159287, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-107670.7890625, 40754.09765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-107655.42614566, 40742.266529465, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-108294.203125, 41156.81640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-108315.3515625, 41174.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-108358.3671875, 41209.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-108296.73165563, 41201.390344581, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-108339.50969715, 41235.79566421, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-108318.76215888, 41218.338473249, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-108336.5234375, 41191.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))


class Lymington(Airport):
    id = 37
    name = "Lymington"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4525000, vhf_low_hz=39950000, vhf_high_hz=119550000, uhf_hz=251550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(139651.4375, -90746.367188, terrain), terrain)

        self.runways.append(Runway(id=1, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[])))
        self.runways.append(Runway(id=2, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(139529.6875, -90450.015625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(139549.59375, -90471.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(139570.15625, -90492.421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(139268.953125, -90824.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(139294.59375, -90818.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(139299.84375, -90716.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(139328.375, -90669.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(139359.28125, -90640.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(139457.453125, -90732.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(139479.6875, -90827.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(139514.625, -90821.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(139498.203125, -90779.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(139576.609375, -90835.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(139626.65625, -90895.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(139661.46875, -90909.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(139692.140625, -90938.8671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(139723.578125, -90968.4609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(139734.515625, -91056.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(139730.21875, -91023.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(139783.421875, -91046.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(139913.109375, -91205.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(139956.390625, -91198.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(139901.703125, -91176.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(139979.796875, -90840.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(139950.921875, -90836.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(139970.53125, -90879.5078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(139891.203125, -90825.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(139863.328125, -90795.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(139833.75, -90763.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(139822.78125, -90674.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(139793.34375, -90666.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(139810.078125, -90714.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(139735.46875, -90661.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(139706.671875, -90627, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(139673.15625, -90601.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(139667.59375, -90508, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(139640.125, -90502.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(139649.921875, -90550.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(139670.484375, -90227.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(139644.578125, -90238.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(139649.203125, -90189.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(139661.796875, -90132.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(139689.234375, -90096.5703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(139710.453125, -90061.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(139790.65625, -90035.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(139767.5625, -90042.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(139768.71875, -89994.9296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(139034.71875, -90579.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(139055.828125, -90614.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(139058.546875, -90566.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(138984.203125, -90701.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(139002.921875, -90681.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(139024.453125, -90720.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(139150.46875, -90432.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(139137.25, -90510.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(139121.828125, -90534.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))


class Vrigny(Airport):
    id = 38
    name = "Vrigny"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4550000, vhf_low_hz=40000000, vhf_high_hz=119600000, uhf_hz=251600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-89449.457031, 25165.625977, terrain), terrain)

        self.runways.append(Runway(id=None, name='14-32', main=RunwayApproach(name='14', heading=140, beacons=[]), opposite=RunwayApproach(name='32', heading=320, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-89083.0625, 24970.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-89741.2265625, 25585.947265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-89720.5625, 25564.666015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-89141.296875, 24758.38671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-89096.9140625, 24984.990234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-89155.90625, 24772.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-89700.3515625, 25543.236328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-89184.71875, 24801.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-89198.625, 24816.169921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-89678.9375, 25520.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-89068.8203125, 24956.998046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-89054.6171875, 24943.146484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-89170.15625, 24787.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-89213.4296875, 24831.767578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-89153.125, 25040.314453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-89703.3046875, 25494.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-89195.6015625, 25082.134765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-89181.015625, 25067.65234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-89166.6640625, 25053.86328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-89724.0234375, 25516.376953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-89124.828125, 25013.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-89111.3046875, 24999.03515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-89126.5859375, 24743.837890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-89744.0546875, 25537.4765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-89765.3828125, 25559.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-89139.234375, 25027.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-89556.844132522, 25528.408776908, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-89210.46875, 25125.814453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-89309.360650073, 25243.067521939, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-89523.743335066, 25489.642155088, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-89244.665975109, 25164.959581396, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-89277.659318814, 25203.536590707, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))


class Odiham(Airport):
    id = 39
    name = "Odiham"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4575000, vhf_low_hz=40050000, vhf_high_hz=119650000, uhf_hz=251650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(193093.797089, -51833.476086, terrain), terrain)

        self.runways.append(Runway(id=1, name='28-10', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='10', heading=100, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(192617.70106807, -51476.334692121, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(192862.5, -52200.49609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(192888.84375, -52175.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(192913.40625, -52152.31640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(192937.0625, -52129.41015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(192960.9375, -52106.47265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(192985.96875, -52081.5546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(192611.12317244, -51694.808937604, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(192619.91922817, -51422.088442035, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(192612.76734358, -51636.347159812, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(192614.84026494, -51581.043885213, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(192622.00935273, -51366.706798955, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(192616.73992273, -51524.737088891, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))


class Conches(Airport):
    id = 40
    name = "Conches"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4625000, vhf_low_hz=40150000, vhf_high_hz=119750000, uhf_hz=251750000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-57037.711316, 94560.483218, terrain), terrain)

        self.runways.append(Runway(id=1, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-57048.011983033, 95159.09477206, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=39.857483, width=42.0, height=13.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-57465.18359375, 94518.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-57429.0625, 94513.328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-57395.8046875, 94508.3203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-57363.1953125, 94503.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-57330.3671875, 94499.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-57295.3125, 94495.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-57220.198411419, 95023.58459672, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-57001.400113475, 95186.400226503, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-57175.344003031, 95059.219892526, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-57130.259851058, 95095.032029942, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-56957.354326224, 95222.396008971, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-57086.303946028, 95129.006197415, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=39.857483, width=42.0, height=13.0, shelter=False))


class West_Malling(Airport):
    id = 41
    name = "West Malling"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4650000, vhf_low_hz=40200000, vhf_high_hz=119800000, uhf_hz=251800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(200585.023428, 41958.844877, terrain), terrain)

        self.runways.append(Runway(id=1, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(200828.25, 41805.25390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(200682.421875, 41512.11328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(200120.0625, 41655.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(200202.828125, 41602.85546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(200249.28125, 41764.4296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(201440.453125, 41763.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(201469.5625, 41756.33984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(201519.28125, 41816.23046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(201505.578125, 41845.5234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(201264.71875, 42439.04296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(201210.96875, 42531.09765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))


class Villacoublay(Airport):
    id = 42
    name = "Villacoublay"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4675000, vhf_low_hz=40250000, vhf_high_hz=119850000, uhf_hz=251850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-70139.621094, 186884.203125, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-69834.2265625, 188256.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-69802.5, 188175.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-69719.6015625, 188157.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-69737.84375, 188285.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-69634.65625, 187977.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-69590.65625, 187863.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-69520.109375, 187760.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-69454.234375, 188167.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-69325.9609375, 188105.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-69468.5703125, 188036.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-69284.875, 187975.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-69204.578125, 188018.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-70867.6328125, 186900.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-70766.9609375, 187027.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-70743.1484375, 186930.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-70687.1640625, 186871.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-70603.59375, 186935.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-70667, 187034.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-70342.9375, 186243.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-70387.4609375, 186122.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-70420.828125, 186038.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-70407.03125, 185984.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-70342.59375, 185897.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-69966.171875, 185683.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-69916.4296875, 185535.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-69902.5234375, 185433.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-69890.21875, 185363.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-69881.3671875, 185281.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-69820.453125, 185259.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-69697.2109375, 185375.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-69726.4140625, 185473.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-69782.9453125, 185518.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-69819.3984375, 185587.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-69836.3984375, 185671.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-69753.8203125, 185823.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-69509.3515625, 185490.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-68886.28125, 186829.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-68881.40625, 186777.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-68875.0703125, 186720.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-68875.6796875, 186667.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-68871.5546875, 186623.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-68867.3515625, 186579.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-68863.03125, 186536.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-68858.6015625, 186246.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-68855.9765625, 186197.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-68852.984375, 186151.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-68850.875, 186106.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-68894.796875, 186961.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-68891.9375, 186921.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-68889.203125, 186882.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-69661.1328125, 185525.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-69670.2578125, 185560.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-69679.390625, 185594.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-69688.875, 185629.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-69351.0390625, 185148.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-69386.8046875, 185183.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-69421.328125, 185217.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-69485.6875, 185283.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-69200.890625, 185002.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-69232.890625, 185033.984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-69267.828125, 185068.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-69060.609375, 184847.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-69086.9140625, 184874.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-69113.1015625, 184900.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-68965.8671875, 184984.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-69555.6171875, 185639.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-68769.640625, 184984, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-68770.25, 185022.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-68770.7734375, 185061.53125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-68771.3046875, 185099.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-68771.7421875, 185136.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-69011.5546875, 186996.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-69010.2734375, 187028.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-69009.0078125, 187058.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-69504.1796875, 188282.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-69453, 185251.203125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))


class Kenley(Airport):
    id = 43
    name = "Kenley"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4700000, vhf_low_hz=40300000, vhf_high_hz=119900000, uhf_hz=251900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(202826.03125, 6852.842529, terrain), terrain)

        self.runways.append(Runway(id=2, name='02-08', main=RunwayApproach(name='02', heading=20, beacons=[]), opposite=RunwayApproach(name='08', heading=80, beacons=[])))
        self.runways.append(Runway(id=2, name='02-30', main=RunwayApproach(name='02', heading=20, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(202595.78125, 6970.4379882812, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(202611.53125, 7004.5336914062, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(202626.796875, 7037.8247070312, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(202642.140625, 7070.927734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(202574.15625, 7209.626953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(202539.765625, 7139.162109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(202496.671875, 7003.9350585938, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(202527.578125, 7113.6704101562, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(202515.15625, 7087.8588867188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(202500.59375, 7057.6005859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(202552.09375, 7165.01171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))


class Beauvais_Tille(Airport):
    id = 44
    name = "Beauvais-Tille"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4725000, vhf_low_hz=40350000, vhf_high_hz=119950000, uhf_hz=251950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(5710.25293, 174980.65625, terrain), terrain)

        self.runways.append(Runway(id=2, name='22-4', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='4', heading=40, beacons=[])))
        self.runways.append(Runway(id=1, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(6262.09375, 174787.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(6240.2470703125, 174962.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(6145.9399414062, 174568.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(6315.8081054688, 174551.40625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(6204.5229492188, 174864.34375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(6166.85546875, 174959.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(6142.0463867188, 174940.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(6138.4418945312, 174867.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(6113.322265625, 174927.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(6196.3510742188, 174782.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(6181.6088867188, 174806.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(6123.185546875, 174894.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(6187.7958984375, 174980.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))


class Cormeilles_en_Vexin(Airport):
    id = 45
    name = "Cormeilles-en-Vexin"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4750000, vhf_low_hz=40400000, vhf_high_hz=120000000, uhf_hz=252000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-34766.40625, 172022.796875, terrain), terrain)

        self.runways.append(Runway(id=1, name='11-29', main=RunwayApproach(name='11', heading=110, beacons=[]), opposite=RunwayApproach(name='29', heading=290, beacons=[])))
        self.runways.append(Runway(id=2, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-34311.79296875, 172471.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-35129.44140625, 172224.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-35082.5625, 172263.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-35036.859375, 172302.15625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-34990.3359375, 172341.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-34944.6953125, 172379.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-34898.1484375, 172417.8125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-34851.6328125, 172456.125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-34805.6484375, 172494.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-34975.65625, 172504.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-34930.52734375, 172544.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-34884.62890625, 172582.765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-33932.37109375, 171908.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-33965.4296875, 172002.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-33903.4609375, 172035.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))


class Creil(Airport):
    id = 46
    name = "Creil"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4775000, vhf_low_hz=40450000, vhf_high_hz=120050000, uhf_hz=252050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-14505.020996, 205999.304688, terrain), terrain)

        self.runways.append(Runway(id=None, name='05-03', main=RunwayApproach(name='05', heading=50, beacons=[]), opposite=RunwayApproach(name='03', heading=30, beacons=[])))
        self.runways.append(Runway(id=None, name='33-15', main=RunwayApproach(name='33', heading=330, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-14967.24609375, 205900.046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='75', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-14978.885742188, 205878.546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='76', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-14990.04296875, 205856.796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='77', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-15003.33984375, 205818.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-14639.576171875, 206523.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-14050.696289062, 207396.4375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-14016.75390625, 207402.328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-14176.767578125, 207244.6875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-14276.419921875, 207185.296875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14610.1484375, 206573.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14734.416015625, 206305.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14903.53515625, 205993.375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='73', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14853.870117188, 206130.734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14826.2734375, 206180.96875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-14391.250976562, 207140.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-14428.768554688, 207213.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-14458.497070312, 207295.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-14466.990234375, 207391.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-14406.911132812, 207487.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-14353.295898438, 207545.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-14255.956054688, 207580.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-14172.5078125, 207549.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-14138.038085938, 207306.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-14193.94921875, 207374.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-14224.322265625, 207448.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-14277.534179688, 207460.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-14346.701171875, 207394.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-14329.267578125, 207288.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-13953.630859375, 205885.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-14272.662109375, 205480.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-14153.848632812, 205368.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-14116.861328125, 205291.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-14294.073242188, 205363.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-14184.846679688, 205419.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-14242.206054688, 205295.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-14214.047851562, 205221.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-14217.755859375, 205139.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-14249.786132812, 205064.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-13878.625, 206183.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-13939.028320312, 206083.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-13864.771484375, 206046.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-13781.850585938, 206050.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-13714.459960938, 206092, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-13802.395507812, 206166.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-13735.298828125, 206244, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-13707.80078125, 206344.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-13748.3984375, 206417.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-13656.55078125, 206154.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-13617.526367188, 206222.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-13597.735351562, 206301.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-13601.922851562, 206379.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-13640.368164062, 206451.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-13651.268554688, 206532.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-13642.43359375, 206612.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-13947.924804688, 205816.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-13955.713867188, 205769.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-13962.881835938, 205724.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-13971.727539062, 205678.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-13978.99609375, 205631.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-13986.342773438, 205586.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-13754.016601562, 206764.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-13642.30859375, 206851.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-13660.674804688, 206936.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-13739.5625, 207026.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-14101.500976562, 207086.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-13788.599609375, 206917.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-15290.245117188, 204973.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-15310.125976562, 205182.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-15349.337890625, 205107.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-15308.97265625, 205017.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-15207.4765625, 205108.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-14911.240234375, 204916.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-14955.8671875, 204795.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-14819.525390625, 204873.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-14841.149414062, 204761.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-14746.83203125, 204774.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-14931.790039062, 205942.65625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-14708.107421875, 206352.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=7.0, shelter=False))


class Guyancourt(Airport):
    id = 47
    name = "Guyancourt"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4800000, vhf_low_hz=40500000, vhf_high_hz=120100000, uhf_hz=252100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-71717.359375, 177759.757812, terrain), terrain)

        self.runways.append(Runway(id=2, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.runways.append(Runway(id=3, name='07-250', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='250', heading=2500, beacons=[])))
        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-71322.0078125, 177463.71875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-71299.3671875, 177485.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-71275.734375, 177505.75, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-71406.5859375, 177331.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-71397.3515625, 177366.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-71386.171875, 177400.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-71375.15625, 177435.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))


class Lonrai(Airport):
    id = 48
    name = "Lonrai"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4825000, vhf_low_hz=40550000, vhf_high_hz=120150000, uhf_hz=252150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-112074.119908, 28981.238521, terrain), terrain)

        self.runways.append(Runway(id=1, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-111873.48958364, 29536.287323808, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-111885.89013091, 29515.6933843, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-111897.96044341, 29494.339868675, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-111908.38500823, 29473.730127191, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-112217.3399263, 28924.643822644, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-112230.77538268, 28903.843280412, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-112242.28854629, 28882.369569279, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-112253.00100584, 28860.586155472, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-112169.640625, 29109.005859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-112146.34375, 29150.41796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-112116.2578125, 29203.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-112092.84375, 29244.669921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-112065.34375, 29293.8046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-112042.140625, 29334.8359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))


class Dinan_Trelivan(Airport):
    id = 49
    name = "Dinan-Trelivan"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4850000, vhf_low_hz=40600000, vhf_high_hz=120200000, uhf_hz=252200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-118842.234375, -129198.449219, terrain), terrain)

        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-118586.6171875, -129182.96875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-118592.61814178, -129208.52526636, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-118581.828125, -129153.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-118559.62457268, -129024.24326762, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-118562.296875, -129076.90239326, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-118562.6875, -128953.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-118656.3487953, -129316.6116531, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-118667.7109375, -129333.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-118678.99128104, -129349.34007634, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-118722.58363549, -129300.24769799, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-118706.56801049, -129277.95265981, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-118610.1931409, -129266.25611039, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-118623.92260017, -129045.31252391, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-118639.79803441, -129057.90195073, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-118737.67831586, -129322.13374287, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-118562.3984375, -129050.18354424, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-118607.28125, -129291.53125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))


class Fecamp_Benouville(Airport):
    id = 51
    name = "Fecamp-Benouville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4900000, vhf_low_hz=40700000, vhf_high_hz=120300000, uhf_hz=252300000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(31017.939453, 46236.578125, terrain), terrain)

        self.runways.append(Runway(id=None, name='36-18', main=RunwayApproach(name='36', heading=360, beacons=[]), opposite=RunwayApproach(name='18', heading=180, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(30553.982421875, 46407.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(30586.41015625, 46419.99609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(30614.54296875, 46385.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(30716.740234375, 46395.08984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(30685.271484375, 46407.44140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(30766.869140625, 46366.87890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(30809.087890625, 46366.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(30855.2578125, 46367.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(30981.88671875, 46367.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(31023.7578125, 46368.14453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(31070.34765625, 46368.26171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(31367.447265625, 46345.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(31412.794921875, 46352.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(31453.949386049, 46356.17842574, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(31306.330078125, 46437.78125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(31351.279296875, 46439.26953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(31396.41796875, 46439.76171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(31502.703125, 46452.601475102, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(31450.780408452, 46451.613532919, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))


class Farnborough(Airport):
    id = 52
    name = "Farnborough"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4925000, vhf_low_hz=40750000, vhf_high_hz=120350000, uhf_hz=252350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(198359.484375, -40320.855469, terrain), terrain)

        self.runways.append(Runway(id=None, name='24-6', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='6', heading=60, beacons=[])))
        self.runways.append(Runway(id=None, name='17-35', main=RunwayApproach(name='17', heading=170, beacons=[]), opposite=RunwayApproach(name='35', heading=350, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(198847.265625, -39465.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(198831.875, -39373.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(198832.125, -39307.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(198847.203125, -39503.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(198905.3125, -39584.15234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(198884.640625, -39561.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(198863.9375, -39540.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(198847.21875, -39427.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))


class Friston(Airport):
    id = 53
    name = "Friston"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4950000, vhf_low_hz=40800000, vhf_high_hz=120400000, uhf_hz=252400000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(143314.552925, 28131.333438, terrain), terrain)

        self.runways.append(Runway(id=1, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(142996.28068421, 27699.255676396, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(143007.51191749, 27719.406222191, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(143018.88896152, 27740.234908029, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(143030.36401891, 27760.836668783, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(143041.75775379, 27782.005533566, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(143052.8212539, 27801.617985575, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(143600.41371536, 28434.121050349, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(143065.68821091, 27822.038410667, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(143305.81803447, 27863.462449786, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(143295.06027674, 27845.46523407, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(143284.84333966, 27827.221822171, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(143274.48258006, 27809.638785336, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(143264.39667542, 27792.091250901, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(143253.69259614, 27774.251591918, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(143242.63374588, 27756.391936499, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(143232.1142731, 27737.816862274, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(143221.53919898, 27719.323392563, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(143211.6941102, 27700.965931079, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(143201.35316206, 27683.048824732, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(143646.67792542, 28316.665469651, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(143618.17792542, 28273.763125901, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(143440.24042542, 27999.919375901, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(143410.58417542, 27958.692813401, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(143382.14667542, 27915.903750901, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(143354.70917542, 27873.360782151, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(143617.01221244, 28461.117342141, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(143633.92518741, 28488.070071905, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(143649.43705469, 28516.016373769, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(143624.68248788, 28530.0162384, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(143608.49139064, 28502.41857787, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(143592.46390364, 28475.533857077, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(143575.94250304, 28448.808186925, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Deanland(Airport):
    id = 54
    name = "Deanland"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=4975000, vhf_low_hz=40850000, vhf_high_hz=120450000, uhf_hz=252450000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(156912.962846, 26832.963152, terrain), terrain)

        self.runways.append(Runway(id=1, name='22-34', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='34', heading=340, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(157212.546875, 27125.49609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(157231.28125, 27149.888671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(157250.078125, 27174.310546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(157268.25, 27198.818359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(157291.4375, 27182.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(157273.328125, 27157.568359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(157254.734375, 27132.833984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(156929.796875, 26574.873046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(156961.703125, 26614.169921875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(156994.609375, 26653.591796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(157028.609375, 26691.353515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(157235.296875, 26944.173828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(157268.328125, 26983.728515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(156754.515625, 26400.638671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(156766.71875, 26417.216796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(156778.828125, 26433.876953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(156791.265625, 26450.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(156803.4375, 26467.390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(156816.1875, 26483.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(156828.546875, 26500.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(156840.75, 26517.14453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(156852.765625, 26533.619140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(156864.703125, 26550.41796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(156876.90625, 26566.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(156628.984375, 26543.689453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(157236.140625, 27107.76171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(156615.453125, 26527.322265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(156603.171875, 26510.095703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(156591.046875, 26492.755859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(156578.46875, 26475.26953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(156566.59375, 26458.04296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(156553.796875, 26439.779296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))


class Triqueville(Airport):
    id = 55
    name = "Triqueville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5000000, vhf_low_hz=40900000, vhf_high_hz=120500000, uhf_hz=252500000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-14226.603516, 55691.503906, terrain), terrain)

        self.runways.append(Runway(id=1, name='34-15', main=RunwayApproach(name='34', heading=340, beacons=[]), opposite=RunwayApproach(name='15', heading=150, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-14705.537109375, 55939.05859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-14685.166015625, 55931.62890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-14664.919921875, 55924.3828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-14644.606445312, 55916.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-14624.958007812, 55909.59765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-14604.49609375, 55901.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-13884.202148438, 55450.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-14584.291015625, 55892.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-14503.845703125, 55656.10546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-14527.28125, 55664.91796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-14549.239257812, 55672.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-14569.028320312, 55680.21484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-14589.435546875, 55688.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-14609.37890625, 55696.22265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-14629.600585938, 55703.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-14649.911132812, 55712.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-14670.053710938, 55720.1328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-14690.473632812, 55728.91015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-14709.33203125, 55738.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-13992.20703125, 55393.109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-14037.961914062, 55416.46875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-14335.823242188, 55551.0625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-14380.845703125, 55576.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-14425.71875, 55596.6484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-14474.032226562, 55616.40234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-13854.411132812, 55438.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-13825.212890625, 55427.35546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-13795.788085938, 55416.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-13784.91796875, 55444.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-13813.325195312, 55455.37890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-13843.33984375, 55467.59765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-13873.290039062, 55479.55859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Poix(Airport):
    id = 56
    name = "Poix"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5025000, vhf_low_hz=40950000, vhf_high_hz=120550000, uhf_hz=252550000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(45570.672226, 162442.924569, terrain), terrain)

        self.runways.append(Runway(id=2, name='27-09', main=RunwayApproach(name='27', heading=270, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.runways.append(Runway(id=1, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(46122.9296875, 163000.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(45523.750675538, 163346.24748948, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(46004.495043814, 163057.41436029, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(45485.757625146, 163306.50566729, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(46109.8828125, 163016.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(46093.5625, 163030.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(45554.806592866, 163380.5082223, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(45376.613025694, 161537.61717466, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(45429.570893301, 161554.98839077, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(45481.485488129, 161573.40639604, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(44805.386287243, 162818.19363609, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(44769.670165708, 162526.32719064, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(44774.948665592, 162579.75396917, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(44799.190250115, 162764.36748899, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(44811.511738921, 162872.80425245, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(46044.255807868, 163149.73513409, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(46015.74810492, 163174.67082118, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(44892.380275478, 162321.11148477, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(44895.382016549, 162279.97216874, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(44889.46889938, 162369.05260975, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(44898.48546381, 162237.68816198, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(45835.093735076, 163366.01263996, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(45795.213210474, 163400.98402369, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(46135.859375, 162985.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))


class Orly(Airport):
    id = 57
    name = "Orly"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5050000, vhf_low_hz=41000000, vhf_high_hz=120600000, uhf_hz=252600000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-72761.085938, 200856.46875, terrain), terrain)

        self.runways.append(Runway(id=2, name='01-19', main=RunwayApproach(name='01', heading=10, beacons=[]), opposite=RunwayApproach(name='19', heading=190, beacons=[])))
        self.runways.append(Runway(id=1, name='07-25', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='25', heading=250, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-72146.8515625, 199597.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-72336.96875, 199464.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-72257.28125, 199578.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-72103.171875, 199577.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-72073.234375, 199708.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-71978.6484375, 199759.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-71882.296875, 199769.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-71838.140625, 199864.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-72391.265625, 199520.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-72543.734375, 199425.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='57', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-72629.6328125, 199439.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-72702.7734375, 199503.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-72798.1171875, 199427.5, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-71962.828125, 200008.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='76', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-72417.6171875, 199779.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='61', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-72083.625, 199961.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='75', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-72333.8984375, 199726.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-71893.0390625, 200036.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='77', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-73028.0078125, 201595.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-73186.5, 201589.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-73325.65625, 201627.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-73393.859375, 201774.25, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-73586.640625, 202058.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-73543.328125, 201967.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-74760.1640625, 201430.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-74814.0703125, 201263.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-74935.3515625, 201307.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-74948.5234375, 201363.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-74966.859375, 201220.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-74954.4453125, 201082.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-74938.109375, 200995.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-75094.0390625, 201077.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-75240.7890625, 200937, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-75361.0078125, 200905.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-74847.5703125, 200674.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-73648.0859375, 201915.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-72575.6796875, 199707.640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='62', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-73311.140625, 201339.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-71786.703125, 199782.515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='73', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-71836.5625, 200082.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='78', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-72744.4609375, 199333.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-73080.78125, 199359.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-73964.3359375, 200048.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-73907.390625, 199907.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-73947.625, 199411.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-74014.75, 199420.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-74262.25, 199388.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-74299.2734375, 199392.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-74336.78125, 199397.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-74678.3359375, 201426.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-73197.2265625, 199267.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-73178.3359375, 199265.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-73159.5078125, 199262.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-73140.78125, 199260.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-73232.4609375, 199271.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-73260.2109375, 199275.546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-72923.4765625, 199406.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='47', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-72916.3046875, 199428.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='48', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-72908.890625, 199449.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='49', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-72901.8984375, 199469.984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='50', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-72893.5234375, 199494.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='51', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-72928.15625, 199504.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-72950.3125, 199462.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-72939.1484375, 199485.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-72908.1640625, 199540.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='46', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-72917.8515625, 199523.28125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='45', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-72848.0390625, 199343.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='52', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-71750.3203125, 199550.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-71752.4375, 199579.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-71754.046875, 199608.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='70', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-71755.5625, 199638.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-73001.75, 199252.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-72979.203125, 199249.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-73042.6953125, 199258.859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-73022.921875, 199256.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-72956.9375, 199246.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-72935.1796875, 199242.875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-72946.3828125, 199341.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='41', length=24.0, width=33.0, height=7.0, shelter=False))


class Stoney_Cross(Airport):
    id = 58
    name = "Stoney Cross"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5075000, vhf_low_hz=41050000, vhf_high_hz=120650000, uhf_hz=252650000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(155989.046875, -101186.269531, terrain), terrain)

        self.runways.append(Runway(id=2, name='19-24', main=RunwayApproach(name='19', heading=190, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.runways.append(Runway(id=1, name='06-24', main=RunwayApproach(name='06', heading=60, beacons=[]), opposite=RunwayApproach(name='24', heading=240, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(156237.71875, -101166.265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(155773.5, -101826.015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(155799.3125, -101717.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(155873.484375, -101811.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(155956.125, -101604.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(155899.859375, -101701.0390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(156025.875, -101509.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(155917.546875, -101495.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(156158.796875, -101300.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(156103.125, -101403.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(155996.21875, -101406.9765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(156213.15625, -101194.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(156051.53125, -101313.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(156110.171875, -101199.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(156639.25, -101022.0390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(155641.015625, -101484.5078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(155651.90625, -101435.7734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(155705.078125, -101274.3046875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(156068.84375, -101462.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(156256.6875, -101130.609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(155994.796875, -101558.1875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(156421.890625, -101033.1171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(156265.71875, -101091.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(156159.46875, -101104.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(156363.296875, -101035.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(156480.625, -101008.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(156584.90625, -100999.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(156696.609375, -101018.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(156268.3125, -100966.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(156402.8125, -100936.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(156811.40625, -101039.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(156949.015625, -101023.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(155678.0625, -101615.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(155812.234375, -101267.1015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(155525.953125, -101720.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(155781.78125, -101381.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(155744.8125, -101508.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(156650.90625, -100925.6484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(156767.125, -100945.21875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=7.0, shelter=False))


class Amiens_Glisy(Airport):
    id = 59
    name = "Amiens-Glisy"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5100000, vhf_low_hz=41100000, vhf_high_hz=120700000, uhf_hz=252700000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(53847.228516, 191583.054688, terrain), terrain)

        self.runways.append(Runway(id=2, name='02-20', main=RunwayApproach(name='02', heading=20, beacons=[]), opposite=RunwayApproach(name='20', heading=200, beacons=[])))
        self.runways.append(Runway(id=1, name='28-09', main=RunwayApproach(name='28', heading=280, beacons=[]), opposite=RunwayApproach(name='09', heading=90, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(53330.36328125, 191856.171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(53325.953125, 191680.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(53477.8828125, 192055.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(53312.52734375, 192097.890625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(53375.85546875, 191771.84375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(53398.8359375, 191671.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(53426.2265625, 191686.9375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(53440.79296875, 191759.296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(53456.64453125, 191696.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(53396.12890625, 191851.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(53407.078125, 191825.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(53451.76953125, 191729.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(53375.01171875, 191654.171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))


class Ronai(Airport):
    id = 60
    name = "Ronai"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5150000, vhf_low_hz=41200000, vhf_high_hz=120800000, uhf_hz=252800000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-73103.863029, 12831.820116, terrain), terrain)

        self.runways.append(Runway(id=1, name='25-07', main=RunwayApproach(name='25', heading=250, beacons=[]), opposite=RunwayApproach(name='07', heading=70, beacons=[])))
        self.runways.append(Runway(id=2, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-72758.3125, 13024.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-72892.5234375, 13181.384765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-73307.166825714, 11889.698160126, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-73389.21875, 11949.977539062, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-73410.6796875, 11955.635742188, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-73431.4140625, 11962.322265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-73169.937103915, 11871.834873531, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-72983.8203125, 11844.077148438, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-73029.6171875, 11850.82421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-73602.931830133, 13342.7933149, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-73657.53125, 13266.23828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-72602.4765625, 12761.599609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-72581.71875, 12720.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-72675.90625, 12901.001953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-72561.3828125, 12678.3515625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-72698.46875, 12940.918945312, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-73630.71875, 13303.510742188, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))


class Rouen_Boos(Airport):
    id = 61
    name = "Rouen-Boos"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5175000, vhf_low_hz=41250000, vhf_high_hz=120850000, uhf_hz=252850000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-5907.391602, 107717.90625, terrain), terrain)

        self.runways.append(Runway(id=1, name='22-04', main=RunwayApproach(name='22', heading=220, beacons=[]), opposite=RunwayApproach(name='04', heading=40, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-5450.1596679688, 108003.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-5466.9482421875, 107989.8359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-5483.5043945312, 107976.1171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-5500.4111328125, 107962.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-5516.6088867188, 107949.2890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-5533.7529296875, 107935.6640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-6289.724609375, 107546.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-5551.84765625, 107922.90625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-5796.4145507812, 107974.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-5776.8803710938, 107990.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-5759.0668945312, 108005.046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-5742.427734375, 108018.1875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-5725.1713867188, 108031.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-5708.0834960938, 108044.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-5691.08984375, 108058.1640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-5673.60546875, 108071.40625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-5656.5654296875, 108084.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-5638.6020507812, 108097.8125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-5620.435546875, 108108.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-6283.6108398438, 107668.5078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-6240.1791992188, 107695.9453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-5972.4755859375, 107883.484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-5927.9389648438, 107909.4140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-5887.41015625, 107937.5546875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-5845.7709960938, 107969.03125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-6314.8715820312, 107526.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-6339.3349609375, 107507.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-6363.9541015625, 107487.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-6345.482421875, 107464.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-6321.3017578125, 107482.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-6295.482421875, 107502.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-6269.9096679688, 107522.125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Deauville(Airport):
    id = 62
    name = "Deauville"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5200000, vhf_low_hz=41300000, vhf_high_hz=120900000, uhf_hz=252900000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-12067.121558, 33696.617711, terrain), terrain)

        self.runways.append(Runway(id=None, name='12-30', main=RunwayApproach(name='12', heading=120, beacons=[]), opposite=RunwayApproach(name='30', heading=300, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-12125.049804688, 33373.1640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-12141.852539062, 33421.71484375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-11967.440429688, 33253.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))


class Saint_Aubin(Airport):
    id = 63
    name = "Saint-Aubin"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5225000, vhf_low_hz=41350000, vhf_high_hz=120950000, uhf_hz=252950000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(49020.731342, 97561.316092, terrain), terrain)

        self.runways.append(Runway(id=None, name='31-12', main=RunwayApproach(name='31', heading=310, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(49025.50390625, 97895.359375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(49049.19140625, 97849.7734375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(48852.1875, 97990.625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(48827.125, 97974.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))


class Flers(Airport):
    id = 64
    name = "Flers"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5250000, vhf_low_hz=41400000, vhf_high_hz=121000000, uhf_hz=253000000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-82446.199219, -18789.142578, terrain), terrain)

        self.runways.append(Runway(id=1, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-82075.3046875, -18397.857421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-82088.109375, -18415.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-82100.6953125, -18432.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-82113.6484375, -18450.1953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-82126.0078125, -18467.07421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-82139.1796875, -18484.564453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-82773.28125, -19050.970703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-82153.4921875, -18501.458984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-82403.1640625, -18512.982421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-82388.1796875, -18492.919921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-82374.6953125, -18473.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-82361.890625, -18457.06640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-82348.5703125, -18439.67578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-82335.3046875, -18422.751953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-82322.2265625, -18405.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-82308.625, -18388.2734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-82295.4765625, -18371.111328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-82281.375, -18353.931640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-82266.5859375, -18338.578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-82797.96875, -18931.39453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-82762.8203125, -18893.931640625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-82550.7578125, -18645.201171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-82514.15625, -18608.91796875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-82481.9921875, -18571.51171875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-82449.5859375, -18530.58984375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-82792.671875, -19076.37109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-82811.46875, -19101.330078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-82830.3828125, -19126.4921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-82806.578125, -19144.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-82787.859375, -19120.533203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-82767.78125, -19095.095703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-82747.9609375, -19069.650390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Avranches_Le_Val_Saint_Pere(Airport):
    id = 65
    name = "Avranches Le Val-Saint-Pere"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5275000, vhf_low_hz=41450000, vhf_high_hz=121050000, uhf_hz=253050000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-92981.292969, -76298.9375, terrain), terrain)

        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-92711.4921875, -76765.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-92724.640625, -76748.453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-92737.78125, -76731.4375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-92750.78125, -76714.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-92763.453125, -76697.4296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-92776.484375, -76679.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-93139.4140625, -75910.953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-92788.6171875, -76661.3125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-92728.734375, -76418.65625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-92713.7578125, -76438.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-92699.40625, -76457.03125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-92686.8515625, -76474.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-92673.9609375, -76491.8203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-92661.5, -76509.34375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-92648.65625, -76526.7890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-92636.0234375, -76544.71875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-92623.3046875, -76562.2109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-92610.8359375, -76580.609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-92600.3125, -76599.1484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-93017.75, -75921.25, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-92991.8125, -75965.59375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-92813.578125, -76239.578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-92789.1875, -76284.9765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-92762.4609375, -76326.4453125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-92732.4296875, -76369.140625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-93158.2578125, -75885.140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-93176.84375, -75860.0234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-93195.6015625, -75834.75, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-93219.8125, -75852.3984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-93201.9609375, -75877.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-93183.28125, -75903.6796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-93164.515625, -75929.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))


class Gravesend(Airport):
    id = 66
    name = "Gravesend"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5300000, vhf_low_hz=41500000, vhf_high_hz=121100000, uhf_hz=253100000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(216978.257812, 40643.498047, terrain), terrain)

        self.runways.append(Runway(id=1, name='24-06', main=RunwayApproach(name='24', heading=240, beacons=[]), opposite=RunwayApproach(name='06', heading=60, beacons=[])))
        self.runways.append(Runway(id=1, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[]), opposite=RunwayApproach(name='36', heading=360, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(216215.5, 40828.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(216281.625, 40834.19140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(216341.171875, 40823.0546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(216390.875, 40865.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(216452.765625, 40846.3359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(216485.953125, 40886.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(216538.890625, 40884.09375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(216555.625, 40932.48828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(216600.734375, 40938.84375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(217398.96875, 41367.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(217388.1875, 41295.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(217327.578125, 41266.56640625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(217256.890625, 41164.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(217239.296875, 41101.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(217183.90625, 41050.95703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(217202.578125, 40944.22265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(217197.734375, 40884.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(217485.234375, 40764.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(217550.328125, 40794.12890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(217633.34375, 40758.69140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(217694.953125, 40788.6015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(217660.421875, 40465.7109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(217577.234375, 40426.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(217520.71875, 40436.46484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(217508.609375, 40324.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='40', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(217530.609375, 40251.01953125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='41', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(217479.046875, 40350.98828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='39', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(217451.71875, 40286.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(217298.40625, 40254.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(217275.546875, 40122.2109375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='33', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(217205.265625, 40126.86328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='32', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(217104.6875, 40138.7265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(216874.28125, 40089.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(216801.34375, 40105.74609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(216839.21875, 39997.09375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='29', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(216759.921875, 40019.859375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='27', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(216712.3125, 40067.17578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(216664.015625, 40049.2265625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='25', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(216663.625, 40185.18359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(216553.25, 40180.28125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(217320.25, 40175.28515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(217424.65625, 40178.84765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='36', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(217439.875, 40195.375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='37', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(217358.21875, 41236.25390625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))


class Beaumont_le_Roger(Airport):
    id = 67
    name = "Beaumont-le-Roger"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5325000, vhf_low_hz=41550000, vhf_high_hz=121150000, uhf_hz=253150000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-39697.355469, 81625.679688, terrain), terrain)

        self.runways.append(Runway(id=2, name='04-22', main=RunwayApproach(name='04', heading=40, beacons=[]), opposite=RunwayApproach(name='22', heading=220, beacons=[])))
        self.runways.append(Runway(id=3, name='07-250', main=RunwayApproach(name='07', heading=70, beacons=[]), opposite=RunwayApproach(name='250', heading=2500, beacons=[])))
        self.runways.append(Runway(id=1, name='13-31', main=RunwayApproach(name='13', heading=130, beacons=[]), opposite=RunwayApproach(name='31', heading=310, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-40130.7109375, 81862.6328125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-40150.01171875, 81837.828125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-40170.546875, 81814.4609375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-40065.671875, 82005.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-40069.86328125, 81969.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-40076.12109375, 81934.0703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-40082.140625, 81898.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))


class Broglie(Airport):
    id = 68
    name = "Broglie"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5350000, vhf_low_hz=41600000, vhf_high_hz=121200000, uhf_hz=253200000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-49720.132812, 60287.275391, terrain), terrain)

        self.runways.append(Runway(id=1, name='30-12', main=RunwayApproach(name='30', heading=300, beacons=[]), opposite=RunwayApproach(name='12', heading=120, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-49896.807116029, 60302.937889971, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-49752.7578125, 59954.078125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-50027.1640625, 60620.15234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-49916.358957641, 60349.748269249, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-49735.816324086, 59905.13604836, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-50017.7265625, 60602.19921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-49999.7578125, 60567.828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-50008.6484375, 60585.00390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-49936.412813387, 60396.881274997, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-49877.3203125, 60256.09765625, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-49982.2265625, 60533.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-49973.1953125, 60515.6875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-49955.3359375, 60481.70703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-49964.1640625, 60498.83984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-49937.1328125, 60447.53515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-49845.5390625, 60686.61328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-49862.4453125, 60721.359375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-49853.8515625, 60703.92578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-49990.7109375, 60550.66015625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-49946.1484375, 60464.51953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-49608.4609375, 59871.97265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-49565.2734375, 59864.79296875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-49553.5546875, 59839.76953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-49541.2265625, 59814.30859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-49577.1796875, 59889.3671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-49581.8828125, 59823.26953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-49569.9140625, 59798.69921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-49594.2890625, 59847.921875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-49898.2578125, 60790.71484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-49889.3203125, 60773.32421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-49880.3828125, 60756.27734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-49871.4765625, 60738.60546875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=16.0, width=16.900002, height=6.0, shelter=False))


class Bernay_Saint_Martin(Airport):
    id = 69
    name = "Bernay Saint Martin"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5375000, vhf_low_hz=41650000, vhf_high_hz=121250000, uhf_hz=253250000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-39510.072021, 67097.558513, terrain), terrain)

        self.runways.append(Runway(id=None, name='18-36', main=RunwayApproach(name='18', heading=180, beacons=[]), opposite=RunwayApproach(name='36', heading=360, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-39077.40625, 67316.4453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-39025.44140625, 67317.7421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=24.0, width=33.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-39131.7265625, 67302.234375, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-39176.86328125, 67301.7421875, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-39221.81640625, 67300.2578125, self._terrain), large=False, heli=False,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-39074.643818437, 67218.026271578, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-39115.34765625, 67214.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-39160.69921875, 67207.5234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-39457.796875, 67230.734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-39504.38671875, 67230.6171875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-39546.2578125, 67230.4140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-39672.88671875, 67229.7578125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-39719.05859375, 67228.9609375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-39761.27734375, 67229.3515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-39842.87109375, 67269.9140625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-39811.40234375, 67257.5625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-39913.6015625, 67248.265625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-39941.734375, 67282.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=16.0, width=16.900002, height=6.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-39974.16015625, 67269.8046875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=16.0, width=16.900002, height=6.0, shelter=False))


class Saint_Andre_de_lEure(Airport):
    id = 70
    name = "Saint-Andre-de-lEure"
    tacan = None
    unit_zones: List[mapping.Rectangle] = []
    civilian = False
    slot_version = 2
    atc_radio = AtcRadio(hf_hz=5425000, vhf_low_hz=41750000, vhf_high_hz=121350000, uhf_hz=253350000)

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point(-60655.054688, 117310.871094, terrain), terrain)

        self.runways.append(Runway(id=2, name='23-05', main=RunwayApproach(name='23', heading=230, beacons=[]), opposite=RunwayApproach(name='05', heading=50, beacons=[])))
        self.runways.append(Runway(id=1, name='31-13', main=RunwayApproach(name='31', heading=310, beacons=[]), opposite=RunwayApproach(name='13', heading=130, beacons=[])))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-60729.296875, 115508.8515625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-60554.5390625, 115574.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-60471.70703125, 115624.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-60635.11328125, 115709.8828125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-60806.4296875, 115666.078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-60581.33203125, 115811.6328125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-60894.4375, 115706.796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-60925.6875, 115830.0078125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-60882.18359375, 115886.15625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-61054.6875, 115996.703125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-61172.74609375, 116151.421875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-61203.109375, 116216.0625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-61272.78125, 116233.234375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-61337.83984375, 116199.890625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-61400.98828125, 116280.671875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-61326.3671875, 116305.78125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-61202.03515625, 116371.8984375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-61272.1171875, 116383.0859375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-61383.26171875, 116407.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-61451.78515625, 116399.5390625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-61581.62890625, 116440.203125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-61457.26953125, 117513.6953125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-61538.93359375, 117440.9453125, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-61712.53515625, 117632.1796875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-61758.125, 117728.59375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-61835.6953125, 117749.7734375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-61910.5625, 117743.46875, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-62024.09375, 117790.765625, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-62029.68359375, 117848.484375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=7.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-61989.5234375, 117931.109375, self._terrain), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=7.0, shelter=False))


ALL_AIRPORTS: List[Type[Airport]] = [
    Saint_Pierre_du_Mont,
    Lignerolles,
    Cretteville,
    Maupertus,
    Brucheville,
    Meautis,
    Cricqueville_en_Bessin,
    Lessay,
    Sainte_Laurent_sur_Mer,
    Biniville,
    Cardonville,
    Deux_Jumeaux,
    Chippelle,
    Beuzeville,
    Azeville,
    Picauville,
    Le_Molay,
    Longues_sur_Mer,
    Carpiquet,
    Bazenville,
    Sainte_Croix_sur_Mer,
    Beny_sur_Mer,
    Rucqueville,
    Sommervieu,
    Lantheuil,
    Evreux,
    Chailey,
    Needs_Oar_Point,
    Funtington,
    Tangmere,
    Ford,
    Argentan,
    Goulet,
    Barville,
    Essay,
    Hauterive,
    Lymington,
    Vrigny,
    Odiham,
    Conches,
    West_Malling,
    Villacoublay,
    Kenley,
    Beauvais_Tille,
    Cormeilles_en_Vexin,
    Creil,
    Guyancourt,
    Lonrai,
    Dinan_Trelivan,
    Fecamp_Benouville,
    Farnborough,
    Friston,
    Deanland,
    Triqueville,
    Poix,
    Orly,
    Stoney_Cross,
    Amiens_Glisy,
    Ronai,
    Rouen_Boos,
    Deauville,
    Saint_Aubin,
    Flers,
    Avranches_Le_Val_Saint_Pere,
    Gravesend,
    Beaumont_le_Roger,
    Broglie,
    Bernay_Saint_Martin,
    Saint_Andre_de_lEure,
]

