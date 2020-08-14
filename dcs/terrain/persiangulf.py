from dcs.terrain.terrain import Terrain, Airport, Runway, ParkingSlot, MapView, Graph
import dcs.mapping as mapping
from datetime import datetime, timezone
import random


class Abu_Musa_Island_Airport(Airport):
    id = 1
    name = "Abu Musa Island Airport"
    position = mapping.Point(-31505.274308, -121335.307759)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Abu_Musa_Island_Airport, self).__init__()

        self.runways.append(Runway(80))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-31265.763702393, -121984.875), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-31235.46484375, -121986.890625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-31243.45123291, -122057.5), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-31250.574249268, -122125.46862793), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-31279.804626465, -122121.92980957), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-31309.128890991, -122118.99987793), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-31295.628936768, -121981.8671875), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-31277.535095215, -122054.63250732), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))


class Bandar_Abbas_Intl(Airport):
    id = 2
    name = "Bandar Abbas Intl"
    position = mapping.Point(115765.882813, 14257.968262)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Bandar_Abbas_Intl, self).__init__()

        self.runways.append(Runway(30))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(117866.46875, 15125.918945312), large=False, heli=True,
                airplanes=True, slot_name='H06', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(117837.90625, 15109.52734375), large=False, heli=True,
                airplanes=True, slot_name='H05', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(117425.78125, 14748.622070313), large=False, heli=True,
                airplanes=True, slot_name='F18', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(117804.5859375, 15091.119140625), large=False, heli=True,
                airplanes=True, slot_name='H04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(117522.1875, 14800.169921875), large=False, heli=True,
                airplanes=True, slot_name='F26', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(117360.3828125, 14704.897460938), large=False, heli=True,
                airplanes=True, slot_name='F14', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(117540.2109375, 14730.541992188), large=False, heli=True,
                airplanes=True, slot_name='F25', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(117775.2109375, 15075.180664063), large=False, heli=True,
                airplanes=True, slot_name='H03', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(117743.1875, 15057.594726562), large=False, heli=True,
                airplanes=True, slot_name='H02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(117714.4375, 15041.0546875), large=False, heli=True,
                airplanes=True, slot_name='H01', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(117173.0625, 14596.526367188), large=False, heli=False,
                airplanes=True, slot_name='F06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(117108.421875, 14492.866210938), large=False, heli=True,
                airplanes=True, slot_name='F05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(117458.1640625, 14765.737304688), large=False, heli=True,
                airplanes=True, slot_name='F20', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(117394.046875, 14731.682617188), large=False, heli=True,
                airplanes=True, slot_name='F16', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(117199.3515625, 14609.822265625), large=False, heli=False,
                airplanes=True, slot_name='F08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(117226.8359375, 14625.44140625), large=False, heli=False,
                airplanes=True, slot_name='F10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(117490.578125, 14782.989257813), large=False, heli=True,
                airplanes=True, slot_name='F24', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(117252.96875, 14637.84375), large=False, heli=False,
                airplanes=True, slot_name='F12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(114862.4375, 13292.00390625), large=False, heli=True,
                airplanes=True, slot_name='B01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(118610.6796875, 15614.306640625), large=False, heli=True,
                airplanes=True, slot_name='H07', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(117259.25, 14586.584960937), large=False, heli=False,
                airplanes=True, slot_name='F11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(117510.1796875, 14713.831054687), large=False, heli=True,
                airplanes=True, slot_name='F23', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(117478.5859375, 14696.87109375), large=False, heli=True,
                airplanes=True, slot_name='F21', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(117349.34375, 14625.948242187), large=False, heli=True,
                airplanes=True, slot_name='F13', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(116987.8515625, 14514.446289063), large=False, heli=True,
                airplanes=True, slot_name='F04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(118995.8046875, 15455.541015625), large=False, heli=True,
                airplanes=True, slot_name='H08', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(117022.2109375, 14532.93359375), large=False, heli=True,
                airplanes=True, slot_name='F03', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(117444.7265625, 14680.666015625), large=False, heli=True,
                airplanes=True, slot_name='F19', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(117041.28125, 14476.921875), large=False, heli=True,
                airplanes=True, slot_name='F02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(117194.609375, 14550.9453125), large=False, heli=False,
                airplanes=True, slot_name='F07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(117413.171875, 14662.903320313), large=False, heli=True,
                airplanes=True, slot_name='F17', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(114962.609375, 13344.315429688), large=False, heli=True,
                airplanes=True, slot_name='B02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(117382.3203125, 14645.4296875), large=False, heli=True,
                airplanes=True, slot_name='F15', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(117225.671875, 14569.0859375), large=False, heli=False,
                airplanes=True, slot_name='F09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(115060.484375, 13396.690429687), large=False, heli=True,
                airplanes=True, slot_name='B03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(117009.34375, 14458.671875), large=False, heli=True,
                airplanes=True, slot_name='F01', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(118329.9140625, 15004.446289062), large=False, heli=False,
                airplanes=True, slot_name='J14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(118311.640625, 15037.810546875), large=False, heli=False,
                airplanes=True, slot_name='J13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(118317.1875, 14575.920898437), large=False, heli=False,
                airplanes=True, slot_name='J01', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(118349.4375, 14595.278320313), large=False, heli=False,
                airplanes=True, slot_name='J02', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(118431.1484375, 14312.931640625), large=False, heli=False,
                airplanes=True, slot_name='J04', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(118441.6015625, 14349.5390625), large=False, heli=False,
                airplanes=True, slot_name='J03', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(118586.6484375, 14503.970703125), large=False, heli=False,
                airplanes=True, slot_name='J06', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(118551, 14515.74609375), large=False, heli=False,
                airplanes=True, slot_name='J05', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(118803.6953125, 14758.4375), large=False, heli=False,
                airplanes=True, slot_name='J08', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(118767.34375, 14769.88671875), large=False, heli=False,
                airplanes=True, slot_name='J07', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(118711.5859375, 14901.384765625), large=False, heli=False,
                airplanes=True, slot_name='J10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(118674.890625, 14912.73828125), large=False, heli=False,
                airplanes=True, slot_name='J09', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(118679.9453125, 15105.109375), large=False, heli=False,
                airplanes=True, slot_name='J11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(118690.671875, 15141.571289062), large=False, heli=False,
                airplanes=True, slot_name='J12', length=20.5, width=14.5, height=11.0, shelter=False))


class Bandar_Lengeh(Airport):
    id = 3
    name = "Bandar Lengeh"
    position = mapping.Point(41536.408234, -140987.327942)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Bandar_Lengeh, self).__init__()

        self.runways.append(Runway(80))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(41385.64441061, -140533.0625), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(41388.109597206, -140563.28137207), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(41378.870973349, -140597.828125), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(41378.61730814, -140629.703125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(41366.503915787, -140661.09368896), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))


class Al_Dhafra_AB(Airport):
    id = 4
    name = "Al Dhafra AB"
    position = mapping.Point(-211027.78125, -173240.007813)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Al_Dhafra_AB, self).__init__()

        self.runways.append(Runway(130))
        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-210753.59375, -174987.828125), large=False, heli=False,
                airplanes=True, slot_name='101', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-210738.890625, -174976.171875), large=False, heli=False,
                airplanes=True, slot_name='102', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-210724.75, -174964.015625), large=False, heli=False,
                airplanes=True, slot_name='103', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-210709.84375, -174953.484375), large=False, heli=False,
                airplanes=True, slot_name='104', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-210696.1875, -174943.125), large=False, heli=False,
                airplanes=True, slot_name='105', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-210682.4375, -174931.9375), large=False, heli=False,
                airplanes=True, slot_name='106', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-210666.671875, -174920.859375), large=False, heli=False,
                airplanes=True, slot_name='107', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-210652.953125, -174908.875), large=False, heli=False,
                airplanes=True, slot_name='108', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-210651.359375, -175023.734375), large=False, heli=True,
                airplanes=True, slot_name='100', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-210601.875, -174985.15625), large=False, heli=True,
                airplanes=True, slot_name='99', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-209540.390625, -173990.90625), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-209558.765625, -173965.96875), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-209577.546875, -173939.96875), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-209600.78125, -173906.734375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-209906.78125, -173724.078125), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-209936.15625, -173687.703125), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-209963.703125, -173650.125), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-210102.4375, -173366.640625), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-210124.65625, -173385.578125), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-210148.28125, -173403.0625), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-210170.453125, -173422.140625), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-210207.34375, -173375.03125), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-210183.765625, -173357.53125), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-210161.890625, -173337.8125), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-210139, -173319.609375), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-210220.765625, -173310.390625), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-210243.0625, -173281.46875), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-210267.515625, -173249.625), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-210293.96875, -173216.171875), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-210264.84375, -173205.9375), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-210243.90625, -173233.375), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-210219.8125, -173264.03125), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-210197.484375, -173292.78125), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-210277.453125, -173142), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-210301.453125, -173158.78125), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-210323, -173179.140625), large=False, heli=False,
                airplanes=True, slot_name='26', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-210344.60581236, -173198.93424279), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-210312.625, -173096.9375), large=False, heli=False,
                airplanes=True, slot_name='28', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-210335.09375, -173115.859375), large=False, heli=False,
                airplanes=True, slot_name='29', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-210357.0625, -173135.28125), large=False, heli=False,
                airplanes=True, slot_name='30', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-210380.96875, -173152.078125), large=False, heli=False,
                airplanes=True, slot_name='31', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-210348.296875, -173051.296875), large=False, heli=False,
                airplanes=True, slot_name='32', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-210370, -173070.921875), large=False, heli=False,
                airplanes=True, slot_name='33', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-210392.36756929, -173090.18393736), large=False, heli=False,
                airplanes=True, slot_name='34', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-210415.84375, -173107.4375), large=False, heli=False,
                airplanes=True, slot_name='35', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-210442.71875, -173061.96875), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-210467.171875, -173029.234375), large=False, heli=False,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-210486.046875, -173005.515625), large=False, heli=False,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-210509.296875, -172972.78125), large=False, heli=False,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-210528.390625, -172948.03125), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-210546.984375, -172923.875), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-210560.515625, -172904.71875), large=False, heli=False,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-210579.78125, -172880.015625), large=False, heli=False,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-210597.9375, -172855.609375), large=False, heli=False,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-210613.171875, -172836.453125), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-210632.0625, -172811.421875), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-210650.5625, -172787.328125), large=False, heli=False,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-210770.578125, -172726.015625), large=False, heli=False,
                airplanes=True, slot_name='48', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-210792.359375, -172698.03125), large=False, heli=False,
                airplanes=True, slot_name='49', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-210814.25, -172669.5625), large=False, heli=False,
                airplanes=True, slot_name='50', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-210836.984375, -172642.109375), large=False, heli=False,
                airplanes=True, slot_name='51', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-210858.03125, -172615.09375), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-210880.546875, -172588.4375), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-210803.3125, -172778.078125), large=False, heli=False,
                airplanes=True, slot_name='54', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-210826.34375, -172747.421875), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-210848.046875, -172719.40625), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-210870.5, -172690.671875), large=False, heli=False,
                airplanes=True, slot_name='57', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-210891.28125, -172662.84375), large=False, heli=False,
                airplanes=True, slot_name='58', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-210913.25, -172635.953125), large=False, heli=False,
                airplanes=True, slot_name='59', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-210903.59375, -172482.828125), large=False, heli=False,
                airplanes=True, slot_name='70', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-210920.609375, -172460.890625), large=False, heli=False,
                airplanes=True, slot_name='71', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-210939.15625, -172437.796875), large=False, heli=False,
                airplanes=True, slot_name='72', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-210956.84375, -172414.8125), large=False, heli=False,
                airplanes=True, slot_name='73', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-210974.921875, -172392.125), large=False, heli=False,
                airplanes=True, slot_name='74', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-210992.703125, -172368.734375), large=False, heli=False,
                airplanes=True, slot_name='75', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-211009.5625, -172347.953125), large=False, heli=False,
                airplanes=True, slot_name='76', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-211027.5, -172324.265625), large=False, heli=False,
                airplanes=True, slot_name='77', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-211044.71875, -172302.1875), large=False, heli=False,
                airplanes=True, slot_name='78', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-211062.25, -172279.78125), large=False, heli=False,
                airplanes=True, slot_name='79', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-210856.234375, -172452.15625), large=False, heli=False,
                airplanes=True, slot_name='60', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-210874.53125, -172428.90625), large=False, heli=False,
                airplanes=True, slot_name='61', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-210892.953125, -172405.671875), large=False, heli=False,
                airplanes=True, slot_name='62', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-210910.890625, -172381.96875), large=False, heli=False,
                airplanes=True, slot_name='63', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-210928.640625, -172359.78125), large=False, heli=False,
                airplanes=True, slot_name='64', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-210946.84375, -172336.5625), large=False, heli=False,
                airplanes=True, slot_name='65', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-210964.53125, -172313.59375), large=False, heli=False,
                airplanes=True, slot_name='66', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-210981.890625, -172291.625), large=False, heli=False,
                airplanes=True, slot_name='67', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-210999.1875, -172269.5), large=False, heli=False,
                airplanes=True, slot_name='68', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-211017.5, -172245.109375), large=False, heli=False,
                airplanes=True, slot_name='69', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-211041.5625, -172455.484375), large=False, heli=False,
                airplanes=True, slot_name='80', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-211053.40625, -172440.515625), large=False, heli=False,
                airplanes=True, slot_name='81', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-211064.765625, -172426.125), large=False, heli=False,
                airplanes=True, slot_name='82', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-211075.828125, -172411.6875), large=False, heli=False,
                airplanes=True, slot_name='83', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-211087.25, -172397.359375), large=False, heli=False,
                airplanes=True, slot_name='84', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-211098.53125, -172383.09375), large=False, heli=False,
                airplanes=True, slot_name='85', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-211108.953125, -172369.859375), large=False, heli=False,
                airplanes=True, slot_name='86', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-211376, -172039.078125), large=False, heli=True,
                airplanes=True, slot_name='90', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-211342.46875, -172082.640625), large=False, heli=True,
                airplanes=True, slot_name='89', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-211308.171875, -172127.265625), large=False, heli=True,
                airplanes=True, slot_name='88', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-211271.171875, -172172.375), large=False, heli=True,
                airplanes=True, slot_name='87', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(-211282.578125, -171743.0625), large=False, heli=True,
                airplanes=True, slot_name='91', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-211392.921875, -171600.78125), large=False, heli=True,
                airplanes=True, slot_name='94', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-211441.25, -171645.421875), large=False, heli=True,
                airplanes=True, slot_name='95', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-211346.625, -171766.546875), large=False, heli=True,
                airplanes=True, slot_name='92', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-211381.125, -171828.46875), large=False, heli=True,
                airplanes=True, slot_name='93', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-211491.421875, -171687.265625), large=False, heli=True,
                airplanes=True, slot_name='96', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-211546.625, -171721.40625), large=False, heli=True,
                airplanes=True, slot_name='97', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-212630.109375, -172441.59375), large=False, heli=False,
                airplanes=True, slot_name='185', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-212647.9375, -172417.09375), large=False, heli=False,
                airplanes=True, slot_name='186', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-212667.21875, -172393.0625), large=False, heli=False,
                airplanes=True, slot_name='187', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-212686.078125, -172369), large=False, heli=False,
                airplanes=True, slot_name='188', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-212703.734375, -172344.890625), large=False, heli=False,
                airplanes=True, slot_name='189', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-213346.8125, -171661.484375), large=False, heli=True,
                airplanes=True, slot_name='190', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-213959.375, -171335.515625), large=False, heli=False,
                airplanes=True, slot_name='197', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-213944, -171323.875), large=False, heli=False,
                airplanes=True, slot_name='196', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-213927.1875, -171310.484375), large=False, heli=False,
                airplanes=True, slot_name='195', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-213911.21875, -171298.546875), large=False, heli=False,
                airplanes=True, slot_name='194', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-213895.25, -171286.28125), large=False, heli=False,
                airplanes=True, slot_name='193', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-213876.609375, -171272.75), large=False, heli=False,
                airplanes=True, slot_name='192', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-214253.640625, -171562.40625), large=False, heli=False,
                airplanes=True, slot_name='198', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-214268.921875, -171574.15625), large=False, heli=False,
                airplanes=True, slot_name='199', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-214284.859375, -171588.578125), large=False, heli=False,
                airplanes=True, slot_name='200', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-214301.25, -171600.0625), large=False, heli=False,
                airplanes=True, slot_name='201', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=127, position=mapping.Point(-214316.96875, -171612.6875), large=False, heli=False,
                airplanes=True, slot_name='202', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=128, position=mapping.Point(-214333.96875, -171628.296875), large=False, heli=False,
                airplanes=True, slot_name='203', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-214497.71875, -171752.078125), large=False, heli=False,
                airplanes=True, slot_name='204', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=130, position=mapping.Point(-214503.8125, -171732.25), large=False, heli=False,
                airplanes=True, slot_name='205', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=131, position=mapping.Point(-214534.515625, -171741.265625), large=False, heli=False,
                airplanes=True, slot_name='209', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=132, position=mapping.Point(-214529.265625, -171761.28125), large=False, heli=False,
                airplanes=True, slot_name='208', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=133, position=mapping.Point(-214515.578125, -171699.25), large=False, heli=False,
                airplanes=True, slot_name='206', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=134, position=mapping.Point(-214521.609375, -171680.265625), large=False, heli=False,
                airplanes=True, slot_name='207', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=135, position=mapping.Point(-214544.03125, -171707.671875), large=False, heli=False,
                airplanes=True, slot_name='210', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=136, position=mapping.Point(-214551.421875, -171688.875), large=False, heli=False,
                airplanes=True, slot_name='211', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=137, position=mapping.Point(-214657.1875, -171677.78125), large=False, heli=False,
                airplanes=True, slot_name='212', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=138, position=mapping.Point(-214660.921875, -171657.859375), large=False, heli=False,
                airplanes=True, slot_name='213', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=139, position=mapping.Point(-214692.671875, -171663.03125), large=False, heli=False,
                airplanes=True, slot_name='217', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=140, position=mapping.Point(-214689.625, -171683.4375), large=False, heli=False,
                airplanes=True, slot_name='216', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=141, position=mapping.Point(-214668.265625, -171624.078125), large=False, heli=False,
                airplanes=True, slot_name='214', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=142, position=mapping.Point(-214671.9375, -171604.34375), large=False, heli=False,
                airplanes=True, slot_name='215', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=143, position=mapping.Point(-214700.1875, -171629.734375), large=False, heli=False,
                airplanes=True, slot_name='218', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=144, position=mapping.Point(-214702.625, -171609.59375), large=False, heli=False,
                airplanes=True, slot_name='219', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=145, position=mapping.Point(-214565.421875, -171553.78125), large=False, heli=False,
                airplanes=True, slot_name='220', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=146, position=mapping.Point(-214567.515625, -171533.90625), large=False, heli=False,
                airplanes=True, slot_name='221', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=147, position=mapping.Point(-214570.28125, -171499.21875), large=False, heli=False,
                airplanes=True, slot_name='222', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=148, position=mapping.Point(-214572.296875, -171479.015625), large=False, heli=False,
                airplanes=True, slot_name='223', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=149, position=mapping.Point(-214596.46875, -171557.09375), large=False, heli=False,
                airplanes=True, slot_name='224', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=150, position=mapping.Point(-214597.59375, -171536.09375), large=False, heli=False,
                airplanes=True, slot_name='225', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=151, position=mapping.Point(-214602.15625, -171502.390625), large=False, heli=False,
                airplanes=True, slot_name='226', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=152, position=mapping.Point(-214603.5625, -171482.109375), large=False, heli=False,
                airplanes=True, slot_name='227', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=153, position=mapping.Point(-214751.625, -171451.328125), large=False, heli=False,
                airplanes=True, slot_name='228', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=154, position=mapping.Point(-214750.59375, -171431), large=False, heli=False,
                airplanes=True, slot_name='229', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=155, position=mapping.Point(-214782.375, -171449.75), large=False, heli=False,
                airplanes=True, slot_name='232', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=156, position=mapping.Point(-214781.546875, -171429.25), large=False, heli=False,
                airplanes=True, slot_name='233', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=157, position=mapping.Point(-214747.796875, -171396.40625), large=False, heli=False,
                airplanes=True, slot_name='230', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=158, position=mapping.Point(-214780.34375, -171395.015625), large=False, heli=False,
                airplanes=True, slot_name='234', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=159, position=mapping.Point(-214747.078125, -171376.046875), large=False, heli=False,
                airplanes=True, slot_name='231', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=160, position=mapping.Point(-214778.921875, -171374.34375), large=False, heli=False,
                airplanes=True, slot_name='235', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=161, position=mapping.Point(-214900.171875, -171304.40625), large=False, heli=False,
                airplanes=True, slot_name='236', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=162, position=mapping.Point(-214896.9375, -171284.15625), large=False, heli=False,
                airplanes=True, slot_name='237', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=163, position=mapping.Point(-214932.18347921, -171298.78974972), large=False, heli=False,
                airplanes=True, slot_name='240', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=164, position=mapping.Point(-214928.25, -171278.453125), large=False, heli=False,
                airplanes=True, slot_name='241', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=165, position=mapping.Point(-214890.484375, -171249.1875), large=False, heli=False,
                airplanes=True, slot_name='238', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=166, position=mapping.Point(-214921.625, -171244.4375), large=False, heli=False,
                airplanes=True, slot_name='242', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=167, position=mapping.Point(-214886.890625, -171229.484375), large=False, heli=False,
                airplanes=True, slot_name='239', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=168, position=mapping.Point(-214917.78125, -171224.25), large=False, heli=False,
                airplanes=True, slot_name='243', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=169, position=mapping.Point(-214903.390625, -171158.171875), large=False, heli=False,
                airplanes=True, slot_name='244', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=170, position=mapping.Point(-214897.34375, -171139.578125), large=False, heli=False,
                airplanes=True, slot_name='245', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=171, position=mapping.Point(-214933.53125, -171149.453125), large=False, heli=False,
                airplanes=True, slot_name='248', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=172, position=mapping.Point(-214927.546875, -171130.21875), large=False, heli=False,
                airplanes=True, slot_name='249', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=173, position=mapping.Point(-214887.984375, -171106), large=False, heli=False,
                airplanes=True, slot_name='246', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=174, position=mapping.Point(-214881.8125, -171087.15625), large=False, heli=False,
                airplanes=True, slot_name='247', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=175, position=mapping.Point(-214917.9375, -171097.46875), large=False, heli=False,
                airplanes=True, slot_name='250', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=176, position=mapping.Point(-214910.984375, -171077.625), large=False, heli=False,
                airplanes=True, slot_name='251', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=177, position=mapping.Point(-214250.828125, -172216.921875), large=False, heli=True,
                airplanes=False, slot_name='191', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=178, position=mapping.Point(-213414.375, -173007.84375), large=False, heli=False,
                airplanes=True, slot_name='169', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=179, position=mapping.Point(-213398.6875, -173027.6875), large=False, heli=False,
                airplanes=True, slot_name='168', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=180, position=mapping.Point(-213383.359375, -173047.671875), large=False, heli=False,
                airplanes=True, slot_name='167', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=181, position=mapping.Point(-213367.71875, -173067.5625), large=False, heli=False,
                airplanes=True, slot_name='166', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=182, position=mapping.Point(-213353.21875, -173087.0625), large=False, heli=False,
                airplanes=True, slot_name='165', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=183, position=mapping.Point(-213319.09375, -173130.328125), large=False, heli=False,
                airplanes=True, slot_name='164', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=184, position=mapping.Point(-213303.234375, -173150.25), large=False, heli=False,
                airplanes=True, slot_name='163', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=185, position=mapping.Point(-213287.640625, -173170.3125), large=False, heli=False,
                airplanes=True, slot_name='162', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=186, position=mapping.Point(-213272.15625, -173190.015625), large=False, heli=False,
                airplanes=True, slot_name='161', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=187, position=mapping.Point(-213257.1875, -173209.625), large=False, heli=False,
                airplanes=True, slot_name='160', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=188, position=mapping.Point(-213222.484375, -173253.609375), large=False, heli=False,
                airplanes=True, slot_name='159', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=189, position=mapping.Point(-213206.78125, -173273.640625), large=False, heli=False,
                airplanes=True, slot_name='158', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=190, position=mapping.Point(-213191.390625, -173293.78125), large=False, heli=False,
                airplanes=True, slot_name='157', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=191, position=mapping.Point(-213175.84375, -173313.46875), large=False, heli=False,
                airplanes=True, slot_name='156', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=192, position=mapping.Point(-213160.78125, -173333.015625), large=False, heli=False,
                airplanes=True, slot_name='155', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=193, position=mapping.Point(-213449.9375, -173037.21875), large=False, heli=False,
                airplanes=True, slot_name='184', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=194, position=mapping.Point(-213434, -173058.359375), large=False, heli=False,
                airplanes=True, slot_name='183', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=195, position=mapping.Point(-213418.625, -173077.828125), large=False, heli=False,
                airplanes=True, slot_name='182', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=196, position=mapping.Point(-213401.859375, -173099.5), large=False, heli=False,
                airplanes=True, slot_name='181', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=197, position=mapping.Point(-213385.71875, -173119.015625), large=False, heli=False,
                airplanes=True, slot_name='180', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=198, position=mapping.Point(-213349.84375, -173165.40625), large=False, heli=False,
                airplanes=True, slot_name='179', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=199, position=mapping.Point(-213333.875, -173186.140625), large=False, heli=False,
                airplanes=True, slot_name='178', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=200, position=mapping.Point(-213318.59375, -173205.125), large=False, heli=False,
                airplanes=True, slot_name='177', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=201, position=mapping.Point(-213301.6875, -173227.015625), large=False, heli=False,
                airplanes=True, slot_name='176', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=202, position=mapping.Point(-213285.890625, -173247.34375), large=False, heli=False,
                airplanes=True, slot_name='175', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=203, position=mapping.Point(-213256.9375, -173284.890625), large=False, heli=False,
                airplanes=True, slot_name='174', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=204, position=mapping.Point(-213240.90625, -173305.203125), large=False, heli=False,
                airplanes=True, slot_name='173', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=205, position=mapping.Point(-213225.59375, -173324.5625), large=False, heli=False,
                airplanes=True, slot_name='172', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=206, position=mapping.Point(-213208.640625, -173346.296875), large=False, heli=False,
                airplanes=True, slot_name='171', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=207, position=mapping.Point(-213192.625, -173366.46875), large=False, heli=False,
                airplanes=True, slot_name='170', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=208, position=mapping.Point(-212562.15625, -174157.390625), large=False, heli=False,
                airplanes=True, slot_name='149', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=209, position=mapping.Point(-212546.859375, -174177.640625), large=False, heli=False,
                airplanes=True, slot_name='148', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=210, position=mapping.Point(-212530.953125, -174197.609375), large=False, heli=False,
                airplanes=True, slot_name='147', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=211, position=mapping.Point(-212515.125, -174218.03125), large=False, heli=False,
                airplanes=True, slot_name='146', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=212, position=mapping.Point(-212500.53125, -174237.265625), large=False, heli=False,
                airplanes=True, slot_name='145', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=213, position=mapping.Point(-212462.109375, -174286.53125), large=False, heli=False,
                airplanes=True, slot_name='138', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=214, position=mapping.Point(-212445.4375, -174307.53125), large=False, heli=False,
                airplanes=True, slot_name='137', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=215, position=mapping.Point(-212428.90625, -174328.484375), large=False, heli=False,
                airplanes=True, slot_name='136', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=216, position=mapping.Point(-212413.65625, -174348.34375), large=False, heli=False,
                airplanes=True, slot_name='135', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=217, position=mapping.Point(-212397.828125, -174368.875), large=False, heli=False,
                airplanes=True, slot_name='134', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=218, position=mapping.Point(-212382.796875, -174388.078125), large=False, heli=False,
                airplanes=True, slot_name='133', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=219, position=mapping.Point(-212425.34375, -174432.640625), large=False, heli=False,
                airplanes=True, slot_name='139', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=220, position=mapping.Point(-212441.3125, -174411.8125), large=False, heli=False,
                airplanes=True, slot_name='140', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=221, position=mapping.Point(-212457.671875, -174390.5625), large=False, heli=False,
                airplanes=True, slot_name='141', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=222, position=mapping.Point(-212474.171875, -174369.515625), large=False, heli=False,
                airplanes=True, slot_name='142', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=223, position=mapping.Point(-212490.234375, -174349.125), large=False, heli=False,
                airplanes=True, slot_name='143', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=224, position=mapping.Point(-212505.328125, -174329.3125), large=False, heli=False,
                airplanes=True, slot_name='144', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=225, position=mapping.Point(-212544.484375, -174279.578125), large=False, heli=False,
                airplanes=True, slot_name='150', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=226, position=mapping.Point(-212561, -174258.40625), large=False, heli=False,
                airplanes=True, slot_name='151', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=227, position=mapping.Point(-212577.484375, -174237.203125), large=False, heli=False,
                airplanes=True, slot_name='152', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=228, position=mapping.Point(-212593.453125, -174217.109375), large=False, heli=False,
                airplanes=True, slot_name='153', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=229, position=mapping.Point(-212608.71875, -174196.765625), large=False, heli=False,
                airplanes=True, slot_name='154', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=230, position=mapping.Point(-212359.125, -174711.84375), large=False, heli=False,
                airplanes=True, slot_name='132', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=231, position=mapping.Point(-212343.15625, -174699.640625), large=False, heli=False,
                airplanes=True, slot_name='131', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=232, position=mapping.Point(-212325.72694429, -174687.24730267), large=False, heli=False,
                airplanes=True, slot_name='130', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=233, position=mapping.Point(-212310.296875, -174674.375), large=False, heli=False,
                airplanes=True, slot_name='129', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=234, position=mapping.Point(-212294.28125, -174662.15625), large=False, heli=False,
                airplanes=True, slot_name='128', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=235, position=mapping.Point(-212277.484375, -174651.28125), large=False, heli=False,
                airplanes=True, slot_name='127', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=236, position=mapping.Point(-212260.578125, -174638.21875), large=False, heli=False,
                airplanes=True, slot_name='126', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=237, position=mapping.Point(-212246, -174625.625), large=False, heli=False,
                airplanes=True, slot_name='125', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=238, position=mapping.Point(-212038.359375, -174593.625), large=False, heli=False,
                airplanes=True, slot_name='124', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=239, position=mapping.Point(-212021.390625, -174580.609375), large=False, heli=False,
                airplanes=True, slot_name='123', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=240, position=mapping.Point(-212005.90625, -174567.859375), large=False, heli=False,
                airplanes=True, slot_name='122', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=241, position=mapping.Point(-211989.84375, -174555.65625), large=False, heli=False,
                airplanes=True, slot_name='121', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=242, position=mapping.Point(-211974.03125, -174543.53125), large=False, heli=False,
                airplanes=True, slot_name='120', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=243, position=mapping.Point(-211956.28125, -174531.421875), large=False, heli=False,
                airplanes=True, slot_name='119', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=244, position=mapping.Point(-211940.65625, -174520.34375), large=False, heli=False,
                airplanes=True, slot_name='118', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=245, position=mapping.Point(-211662.65625, -174298.671875), large=False, heli=False,
                airplanes=True, slot_name='116', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=246, position=mapping.Point(-211647.21875, -174287.078125), large=False, heli=False,
                airplanes=True, slot_name='115', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=247, position=mapping.Point(-211630.40625, -174273.859375), large=False, heli=False,
                airplanes=True, slot_name='114', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=248, position=mapping.Point(-211614.515625, -174261.75), large=False, heli=False,
                airplanes=True, slot_name='113', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=249, position=mapping.Point(-211598.828125, -174249.09375), large=False, heli=False,
                airplanes=True, slot_name='112', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=250, position=mapping.Point(-211582.796875, -174237.265625), large=False, heli=False,
                airplanes=True, slot_name='111', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=251, position=mapping.Point(-211565.96875, -174223.921875), large=False, heli=False,
                airplanes=True, slot_name='110', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=252, position=mapping.Point(-211549.765625, -174212.0625), large=False, heli=False,
                airplanes=True, slot_name='109', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=253, position=mapping.Point(-211593.0625, -171758.296875), large=False, heli=True,
                airplanes=True, slot_name='98', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Dubai_Intl(Airport):
    id = 5
    name = "Dubai Intl"
    position = mapping.Point(-100594.371094, -88875.371094)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Dubai_Intl, self).__init__()

        self.runways.append(Runway(300))
        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-101536.4765625, -88944.609375), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-101659.375, -88752.8359375), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-101462.375, -89063.1484375), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-101388.6875, -89181.7734375), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-101315.046875, -89300.40625), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-101203.3125, -89477.7734375), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-101112.15625, -89624.046875), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-100964.2734375, -89861.078125), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-101749.0703125, -88995.5234375), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-101675.1171875, -89113.984375), large=False, heli=True,
                airplanes=True, slot_name='24', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-101561.53125, -89295.6484375), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-101487.359375, -89414.203125), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-101376.21875, -89591.71875), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-101265.203125, -89769.21875), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-101173.9453125, -89915.6640625), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-101099.3203125, -90033.625), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-101018.578125, -90142.0546875), large=False, heli=True,
                airplanes=True, slot_name='31', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-100962.6171875, -90228.7265625), large=False, heli=True,
                airplanes=True, slot_name='32', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-100923.15625, -90291.8671875), large=False, heli=True,
                airplanes=True, slot_name='33', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-100896.03125, -90335.1640625), large=False, heli=True,
                airplanes=True, slot_name='34', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-100738.2734375, -90219.8671875), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-100851.9921875, -90038.515625), large=False, heli=True,
                airplanes=True, slot_name='14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-101959.875, -88561.6640625), large=False, heli=True,
                airplanes=True, slot_name='78', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-102106.109375, -88329.0390625), large=False, heli=True,
                airplanes=True, slot_name='79', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-102200.828125, -88179.2578125), large=False, heli=True,
                airplanes=True, slot_name='80', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-102248.1015625, -88104.5625), large=False, heli=True,
                airplanes=True, slot_name='81', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-102346.46875, -87933.84375), large=False, heli=True,
                airplanes=True, slot_name='82', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-102129.5703125, -87898.8203125), large=False, heli=True,
                airplanes=True, slot_name='77', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-102036.5546875, -88049.2265625), large=False, heli=True,
                airplanes=True, slot_name='76', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-101989.90625, -88124.5390625), large=False, heli=True,
                airplanes=True, slot_name='75', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-101896.5859375, -88274.7734375), large=False, heli=True,
                airplanes=True, slot_name='74', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-101847.671875, -88353.609375), large=False, heli=True,
                airplanes=True, slot_name='73', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-102313.96875, -87531.265625), large=False, heli=True,
                airplanes=True, slot_name='83', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-102387.859375, -87411.6328125), large=False, heli=True,
                airplanes=True, slot_name='84', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-102462.0859375, -87294.1171875), large=False, heli=True,
                airplanes=True, slot_name='85', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-102536.390625, -87175.875), large=False, heli=True,
                airplanes=True, slot_name='86', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-102695.9296875, -87089.921875), large=False, heli=True,
                airplanes=True, slot_name='87', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-102817.328125, -87160.484375), large=False, heli=True,
                airplanes=True, slot_name='88', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-102931.9296875, -87026.546875), large=False, heli=True,
                airplanes=True, slot_name='89', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-102816.234375, -86948.8515625), large=False, heli=True,
                airplanes=True, slot_name='90', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-102700.3828125, -86872.484375), large=False, heli=True,
                airplanes=True, slot_name='91', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-103094.5546875, -86333.859375), large=False, heli=True,
                airplanes=True, slot_name='93', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-103177.71875, -86203.2578125), large=False, heli=True,
                airplanes=True, slot_name='94', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-103353.5, -85889.2265625), large=False, heli=True,
                airplanes=True, slot_name='96', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-103269.9375, -86032.7421875), large=False, heli=True,
                airplanes=True, slot_name='95', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-103040.6875, -86446.234375), large=False, heli=True,
                airplanes=True, slot_name='92', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-99332.8515625, -90198.265625), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-99406.8515625, -90079.671875), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-99481.0234375, -89961.21875), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-99555.0625, -89842.875), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-99629.1015625, -89724.2734375), large=False, heli=True,
                airplanes=True, slot_name='39', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-99703.1875, -89605.8203125), large=False, heli=True,
                airplanes=True, slot_name='40', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-99777.078125, -89487.34375), large=False, heli=True,
                airplanes=True, slot_name='41', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-99851.1875, -89368.8046875), large=False, heli=True,
                airplanes=True, slot_name='42', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-99925.3125, -89250.3828125), large=False, heli=True,
                airplanes=True, slot_name='43', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-99999.3125, -89131.8125), large=False, heli=True,
                airplanes=True, slot_name='44', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-100073.328125, -89013.4296875), large=False, heli=True,
                airplanes=True, slot_name='45', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-100147.5625, -88894.953125), large=False, heli=True,
                airplanes=True, slot_name='46', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-100221.703125, -88776.6171875), large=False, heli=True,
                airplanes=True, slot_name='47', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-100295.7265625, -88658.046875), large=False, heli=True,
                airplanes=True, slot_name='48', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-100369.921875, -88539.5), large=False, heli=True,
                airplanes=True, slot_name='49', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-100438.53125, -88423.4375), large=False, heli=True,
                airplanes=True, slot_name='50', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-100651.109375, -88089.3515625), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-100624.90625, -88130.9921875), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-100605.1015625, -88162.640625), large=False, heli=True,
                airplanes=True, slot_name='58', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-100585.3515625, -88194.265625), large=False, heli=True,
                airplanes=True, slot_name='57', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-100565.5625, -88225.8515625), large=False, heli=True,
                airplanes=True, slot_name='56', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-100545.890625, -88257.5), large=False, heli=True,
                airplanes=True, slot_name='55', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-100526.0546875, -88289.015625), large=False, heli=True,
                airplanes=True, slot_name='54', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-100506.4140625, -88320.65625), large=False, heli=True,
                airplanes=True, slot_name='53', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-100486.6484375, -88352.234375), large=False, heli=True,
                airplanes=True, slot_name='52', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-100466.6796875, -88383.2265625), large=False, heli=True,
                airplanes=True, slot_name='51', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-100759.609375, -87915.8203125), large=False, heli=True,
                airplanes=True, slot_name='68', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-100657.40625, -87912.3046875), large=False, heli=True,
                airplanes=True, slot_name='67', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-101014.34375, -87369.8828125), large=False, heli=True,
                airplanes=True, slot_name='69', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-101076.9765625, -87270.375), large=False, heli=True,
                airplanes=True, slot_name='70', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-101121.0625, -87200.46875), large=False, heli=True,
                airplanes=True, slot_name='71', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-101183.078125, -87099.3984375), large=False, heli=True,
                airplanes=True, slot_name='72', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-99985.4375, -90875.6953125), large=False, heli=True,
                airplanes=True, slot_name='08', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-99873.3984375, -91056.0546875), large=False, heli=True,
                airplanes=True, slot_name='07', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-99738.8046875, -91171.65625), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-99663.0625, -91289.9453125), large=False, heli=True,
                airplanes=True, slot_name='03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-99537.1015625, -91276.390625), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-99579.9609375, -91209.5859375), large=False, heli=True,
                airplanes=True, slot_name='02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-100065.21875, -91519.8671875), large=False, heli=True,
                airplanes=True, slot_name='11', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-100187.125, -91478.0625), large=False, heli=True,
                airplanes=True, slot_name='12', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-99960.6015625, -91457.8359375), large=False, heli=True,
                airplanes=True, slot_name='10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-99874.8046875, -91394.8984375), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-99799.125, -90966.65625), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-99872.3046875, -90849.5546875), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-100497.671875, -87813.1015625), large=False, heli=True,
                airplanes=True, slot_name='63', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-100618.0546875, -87887.703125), large=False, heli=True,
                airplanes=True, slot_name='66', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-100578.3203125, -87862.75), large=False, heli=True,
                airplanes=True, slot_name='65', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-100537.796875, -87838.5390625), large=False, heli=True,
                airplanes=True, slot_name='64', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-100556.3359375, -88000.8359375), large=False, heli=True,
                airplanes=True, slot_name='61', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-100516.890625, -87976.8125), large=False, heli=True,
                airplanes=True, slot_name='62', length=43.057953, width=40.0, height=None, shelter=False))


class Al_Maktoum_Intl(Airport):
    id = 6
    name = "Al Maktoum Intl"
    position = mapping.Point(-140127.671875, -110068.890625)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Al_Maktoum_Intl, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-140247.46875, -111218.859375), large=False, heli=True,
                airplanes=False, slot_name='14', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-140281.8125, -111163.859375), large=False, heli=True,
                airplanes=False, slot_name='15', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-140326.34375, -111096.9921875), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-140379.34375, -111012.0078125), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-140440.5625, -110914.25), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-140480.5, -110850.671875), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-140599.609375, -110660.484375), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-140639.375, -110596.9140625), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-140390.921875, -111313.609375), large=False, heli=True,
                airplanes=True, slot_name='13', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-140454.625, -111354.0625), large=False, heli=True,
                airplanes=True, slot_name='12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-140518.203125, -111393.875), large=False, heli=True,
                airplanes=True, slot_name='11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-140582.734375, -111433.1171875), large=False, heli=True,
                airplanes=True, slot_name='10', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-140645.640625, -111473.8046875), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-140722.90625, -111520.4375), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-140790.96875, -111564.296875), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-140850.3125, -111599.6953125), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-140914.453125, -111641.09375), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-140990.578125, -111687.625), large=False, heli=True,
                airplanes=True, slot_name='04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-141062.953125, -111732.8125), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-141126.9375, -111772.5390625), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-141185.28125, -111808.8671875), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-141080.796875, -110527.4375), large=False, heli=True,
                airplanes=True, slot_name='32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-141148.859375, -110569.9296875), large=False, heli=True,
                airplanes=True, slot_name='31', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-141216.65625, -110612.328125), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-141284.890625, -110654.765625), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-140794.828125, -110664.1640625), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-140921.125, -110743.0390625), large=False, heli=True,
                airplanes=True, slot_name='23', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-141031.3125, -110811.5546875), large=False, heli=True,
                airplanes=True, slot_name='24', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-141141.5625, -110880.546875), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-141306.859375, -110984.15625), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-141417.03125, -111052.765625), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-141527.3125, -111121.5546875), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-140832.234375, -110287.03125), large=False, heli=True,
                airplanes=True, slot_name='33', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-140871.578125, -110223.59375), large=False, heli=True,
                airplanes=True, slot_name='34', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-140916.234375, -110151.0859375), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-140968.875, -110065.84375), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-141051.25, -109933.40625), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-141130.1875, -109806.7578125), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-141199.640625, -109696.5234375), large=False, heli=True,
                airplanes=True, slot_name='39', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-142040.546875, -108353.59375), large=False, heli=True,
                airplanes=True, slot_name='40', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-142093.671875, -108268.6484375), large=False, heli=True,
                airplanes=True, slot_name='41', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-142146.84375, -108184), large=False, heli=True,
                airplanes=True, slot_name='42', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-142200, -108099.609375), large=False, heli=True,
                airplanes=True, slot_name='43', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-142306.203125, -107929.921875), large=False, heli=True,
                airplanes=True, slot_name='44', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-142354.046875, -107853.8515625), large=False, heli=True,
                airplanes=True, slot_name='45', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-142393.96875, -107790.3203125), large=False, heli=True,
                airplanes=True, slot_name='46', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-142433.953125, -107726.8046875), large=False, heli=True,
                airplanes=True, slot_name='47', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-142473.46875, -107663.3203125), large=False, heli=True,
                airplanes=True, slot_name='48', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-142513.34375, -107599.7109375), large=False, heli=True,
                airplanes=True, slot_name='49', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-142553.671875, -107536.515625), large=False, heli=True,
                airplanes=True, slot_name='50', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-141037.265625, -112023.875), large=False, heli=True,
                airplanes=True, slot_name='69', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-140973.65625, -111984.0625), large=False, heli=True,
                airplanes=True, slot_name='68', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-140909.609375, -111945.3046875), large=False, heli=True,
                airplanes=True, slot_name='67', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-140845.65625, -111906.21875), large=False, heli=True,
                airplanes=True, slot_name='66', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-140700.015625, -111815.2734375), large=False, heli=True,
                airplanes=True, slot_name='65', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-140640.75, -111779.59375), large=False, heli=True,
                airplanes=True, slot_name='64', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-140577.8125, -111738.1875), large=False, heli=True,
                airplanes=True, slot_name='63', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-140501.125, -111691.53125), large=False, heli=True,
                airplanes=True, slot_name='62', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-140427.5, -111648.375), large=False, heli=True,
                airplanes=True, slot_name='61', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-140363.9375, -111607.9921875), large=False, heli=True,
                airplanes=True, slot_name='60', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-140306.78125, -111569.875), large=False, heli=True,
                airplanes=True, slot_name='59', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-143019.234375, -109123.5546875), large=False, heli=True,
                airplanes=True, slot_name='54', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-142960.53125, -109087.5), large=False, heli=True,
                airplanes=True, slot_name='53', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-142896.40625, -109047.9296875), large=False, heli=True,
                airplanes=True, slot_name='52', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-142769.03125, -108970.9921875), large=False, heli=True,
                airplanes=True, slot_name='51', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-143099.71875, -108999.578125), large=False, heli=True,
                airplanes=True, slot_name='58', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-142975.6875, -108925.21875), large=False, heli=True,
                airplanes=True, slot_name='57', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-142912.75, -108885.8046875), large=False, heli=True,
                airplanes=True, slot_name='56', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-142848.734375, -108847.640625), large=False, heli=True,
                airplanes=True, slot_name='55', length=43.057953, width=40.0, height=None, shelter=False))


class Fujairah_Intl(Airport):
    id = 7
    name = "Fujairah Intl"
    position = mapping.Point(-117531.972946, 7939.275818)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Fujairah_Intl, self).__init__()

        self.runways.append(Runway(290))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-117293.855896, 8304.8382568359), large=False, heli=True,
                airplanes=True, slot_name='01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-117250.05471802, 8540.6785888672), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-117313.23373413, 8519.846862793), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-117374.25790405, 8477.9990234375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))


class Tunb_Island_AFB(Airport):
    id = 8
    name = "Tunb Island AFB"
    position = mapping.Point(10515.440918, -92440.328125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tunb_Island_AFB, self).__init__()

        self.runways.append(Runway(30))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(10327.60546875, -92808.609375), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(10350.327148438, -92838.28125), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(10314.954101562, -92779.4453125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(10298.874023438, -92745.8203125), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))


class Havadarya(Airport):
    id = 9
    name = "Havadarya"
    position = mapping.Point(109297.824219, -6278.723145)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Havadarya, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(109336.5078125, -6856.7319335937), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(109384.078125, -6866.2299804687), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(109391.328125, -6827.91796875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(109372.765625, -7220.5078125), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(109348.5, -7215.0791015625), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(109324.28125, -7210.3315429688), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(109299.640625, -7204.5029296875), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(109272.6796875, -7198.9067382812), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(109248.265625, -7192.9736328125), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(109245.078125, -7286.328125), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(109239.9765625, -7311.9287109375), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(109234.546875, -7339.501953125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(109228.7421875, -7366.6264648438), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(109344.4609375, -6815.3618164063), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(109184.8671875, -5813.2958984375), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(109147.421875, -5806.8813476563), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(109208.40625, -5691.572265625), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(109171.203125, -5683.9223632812), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(109191.375, -5780.2827148437), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(109153.9140625, -5772.7641601563), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(109215.3671875, -5657.0385742187), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(109177.734375, -5649.7006835937), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))


class Khasab(Airport):
    id = 10
    name = "Khasab"
    position = mapping.Point(-219.726892, -177.707709)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Khasab, self).__init__()

        self.runways.append(Runway(190))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-1017.2598266602, -602.64483642578), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-993.78546142578, -596.85540771484), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-970.39038085937, -590.92138671875), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-946.86694335938, -585.11224365234), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-923.39343261719, -579.32574462891), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-899.84790039063, -573.57952880859), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-876.40319824219, -567.68103027344), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-787.23937988281, -547.58770751953), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-763.80834960937, -541.49548339844), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-740.30584716797, -535.81024169922), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-714.90942382813, -530.10400390625), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-673.22117416432, -522.01122705626), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))


class Lar_Airbase(Airport):
    id = 11
    name = "Lar Airbase"
    position = mapping.Point(168977.578922, -182359.639734)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lar_Airbase, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(168556.390625, -182527.234375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(168561.5625, -182399.140625), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(168562.390625, -182481.734375), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(168562.109375, -182430.84375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(168614.578125, -182785.015625), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))


class Al_Minhad_AB(Airport):
    id = 12
    name = "Al Minhad AB"
    position = mapping.Point(-126013.707153, -89133.460938)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Al_Minhad_AB, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-126253.08361816, -89660.172302246), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-126302.70910645, -89660.520629883), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-126353.11022949, -89659.443786621), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-126253.17944336, -89561.108947754), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-126302.8203125, -89560.616333008), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-126353.41662598, -89559.875244141), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-126252.84289551, -89459.989013672), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-126302.9921875, -89459.988525391), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-126353.63293457, -89458.822753906), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-126315.5078125, -89380.320251465), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-126353.45446777, -89388.752197266), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-126353.33312988, -89500.376831055), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-126302.64611816, -89499.628967285), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-126252.89318848, -89499.913757324), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-126253.06750488, -89599.119384766), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-126302.78125, -89598.968688965), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-126353.2578125, -89599.073547363), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-126378.796875, -90475.5), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-126378.93737793, -90433.34362793), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-126378.7734375, -90392.5859375), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-126378.62463379, -90350.187866211), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-126378.9765625, -90309.515625), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-126379.34362793, -90267.74987793), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-126378.59375, -90226.6796875), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-126378.328125, -90184.28125), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-126378.71081543, -90143.51550293), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-126317.85949707, -90475.913452148), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-126318.03112793, -90434.05480957), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-126317.89868164, -90393.296386719), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-126317.72705078, -90351.29675293), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-126317.21862793, -90309.63293457), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-126318.00012207, -90268.30480957), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-126317.5234375, -90227.2890625), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-126317.69555664, -90185.58581543), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-126317.62487793, -90144.21105957), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-126315.45324707, -89229.179931641), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-126315.69543457, -89204.4609375), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-126314.4453125, -89028.7265625), large=False, heli=True,
                airplanes=True, slot_name='42', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-126335.625, -88954.890640259), large=False, heli=True,
                airplanes=True, slot_name='Stand01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-126381.17199707, -88950.023422241), large=False, heli=True,
                airplanes=True, slot_name='43', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-126320.47387695, -88654.495857239), large=False, heli=True,
                airplanes=True, slot_name='47', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-126369.56311035, -88862.332321167), large=False, heli=True,
                airplanes=True, slot_name='44', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-126370.4251709, -88802.528015137), large=False, heli=True,
                airplanes=True, slot_name='45', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-126370.60241699, -88747.73041153), large=False, heli=True,
                airplanes=True, slot_name='46', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-126380.29626465, -88651.143424988), large=False, heli=True,
                airplanes=True, slot_name='48', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-126312.14245605, -88090.050231934), large=False, heli=True,
                airplanes=True, slot_name='49', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-126312.02441406, -88000.29095459), large=False, heli=True,
                airplanes=True, slot_name='50', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-126312.03369141, -87610.740844727), large=False, heli=False,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-126311.96899414, -87586.267211914), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-126312.19165039, -87562.348022461), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-126312.15795898, -87538.94140625), large=False, heli=False,
                airplanes=True, slot_name='54', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-126312.00500488, -87515.07409668), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-126311.92248535, -87488.044921875), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-126342.4822998, -87617.952758789), large=False, heli=False,
                airplanes=True, slot_name='57', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-126342.41821289, -87587.591064453), large=False, heli=False,
                airplanes=True, slot_name='58', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-126342.60693359, -87557.223388672), large=False, heli=False,
                airplanes=True, slot_name='59', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-126342.60864258, -87527.473510742), large=False, heli=False,
                airplanes=True, slot_name='60', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-126342.72473145, -87497.182617188), large=False, heli=False,
                airplanes=True, slot_name='61', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-126515.6953125, -90985.948486328), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-126580.08117676, -90985.940673828), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-126580.07641602, -90906.190673828), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-126515.65429688, -90906.147460938), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))


class Qeshm_Island(Airport):
    id = 13
    name = "Qeshm Island"
    position = mapping.Point(64800.714844, -33383.481445)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Qeshm_Island, self).__init__()

        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(65148.21875, -33696.6328125), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(65102.96484375, -33751.9140625), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(65058.5234375, -33805.59375), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(65014.59375, -33858.51953125), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(64968.7109375, -33909.875), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(64922.87109375, -33966.51953125), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(64865.3828125, -34016.39453125), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(64812.84765625, -34082.34765625), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(64761.55859375, -34141.59765625), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(64731.578125, -33924.45703125), large=False, heli=True,
                airplanes=True, slot_name='11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(64689.7890625, -33968.71875), large=False, heli=True,
                airplanes=True, slot_name='12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(64773.828125, -33869.1015625), large=False, heli=True,
                airplanes=True, slot_name='10', length=43.057953, width=40.0, height=None, shelter=False))


class Sharjah_Intl(Airport):
    id = 14
    name = "Sharjah Intl"
    position = mapping.Point(-92544.089844, -73373.601563)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Sharjah_Intl, self).__init__()

        self.runways.append(Runway(300))
        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-93511.0078125, -72815.6015625), large=False, heli=True,
                airplanes=True, slot_name='46', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-93548.203125, -72841.1015625), large=False, heli=True,
                airplanes=True, slot_name='45', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-93586.015625, -72865.5078125), large=False, heli=True,
                airplanes=True, slot_name='44', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-93732.7265625, -72655.046875), large=False, heli=True,
                airplanes=True, slot_name='47', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-93450.328125, -73049.34375), large=False, heli=True,
                airplanes=True, slot_name='41', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-93490.078125, -72985.984375), large=False, heli=True,
                airplanes=True, slot_name='42', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-93408.4765625, -73111.5703125), large=False, heli=True,
                airplanes=True, slot_name='40', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-93367.296875, -73174.4140625), large=False, heli=True,
                airplanes=True, slot_name='39', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-93326.421875, -73237.0546875), large=False, heli=True,
                airplanes=True, slot_name='38', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-93286.046875, -73300.328125), large=False, heli=True,
                airplanes=True, slot_name='37', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-93172.2265625, -73366.796875), large=False, heli=True,
                airplanes=True, slot_name='34', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-93209.9609375, -73391.234375), large=False, heli=True,
                airplanes=True, slot_name='35', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-93247.484375, -73415.765625), large=False, heli=True,
                airplanes=True, slot_name='36', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-93138.5078125, -73583.796875), large=False, heli=True,
                airplanes=True, slot_name='30', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-93100.859375, -73559.40625), large=False, heli=True,
                airplanes=True, slot_name='29', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-93063.2578125, -73534.875), large=False, heli=True,
                airplanes=True, slot_name='28', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-93030.09375, -73750.25), large=False, heli=True,
                airplanes=True, slot_name='24', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-92992.53125, -73726.1875), large=False, heli=True,
                airplanes=True, slot_name='23', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-92954.671875, -73701.6484375), large=False, heli=True,
                airplanes=True, slot_name='22', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-93091.609375, -73656.0546875), large=False, heli=True,
                airplanes=True, slot_name='27', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-93054.171875, -73631.4921875), large=False, heli=True,
                airplanes=True, slot_name='26', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-93016.234375, -73606.9296875), large=False, heli=True,
                airplanes=True, slot_name='25', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-93125.2890625, -73439.4140625), large=False, heli=True,
                airplanes=True, slot_name='31', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-93163.140625, -73464.140625), large=False, heli=True,
                airplanes=True, slot_name='32', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-93200.71875, -73488.53125), large=False, heli=True,
                airplanes=True, slot_name='33', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-92966.6875, -73998.8671875), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-93066.765625, -74065.2265625), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-93166.5859375, -74131.7734375), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-93268.15625, -74195.6484375), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-93167.578125, -74350.6953125), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-93066.546875, -74286.0859375), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-92967.390625, -74218.4609375), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-92869.6796875, -74147.6015625), large=False, heli=True,
                airplanes=True, slot_name='14', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-92321.4296875, -75170.703125), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-92380.546875, -75232.515625), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-92480.5234375, -75270.234375), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-92361.0703125, -74968.0546875), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-92377.6484375, -74942.921875), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-92393.9765625, -74917.7421875), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-92410.21875, -74892.4765625), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-92184.296875, -75476.1328125), large=False, heli=True,
                airplanes=True, slot_name='06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-91881.9140625, -75455.484375), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-91838.046875, -75521.953125), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-91805.5078125, -75572.7109375), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-91775.453125, -75618.5), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-91745.53125, -75664.6875), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-93530.78125, -72922.8984375), large=False, heli=True,
                airplanes=True, slot_name='43', length=43.057953, width=40.0, height=None, shelter=False))


class Sirri_Island(Airport):
    id = 15
    name = "Sirri Island"
    position = mapping.Point(-26946.104553, -170745.015625)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sirri_Island, self).__init__()

        self.runways.append(Runway(300))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-27713.302612305, -170052.375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-27754.28125, -169999.1875), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))


class Tunb_Kochak(Airport):
    id = 16
    name = "Tunb Kochak"
    position = mapping.Point(9023.430176, -109467.078125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tunb_Kochak, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(8992.48046875, -109345.625), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(9012.076171875, -109348.078125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=11.0, shelter=False))


class Sir_Abu_Nuayr(Airport):
    id = 17
    name = "Sir Abu Nuayr"
    position = mapping.Point(-103102.871094, -202973.078125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sir_Abu_Nuayr, self).__init__()

        self.runways.append(Runway(280))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-103019.671875, -203136.546875), large=False, heli=True,
                airplanes=True, slot_name='02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-102999.2421875, -203072.890625), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-102994.6171875, -203101.765625), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-102984.8203125, -203160.109375), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))


class Kerman_Airport(Airport):
    id = 18
    name = "Kerman Airport"
    position = mapping.Point(454116.796875, 71096.085938)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Kerman_Airport, self).__init__()

        self.runways.append(Runway(340))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(452845.03125, 71861.46875), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(452796.15625, 71880.796875), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(452747.21875, 71899.859375), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(452697.21875, 71919.546875), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(452647.375, 71939.0625), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(452599.40625, 71957.890625), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(452549.625, 71977.5625), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(452499.53125, 71997.5625), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(452410.90625, 72019.0234375), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(454129, 71762.2734375), large=False, heli=True,
                airplanes=True, slot_name='12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(454102.4375, 71808.3046875), large=False, heli=True,
                airplanes=True, slot_name='11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(454075, 71853.2421875), large=False, heli=True,
                airplanes=True, slot_name='10', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(455167.46875, 71263.9609375), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(455180.1875, 71303.1796875), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(455192.4375, 71341.4296875), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(455205.03125, 71380.59375), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(455217.375, 71418.6171875), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(455373.78125, 71199.828125), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(455388.8125, 71234.1015625), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(455401.46875, 71262.46875), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(455416.5625, 71138.265625), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(455429.0625, 71166.2890625), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(455450.59375, 71219.03125), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(455467.5, 71256.2109375), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(455665.1875, 71779.9921875), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(456003.40625, 71559.8046875), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(456126.375, 71891.390625), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(456343.625, 72323.3984375), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(456061.96875, 72615.1484375), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(455588, 72518.3125), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(455236.5, 72309.78125), large=False, heli=True,
                airplanes=True, slot_name='31', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(455132.40625, 71994.5703125), large=False, heli=True,
                airplanes=True, slot_name='32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(454784.875, 71793.09375), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(454463.09375, 71766.375), large=False, heli=True,
                airplanes=True, slot_name='35', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(454315.03125, 72126.8984375), large=False, heli=True,
                airplanes=True, slot_name='34', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(454683.40625, 72354.203125), large=False, heli=True,
                airplanes=True, slot_name='33', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(455736.46875, 72163.484375), large=False, heli=True,
                airplanes=True, slot_name='41', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(455825.375, 72122.84375), large=False, heli=True,
                airplanes=True, slot_name='39', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(455927.53125, 72080.765625), large=False, heli=True,
                airplanes=True, slot_name='37', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(455914.125, 72179.9375), large=False, heli=True,
                airplanes=True, slot_name='38', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(455817.875, 72222.4375), large=False, heli=True,
                airplanes=True, slot_name='40', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(455720.1875, 72263.671875), large=False, heli=True,
                airplanes=True, slot_name='42', length=26.0, width=24.0, height=11.0, shelter=False))


class Shiraz_International_Airport(Airport):
    id = 19
    name = "Shiraz International Airport"
    position = mapping.Point(381101.03125, -351636.515625)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Shiraz_International_Airport, self).__init__()

        self.runways.append(Runway(290))
        self.runways.append(Runway(290))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(379150.96875, -350239.96875), large=False, heli=True,
                airplanes=True, slot_name='E06', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(379192.9375, -350325.09375), large=False, heli=True,
                airplanes=True, slot_name='E05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(379230.5625, -350399.84375), large=False, heli=True,
                airplanes=True, slot_name='E04', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(379269.71875, -350478.0625), large=False, heli=True,
                airplanes=True, slot_name='E03', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(379308.84375, -350555.25), large=False, heli=True,
                airplanes=True, slot_name='E02', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(379350.59375, -350638.46875), large=False, heli=True,
                airplanes=True, slot_name='E01', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(382003.59375, -352733.03125), large=False, heli=False,
                airplanes=True, slot_name='A30', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(380260.9375, -352729.1875), large=False, heli=False,
                airplanes=True, slot_name='D21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(380250.625, -352708.40625), large=False, heli=False,
                airplanes=True, slot_name='D22', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(380238.96875, -352690.21875), large=False, heli=False,
                airplanes=True, slot_name='D23', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(380201.82719463, -352611.86028146), large=False, heli=False,
                airplanes=True, slot_name='D24', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(380191.3125, -352591.375), large=False, heli=False,
                airplanes=True, slot_name='D25', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(380181.0625, -352572.0625), large=False, heli=False,
                airplanes=True, slot_name='D26', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(380415.13932905, -352788.73201312), large=False, heli=False,
                airplanes=True, slot_name='D20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(380404.59742911, -352769.31813804), large=False, heli=False,
                airplanes=True, slot_name='D19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(380394.83507018, -352749.62540198), large=False, heli=False,
                airplanes=True, slot_name='D18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(380487.58172408, -352717.10799074), large=False, heli=True,
                airplanes=True, slot_name='D17', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(380477.58172408, -352694.04549074), large=False, heli=True,
                airplanes=True, slot_name='D16', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(380455.95672408, -352648.32674074), large=False, heli=True,
                airplanes=True, slot_name='D15', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(380444.98797408, -352625.67049074), large=False, heli=True,
                airplanes=True, slot_name='D14', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(380424.04098026, -352582.83093395), large=False, heli=True,
                airplanes=True, slot_name='D13', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(380412.35348026, -352560.58093395), large=False, heli=True,
                airplanes=True, slot_name='D12', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(380390.50973026, -352516.14343395), large=False, heli=True,
                airplanes=True, slot_name='D11', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(380378.54098026, -352493.98718395), large=False, heli=True,
                airplanes=True, slot_name='D10', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(380308.3125, -352335.96875), large=False, heli=True,
                airplanes=True, slot_name='D27', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(380295.96875, -352311.40625), large=False, heli=True,
                airplanes=True, slot_name='D28', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(380284.28125, -352287.46875), large=False, heli=True,
                airplanes=True, slot_name='D29', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(380273.40625, -352262.75), large=False, heli=True,
                airplanes=True, slot_name='D30', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(380260.96875, -352239.125), large=False, heli=True,
                airplanes=True, slot_name='D31', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(380549.0625, -352686.75), large=False, heli=True,
                airplanes=True, slot_name='D09', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(380537.78125, -352664.21875), large=False, heli=True,
                airplanes=True, slot_name='D08', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(380526.71875, -352640.4375), large=False, heli=True,
                airplanes=True, slot_name='D07', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(380515.9375, -352618.9375), large=False, heli=True,
                airplanes=True, slot_name='D06', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(380505.125, -352596.1875), large=False, heli=True,
                airplanes=True, slot_name='D05', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(380484.96875, -352552.125), large=False, heli=True,
                airplanes=True, slot_name='D04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(380473.09375, -352529.96875), large=False, heli=True,
                airplanes=True, slot_name='D03', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(380451.46875, -352485.34375), large=False, heli=True,
                airplanes=True, slot_name='D02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(380440.15625, -352462.78125), large=False, heli=True,
                airplanes=True, slot_name='D01', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(380361.46875, -352309.1875), large=False, heli=True,
                airplanes=True, slot_name='D36', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(380348.53125, -352284.9375), large=False, heli=True,
                airplanes=True, slot_name='D35', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(380335.46875, -352261.65625), large=False, heli=True,
                airplanes=True, slot_name='D34', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(380322.1875, -352238.1875), large=False, heli=True,
                airplanes=True, slot_name='D33', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(380309.46875, -352214.59375), large=False, heli=True,
                airplanes=True, slot_name='D32', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(380581.77018863, -353791.45604661), large=False, heli=False,
                airplanes=True, slot_name='C20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(380564.30123334, -353758.33323049), large=False, heli=False,
                airplanes=True, slot_name='C21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(380895.53688551, -353719.44631128), large=False, heli=False,
                airplanes=True, slot_name='C18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(380878.50100247, -353685.99048323), large=False, heli=False,
                airplanes=True, slot_name='C19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(381258.71875, -354104.5), large=False, heli=True,
                airplanes=True, slot_name='C01', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(381247.28125, -354082), large=False, heli=True,
                airplanes=True, slot_name='C02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(381236, -354059.375), large=False, heli=True,
                airplanes=True, slot_name='C03', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(381225.0625, -354036.40625), large=False, heli=True,
                airplanes=True, slot_name='C04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(381213.875, -354014.125), large=False, heli=True,
                airplanes=True, slot_name='C05', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(381201.65625, -353992.71875), large=False, heli=True,
                airplanes=True, slot_name='C06', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(381191, -353970.3125), large=False, heli=True,
                airplanes=True, slot_name='C07', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(381179.5625, -353948.375), large=False, heli=True,
                airplanes=True, slot_name='C08', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(381169.34375, -353925.53125), large=False, heli=True,
                airplanes=True, slot_name='C09', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(381156.28125, -353903.46875), large=False, heli=True,
                airplanes=True, slot_name='C10', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(381063.21875, -353891.28125), large=False, heli=True,
                airplanes=True, slot_name='C11', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(381052.90625, -353870.6875), large=False, heli=True,
                airplanes=True, slot_name='C12', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(381042.65625, -353850.3125), large=False, heli=True,
                airplanes=True, slot_name='C13', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(381033.125, -353829.375), large=False, heli=True,
                airplanes=True, slot_name='C14', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(381023.09375, -353808.8125), large=False, heli=True,
                airplanes=True, slot_name='C15', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(381013.28125, -353787.59375), large=False, heli=True,
                airplanes=True, slot_name='C16', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(381001.1875, -353763.8125), large=False, heli=True,
                airplanes=True, slot_name='C17', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(381798.75, -353716.25), large=False, heli=True,
                airplanes=True, slot_name='05', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(381824.53125, -353706.5625), large=False, heli=True,
                airplanes=True, slot_name='04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(381850.28125, -353697.75), large=False, heli=True,
                airplanes=True, slot_name='03', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(381877.21875, -353680.375), large=False, heli=True,
                airplanes=True, slot_name='02', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(381902.6875, -353667.71875), large=False, heli=True,
                airplanes=True, slot_name='01', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(381077.21875, -350695.34375), large=False, heli=True,
                airplanes=True, slot_name='B21', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(381098.5625, -350739.15625), large=False, heli=True,
                airplanes=True, slot_name='B20', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(381120.3125, -350784.375), large=False, heli=True,
                airplanes=True, slot_name='B19', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(381141.6875, -350827.8125), large=False, heli=True,
                airplanes=True, slot_name='B18', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(381164.125, -350872.40625), large=False, heli=True,
                airplanes=True, slot_name='B17', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(381185.9375, -350915.5), large=False, heli=True,
                airplanes=True, slot_name='B16', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(381207.375, -350959.65625), large=False, heli=True,
                airplanes=True, slot_name='B15', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(381229.5625, -351004.71875), large=False, heli=True,
                airplanes=True, slot_name='B14', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(381252.84375, -351048.3125), large=False, heli=True,
                airplanes=True, slot_name='B13', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(381273.8125, -351090.90625), large=False, heli=True,
                airplanes=True, slot_name='B12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(381296.21875, -351135.96875), large=False, heli=True,
                airplanes=True, slot_name='B11', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(381389.6875, -351360.84375), large=False, heli=True,
                airplanes=True, slot_name='B10', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(381412.71875, -351404.71875), large=False, heli=True,
                airplanes=True, slot_name='B09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(381433.96875, -351448.4375), large=False, heli=True,
                airplanes=True, slot_name='B08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(381455.96875, -351493.3125), large=False, heli=True,
                airplanes=True, slot_name='B07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(381477.78125, -351537.5), large=False, heli=True,
                airplanes=True, slot_name='B06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(381500.53125, -351581.75), large=False, heli=True,
                airplanes=True, slot_name='B05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(381522.21875, -351625.4375), large=False, heli=True,
                airplanes=True, slot_name='B04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(381544.5625, -351669.71875), large=False, heli=True,
                airplanes=True, slot_name='B03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(381561.8125, -351816.375), large=False, heli=True,
                airplanes=True, slot_name='B01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(381593.625, -351800.3125), large=False, heli=True,
                airplanes=True, slot_name='B02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(381994.34375, -352715), large=False, heli=False,
                airplanes=True, slot_name='A29', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(381985.46875, -352697.375), large=False, heli=False,
                airplanes=True, slot_name='A28', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(381976.34375, -352678.9375), large=False, heli=False,
                airplanes=True, slot_name='A27', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(381965, -352656.53125), large=False, heli=False,
                airplanes=True, slot_name='A26', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(382067.9375, -352700.625), large=False, heli=False,
                airplanes=True, slot_name='A20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(382058.59375, -352682.53125), large=False, heli=False,
                airplanes=True, slot_name='A21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(382049.59375, -352665.0625), large=False, heli=False,
                airplanes=True, slot_name='A22', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(382040.65625, -352646.59375), large=False, heli=False,
                airplanes=True, slot_name='A23', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(382029.25, -352624.21875), large=False, heli=False,
                airplanes=True, slot_name='A24', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(382005.71875, -352582.375), large=False, heli=True,
                airplanes=True, slot_name='A25', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(382110.6875, -352924.78125), large=False, heli=False,
                airplanes=True, slot_name='A17', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(382097.34375, -352897.59375), large=False, heli=False,
                airplanes=True, slot_name='A18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(382084.65625, -352870.96875), large=False, heli=False,
                airplanes=True, slot_name='A19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(382177.875, -352924.25), large=False, heli=False,
                airplanes=True, slot_name='A13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(382164.34375, -352897.6875), large=False, heli=False,
                airplanes=True, slot_name='A14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(382151.375, -352870.1875), large=False, heli=False,
                airplanes=True, slot_name='A15', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(382138.59375, -352843.625), large=False, heli=False,
                airplanes=True, slot_name='A16', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(382295.3125, -353233.6875), large=False, heli=True,
                airplanes=True, slot_name='A11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(382315.8125, -353274.75), large=False, heli=True,
                airplanes=True, slot_name='A10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(382336.15625, -353315.84375), large=False, heli=True,
                airplanes=True, slot_name='A09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(382354.71875, -353359.0625), large=False, heli=True,
                airplanes=True, slot_name='A08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(382423.78125, -353324.4375), large=False, heli=True,
                airplanes=True, slot_name='A03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(382405.25, -353281.0625), large=False, heli=True,
                airplanes=True, slot_name='A04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(382384.90625, -353240.03125), large=False, heli=True,
                airplanes=True, slot_name='A05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(382364.375, -353198.9375), large=False, heli=True,
                airplanes=True, slot_name='A06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(382344.65625, -353156.96875), large=False, heli=True,
                airplanes=True, slot_name='A07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(382459.46875, -353469.59375), large=False, heli=True,
                airplanes=True, slot_name='A02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(382450.78125, -353635.3125), large=False, heli=True,
                airplanes=True, slot_name='A01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(382274.09375, -353192.0625), large=False, heli=True,
                airplanes=True, slot_name='A12', length=26.0, width=24.0, height=11.0, shelter=False))


class Sas_Al_Nakheel_Airport(Airport):
    id = 20
    name = "Sas Al Nakheel Airport"
    position = mapping.Point(-189610.289063, -175974.148438)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Sas_Al_Nakheel_Airport, self).__init__()

        self.runways.append(Runway(160))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-189181.953125, -176242.125), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-190351.625, -176155.96875), large=False, heli=True,
                airplanes=False, slot_name='82', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-190237.53125, -176192.25), large=False, heli=True,
                airplanes=False, slot_name='80', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-190580.828125, -175862.5), large=False, heli=True,
                airplanes=False, slot_name='87', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-190592.75, -175899.171875), large=False, heli=True,
                airplanes=False, slot_name='86', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-190604.53125, -175936.34375), large=False, heli=True,
                airplanes=False, slot_name='85', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-190428.21875, -176131.921875), large=False, heli=True,
                airplanes=False, slot_name='84', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-190390.6875, -176143.9375), large=False, heli=True,
                airplanes=False, slot_name='83', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-190275.46875, -176180.125), large=False, heli=True,
                airplanes=False, slot_name='81', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-190088.1853878, -176007.48578314), large=False, heli=True,
                airplanes=False, slot_name='64', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-190113.09046656, -175999.73840989), large=False, heli=True,
                airplanes=False, slot_name='63', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-190137.97719882, -175992.15599547), large=False, heli=True,
                airplanes=False, slot_name='62', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-190162.75, -175984.40625), large=False, heli=True,
                airplanes=False, slot_name='61', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-190187.59269146, -175976.39365837), large=False, heli=True,
                airplanes=False, slot_name='60', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-190245.67793127, -175958.94569429), large=False, heli=True,
                airplanes=False, slot_name='59', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-190270.52761063, -175951.1896122), large=False, heli=True,
                airplanes=False, slot_name='58', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-190295.27638404, -175943.24241657), large=False, heli=True,
                airplanes=False, slot_name='57', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-190320.06373551, -175935.54035011), large=False, heli=True,
                airplanes=False, slot_name='56', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-190344.98116664, -175927.81719097), large=False, heli=True,
                airplanes=False, slot_name='55', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-190403.75158681, -175910.51717708), large=False, heli=True,
                airplanes=False, slot_name='54', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-189334.203125, -176193.09375), large=False, heli=True,
                airplanes=False, slot_name='28', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-190453.21875, -175894.84375), large=False, heli=True,
                airplanes=False, slot_name='52', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-190478, -175887.265625), large=False, heli=True,
                airplanes=False, slot_name='51', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-190502.796875, -175879.265625), large=False, heli=True,
                airplanes=False, slot_name='50', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-190531.46875, -175968.09375), large=False, heli=True,
                airplanes=False, slot_name='79', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-190506.8125, -175976.234375), large=False, heli=True,
                airplanes=False, slot_name='78', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-190481.9375, -175983.71875), large=False, heli=True,
                airplanes=False, slot_name='77', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-190457.125, -175991.28125), large=False, heli=True,
                airplanes=False, slot_name='76', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-190432.125, -175999.03125), large=False, heli=True,
                airplanes=False, slot_name='75', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-190374.0625, -176018.328125), large=False, heli=True,
                airplanes=False, slot_name='74', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-190349.078125, -176026.078125), large=False, heli=True,
                airplanes=False, slot_name='73', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-190324.46875, -176033.9375), large=False, heli=True,
                airplanes=False, slot_name='72', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-190299.59375, -176041.84375), large=False, heli=True,
                airplanes=False, slot_name='71', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-190274.765625, -176049.640625), large=False, heli=True,
                airplanes=False, slot_name='70', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-190217.625, -176070.21875), large=False, heli=True,
                airplanes=False, slot_name='69', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-190192.75, -176077.859375), large=False, heli=True,
                airplanes=False, slot_name='68', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-190167.96875, -176085.53125), large=False, heli=True,
                airplanes=False, slot_name='67', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-190143.15625, -176093.140625), large=False, heli=True,
                airplanes=False, slot_name='66', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-190117.9375, -176100.953125), large=False, heli=True,
                airplanes=False, slot_name='65', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-190116.625, -175513.8125), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-190128.765625, -175551.5), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-190140.765625, -175589.46875), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-190152.90625, -175628.5), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-190364.5625, -175517.703125), large=False, heli=True,
                airplanes=False, slot_name='47', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-190352.453125, -175479.875), large=False, heli=True,
                airplanes=False, slot_name='48', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-190341.1875, -175441.890625), large=False, heli=True,
                airplanes=False, slot_name='49', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-190291.84576744, -175457.57535611), large=False, heli=True,
                airplanes=False, slot_name='46', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-190304.125, -175495.40625), large=False, heli=True,
                airplanes=False, slot_name='45', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-190316.140625, -175533.078125), large=False, heli=True,
                airplanes=False, slot_name='44', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-190229.75, -175477.53125), large=False, heli=True,
                airplanes=False, slot_name='43', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-190241.765625, -175515.359375), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-190254.09375, -175553.109375), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-190177.65625, -175494.078125), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-190189.84375, -175531.90625), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-190202.234375, -175569.578125), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-190017.515625, -175698.40625), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-189989.71875, -175707.53125), large=False, heli=True,
                airplanes=False, slot_name='32', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-189960.625, -175716.953125), large=False, heli=True,
                airplanes=False, slot_name='31', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-189931.859375, -175725.984375), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-189903.546875, -175735.09375), large=False, heli=True,
                airplanes=False, slot_name='29', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-189091.29208999, -176227.8293457), large=False, heli=True,
                airplanes=True, slot_name='11', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-189055.1358772, -176239.3030044), large=False, heli=True,
                airplanes=True, slot_name='10', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-188910, -176281.6875), large=False, heli=True,
                airplanes=True, slot_name='09', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-188873.14698574, -176293.24073574), large=False, heli=True,
                airplanes=True, slot_name='08', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-188837.0625, -176304.9375), large=False, heli=True,
                airplanes=True, slot_name='07', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-188801.9375, -176316.25), large=False, heli=True,
                airplanes=True, slot_name='06', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-188765.671875, -176327.734375), large=False, heli=True,
                airplanes=True, slot_name='05', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-188715.578125, -176343.67665947), large=False, heli=True,
                airplanes=True, slot_name='04', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-189332.8125, -176261.328125), large=False, heli=True,
                airplanes=False, slot_name='27', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-189289.125, -176275.3125), large=False, heli=True,
                airplanes=False, slot_name='26', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-189245.53125, -176289.203125), large=False, heli=True,
                airplanes=False, slot_name='25', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-189201.734375, -176303.40625), large=False, heli=True,
                airplanes=False, slot_name='24', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-189110.78125, -176288.9375), large=False, heli=True,
                airplanes=True, slot_name='22', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-189074.8125, -176300.65625), large=False, heli=True,
                airplanes=True, slot_name='21', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-189038.25, -176312.25), large=False, heli=True,
                airplanes=True, slot_name='20', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-189002.859375, -176323.828125), large=False, heli=True,
                airplanes=True, slot_name='19', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-188967.40625, -176335.140625), large=False, heli=True,
                airplanes=True, slot_name='18', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-188930.78125, -176346.8125), large=False, heli=True,
                airplanes=True, slot_name='17', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-188894.171875, -176358.5), large=False, heli=True,
                airplanes=True, slot_name='16', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-188858.015625, -176370.125), large=False, heli=True,
                airplanes=True, slot_name='15', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-188822.96875, -176381.4375), large=False, heli=True,
                airplanes=True, slot_name='14', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-188786.703125, -176393.09375), large=False, heli=True,
                airplanes=True, slot_name='13', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-188736.375, -176409.0625), large=False, heli=True,
                airplanes=True, slot_name='12', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-188678.19481543, -176481.29033451), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-188639.64833848, -176493.55102795), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-188601.55795467, -176506.33977556), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-190428.390625, -175902.5625), large=False, heli=True,
                airplanes=False, slot_name='53', length=30.096436, width=23.0, height=10.0, shelter=False))


class Bandar_e_Jask_airfield(Airport):
    id = 21
    name = "Bandar-e-Jask airfield"
    position = mapping.Point(-57247.5, 156196.507813)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Bandar_e_Jask_airfield, self).__init__()

        self.runways.append(Runway(60))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-57597.375, 154792.71875), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-57606.103779506, 154713.31722941), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-57655.1328125, 154757.625), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-57726.48676071, 154987.23467391), large=False, heli=True,
                airplanes=False, slot_name='04', length=42.0, width=34.0, height=14.0, shelter=False))


class Abu_Dhabi_International_Airport(Airport):
    id = 22
    name = "Abu Dhabi International Airport"
    position = mapping.Point(-188457.460938, -162030.984375)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Abu_Dhabi_International_Airport, self).__init__()

        self.runways.append(Runway(130))
        self.runways.append(Runway(310))
        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-189270.15625, -164756.421875), large=False, heli=True,
                airplanes=True, slot_name='16', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-189553.984375, -164405.828125), large=False, heli=True,
                airplanes=True, slot_name='21', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-190028.71875, -163968.3125), large=False, heli=True,
                airplanes=True, slot_name='44', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-189969.578125, -164042.484375), large=False, heli=True,
                airplanes=True, slot_name='42', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-190059.75, -163929.953125), large=False, heli=True,
                airplanes=True, slot_name='45', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-190090.21875, -163894.1875), large=False, heli=True,
                airplanes=True, slot_name='46', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-190126.9375, -163847.5625), large=False, heli=True,
                airplanes=True, slot_name='47', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-190156.15625, -163809.03125), large=False, heli=True,
                airplanes=True, slot_name='48', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-190184.4375, -163773.21875), large=False, heli=True,
                airplanes=True, slot_name='49', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-190213.90625, -163737.34375), large=False, heli=True,
                airplanes=True, slot_name='50', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-190242.953125, -163701.3125), large=False, heli=True,
                airplanes=True, slot_name='51', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-189991.6875, -163913.046875), large=False, heli=False,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-190020.03125, -163877.015625), large=False, heli=False,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-190048.875, -163840.828125), large=False, heli=False,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-190078.0625, -163805.5625), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-190107.125, -163769.203125), large=False, heli=False,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-190135.96875, -163732.671875), large=False, heli=False,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-190166.21875, -163697.640625), large=False, heli=False,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-190194.21875, -163661.59375), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-190222.125, -163625.734375), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-190756.078125, -163434.453125), large=False, heli=True,
                airplanes=True, slot_name='54', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-190803, -163374.84375), large=False, heli=True,
                airplanes=True, slot_name='55', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-190849.109375, -163317.96875), large=False, heli=True,
                airplanes=True, slot_name='56', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-191192.25, -162930.28125), large=False, heli=True,
                airplanes=True, slot_name='61', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-191141.5, -162792), large=False, heli=True,
                airplanes=True, slot_name='63', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-191165.953125, -162724.109375), large=False, heli=True,
                airplanes=True, slot_name='64', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-191644.25, -162257.96875), large=False, heli=True,
                airplanes=True, slot_name='83', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-191687.15625, -162204.671875), large=False, heli=True,
                airplanes=True, slot_name='84', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-191730.28125, -162151.609375), large=False, heli=True,
                airplanes=True, slot_name='85', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-191773.09375, -162097.3125), large=False, heli=True,
                airplanes=True, slot_name='86', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-191816.28125, -162043.0625), large=False, heli=True,
                airplanes=True, slot_name='87', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-191862.140625, -161986.90625), large=False, heli=True,
                airplanes=True, slot_name='88', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-191907.625, -161930.546875), large=False, heli=True,
                airplanes=True, slot_name='89', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-191952.265625, -161874.421875), large=False, heli=True,
                airplanes=True, slot_name='90', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-191997.578125, -161818.796875), large=False, heli=True,
                airplanes=True, slot_name='91', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-192042.6875, -161762.703125), large=False, heli=True,
                airplanes=True, slot_name='92', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-192090.125, -161703.84375), large=False, heli=True,
                airplanes=True, slot_name='93', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-191250.6875, -162332.625), large=False, heli=True,
                airplanes=True, slot_name='74', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-191300.0625, -162271.28125), large=False, heli=True,
                airplanes=True, slot_name='75', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-191347.8125, -162210.3125), large=False, heli=True,
                airplanes=True, slot_name='76', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-191498.375, -162025.375), large=False, heli=True,
                airplanes=True, slot_name='77', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-191545.984375, -161964.53125), large=False, heli=True,
                airplanes=True, slot_name='78', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-191594.34375, -161905.890625), large=False, heli=True,
                airplanes=True, slot_name='79', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-191641.796875, -161845.71875), large=False, heli=True,
                airplanes=True, slot_name='80', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-191690.96875, -161784.5625), large=False, heli=True,
                airplanes=True, slot_name='81', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-191739.515625, -161723.71875), large=False, heli=True,
                airplanes=True, slot_name='82', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-192546.078125, -161421.6875), large=False, heli=True,
                airplanes=True, slot_name='111', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-192514.5625, -161396.625), large=False, heli=True,
                airplanes=True, slot_name='110', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-192483.140625, -161371.265625), large=False, heli=True,
                airplanes=True, slot_name='109', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-192451.515625, -161346.140625), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-192420.171875, -161321.59375), large=False, heli=True,
                airplanes=True, slot_name='107', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-192378.9375, -161525.15625), large=False, heli=True,
                airplanes=False, slot_name='102', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-192347.421875, -161499.25), large=False, heli=True,
                airplanes=False, slot_name='101', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-192315.984375, -161473.875), large=False, heli=True,
                airplanes=False, slot_name='100', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-192284.34375, -161447.71875), large=False, heli=True,
                airplanes=False, slot_name='99', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-192374.328125, -161464.8125), large=False, heli=True,
                airplanes=False, slot_name='105', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-192406.484375, -161490.8125), large=False, heli=True,
                airplanes=False, slot_name='106', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-192342.734375, -161439.125), large=False, heli=True,
                airplanes=False, slot_name='104', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-192310.328125, -161414.53125), large=False, heli=True,
                airplanes=False, slot_name='103', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-192313.265625, -161586.21875), large=False, heli=True,
                airplanes=False, slot_name='96', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-192278.9375, -161559.359375), large=False, heli=True,
                airplanes=False, slot_name='95', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-192244.5, -161531.8125), large=False, heli=True,
                airplanes=False, slot_name='94', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-192353.5625, -161623.140625), large=False, heli=True,
                airplanes=False, slot_name='97', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-192403.90625, -161615.5), large=False, heli=True,
                airplanes=False, slot_name='98', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-192533.828125, -161660), large=False, heli=False,
                airplanes=True, slot_name='113', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-192558.9375, -161628.328125), large=False, heli=False,
                airplanes=True, slot_name='114', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-192510.5, -161692.375), large=False, heli=False,
                airplanes=True, slot_name='112', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-191145.75, -161102.171875), large=False, heli=True,
                airplanes=True, slot_name='117', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-191194.890625, -161042.671875), large=False, heli=True,
                airplanes=True, slot_name='118', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-191243.125, -160980.453125), large=False, heli=True,
                airplanes=True, slot_name='119', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-191298.171875, -160913.15625), large=False, heli=True,
                airplanes=True, slot_name='120', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-191348.234375, -160853.921875), large=False, heli=True,
                airplanes=True, slot_name='121', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-191395.015625, -160793.5), large=False, heli=True,
                airplanes=True, slot_name='122', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-191443.640625, -160733.875), large=False, heli=True,
                airplanes=True, slot_name='123', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-191095.65625, -161161.390625), large=False, heli=True,
                airplanes=True, slot_name='116', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(-191039.359375, -161230.515625), large=False, heli=True,
                airplanes=True, slot_name='115', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(-191491.53125, -160674.25), large=False, heli=True,
                airplanes=True, slot_name='124', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(-191539.09375, -160612.890625), large=False, heli=True,
                airplanes=True, slot_name='125', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(-191587.6875, -160552.421875), large=False, heli=True,
                airplanes=True, slot_name='126', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(-191605.546875, -162665.640625), large=False, heli=False,
                airplanes=True, slot_name='69', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(-191569.6875, -162637.125), large=False, heli=False,
                airplanes=True, slot_name='70', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(-191515.46875, -162596.9375), large=False, heli=True,
                airplanes=True, slot_name='71', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(-191443.921875, -162539.59375), large=False, heli=True,
                airplanes=True, slot_name='72', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(-191386.09375, -162493.15625), large=False, heli=True,
                airplanes=True, slot_name='73', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(-189013.171875, -160320.328125), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(-189047.75, -160275.609375), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(-189080.703125, -160236.59375), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(-189114.5, -160192.9375), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(-189147.375, -160153.65625), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(-189180.375, -160110.296875), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(-188981.84375, -160360.03125), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(-188946.640625, -160403.234375), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(-189078.75, -160457.5), large=False, heli=True,
                airplanes=True, slot_name='09', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(-189123.453125, -160400.03125), large=False, heli=True,
                airplanes=True, slot_name='10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(-189170.640625, -160342.453125), large=False, heli=True,
                airplanes=True, slot_name='11', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(-189216.875, -160285.640625), large=False, heli=True,
                airplanes=True, slot_name='12', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(-189265.03125, -160227.265625), large=False, heli=True,
                airplanes=True, slot_name='13', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(-189405.5, -160053.15625), large=False, heli=True,
                airplanes=True, slot_name='14', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(-189452, -159995.8125), large=False, heli=True,
                airplanes=True, slot_name='15', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(-189330.140625, -164681.1875), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(-189391.6875, -164606.0625), large=False, heli=True,
                airplanes=True, slot_name='18', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(-189549.3125, -164732.5625), large=False, heli=True,
                airplanes=True, slot_name='25', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(-189598.65625, -164671.125), large=False, heli=True,
                airplanes=True, slot_name='26', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(-189648.53125, -164609.015625), large=False, heli=True,
                airplanes=True, slot_name='27', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(-189695.65625, -164550.3125), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(-189446.265625, -164891.609375), large=False, heli=True,
                airplanes=True, slot_name='22', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(-189472.96875, -164858.359375), large=False, heli=True,
                airplanes=True, slot_name='23', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(-189499.15625, -164824.9375), large=False, heli=True,
                airplanes=True, slot_name='24', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(-189729.234375, -164477.8125), large=False, heli=True,
                airplanes=True, slot_name='29', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(-189756.53125, -164443.9375), large=False, heli=True,
                airplanes=True, slot_name='30', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(-189786.53125, -164406.34375), large=False, heli=True,
                airplanes=True, slot_name='31', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(-189814.84375, -164371.109375), large=False, heli=True,
                airplanes=True, slot_name='32', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(-190697.140625, -163507.28125), large=False, heli=True,
                airplanes=True, slot_name='53', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(-190647.015625, -163568.640625), large=False, heli=True,
                airplanes=True, slot_name='52', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(-190895.421875, -163258.921875), large=False, heli=True,
                airplanes=True, slot_name='57', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(-190942, -163203.140625), large=False, heli=True,
                airplanes=True, slot_name='58', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(-190988.3125, -163139.640625), large=False, heli=True,
                airplanes=True, slot_name='59', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(-191045.78125, -163071.734375), large=False, heli=True,
                airplanes=True, slot_name='60', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(-191146.703125, -162870.953125), large=False, heli=True,
                airplanes=True, slot_name='62', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(-189445.71875, -164537.828125), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=122, position=mapping.Point(-189497.921875, -164471.671875), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=123, position=mapping.Point(-191224.53125, -162684.75), large=False, heli=True,
                airplanes=True, slot_name='65', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=124, position=mapping.Point(-191299.5, -162672.859375), large=False, heli=True,
                airplanes=True, slot_name='66', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=125, position=mapping.Point(-191361.09375, -162705.84375), large=False, heli=True,
                airplanes=True, slot_name='67', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=126, position=mapping.Point(-191404.71875, -162755.46875), large=False, heli=True,
                airplanes=True, slot_name='68', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=129, position=mapping.Point(-189999.84375, -164004.375), large=False, heli=True,
                airplanes=True, slot_name='43', length=43.057953, width=40.0, height=None, shelter=False))


class Al_Bateen_Airport(Airport):
    id = 23
    name = "Al-Bateen Airport"
    position = mapping.Point(-190946.55263, -181928.271658)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Al_Bateen_Airport, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-190337.921875, -183074.21875), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-190361.078125, -183092.4375), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-190383.390625, -183110.625), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-190406.734375, -183129.09375), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-190436.390625, -183092.3125), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-190413.234375, -183073.96875), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-190389.828125, -183056.796875), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-190366.5, -183038.359375), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-190398.09375, -182998.921875), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-190421.71875, -183017.1875), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-190444.78125, -183034.78125), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-190467.734375, -183053.5), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-190475.375, -182996.953125), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-190452.40625, -182978.984375), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-190428.890625, -182960.625), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-190459.390625, -182922.609375), large=False, heli=False,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-190482.6875, -182941.3125), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-190505.5625, -182959.875), large=False, heli=False,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-190131.40625, -183377.5), large=False, heli=True,
                airplanes=True, slot_name='05', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-190165.71875, -183332.390625), large=False, heli=True,
                airplanes=True, slot_name='06', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-190200.171875, -183290.140625), large=False, heli=True,
                airplanes=True, slot_name='08', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-190062.71875, -183400.953125), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-190057.109375, -183435.625), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-190039.71875, -183465.078125), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-190016.078125, -183489.28125), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-190174.59375, -183304.921875), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-190207.578125, -183259.40625), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-190223.90625, -183238.875), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-190670.984375, -182854.59375), large=False, heli=True,
                airplanes=True, slot_name='32', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-190640.8125, -182828.671875), large=False, heli=True,
                airplanes=True, slot_name='31', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-190608.25, -182804.78125), large=False, heli=True,
                airplanes=True, slot_name='30', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-190575.92934315, -182779.76451759), large=False, heli=False,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-190747.78125, -182743.203125), large=False, heli=True,
                airplanes=True, slot_name='35', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-190725.09375, -182724.953125), large=False, heli=True,
                airplanes=True, slot_name='34', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-190700.96875, -182704.703125), large=False, heli=True,
                airplanes=True, slot_name='33', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-190742.859375, -182650.34375), large=False, heli=True,
                airplanes=True, slot_name='36', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-190766.3125, -182667.421875), large=False, heli=True,
                airplanes=True, slot_name='37', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-190789.484375, -182685.6875), large=False, heli=True,
                airplanes=True, slot_name='38', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-190837.25, -182579.390625), large=False, heli=True,
                airplanes=True, slot_name='40', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-190791.9375, -182546.375), large=False, heli=True,
                airplanes=True, slot_name='39', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-191042.015625, -182218.375), large=False, heli=True,
                airplanes=True, slot_name='41', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-191079, -182172.953125), large=False, heli=True,
                airplanes=True, slot_name='42', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-191121, -182120.625), large=False, heli=True,
                airplanes=True, slot_name='43', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-191161.171875, -182070.84375), large=False, heli=True,
                airplanes=True, slot_name='44', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-191207.171875, -182014.765625), large=False, heli=True,
                airplanes=True, slot_name='45', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-191439.671875, -181729.609375), large=False, heli=True,
                airplanes=True, slot_name='46', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-191487.71875, -181670.109375), large=False, heli=True,
                airplanes=True, slot_name='47', length=25.0, width=20.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-191535.828125, -181611.109375), large=False, heli=True,
                airplanes=True, slot_name='48', length=25.0, width=20.0, height=11.0, shelter=False))


class Kish_International_Airport(Airport):
    id = 24
    name = "Kish International Airport"
    position = mapping.Point(42784.291016, -225094.046875)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Kish_International_Airport, self).__init__()

        self.runways.append(Runway(100))
        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(43106.234375, -226229.578125), large=False, heli=True,
                airplanes=True, slot_name='01', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(43101.22265625, -226184.96875), large=False, heli=True,
                airplanes=True, slot_name='02', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(43096.3125, -226139.984375), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(43091.1015625, -226095.40625), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(43086.33203125, -226050.8125), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(43080.83984375, -226006.0625), large=False, heli=True,
                airplanes=True, slot_name='06', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(43075.6953125, -225961.328125), large=False, heli=True,
                airplanes=True, slot_name='07', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(43070.61328125, -225916.5625), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(43026.171875, -225817), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(43020.77734375, -225779.890625), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(43017.2890625, -225742.4375), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(43013.1953125, -225705.1875), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(43008.1953125, -225668.0625), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(43004.56640625, -225630.65625), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(43105.91796875, -225790.203125), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(43101.359375, -225752.953125), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(43097.7578125, -225715.75), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(43093.6328125, -225678.390625), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(43089.8125, -225641), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(43084.69921875, -225603.78125), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(43222.8671875, -225493.75), large=False, heli=True,
                airplanes=True, slot_name='21', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(43218.15234375, -225449.34375), large=False, heli=True,
                airplanes=True, slot_name='22', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(43213.3359375, -225405.15625), large=False, heli=True,
                airplanes=True, slot_name='23', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(43208.7734375, -225360.8125), large=False, heli=True,
                airplanes=True, slot_name='24', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(43203.98828125, -225316.53125), large=False, heli=True,
                airplanes=True, slot_name='25', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(43198.9765625, -225272.484375), large=False, heli=True,
                airplanes=True, slot_name='26', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(43194.1953125, -225228.1875), large=False, heli=True,
                airplanes=True, slot_name='27', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(43189.21875, -225184.046875), large=False, heli=True,
                airplanes=True, slot_name='28', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(43184.53515625, -225139.65625), large=False, heli=True,
                airplanes=True, slot_name='29', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(43179.9765625, -225095.4375), large=False, heli=True,
                airplanes=True, slot_name='30', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(43091.96484375, -225507.84375), large=False, heli=True,
                airplanes=True, slot_name='31', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(43086.97265625, -225463.71875), large=False, heli=True,
                airplanes=True, slot_name='32', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(43082.1953125, -225419.3125), large=False, heli=True,
                airplanes=True, slot_name='33', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(43077.50390625, -225375.125), large=False, heli=True,
                airplanes=True, slot_name='34', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(43072.7265625, -225330.78125), large=False, heli=True,
                airplanes=True, slot_name='35', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(43067.87890625, -225286.625), large=False, heli=True,
                airplanes=True, slot_name='36', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(43063.1484375, -225242.40625), large=False, heli=True,
                airplanes=True, slot_name='37', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(43058.30859375, -225198.203125), large=False, heli=True,
                airplanes=True, slot_name='38', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(43053.6171875, -225154.03125), large=False, heli=True,
                airplanes=True, slot_name='39', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(43048.7109375, -225109.765625), large=False, heli=True,
                airplanes=True, slot_name='40', length=41.648293, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(41891.80859375, -223559.90625), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(41911.8515625, -223557.640625), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(41926.45703125, -223639.8125), large=False, heli=False,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(41891.3203125, -223643.953125), large=False, heli=False,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(41914.4765625, -223730.171875), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(41877.234375, -223734.875), large=False, heli=False,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=11.0, shelter=False))


class Al_Ain_International_Airport(Airport):
    id = 25
    name = "Al Ain International Airport"
    position = mapping.Point(-211058.15625, -65421.177734)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Al_Ain_International_Airport, self).__init__()

        self.runways.append(Runway(190))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-209643.34375, -64532.62890625), large=False, heli=False,
                airplanes=True, slot_name='6', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-209640.078125, -64554.75390625), large=False, heli=False,
                airplanes=True, slot_name='5', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-209637.171875, -64575.58984375), large=False, heli=False,
                airplanes=True, slot_name='4', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-209673.859375, -64668.51953125), large=False, heli=False,
                airplanes=True, slot_name='7', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-209677.546875, -64642.9140625), large=False, heli=False,
                airplanes=True, slot_name='8', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-209749.015625, -64641.5625), large=False, heli=False,
                airplanes=True, slot_name='9', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-209753.03125, -64612.109375), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-209849.671875, -64641.27734375), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-210208.734375, -64655.36328125), large=False, heli=True,
                airplanes=True, slot_name='13', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-210265.65625, -64664.7109375), large=False, heli=True,
                airplanes=True, slot_name='14', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-210331.25, -64673.96875), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-210550.6875, -64905.04296875), large=False, heli=True,
                airplanes=False, slot_name='16', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-210910.25, -64758.93359375), large=False, heli=True,
                airplanes=True, slot_name='17', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-211049.890625, -64778.53515625), large=False, heli=True,
                airplanes=True, slot_name='19', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-211119.875, -64788.12890625), large=False, heli=True,
                airplanes=True, slot_name='20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-211181.15625, -64796.07421875), large=False, heli=True,
                airplanes=True, slot_name='21', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-211250.1875, -64805.484375), large=False, heli=True,
                airplanes=True, slot_name='22', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-210976.78125, -64796.09765625), large=False, heli=True,
                airplanes=True, slot_name='18', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-211392.859375, -64914.515625), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-211400.34375, -64861.3828125), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-211409.25, -64916.7734375), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-211425.71875, -64918.84375), large=False, heli=False,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-211442.40625, -64920.9921875), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-211508.125, -64931.43359375), large=False, heli=False,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-211541.09375, -64935.83984375), large=False, heli=False,
                airplanes=True, slot_name='30', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-211574.6875, -64939.90625), large=False, heli=False,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-211607.5, -64943.87890625), large=False, heli=False,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-211631.953125, -64887.1875), large=False, heli=False,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-211640.53125, -64948.0390625), large=False, heli=False,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-211663.3125, -64905.8046875), large=False, heli=False,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-211673.640625, -64953.83984375), large=False, heli=False,
                airplanes=True, slot_name='38', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-211696.578125, -64910.48828125), large=False, heli=False,
                airplanes=True, slot_name='39', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-211706.703125, -64958.64453125), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-211729.125, -64915.28515625), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-211739.40625, -64964.17578125), large=False, heli=False,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-211762.359375, -64919.96484375), large=False, heli=False,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-211772.828125, -64969.66015625), large=False, heli=False,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-211794.984375, -64925.015625), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-211805.515625, -64974.86328125), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-211828, -64929.7265625), large=False, heli=False,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-212313.640625, -64950.05859375), large=False, heli=True,
                airplanes=False, slot_name='56', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-212371.703125, -64958.7421875), large=False, heli=True,
                airplanes=False, slot_name='57', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-212429.421875, -64967.33203125), large=False, heli=True,
                airplanes=False, slot_name='58', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-212487.125, -64975.38671875), large=False, heli=True,
                airplanes=False, slot_name='59', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-212544.875, -64983.50390625), large=False, heli=True,
                airplanes=False, slot_name='60', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-213709.90625, -65109.68359375), large=False, heli=True,
                airplanes=True, slot_name='73', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-213721.4375, -65029.53125), large=False, heli=True,
                airplanes=True, slot_name='74', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-213609.84375, -65095.8984375), large=False, heli=True,
                airplanes=True, slot_name='71', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-213621.140625, -65015.6328125), large=False, heli=True,
                airplanes=True, slot_name='72', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-213511.234375, -65082.09375), large=False, heli=True,
                airplanes=True, slot_name='69', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-213522.71875, -65001.88671875), large=False, heli=True,
                airplanes=True, slot_name='70', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-213411.734375, -65068.02734375), large=False, heli=True,
                airplanes=True, slot_name='67', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-213423.15625, -64987.86328125), large=False, heli=True,
                airplanes=True, slot_name='68', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-213313.9375, -65053.21875), large=False, heli=True,
                airplanes=True, slot_name='65', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-213325.328125, -64973.01953125), large=False, heli=True,
                airplanes=True, slot_name='66', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-213016.28125, -65012.85546875), large=False, heli=True,
                airplanes=True, slot_name='61', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-213027.40625, -64932.671875), large=False, heli=True,
                airplanes=True, slot_name='62', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-213214.015625, -65039.82421875), large=False, heli=True,
                airplanes=True, slot_name='63', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-213225.375, -64959.69140625), large=False, heli=True,
                airplanes=True, slot_name='64', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-211450.03125, -64868.05859375), large=False, heli=False,
                airplanes=True, slot_name='28', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-211599, -64882.8515625), large=False, heli=False,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-211565.8125, -64878.453125), large=False, heli=False,
                airplanes=True, slot_name='31', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-209821.890625, -64621.9765625), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-209311.625, -64852.9609375), large=False, heli=False,
                airplanes=True, slot_name='2', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-209337.5625, -64856.515625), large=False, heli=False,
                airplanes=True, slot_name='3', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-209286.625, -64854.171875), large=False, heli=False,
                airplanes=True, slot_name='1', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-211992.6875, -64896.4921875), large=False, heli=False,
                airplanes=True, slot_name='48', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-212025.8125, -64901.39453125), large=False, heli=False,
                airplanes=True, slot_name='49', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-212058.234375, -64906.9921875), large=False, heli=False,
                airplanes=True, slot_name='50', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-212091.59375, -64910.05078125), large=False, heli=False,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-212124.90625, -64915.0390625), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-212157.578125, -64919.45703125), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-212190.875, -64922.91796875), large=False, heli=False,
                airplanes=True, slot_name='54', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(-212223.609375, -64926.93359375), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.5, width=14.5, height=11.0, shelter=False))


class Lavan_Island_Airport(Airport):
    id = 26
    name = "Lavan Island Airport"
    position = mapping.Point(75789.741687, -286801.46313)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Lavan_Island_Airport, self).__init__()

        self.runways.append(Runway(110))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(75569.2578125, -286948.1875), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(75557.359375, -286984.34375), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(75593.5625, -287067.09375), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=11.0, shelter=False))


class Jiroft_Airport(Airport):
    id = 27
    name = "Jiroft Airport"
    position = mapping.Point(282607.962896, 141685.262108)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Jiroft_Airport, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(282949.9375, 141762.96875), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(282912.96875, 141809.546875), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(282983.96875, 141716.1875), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=11.0, shelter=False))


class Ras_Al_Khaimah(Airport):
    id = 28
    name = "Ras Al Khaimah"
    position = mapping.Point(-61597.517578, -30802.77832)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Ras_Al_Khaimah, self).__init__()

        self.runways.append(Runway(350))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-61266.63671875, -30535.681640625), large=False, heli=True,
                airplanes=True, slot_name='12', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-61342.05078125, -30518.6484375), large=False, heli=True,
                airplanes=True, slot_name='13', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-61402.73046875, -30502.13671875), large=False, heli=True,
                airplanes=True, slot_name='14', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-61475.578125, -30498.08203125), large=False, heli=True,
                airplanes=True, slot_name='15', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-61199.7109375, -30555.169921875), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-61152.8125, -30566.625), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-61040.9765625, -30716.130859375), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-61086.83203125, -30704.681640625), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-61138.0703125, -30692.19921875), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-61191.9609375, -30677.60546875), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-61324.31640625, -30652.87890625), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-61367.296875, -30641.451171875), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-61412.5859375, -30628.76171875), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-63740.3125, -30830.5546875), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-63696.48828125, -30853.599609375), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-63693.69921875, -30817.26171875), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-61097.9609375, -30583.76953125), large=False, heli=True,
                airplanes=True, slot_name='09', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-61026.64453125, -30603.8828125), large=False, heli=True,
                airplanes=True, slot_name='08', length=43.057953, width=40.0, height=None, shelter=False))


class Liwa_Airbase(Airport):
    id = 29
    name = "Liwa Airbase"
    position = mapping.Point(-275765.53125, -248213.578125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Liwa_Airbase, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-275178.9375, -249924.1875), large=False, heli=True,
                airplanes=True, slot_name='05', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-274636.25, -249777), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-274662.8125, -249817.453125), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-275104.40625, -250004.90625), large=False, heli=True,
                airplanes=True, slot_name='03', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-275140.46875, -249965.515625), large=False, heli=True,
                airplanes=True, slot_name='04', length=43.057953, width=40.0, height=None, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-275771.65625, -249029.625), large=False, heli=False,
                airplanes=True, slot_name='27', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-275785.40625, -249014.390625), large=False, heli=False,
                airplanes=True, slot_name='28', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-275975.53125, -248798.59375), large=False, heli=False,
                airplanes=True, slot_name='31', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-276141.125, -248444.484375), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-276119.78125, -248468.34375), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-276098.25, -248492.15625), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-276077.34375, -248514.953125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-276422.25, -248125.8125), large=False, heli=True,
                airplanes=True, slot_name='36', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-276489.9375, -248051.625), large=False, heli=True,
                airplanes=True, slot_name='37', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-276556.5625, -247979.53125), large=False, heli=True,
                airplanes=True, slot_name='38', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-276682, -247840.375), large=False, heli=False,
                airplanes=True, slot_name='39', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-276695.59375, -247825.609375), large=False, heli=False,
                airplanes=True, slot_name='40', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-276708.90625, -247810.53125), large=False, heli=False,
                airplanes=True, slot_name='41', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-276727, -247790.921875), large=False, heli=False,
                airplanes=True, slot_name='42', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-276740.4375, -247775.90625), large=False, heli=False,
                airplanes=True, slot_name='43', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-276940.65625, -247556.96875), large=False, heli=False,
                airplanes=True, slot_name='49', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-276954.40625, -247542.28125), large=False, heli=False,
                airplanes=True, slot_name='50', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-276967.78125, -247527.109375), large=False, heli=False,
                airplanes=True, slot_name='51', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-276985.84375, -247507.5), large=False, heli=False,
                airplanes=True, slot_name='52', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-276999.4375, -247492.609375), large=False, heli=False,
                airplanes=True, slot_name='53', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-276838.15625, -247668.671875), large=False, heli=False,
                airplanes=True, slot_name='46', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-276851.875, -247653.953125), large=False, heli=False,
                airplanes=True, slot_name='47', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-276865.0625, -247638.875), large=False, heli=False,
                airplanes=True, slot_name='48', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-276806.625, -247703.359375), large=False, heli=False,
                airplanes=True, slot_name='44', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-276820.21875, -247688.484375), large=False, heli=False,
                airplanes=True, slot_name='45', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-277094.375, -247388.515625), large=False, heli=False,
                airplanes=True, slot_name='56', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-277108.125, -247373.875), large=False, heli=False,
                airplanes=True, slot_name='57', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-277121.6875, -247358.40625), large=False, heli=False,
                airplanes=True, slot_name='58', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-277062.90625, -247423.25), large=False, heli=False,
                airplanes=True, slot_name='54', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-277076.375, -247408.3125), large=False, heli=False,
                airplanes=True, slot_name='55', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-277205.28125, -247027.515625), large=False, heli=True,
                airplanes=True, slot_name='60', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-277173.25, -246999.75), large=False, heli=True,
                airplanes=True, slot_name='59', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-275757.9375, -249044.46875), large=False, heli=False,
                airplanes=True, slot_name='26', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-275961.1875, -248813.53125), large=False, heli=False,
                airplanes=True, slot_name='30', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-275947.5, -248828.34375), large=False, heli=False,
                airplanes=True, slot_name='29', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-275001.96875, -249652.78125), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-275020.40625, -249632.578125), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-275054.3125, -249673.1875), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-275038.59375, -249612.515625), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-275073.0625, -249653.375), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-275035.375, -249692.375), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-275154.46875, -249566.96875), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-275173.3125, -249547.09375), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-275192.21875, -249527.8125), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-275092.1875, -249633.78125), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-275111.0625, -249614.15625), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-275056.4375, -249592.1875), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-275074.8125, -249572.265625), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-275211.1875, -249508.4375), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-275230.09375, -249489.03125), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-275117.1875, -249526.703125), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-275135.25, -249506.53125), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-275153.5625, -249486.515625), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-275171.90625, -249466.28125), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-275190.09375, -249446.140625), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=18.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-277336.78125, -247143.078125), large=False, heli=False,
                airplanes=True, slot_name='61', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-277356.75, -247160.96875), large=False, heli=False,
                airplanes=True, slot_name='62', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-277376.84375, -247179.046875), large=False, heli=False,
                airplanes=True, slot_name='63', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-277396.84375, -247196.125), large=False, heli=False,
                airplanes=True, slot_name='64', length=20.5, width=14.5, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-277416.90625, -247214.046875), large=False, heli=False,
                airplanes=True, slot_name='65', length=20.5, width=14.5, height=11.0, shelter=False))


class PersianGulf(Terrain):
    center = {"lat": 0, "long": 0}
    bounds = mapping.Rectangle(-218768.750000, -392081.937500, 197357.906250, 333129.125000)
    map_view_default = MapView(bounds.center(), 1000000)
    city_graph = None
    temperature = [
        (10, 20),
        (11, 20),
        (13, 22),
        (16, 26),
        (18, 30),
        (20, 36),
        (24, 39),
        (25, 40),
        (22, 37),
        (20, 32),
        (16, 26),
        (12, 22)
    ]
    assert(len(temperature) == 12)

    def __init__(self):
        super(PersianGulf, self).__init__("PersianGulf")
        self.bullseye_blue = {"x": PersianGulf.bounds.center().x, "y": PersianGulf.bounds.center().y}
        self.bullseye_red = {"x": PersianGulf.bounds.center().x, "y": PersianGulf.bounds.center().y}

        self.airports['Abu Musa Island Airport'] = Abu_Musa_Island_Airport()
        self.airports['Bandar Abbas Intl'] = Bandar_Abbas_Intl()
        self.airports['Bandar Lengeh'] = Bandar_Lengeh()
        self.airports['Al Dhafra AB'] = Al_Dhafra_AB()
        self.airports['Dubai Intl'] = Dubai_Intl()
        self.airports['Al Maktoum Intl'] = Al_Maktoum_Intl()
        self.airports['Fujairah Intl'] = Fujairah_Intl()
        self.airports['Tunb Island AFB'] = Tunb_Island_AFB()
        self.airports['Havadarya'] = Havadarya()
        self.airports['Khasab'] = Khasab()
        self.airports['Lar Airbase'] = Lar_Airbase()
        self.airports['Al Minhad AB'] = Al_Minhad_AB()
        self.airports['Qeshm Island'] = Qeshm_Island()
        self.airports['Sharjah Intl'] = Sharjah_Intl()
        self.airports['Sirri Island'] = Sirri_Island()
        self.airports['Tunb Kochak'] = Tunb_Kochak()
        self.airports['Sir Abu Nuayr'] = Sir_Abu_Nuayr()
        self.airports['Kerman Airport'] = Kerman_Airport()
        self.airports['Shiraz International Airport'] = Shiraz_International_Airport()
        self.airports['Sas Al Nakheel Airport'] = Sas_Al_Nakheel_Airport()
        self.airports['Bandar-e-Jask airfield'] = Bandar_e_Jask_airfield()
        self.airports['Abu Dhabi International Airport'] = Abu_Dhabi_International_Airport()
        self.airports['Al-Bateen Airport'] = Al_Bateen_Airport()
        self.airports['Kish International Airport'] = Kish_International_Airport()
        self.airports['Al Ain International Airport'] = Al_Ain_International_Airport()
        self.airports['Lavan Island Airport'] = Lavan_Island_Airport()
        self.airports['Jiroft Airport'] = Jiroft_Airport()
        self.airports['Ras Al Khaimah'] = Ras_Al_Khaimah()
        self.airports['Liwa Airbase'] = Liwa_Airbase()

    def abu_musa_island_airport(self) -> Airport:
        return self.airports["Abu Musa Island Airport"]

    def bandar_abbas_intl(self) -> Airport:
        return self.airports["Bandar Abbas Intl"]

    def bandar_lengeh(self) -> Airport:
        return self.airports["Bandar Lengeh"]

    def al_dhafra_ab(self) -> Airport:
        return self.airports["Al Dhafra AB"]

    def dubai_intl(self) -> Airport:
        return self.airports["Dubai Intl"]

    def al_maktoum_intl(self) -> Airport:
        return self.airports["Al Maktoum Intl"]

    def fujairah_intl(self) -> Airport:
        return self.airports["Fujairah Intl"]

    def tunb_island_afb(self) -> Airport:
        return self.airports["Tunb Island AFB"]

    def havadarya(self) -> Airport:
        return self.airports["Havadarya"]

    def khasab(self) -> Airport:
        return self.airports["Khasab"]

    def lar_airbase(self) -> Airport:
        return self.airports["Lar Airbase"]

    def al_minhad_ab(self) -> Airport:
        return self.airports["Al Minhad AB"]

    def qeshm_island(self) -> Airport:
        return self.airports["Qeshm Island"]

    def sharjah_intl(self) -> Airport:
        return self.airports["Sharjah Intl"]

    def sirri_island(self) -> Airport:
        return self.airports["Sirri Island"]

    def tunb_kochak(self) -> Airport:
        return self.airports["Tunb Kochak"]

    def sir_abu_nuayr(self) -> Airport:
        return self.airports["Sir Abu Nuayr"]

    def kerman_airport(self) -> Airport:
        return self.airports["Kerman Airport"]

    def shiraz_international_airport(self) -> Airport:
        return self.airports["Shiraz International Airport"]

    def sas_al_nakheel_airport(self) -> Airport:
        return self.airports["Sas Al Nakheel Airport"]

    def bandar_e_jask_airfield(self) -> Airport:
        return self.airports["Bandar-e-Jask airfield"]

    def abu_dhabi_international_airport(self) -> Airport:
        return self.airports["Abu Dhabi International Airport"]

    def al_bateen_airport(self) -> Airport:
        return self.airports["Al-Bateen Airport"]

    def kish_international_airport(self) -> Airport:
        return self.airports["Kish International Airport"]

    def al_ain_international_airport(self) -> Airport:
        return self.airports["Al Ain International Airport"]

    def lavan_island_airport(self) -> Airport:
        return self.airports["Lavan Island Airport"]

    def jiroft_airport(self) -> Airport:
        return self.airports["Jiroft Airport"]

    def ras_al_khaimah(self) -> Airport:
        return self.airports["Ras Al Khaimah"]

    def liwa_airbase(self) -> Airport:
        return self.airports["Liwa Airbase"]
