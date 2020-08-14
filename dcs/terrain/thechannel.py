import dcs.mapping as mapping
from dcs.terrain.terrain import Airport, Runway, ParkingSlot, Terrain, MapView


class Abbeville_Drucat(Airport):
    id = 1
    name = "Abbeville Drucat"
    position = mapping.Point(-81676.550781, 15906.308105)
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
                crossroad_idx=5, position=mapping.Point(-81904.96875, 18212.265625), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-81981.75, 18186.1328125), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-82036.9921875, 18140.03125), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-82104.96875, 18073.689453125), large=False, heli=False,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-82129.5390625, 18024.455078125), large=False, heli=False,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-82251.1328125, 17997.052734375), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
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
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-80920.09375, 18382.9296875), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-80843.6640625, 18428.873046875), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-80718.4921875, 17059.05859375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-80717.234375, 17166.173828125), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-80798.8046875, 16778.943359375), large=False, heli=False,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))


class Merville_Calonne(Airport):
    id = 2
    name = "Merville Calonne"
    position = mapping.Point(-29173.647461, 74342.222656)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Merville_Calonne, self).__init__()

        self.runways.append(Runway(210))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-28799.3125, 73304.28125), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-28877.72265625, 73330.0625), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-28947.390625, 73366.6484375), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-29033.779296875, 73389.8125), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-29095.7578125, 73439.578125), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-29123.04296875, 73529.109375), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-29171.232421875, 73592.3203125), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-29233.537109375, 73642.328125), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-29314.5, 73666.9609375), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-28822.259765625, 73455.8125), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-28874.470703125, 73517.0078125), large=False, heli=True,
                airplanes=True, slot_name='11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-28899.98828125, 73610.71875), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-28992.685546875, 73620.203125), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-29044.515625, 73681.5625), large=False, heli=True,
                airplanes=True, slot_name='14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-29080.21875, 73759.6484375), large=False, heli=True,
                airplanes=True, slot_name='15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-29189.1171875, 73756.984375), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-29730.138671875, 74204.2890625), large=False, heli=True,
                airplanes=True, slot_name='24', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-29778.630859375, 74266.1640625), large=False, heli=True,
                airplanes=True, slot_name='25', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-29878.7578125, 74328.1796875), large=False, heli=True,
                airplanes=True, slot_name='26', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-29951.150390625, 74389.2421875), large=False, heli=True,
                airplanes=True, slot_name='27', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-30050.033203125, 74320.78125), large=False, heli=True,
                airplanes=True, slot_name='28', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-29824.75, 74133.171875), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-29924.77734375, 74115.6796875), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-29998.619140625, 74074.3515625), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-30025.546875, 73993.875), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-30101.873046875, 73954.5859375), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-30011.443359375, 74237.671875), large=False, heli=True,
                airplanes=True, slot_name='29', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-30087.978515625, 74200.8671875), large=False, heli=True,
                airplanes=True, slot_name='30', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-30127.7890625, 74129.8671875), large=False, heli=True,
                airplanes=True, slot_name='31', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-30191.65234375, 74081.359375), large=False, heli=True,
                airplanes=True, slot_name='32', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-30251.1640625, 73903.1875), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-30272.64453125, 73826.453125), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-28323.58203125, 75295.2578125), large=False, heli=True,
                airplanes=True, slot_name='42', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-28401.041015625, 75344.8046875), large=False, heli=True,
                airplanes=True, slot_name='41', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-28518.671875, 75338.5), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-28634.095703125, 75361.375), large=False, heli=True,
                airplanes=True, slot_name='39', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-28711.80078125, 75333.7265625), large=False, heli=True,
                airplanes=True, slot_name='38', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-28450.36328125, 75186.1640625), large=False, heli=True,
                airplanes=True, slot_name='43', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-28527.072265625, 75173.59375), large=False, heli=True,
                airplanes=True, slot_name='44', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-28607.244140625, 75176.359375), large=False, heli=True,
                airplanes=True, slot_name='45', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-28683.728515625, 75216.828125), large=False, heli=True,
                airplanes=True, slot_name='46', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-28722.900390625, 75104.671875), large=False, heli=True,
                airplanes=True, slot_name='47', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-28696.640625, 74998.0390625), large=False, heli=True,
                airplanes=True, slot_name='48', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-28811.0859375, 74962.1796875), large=False, heli=True,
                airplanes=True, slot_name='33', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-28830.884765625, 75039.484375), large=False, heli=True,
                airplanes=True, slot_name='34', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-28847.97265625, 75124.5078125), large=False, heli=True,
                airplanes=True, slot_name='35', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-28833.287109375, 75208.5625), large=False, heli=True,
                airplanes=True, slot_name='36', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-28786.783203125, 75283.796875), large=False, heli=True,
                airplanes=True, slot_name='37', length=40.0, width=40.0, height=12.0, shelter=False))


class Saint_Omer_Longuenesse(Airport):
    id = 3
    name = "Saint Omer Longuenesse"
    position = mapping.Point(-16951.71582, 45171.712891)
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
                crossroad_idx=4, position=mapping.Point(-16855.115234375, 44527.1484375), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
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
                crossroad_idx=8, position=mapping.Point(-16722.392578125, 44772.96875), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
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
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-16793.97265625, 45099.703125), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-16809.5078125, 45117.296875), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-16818.837890625, 45140.3046875), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-17215.724609375, 44984.875), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-16821.943359375, 45192.65625), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
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
                airplanes=True, slot_name='31', length=20.5, width=14.5, height=8.0, shelter=False))
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
    position = mapping.Point(16494.189453, 46950.742188)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Dunkirk_Mardyck, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(16620.982421875, 47046.9921875), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(16787.392578125, 47593.80078125), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
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
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(16758.31640625, 48566.203125), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(15870.676757813, 47370.9140625), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
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
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(16137.262695313, 46960.53125), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(17033.4609375, 48436.95703125), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(16002.551757812, 47291.11328125), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(16641.48828125, 47155.7890625), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))


class Manston(Airport):
    id = 5
    name = "Manston"
    position = mapping.Point(52264.28125, -15827.487793)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Manston, self).__init__()

        self.runways.append(Runway(100))
        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(53406.3125, -14998.573242188), large=False, heli=False,
                airplanes=True, slot_name='68', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(53203.453125, -15266.77734375), large=False, heli=False,
                airplanes=True, slot_name='65', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(52945.296875, -15751.91015625), large=False, heli=False,
                airplanes=True, slot_name='57', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(52928.75, -15769.467773437), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(52752.9296875, -15980.0546875), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(53156.59375, -17053.43359375), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(53312.48828125, -17081.896484375), large=False, heli=False,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(52365.48046875, -17052.736328125), large=False, heli=True,
                airplanes=True, slot_name='12', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(52323.21875, -16874.927734375), large=False, heli=True,
                airplanes=True, slot_name='11', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(52283.64453125, -16696.306640625), large=False, heli=True,
                airplanes=True, slot_name='10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(52156.890625, -16102.392578125), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(52121.296875, -15947.27734375), large=False, heli=True,
                airplanes=True, slot_name='08', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(52086.734375, -15785.474609375), large=False, heli=True,
                airplanes=True, slot_name='07', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(52052.79296875, -15624.427734375), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(52014.1015625, -15459.830078125), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(51978.41796875, -15306.775390625), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(51907.2421875, -14972.000976563), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(51853.65625, -14719.455078125), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(51806.7734375, -14491.458984375), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
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
                crossroad_idx=33, position=mapping.Point(52668.69140625, -16079.984375), large=False, heli=True,
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
                crossroad_idx=49, position=mapping.Point(53123.01953125, -17070.728515625), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(53090.97265625, -17088.548828125), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(53061.2421875, -17103.8671875), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(53033.53515625, -17118.177734375), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(52641.765625, -16708.86328125), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(52649.06640625, -16742.412109375), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(53036.67578125, -15700.387695313), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(53040.984375, -15654.38671875), large=False, heli=False,
                airplanes=True, slot_name='59', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(53171.796875, -15473.270507813), large=False, heli=True,
                airplanes=True, slot_name='63', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(53106.578125, -15625.421875), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(53109.8203125, -15563.850585938), large=False, heli=False,
                airplanes=True, slot_name='61', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(53163.23046875, -15388.58984375), large=False, heli=False,
                airplanes=True, slot_name='64', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(53160.6640625, -15522.41015625), large=False, heli=True,
                airplanes=True, slot_name='62', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(53248.34375, -15219.190429687), large=False, heli=True,
                airplanes=True, slot_name='66', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(53272.7421875, -15174.526367187), large=False, heli=True,
                airplanes=True, slot_name='67', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(52626.15625, -16639.712890625), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(52633.453125, -16673.265625), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(52611.10546875, -16571.271484375), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(52618.71875, -16604.5390625), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(52665.2890625, -16780.703125), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(52590.48046875, -16524.296875), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(52826.796875, -15893.015625), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=8.0, shelter=False))


class Hawkinge(Airport):
    id = 6
    name = "Hawkinge"
    position = mapping.Point(27031.420898, -29403.830078)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Hawkinge, self).__init__()

        self.runways.append(Runway(190))
        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(27040, -30028.244140625), large=False, heli=False,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(27308.40234375, -29087.111328125), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(27276.8046875, -29072.44140625), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(27244.27734375, -29057.19140625), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(27211.73046875, -29041.603515625), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(27420.6953125, -29182.8515625), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(27200.55078125, -29937.79296875), large=False, heli=False,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(26932.28125, -30194.1953125), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(27140.705078125, -29000.99609375), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(26591.95703125, -30091.30078125), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(26573.298828125, -30068.294921875), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(26647.7734375, -30132.556640625), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(26631.279296875, -30108.376953125), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(26724.1640625, -30207.951171875), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(26699.814453125, -30192.974609375), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(26771.0234375, -29008.568359375), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(26748.544921875, -29027.4140625), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(26802.212890625, -28970.296875), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(26818.9296875, -28946.75), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(26838.42578125, -28883.888671875), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(26856.09765625, -28859.921875), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(27071.71875, -28954.021484375), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(27074.619140625, -30069.642578125), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(26579.890625, -29575.828125), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(27157.048828125, -29923.697265625), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(27139.091796875, -29903.3515625), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))


class Lympne(Airport):
    id = 7
    name = "Lympne"
    position = mapping.Point(23796.457031, -39541.675781)
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
    position = mapping.Point(49629.695313, -67886.082031)
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
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(50069.91796875, -67573.203125), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(50055.5078125, -67551.859375), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(49988.234375, -67435.2890625), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(50009.2421875, -67892.328125), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(50020.46875, -67911.6484375), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(50031.15625, -67930.6796875), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(50042.63671875, -67947.390625), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(50053.08203125, -67964.3203125), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(50063.7109375, -67981.5546875), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(50111.7265625, -67951.90625), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(50099.87890625, -67932.140625), large=False, heli=True,
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
                crossroad_idx=26, position=mapping.Point(50034.46484375, -68246.7890625), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(50013.67578125, -68263.84375), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(49993.0859375, -68280.703125), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(49971.359375, -68298.5234375), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(49946.34375, -68319.171875), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(49923.33203125, -68337.96875), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(49883.68359375, -67357.6328125), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(49953.921875, -67380.265625), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))


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
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
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
                crossroad_idx=16, position=mapping.Point(28823.103515625, -61778.9453125), large=False, heli=True,
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
                crossroad_idx=44, position=mapping.Point(29280.853515625, -61083.7265625), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(29163.4765625, -61154.9140625), large=False, heli=True,
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
                crossroad_idx=49, position=mapping.Point(29489.765625, -60955.5546875), large=False, heli=True,
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
                crossroad_idx=82, position=mapping.Point(28847.181640625, -61891.40625), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))


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
        self.airports['High Halden'] = High_Halden()

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

    def high_halden(self) -> Airport:
        return self.airports["High Halden"]