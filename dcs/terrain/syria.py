import dcs.mapping as mapping
from dcs.terrain.terrain import Airport, Runway, ParkingSlot, Terrain, MapView




class Abu_al_Duhur(Airport):
    id = 1
    name = "Abu al-Duhur"
    position = mapping.Point(76048.957031, 111344.925781)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Abu_al_Duhur, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(76278.421875, 112793.0546875), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(76280.484375, 112763.25), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(76282.2890625, 112736.3046875), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(76284.1953125, 112705.6796875), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(76400.609375, 110599.65625), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(76402.859375, 110567.171875), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(76404.890625, 110536.2734375), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(76406.9296875, 110499.9375), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(76409.6328125, 110467.5703125), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(76411.3984375, 110436.765625), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(76414.28125, 110395.2109375), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(76416.4609375, 110362.796875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(76418.4140625, 110331.859375), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(76420.359375, 110301.1015625), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(76422.5078125, 110268.7109375), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(76424.5234375, 110237.8515625), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(75966.7890625, 109730.6171875), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(75991.09375, 109711.640625), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(75803.5078125, 109767.09375), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(75787.90625, 109793.015625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(76501.0859375, 109760.703125), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(76490.6953125, 110072.265625), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(76508.8671875, 110095.625), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(76616.0625, 109895.9296875), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(75492.9453125, 113106.21875), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(75527.59375, 113285.515625), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(75745.9296875, 113080.5625), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(75771.4453125, 113096.8046875), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(75780.125, 112892.0390625), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(75761.453125, 112869.125), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(76338.578125, 112682.484375), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(76358.4140625, 112659.1484375), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(76308.984375, 112864.46875), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(76307.375, 112894.4765625), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(76437.9453125, 113020.0859375), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(76293.3046875, 113035.640625), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Adana_Sakirpasa(Airport):
    id = 2
    name = "Adana Sakirpasa"
    position = mapping.Point(219468.664823, -48332.726595)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Adana_Sakirpasa, self).__init__()

        self.runways.append(Runway(50))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(219900.5625, -46846.515625), large=False, heli=True,
                airplanes=True, slot_name='A02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(219858.125, -46855.546875), large=False, heli=True,
                airplanes=True, slot_name='A03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(219815.28125, -46864.4453125), large=False, heli=True,
                airplanes=True, slot_name='A04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(219762.125, -47053.75390625), large=False, heli=True,
                airplanes=True, slot_name='A18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(219807.296875, -47023.7109375), large=False, heli=True,
                airplanes=True, slot_name='A19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(219849.4375, -47014.03515625), large=False, heli=True,
                airplanes=True, slot_name='A20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(219890.65625, -47004), large=False, heli=True,
                airplanes=True, slot_name='A21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(219488.75, -47186.5546875), large=False, heli=True,
                airplanes=True, slot_name='A11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(219525.828125, -47211.81640625), large=False, heli=True,
                airplanes=True, slot_name='A12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(219562.796875, -47237.203125), large=False, heli=True,
                airplanes=True, slot_name='A13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(219600, -47262.6640625), large=False, heli=True,
                airplanes=True, slot_name='A14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(219741.6875, -47087.30078125), large=False, heli=True,
                airplanes=True, slot_name='A17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(219719.5, -47122.19921875), large=False, heli=True,
                airplanes=True, slot_name='A16', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(219697.046875, -47157.515625), large=False, heli=True,
                airplanes=True, slot_name='A15', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(219574.234375, -47078.08203125), large=False, heli=True,
                airplanes=True, slot_name='A10', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(219602.96875, -47017.16015625), large=False, heli=True,
                airplanes=True, slot_name='A09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(219634.609375, -46966.6171875), large=False, heli=True,
                airplanes=True, slot_name='A08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(219662.421875, -46926.73828125), large=False, heli=True,
                airplanes=True, slot_name='A07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(219941.34375, -46837.109375), large=False, heli=True,
                airplanes=True, slot_name='A01', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(220288.765625, -47549.07421875), large=False, heli=True,
                airplanes=True, slot_name='E10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(220298.21875, -47535.03125), large=False, heli=True,
                airplanes=True, slot_name='E11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(220307.859375, -47521.16015625), large=False, heli=True,
                airplanes=True, slot_name='E12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(220317.359375, -47507.09765625), large=False, heli=True,
                airplanes=True, slot_name='E13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(220326.84375, -47492.9609375), large=False, heli=True,
                airplanes=True, slot_name='E14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(220336.21875, -47479.0546875), large=False, heli=True,
                airplanes=True, slot_name='E15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(220345.6875, -47464.9140625), large=False, heli=True,
                airplanes=True, slot_name='E16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(220354.859375, -47450.5703125), large=False, heli=True,
                airplanes=True, slot_name='E17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(220322.609375, -47572.0859375), large=False, heli=True,
                airplanes=True, slot_name='E09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(220332.09375, -47558.03125), large=False, heli=True,
                airplanes=True, slot_name='E08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(220341.578125, -47544), large=False, heli=True,
                airplanes=True, slot_name='E07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(220351, -47529.953125), large=False, heli=True,
                airplanes=True, slot_name='E06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(220360.65625, -47516.0546875), large=False, heli=True,
                airplanes=True, slot_name='E05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(220370.421875, -47502.0703125), large=False, heli=True,
                airplanes=True, slot_name='E04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(220379.953125, -47488.0859375), large=False, heli=True,
                airplanes=True, slot_name='E03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(220389.625, -47474.3125), large=False, heli=True,
                airplanes=True, slot_name='E02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(220399.078125, -47460.22265625), large=False, heli=True,
                airplanes=True, slot_name='E01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(219772.8125, -46873.67578125), large=False, heli=True,
                airplanes=True, slot_name='A05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(219518.03125, -47376.125), large=False, heli=True,
                airplanes=True, slot_name='D09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(219730.984375, -46882.53515625), large=False, heli=True,
                airplanes=True, slot_name='A06', length=40.0, width=40.0, height=12.0, shelter=False))


class Al_Qusayr(Airport):
    id = 3
    name = "Al Qusayr"
    position = mapping.Point(-51906.964844, 60013.205078)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Al_Qusayr, self).__init__()

        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-52056.5390625, 61770.86328125), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-52566.94921875, 61464.7890625), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-52500.484375, 61317.16796875), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-51948.35546875, 61612.2578125), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-51972.328125, 61593.85546875), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-52038.29296875, 61746.96484375), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-52766.8828125, 60728.390625), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-52640.1328125, 60846.4296875), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-52501.90234375, 60966.1015625), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-52605.703125, 61212.45703125), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-52790.546875, 61230.703125), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-52867.08984375, 60932.19921875), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-52081.63671875, 61509.1015625), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-52087.23046875, 61538.1484375), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-52093.78125, 61567.65625), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-52075.3125, 61479.44140625), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-52069.45703125, 61451.28125), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-51863.296875, 61428.0859375), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-51812.81640625, 61198.140625), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-51989.81640625, 61405.69140625), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-51782.390625, 60877.16015625), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-51936.0390625, 61043.2421875), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-51870.59765625, 60628.65234375), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-51317.875, 58704.515625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-51364.1015625, 58951.3671875), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-51407.0625, 59198.75), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-52663.64453125, 60956.81640625), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-52700.69140625, 60924.24609375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-52644.203125, 60973.25), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-52553.6171875, 61054.27734375), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-52531.56640625, 61073.28125), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-52576.43359375, 61034.078125), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-52619.29296875, 60995.71484375), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-52597.859375, 61015.2109375), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))


class An_Nasiriyah(Airport):
    id = 4
    name = "An Nasiriyah"
    position = mapping.Point(-124683.742188, 85510.828125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(An_Nasiriyah, self).__init__()

        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-123598.6015625, 86827.671875), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-123275.296875, 86664.0859375), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-123568.1015625, 86825.8828125), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-123106.7578125, 86653.2421875), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-125357.9453125, 84394.0859375), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-123721.4296875, 86703.7265625), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-123701.046875, 86681.3359375), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-125473.6796875, 84044.0625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-123541.8359375, 86164.84375), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-123564.3984375, 86185.2109375), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-123924.6875, 86560.828125), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-123895.953125, 86569.4765625), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-125594.9453125, 84158.2734375), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-122879.5625, 86506.7265625), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-123152.28125, 86265.3359375), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-123062.15625, 86384.8359375), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-123047.2421875, 86024.8203125), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-122640.78125, 86333.828125), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-125131.5234375, 84656.09375), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-122956.1015625, 86242.4140625), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Beirut_Rafic_Hariri(Airport):
    id = 6
    name = "Beirut-Rafic Hariri"
    position = mapping.Point(-131257.175781, -42287.623047)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Beirut_Rafic_Hariri, self).__init__()

        self.runways.append(Runway(350))
        self.runways.append(Runway(210))
        self.runways.append(Runway(340))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-131575.125, -41971.7890625), large=False, heli=True,
                airplanes=True, slot_name='G20', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-131642.984375, -41980.86328125), large=False, heli=True,
                airplanes=True, slot_name='G19', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-131692.421875, -41993.0703125), large=False, heli=True,
                airplanes=True, slot_name='G18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-131786.734375, -41945.84375), large=False, heli=True,
                airplanes=True, slot_name='G17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-131951.234375, -41991.8515625), large=False, heli=True,
                airplanes=True, slot_name='S3', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-131964.4375, -41914.20703125), large=False, heli=True,
                airplanes=True, slot_name='S2', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-131979.609375, -41838.609375), large=False, heli=True,
                airplanes=True, slot_name='S1', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-131758.71875, -41885.71875), large=False, heli=True,
                airplanes=True, slot_name='G16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-131771.546875, -41667.3828125), large=False, heli=True,
                airplanes=True, slot_name='G7', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-131725.765625, -41648.984375), large=False, heli=True,
                airplanes=True, slot_name='G6', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-131488.5625, -41470.69140625), large=False, heli=True,
                airplanes=True, slot_name='G1', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-131557.375, -41523.92578125), large=False, heli=True,
                airplanes=True, slot_name='G2', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-131393.5625, -41979.4296875), large=False, heli=True,
                airplanes=True, slot_name='G23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-131620.078125, -41581.546875), large=False, heli=True,
                airplanes=True, slot_name='G3', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-131674.96875, -41628.92578125), large=False, heli=True,
                airplanes=True, slot_name='G5', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-131595.9375, -41841.8359375), large=False, heli=True,
                airplanes=True, slot_name='G13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-131650.390625, -41857.63671875), large=False, heli=True,
                airplanes=True, slot_name='G14', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-131706.890625, -41870.36328125), large=False, heli=True,
                airplanes=True, slot_name='G15', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-131682.546875, -41763.52734375), large=False, heli=True,
                airplanes=True, slot_name='G11', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-131632.953125, -41746.82421875), large=False, heli=True,
                airplanes=True, slot_name='G12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-131836.875, -41722.828125), large=False, heli=True,
                airplanes=True, slot_name='G8', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-131794.03125, -41787.97265625), large=False, heli=True,
                airplanes=True, slot_name='G9', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-131735.46875, -41775.55859375), large=False, heli=True,
                airplanes=True, slot_name='G10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-131499.8125, -41955.84375), large=False, heli=True,
                airplanes=True, slot_name='G21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-131443.328125, -41976.93359375), large=False, heli=True,
                airplanes=True, slot_name='G22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-131341.171875, -41978.5625), large=False, heli=True,
                airplanes=True, slot_name='G24', length=40.0, width=40.0, height=12.0, shelter=False))


class Damascus(Airport):
    id = 7
    name = "Damascus"
    position = mapping.Point(-178652.320313, 52081.296875)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Damascus, self).__init__()

        self.runways.append(Runway(230))
        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-182103.921875, 50133.484375), large=False, heli=True,
                airplanes=True, slot_name='027', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-182079.9375, 50162.125), large=False, heli=True,
                airplanes=True, slot_name='028', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-182151.59375, 50076.640625), large=False, heli=True,
                airplanes=True, slot_name='025', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-182127.9375, 50105.02734375), large=False, heli=True,
                airplanes=True, slot_name='026', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-182597.125, 49554.92578125), large=False, heli=True,
                airplanes=True, slot_name='020', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-182576.625, 49579.90625), large=False, heli=True,
                airplanes=True, slot_name='021', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-182618, 49528.79296875), large=False, heli=True,
                airplanes=True, slot_name='019', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-182638.34375, 49502.859375), large=False, heli=True,
                airplanes=True, slot_name='018', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-182534.421875, 49631.0234375), large=False, heli=True,
                airplanes=True, slot_name='023', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-182658.859375, 49476.6328125), large=False, heli=True,
                airplanes=True, slot_name='017', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-182555.703125, 49605.609375), large=False, heli=True,
                airplanes=True, slot_name='022', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-182171.78125, 50052.8125), large=False, heli=True,
                airplanes=True, slot_name='024', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-180549.03125, 52349.53125), large=False, heli=True,
                airplanes=True, slot_name='605', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-180023.578125, 51576.33984375), large=False, heli=True,
                airplanes=True, slot_name='104', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-180034.046875, 51822.71875), large=False, heli=True,
                airplanes=True, slot_name='107', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-180121.078125, 51656.84765625), large=False, heli=True,
                airplanes=True, slot_name='108', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-180216.625, 51742.62109375), large=False, heli=True,
                airplanes=True, slot_name='112', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-179968.0625, 51721.75390625), large=False, heli=True,
                airplanes=True, slot_name='103', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-180071.171875, 51613.84375), large=False, heli=True,
                airplanes=True, slot_name='106', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-180179.84375, 51706.2578125), large=False, heli=True,
                airplanes=True, slot_name='110', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-180093.234375, 51938.5078125), large=False, heli=True,
                airplanes=True, slot_name='109', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-180503.359375, 52077.76953125), large=False, heli=True,
                airplanes=True, slot_name='405', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-180508.796875, 51856.6796875), large=False, heli=True,
                airplanes=True, slot_name='402', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-180476.796875, 52054.9765625), large=False, heli=True,
                airplanes=True, slot_name='403', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-180572.671875, 51942.6484375), large=False, heli=True,
                airplanes=True, slot_name='406', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-180451.734375, 52033.3359375), large=False, heli=True,
                airplanes=True, slot_name='401', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-180545.109375, 51920.609375), large=False, heli=True,
                airplanes=True, slot_name='404', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-179810.96875, 51569.44921875), large=False, heli=True,
                airplanes=True, slot_name='201', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-179976.46875, 51775.23046875), large=False, heli=True,
                airplanes=True, slot_name='105', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-179954.453125, 51551.546875), large=False, heli=True,
                airplanes=True, slot_name='102', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-179840.0625, 51725.0859375), large=False, heli=True,
                airplanes=True, slot_name='101', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-179999.09375, 51471.859375), large=False, heli=True,
                airplanes=True, slot_name='205', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-179926.27465564, 51484.920570022), large=False, heli=True,
                airplanes=True, slot_name='204', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-180440.125, 52258.203125), large=False, heli=True,
                airplanes=True, slot_name='603', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-180491.015625, 52300.703125), large=False, heli=True,
                airplanes=True, slot_name='604', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-180378.5625, 52206.59375), large=False, heli=True,
                airplanes=True, slot_name='602', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-180325.46875, 52162), large=False, heli=True,
                airplanes=True, slot_name='601', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-182418.078125, 50021.2890625), large=False, heli=True,
                airplanes=True, slot_name='030', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-182505.875, 49926.953125), large=False, heli=True,
                airplanes=True, slot_name='031', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-182591.890625, 49820.92578125), large=False, heli=True,
                airplanes=True, slot_name='032', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-182434.578125, 49777.859375), large=False, heli=True,
                airplanes=True, slot_name='033', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-182357.765625, 49878.80859375), large=False, heli=True,
                airplanes=True, slot_name='034', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-180319.75, 51928.64453125), large=False, heli=True,
                airplanes=True, slot_name='302', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-180304.625, 51797.5078125), large=False, heli=True,
                airplanes=True, slot_name='305', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-180325.234375, 51866.23828125), large=False, heli=True,
                airplanes=True, slot_name='303', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-181032.0625, 53098.3125), large=False, heli=False,
                airplanes=True, slot_name='003', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-181048.265625, 53005.3125), large=False, heli=False,
                airplanes=True, slot_name='004', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-182336.234375, 50118.328125), large=False, heli=True,
                airplanes=True, slot_name='029', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-179802, 51497.5234375), large=False, heli=True,
                airplanes=True, slot_name='202', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-179854.0625, 51491.703125), large=False, heli=True,
                airplanes=True, slot_name='203', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-180239.546875, 51845.08984375), large=False, heli=True,
                airplanes=True, slot_name='114', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-180241.75, 51945.69921875), large=False, heli=True,
                airplanes=True, slot_name='301', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-181462.96875, 52711.265625), large=False, heli=False,
                airplanes=True, slot_name='007', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-181522.421875, 52640.15234375), large=False, heli=False,
                airplanes=True, slot_name='008', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-181364.140625, 52643.0546875), large=False, heli=False,
                airplanes=True, slot_name='006', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(-181336.390625, 52654.6328125), large=False, heli=False,
                airplanes=True, slot_name='005', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(-180913.796875, 53041.88671875), large=False, heli=False,
                airplanes=True, slot_name='002', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(-180883.6875, 53046.20703125), large=False, heli=False,
                airplanes=True, slot_name='001', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(-183196.75, 50492.57421875), large=False, heli=False,
                airplanes=True, slot_name='009', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(-183275.21875, 50455.08203125), large=False, heli=False,
                airplanes=True, slot_name='010', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(-183207.46875, 50352.9140625), large=False, heli=False,
                airplanes=True, slot_name='011', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=65, position=mapping.Point(-183209.59375, 50323.0859375), large=False, heli=False,
                airplanes=True, slot_name='012', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(-183540.765625, 50043.6328125), large=False, heli=False,
                airplanes=True, slot_name='013', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(-183629.3125, 50000.96875), large=False, heli=False,
                airplanes=True, slot_name='014', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(-183553.53125, 49894.3984375), large=False, heli=False,
                airplanes=True, slot_name='015', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(-183554.109375, 49864.30078125), large=False, heli=False,
                airplanes=True, slot_name='016', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(-180308.046875, 51844.01171875), large=False, heli=True,
                airplanes=True, slot_name='304', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(-180530.953125, 52101.3984375), large=False, heli=True,
                airplanes=True, slot_name='407', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(-180561.375, 52125.96484375), large=False, heli=True,
                airplanes=True, slot_name='409', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(-180597.59375, 51963.85546875), large=False, heli=True,
                airplanes=True, slot_name='408', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(-180626.328125, 51986.86328125), large=False, heli=True,
                airplanes=True, slot_name='410', length=26.0, width=24.0, height=11.0, shelter=False))


class Marj_as_Sultan_South(Airport):
    id = 8
    name = "Marj as Sultan South"
    position = mapping.Point(-171711.34375, 48243.474609)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Marj_as_Sultan_South, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-171652.453125, 48101.5703125), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-171651.875, 48367.8515625), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-171771.4375, 48372.2265625), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-171773.296875, 48102.4765625), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-171779.828125, 48248.85546875), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-171767.15625, 48195.12109375), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-171767, 48305.7265625), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-171654.703125, 48291.1796875), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-171646.5625, 48235.890625), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-171656.25, 48179.6640625), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-171852.984375, 48086.94921875), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-171904.359375, 48083.8125), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-171956.9375, 48100.26171875), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-172016.921875, 48085.01953125), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-172074.390625, 48100.44921875), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-171934.328125, 48309.90625), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-171918.421875, 48256.94921875), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-172001.609375, 48264.4140625), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-171981.046875, 48210.8515625), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-171953.5625, 48166.6171875), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.096436, width=23.0, height=10.0, shelter=False))


class Al_Dumayr(Airport):
    id = 9
    name = "Al-Dumayr"
    position = mapping.Point(-158713.015625, 73973.308594)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Al_Dumayr, self).__init__()

        self.runways.append(Runway(240))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-158242.609375, 75715.703125), large=False, heli=False,
                airplanes=True, slot_name='43', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-158232.625, 75689.1953125), large=False, heli=False,
                airplanes=True, slot_name='42', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-158761.4375, 72028.609375), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-157710.171875, 75231.796875), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-157622.9375, 75800.9140625), large=False, heli=False,
                airplanes=True, slot_name='40', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-157653.703125, 75803.328125), large=False, heli=False,
                airplanes=True, slot_name='41', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-157471.734375, 75794.2734375), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-157449.46875, 75771.4609375), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-158137.703125, 76126.078125), large=False, heli=False,
                airplanes=True, slot_name='45', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-158431.59375, 75707.96875), large=False, heli=False,
                airplanes=True, slot_name='47', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-158785.5625, 75609.828125), large=False, heli=False,
                airplanes=True, slot_name='52', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-158814.5625, 75600.6015625), large=False, heli=False,
                airplanes=True, slot_name='53', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-158554.96875, 75493.984375), large=False, heli=False,
                airplanes=True, slot_name='50', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-158565.078125, 75465.546875), large=False, heli=False,
                airplanes=True, slot_name='51', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-158538.359375, 75180.0703125), large=False, heli=False,
                airplanes=True, slot_name='56', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-158523.875, 75154.296875), large=False, heli=False,
                airplanes=True, slot_name='57', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-158921.171875, 75350.21875), large=False, heli=False,
                airplanes=True, slot_name='55', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-158948.625, 75362.234375), large=False, heli=False,
                airplanes=True, slot_name='54', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-159469.859375, 72838.5234375), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-159440.78125, 72832.9453125), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-158889.359375, 72559.9765625), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-158870.78125, 72584.0703125), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-158174.84375, 72182.0390625), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-158177.65625, 72212.421875), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-158556.390625, 72571.9140625), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-158541.5625, 72597.59375), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-158377.15625, 72713.1796875), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-158359.90625, 72737.4765625), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-158488.296875, 72776.90625), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-158707.703125, 72821.8359375), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-158722.96875, 72847.4453125), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-157680.328125, 75131.9765625), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-157650.125, 75128.65625), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-157690.15625, 75229.3671875), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-157670.25, 75227.34375), large=False, heli=True,
                airplanes=True, slot_name='29', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-157649.921875, 75224.8828125), large=False, heli=True,
                airplanes=True, slot_name='30', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-157630.546875, 75222.109375), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-157610.375, 75220.0546875), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-157591.046875, 75218.3203125), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-157570.15625, 75215.796875), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-157747.671875, 75288.5078125), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-157630.234375, 75404.1484375), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-157627.921875, 75434.4609375), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-159437, 73087.453125), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-159448.609375, 73116.5), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-158510.421875, 73433.4609375), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-158459.09375, 73546.7890625), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-158183.984375, 75940.3515625), large=False, heli=False,
                airplanes=True, slot_name='44', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-158419.015625, 75930.8359375), large=False, heli=False,
                airplanes=True, slot_name='46', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-158339.359375, 75523.203125), large=False, heli=False,
                airplanes=True, slot_name='49', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-158363.0625, 75542.0078125), large=False, heli=False,
                airplanes=True, slot_name='48', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-157734.453125, 74958.09375), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-157770.0625, 74842.5703125), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-157912.9375, 74982.0078125), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-157874.734375, 75070.078125), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-157859.15625, 75102.3203125), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-157901.890625, 75007.4140625), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=24.0, height=11.0, shelter=False))


class Eyn_Shemer(Airport):
    id = 10
    name = "Eyn Shemer"
    position = mapping.Point(-283538.6875, -92619.707031)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Eyn_Shemer, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-283520.1875, -92408.5234375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-283534, -92333.6484375), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-283482.875, -92456.625), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-283477.09375, -92496.3125), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-283486.0625, -92572.09375), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))


class Haifa(Airport):
    id = 13
    name = "Haifa"
    position = mapping.Point(-242620.820313, -87704.414062)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Haifa, self).__init__()

        self.runways.append(Runway(340))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-242233.8125, -87917.359375), large=False, heli=True,
                airplanes=False, slot_name='G5', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-242259.09375, -87908.7734375), large=False, heli=True,
                airplanes=False, slot_name='G4', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-242298.84375, -87894.9375), large=False, heli=True,
                airplanes=False, slot_name='G2', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-242325.125, -87886.53125), large=False, heli=True,
                airplanes=False, slot_name='G1', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-242570.5625, -88062.0625), large=False, heli=True,
                airplanes=True, slot_name='A4', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-242545.73204501, -88004.954450024), large=False, heli=True,
                airplanes=True, slot_name='A3', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-242533.33099391, -87969.439396831), large=False, heli=True,
                airplanes=True, slot_name='A2', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-242520.9375, -87929.8515625), large=False, heli=True,
                airplanes=True, slot_name='A1', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-242438.1875, -87631.1484375), large=False, heli=True,
                airplanes=True, slot_name='Z1', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-242420.984375, -87576.859375), large=False, heli=True,
                airplanes=True, slot_name='Z2', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-242401.984375, -87516.6171875), large=False, heli=True,
                airplanes=True, slot_name='Z3', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-242382.6875, -87455.65625), large=False, heli=True,
                airplanes=True, slot_name='Z4', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-242365.09375, -87399.3359375), large=False, heli=True,
                airplanes=True, slot_name='Z5', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-242347.703125, -87345.6171875), large=False, heli=True,
                airplanes=True, slot_name='Z6', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-242328.296875, -87283.953125), large=False, heli=True,
                airplanes=True, slot_name='Z7', length=26.0, width=22.0, height=11.0, shelter=False))


class Hama(Airport):
    id = 14
    name = "Hama"
    position = mapping.Point(8662.594238, 74333.1875)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Hama, self).__init__()

        self.runways.append(Runway(90))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(8969.19140625, 73061.1796875), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(8987.0947265625, 73065.3359375), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(9003.8330078125, 73069.734375), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(9021.369140625, 73074.1953125), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(9038.6923828125, 73077.3125), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(9096.544921875, 73140.375), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(9087.6318359375, 73188.2421875), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(9080.4033203125, 73239.0703125), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(9070.2822265625, 73292.5078125), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(9063.8837890625, 73341.046875), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(8982.041015625, 73805.890625), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(8960.087890625, 73925.203125), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(8924.4296875, 74126.40625), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(8878.3486328125, 74368.84375), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(8806.32421875, 74738.8671875), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(9109.76171875, 73521.03125), large=False, heli=False,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(8805.6953125, 72709.8046875), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(8773.591796875, 72623.390625), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(9226.1826171875, 72544.3203125), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(9243.23046875, 72845.609375), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(9294.3466796875, 72885.828125), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(9209.2319367427, 73030.804909862), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(9192.7968205551, 73005.340178898), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(9091.3388671875, 74045.9375), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(8979.2412109375, 74404.8671875), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(9073.3447265625, 74481.828125), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(8909.4150390625, 74607.09375), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(8864.17578125, 74566.4765625), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(8875.3984375, 74498.046875), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(8918.9296875, 74538.0625), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(8858.369140625, 74960.9921875), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(8849.240234375, 74935.5390625), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(8932.3183460386, 75197.143783636), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(8873.484375, 75257.5), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(8987.3818359375, 75374.9140625), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(8896.9404296875, 75458.9453125), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(8868.0625, 75585.1171875), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(8974.4609375, 75647.84375), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(8708.390625, 75648.546875), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(8694.986328125, 75675.75), large=False, heli=False,
                airplanes=True, slot_name='40', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(8589.353515625, 75614.3984375), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(8571.681640625, 75610.78125), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(8554.55078125, 75607.328125), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(8538.439453125, 75603.234375), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(8521.263671875, 75601.2421875), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(8503.4921875, 75597.0625), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=8.0, shelter=False))


class Hatay(Airport):
    id = 15
    name = "Hatay"
    position = mapping.Point(147687.484375, 39418.742188)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Hatay, self).__init__()

        self.runways.append(Runway(40))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(147685.390625, 38910.453125), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(147745.34375, 38967.5625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(147655.046875, 38881.921875), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(147595.453125, 38823.1015625), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(147625, 38852.58984375), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(147866.75, 39084.96484375), large=False, heli=True,
                airplanes=True, slot_name='10', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(147836.515625, 39055.02734375), large=False, heli=True,
                airplanes=True, slot_name='09', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(147715.125, 38939.109375), large=False, heli=True,
                airplanes=True, slot_name='05', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(147775.15625, 38996.359375), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(147805.625, 39025.6796875), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))


class Incirlik(Airport):
    id = 16
    name = "Incirlik"
    position = mapping.Point(221207.757813, -35240.320313)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Incirlik, self).__init__()

        self.runways.append(Runway(230))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(221611.15625, -35769.90625), large=False, heli=True,
                airplanes=True, slot_name='45', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(221592.65625, -35796.59765625), large=False, heli=True,
                airplanes=True, slot_name='44', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(220781.78125, -36704.08984375), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(220757.921875, -36711.8515625), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(220734.671875, -36719.22265625), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(220541.8125, -35443.36328125), large=False, heli=True,
                airplanes=True, slot_name='109', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(220563.078125, -35410.88671875), large=False, heli=True,
                airplanes=True, slot_name='108', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(220585.9375, -35378.09375), large=False, heli=True,
                airplanes=True, slot_name='107', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(220609.28125, -35345.23828125), large=False, heli=True,
                airplanes=True, slot_name='106', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(220631.859375, -35312.375), large=False, heli=True,
                airplanes=True, slot_name='105', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(220654.40625, -35279.58203125), large=False, heli=True,
                airplanes=True, slot_name='104', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(220677.1875, -35246.8125), large=False, heli=True,
                airplanes=True, slot_name='103', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(220699.9375, -35213.90234375), large=False, heli=True,
                airplanes=True, slot_name='102', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(220723.4375, -35181.16796875), large=False, heli=True,
                airplanes=True, slot_name='101', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(220746.421875, -35148.296875), large=False, heli=True,
                airplanes=True, slot_name='100', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(220807.734375, -35045.38671875), large=False, heli=True,
                airplanes=True, slot_name='97', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(220853.53125, -35075.9375), large=False, heli=True,
                airplanes=True, slot_name='96', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(220899.09375, -35108.0625), large=False, heli=True,
                airplanes=True, slot_name='95', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(220965.453125, -35013.2578125), large=False, heli=True,
                airplanes=True, slot_name='92', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(220919.4375, -34981.546875), large=False, heli=True,
                airplanes=True, slot_name='93', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(220874.34375, -34950.09375), large=False, heli=True,
                airplanes=True, slot_name='94', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(220936.609375, -34861.01171875), large=False, heli=True,
                airplanes=True, slot_name='91', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(220982.375, -34891.5625), large=False, heli=True,
                airplanes=True, slot_name='90', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(221027.9375, -34923.5625), large=False, heli=True,
                airplanes=True, slot_name='89', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(221118.59375, -34820.7421875), large=False, heli=True,
                airplanes=True, slot_name='88', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(221240.765625, -34645.94921875), large=False, heli=True,
                airplanes=True, slot_name='87', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(221362.125, -34472.8515625), large=False, heli=True,
                airplanes=True, slot_name='86', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(221415.515625, -34336.8203125), large=False, heli=True,
                airplanes=False, slot_name='84', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(221455.84375, -34365.1171875), large=False, heli=True,
                airplanes=False, slot_name='83', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(221369.71875, -34261.078125), large=False, heli=True,
                airplanes=True, slot_name='85', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(222286.53125, -34268.48828125), large=False, heli=True,
                airplanes=True, slot_name='62', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(222337.203125, -34308.046875), large=False, heli=True,
                airplanes=True, slot_name='61', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(221783.03125, -34998.94140625), large=False, heli=True,
                airplanes=True, slot_name='59', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(221769.46875, -35121.02734375), large=False, heli=True,
                airplanes=True, slot_name='58', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(221663.328125, -35173.625), large=False, heli=True,
                airplanes=True, slot_name='57', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(221352.046875, -35618.01953125), large=False, heli=True,
                airplanes=True, slot_name='56', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(221334.53125, -35740.390625), large=False, heli=True,
                airplanes=True, slot_name='55', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(221218, -35794.05078125), large=False, heli=True,
                airplanes=True, slot_name='54', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(221660.515625, -33924.92578125), large=False, heli=True,
                airplanes=True, slot_name='74', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(220193.0625, -37450.8125), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(220107.609375, -37415.9453125), large=False, heli=False,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(220112.859375, -37340.12890625), large=False, heli=False,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(220493.671875, -36634.79296875), large=False, heli=True,
                airplanes=True, slot_name='120', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(220474.953125, -36622.3203125), large=False, heli=True,
                airplanes=True, slot_name='119', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(220456.40625, -36609.5234375), large=False, heli=True,
                airplanes=True, slot_name='118', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(220437.625, -36597.515625), large=False, heli=True,
                airplanes=True, slot_name='117', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(220419.0625, -36585.29296875), large=False, heli=True,
                airplanes=True, slot_name='116', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(220400.5625, -36573.3203125), large=False, heli=True,
                airplanes=True, slot_name='115', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(220381.1875, -36562.65625), large=False, heli=True,
                airplanes=True, slot_name='114', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(220036.31208129, -36235.521118004), large=False, heli=True,
                airplanes=True, slot_name='113', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(220080.15583129, -36170.985961754), large=False, heli=True,
                airplanes=True, slot_name='112', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(220125.32770629, -36107.431274254), large=False, heli=True,
                airplanes=True, slot_name='111', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(220425.25, -35753.1953125), large=False, heli=True,
                airplanes=True, slot_name='110', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(221190.96875, -36151.00390625), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(221186.8125, -36175.6953125), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(221183.578125, -36199.9921875), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(222191.25, -34015.05859375), large=False, heli=True,
                airplanes=True, slot_name='69', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(222208.984375, -34028.06640625), large=False, heli=True,
                airplanes=True, slot_name='68', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=59, position=mapping.Point(222227.15625, -34040.80859375), large=False, heli=True,
                airplanes=True, slot_name='67', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=60, position=mapping.Point(222244.640625, -34054.7109375), large=False, heli=True,
                airplanes=True, slot_name='66', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=61, position=mapping.Point(222263.4375, -34067.50390625), large=False, heli=True,
                airplanes=True, slot_name='65', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=62, position=mapping.Point(222281.34375, -34080.6640625), large=False, heli=True,
                airplanes=True, slot_name='64', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=63, position=mapping.Point(222300.140625, -34093.53515625), large=False, heli=True,
                airplanes=True, slot_name='63', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=64, position=mapping.Point(220883.36946329, -36797.266717627), large=False, heli=False,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=66, position=mapping.Point(221647.10682397, -34034.708625521), large=False, heli=False,
                airplanes=True, slot_name='80', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=67, position=mapping.Point(221546.765625, -33983.25), large=False, heli=False,
                airplanes=True, slot_name='77', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=68, position=mapping.Point(221638.83425668, -33963.162925452), large=False, heli=False,
                airplanes=True, slot_name='76', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=69, position=mapping.Point(221703.7883702, -33826.07019641), large=False, heli=False,
                airplanes=True, slot_name='72', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=70, position=mapping.Point(221740.65625, -33861.43359375), large=False, heli=False,
                airplanes=True, slot_name='71', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=71, position=mapping.Point(221865.40625, -33788.88671875), large=False, heli=True,
                airplanes=True, slot_name='70', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=72, position=mapping.Point(220146.359375, -37479.921875), large=False, heli=False,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=73, position=mapping.Point(220263.046875, -37561.2734375), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=74, position=mapping.Point(220273.125, -37497.6953125), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=75, position=mapping.Point(220411.9375, -37532.71484375), large=False, heli=False,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=76, position=mapping.Point(220813.578125, -37058.859375), large=False, heli=False,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=77, position=mapping.Point(220785.890625, -36909.70703125), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=78, position=mapping.Point(220851.265625, -36981.671875), large=False, heli=False,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=79, position=mapping.Point(220944.01050823, -36643.995148013), large=False, heli=False,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=80, position=mapping.Point(221090.36135542, -36728.831590744), large=False, heli=False,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=81, position=mapping.Point(221281.02574291, -36368.447959114), large=False, heli=False,
                airplanes=True, slot_name='32', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=82, position=mapping.Point(221103.95074849, -36012.221424422), large=False, heli=False,
                airplanes=True, slot_name='36', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=83, position=mapping.Point(221231.51328988, -35897.102207332), large=False, heli=False,
                airplanes=True, slot_name='37', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=84, position=mapping.Point(221333.29232681, -36099.001191648), large=False, heli=False,
                airplanes=True, slot_name='38', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=85, position=mapping.Point(221358.12499915, -35922.470228533), large=False, heli=False,
                airplanes=True, slot_name='39', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=86, position=mapping.Point(220594.484375, -37063.2734375), large=False, heli=False,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=87, position=mapping.Point(220542.53125, -35204.52734375), large=False, heli=False,
                airplanes=True, slot_name='99', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=88, position=mapping.Point(220626.15625, -35085.046875), large=False, heli=False,
                airplanes=True, slot_name='98', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=89, position=mapping.Point(221444.45708161, -36079.56779594), large=False, heli=False,
                airplanes=True, slot_name='40', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=90, position=mapping.Point(221607.40589841, -35987.160574582), large=False, heli=False,
                airplanes=True, slot_name='41', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=91, position=mapping.Point(221495.73500344, -35839.332156517), large=False, heli=False,
                airplanes=True, slot_name='42', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=92, position=mapping.Point(221678.0450994, -35889.38776017), large=False, heli=False,
                airplanes=True, slot_name='43', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=93, position=mapping.Point(221789.22355717, -35596.662789779), large=False, heli=False,
                airplanes=True, slot_name='46', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=94, position=mapping.Point(221767.93855074, -35481.726175668), large=False, heli=False,
                airplanes=True, slot_name='48', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=95, position=mapping.Point(221609.71011163, -35574.54580749), large=False, heli=False,
                airplanes=True, slot_name='47', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=96, position=mapping.Point(221532.83980768, -35468.178018355), large=False, heli=False,
                airplanes=True, slot_name='49', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=97, position=mapping.Point(221602.72381839, -35303.758874098), large=False, heli=False,
                airplanes=True, slot_name='50', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=98, position=mapping.Point(222195.578125, -34587.5546875), large=False, heli=True,
                airplanes=True, slot_name='60', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=99, position=mapping.Point(220663.640625, -37135.55078125), large=False, heli=False,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=100, position=mapping.Point(220743.921875, -36856.796875), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=101, position=mapping.Point(220743.34375, -37255.38671875), large=False, heli=False,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=102, position=mapping.Point(220645.34375, -37207.28125), large=False, heli=False,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=103, position=mapping.Point(220536.765625, -37350.32421875), large=False, heli=False,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=104, position=mapping.Point(220638.078125, -37388.04296875), large=False, heli=False,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=105, position=mapping.Point(220543.34375, -37464.578125), large=False, heli=False,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=106, position=mapping.Point(220442, -37392.55078125), large=False, heli=False,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=107, position=mapping.Point(220345.09375, -37379.79296875), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=108, position=mapping.Point(220288.9375, -37350.42578125), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=109, position=mapping.Point(220245.8125, -37302.63671875), large=False, heli=False,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=110, position=mapping.Point(220313.546875, -37559.078125), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=111, position=mapping.Point(220630.828125, -36798.72265625), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=112, position=mapping.Point(220606.5, -36725.39453125), large=False, heli=False,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=113, position=mapping.Point(221706.22507888, -33958.722211503), large=False, heli=False,
                airplanes=True, slot_name='73', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=114, position=mapping.Point(221578.47547411, -33891.207376976), large=False, heli=False,
                airplanes=True, slot_name='75', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=115, position=mapping.Point(221590.0334255, -34123.987891279), large=False, heli=False,
                airplanes=True, slot_name='82', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=116, position=mapping.Point(221569.984375, -34066.69140625), large=False, heli=True,
                airplanes=True, slot_name='81', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=117, position=mapping.Point(221567.359375, -34039.6796875), large=False, heli=True,
                airplanes=True, slot_name='79', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=118, position=mapping.Point(221564.40625, -34012.734375), large=False, heli=True,
                airplanes=True, slot_name='78', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=119, position=mapping.Point(220917.1875, -36237.328125), large=False, heli=True,
                airplanes=True, slot_name='53', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=120, position=mapping.Point(220784.734375, -36414.4453125), large=False, heli=True,
                airplanes=True, slot_name='51', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=121, position=mapping.Point(220896.90625, -36357.92578125), large=False, heli=True,
                airplanes=True, slot_name='52', length=78.722809, width=67.096466, height=18.0, shelter=False))


class Jirah(Airport):
    id = 17
    name = "Jirah"
    position = mapping.Point(115359.652344, 187020.734375)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Jirah, self).__init__()

        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(115251.65625, 188431.671875), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(115247.0625, 188456.609375), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(115256.4296875, 188406.671875), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(115233.203125, 188529.59375), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(115237.7109375, 188505.8125), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(115242.3671875, 188480.90625), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(115261.1953125, 188381.796875), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(115274.96875, 188308.09375), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(115269.9921875, 188332.75), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(115265.5078125, 188356.421875), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(115500.3046875, 187918.171875), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(115610.015625, 188144.40625), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(115387.28125, 187936.125), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(114840.78125, 188132.8125), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(114820.4765625, 188414.484375), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(115033.0234375, 187674.25), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(114965.78125, 188002.296875), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(114899.359375, 187879.53125), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(114886.15625, 188621.90625), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(115390.9375, 188318.203125), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(115488.7109375, 187471.15625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(115476.65625, 188641.28125), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(115598.4921875, 188546.25), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(115666.921875, 187660.171875), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(115360.2109375, 188654.09375), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(114970.328125, 188493.078125), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(114916.1015625, 188617.359375), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(115201.296875, 188650.59375), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Khalkhalah(Airport):
    id = 18
    name = "Khalkhalah"
    position = mapping.Point(-218620.25, 56161.078125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Khalkhalah, self).__init__()

        self.runways.append(Runway(250))
        self.runways.append(Runway(330))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-216011.40625, 52803.390625), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-216074.609375, 52836.6171875), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-216043.53125, 52819.75), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-216101.6875, 52853.29296875), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-215989.515625, 52790.5), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-217979.421875, 57278.265625), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-218040, 57041.01171875), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-218062.15625, 57020.7265625), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-217744.34375, 57152.82421875), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-217986.484375, 57307.3515625), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-216192.8125, 52301.66015625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-215750.25, 52284.4140625), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-216059.515625, 52221), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-215903.734375, 52357.25), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-215875.40625, 52365.62109375), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-215613.0625, 52575.140625), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-215737.375, 52689.80078125), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-215851.78125, 52713.32421875), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-218599.375, 53658.76953125), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-215883.9375, 52822.5234375), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-218481.53125, 53551.31640625), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-218571.828125, 53842.35546875), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-218350.890625, 54182.41796875), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-218107.90625, 54165.703125), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-218107.5625, 54195.2109375), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-218563.625, 53813.66796875), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-217911.8125, 57665.0234375), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-218393.625, 54069.0625), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-215878.125, 52726.46484375), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-217932.609375, 57684.0234375), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-217847.1875, 57492.35546875), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-217858.8125, 57466.671875), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-217719.53125, 57668.93359375), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-217712.921875, 57641.23828125), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-217772.625, 57164.00390625), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-218299.40625, 55644.5234375), large=False, heli=True,
                airplanes=False, slot_name='H01', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-218171.015625, 55612.8515625), large=False, heli=True,
                airplanes=False, slot_name='H02', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-218243.9375, 55867.2578125), large=False, heli=True,
                airplanes=False, slot_name='H04', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-218116.484375, 55835.3203125), large=False, heli=True,
                airplanes=False, slot_name='H03', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-218050.8125, 56036.8125), large=False, heli=True,
                airplanes=False, slot_name='H05', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-217920.90625, 56003.7734375), large=False, heli=True,
                airplanes=False, slot_name='H06', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-217996.21875, 56259.5703125), large=False, heli=True,
                airplanes=False, slot_name='H08', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-217864.5, 56225.8515625), large=False, heli=True,
                airplanes=False, slot_name='H07', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-217750.171875, 56622.94140625), large=False, heli=True,
                airplanes=False, slot_name='H09', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-217622.03125, 56589.1796875), large=False, heli=True,
                airplanes=False, slot_name='H10', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-217696.828125, 56844.046875), large=False, heli=True,
                airplanes=False, slot_name='H12', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-217564.34375, 56809.984375), large=False, heli=True,
                airplanes=False, slot_name='H11', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-218250.84375, 53425.7890625), large=False, heli=True,
                airplanes=False, slot_name='H13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-218151.328125, 53375.6328125), large=False, heli=True,
                airplanes=False, slot_name='H14', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-217982.984375, 53285.57421875), large=False, heli=True,
                airplanes=False, slot_name='H15', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(-217891.921875, 53233.8828125), large=False, heli=True,
                airplanes=False, slot_name='H16', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(-217712.625, 53168.71875), large=False, heli=True,
                airplanes=False, slot_name='H17', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(-217634.546875, 53101.13671875), large=False, heli=True,
                airplanes=False, slot_name='H18', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(-217539.90625, 53069.0546875), large=False, heli=True,
                airplanes=False, slot_name='H19', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=58, position=mapping.Point(-217461.09375, 53000.90625), large=False, heli=True,
                airplanes=False, slot_name='H20', length=30.096436, width=23.0, height=10.0, shelter=False))


class King_Hussein_Air_College(Airport):
    id = 19
    name = "King Hussein Air College"
    position = mapping.Point(-296592.405413, 24944.355658)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(King_Hussein_Air_College, self).__init__()

        self.runways.append(Runway(130))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-296638.53473556, 24180.32848277), large=False, heli=True,
                airplanes=True, slot_name='44', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-296668.74881378, 24220.237514344), large=False, heli=True,
                airplanes=True, slot_name='41', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-296649.38969181, 24192.808271592), large=False, heli=True,
                airplanes=True, slot_name='43', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-296657.56131378, 24207.833217469), large=False, heli=True,
                airplanes=True, slot_name='42', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-296577.74881378, 24119.186733094), large=False, heli=True,
                airplanes=True, slot_name='49', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-296537.31131378, 24074.258998719), large=False, heli=True,
                airplanes=True, slot_name='52', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-296551.03006378, 24089.505092469), large=False, heli=True,
                airplanes=True, slot_name='51', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-296564.53006378, 24104.505092469), large=False, heli=True,
                airplanes=True, slot_name='50', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-296604.0114239, 24142.95477655), large=False, heli=True,
                airplanes=True, slot_name='47', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-296589.03006378, 24131.704311219), large=False, heli=True,
                airplanes=True, slot_name='48', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-296629.15216712, 24166.128825637), large=False, heli=True,
                airplanes=True, slot_name='45', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-296617.78818809, 24154.041167605), large=False, heli=True,
                airplanes=True, slot_name='46', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-295961.59375, 23764.876953125), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-296035.96875, 23715.93359375), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-295883.3125, 23814.978515625), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-296011.34375, 23732.806640625), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-295910.46875, 23798.123046875), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-295936.6875, 23781.3671875), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-295986.1875, 23748.37109375), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-297933.97112481, 26085.39973119), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-297853.62104594, 26005.231704819), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-298013.19758872, 26176.240044867), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-298008.27544296, 25395.875449027), large=False, heli=False,
                airplanes=True, slot_name='34', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-296136.49667777, 23596.228672641), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-297987.45798596, 25471.236730109), large=False, heli=False,
                airplanes=True, slot_name='33', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-297767.44966778, 25543.556640625), large=False, heli=False,
                airplanes=True, slot_name='31', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-297782.50243281, 25428.64625618), large=False, heli=False,
                airplanes=True, slot_name='36', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-297730.53761074, 25658.870143357), large=False, heli=False,
                airplanes=True, slot_name='30', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-297910.5241298, 25715.468414813), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-297873.90625, 25830.609375), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-297924.45798596, 25307.497537845), large=False, heli=False,
                airplanes=True, slot_name='35', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-297806.40862481, 25935.712099303), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-297840.4375, 25211.94921875), large=False, heli=False,
                airplanes=True, slot_name='38', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-297704.46208011, 25338.725111856), large=False, heli=False,
                airplanes=True, slot_name='37', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-297761.89352852, 25122.497545509), large=False, heli=False,
                airplanes=True, slot_name='39', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-297952.63080704, 25587.055690232), large=False, heli=False,
                airplanes=True, slot_name='32', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-295941.34375, 23674.439453125), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-295819.07191023, 23633.595176932), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-296122.25, 23996.90234375), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-296159.15486711, 23884.298015472), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-295690.30251845, 23596.532376325), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-295737.98838044, 23716.448777959), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-296008.6324709, 23558.024963619), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-297113.83953047, 26250.561767147), large=False, heli=True,
                airplanes=True, slot_name='21', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-296317.5625, 24213.353515625), large=False, heli=True,
                airplanes=True, slot_name='40', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-297239.13984637, 26143.442253059), large=False, heli=True,
                airplanes=True, slot_name='23', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(-297232.85658389, 26258.429971188), large=False, heli=True,
                airplanes=True, slot_name='22', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(-295341.53125, 24280.47265625), large=False, heli=True,
                airplanes=True, slot_name='18', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(-295459.44976252, 24166.80340192), large=False, heli=True,
                airplanes=True, slot_name='16', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(-295347.96875, 24161.236328125), large=False, heli=True,
                airplanes=True, slot_name='17', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(-297119.25181292, 26136.364902449), large=False, heli=True,
                airplanes=True, slot_name='20', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(-295451.09918875, 24286.377999792), large=False, heli=True,
                airplanes=True, slot_name='19', length=40.0, width=40.0, height=12.0, shelter=False))


class Kiryat_Shmona(Airport):
    id = 20
    name = "Kiryat Shmona"
    position = mapping.Point(-199486.15625, -34500.683594)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Kiryat_Shmona, self).__init__()

        self.runways.append(Runway(210))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-199734.36850518, -34826.638614409), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-199700.22489132, -34799.96031596), large=False, heli=True,
                airplanes=True, slot_name='01', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-199716.36883376, -34813.059689861), large=False, heli=True,
                airplanes=True, slot_name='02', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-199751.51569989, -34841.673689957), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-199866.36008004, -35206.713256411), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))


class Bassel_Al_Assad(Airport):
    id = 21
    name = "Bassel Al-Assad"
    position = mapping.Point(41880.861328, 5656.833496)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Bassel_Al_Assad, self).__init__()

        self.runways.append(Runway(350))
        self.runways.append(Runway(350))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(43002.09375, 5465.603515625), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(43025.1171875, 5465.9375), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(43048.53515625, 5463.6826171875), large=False, heli=True,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(43071.828125, 5463.578125), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(42752.359375, 5383.3286132812), large=False, heli=True,
                airplanes=True, slot_name='05', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(43095.1484375, 5463.3076171875), large=False, heli=True,
                airplanes=True, slot_name='12', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(43118.21875, 5462.6240234375), large=False, heli=True,
                airplanes=True, slot_name='14', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(43142.09765625, 5462.0444335938), large=False, heli=True,
                airplanes=True, slot_name='16', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(43164.859375, 5461.5786132813), large=False, heli=True,
                airplanes=True, slot_name='18', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(42843.66015625, 5142.7290039063), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(43069.46484375, 5385.1118164063), large=False, heli=True,
                airplanes=True, slot_name='11', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(43092.61328125, 5384.4233398438), large=False, heli=True,
                airplanes=True, slot_name='13', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(43139.390625, 5383.173828125), large=False, heli=True,
                airplanes=True, slot_name='17', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(43162.37109375, 5382.5244140625), large=False, heli=True,
                airplanes=True, slot_name='19', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(43187.28125, 5381.8237304688), large=False, heli=True,
                airplanes=True, slot_name='20', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(43212.05078125, 5381.001953125), large=False, heli=True,
                airplanes=True, slot_name='21', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(43235.109375, 5380.4692382813), large=False, heli=True,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(43259.015625, 5379.7275390625), large=False, heli=True,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(42929.23828125, 6348.857421875), large=False, heli=True,
                airplanes=False, slot_name='44', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(42811.34765625, 6410.4047851563), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(42810.08984375, 6374.55078125), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(42809.2421875, 6337.7470703125), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(42808.4140625, 6298.65625), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(42807.34765625, 6259.6547851563), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(42806.12109375, 6218.9838867188), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(42805.26953125, 6179.673828125), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(42803.80859375, 6137.8505859375), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(42803.16015625, 6098.1176757813), large=False, heli=True,
                airplanes=False, slot_name='32', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(43280.63671875, 5898.7133789063), large=False, heli=True,
                airplanes=True, slot_name='26', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(43302.5390625, 5898.7919921875), large=False, heli=True,
                airplanes=True, slot_name='25', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(43325.046875, 5898.7919921875), large=False, heli=True,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(42633.39453125, 5368.357421875), large=False, heli=True,
                airplanes=True, slot_name='03', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(42596.269256892, 6145.3646321182), large=False, heli=True,
                airplanes=True, slot_name='29', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(42672.96316446, 6143.9422912475), large=False, heli=True,
                airplanes=True, slot_name='28', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(42518.586998622, 6146.2915866218), large=False, heli=True,
                airplanes=True, slot_name='30', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(42439.484228404, 6146.9443134145), large=False, heli=True,
                airplanes=True, slot_name='31', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(42360.345092717, 6147.609166584), large=False, heli=True,
                airplanes=True, slot_name='32', length=78.722809, width=67.096466, height=18.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(43115.62109375, 5383.8115234375), large=False, heli=True,
                airplanes=True, slot_name='15', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(42518.8515625, 5371.0561523438), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(42634.25390625, 5417.1015625), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(42520.1875, 5418.8720703125), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(42927.828125, 6270.6494140625), large=False, heli=True,
                airplanes=False, slot_name='43', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(42925.5703125, 6191.8510742188), large=False, heli=True,
                airplanes=False, slot_name='42', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(42923.68359375, 6111.470703125), large=False, heli=True,
                airplanes=False, slot_name='41', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=48, position=mapping.Point(43098.953125, 6175.123046875), large=False, heli=True,
                airplanes=False, slot_name='50', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=49, position=mapping.Point(43100.83984375, 6255.427734375), large=False, heli=True,
                airplanes=False, slot_name='51', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=50, position=mapping.Point(43102.625, 6336.0385742188), large=False, heli=True,
                airplanes=False, slot_name='52', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=51, position=mapping.Point(43123.37109375, 6467.474609375), large=False, heli=True,
                airplanes=False, slot_name='53', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=52, position=mapping.Point(42987.2265625, 6474.1025390625), large=False, heli=True,
                airplanes=False, slot_name='49', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=53, position=mapping.Point(43004.6953125, 6373.3154296875), large=False, heli=True,
                airplanes=False, slot_name='48', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=54, position=mapping.Point(43003.1953125, 6297.884765625), large=False, heli=True,
                airplanes=False, slot_name='47', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=55, position=mapping.Point(43002.01171875, 6219.3071289063), large=False, heli=True,
                airplanes=False, slot_name='46', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=56, position=mapping.Point(42998.87890625, 6141.4501953125), large=False, heli=True,
                airplanes=False, slot_name='45', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=57, position=mapping.Point(43258.43359375, 5898.2568359375), large=False, heli=True,
                airplanes=True, slot_name='27', length=20.5, width=14.5, height=8.0, shelter=False))


class Marj_as_Sultan_North(Airport):
    id = 22
    name = "Marj as Sultan North"
    position = mapping.Point(-170245.078125, 47500.599609)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Marj_as_Sultan_North, self).__init__()

        self.runways.append(Runway(260))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-170310.71875, 47426.27734375), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-170281.296875, 47602.125), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-170234.984375, 47371.68359375), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-170108.171875, 47430.20703125), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-170153.375, 47438.53515625), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-170197.75, 47446.05078125), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-170167.578125, 47621.31640625), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-170180.875, 47544.80859375), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-170136.359375, 47536.38671875), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-170188.890625, 47496.6328125), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-170302.75, 47470.953125), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-170295.5, 47514.87890625), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-170288.609375, 47557.875), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-170091.296875, 47529.609375), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))


class Marj_Ruhayyil(Airport):
    id = 23
    name = "Marj Ruhayyil"
    position = mapping.Point(-194233.65625, 46043.966797)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Marj_Ruhayyil, self).__init__()

        self.runways.append(Runway(240))
        self.runways.append(Runway(240))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-194252.22073458, 44232.854627202), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-194282.21875, 44230.59375), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-194587.85030673, 44375.688341548), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-194605.65625, 44400.29296875), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-194124.6144741, 44277.470482914), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-194099.36093226, 44293.888451664), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-194128.546875, 44531.359375), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-194100.22905998, 44540.388561179), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-194480.765625, 44791.16796875), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-194556.609375, 44841.984375), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-194976.140625, 44895.94921875), large=False, heli=False,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-194908.75, 45020.33984375), large=False, heli=False,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-195966.953125, 44616.890625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-195829.390625, 44794.6484375), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-195804, 44903.04296875), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-193736.65625, 47612.9921875), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-193710.59375, 47741.5390625), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-193616.88251101, 47589.723460219), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-193603.15627271, 47617.047460996), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-193324.25, 47615.77734375), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-193352.51276164, 47604.823326873), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-193307.015625, 47385.1328125), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-193221, 47472.08984375), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-192887.953125, 47039.421372519), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-192876.48304601, 47011.156093145), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-192748.25, 47334.640625), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-192731.89263809, 47309.126080949), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-193774.671875, 47135.82421875), large=False, heli=True,
                airplanes=False, slot_name='33', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-193754.9375, 47177.62109375), large=False, heli=True,
                airplanes=False, slot_name='32', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-193737, 47214.8984375), large=False, heli=True,
                airplanes=False, slot_name='31', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-193716.78125, 47258.140625), large=False, heli=True,
                airplanes=False, slot_name='30', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-193698.015625, 47295.05078125), large=False, heli=True,
                airplanes=False, slot_name='29', length=42.0, width=34.0, height=14.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-193679.28125, 47335.83203125), large=False, heli=True,
                airplanes=False, slot_name='28', length=42.0, width=34.0, height=14.0, shelter=False))


class Megiddo(Airport):
    id = 24
    name = "Megiddo"
    position = mapping.Point(-266965.015625, -71068.832031)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Megiddo, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-266866.625, -70705.734375), large=False, heli=True,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-266846.3125, -70716.65625), large=False, heli=True,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-266827.6875, -70726.078125), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-266806.90625, -70738.5625), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-266786.25, -70749.25), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-266767.5625, -70758.78125), large=False, heli=True,
                airplanes=True, slot_name='03', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-266966.90625, -72310.21875), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-266966.875, -72279.890625), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-267257.4375, -70506.171875), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-266798.84375, -70053.90625), large=False, heli=True,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))


class Mezzeh(Airport):
    id = 25
    name = "Mezzeh"
    position = mapping.Point(-172160.445313, 24865.664062)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Mezzeh, self).__init__()

        self.runways.append(Runway(60))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-171953.0625, 25448.78515625), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-171989.578125, 25521.158203125), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-172004.65625, 25550.392578125), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-172004.78125, 24883.3046875), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-171606.0625, 26258.939453125), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-171359.1875, 26056.25390625), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-171343.921875, 26082.5703125), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-171956.21875, 26037.05859375), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-171618.53125, 25034.962890625), large=False, heli=True,
                airplanes=True, slot_name='12', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-171582.265625, 25078.34375), large=False, heli=True,
                airplanes=True, slot_name='13', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-172922.21875, 23871.599609375), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-172891.4375, 23873.232421875), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-172511.296875, 23612.494140625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-172528.015625, 23638.748046875), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-171630.921875, 26241.953125), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-172090.234375, 24730.0703125), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-172219.59375, 24488.287109375), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-172321.125, 24304.59375), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-172387.5, 24179.16796875), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-172467.09375, 24034.333984375), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-172558.390625, 23857.443359375), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-171426.265625, 25749.81640625), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Minakh(Airport):
    id = 26
    name = "Minakh"
    position = mapping.Point(163697.53125, 107430.601563)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Minakh, self).__init__()

        self.runways.append(Runway(280))
        self.runways.append(Runway(220))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(163441.609375, 107169.1953125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(163441.5625, 107195.296875), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(163441.953125, 107221.609375), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(163442.640625, 107245.7890625), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(163443.40625, 107271.015625), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(163443.890625, 107297.15625), large=False, heli=True,
                airplanes=True, slot_name='02', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(163444.09375, 107322.8359375), large=False, heli=True,
                airplanes=True, slot_name='01', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(163823.41331683, 107561.65390968), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(164023.65159003, 107455.22314563), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(164209.609375, 107547.2109375), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(163979.53125, 107607.203125), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(163788.18472768, 107747.93011305), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(163994.65625, 106824.8671875), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(164045.59375, 106890.6015625), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(164059, 106980.21875), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(164090.34375, 107040.0546875), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(164161.625, 107118.53125), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(164225.234375, 107165.0859375), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(164255.4375, 107237.421875), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(164248.953125, 107324.3359375), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.096436, width=23.0, height=10.0, shelter=False))


class Aleppo(Airport):
    id = 27
    name = "Aleppo"
    position = mapping.Point(125576.863281, 123125.304688)
    tacan = None
    unit_zones = []
    civilian = True
    slot_version = 2

    def __init__(self):
        super(Aleppo, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(125126.828125, 124845.09375), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(125262.703125, 124155), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(125252.3125, 124267.0703125), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(125223.34375, 124425.1640625), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(125429.6640625, 122696.0234375), large=False, heli=True,
                airplanes=False, slot_name='H01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(125324.71875, 122681.640625), large=False, heli=True,
                airplanes=False, slot_name='H02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(125937.7890625, 123365.9921875), large=False, heli=True,
                airplanes=True, slot_name='03', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(125904.6328125, 123406.4609375), large=False, heli=True,
                airplanes=True, slot_name='04', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(125902.96875, 123620.9296875), large=False, heli=True,
                airplanes=True, slot_name='07', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(125833.09375, 123609.1484375), large=False, heli=True,
                airplanes=True, slot_name='08', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(125913.09375, 123507.28125), large=False, heli=True,
                airplanes=True, slot_name='06', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(125908.5859375, 123454.203125), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(125924.7734375, 123291.3828125), large=False, heli=True,
                airplanes=True, slot_name='02', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(125960.640625, 123249.3671875), large=False, heli=True,
                airplanes=True, slot_name='01', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(125219.8203125, 124455.78125), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(125211.1640625, 124628.28125), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(125318.1875, 122730.7421875), large=False, heli=True,
                airplanes=False, slot_name='H04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(125311.09375, 122779.3359375), large=False, heli=True,
                airplanes=False, slot_name='H06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(125305.0703125, 122828.0234375), large=False, heli=True,
                airplanes=False, slot_name='H08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(125422.765625, 122744.5625), large=False, heli=True,
                airplanes=False, slot_name='H03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(125416.109375, 122793.140625), large=False, heli=True,
                airplanes=False, slot_name='H05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(125409.2890625, 122841.6875), large=False, heli=True,
                airplanes=False, slot_name='H07', length=30.096436, width=23.0, height=10.0, shelter=False))


class Palmyra(Airport):
    id = 28
    name = "Palmyra"
    position = mapping.Point(-55704.023438, 220114.742188)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Palmyra, self).__init__()

        self.runways.append(Runway(80))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-55613.91796875, 218666.296875), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-55610.5625, 218694.875), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-55602.03515625, 218886.8125), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-55601.4453125, 219086.21875), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-55414.0703125, 219271.609375), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-55409.51171875, 219314.265625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-55405.26171875, 219356.703125), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-55401.2265625, 219401.453125), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-55316.3671875, 220228.953125), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-55119.5234375, 220463.5), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-55069.37109375, 220724.34375), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-55214.5703125, 221011.34375), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-55395.75, 221064.671875), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-55380.3359375, 221201.484375), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-55315.9765625, 221317.578125), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-55092.93359375, 221375.953125), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-55338.85546875, 221494.04272633), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-55336.21875, 221523.515625), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-55402.53515625, 221434.53125), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-55398.62109375, 221469.734375), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-55155.953125, 221746.0625), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-55353.92578125, 221646.18611711), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Qabr_as_Sitt(Airport):
    id = 29
    name = "Qabr as Sitt"
    position = mapping.Point(-174594.53125, 37227.242188)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Qabr_as_Sitt, self).__init__()

        self.runways.append(Runway(60))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-174752.078125, 37094.52734375), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-174729.96875, 37178.1953125), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-174711.93532459, 37236.404717206), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-174572.140625, 37409.44921875), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-174493.796875, 37202.13671875), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-174534.328125, 37068.0546875), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-174553.125, 36989.44921875), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-174627.015625, 36981.359375), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-174636.109375, 37033.96875), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))


class Ramat_David(Airport):
    id = 30
    name = "Ramat David"
    position = mapping.Point(-259102.148438, -75789.410156)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Ramat_David, self).__init__()

        self.runways.append(Runway(270))
        self.runways.append(Runway(330))
        self.runways.append(Runway(290))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-258930.734375, -75766.90625), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-258932.140625, -75743.578125), large=False, heli=False,
                airplanes=True, slot_name='10', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-258930.796875, -75719.90625), large=False, heli=False,
                airplanes=True, slot_name='09', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-258929.90625, -75696.2734375), large=False, heli=False,
                airplanes=True, slot_name='08', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-258928.78125, -75672.6484375), large=False, heli=False,
                airplanes=True, slot_name='07', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-258810.734375, -74591.734375), large=False, heli=True,
                airplanes=True, slot_name='36', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-258826.5625, -74570.46875), large=False, heli=True,
                airplanes=True, slot_name='35', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-258841.953125, -74549.3984375), large=False, heli=True,
                airplanes=True, slot_name='34', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-258858.09375, -74527.859375), large=False, heli=True,
                airplanes=True, slot_name='33', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(-258874.15625, -74506.3671875), large=False, heli=True,
                airplanes=True, slot_name='32', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(-258823.734375, -76847.8515625), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(-258840.78125, -76822.9375), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(-258360.25, -75909.640625), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(-259885.6875, -74320.171875), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(-259533.484375, -74288.078125), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(-259300.515625, -74383.796875), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(-259876.203125, -74352.4375), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(-259535.546875, -74323.1484375), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(-259322.9375, -74411.09375), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(-258892.765625, -74483.3046875), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(-258909.015625, -74462.171875), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(-258390.265625, -76228.5), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(-258415.015625, -76203.28125), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(-258394.84375, -75913.296875), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(-259974.390625, -74785.5390625), large=False, heli=False,
                airplanes=True, slot_name='19', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(-259999.734375, -74810.140625), large=False, heli=False,
                airplanes=True, slot_name='18', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(-259545.140625, -75441.2265625), large=False, heli=False,
                airplanes=True, slot_name='14', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(-259567.296875, -75468.484375), large=False, heli=False,
                airplanes=True, slot_name='15', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(-259785.734375, -75052.375), large=False, heli=False,
                airplanes=True, slot_name='16', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(-259802.671875, -75081.9375), large=False, heli=False,
                airplanes=True, slot_name='17', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(-259277.3125, -75543.53125), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(-259269.875, -75576.8046875), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(-258770.671875, -75184.9765625), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(-258768.96875, -75157.6640625), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(-258767.25, -75131.9453125), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(-258765.4375, -75105.796875), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(-258763.65625, -75079.7734375), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(-259959.90625, -74257.859375), large=False, heli=False,
                airplanes=True, slot_name='22', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(-259939.59375, -74245.90625), large=False, heli=False,
                airplanes=True, slot_name='23', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(-259919.5, -74234.0546875), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(-259878.703125, -74210.5703125), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(-259899.421875, -74221.828125), large=False, heli=False,
                airplanes=True, slot_name='24', length=20.5, width=14.5, height=8.0, shelter=False))


class Kuweires(Airport):
    id = 31
    name = "Kuweires"
    position = mapping.Point(125810.890625, 155253.8125)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Kuweires, self).__init__()

        self.runways.append(Runway(280))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(125533.8359375, 154375.15625), large=False, heli=True,
                airplanes=True, slot_name='31', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(125528.4296875, 154402.171875), large=False, heli=True,
                airplanes=True, slot_name='30', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(125523.1640625, 154429.421875), large=False, heli=True,
                airplanes=True, slot_name='29', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(125518.0078125, 154456.515625), large=False, heli=True,
                airplanes=True, slot_name='28', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(125512.703125, 154483.703125), large=False, heli=True,
                airplanes=True, slot_name='27', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(125507.5078125, 154510.890625), large=False, heli=True,
                airplanes=True, slot_name='26', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(125502.1328125, 154537.90625), large=False, heli=True,
                airplanes=True, slot_name='25', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(125496.78125, 154565.234375), large=False, heli=True,
                airplanes=True, slot_name='24', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(125491.609375, 154592.265625), large=False, heli=True,
                airplanes=True, slot_name='23', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(125486.3984375, 154619.40625), large=False, heli=True,
                airplanes=True, slot_name='22', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(125438.953125, 154863.765625), large=False, heli=True,
                airplanes=True, slot_name='13', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(125433.6484375, 154890.953125), large=False, heli=True,
                airplanes=True, slot_name='12', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(125454.75, 154782.40625), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(125449.40625, 154809.4375), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(125444.171875, 154836.71875), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(125470.640625, 154700.9375), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(125465.4296875, 154728.03125), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(125460.0859375, 154755.1875), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(125475.7734375, 154673.6875), large=False, heli=True,
                airplanes=True, slot_name='20', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(125481.0625, 154646.59375), large=False, heli=True,
                airplanes=True, slot_name='21', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(125868.921875, 154054.40625), large=False, heli=True,
                airplanes=True, slot_name='32', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(125887.0234375, 154058.84375), large=False, heli=True,
                airplanes=True, slot_name='33', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(125904.7578125, 154062.578125), large=False, heli=True,
                airplanes=True, slot_name='34', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(125923.171875, 154066.25), large=False, heli=True,
                airplanes=True, slot_name='35', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(125941.09375, 154069.296875), large=False, heli=True,
                airplanes=True, slot_name='36', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(125959.3984375, 154072.71875), large=False, heli=True,
                airplanes=True, slot_name='37', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(125225.8125, 156555.96875), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(125226.9375, 156585.71875), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(125679.140625, 156731.375), large=False, heli=False,
                airplanes=True, slot_name='09', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(125792.4375, 156752.140625), large=False, heli=False,
                airplanes=True, slot_name='08', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(125922.671875, 156113.546875), large=False, heli=False,
                airplanes=True, slot_name='07', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(126393.15625, 155059.515625), large=False, heli=False,
                airplanes=True, slot_name='06', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(126338.3984375, 154689.5625), large=False, heli=False,
                airplanes=True, slot_name='05', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(126128.96875, 154563.75), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(126182.2421875, 154301.9375), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(126242.4140625, 154137.96875), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(126275.84375, 154017.4375), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Rayak(Airport):
    id = 32
    name = "Rayak"
    position = mapping.Point(-130132.492188, 4053.336304)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Rayak, self).__init__()

        self.runways.append(Runway(220))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-129373.9453125, 5490.4599609375), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-129356.2734375, 5509.322265625), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-129338.859375, 5527.9926757812), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-129321.265625, 5546.7426757813), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-129275.3125, 5484.6723632813), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-129291.9921875, 5465.0029296875), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-129309.4140625, 5445.9350585937), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-129326.6015625, 5427.5703125), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-129417.609375, 5385.3833007813), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-129437.25, 5364.3862304688), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-129412.0078125, 5439.1123046875), large=False, heli=True,
                airplanes=True, slot_name='04', length=40.0, width=40.0, height=12.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-129473.09375, 5325.6313476562), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))


class Rene_Mouawad(Airport):
    id = 33
    name = "Rene Mouawad"
    position = mapping.Point(-48306.007813, 8690.693604)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Rene_Mouawad, self).__init__()

        self.runways.append(Runway(240))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-47948.4140625, 8702.654296875), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-47964.61328125, 8671.2744140625), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-47900.51171875, 8797.40234375), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-47917.640625, 8766.47265625), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(-47933.48828125, 8734.7802734375), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(-47979.92578125, 8642.92578125), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(-47885.35546875, 8829.9736328125), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(-47869.05859375, 8861.5), large=False, heli=True,
                airplanes=True, slot_name='10', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(-47852.80078125, 8893.1640625), large=False, heli=True,
                airplanes=True, slot_name='11', length=26.0, width=24.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(-48921.453125, 7167.7524414062), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(-48860.46875, 7303.2216796875), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(-47529.86328125, 9976.3935546875), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(-47367.125, 9996.330078125), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))


class Tabqa(Airport):
    id = 37
    name = "Tabqa"
    position = mapping.Point(76964.6875, 243605.21875)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Tabqa, self).__init__()

        self.runways.append(Runway(270))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(77222.4296875, 244747.015625), large=False, heli=False,
                airplanes=True, slot_name='13', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(77359.6171875, 245047.609375), large=False, heli=False,
                airplanes=True, slot_name='21', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(77244.84375, 244727.25), large=False, heli=False,
                airplanes=True, slot_name='12', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(77246.140625, 245090.09375), large=False, heli=False,
                airplanes=True, slot_name='22', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(77246.4921875, 245120.5), large=False, heli=False,
                airplanes=True, slot_name='23', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(77351.390625, 242655.375), large=False, heli=False,
                airplanes=True, slot_name='11', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(77196.5703125, 245305.875), large=False, heli=False,
                airplanes=True, slot_name='27', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(77352.125, 242625.46875), large=False, heli=False,
                airplanes=True, slot_name='10', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(77350, 245283.40625), large=False, heli=False,
                airplanes=True, slot_name='24', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(77607.1328125, 242237.953125), large=False, heli=False,
                airplanes=True, slot_name='04', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(77463.59375, 242046.578125), large=False, heli=False,
                airplanes=True, slot_name='03', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(77408.875, 245447.734375), large=False, heli=False,
                airplanes=True, slot_name='25', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(77385.1875, 241958.71875), large=False, heli=False,
                airplanes=True, slot_name='02', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(77285.9296875, 245521.359375), large=False, heli=False,
                airplanes=True, slot_name='26', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(77370.390625, 241932.171875), large=False, heli=False,
                airplanes=True, slot_name='01', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(76687.8125, 245209.546875), large=False, heli=False,
                airplanes=True, slot_name='29', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(76707.078125, 245232.828125), large=False, heli=False,
                airplanes=True, slot_name='28', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(77407.8046875, 242174.21875), large=False, heli=True,
                airplanes=True, slot_name='05', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(77406.09375, 242210.265625), large=False, heli=True,
                airplanes=True, slot_name='06', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(77404.4140625, 242244.046875), large=False, heli=True,
                airplanes=True, slot_name='07', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(77428.3984375, 244914.796875), large=False, heli=False,
                airplanes=True, slot_name='20', length=18.449999, width=13.049999, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(77402.2109375, 242277.921875), large=False, heli=True,
                airplanes=True, slot_name='08', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(77400.1640625, 242313.09375), large=False, heli=True,
                airplanes=True, slot_name='09', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(77169.578125, 244860.671875), large=False, heli=True,
                airplanes=True, slot_name='14', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(77167.7265625, 244890.484375), large=False, heli=True,
                airplanes=True, slot_name='15', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(77165.5859375, 244920.59375), large=False, heli=True,
                airplanes=True, slot_name='16', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(77163.546875, 244951.046875), large=False, heli=True,
                airplanes=True, slot_name='17', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(77162.46875, 244980.015625), large=False, heli=True,
                airplanes=True, slot_name='18', length=26.0, width=22.0, height=11.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(77161.1328125, 245007.25), large=False, heli=True,
                airplanes=True, slot_name='19', length=26.0, width=22.0, height=11.0, shelter=False))


class Taftanaz(Airport):
    id = 38
    name = "Taftanaz"
    position = mapping.Point(103485.984375, 82766.667969)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Taftanaz, self).__init__()

        self.runways.append(Runway(100))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(103153.359375, 82645.1953125), large=False, heli=True,
                airplanes=False, slot_name='17', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(103122.875, 82555.2109375), large=False, heli=True,
                airplanes=False, slot_name='18', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(103196.7890625, 82495.8671875), large=False, heli=True,
                airplanes=False, slot_name='19', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(103244.46875, 82597.109375), large=False, heli=True,
                airplanes=False, slot_name='20', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(103101.71875, 82386.3828125), large=False, heli=True,
                airplanes=False, slot_name='14', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(103078.6171875, 82483.9921875), large=False, heli=True,
                airplanes=False, slot_name='15', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=6, position=mapping.Point(102969.3671875, 82480.1484375), large=False, heli=True,
                airplanes=False, slot_name='13', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=7, position=mapping.Point(103028.59375, 82565.40625), large=False, heli=True,
                airplanes=False, slot_name='16', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=8, position=mapping.Point(102883.828125, 82596.4609375), large=False, heli=True,
                airplanes=False, slot_name='08', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=9, position=mapping.Point(102966.2109375, 82670.1015625), large=False, heli=True,
                airplanes=False, slot_name='05', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=10, position=mapping.Point(102878.8515625, 82433.8828125), large=False, heli=True,
                airplanes=False, slot_name='12', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=11, position=mapping.Point(102944.9140625, 82367.8828125), large=False, heli=True,
                airplanes=False, slot_name='11', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=12, position=mapping.Point(102970.3515625, 82271.078125), large=False, heli=True,
                airplanes=False, slot_name='10', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=13, position=mapping.Point(102860.5078125, 82323.1171875), large=False, heli=True,
                airplanes=False, slot_name='09', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=14, position=mapping.Point(102818.1875, 82664.875), large=False, heli=True,
                airplanes=False, slot_name='07', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=15, position=mapping.Point(102868.484375, 82738.84375), large=False, heli=True,
                airplanes=False, slot_name='06', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=16, position=mapping.Point(103054.9375, 82883.15625), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=17, position=mapping.Point(103139.859375, 82959.328125), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=18, position=mapping.Point(103128.59375, 82819.5390625), large=False, heli=True,
                airplanes=False, slot_name='04', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=19, position=mapping.Point(103203.8515625, 82889.1484375), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=20, position=mapping.Point(103301.671875, 82724.296875), large=False, heli=True,
                airplanes=False, slot_name='21', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=21, position=mapping.Point(103337.5, 82817.8046875), large=False, heli=True,
                airplanes=False, slot_name='24', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=22, position=mapping.Point(103414.6171875, 82785.03125), large=False, heli=True,
                airplanes=False, slot_name='23', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=23, position=mapping.Point(103384.9296875, 82692.171875), large=False, heli=True,
                airplanes=False, slot_name='22', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=24, position=mapping.Point(103351.03125, 82567.734375), large=False, heli=True,
                airplanes=False, slot_name='25', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=25, position=mapping.Point(103338.921875, 82465.53125), large=False, heli=True,
                airplanes=False, slot_name='26', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=26, position=mapping.Point(103417.484375, 82449.078125), large=False, heli=True,
                airplanes=False, slot_name='27', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=27, position=mapping.Point(103455.703125, 82541.296875), large=False, heli=True,
                airplanes=False, slot_name='28', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=28, position=mapping.Point(103318.25, 82286.5078125), large=False, heli=True,
                airplanes=False, slot_name='31', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=29, position=mapping.Point(103391.140625, 82343.390625), large=False, heli=True,
                airplanes=False, slot_name='30', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=30, position=mapping.Point(103473.765625, 82275.6875), large=False, heli=True,
                airplanes=False, slot_name='32', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=31, position=mapping.Point(103481.203125, 82380.7109375), large=False, heli=True,
                airplanes=False, slot_name='29', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=32, position=mapping.Point(103377.71875, 82049.65625), large=False, heli=True,
                airplanes=False, slot_name='34', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=33, position=mapping.Point(103472.140625, 82072.25), large=False, heli=True,
                airplanes=False, slot_name='35', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=34, position=mapping.Point(103492.9296875, 82195.796875), large=False, heli=True,
                airplanes=False, slot_name='33', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=35, position=mapping.Point(103558.625, 82118.609375), large=False, heli=True,
                airplanes=False, slot_name='36', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=36, position=mapping.Point(103687.8203125, 82244.6328125), large=False, heli=True,
                airplanes=False, slot_name='37', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=37, position=mapping.Point(103650.734375, 82344.84375), large=False, heli=True,
                airplanes=False, slot_name='40', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=38, position=mapping.Point(103750.71875, 82325.4765625), large=False, heli=True,
                airplanes=False, slot_name='39', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=39, position=mapping.Point(103766.1875, 82232.3671875), large=False, heli=True,
                airplanes=False, slot_name='38', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=40, position=mapping.Point(103633.375, 82499.390625), large=False, heli=True,
                airplanes=False, slot_name='41', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=41, position=mapping.Point(103724.3984375, 82534.6796875), large=False, heli=True,
                airplanes=False, slot_name='42', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=42, position=mapping.Point(103673.234375, 82638.078125), large=False, heli=True,
                airplanes=False, slot_name='43', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=43, position=mapping.Point(103593.5390625, 82591.7890625), large=False, heli=True,
                airplanes=False, slot_name='44', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=44, position=mapping.Point(103575.0703125, 82708.328125), large=False, heli=True,
                airplanes=False, slot_name='45', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=45, position=mapping.Point(103555.0703125, 82804.59375), large=False, heli=True,
                airplanes=False, slot_name='48', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=46, position=mapping.Point(103649.953125, 82860.0859375), large=False, heli=True,
                airplanes=False, slot_name='47', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=47, position=mapping.Point(103681.734375, 82764.34375), large=False, heli=True,
                airplanes=False, slot_name='46', length=30.096436, width=23.0, height=10.0, shelter=False))


class Wujah_Al_Hajar(Airport):
    id = 40
    name = "Wujah Al Hajar"
    position = mapping.Point(-81524.375, -22832.533203)
    tacan = None
    unit_zones = []
    civilian = False
    slot_version = 2

    def __init__(self):
        super(Wujah_Al_Hajar, self).__init__()

        self.runways.append(Runway(20))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=0, position=mapping.Point(-81061.453125, -22970.05078125), large=False, heli=True,
                airplanes=True, slot_name='04', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=1, position=mapping.Point(-81146.743434093, -22962.737692383), large=False, heli=True,
                airplanes=False, slot_name='01', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=2, position=mapping.Point(-81133.187367034, -22987.014084215), large=False, heli=True,
                airplanes=False, slot_name='02', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=3, position=mapping.Point(-81113.930704375, -23006.491492389), large=False, heli=True,
                airplanes=False, slot_name='03', length=30.096436, width=23.0, height=10.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=4, position=mapping.Point(-81073.328125, -22949.078125), large=False, heli=True,
                airplanes=True, slot_name='05', length=20.5, width=14.5, height=8.0, shelter=False))
        self.parking_slots.append(ParkingSlot(
                crossroad_idx=5, position=mapping.Point(-81086.0234375, -22926.443359375), large=False, heli=True,
                airplanes=True, slot_name='06', length=20.5, width=14.5, height=8.0, shelter=False))


class Syria(Terrain):
    center = {"lat": 35.021, "long": 35.901}
    bounds = mapping.Rectangle(-320000, -579986, 300000, 579998)
    map_view_default = MapView(bounds.center(), 1000000)
    city_graph = None
    temperature = [
        (2, 8),
        (3, 11),
        (6, 15),
        (10, 21),
        (15, 27),
        (18, 32),
        (22, 35),
        (22, 35),
        (19, 32),
        (14, 26),
        (7, 17),
        (4, 10)
    ]
    assert (len(temperature) == 12)

    def __init__(self):
        super(Syria, self).__init__("Syria")
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports['Abu al-Duhur'] = Abu_al_Duhur()
        self.airports['Adana Sakirpasa'] = Adana_Sakirpasa()
        self.airports['Al Qusayr'] = Al_Qusayr()
        self.airports['An Nasiriyah'] = An_Nasiriyah()
        self.airports['Beirut-Rafic Hariri'] = Beirut_Rafic_Hariri()
        self.airports['Damascus'] = Damascus()
        self.airports['Marj as Sultan South'] = Marj_as_Sultan_South()
        self.airports['Al-Dumayr'] = Al_Dumayr()
        self.airports['Eyn Shemer'] = Eyn_Shemer()
        self.airports['Haifa'] = Haifa()
        self.airports['Hama'] = Hama()
        self.airports['Hatay'] = Hatay()
        self.airports['Incirlik'] = Incirlik()
        self.airports['Jirah'] = Jirah()
        self.airports['Khalkhalah'] = Khalkhalah()
        self.airports['King Hussein Air College'] = King_Hussein_Air_College()
        self.airports['Kiryat Shmona'] = Kiryat_Shmona()
        self.airports['Bassel Al-Assad'] = Bassel_Al_Assad()
        self.airports['Marj as Sultan North'] = Marj_as_Sultan_North()
        self.airports['Marj Ruhayyil'] = Marj_Ruhayyil()
        self.airports['Megiddo'] = Megiddo()
        self.airports['Mezzeh'] = Mezzeh()
        self.airports['Minakh'] = Minakh()
        self.airports['Aleppo'] = Aleppo()
        self.airports['Palmyra'] = Palmyra()
        self.airports['Qabr as Sitt'] = Qabr_as_Sitt()
        self.airports['Ramat David'] = Ramat_David()
        self.airports['Kuweires'] = Kuweires()
        self.airports['Rayak'] = Rayak()
        self.airports['Rene Mouawad'] = Rene_Mouawad()
        self.airports['Tabqa'] = Tabqa()
        self.airports['Taftanaz'] = Taftanaz()
        self.airports['Wujah Al Hajar'] = Wujah_Al_Hajar()

    def abu_al_duhur(self) -> Airport:
        return self.airports["Abu al-Duhur"]

    def adana_sakirpasa(self) -> Airport:
        return self.airports["Adana Sakirpasa"]

    def al_qusayr(self) -> Airport:
        return self.airports["Al Qusayr"]

    def an_nasiriyah(self) -> Airport:
        return self.airports["An Nasiriyah"]

    def beirut_rafic_hariri(self) -> Airport:
        return self.airports["Beirut-Rafic Hariri"]

    def damascus(self) -> Airport:
        return self.airports["Damascus"]

    def marj_as_sultan_south(self) -> Airport:
        return self.airports["Marj as Sultan South"]

    def al_dumayr(self) -> Airport:
        return self.airports["Al-Dumayr"]

    def eyn_shemer(self) -> Airport:
        return self.airports["Eyn Shemer"]

    def haifa(self) -> Airport:
        return self.airports["Haifa"]

    def hama(self) -> Airport:
        return self.airports["Hama"]

    def hatay(self) -> Airport:
        return self.airports["Hatay"]

    def incirlik(self) -> Airport:
        return self.airports["Incirlik"]

    def jirah(self) -> Airport:
        return self.airports["Jirah"]

    def khalkhalah(self) -> Airport:
        return self.airports["Khalkhalah"]

    def king_hussein_air_college(self) -> Airport:
        return self.airports["King Hussein Air College"]

    def kiryat_shmona(self) -> Airport:
        return self.airports["Kiryat Shmona"]

    def bassel_al_assad(self) -> Airport:
        return self.airports["Bassel Al-Assad"]

    def marj_as_sultan_north(self) -> Airport:
        return self.airports["Marj as Sultan North"]

    def marj_ruhayyil(self) -> Airport:
        return self.airports["Marj Ruhayyil"]

    def megiddo(self) -> Airport:
        return self.airports["Megiddo"]

    def mezzeh(self) -> Airport:
        return self.airports["Mezzeh"]

    def minakh(self) -> Airport:
        return self.airports["Minakh"]

    def aleppo(self) -> Airport:
        return self.airports["Aleppo"]

    def palmyra(self) -> Airport:
        return self.airports["Palmyra"]

    def qabr_as_sitt(self) -> Airport:
        return self.airports["Qabr as Sitt"]

    def ramat_david(self) -> Airport:
        return self.airports["Ramat David"]

    def kuweires(self) -> Airport:
        return self.airports["Kuweires"]

    def rayak(self) -> Airport:
        return self.airports["Rayak"]

    def rene_mouawad(self) -> Airport:
        return self.airports["Rene Mouawad"]

    def tabqa(self) -> Airport:
        return self.airports["Tabqa"]

    def taftanaz(self) -> Airport:
        return self.airports["Taftanaz"]

    def wujah_al_hajar(self) -> Airport:
        return self.airports["Wujah Al Hajar"]