import dcs.mapping as mapping
from dcs.terrain.terrain import Airport, Runway, ParkingSlot, Terrain, MapView


class Abbeville_Drucat(Airport):
    id = 1
    name = "Abbeville Drucat"
    position = mapping.Point(-81655.472418, 15915.37745)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Abbeville_Drucat, self).__init__()

        self.runways.append(Runway(20))
        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-80735.7109375, 16925.8671875), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-81904.96875, 18212.265625), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-81981.75, 18186.1328125), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-82036.9921875, 18140.03125), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-82104.96875, 18073.689453125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-82129.5390625, 18024.455078125), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-82251.1328125, 17997.052734375), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-82177.9140625, 18076.76953125), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-82156.6171875, 18166.736328125), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-80611.53125, 17394.251953125), large=False, heli=False,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-80539.515625, 17308.9140625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-80572.734375, 17265.576171875), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-80796.953125, 17540.17578125), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-80770.890625, 17580.666015625), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-80780.75, 17636.404296875), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-80849.515625, 17666.310546875), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-80876.828125, 17769.578125), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-80916.1171875, 17871.734375), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-80914.4921875, 17947.568359375), large=False, heli=False,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-80921.890625, 18065.88671875), large=False, heli=False,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-80939.0234375, 18224.556640625), large=False, heli=False,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-80966.4453125, 18286.35546875), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-80920.09375, 18382.9296875), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-80843.6640625, 18428.873046875), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-80718.4921875, 17059.05859375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-80717.234375, 17166.173828125), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-80798.8046875, 16778.943359375), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))


class Merville_Calonne(Airport):
    id = 2
    name = "Merville Calonne"
    position = mapping.Point(-29311.714574, 73776.745175)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Merville_Calonne, self).__init__()

        self.runways.append(Runway(140))
        self.runways.append(Runway(80))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-29541.197265625, 74560.453125), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-29605.87109375, 74482.9921875), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-29512.830078125, 74632.171875), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-29518.63671875, 74474.890625), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-29296.046875, 75429.5859375), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-29328.765625, 75363.4609375), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-29206.53515625, 75607.125), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-28544.865234375, 74317.705265458), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-30525.655500722, 73410.473084701), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-30436.255297981, 73461.735072882), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-30336.976685026, 73543.019908637), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-30246.471850117, 73603.742384118), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-30146.132854266, 73685.819699318), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-30036.913173203, 73773.209816169), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-29946.807133166, 73854.948610425), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-29847.108073276, 73914.538902697), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-29805.960292506, 74031.806077283), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-29681.333984375, 74391.25), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-29433.521484375, 74578.59375), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-29364.515625, 74574.8359375), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-29480.94921875, 74775.1796875), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-29472.564453125, 74847.2109375), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-29246.328125, 75229.8046875), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-29279.302734375, 75141.3359375), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-29211.056640625, 75280.2734375), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-29184.376953125, 75394.4765625), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-29417.6015625, 75047.2265625), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-29141.765625, 75508.0546875), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-29274.0078125, 75466.9609375), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-28682.921875, 73653.6953125), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-28627.083984375, 73883.8984375), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-28642.923828125, 73809.171875), large=False, heli=True,
                airplanes=True, slot_name='50', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-28596.15625, 74105.7734375), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-28593.265625, 74030.6953125), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-28577.380859375, 74225.6796875), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-28778.828125, 73885.3046875), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-28927.521484375, 73916.0546875), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-28830.900390625, 74257.90625), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-28910.328125, 74256.125), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-29082.73828125, 73966.484375), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-29242.759765625, 73983.4140625), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-28857.173828125, 74415.3046875), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-28935.875, 74419.4375), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-28598.283203125, 75266.203125), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-28206.3671875, 75119.6953125), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-28173.2109375, 74809.265625), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-28232.845703125, 74755.5703125), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-28159.310546875, 75042.046875), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-28364.326171875, 74477.671875), large=False, heli=False,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-28288.466796875, 74516.046875), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-28471.21484375, 74431.3828125), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))


class Saint_Omer_Longuenesse(Airport):
    id = 3
    name = "Saint Omer Longuenesse"
    position = mapping.Point(-16951.693085, 45167.689101)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Saint_Omer_Longuenesse, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-16750.32421875, 44658.95703125), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-16685.8984375, 44518.21484375), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-16855.115234375, 44527.1484375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-16827.42990945, 44712.185374436), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-16854.392330572, 44729.218354763), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-16877.047453213, 44750.456918223), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-16722.392578125, 44772.96875), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-16689.876953125, 44806.828125), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-16652.298797382, 44860.903628482), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-16595.658713604, 44887.251680392), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-16553.65973541, 44920.352995763), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-16593.215956891, 44964.096865776), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-16627.873343939, 44935.366347516), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-16668.584157662, 44920.392109471), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-16676.357421875, 44994.4765625), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-16804.998046875, 45454.98046875), large=False, heli=False,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-16803.26171875, 45494.9609375), large=False, heli=False,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-16865.859375, 45763.0859375), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-16811.2890625, 45671.34765625), large=False, heli=False,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-16821.287109375, 45690.41015625), large=False, heli=False,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-16774.31640625, 45083.71484375), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-16793.97265625, 45099.703125), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-16809.5078125, 45117.296875), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-16818.837890625, 45140.3046875), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-17215.724609375, 44984.875), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-16821.943359375, 45192.65625), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-16821.212890625, 45220.6796875), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-16820.3125, 45247.28125), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-16819.59765625, 45274.015625), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-16819.244140625, 45299.265625), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-16818.4609375, 45326.1328125), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-16818.9921875, 45350.8984375), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-16818.4609375, 45376.74609375), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-16827.734375, 45737.41015625), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-16854.868761609, 44801.815367799), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-16825.925056084, 44795.365110598), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-16886.608270818, 44808.178335765), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))


class Dunkirk_Mardyck(Airport):
    id = 4
    name = "Dunkirk Mardyck"
    position = mapping.Point(16496.0384, 46954.354309)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Dunkirk_Mardyck, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(16624.70932447, 47046.241339207), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(16787.392578125, 47593.80078125), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(16972.494140625, 48500.3828125), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(16976.068359375, 48551.44921875), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(17037.724609375, 48569.19921875), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(17033.396484375, 48517.35546875), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(17111.234375, 48471.1015625), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(17104.76171875, 48412.56640625), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(17087.908203125, 48255.24609375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(16758.31640625, 48566.203125), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(15870.676757813, 47370.9140625), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(16001.8515625, 47390.39453125), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(16003.302734375, 47201.85546875), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(16002.684570313, 47140.2578125), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(16124.993164063, 47287.0078125), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(16137.262695313, 46960.53125), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(17033.4609375, 48436.95703125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(16002.551757812, 47291.11328125), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(16643.550829076, 47155.425083472), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))


class Manston(Airport):
    id = 5
    name = "Manston"
    position = mapping.Point(52264.839159, -15815.916617)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Manston, self).__init__()

        self.runways.append(Runway(100))
        self.runways.append(Runway(40))
        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(53415.399652829, -15004.037609836), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(53203.453125, -15266.77734375), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(52889.992267619, -15691.540859472), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(52852.2215957, -15721.613709093), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(52754.103738253, -15981.354529405), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(53156.59375, -17053.43359375), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(53312.48828125, -17081.896484375), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(52365.48046875, -17052.736328125), large=False, heli=True,
                airplanes=True, slot_name='12', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(52323.21875, -16874.927734375), large=False, heli=True,
                airplanes=True, slot_name='11', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(52283.64453125, -16696.306640625), large=False, heli=True,
                airplanes=True, slot_name='10', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(52156.890625, -16102.392578125), large=False, heli=True,
                airplanes=True, slot_name='09', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(52121.296875, -15947.27734375), large=False, heli=True,
                airplanes=True, slot_name='08', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(52086.734375, -15785.474609375), large=False, heli=True,
                airplanes=True, slot_name='07', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(52052.79296875, -15624.427734375), large=False, heli=True,
                airplanes=True, slot_name='06', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(52014.1015625, -15459.830078125), large=False, heli=True,
                airplanes=True, slot_name='05', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(51978.41796875, -15306.775390625), large=False, heli=True,
                airplanes=True, slot_name='04', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(51907.2421875, -14972.000976563), large=False, heli=True,
                airplanes=True, slot_name='03', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(51853.65625, -14719.455078125), large=False, heli=True,
                airplanes=True, slot_name='02', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(51806.7734375, -14491.458984375), large=False, heli=True,
                airplanes=True, slot_name='01', length=60.0, width=52.0, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(52943.3359375, -15855.366210938), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(52924.890625, -15874.98046875), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(52871.875, -15943.8828125), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(52859.26953125, -15963.577148438), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(52734.78515625, -16222.831054688), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(52710.4765625, -16243.317382813), large=False, heli=True,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(52685.48828125, -16263.963867187), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(52660.27734375, -16286.13671875), large=False, heli=True,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(52632.6640625, -16309.178710937), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(52605.9375, -16330.698242188), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(52691.00390625, -16067.98046875), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(52529.286983472, -16093.951385767), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(53383.01171875, -17257.74609375), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(53354.6015625, -17253.74609375), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(53325.6171875, -17248.130859375), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(53277.57421875, -17240.888671875), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(53244.83203125, -17234.91015625), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(53210.19921875, -17228.7421875), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(53174.734375, -17222.40625), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(53140.9453125, -17216.03515625), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(53105.46875, -17209.234375), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(53069.45703125, -17202.203125), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(53035.56640625, -17195.953125), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(53000.06640625, -17189.93359375), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(52964.078125, -17183.412109375), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(52929.88671875, -17177.169921875), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(52896.27734375, -17170.6484375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(53099.958793617, -17040.634821646), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(53074.36822417, -17093.530157749), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(53021.333585944, -17115.605011487), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(52965.092339316, -17099.178109948), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(52658.589123218, -16704.190087301), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(52675.801844723, -16769.039779391), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(53036.67578125, -15700.387695313), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(53049.452635361, -15662.070210043), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(53171.796875, -15473.270507813), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(53106.578125, -15625.421875), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(53114.579341337, -15567.077691777), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(53163.23046875, -15388.58984375), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(53160.6640625, -15522.41015625), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(53248.34375, -15219.190429687), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(53272.7421875, -15174.526367187), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(52640.726086012, -16595.224997712), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(52626.279294177, -16660.506374526), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(52609.57403729, -16492.316815779), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(52629.303522313, -16542.480661458), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(52695.415427903, -16824.546270197), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(52595.660045573, -16437.552815733), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(52830.25671405, -15896.117891053), large=False, heli=False,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))


class Hawkinge(Airport):
    id = 6
    name = "Hawkinge"
    position = mapping.Point(26989.935547, -29402.577148)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Hawkinge, self).__init__()

        self.runways.append(Runway(190))
        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(26914.835850485, -29944.036577881), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(27308.40625, -29087.11328125), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(27276.8046875, -29072.44140625), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(27244.27734375, -29057.19140625), large=False, heli=True,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(27211.73046875, -29041.603515625), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(27420.701171875, -29182.8515625), large=False, heli=False,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(26932.279296875, -30194.193359375), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(27140.705078125, -29000.994140625), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(26591.95703125, -30091.294921875), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(26573.298828125, -30068.294921875), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(26647.76953125, -30132.560546875), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(26631.279296875, -30108.376953125), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(26724.162109375, -30207.953125), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(26699.81640625, -30192.970703125), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(26763.897225338, -29007.415273814), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(26747.384023814, -29031.500321819), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(26802.2109375, -28970.298828125), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(26818.9296875, -28946.75), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(26838.416015625, -28883.884765625), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(26856.09765625, -28859.921875), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(27071.71875, -28954.021484375), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(27041.60621108, -30030.571288543), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(26497.102972323, -29644.23622053), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(27194.355770503, -29970.08790368), large=False, heli=False,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(27178.436607099, -29950.835319321), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(27064.363911061, -30053.306566973), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(27026.258235644, -30009.823878985), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(26879.041018405, -29974.022329142), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(27156.990693363, -29927.494429933), large=False, heli=False,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(27253.413645141, -29920.199752406), large=False, heli=False,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(27139.410262681, -29908.645773082), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(27038.993580025, -29821.420467071), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(27016.209619782, -29844.479916127), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(27246.8046875, -29859.53125), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(26848.85546875, -30205.373046875), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(26974.484199237, -30104.861154343), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(26991.353516948, -30124.664664058), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(27082.142298807, -30071.17991009), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(26911.96558069, -30159.130728284), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(27404.31640625, -29563.7109375), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(27383.044921875, -29586.025390625), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(27374.654296875, -29615.662109375), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(27381.04296875, -29650.357421875), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(27345.60546875, -29654.3125), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(27329.087890625, -29678.388671875), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(27223.621466552, -29789.419945788), large=False, heli=False,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(26513.474609375, -29585.625), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(26489.952284337, -29680.798576537), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(26789.361328125, -30187.060546875), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(26763.98828125, -30167.96484375), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(27342.568359375, -29106.7421875), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(27001.9453125, -28899.037109375), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(26966.169921875, -28886.48828125), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(27181.6953125, -29829.951171875), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.5, width=14.5, height=8.0, shelter=False))


class Lympne(Airport):
    id = 7
    name = "Lympne"
    position = mapping.Point(23776.550782, -39519.907352)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lympne, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(23345.69140625, -39134.625), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(23201.74609375, -39010.74609375), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(23783.634765625, -39796.25390625), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(23748.3203125, -39728.65234375), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(23686.923828125, -39705.84765625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(23644.4921875, -39668.9140625), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(23591.3515625, -39682), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(23516.357421875, -39700.60546875), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(23471.884765625, -39712.6328125), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(23254.34765625, -39557.3359375), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(23255.8984375, -39531.75390625), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(23251.603515625, -39492.6484375), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(23246.7109375, -39461.828125), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(23244.21875, -39432.16796875), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(23241.810546875, -39402.59375), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(23239.392578125, -39372.625), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(23236.884765625, -39342.32421875), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(23234.56640625, -39312.13671875), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(23232.04296875, -39281.43359375), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(23823.890625, -39832.484375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(23863.69140625, -39868.34375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(23894.69140625, -39896.23046875), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))


class Detling(Airport):
    id = 8
    name = "Detling"
    position = mapping.Point(49594.237665, -67923.302526)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Detling, self).__init__()

        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(50092, -67870.7734375), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(49994.62109375, -67868.7890625), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(49976.59375, -67835.890625), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(49966.203125, -67798.328125), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(49965.953125, -67758.3125), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(49974.75, -67717.578125), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(49988.5859375, -67680.0625), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(50083.7734375, -67595.6328125), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(50061.112588101, -67560.120845179), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(50046.702431851, -67538.777095179), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(49988.234375, -67435.2890625), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(49986.201273748, -67907.109088539), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(49997.427836248, -67926.429401039), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(50008.115336248, -67945.460651039), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(50019.595804998, -67962.171588539), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(50030.041117498, -67979.101276039), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(50070.890915279, -68005.324037469), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(50149.260983714, -67943.879991794), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(50125.222580787, -67921.86449886), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(49863.71484375, -67428.3828125), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(49883.0390625, -67414.96875), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(49884.2734375, -67527.0859375), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(49864.43359375, -67539.1953125), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(49847.52734375, -67549.3984375), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(50058.239371502, -68227.920389681), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(50028.770719505, -68251.054982867), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(50001.891318149, -68273.533029329), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(49971.359375, -68298.5234375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(49941.186312763, -68323.32298302), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(49911.759245255, -68345.138845671), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(49883.68359375, -67357.6328125), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(49953.921875, -67380.265625), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))


class Eastchurch(Airport):
    id = 10
    name = "Eastchurch"
    position = mapping.Point(58521.966797, -50427.824219)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Eastchurch, self).__init__()

        self.runways.append(Runway(280))
        self.runways.append(Runway(200))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(59137.216053581, -49839.741051806), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(59178.596606036, -49945.329970301), large=False, heli=False,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(59233.55078125, -49983.77734375), large=False, heli=False,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(59269.01171875, -49972.06640625), large=False, heli=False,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(59066.23046875, -49934.18359375), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(59017.4921875, -49964.6484375), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(58934.90625, -49983.4921875), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(58910.44921875, -50006.66796875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(58858.078125, -50022.61328125), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(58820.770242833, -50037.097473345), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(58777.374118417, -50058.69810585), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(58534.7109375, -50190.765625), large=False, heli=False,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(58612.91015625, -50509.8828125), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(58631.078125, -50548.1015625), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(58644.7734375, -50594.171875), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(58630.6484375, -50641.99609375), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(58238.942529162, -50488.420117264), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(58242.15234375, -50528.56640625), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(58277.62109375, -50580.765625), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(58310.19140625, -50641.14453125), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(58395.484375, -50756.08203125), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(58473.2109375, -50840.1171875), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(58396.90234375, -50609.53515625), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(58323.35546875, -50505.484375), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(58300.66796875, -50411.23828125), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(58740.30078125, -50171.09375), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(58625.154248207, -50121.261219919), large=False, heli=False,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(58732.520159315, -50070.368498774), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(58682.3671875, -50094.125), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(58846.619549588, -50133.527482683), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(58948.5390625, -50072.99609375), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(58966.6015625, -50093.58984375), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(58920.503856431, -50122.993456371), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(59022.984375, -50065.3046875), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(58976.3359375, -49964.10546875), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(59118.29296875, -50010.6015625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(59136.66015625, -50031.29296875), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(59086.577225492, -50058.978922765), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(58596.543316342, -50296.821686656), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(58775.669380248, -50247.456445066), large=False, heli=False,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(58810.128488891, -50233.355796995), large=False, heli=False,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(58185.475291315, -50464.647998835), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))


class High_Halden(Airport):
    id = 12
    name = "High Halden"
    position = mapping.Point(28992.270508, -62020.105469)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(High_Halden, self).__init__()

        self.runways.append(Runway(110))
        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(29893.03515625, -60978.26171875), large=False, heli=True,
                airplanes=True, slot_name='56', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(29906.265625, -60952.12109375), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(29920.90625, -61047.30078125), large=False, heli=False,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(28669.79296875, -61436.43359375), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(28799.478515625, -61688.06640625), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(28802.302975559, -61717.962317687), large=False, heli=False,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(29030.19921875, -62638.83984375), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(29066.056640625, -62638.703125), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(29006.9453125, -62611.453125), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(29004.22265625, -62554.95703125), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(28907.9375, -61307.63671875), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(28769.376953125, -61631.80078125), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(28818.28152146, -61779.993572101), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(28773.73046875, -61829.390625), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(28869.740234375, -62005.37890625), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(28850.638671875, -61916.87109375), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(28820.255859375, -61968.77734375), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(28875.26953125, -62033.1484375), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(28823.474609375, -62100.96875), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(28830.435546875, -62064.53125), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(28891.017578125, -62125.796875), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(28817.3359375, -62177.42578125), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(28837.1171875, -62263.390625), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(28929.705078125, -62308.16796875), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(28866.798828125, -62387.12890625), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(28959.255859375, -62436.02734375), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(28904.9375, -62515.3671875), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(28828.00390625, -62143.65625), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(28845.28515625, -62229.82421875), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(28872.94921875, -62354.12109375), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(28912.580078125, -62477.8359375), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(28898.876953125, -62282.7109375), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(28927.14453125, -62403.65625), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(28931.220703125, -62540.4140625), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(28948.283203125, -61277.3359375), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(28994.4609375, -61251.44921875), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(29027.24609375, -61227.625), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(29075.998046875, -61118.1640625), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(29169.4453125, -61086.8203125), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(29235.75, -61101.48828125), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(29278.334555047, -61078.838891888), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(29160.419138664, -61149.454377078), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(29315.845703125, -61060.7734375), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(29338.0859375, -60988.75), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(29441.05078125, -60979.4296875), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(29485.204102381, -60947.832955696), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(29521.095703125, -60935.73046875), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(29547.1953125, -60855.515625), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(29623.72265625, -60872.0703125), large=False, heli=True,
                airplanes=True, slot_name='54', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(29585.650390625, -60863.25), large=False, heli=True,
                airplanes=True, slot_name='53', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(29370.611328125, -60994.6640625), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(29202.431640625, -61084.39453125), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(29106.80078125, -61105.578125), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(29032.36328125, -61165.94140625), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(29314.0703125, -61015.54296875), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(29528.37109375, -60885.8125), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(29067.1328125, -61482.41015625), large=False, heli=True,
                airplanes=True, slot_name='79', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(29141.05859375, -61494.5390625), large=False, heli=True,
                airplanes=True, slot_name='77', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(29169.58203125, -61414.6953125), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(29274.083984375, -61432.140625), large=False, heli=True,
                airplanes=True, slot_name='73', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(29274.0859375, -61357.28125), large=False, heli=True,
                airplanes=True, slot_name='71', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(29370.64453125, -61294.6328125), large=False, heli=True,
                airplanes=True, slot_name='70', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(29452.283203125, -61308.9375), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(29541.73046875, -61253.55859375), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(29558.8828125, -61184.20703125), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(29694.529296875, -61159.4375), large=False, heli=True,
                airplanes=True, slot_name='61', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(29767.5703125, -61057.1875), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(29807.02734375, -61028.734375), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(29665.083984375, -61155.9296875), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(29509.04296875, -61253.921875), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(29421.974609375, -61303.3828125), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(29232.9765625, -61422.91796875), large=False, heli=True,
                airplanes=True, slot_name='74', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(29103.5546875, -61489.796875), large=False, heli=True,
                airplanes=True, slot_name='78', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(29159.43359375, -61465.609375), large=False, heli=True,
                airplanes=True, slot_name='76', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(29295.35546875, -61403.2421875), large=False, heli=True,
                airplanes=True, slot_name='72', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(29448.609375, -61263.4140625), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(29559.1640625, -61222.90625), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(29693.294921875, -61115.0390625), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(28843.921133962, -61891.188882889), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))


class Headcorn(Airport):
    id = 13
    name = "Headcorn"
    position = mapping.Point(35780.818359, -62104.402344)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Headcorn, self).__init__()

        self.runways.append(Runway(100))
        self.runways.append(Runway(190))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(35068.9765625, -62497.765625), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(35088.3984375, -62531.62890625), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(35190.78125, -62560.99609375), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(35161.453125, -62526.9609375), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(35223.7734375, -62550.8125), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(35282.81640625, -62520.0625), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(35097.9296875, -62458.89453125), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(35348.09765625, -62526.79296875), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(35320.90625, -62547.6875), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(35478.015625, -62497.9140625), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(35412.953125, -62491.046875), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(35452.2890625, -62522.2421875), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(35497.3359375, -62431.28125), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(35559.18359375, -62497.80859375), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(35524.73828125, -62493.62890625), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(35579.71875, -62444.1484375), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(35652.015625, -62415.68359375), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(35673.171875, -62465.078125), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(35601.19921875, -62530.4921875), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(35678.1015625, -62588.015625), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(35668.5625, -62632.02734375), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(35609.83203125, -62678.91015625), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(35625.0859375, -62646.21875), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(35650.234375, -62559.296875), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(35647.0234375, -62751.80859375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(35704.34375, -62784.0078125), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(35658.66015625, -62782.6015625), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(35059.19921875, -62248.30859375), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(35237.65234375, -62172.46875), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(35339.13671875, -62217.453125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(35368.109375, -62140.7734375), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(35476.33984375, -62122.9140625), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(35559.33984375, -62172.875), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(35590.18359375, -62167.203125), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(35414.5, -62140.98046875), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(35274.4453125, -62205.3046875), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(35210.94921875, -62195.87109375), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(35447.53125, -62143.234375), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(35514.140625, -62150.328125), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(35663.84375, -62076.09375), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(35663.3984375, -62044.8046875), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(35658.82421875, -61945.9140625), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(35647.9609375, -61903.53125), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(35651.4453125, -61861.34765625), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(35530.8671875, -61723.53515625), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(35643.07421875, -61637.83203125), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(35640.76171875, -61605.49609375), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(35574.840120602, -62053.22432747), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(35573.821915034, -61932.623391444), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(35619.8828125, -61688.7890625), large=False, heli=True,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(35601.8046875, -61750.45703125), large=False, heli=True,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(35632.046875, -61521.52734375), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(35635.2890625, -61443.84765625), large=False, heli=False,
                airplanes=True, slot_name='53', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(35885.94140625, -61518.53515625), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(35878.1015625, -61561.41796875), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(35893.19921875, -61603.4453125), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(35883, -61640.53515625), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(35948.8515625, -61700.08984375), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(35886.875, -61753.47265625), large=False, heli=True,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(35901.58203125, -61795.86328125), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(35894.5, -61903.875), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(35960.453125, -61968.1953125), large=False, heli=True,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(35900.52734375, -62023.1328125), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(35953.375, -62010.7109375), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(35940.75, -61741.4921875), large=False, heli=True,
                airplanes=True, slot_name='60', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(35938.9609375, -61658.875), large=False, heli=True,
                airplanes=True, slot_name='58', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(35950.8203125, -61925.98046875), large=False, heli=True,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(35972.27734375, -62076.2578125), large=False, heli=True,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(36010.83203125, -62006.390625), large=False, heli=True,
                airplanes=True, slot_name='69', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(36040.078125, -61992.24609375), large=False, heli=True,
                airplanes=True, slot_name='70', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(36068.80078125, -62030.296875), large=False, heli=True,
                airplanes=True, slot_name='71', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(36117.8203125, -62045.6640625), large=False, heli=True,
                airplanes=True, slot_name='72', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(36157.40625, -61980.0703125), large=False, heli=True,
                airplanes=True, slot_name='73', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(36191.67578125, -62001.84765625), large=False, heli=True,
                airplanes=True, slot_name='74', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(36258.4375, -61990), large=False, heli=True,
                airplanes=True, slot_name='76', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(36303.14453125, -62001.3671875), large=False, heli=True,
                airplanes=True, slot_name='77', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(36223.28125, -62033.59375), large=False, heli=True,
                airplanes=True, slot_name='75', length=20.5, width=14.5, height=8.0, shelter=False))


class Biggin_Hill(Airport):
    id = 14
    name = "Biggin Hill"
    position = mapping.Point(53454.535156, -107463.621094)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Biggin_Hill, self).__init__()

        self.runways.append(Runway(50))
        self.runways.append(Runway(120))
        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(53541.765625, -107856.4453125), large=False, heli=False,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(52866.27734375, -106806.453125), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(53395.124552726, -106989.45777658), large=False, heli=False,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(53523.708207458, -106909.86445014), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(53481.3203125, -106855.9765625), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(53255.79296875, -106984.46875), large=False, heli=False,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(52972.7578125, -106789.1015625), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(52660.72265625, -106970.1171875), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(52626.96484375, -107212.5703125), large=False, heli=False,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(52772.70703125, -107204.0234375), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(52856.89453125, -107356.2890625), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(52791.15234375, -106958.9375), large=False, heli=True,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(52775.16015625, -106991.0625), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(52783, -107024.78125), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(52766.015625, -107054.578125), large=False, heli=True,
                airplanes=True, slot_name='31', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(52794.7109375, -107075.8359375), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(52802.4140625, -107115.046875), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(52858.6171875, -107186.3046875), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(52831.6171875, -107163.328125), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(52879.5390625, -107215.7265625), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(53003.87890625, -107561.25), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(52990.84765625, -107511.515625), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(52893.7109375, -107573.7265625), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(52926.2578125, -107530.546875), large=False, heli=True,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(52969.556875171, -107750.02301713), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(52991.136502198, -107763.42883234), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(53217.637842237, -107886.96198205), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(53256.671875, -107926.234375), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(53285.17578125, -107925.40625), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(53348.58203125, -107941.0625), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(53330.44140625, -107930.75), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(53936.65234375, -107688.78125), large=False, heli=False,
                airplanes=True, slot_name='58', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(54070.74609375, -107558.71875), large=False, heli=False,
                airplanes=True, slot_name='60', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(54142.328125, -107575.0390625), large=False, heli=False,
                airplanes=True, slot_name='61', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(54100.828125, -107400.328125), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(54244.64453125, -107460.859375), large=False, heli=False,
                airplanes=True, slot_name='64', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(53723.73828125, -107013.8828125), large=False, heli=False,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(53832.47265625, -106918.734375), large=False, heli=False,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(52874.7421875, -107434.1328125), large=False, heli=True,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(52882.66796875, -107405.03125), large=False, heli=True,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(54075.3671875, -107056.609375), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(53916.00390625, -107055.3515625), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(53631.1171875, -107724.4765625), large=False, heli=True,
                airplanes=True, slot_name='55', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(53676.69921875, -107701.96875), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(53713.90625, -107669.8203125), large=False, heli=True,
                airplanes=True, slot_name='57', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(53220.88671875, -107263.8359375), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(53157.939360742, -106899.6474593), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(53055.276385991, -106860.457476), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(52757.96875, -106800.5859375), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(52656.136773526, -107057.00248331), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(52666.796929776, -107026.85761686), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(52742.142785666, -107165.11652118), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(53058.6328125, -106998.546875), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(52899.70703125, -107369.734375), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(53999.68525283, -107565.20365549), large=False, heli=True,
                airplanes=True, slot_name='59', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(54132.3671875, -107499.78125), large=False, heli=True,
                airplanes=True, slot_name='62', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(52631.46484375, -106913.5625), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(53244.03515625, -107133.2265625), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(53374.57421875, -107145.140625), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(53322.46484375, -107141.984375), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(53015.05047932, -107606.58369623), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(52976.53125, -107468.640625), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(54391.71484375, -107227.078125), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(54223.81640625, -107027.578125), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))


class TheChannel(Terrain):
    center = {"lat": 50.875, "long": 1.5875}
    bounds = mapping.Rectangle(74967, -114995, -129982, 129991)
    map_view_default = MapView(mapping.Point(0, 0), 1000000)
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
    assert (len(temperature) == 12)

    def __init__(self):
        super(TheChannel, self).__init__("TheChannel")
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports['Abbeville Drucat'] = Abbeville_Drucat()
        self.airports['Merville Calonne'] = Merville_Calonne()
        self.airports['Saint Omer Longuenesse'] = Saint_Omer_Longuenesse()
        self.airports['Dunkirk Mardyck'] = Dunkirk_Mardyck()
        self.airports['Manston'] = Manston()
        self.airports['Hawkinge'] = Hawkinge()
        self.airports['Lympne'] = Lympne()
        self.airports['Detling'] = Detling()
        self.airports['Eastchurch'] = Eastchurch()
        self.airports['High Halden'] = High_Halden()
        self.airports['Headcorn'] = Headcorn()
        self.airports['Biggin Hill'] = Biggin_Hill()

    def abbeville_drucat(self) -> Airport:
        return self.airports["Abbeville Drucat"]

    def merville_calonne(self) -> Airport:
        return self.airports["Merville Calonne"]

    def saint_omer_longuenesse(self) -> Airport:
        return self.airports["Saint Omer Longuenesse"]

    def dunkirk_mardyck(self) -> Airport:
        return self.airports["Dunkirk Mardyck"]

    def manston(self) -> Airport:
        return self.airports["Manston"]

    def hawkinge(self) -> Airport:
        return self.airports["Hawkinge"]

    def lympne(self) -> Airport:
        return self.airports["Lympne"]

    def detling(self) -> Airport:
        return self.airports["Detling"]

    def eastchurch(self) -> Airport:
        return self.airports["Eastchurch"]

    def high_halden(self) -> Airport:
        return self.airports["High Halden"]

    def headcorn(self) -> Airport:
        return self.airports["Headcorn"]

    def biggin_hill(self) -> Airport:
        return self.airports["Biggin Hill"]
