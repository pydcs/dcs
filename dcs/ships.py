# This file is generated from pydcs_export.lua

import dcs.unittype as unittype


class Speedboat(unittype.ShipType):
    id = "speedboat"
    name = "Boat Armed Hi-speed"
    detection_range = 5000
    threat_range = 1000
    air_weapon_dist = 1000


class VINSON(unittype.ShipType):
    id = "VINSON"
    name = "CVN-70 Carl Vinson"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 30000
    threat_range = 15000
    air_weapon_dist = 15000


class PERRY(unittype.ShipType):
    id = "PERRY"
    name = "FFG Oliver Hazard Perry"
    helicopter_num = 2
    parking = 1
    detection_range = 150000
    threat_range = 100000
    air_weapon_dist = 100000


class TICONDEROG(unittype.ShipType):
    id = "TICONDEROG"
    name = "CG Ticonderoga"
    helicopter_num = 2
    parking = 1
    detection_range = 150000
    threat_range = 100000
    air_weapon_dist = 100000


class ALBATROS(unittype.ShipType):
    id = "ALBATROS"
    name = "Corvette 1124.4 Grisha"
    detection_range = 30000
    threat_range = 16000
    air_weapon_dist = 16000


class KUZNECOW(unittype.ShipType):
    id = "KUZNECOW"
    name = "CV 1143.5 Admiral Kuznetsov"
    plane_num = 24
    helicopter_num = 12
    parking = 3
    detection_range = 25000
    threat_range = 12000
    air_weapon_dist = 12000


class MOLNIYA(unittype.ShipType):
    id = "MOLNIYA"
    name = "Corvette 1241.1 Molniya"
    detection_range = 21000
    threat_range = 2000
    air_weapon_dist = 2000


class MOSCOW(unittype.ShipType):
    id = "MOSCOW"
    name = "Cruiser 1164 Moskva"
    helicopter_num = 1
    parking = 1
    detection_range = 160000
    threat_range = 75000
    air_weapon_dist = 75000


class NEUSTRASH(unittype.ShipType):
    id = "NEUSTRASH"
    name = "Frigate 11540 Neustrashimy"
    helicopter_num = 1
    parking = 1
    detection_range = 27000
    threat_range = 12000
    air_weapon_dist = 12000


class PIOTR(unittype.ShipType):
    id = "PIOTR"
    name = "Battlecruiser 1144.2 Pyotr Velikiy"
    helicopter_num = 1
    parking = 1
    detection_range = 250000
    threat_range = 190000
    air_weapon_dist = 190000


class REZKY(unittype.ShipType):
    id = "REZKY"
    name = "Frigate 1135M Rezky"
    detection_range = 30000
    threat_range = 16000
    air_weapon_dist = 16000


class ELNYA(unittype.ShipType):
    id = "ELNYA"
    name = "Tanker Elnya 160"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Dry_cargo_ship_2(unittype.ShipType):
    id = "Dry-cargo ship-2"
    name = "Cargo Ivanov"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Dry_cargo_ship_1(unittype.ShipType):
    id = "Dry-cargo ship-1"
    name = "Bulker Yakushev"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class ZWEZDNY(unittype.ShipType):
    id = "ZWEZDNY"
    name = "Boat Zvezdny type"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class KILO(unittype.ShipType):
    id = "KILO"
    name = "SSK 877V Kilo"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class IMPROVED_KILO(unittype.ShipType):
    id = "IMPROVED_KILO"
    name = "SSK 636 Improved Kilo"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class SOM(unittype.ShipType):
    id = "SOM"
    name = "SSK 641B Tango"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class CV_1143_5(unittype.ShipType):
    id = "CV_1143_5"
    name = "CV 1143.5 Admiral Kuznetsov(2017)"
    plane_num = 24
    helicopter_num = 12
    parking = 3
    detection_range = 25000
    threat_range = 12000
    air_weapon_dist = 12000


class CastleClass_01(unittype.ShipType):
    id = "CastleClass_01"
    name = "Castle Class"
    plane_num = 0
    helicopter_num = 2
    parking = 1
    detection_range = 25000
    threat_range = 3000
    air_weapon_dist = 3000


class HarborTug(unittype.ShipType):
    id = "HarborTug"
    name = "Harbor Tug"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Hms_invincible(unittype.ShipType):
    id = "hms_invincible"
    name = "HMS Invincible (R05)"
    plane_num = 7
    helicopter_num = 6
    parking = 4
    detection_range = 100000
    threat_range = 74000
    air_weapon_dist = 74000


class Leander_gun_achilles(unittype.ShipType):
    id = "leander-gun-achilles"
    name = "HMS Achilles (F12)"
    helicopter_num = 1
    parking = 1
    detection_range = 180000
    threat_range = 8000
    air_weapon_dist = 8000


class Leander_gun_andromeda(unittype.ShipType):
    id = "leander-gun-andromeda"
    name = "HMS Andromeda (F57)"
    helicopter_num = 1
    parking = 1
    detection_range = 180000
    threat_range = 140000
    air_weapon_dist = 140000


class Leander_gun_ariadne(unittype.ShipType):
    id = "leander-gun-ariadne"
    name = "HMS Ariadne (F72)"
    helicopter_num = 1
    parking = 1
    detection_range = 150000
    threat_range = 100000
    air_weapon_dist = 100000


class Leander_gun_condell(unittype.ShipType):
    id = "leander-gun-condell"
    name = "CNS Almirante Condell (PFG-06)"
    helicopter_num = 1
    parking = 1
    detection_range = 150000
    threat_range = 100000
    air_weapon_dist = 100000


class Leander_gun_lynch(unittype.ShipType):
    id = "leander-gun-lynch"
    name = "CNS Almirante Lynch (PFG-07)"
    helicopter_num = 1
    parking = 1
    detection_range = 180000
    threat_range = 140000
    air_weapon_dist = 140000


class Ship_Tilde_Supply(unittype.ShipType):
    id = "Ship_Tilde_Supply"
    name = "Supply Ship MV Tilde"
    helicopter_num = 1
    parking = 1
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Santafe(unittype.ShipType):
    id = "santafe"
    name = "ARA Santa Fe S-21"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 30000


class Ara_vdm(unittype.ShipType):
    id = "ara_vdm"
    name = "ARA Veinticinco de Mayo"
    plane_num = 15
    helicopter_num = 6
    parking = 8
    detection_range = 18000
    threat_range = 5000
    air_weapon_dist = 5000


class Atconveyor(unittype.ShipType):
    id = "atconveyor"
    name = "SS Atlantic Conveyor"
    plane_num = 6
    helicopter_num = 1
    parking = 7
    detection_range = 100000
    threat_range = 74000
    air_weapon_dist = 74000


class HandyWind(unittype.ShipType):
    id = "HandyWind"
    name = "Bulker Handy Wind"
    helicopter_num = 1
    parking = 1
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Seawise_Giant(unittype.ShipType):
    id = "Seawise_Giant"
    name = "Tanker Seawise Giant"
    helicopter_num = 1
    parking = 1
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class La_Combattante_II(unittype.ShipType):
    id = "La_Combattante_II"
    name = "FAC La Combattante IIa"
    detection_range = 19000
    threat_range = 4000
    air_weapon_dist = 4000


class BDK_775(unittype.ShipType):
    id = "BDK-775"
    name = "LS Ropucha"
    detection_range = 25000
    threat_range = 6000
    air_weapon_dist = 6000


class CVN_71(unittype.ShipType):
    id = "CVN_71"
    name = "CVN-71 Theodore Roosevelt"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 50000
    threat_range = 25000
    air_weapon_dist = 25000


class CVN_72(unittype.ShipType):
    id = "CVN_72"
    name = "CVN-72 Abraham Lincoln"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 50000
    threat_range = 25000
    air_weapon_dist = 25000


class CVN_73(unittype.ShipType):
    id = "CVN_73"
    name = "CVN-73 George Washington"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 50000
    threat_range = 25000
    air_weapon_dist = 25000


class Stennis(unittype.ShipType):
    id = "Stennis"
    name = "CVN-74 John C. Stennis"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 50000
    threat_range = 25000
    air_weapon_dist = 25000


class CVN_75(unittype.ShipType):
    id = "CVN_75"
    name = "CVN-75 Harry S. Truman"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 50000
    threat_range = 25000
    air_weapon_dist = 25000


class USS_Arleigh_Burke_IIa(unittype.ShipType):
    id = "USS_Arleigh_Burke_IIa"
    name = "DDG Arleigh Burke IIa"
    helicopter_num = 2
    parking = 1
    detection_range = 150000
    threat_range = 100000
    air_weapon_dist = 100000


class LHA_Tarawa(unittype.ShipType):
    id = "LHA_Tarawa"
    name = "LHA-1 Tarawa"
    plane_num = 40
    helicopter_num = 36
    parking = 4
    detection_range = 150000
    threat_range = 20000
    air_weapon_dist = 20000


class Type_052B(unittype.ShipType):
    id = "Type_052B"
    name = "Type 052B Destroyer"
    plane_num = 0
    helicopter_num = 1
    parking = 1
    detection_range = 100000
    threat_range = 30000
    air_weapon_dist = 30000


class Type_054A(unittype.ShipType):
    id = "Type_054A"
    name = "Type 054A Frigate"
    plane_num = 0
    helicopter_num = 1
    parking = 1
    detection_range = 160000
    threat_range = 45000
    air_weapon_dist = 45000


class Type_052C(unittype.ShipType):
    id = "Type_052C"
    name = "Type 052C Destroyer"
    plane_num = 0
    helicopter_num = 1
    parking = 1
    detection_range = 260000
    threat_range = 100000
    air_weapon_dist = 100000


class Type_093(unittype.ShipType):
    id = "Type_093"
    name = "Type 093 Attack Submarine"
    detection_range = 40000
    threat_range = 40000
    air_weapon_dist = 0


class Type_071(unittype.ShipType):
    id = "Type_071"
    name = "Type 071 Amphibious Transport Dock"
    helicopter_num = 2
    parking = 2
    detection_range = 300000
    threat_range = 150000
    air_weapon_dist = 150000


class Forrestal(unittype.ShipType):
    id = "Forrestal"
    name = "CV-59 Forrestal"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 50000
    threat_range = 25000
    air_weapon_dist = 25000


class LST_Mk2(unittype.ShipType):
    id = "LST_Mk2"
    name = "LST Mk.II"
    detection_range = 0
    threat_range = 4000
    air_weapon_dist = 4000


class USS_Samuel_Chase(unittype.ShipType):
    id = "USS_Samuel_Chase"
    name = "LS Samuel Chase"
    detection_range = 0
    threat_range = 7000
    air_weapon_dist = 7000


class Higgins_boat(unittype.ShipType):
    id = "Higgins_boat"
    name = "Boat LCVP Higgins"
    detection_range = 3000
    threat_range = 1000
    air_weapon_dist = 1000


class Uboat_VIIC(unittype.ShipType):
    id = "Uboat_VIIC"
    name = "U-boat VIIC U-flak"
    detection_range = 20000
    threat_range = 4000
    air_weapon_dist = 4000


class Schnellboot_type_S130(unittype.ShipType):
    id = "Schnellboot_type_S130"
    name = "Boat Schnellboot type S130"
    detection_range = 10000
    threat_range = 4000
    air_weapon_dist = 4000

ship_map = {
    "speedboat": Speedboat,
    "VINSON": VINSON,
    "PERRY": PERRY,
    "TICONDEROG": TICONDEROG,
    "ALBATROS": ALBATROS,
    "KUZNECOW": KUZNECOW,
    "MOLNIYA": MOLNIYA,
    "MOSCOW": MOSCOW,
    "NEUSTRASH": NEUSTRASH,
    "PIOTR": PIOTR,
    "REZKY": REZKY,
    "ELNYA": ELNYA,
    "Dry-cargo ship-2": Dry_cargo_ship_2,
    "Dry-cargo ship-1": Dry_cargo_ship_1,
    "ZWEZDNY": ZWEZDNY,
    "KILO": KILO,
    "IMPROVED_KILO": IMPROVED_KILO,
    "SOM": SOM,
    "CV_1143_5": CV_1143_5,
    "CastleClass_01": CastleClass_01,
    "HarborTug": HarborTug,
    "hms_invincible": Hms_invincible,
    "leander-gun-achilles": Leander_gun_achilles,
    "leander-gun-andromeda": Leander_gun_andromeda,
    "leander-gun-ariadne": Leander_gun_ariadne,
    "leander-gun-condell": Leander_gun_condell,
    "leander-gun-lynch": Leander_gun_lynch,
    "Ship_Tilde_Supply": Ship_Tilde_Supply,
    "santafe": Santafe,
    "ara_vdm": Ara_vdm,
    "atconveyor": Atconveyor,
    "HandyWind": HandyWind,
    "Seawise_Giant": Seawise_Giant,
    "La_Combattante_II": La_Combattante_II,
    "BDK-775": BDK_775,
    "CVN_71": CVN_71,
    "CVN_72": CVN_72,
    "CVN_73": CVN_73,
    "Stennis": Stennis,
    "CVN_75": CVN_75,
    "USS_Arleigh_Burke_IIa": USS_Arleigh_Burke_IIa,
    "LHA_Tarawa": LHA_Tarawa,
    "Type_052B": Type_052B,
    "Type_054A": Type_054A,
    "Type_052C": Type_052C,
    "Type_093": Type_093,
    "Type_071": Type_071,
    "Forrestal": Forrestal,
    "LST_Mk2": LST_Mk2,
    "USS_Samuel_Chase": USS_Samuel_Chase,
    "Higgins_boat": Higgins_boat,
    "Uboat_VIIC": Uboat_VIIC,
    "Schnellboot_type_S130": Schnellboot_type_S130,
}
