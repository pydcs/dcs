# This file is generated from pydcs_export.lua
from enum import Enum
from typing import Any, Dict, List, Set

from dcs.weapons_data import Weapons
import dcs.task as task
from dcs.unittype import FlyingType

class HelicopterType(FlyingType):
    helicopter = True


class Ka_50(HelicopterType):
    id = "Ka-50"
    flyable = True
    height = 5.6
    width = 14.4
    length = 15.84
    fuel_max = 1450
    max_speed = 300
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                7: 40,
                1: 21.5,
                2: 25.7,
                4: 28,
                8: 50,
                9: 55.5,
                5: 30,
                10: 59.9,
                3: 27,
                6: 32
            },
        },
        2: {
            "channels": {
                15: 0.995,
                13: 0.583,
                7: 0.443,
                1: 0.625,
                2: 0.303,
                4: 0.591,
                8: 0.215,
                16: 1.21,
                9: 0.525,
                5: 0.408,
                10: 1.065,
                14: 0.283,
                3: 0.289,
                6: 0.803,
                12: 0.35,
                11: 0.718
            },
        },
    }

    class Liveries:

        class Georgia(Enum):
            georgia_camo = "georgia camo"

        class Australia(Enum):
            Russia_Worn_Black = "Russia Worn Black"

        class Israel(Enum):
            Israel_IAF_camo_1 = "Israel IAF camo 1"
            Israel_IAF_camo_2 = "Israel IAF camo 2"
            Israel_IAF_camo_3 = "Israel IAF camo 3"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Italy_Aeronautica_Militare = "Italy Aeronautica Militare"
            Algerian_AF_Desert = "Algerian AF Desert"
            France_Armee_de_Terre_1 = "France Armee de Terre 1"
            France_Armee_de_Terre_2 = "France Armee de Terre 2"
            France_Armee_de_Terre_Desert = "France Armee de Terre Desert"
            Russia_Standard_Army = "Russia Standard Army"
            belgium_sar = "belgium sar"
            belgium_camo = "belgium camo"
            belgium_olive = "belgium olive"
            Russia_DOSAAF = "Russia DOSAAF"
            Russia_Demo__024 = "Russia Demo #024"
            Russia_Demo__22__Black_Shark = "Russia Demo #22 `Black Shark`"
            Russia_Demo__Werewolf = "Russia Demo `Werewolf`"
            denmark_camo = "denmark camo"
            Italy_Esercito_Italiano = "Italy Esercito Italiano"
            Abkhazia_1 = "Abkhazia 1"
            Turkey_Fictional_Light_Gray = "Turkey Fictional Light Gray"
            South_Ossetia_1 = "South Ossetia 1"
            Russia_Fictional_Swedish = "Russia Fictional Swedish"
            Turkey_Fictional_1 = "Turkey Fictional 1"
            Turkey_Fictional = "Turkey Fictional"
            Ukraine_Demo = "Ukraine Demo"
            Turkey_fictional_desert_scheme = "Turkey fictional desert scheme"
            Russia_fictional_desert_scheme = "Russia fictional desert scheme"
            Russia_Fictional_Olive_Grey = "Russia Fictional Olive Grey"
            Russia_Fictional_Snow_Splatter = "Russia Fictional Snow Splatter"
            Russia_Fictional_Tropic_Green = "Russia Fictional Tropic Green"
            georgia_camo = "georgia camo"
            german_8320 = "german 8320"
            german_8332 = "german 8332"
            Greek_Army_Aviation = "Greek Army Aviation"
            Hellenic_Navy_Aviation = "Hellenic Navy Aviation"
            Hellenic_Navy_Aviation_2 = "Hellenic Navy Aviation 2"
            Israel_IAF_camo_1 = "Israel IAF camo 1"
            Israel_IAF_camo_2 = "Israel IAF camo 2"
            Israel_IAF_camo_3 = "Israel IAF camo 3"
            Denmark_navy_trainer = "Denmark navy trainer"
            Russia_New_Year = "Russia New Year"
            norway_camo = "norway camo"
            Netherlands_RNAF = "Netherlands RNAF"
            Netherlands_RNAF_wooded = "Netherlands RNAF wooded"
            Spain_SAA_Arido = "Spain SAA Arido"
            Spain_SAA_Boscoso = "Spain SAA Boscoso"
            Spain_SAA_Standard = "Spain SAA Standard"
            Russia_Standard_Army__Worn = "Russia Standard Army (Worn)"
            uk_camo = "uk camo"
            us_army = "us army"
            us_marines_1 = "us marines 1"
            us_marines_2 = "us marines 2"
            ukraine_camo_1 = "ukraine camo 1"
            ukraine_camo_1_dirt = "ukraine camo 1 dirt"
            Russia_Worn_Black = "Russia Worn Black"
            canadian_forces = "canadian forces"

        class Norway(Enum):
            norway_camo = "norway camo"

        class Ukraine(Enum):
            Ukraine_Demo = "Ukraine Demo"
            ukraine_camo_1 = "ukraine camo 1"
            ukraine_camo_1_dirt = "ukraine camo 1 dirt"

        class Belgium(Enum):
            belgium_sar = "belgium sar"
            belgium_camo = "belgium camo"
            belgium_olive = "belgium olive"

        class Greece(Enum):
            Greek_Army_Aviation = "Greek Army Aviation"
            Hellenic_Navy_Aviation = "Hellenic Navy Aviation"
            Hellenic_Navy_Aviation_2 = "Hellenic Navy Aviation 2"

        class UK(Enum):
            uk_camo = "uk camo"

        class Abkhazia(Enum):
            Abkhazia_1 = "Abkhazia 1"

        class SouthOssetia(Enum):
            South_Ossetia_1 = "South Ossetia 1"

        class TheNetherlands(Enum):
            Netherlands_RNAF = "Netherlands RNAF"
            Netherlands_RNAF_wooded = "Netherlands RNAF wooded"

        class Denmark(Enum):
            denmark_camo = "denmark camo"
            Denmark_navy_trainer = "Denmark navy trainer"

        class Sweden(Enum):
            Russia_Fictional_Swedish = "Russia Fictional Swedish"

        class Combined_Joint_Task_Forces_Red(Enum):
            Italy_Aeronautica_Militare = "Italy Aeronautica Militare"
            Algerian_AF_Desert = "Algerian AF Desert"
            France_Armee_de_Terre_1 = "France Armee de Terre 1"
            France_Armee_de_Terre_2 = "France Armee de Terre 2"
            France_Armee_de_Terre_Desert = "France Armee de Terre Desert"
            Russia_Standard_Army = "Russia Standard Army"
            belgium_sar = "belgium sar"
            belgium_camo = "belgium camo"
            belgium_olive = "belgium olive"
            Russia_DOSAAF = "Russia DOSAAF"
            Russia_Demo__024 = "Russia Demo #024"
            Russia_Demo__22__Black_Shark = "Russia Demo #22 `Black Shark`"
            Russia_Demo__Werewolf = "Russia Demo `Werewolf`"
            denmark_camo = "denmark camo"
            Italy_Esercito_Italiano = "Italy Esercito Italiano"
            Abkhazia_1 = "Abkhazia 1"
            Turkey_Fictional_Light_Gray = "Turkey Fictional Light Gray"
            South_Ossetia_1 = "South Ossetia 1"
            Russia_Fictional_Swedish = "Russia Fictional Swedish"
            Turkey_Fictional_1 = "Turkey Fictional 1"
            Turkey_Fictional = "Turkey Fictional"
            Ukraine_Demo = "Ukraine Demo"
            Turkey_fictional_desert_scheme = "Turkey fictional desert scheme"
            Russia_fictional_desert_scheme = "Russia fictional desert scheme"
            Russia_Fictional_Olive_Grey = "Russia Fictional Olive Grey"
            Russia_Fictional_Snow_Splatter = "Russia Fictional Snow Splatter"
            Russia_Fictional_Tropic_Green = "Russia Fictional Tropic Green"
            georgia_camo = "georgia camo"
            german_8320 = "german 8320"
            german_8332 = "german 8332"
            Greek_Army_Aviation = "Greek Army Aviation"
            Hellenic_Navy_Aviation = "Hellenic Navy Aviation"
            Hellenic_Navy_Aviation_2 = "Hellenic Navy Aviation 2"
            Israel_IAF_camo_1 = "Israel IAF camo 1"
            Israel_IAF_camo_2 = "Israel IAF camo 2"
            Israel_IAF_camo_3 = "Israel IAF camo 3"
            Denmark_navy_trainer = "Denmark navy trainer"
            Russia_New_Year = "Russia New Year"
            norway_camo = "norway camo"
            Netherlands_RNAF = "Netherlands RNAF"
            Netherlands_RNAF_wooded = "Netherlands RNAF wooded"
            Spain_SAA_Arido = "Spain SAA Arido"
            Spain_SAA_Boscoso = "Spain SAA Boscoso"
            Spain_SAA_Standard = "Spain SAA Standard"
            Russia_Standard_Army__Worn = "Russia Standard Army (Worn)"
            uk_camo = "uk camo"
            us_army = "us army"
            us_marines_1 = "us marines 1"
            us_marines_2 = "us marines 2"
            ukraine_camo_1 = "ukraine camo 1"
            ukraine_camo_1_dirt = "ukraine camo 1 dirt"
            Russia_Worn_Black = "Russia Worn Black"
            canadian_forces = "canadian forces"

        class France(Enum):
            France_Armee_de_Terre_1 = "France Armee de Terre 1"
            France_Armee_de_Terre_2 = "France Armee de Terre 2"
            France_Armee_de_Terre_Desert = "France Armee de Terre Desert"

        class USA(Enum):
            us_army = "us army"
            us_marines_1 = "us marines 1"
            us_marines_2 = "us marines 2"

        class Russia(Enum):
            Russia_Standard_Army = "Russia Standard Army"
            Russia_DOSAAF = "Russia DOSAAF"
            Russia_Demo__024 = "Russia Demo #024"
            Russia_Demo__22__Black_Shark = "Russia Demo #22 `Black Shark`"
            Russia_Demo__Werewolf = "Russia Demo `Werewolf`"
            Russia_Fictional_Swedish = "Russia Fictional Swedish"
            Russia_fictional_desert_scheme = "Russia fictional desert scheme"
            Russia_Fictional_Olive_Grey = "Russia Fictional Olive Grey"
            Russia_Fictional_Snow_Splatter = "Russia Fictional Snow Splatter"
            Russia_Fictional_Tropic_Green = "Russia Fictional Tropic Green"
            Russia_New_Year = "Russia New Year"
            Russia_Standard_Army__Worn = "Russia Standard Army (Worn)"
            Russia_Worn_Black = "Russia Worn Black"

        class Italy(Enum):
            Italy_Aeronautica_Militare = "Italy Aeronautica Militare"
            Italy_Esercito_Italiano = "Italy Esercito Italiano"

        class Turkey(Enum):
            Turkey_Fictional_Light_Gray = "Turkey Fictional Light Gray"
            Turkey_Fictional_1 = "Turkey Fictional 1"
            Turkey_Fictional = "Turkey Fictional"
            Turkey_fictional_desert_scheme = "Turkey fictional desert scheme"

        class Algeria(Enum):
            Algerian_AF_Desert = "Algerian AF Desert"

        class Germany(Enum):
            german_8320 = "german 8320"
            german_8332 = "german 8332"

        class Spain(Enum):
            Spain_SAA_Arido = "Spain SAA Arido"
            Spain_SAA_Boscoso = "Spain SAA Boscoso"
            Spain_SAA_Standard = "Spain SAA Standard"

        class Canada(Enum):
            canadian_forces = "canadian forces"

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        APU_6___6_9A4172_Vikhr = (1, Weapons.APU_6___6_9A4172_Vikhr)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (1, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (1, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (1, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (1, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (1, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (1, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (1, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450_ = (1, Weapons.Fuel_tank_PTB_450_)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450_ = (2, Weapons.Fuel_tank_PTB_450_)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (3, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450_ = (3, Weapons.Fuel_tank_PTB_450_)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        APU_6___6_9A4172_Vikhr = (4, Weapons.APU_6___6_9A4172_Vikhr)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (4, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450_ = (4, Weapons.Fuel_tank_PTB_450_)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Mi_24V(HelicopterType):
    id = "Mi-24V"
    height = 4.354
    width = 17.3
    length = 20.953
    fuel_max = 1704
    max_speed = 320
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 0
    flare_charge_size = 1

    class Liveries:

        class Georgia(Enum):
            standard = "standard"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Abkhazia = "Abkhazia"
            Algerian_AF_Black = "Algerian AF Black"
            Algerian_AF_New_Desert = "Algerian AF New Desert"
            Algerian_AF_Old_Desert = "Algerian AF Old Desert"
            South_Ossetia = "South Ossetia"
            standard_1 = "standard 1"
            standard_2__faded_and_sun_bleached = "standard 2 (faded and sun-bleached)"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"
            ukraine = "ukraine"
            Ukraine_UN = "Ukraine UN"
            standard = "standard"

        class Ukraine(Enum):
            ukraine = "ukraine"
            Ukraine_UN = "Ukraine UN"

        class Abkhazia(Enum):
            Abkhazia = "Abkhazia"

        class United_Nations_Peacekeepers(Enum):
            Ukraine_UN = "Ukraine UN"

        class SouthOssetia(Enum):
            South_Ossetia = "South Ossetia"

        class Combined_Joint_Task_Forces_Red(Enum):
            Abkhazia = "Abkhazia"
            Algerian_AF_Black = "Algerian AF Black"
            Algerian_AF_New_Desert = "Algerian AF New Desert"
            Algerian_AF_Old_Desert = "Algerian AF Old Desert"
            South_Ossetia = "South Ossetia"
            standard_1 = "standard 1"
            standard_2__faded_and_sun_bleached = "standard 2 (faded and sun-bleached)"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"
            ukraine = "ukraine"
            Ukraine_UN = "Ukraine UN"
            standard = "standard"

        class Russia(Enum):
            standard_1 = "standard 1"
            standard_2__faded_and_sun_bleached = "standard 2 (faded and sun-bleached)"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"

        class Algeria(Enum):
            Algerian_AF_Black = "Algerian AF Black"
            Algerian_AF_New_Desert = "Algerian AF New Desert"
            Algerian_AF_Old_Desert = "Algerian AF Old Desert"

    class Pylon1:
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (1, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (2, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        Fuel_tank_PTB_450 = (2, Weapons.Fuel_tank_PTB_450)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        GUV_VOG = (2, Weapons.GUV_VOG)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (3, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        Fuel_tank_PTB_450 = (3, Weapons.Fuel_tank_PTB_450)
        GUV_YakB_GSHP = (3, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (3, Weapons.GUV_VOG)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (4, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (4, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        Fuel_tank_PTB_450 = (4, Weapons.Fuel_tank_PTB_450)
        GUV_YakB_GSHP = (4, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (4, Weapons.GUV_VOG)

    class Pylon5:
        B_8V20A_CM = (5, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (5, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (5, Weapons.B_8V20A_OM)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (5, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (5, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (5, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        Fuel_tank_PTB_450 = (5, Weapons.Fuel_tank_PTB_450)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        GUV_VOG = (5, Weapons.GUV_VOG)

    class Pylon6:
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (6, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.Transport, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Mi_8MT(HelicopterType):
    id = "Mi-8MT"
    flyable = True
    large_parking_slot = True
    height = 4.908
    width = 21.33
    length = 25.942
    fuel_max = 1929
    max_speed = 250
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1

    panel_radio = {
        1: {
            "channels": {
                1: 127.5,
                2: 135,
                4: 127,
                8: 128,
                16: 132,
                17: 138,
                9: 126,
                18: 122,
                5: 125,
                10: 133,
                20: 137,
                11: 130,
                3: 136,
                6: 121,
                12: 129,
                13: 123,
                7: 141,
                14: 131,
                19: 124,
                15: 134
            },
        },
        2: {
            "channels": {
                7: 40,
                1: 21.5,
                2: 25.7,
                4: 28,
                8: 50,
                9: 55.5,
                5: 30,
                10: 59.9,
                3: 27,
                6: 32
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "ExhaustScreen": True,
        "LeftEngineResource": 90,
        "RightEngineResource": 90,
        "AdditionalArmor": True,
        "CargoHalfdoor": True,
        "GunnersAISkill": 90,
        "NetCrewControlPriority": 1,
        "NS430allow": True,
    }

    class Properties:

        class ExhaustScreen:
            id = "ExhaustScreen"

        class LeftEngineResource:
            id = "LeftEngineResource"

        class RightEngineResource:
            id = "RightEngineResource"

        class AdditionalArmor:
            id = "AdditionalArmor"

        class CargoHalfdoor:
            id = "CargoHalfdoor"

        class GunnersAISkill:
            id = "GunnersAISkill"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class NS430allow:
            id = "NS430allow"

    class Liveries:

        class USSR(Enum):
            BP_RS01 = "BP_RS01"
            Russia_Aeroflot = "Russia_Aeroflot"
            Russia_Army_Weather = "Russia_Army_Weather"

        class Georgia(Enum):
            BP_RS01 = "BP_RS01"
            Georgia = "Georgia"

        class Venezuela(Enum):
            BP_RS01 = "BP_RS01"

        class Australia(Enum):
            BP_RS01 = "BP_RS01"
            Australia = "Australia"
            Standard = "Standard"

        class Israel(Enum):
            BP_RS01 = "BP_RS01"
            Israel = "Israel"
            Standard = "Standard"

        class Combined_Joint_Task_Forces_Blue(Enum):
            BP_RS01 = "BP_RS01"
            Russia_VVS_Standard = "Russia_VVS_Standard"
            USA_AFG = "USA_AFG"
            IR_AFAGIR_Blue = "IR AFAGIR Blue"
            IR_AFAGIR_Sand = "IR AFAGIR Sand"
            Abkhazia = "Abkhazia"
            Algerian_AF_Green = "Algerian AF Green"
            Algerian_AF_Green_EVSAN = "Algerian AF Green EVSAN"
            Algerian_AF_New_Desert = "Algerian AF New Desert"
            Algerian_AF_Old_Desert = "Algerian AF Old Desert"
            Algerian_AF_VIP = "Algerian AF VIP"
            Canada = "Canada"
            Russia_Aeroflot = "Russia_Aeroflot"
            Russia_Gazprom = "Russia_Gazprom"
            Russia_KazanVZ = "Russia_KazanVZ"
            Russia_LII_Gromov_RA_25546 = "Russia_LII_Gromov RA-25546"
            Russia_Police = "Russia_Police"
            Russia_UTair = "Russia_UTair"
            Russia_Vertolety_Russia = "Russia_Vertolety_Russia"
            Russia_Vertolety_Russia_2 = "Russia_Vertolety_Russia_2"
            Russia_Naryan_Mar = "Russia_Naryan-Mar"
            Australia = "Australia"
            France_ARMY = "France ARMY"
            Israel = "Israel"
            Italy_ARMY = "Italy ARMY"
            Netherlands_ARMY = "Netherlands ARMY"
            France_NAVY = "France NAVY"
            Italy_NAVY = "Italy NAVY"
            Netherlands_NAVY = "Netherlands NAVY"
            Norway = "Norway"
            Belgium = "Belgium"
            Denmark = "Denmark"
            South_Ossetia = "South Ossetia"
            Spain = "Spain"
            Georgia = "Georgia"
            Germany = "Germany"
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"
            Hellenic_Army_Aviation = "Hellenic Army Aviation"
            Turkey = "Turkey"
            IR_Iranian_Special_Police_Forces = "IR Iranian Special Police Forces"
            China_PLAAA_Camo = "China PLAAA Camo"
            China_UN = "China UN"
            China_PLAAA_White = "China PLAAA White"
            United_Kingdom = "United Kingdom"
            Russia_VVS_Grey = "Russia_VVS_Grey"
            Russia_VVS_Grey_2 = "Russia_VVS_Grey_2"
            Russia_VVS_Standard_2 = "Russia_VVS_Standard_2"
            Russia_FSB = "Russia_FSB"
            Russia_MVD_Mozdok = "Russia_MVD_Mozdok"
            Russia_MVD_Standard = "Russia_MVD_Standard"
            Russia_VVS_MA = "Russia_VVS_MA"
            Russia_UN = "Russia_UN"
            Russia_PF_Ambulance = "Russia_PF_Ambulance"
            Russia_Army_Weather = "Russia_Army_Weather"
            Insurgents = "Insurgents"
            Ukraine = "Ukraine"
            placeholder = "placeholder"
            Standard = "Standard"

        class Sudan(Enum):
            BP_RS01 = "BP_RS01"

        class Norway(Enum):
            BP_RS01 = "BP_RS01"
            Norway = "Norway"
            Standard = "Standard"

        class Romania(Enum):
            BP_RS01 = "BP_RS01"

        class Iran(Enum):
            BP_RS01 = "BP_RS01"
            IR_AFAGIR_Blue = "IR AFAGIR Blue"
            IR_AFAGIR_Sand = "IR AFAGIR Sand"
            IR_Iranian_Special_Police_Forces = "IR Iranian Special Police Forces"

        class Ukraine(Enum):
            BP_RS01 = "BP_RS01"
            Ukraine = "Ukraine"

        class Libya(Enum):
            BP_RS01 = "BP_RS01"

        class Belgium(Enum):
            BP_RS01 = "BP_RS01"
            Belgium = "Belgium"

        class Slovakia(Enum):
            BP_RS01 = "BP_RS01"

        class Greece(Enum):
            BP_RS01 = "BP_RS01"
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"
            Hellenic_Army_Aviation = "Hellenic Army Aviation"

        class UK(Enum):
            BP_RS01 = "BP_RS01"
            United_Kingdom = "United Kingdom"
            Standard = "Standard"

        class Third_Reich(Enum):
            BP_RS01 = "BP_RS01"

        class Hungary(Enum):
            BP_RS01 = "BP_RS01"

        class Abkhazia(Enum):
            BP_RS01 = "BP_RS01"
            Abkhazia = "Abkhazia"

        class Morocco(Enum):
            BP_RS01 = "BP_RS01"

        class United_Nations_Peacekeepers(Enum):
            BP_RS01 = "BP_RS01"
            Russia_UN = "Russia_UN"

        class Switzerland(Enum):
            BP_RS01 = "BP_RS01"

        class SouthOssetia(Enum):
            BP_RS01 = "BP_RS01"
            South_Ossetia = "South Ossetia"

        class Vietnam(Enum):
            BP_RS01 = "BP_RS01"

        class China(Enum):
            BP_RS01 = "BP_RS01"
            China_PLAAA_Camo = "China PLAAA Camo"
            China_UN = "China UN"
            China_PLAAA_White = "China PLAAA White"

        class Yemen(Enum):
            BP_RS01 = "BP_RS01"

        class Kuwait(Enum):
            BP_RS01 = "BP_RS01"

        class Serbia(Enum):
            BP_RS01 = "BP_RS01"

        class Oman(Enum):
            BP_RS01 = "BP_RS01"

        class India(Enum):
            BP_RS01 = "BP_RS01"

        class Egypt(Enum):
            BP_RS01 = "BP_RS01"

        class TheNetherlands(Enum):
            BP_RS01 = "BP_RS01"
            Netherlands_ARMY = "Netherlands ARMY"
            Netherlands_NAVY = "Netherlands NAVY"
            Standard = "Standard"

        class Poland(Enum):
            BP_RS01 = "BP_RS01"

        class Syria(Enum):
            BP_RS01 = "BP_RS01"

        class Finland(Enum):
            BP_RS01 = "BP_RS01"

        class Kazakhstan(Enum):
            BP_RS01 = "BP_RS01"

        class Denmark(Enum):
            BP_RS01 = "BP_RS01"
            Denmark = "Denmark"

        class Sweden(Enum):
            BP_RS01 = "BP_RS01"

        class Croatia(Enum):
            BP_RS01 = "BP_RS01"

        class CzechRepublic(Enum):
            BP_RS01 = "BP_RS01"

        class GDR(Enum):
            BP_RS01 = "BP_RS01"

        class Yugoslavia(Enum):
            BP_RS01 = "BP_RS01"

        class Bulgaria(Enum):
            BP_RS01 = "BP_RS01"

        class SouthKorea(Enum):
            BP_RS01 = "BP_RS01"

        class Tunisia(Enum):
            BP_RS01 = "BP_RS01"

        class Combined_Joint_Task_Forces_Red(Enum):
            BP_RS01 = "BP_RS01"
            Russia_VVS_Standard = "Russia_VVS_Standard"
            USA_AFG = "USA_AFG"
            IR_AFAGIR_Blue = "IR AFAGIR Blue"
            IR_AFAGIR_Sand = "IR AFAGIR Sand"
            Abkhazia = "Abkhazia"
            Algerian_AF_Green = "Algerian AF Green"
            Algerian_AF_Green_EVSAN = "Algerian AF Green EVSAN"
            Algerian_AF_New_Desert = "Algerian AF New Desert"
            Algerian_AF_Old_Desert = "Algerian AF Old Desert"
            Algerian_AF_VIP = "Algerian AF VIP"
            Canada = "Canada"
            Russia_Aeroflot = "Russia_Aeroflot"
            Russia_Gazprom = "Russia_Gazprom"
            Russia_KazanVZ = "Russia_KazanVZ"
            Russia_LII_Gromov_RA_25546 = "Russia_LII_Gromov RA-25546"
            Russia_Police = "Russia_Police"
            Russia_UTair = "Russia_UTair"
            Russia_Vertolety_Russia = "Russia_Vertolety_Russia"
            Russia_Vertolety_Russia_2 = "Russia_Vertolety_Russia_2"
            Russia_Naryan_Mar = "Russia_Naryan-Mar"
            Australia = "Australia"
            France_ARMY = "France ARMY"
            Israel = "Israel"
            Italy_ARMY = "Italy ARMY"
            Netherlands_ARMY = "Netherlands ARMY"
            France_NAVY = "France NAVY"
            Italy_NAVY = "Italy NAVY"
            Netherlands_NAVY = "Netherlands NAVY"
            Norway = "Norway"
            Belgium = "Belgium"
            Denmark = "Denmark"
            South_Ossetia = "South Ossetia"
            Spain = "Spain"
            Georgia = "Georgia"
            Germany = "Germany"
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"
            Hellenic_Army_Aviation = "Hellenic Army Aviation"
            Turkey = "Turkey"
            IR_Iranian_Special_Police_Forces = "IR Iranian Special Police Forces"
            China_PLAAA_Camo = "China PLAAA Camo"
            China_UN = "China UN"
            China_PLAAA_White = "China PLAAA White"
            United_Kingdom = "United Kingdom"
            Russia_VVS_Grey = "Russia_VVS_Grey"
            Russia_VVS_Grey_2 = "Russia_VVS_Grey_2"
            Russia_VVS_Standard_2 = "Russia_VVS_Standard_2"
            Russia_FSB = "Russia_FSB"
            Russia_MVD_Mozdok = "Russia_MVD_Mozdok"
            Russia_MVD_Standard = "Russia_MVD_Standard"
            Russia_VVS_MA = "Russia_VVS_MA"
            Russia_UN = "Russia_UN"
            Russia_PF_Ambulance = "Russia_PF_Ambulance"
            Russia_Army_Weather = "Russia_Army_Weather"
            Insurgents = "Insurgents"
            Ukraine = "Ukraine"
            placeholder = "placeholder"
            Standard = "Standard"

        class Lebanon(Enum):
            BP_RS01 = "BP_RS01"

        class Portugal(Enum):
            BP_RS01 = "BP_RS01"

        class Cuba(Enum):
            BP_RS01 = "BP_RS01"

        class Insurgents(Enum):
            BP_RS01 = "BP_RS01"
            Insurgents = "Insurgents"
            Standard = "Standard"

        class SaudiArabia(Enum):
            BP_RS01 = "BP_RS01"

        class France(Enum):
            BP_RS01 = "BP_RS01"
            France_ARMY = "France ARMY"
            France_NAVY = "France NAVY"
            Standard = "Standard"

        class USA(Enum):
            BP_RS01 = "BP_RS01"
            USA_AFG = "USA_AFG"
            Standard = "Standard"

        class Honduras(Enum):
            BP_RS01 = "BP_RS01"

        class Qatar(Enum):
            BP_RS01 = "BP_RS01"

        class Russia(Enum):
            BP_RS01 = "BP_RS01"
            Russia_VVS_Standard = "Russia_VVS_Standard"
            Russia_Aeroflot = "Russia_Aeroflot"
            Russia_Gazprom = "Russia_Gazprom"
            Russia_KazanVZ = "Russia_KazanVZ"
            Russia_LII_Gromov_RA_25546 = "Russia_LII_Gromov RA-25546"
            Russia_Police = "Russia_Police"
            Russia_UTair = "Russia_UTair"
            Russia_Vertolety_Russia = "Russia_Vertolety_Russia"
            Russia_Vertolety_Russia_2 = "Russia_Vertolety_Russia_2"
            Russia_Naryan_Mar = "Russia_Naryan-Mar"
            Russia_VVS_Grey = "Russia_VVS_Grey"
            Russia_VVS_Grey_2 = "Russia_VVS_Grey_2"
            Russia_VVS_Standard_2 = "Russia_VVS_Standard_2"
            Russia_FSB = "Russia_FSB"
            Russia_MVD_Mozdok = "Russia_MVD_Mozdok"
            Russia_MVD_Standard = "Russia_MVD_Standard"
            Russia_VVS_MA = "Russia_VVS_MA"
            Russia_UN = "Russia_UN"
            Russia_PF_Ambulance = "Russia_PF_Ambulance"
            Russia_Army_Weather = "Russia_Army_Weather"

        class United_Arab_Emirates(Enum):
            BP_RS01 = "BP_RS01"

        class Italian_Social_Republi(Enum):
            BP_RS01 = "BP_RS01"

        class Austria(Enum):
            BP_RS01 = "BP_RS01"

        class Bahrain(Enum):
            BP_RS01 = "BP_RS01"

        class Italy(Enum):
            BP_RS01 = "BP_RS01"
            Italy_ARMY = "Italy ARMY"
            Italy_NAVY = "Italy NAVY"
            Standard = "Standard"

        class Chile(Enum):
            BP_RS01 = "BP_RS01"

        class Turkey(Enum):
            BP_RS01 = "BP_RS01"
            Turkey = "Turkey"
            Standard = "Standard"

        class Philippines(Enum):
            BP_RS01 = "BP_RS01"

        class Algeria(Enum):
            BP_RS01 = "BP_RS01"
            Algerian_AF_Green = "Algerian AF Green"
            Algerian_AF_Green_EVSAN = "Algerian AF Green EVSAN"
            Algerian_AF_New_Desert = "Algerian AF New Desert"
            Algerian_AF_Old_Desert = "Algerian AF Old Desert"
            Algerian_AF_VIP = "Algerian AF VIP"

        class Pakistan(Enum):
            BP_RS01 = "BP_RS01"

        class Malaysia(Enum):
            BP_RS01 = "BP_RS01"

        class Indonesia(Enum):
            BP_RS01 = "BP_RS01"

        class Iraq(Enum):
            BP_RS01 = "BP_RS01"

        class Germany(Enum):
            BP_RS01 = "BP_RS01"
            Germany = "Germany"
            Standard = "Standard"

        class South_Africa(Enum):
            BP_RS01 = "BP_RS01"

        class Jordan(Enum):
            BP_RS01 = "BP_RS01"

        class Mexico(Enum):
            BP_RS01 = "BP_RS01"

        class USAFAggressors(Enum):
            BP_RS01 = "BP_RS01"

        class Brazil(Enum):
            BP_RS01 = "BP_RS01"

        class Spain(Enum):
            BP_RS01 = "BP_RS01"
            Spain = "Spain"
            Standard = "Standard"

        class Belarus(Enum):
            BP_RS01 = "BP_RS01"

        class Canada(Enum):
            BP_RS01 = "BP_RS01"
            Canada = "Canada"
            Standard = "Standard"

        class NorthKorea(Enum):
            BP_RS01 = "BP_RS01"

        class Ethiopia(Enum):
            BP_RS01 = "BP_RS01"

        class Japan(Enum):
            BP_RS01 = "BP_RS01"

        class Thailand(Enum):
            BP_RS01 = "BP_RS01"

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_CM_GN = (1, Weapons.B_8V20A_CM_GN)
        B_8V20A_CM_RD = (1, Weapons.B_8V20A_CM_RD)
        B_8V20A_CM_WH = (1, Weapons.B_8V20A_CM_WH)
        B_8V20A_CM_BU = (1, Weapons.B_8V20A_CM_BU)
        B_8V20A_CM_YE = (1, Weapons.B_8V20A_CM_YE)
        B_8V20A_CM_VT = (1, Weapons.B_8V20A_CM_VT)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (1, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_100___100kg_GP_Bomb_LD = (1, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (1, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        GUV_VOG = (1, Weapons.GUV_VOG)
#ERRR <CLEAN>

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_CM_GN = (2, Weapons.B_8V20A_CM_GN)
        B_8V20A_CM_RD = (2, Weapons.B_8V20A_CM_RD)
        B_8V20A_CM_WH = (2, Weapons.B_8V20A_CM_WH)
        B_8V20A_CM_BU = (2, Weapons.B_8V20A_CM_BU)
        B_8V20A_CM_YE = (2, Weapons.B_8V20A_CM_YE)
        B_8V20A_CM_VT = (2, Weapons.B_8V20A_CM_VT)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        GUV_YakB_GSHP = (2, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (2, Weapons.GUV_VOG)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (2, Weapons.SAB_100___100kg_flare_illumination_Bomb)
#ERRR <CLEAN>

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_CM_GN = (3, Weapons.B_8V20A_CM_GN)
        B_8V20A_CM_RD = (3, Weapons.B_8V20A_CM_RD)
        B_8V20A_CM_WH = (3, Weapons.B_8V20A_CM_WH)
        B_8V20A_CM_BU = (3, Weapons.B_8V20A_CM_BU)
        B_8V20A_CM_YE = (3, Weapons.B_8V20A_CM_YE)
        B_8V20A_CM_VT = (3, Weapons.B_8V20A_CM_VT)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (3, Weapons.SAB_100___100kg_flare_illumination_Bomb)
#ERRR <CLEAN-200.5>

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_CM_GN = (4, Weapons.B_8V20A_CM_GN)
        B_8V20A_CM_RD = (4, Weapons.B_8V20A_CM_RD)
        B_8V20A_CM_WH = (4, Weapons.B_8V20A_CM_WH)
        B_8V20A_CM_BU = (4, Weapons.B_8V20A_CM_BU)
        B_8V20A_CM_YE = (4, Weapons.B_8V20A_CM_YE)
        B_8V20A_CM_VT = (4, Weapons.B_8V20A_CM_VT)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (4, Weapons.SAB_100___100kg_flare_illumination_Bomb)
#ERRR <CLEAN-200.5>

    class Pylon5:
        B_8V20A_CM = (5, Weapons.B_8V20A_CM)
        B_8V20A_CM_GN = (5, Weapons.B_8V20A_CM_GN)
        B_8V20A_CM_RD = (5, Weapons.B_8V20A_CM_RD)
        B_8V20A_CM_WH = (5, Weapons.B_8V20A_CM_WH)
        B_8V20A_CM_BU = (5, Weapons.B_8V20A_CM_BU)
        B_8V20A_CM_YE = (5, Weapons.B_8V20A_CM_YE)
        B_8V20A_CM_VT = (5, Weapons.B_8V20A_CM_VT)
        B_8V20A_OM = (5, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (5, Weapons.B_8V20A_OFP2)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (5, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        GUV_YakB_GSHP = (5, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (5, Weapons.GUV_VOG)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (5, Weapons.SAB_100___100kg_flare_illumination_Bomb)
#ERRR <CLEAN>

    class Pylon6:
        B_8V20A_CM = (6, Weapons.B_8V20A_CM)
        B_8V20A_CM_GN = (6, Weapons.B_8V20A_CM_GN)
        B_8V20A_CM_RD = (6, Weapons.B_8V20A_CM_RD)
        B_8V20A_CM_WH = (6, Weapons.B_8V20A_CM_WH)
        B_8V20A_CM_BU = (6, Weapons.B_8V20A_CM_BU)
        B_8V20A_CM_YE = (6, Weapons.B_8V20A_CM_YE)
        B_8V20A_CM_VT = (6, Weapons.B_8V20A_CM_VT)
        B_8V20A_OM = (6, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (6, Weapons.B_8V20A_OFP2)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_100___100kg_GP_Bomb_LD = (6, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100___100kg_flare_illumination_Bomb = (6, Weapons.SAB_100___100kg_flare_illumination_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (6, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        GUV_VOG = (6, Weapons.GUV_VOG)
#ERRR <CLEAN>

    class Pylon7:
        KORD_12_7 = (7, Weapons.KORD_12_7)

    class Pylon8:
        PKT_7_62 = (8, Weapons.PKT_7_62)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.CAS, task.GroundAttack, task.Transport, task.AFAC, task.AntishipStrike]
    task_default = task.Transport


class Mi_26(HelicopterType):
    id = "Mi-26"
    group_size_max = 1
    large_parking_slot = True
    height = 12.9
    width = 32
    length = 40.854
    fuel_max = 9600
    max_speed = 300
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 0
    flare_charge_size = 1

    class Liveries:

        class USSR(Enum):
            RF_Air_Force = "RF Air Force"
            United_Nations = "United Nations"

        class Georgia(Enum):
            United_Nations = "United Nations"

        class Venezuela(Enum):
            United_Nations = "United Nations"

        class Australia(Enum):
            United_Nations = "United Nations"

        class Israel(Enum):
            United_Nations = "United Nations"

        class Combined_Joint_Task_Forces_Blue(Enum):
            _7th_Separate_Brigade_of_AA__Kalinov = "7th Separate Brigade of AA (Kalinov)"
            Algerian_Air_Force_SL_22 = "Algerian Air Force SL-22"
            China_Flying_Dragon_Aviation = "China Flying Dragon Aviation"
            RF_Air_Force = "RF Air Force"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"
            United_Nations = "United Nations"

        class Sudan(Enum):
            United_Nations = "United Nations"

        class Norway(Enum):
            United_Nations = "United Nations"

        class Romania(Enum):
            United_Nations = "United Nations"

        class Iran(Enum):
            United_Nations = "United Nations"

        class Ukraine(Enum):
            _7th_Separate_Brigade_of_AA__Kalinov = "7th Separate Brigade of AA (Kalinov)"
            United_Nations = "United Nations"

        class Libya(Enum):
            United_Nations = "United Nations"

        class Belgium(Enum):
            United_Nations = "United Nations"

        class Slovakia(Enum):
            United_Nations = "United Nations"

        class Greece(Enum):
            United_Nations = "United Nations"

        class UK(Enum):
            United_Nations = "United Nations"

        class Third_Reich(Enum):
            United_Nations = "United Nations"

        class Hungary(Enum):
            United_Nations = "United Nations"

        class Abkhazia(Enum):
            United_Nations = "United Nations"

        class Morocco(Enum):
            United_Nations = "United Nations"

        class United_Nations_Peacekeepers(Enum):
            United_Nations = "United Nations"

        class Switzerland(Enum):
            United_Nations = "United Nations"

        class SouthOssetia(Enum):
            United_Nations = "United Nations"

        class Vietnam(Enum):
            United_Nations = "United Nations"

        class China(Enum):
            China_Flying_Dragon_Aviation = "China Flying Dragon Aviation"
            United_Nations = "United Nations"

        class Yemen(Enum):
            United_Nations = "United Nations"

        class Kuwait(Enum):
            United_Nations = "United Nations"

        class Serbia(Enum):
            United_Nations = "United Nations"

        class Oman(Enum):
            United_Nations = "United Nations"

        class India(Enum):
            United_Nations = "United Nations"

        class Egypt(Enum):
            United_Nations = "United Nations"

        class TheNetherlands(Enum):
            United_Nations = "United Nations"

        class Poland(Enum):
            United_Nations = "United Nations"

        class Syria(Enum):
            United_Nations = "United Nations"

        class Finland(Enum):
            United_Nations = "United Nations"

        class Kazakhstan(Enum):
            United_Nations = "United Nations"

        class Denmark(Enum):
            United_Nations = "United Nations"

        class Sweden(Enum):
            United_Nations = "United Nations"

        class Croatia(Enum):
            United_Nations = "United Nations"

        class CzechRepublic(Enum):
            United_Nations = "United Nations"

        class GDR(Enum):
            United_Nations = "United Nations"

        class Yugoslavia(Enum):
            United_Nations = "United Nations"

        class Bulgaria(Enum):
            United_Nations = "United Nations"

        class SouthKorea(Enum):
            United_Nations = "United Nations"

        class Tunisia(Enum):
            United_Nations = "United Nations"

        class Combined_Joint_Task_Forces_Red(Enum):
            _7th_Separate_Brigade_of_AA__Kalinov = "7th Separate Brigade of AA (Kalinov)"
            Algerian_Air_Force_SL_22 = "Algerian Air Force SL-22"
            China_Flying_Dragon_Aviation = "China Flying Dragon Aviation"
            RF_Air_Force = "RF Air Force"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"
            United_Nations = "United Nations"

        class Lebanon(Enum):
            United_Nations = "United Nations"

        class Portugal(Enum):
            United_Nations = "United Nations"

        class Cuba(Enum):
            United_Nations = "United Nations"

        class Insurgents(Enum):
            United_Nations = "United Nations"

        class SaudiArabia(Enum):
            United_Nations = "United Nations"

        class France(Enum):
            United_Nations = "United Nations"

        class USA(Enum):
            United_Nations = "United Nations"

        class Honduras(Enum):
            United_Nations = "United Nations"

        class Qatar(Enum):
            United_Nations = "United Nations"

        class Russia(Enum):
            RF_Air_Force = "RF Air Force"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"
            United_Nations = "United Nations"

        class United_Arab_Emirates(Enum):
            United_Nations = "United Nations"

        class Italian_Social_Republi(Enum):
            United_Nations = "United Nations"

        class Austria(Enum):
            United_Nations = "United Nations"

        class Bahrain(Enum):
            United_Nations = "United Nations"

        class Italy(Enum):
            United_Nations = "United Nations"

        class Chile(Enum):
            United_Nations = "United Nations"

        class Turkey(Enum):
            United_Nations = "United Nations"

        class Philippines(Enum):
            United_Nations = "United Nations"

        class Algeria(Enum):
            Algerian_Air_Force_SL_22 = "Algerian Air Force SL-22"
            United_Nations = "United Nations"

        class Pakistan(Enum):
            United_Nations = "United Nations"

        class Malaysia(Enum):
            United_Nations = "United Nations"

        class Indonesia(Enum):
            United_Nations = "United Nations"

        class Iraq(Enum):
            United_Nations = "United Nations"

        class Germany(Enum):
            United_Nations = "United Nations"

        class South_Africa(Enum):
            United_Nations = "United Nations"

        class Jordan(Enum):
            United_Nations = "United Nations"

        class Mexico(Enum):
            United_Nations = "United Nations"

        class USAFAggressors(Enum):
            United_Nations = "United Nations"

        class Brazil(Enum):
            United_Nations = "United Nations"

        class Spain(Enum):
            United_Nations = "United Nations"

        class Belarus(Enum):
            United_Nations = "United Nations"

        class Canada(Enum):
            United_Nations = "United Nations"

        class NorthKorea(Enum):
            United_Nations = "United Nations"

        class Ethiopia(Enum):
            United_Nations = "United Nations"

        class Japan(Enum):
            United_Nations = "United Nations"

        class Thailand(Enum):
            United_Nations = "United Nations"

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class Ka_27(HelicopterType):
    id = "Ka-27"
    height = 5.2
    width = 15.9
    length = 15.92
    fuel_max = 2616
    max_speed = 290

    class Liveries:

        class Combined_Joint_Task_Forces_Blue(Enum):
            China_PLANAF = "China PLANAF"
            ukraine_camo_1 = "ukraine camo 1"
            standard = "standard"

        class Ukraine(Enum):
            ukraine_camo_1 = "ukraine camo 1"

        class China(Enum):
            China_PLANAF = "China PLANAF"

        class Combined_Joint_Task_Forces_Red(Enum):
            China_PLANAF = "China PLANAF"
            ukraine_camo_1 = "ukraine camo 1"
            standard = "standard"

        class Russia(Enum):
            standard = "standard"

        class Algeria(Enum):
            standard = "standard"

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class UH_60A(HelicopterType):
    id = "UH-60A"
    height = 4.893
    width = 16.4
    length = 18.654
    fuel_max = 1100
    max_speed = 300
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Georgia(Enum):
            standard = "standard"

        class Israel(Enum):
            ISRAIL_UN = "ISRAIL_UN"
            standard = "standard"

        class Combined_Joint_Task_Forces_Blue(Enum):
            ISRAIL_UN = "ISRAIL_UN"
            standard = "standard"

        class Norway(Enum):
            standard = "standard"

        class Ukraine(Enum):
            standard = "standard"

        class Belgium(Enum):
            standard = "standard"

        class UK(Enum):
            standard = "standard"

        class Abkhazia(Enum):
            standard = "standard"

        class United_Nations_Peacekeepers(Enum):
            ISRAIL_UN = "ISRAIL_UN"

        class SouthOssetia(Enum):
            standard = "standard"

        class TheNetherlands(Enum):
            standard = "standard"

        class Denmark(Enum):
            standard = "standard"

        class Combined_Joint_Task_Forces_Red(Enum):
            ISRAIL_UN = "ISRAIL_UN"
            standard = "standard"

        class France(Enum):
            standard = "standard"

        class USA(Enum):
            standard = "standard"

        class Russia(Enum):
            standard = "standard"

        class Italy(Enum):
            standard = "standard"

        class Turkey(Enum):
            standard = "standard"

        class Germany(Enum):
            standard = "standard"

        class Spain(Enum):
            standard = "standard"

        class Canada(Enum):
            standard = "standard"

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class CH_53E(HelicopterType):
    id = "CH-53E"
    large_parking_slot = True
    height = 7.83
    width = 24.08
    length = 30.18
    fuel_max = 2880
    max_speed = 310
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Combined_Joint_Task_Forces_Blue(Enum):
            standard = "standard"

        class Combined_Joint_Task_Forces_Red(Enum):
            standard = "standard"

        class USA(Enum):
            standard = "standard"

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class CH_47D(HelicopterType):
    id = "CH-47D"
    large_parking_slot = True
    height = 5.998
    width = 18.3
    length = 28.3
    fuel_max = 3600
    max_speed = 300
    chaff = 120
    flare = 120
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Australia(Enum):
            Australia_RAAF = "Australia RAAF"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Greek_Army = "Greek Army"
            Australia_RAAF = "Australia RAAF"
            ch_47_green_neth = "ch-47_green neth"
            ch_47_green_spain = "ch-47_green spain"
            ch_47_green_uk = "ch-47_green uk"
            standard = "standard"

        class Greece(Enum):
            Greek_Army = "Greek Army"

        class UK(Enum):
            ch_47_green_uk = "ch-47_green uk"

        class TheNetherlands(Enum):
            ch_47_green_neth = "ch-47_green neth"

        class Combined_Joint_Task_Forces_Red(Enum):
            Greek_Army = "Greek Army"
            Australia_RAAF = "Australia RAAF"
            ch_47_green_neth = "ch-47_green neth"
            ch_47_green_spain = "ch-47_green spain"
            ch_47_green_uk = "ch-47_green uk"
            standard = "standard"

        class USA(Enum):
            standard = "standard"

        class Spain(Enum):
            ch_47_green_spain = "ch-47_green spain"

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class SH_3W(HelicopterType):
    id = "SH-3W"
    large_parking_slot = True
    height = 6.807
    width = 18.91
    length = 30.207
    fuel_max = 2132
    max_speed = 270
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class USSR(Enum):
            standard = "standard"

        class Georgia(Enum):
            standard = "standard"

        class Venezuela(Enum):
            standard = "standard"

        class Australia(Enum):
            standard = "standard"

        class Israel(Enum):
            standard = "standard"

        class Combined_Joint_Task_Forces_Blue(Enum):
            standard = "standard"

        class Sudan(Enum):
            standard = "standard"

        class Norway(Enum):
            standard = "standard"

        class Romania(Enum):
            standard = "standard"

        class Iran(Enum):
            standard = "standard"

        class Ukraine(Enum):
            standard = "standard"

        class Libya(Enum):
            standard = "standard"

        class Belgium(Enum):
            standard = "standard"

        class Slovakia(Enum):
            standard = "standard"

        class Greece(Enum):
            standard = "standard"

        class UK(Enum):
            standard = "standard"

        class Third_Reich(Enum):
            standard = "standard"

        class Hungary(Enum):
            standard = "standard"

        class Abkhazia(Enum):
            standard = "standard"

        class Morocco(Enum):
            standard = "standard"

        class United_Nations_Peacekeepers(Enum):
            standard = "standard"

        class Switzerland(Enum):
            standard = "standard"

        class SouthOssetia(Enum):
            standard = "standard"

        class Vietnam(Enum):
            standard = "standard"

        class China(Enum):
            standard = "standard"

        class Yemen(Enum):
            standard = "standard"

        class Kuwait(Enum):
            standard = "standard"

        class Serbia(Enum):
            standard = "standard"

        class Oman(Enum):
            standard = "standard"

        class India(Enum):
            standard = "standard"

        class Egypt(Enum):
            standard = "standard"

        class TheNetherlands(Enum):
            standard = "standard"

        class Poland(Enum):
            standard = "standard"

        class Syria(Enum):
            standard = "standard"

        class Finland(Enum):
            standard = "standard"

        class Kazakhstan(Enum):
            standard = "standard"

        class Denmark(Enum):
            standard = "standard"

        class Sweden(Enum):
            standard = "standard"

        class Croatia(Enum):
            standard = "standard"

        class CzechRepublic(Enum):
            standard = "standard"

        class GDR(Enum):
            standard = "standard"

        class Yugoslavia(Enum):
            standard = "standard"

        class Bulgaria(Enum):
            standard = "standard"

        class SouthKorea(Enum):
            standard = "standard"

        class Tunisia(Enum):
            standard = "standard"

        class Combined_Joint_Task_Forces_Red(Enum):
            standard = "standard"

        class Lebanon(Enum):
            standard = "standard"

        class Portugal(Enum):
            standard = "standard"

        class Cuba(Enum):
            standard = "standard"

        class Insurgents(Enum):
            standard = "standard"

        class SaudiArabia(Enum):
            standard = "standard"

        class France(Enum):
            standard = "standard"

        class USA(Enum):
            standard = "standard"

        class Honduras(Enum):
            standard = "standard"

        class Qatar(Enum):
            standard = "standard"

        class Russia(Enum):
            standard = "standard"

        class United_Arab_Emirates(Enum):
            standard = "standard"

        class Italian_Social_Republi(Enum):
            standard = "standard"

        class Austria(Enum):
            standard = "standard"

        class Bahrain(Enum):
            standard = "standard"

        class Italy(Enum):
            standard = "standard"

        class Chile(Enum):
            standard = "standard"

        class Turkey(Enum):
            standard = "standard"

        class Philippines(Enum):
            standard = "standard"

        class Algeria(Enum):
            standard = "standard"

        class Pakistan(Enum):
            standard = "standard"

        class Malaysia(Enum):
            standard = "standard"

        class Indonesia(Enum):
            standard = "standard"

        class Iraq(Enum):
            standard = "standard"

        class Germany(Enum):
            standard = "standard"

        class South_Africa(Enum):
            standard = "standard"

        class Jordan(Enum):
            standard = "standard"

        class Mexico(Enum):
            standard = "standard"

        class USAFAggressors(Enum):
            standard = "standard"

        class Brazil(Enum):
            standard = "standard"

        class Spain(Enum):
            standard = "standard"

        class Belarus(Enum):
            standard = "standard"

        class Canada(Enum):
            standard = "standard"

        class NorthKorea(Enum):
            standard = "standard"

        class Ethiopia(Enum):
            standard = "standard"

        class Japan(Enum):
            standard = "standard"

        class Thailand(Enum):
            standard = "standard"

    pylons: Set[int] = set()

    tasks = [task.Transport]
    task_default = task.Transport


class AH_64A(HelicopterType):
    id = "AH-64A"
    height = 4.15
    width = 14.63
    length = 17.87
    fuel_max = 1157
    max_speed = 300
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Israel(Enum):
            ah_64_a_green_isr = "ah-64_a_green isr"

        class Combined_Joint_Task_Forces_Blue(Enum):
            ah_64_a_green_isr = "ah-64_a_green isr"
            ah_64_a_green_neth = "ah-64_a_green neth"
            ah_64_a_green_uk = "ah-64_a_green uk"
            greek_army = "greek army"
            standard = "standard"
            standard_dirty = "standard dirty"

        class Greece(Enum):
            greek_army = "greek army"

        class UK(Enum):
            ah_64_a_green_uk = "ah-64_a_green uk"

        class TheNetherlands(Enum):
            ah_64_a_green_neth = "ah-64_a_green neth"

        class Combined_Joint_Task_Forces_Red(Enum):
            ah_64_a_green_isr = "ah-64_a_green isr"
            ah_64_a_green_neth = "ah-64_a_green neth"
            ah_64_a_green_uk = "ah-64_a_green uk"
            greek_army = "greek army"
            standard = "standard"
            standard_dirty = "standard dirty"

        class USA(Enum):
            standard = "standard"
            standard_dirty = "standard dirty"

    class Pylon1:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (1, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M299___4_x_AGM_114K_Hellfire = (1, Weapons.M299___4_x_AGM_114K_Hellfire)

    class Pylon2:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        M299___4_x_AGM_114K_Hellfire = (2, Weapons.M299___4_x_AGM_114K_Hellfire)

    class Pylon3:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        M299___4_x_AGM_114K_Hellfire = (3, Weapons.M299___4_x_AGM_114K_Hellfire)

    class Pylon4:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M299___4_x_AGM_114K_Hellfire = (4, Weapons.M299___4_x_AGM_114K_Hellfire)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class AH_64D(HelicopterType):
    id = "AH-64D"
    height = 4.15
    width = 14.63
    length = 17.87
    fuel_max = 1157
    max_speed = 280
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Israel(Enum):
            ah_64_d_isr = "ah-64_d_isr"

        class Combined_Joint_Task_Forces_Blue(Enum):
            ah_64_d_green_neth = "ah-64_d_green neth"
            ah_64_d_green_uk = "ah-64_d_green uk"
            ah_64_d_isr = "ah-64_d_isr"
            greek_army = "greek army"
            standard = "standard"

        class Greece(Enum):
            greek_army = "greek army"

        class UK(Enum):
            ah_64_d_green_uk = "ah-64_d_green uk"

        class TheNetherlands(Enum):
            ah_64_d_green_neth = "ah-64_d_green neth"

        class Combined_Joint_Task_Forces_Red(Enum):
            ah_64_d_green_neth = "ah-64_d_green neth"
            ah_64_d_green_uk = "ah-64_d_green uk"
            ah_64_d_isr = "ah-64_d_isr"
            greek_army = "greek army"
            standard = "standard"

        class USA(Enum):
            standard = "standard"

    class Pylon1:
        M299___4_x_AGM_114K_Hellfire = (1, Weapons.M299___4_x_AGM_114K_Hellfire)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (1, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M299___3_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___3_x_AGM_114K_Hellfire__Starboard = (1, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (1, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___1_x_AGM_114K_Hellfire__Starboard = (1, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (1, Weapons.M299___Empty_Launcher)

    class Pylon2:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        M299___4_x_AGM_114K_Hellfire = (2, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___3_x_AGM_114K_Hellfire__Starboard = (2, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (2, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___1_x_AGM_114K_Hellfire__Starboard = (2, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (2, Weapons.M299___Empty_Launcher)

    class Pylon3:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        M299___4_x_AGM_114K_Hellfire = (3, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (3, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___3_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (3, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (3, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___1_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (3, Weapons.M299___Empty_Launcher)

    class Pylon4:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M299___4_x_AGM_114K_Hellfire = (4, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (4, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___3_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (4, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (4, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___1_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (4, Weapons.M299___Empty_Launcher)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class AH_1W(HelicopterType):
    id = "AH-1W"
    height = 3.9
    width = 14.64
    length = 17.27
    fuel_max = 1250.0
    max_speed = 290
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Israel(Enum):
            standard = "standard"

        class Combined_Joint_Task_Forces_Blue(Enum):
            USA_X_Black = "USA X Black"
            USA_Marines = "USA Marines"
            standard = "standard"
            Turkey_1 = "Turkey 1"
            Turkey_2 = "Turkey 2"

        class Combined_Joint_Task_Forces_Red(Enum):
            USA_X_Black = "USA X Black"
            USA_Marines = "USA Marines"
            standard = "standard"
            Turkey_1 = "Turkey 1"
            Turkey_2 = "Turkey 2"

        class USA(Enum):
            USA_X_Black = "USA X Black"
            USA_Marines = "USA Marines"
            standard = "standard"

        class Turkey(Enum):
            Turkey_1 = "Turkey 1"
            Turkey_2 = "Turkey 2"

    class Pylon1:
        M299___4_x_AGM_114K_Hellfire = (1, Weapons.M299___4_x_AGM_114K_Hellfire)
        _4_x_BGM_71D_TOW_ATGM = (1, Weapons._4_x_BGM_71D_TOW_ATGM)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (1, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M260_HYDRA = (1, Weapons.M260_HYDRA)

    class Pylon2:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M260_HYDRA = (2, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (2, Weapons.M260_HYDRA_WP)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)

    class Pylon3:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M260_HYDRA = (3, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (3, Weapons.M260_HYDRA_WP)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)

    class Pylon4:
        M299___4_x_AGM_114K_Hellfire = (4, Weapons.M299___4_x_AGM_114K_Hellfire)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M260_HYDRA = (4, Weapons.M260_HYDRA)
        _4_x_BGM_71D_TOW_ATGM = (4, Weapons._4_x_BGM_71D_TOW_ATGM)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class SH_60B(HelicopterType):
    id = "SH-60B"
    height = 4.893
    width = 16.4
    length = 18.654
    fuel_max = 1100
    max_speed = 240
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Combined_Joint_Task_Forces_Blue(Enum):
            Hellenic_Navy = "Hellenic Navy"
            standard = "standard"

        class Greece(Enum):
            Hellenic_Navy = "Hellenic Navy"

        class Combined_Joint_Task_Forces_Red(Enum):
            Hellenic_Navy = "Hellenic Navy"
            standard = "standard"

        class USA(Enum):
            standard = "standard"

    class Pylon1:
        AGM_119B_Penguin_ASM = (1, Weapons.AGM_119B_Penguin_ASM)

    pylons: Set[int] = {1}

    tasks = [task.AntishipStrike, task.Transport]
    task_default = task.Transport


class UH_1H(HelicopterType):
    id = "UH-1H"
    flyable = True
    height = 4.41
    width = 14.7
    length = 17.62
    fuel_max = 631
    max_speed = 200
    chaff = 0
    flare = 60
    charge_total = 60
    chaff_charge_size = 0
    flare_charge_size = 1
    radio_frequency = 251

    panel_radio = {
        1: {
            "channels": {
                1: 251,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "ExhaustScreen": True,
        "GunnersAISkill": 90,
        "EngineResource": 90,
        "SoloFlight": False,
        "NetCrewControlPriority": 0,
    }

    class Properties:

        class ExhaustScreen:
            id = "ExhaustScreen"

        class GunnersAISkill:
            id = "GunnersAISkill"

        class EngineResource:
            id = "EngineResource"

        class SoloFlight:
            id = "SoloFlight"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Copilot = 1
                Ask_Always = -1
                Equally_Responsible = -2

    class Liveries:

        class Georgia(Enum):
            Georgian_AF_Camo = "Georgian AF Camo"
            Georgian_Air_Force = "Georgian Air Force"

        class Australia(Enum):
            Australia_RAAF_171_Sqn = "Australia RAAF 171 Sqn"
            Australia_RAAF_1968 = "Australia RAAF 1968"
            Australia_Royal_Navy = "Australia Royal Navy"

        class Israel(Enum):
            Israel_Army = "Israel Army"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Italy_15B_Stormo_S_A_R__Soccorso = "Italy 15B Stormo S.A.R -Soccorso"
            Algerian_AF_BV_32 = "Algerian AF BV-32"
            Army_Standard = "Army Standard"
            Canadian_Force = "Canadian Force"
            Italy_E_I__4B_Regg__ALTAIR = "Italy E.I. 4B Regg. ALTAIR"
            French_Army = "French Army"
            Georgian_AF_Camo = "Georgian AF Camo"
            Georgian_Air_Force = "Georgian Air Force"
            Greek_Army_Aviation = "Greek Army Aviation"
            Greek_Army_Aviation_Medic = "Greek Army Aviation Medic"
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"
            Israel_Army = "Israel Army"
            Luftwaffe = "Luftwaffe"
            Italy_Marina_Militare_s_n__80951_7_20 = "Italy Marina Militare s.n. 80951 7-20"
            Norwegian_Coast_Guard__235 = "Norwegian Coast Guard (235)"
            Norwegian_UN = "Norwegian UN"
            _Civilian__Standard = "[Civilian] Standard"
            Australia_RAAF_171_Sqn = "Australia RAAF 171 Sqn"
            Australia_RAAF_1968 = "Australia RAAF 1968"
            RF_Air_Force_Broken = "RF Air Force Broken"
            RF_Air_Force_Grey = "RF Air Force Grey"
            Australia_Royal_Navy = "Australia Royal Navy"
            Royal_Netherlands_AF = "Royal Netherlands AF"
            Spanish_Army = "Spanish Army"
            Spanish_UN = "Spanish UN"
            Turkish_Air_Force = "Turkish Air Force"
            US_ARMY_1972 = "US ARMY 1972"
            US_DOS = "US DOS"
            US_Ft__Rucker = "US Ft. Rucker"
            US_NAVY = "US NAVY"
            USA_Red_Flag = "USA Red Flag"
            USA_UN = "USA UN"
            Ukrainian_Army = "Ukrainian Army"
            XW_PFJ_Air_America = "XW-PFJ Air America"
            _Civilian__Medical = "[Civilian] Medical"
            _Civilian__NASA = "[Civilian] NASA"
            _Civilian__VIP = "[Civilian] VIP"

        class Norway(Enum):
            Norwegian_Coast_Guard__235 = "Norwegian Coast Guard (235)"
            Norwegian_UN = "Norwegian UN"
            _Civilian__Standard = "[Civilian] Standard"

        class Ukraine(Enum):
            Ukrainian_Army = "Ukrainian Army"

        class Belgium(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Greece(Enum):
            Greek_Army_Aviation = "Greek Army Aviation"
            Greek_Army_Aviation_Medic = "Greek Army Aviation Medic"
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"

        class UK(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Abkhazia(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class United_Nations_Peacekeepers(Enum):
            Norwegian_UN = "Norwegian UN"
            Spanish_UN = "Spanish UN"
            USA_UN = "USA UN"

        class SouthOssetia(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class TheNetherlands(Enum):
            Royal_Netherlands_AF = "Royal Netherlands AF"

        class Denmark(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Combined_Joint_Task_Forces_Red(Enum):
            Italy_15B_Stormo_S_A_R__Soccorso = "Italy 15B Stormo S.A.R -Soccorso"
            Algerian_AF_BV_32 = "Algerian AF BV-32"
            Army_Standard = "Army Standard"
            Canadian_Force = "Canadian Force"
            Italy_E_I__4B_Regg__ALTAIR = "Italy E.I. 4B Regg. ALTAIR"
            French_Army = "French Army"
            Georgian_AF_Camo = "Georgian AF Camo"
            Georgian_Air_Force = "Georgian Air Force"
            Greek_Army_Aviation = "Greek Army Aviation"
            Greek_Army_Aviation_Medic = "Greek Army Aviation Medic"
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"
            Israel_Army = "Israel Army"
            Luftwaffe = "Luftwaffe"
            Italy_Marina_Militare_s_n__80951_7_20 = "Italy Marina Militare s.n. 80951 7-20"
            Norwegian_Coast_Guard__235 = "Norwegian Coast Guard (235)"
            Norwegian_UN = "Norwegian UN"
            _Civilian__Standard = "[Civilian] Standard"
            Australia_RAAF_171_Sqn = "Australia RAAF 171 Sqn"
            Australia_RAAF_1968 = "Australia RAAF 1968"
            RF_Air_Force_Broken = "RF Air Force Broken"
            RF_Air_Force_Grey = "RF Air Force Grey"
            Australia_Royal_Navy = "Australia Royal Navy"
            Royal_Netherlands_AF = "Royal Netherlands AF"
            Spanish_Army = "Spanish Army"
            Spanish_UN = "Spanish UN"
            Turkish_Air_Force = "Turkish Air Force"
            US_ARMY_1972 = "US ARMY 1972"
            US_DOS = "US DOS"
            US_Ft__Rucker = "US Ft. Rucker"
            US_NAVY = "US NAVY"
            USA_Red_Flag = "USA Red Flag"
            USA_UN = "USA UN"
            Ukrainian_Army = "Ukrainian Army"
            XW_PFJ_Air_America = "XW-PFJ Air America"
            _Civilian__Medical = "[Civilian] Medical"
            _Civilian__NASA = "[Civilian] NASA"
            _Civilian__VIP = "[Civilian] VIP"

        class Insurgents(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class France(Enum):
            French_Army = "French Army"

        class USA(Enum):
            Army_Standard = "Army Standard"
            _Civilian__Standard = "[Civilian] Standard"
            US_ARMY_1972 = "US ARMY 1972"
            US_DOS = "US DOS"
            US_Ft__Rucker = "US Ft. Rucker"
            US_NAVY = "US NAVY"
            USA_Red_Flag = "USA Red Flag"
            USA_UN = "USA UN"
            XW_PFJ_Air_America = "XW-PFJ Air America"
            _Civilian__Medical = "[Civilian] Medical"
            _Civilian__NASA = "[Civilian] NASA"
            _Civilian__VIP = "[Civilian] VIP"

        class Russia(Enum):
            RF_Air_Force_Broken = "RF Air Force Broken"
            RF_Air_Force_Grey = "RF Air Force Grey"

        class Italy(Enum):
            Italy_15B_Stormo_S_A_R__Soccorso = "Italy 15B Stormo S.A.R -Soccorso"
            Italy_E_I__4B_Regg__ALTAIR = "Italy E.I. 4B Regg. ALTAIR"
            Italy_Marina_Militare_s_n__80951_7_20 = "Italy Marina Militare s.n. 80951 7-20"

        class Turkey(Enum):
            Turkish_Air_Force = "Turkish Air Force"

        class Algeria(Enum):
            Algerian_AF_BV_32 = "Algerian AF BV-32"

        class Germany(Enum):
            Luftwaffe = "Luftwaffe"

        class Spain(Enum):
            Spanish_Army = "Spanish Army"
            Spanish_UN = "Spanish UN"

        class Canada(Enum):
            Canadian_Force = "Canadian Force"

    class Pylon1:
        M134_L = (1, Weapons.M134_L)

    class Pylon2:
        XM158_MK1 = (2, Weapons.XM158_MK1)
        XM158_MK5 = (2, Weapons.XM158_MK5)
        XM158_M151 = (2, Weapons.XM158_M151)
        XM158_M156 = (2, Weapons.XM158_M156)
        XM158_M274 = (2, Weapons.XM158_M274)
        XM158_M257 = (2, Weapons.XM158_M257)
        M261_MK151 = (2, Weapons.M261_MK151)
        M261_MK156 = (2, Weapons.M261_MK156)

    class Pylon3:
        M134_SIDE_L = (3, Weapons.M134_SIDE_L)
        M60_SIDE_L = (3, Weapons.M60_SIDE_L)

    class Pylon4:
        M134_SIDE_R = (4, Weapons.M134_SIDE_R)
        M60_SIDE_R = (4, Weapons.M60_SIDE_R)

    class Pylon5:
        XM158_MK1 = (5, Weapons.XM158_MK1)
        XM158_MK5 = (5, Weapons.XM158_MK5)
        XM158_M151 = (5, Weapons.XM158_M151)
        XM158_M156 = (5, Weapons.XM158_M156)
        XM158_M274 = (5, Weapons.XM158_M274)
        XM158_M257 = (5, Weapons.XM158_M257)
        M261_MK151 = (5, Weapons.M261_MK151)
        M261_MK156 = (5, Weapons.M261_MK156)

    class Pylon6:
        M134_R = (6, Weapons.M134_R)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Transport]
    task_default = task.Transport


class Mi_28N(HelicopterType):
    id = "Mi-28N"
    height = 5.087
    width = 17.2
    length = 17.87
    fuel_max = 1500
    max_speed = 305
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1

    class Liveries:

        class Combined_Joint_Task_Forces_Blue(Enum):
            AAF_SC_11 = "AAF SC-11"
            AAF_SC_12 = "AAF SC-12"
            night = "night"
            standard = "standard"

        class Combined_Joint_Task_Forces_Red(Enum):
            AAF_SC_11 = "AAF SC-11"
            AAF_SC_12 = "AAF SC-12"
            night = "night"
            standard = "standard"

        class Russia(Enum):
            night = "night"
            standard = "standard"

        class Algeria(Enum):
            AAF_SC_11 = "AAF SC-11"
            AAF_SC_12 = "AAF SC-12"

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        _9M114_Shturm_V_8__AT_6_Spiral____ATGM__SACLOS = (1, Weapons._9M114_Shturm_V_8__AT_6_Spiral____ATGM__SACLOS)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (1, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (1, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (1, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (1, Weapons.Fuel_tank_PTB_450)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (1, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        FAB_500_M_62___500kg_GP_Bomb_LD = (1, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (1, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (1, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (2, Weapons.Fuel_tank_PTB_450)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (3, Weapons.Fuel_tank_PTB_450)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (3, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (4, Weapons.Fuel_tank_PTB_450)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (4, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        _9M114_Shturm_V_8__AT_6_Spiral____ATGM__SACLOS = (4, Weapons._9M114_Shturm_V_8__AT_6_Spiral____ATGM__SACLOS)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class OH_58D(HelicopterType):
    id = "OH-58D"
    height = 2.29
    width = 10.53
    length = 10.48
    fuel_max = 454
    max_speed = 220
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        M260_HYDRA = (1, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (1, Weapons.M260_HYDRA_WP)
        AGM114x2_OH_58 = (1, Weapons.AGM114x2_OH_58)
        oh_58_brauning = (1, Weapons.oh_58_brauning)

    class Pylon2:
        M260_HYDRA_WP = (2, Weapons.M260_HYDRA_WP)
        M260_HYDRA = (2, Weapons.M260_HYDRA)
        AGM114x2_OH_58 = (2, Weapons.AGM114x2_OH_58)

    pylons: Set[int] = {1, 2}

    tasks = [task.AFAC, task.Transport, task.GroundAttack, task.Escort, task.AntishipStrike]
    task_default = task.AFAC


class AH_64D_BLK_II(HelicopterType):
    id = "AH-64D_BLK_II"
    flyable = True
    height = 4.15
    width = 14.63
    length = 17.87
    fuel_max = 1438
    max_speed = 365
    chaff = 30
    flare = 60
    charge_total = 90
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True

    panel_radio = {
        1: {
            "channels": {
                7: 141,
                1: 127.5,
                2: 135,
                4: 127,
                8: 128,
                9: 126,
                5: 125,
                10: 137,
                3: 136,
                6: 121
            },
        },
        2: {
            "channels": {
                7: 325,
                1: 225,
                2: 240,
                4: 270,
                8: 350,
                9: 375,
                5: 285,
                10: 390,
                3: 255,
                6: 300
            },
        },
        4: {
            "channels": {
                7: 30.035,
                1: 30,
                2: 30.01,
                4: 30.02,
                8: 30.04,
                9: 30.045,
                5: 30.025,
                10: 30.05,
                3: 30.015,
                6: 30.03
            },
        },
        3: {
            "channels": {
                7: 30.035,
                1: 30,
                2: 30.01,
                4: 30.02,
                8: 30.04,
                9: 30.045,
                5: 30.025,
                10: 30.05,
                3: 30.015,
                6: 30.03
            },
        },
    }

    callnames: Dict[str, List[str]] = {
        "USA": [
            "ArmyAir",
            "Apache",
            "Crow",
            "Chaos",
            "Sioux",
            "Gatling",
            "Gunslinger",
            "Hammerhead",
            "Bootleg",
            "Palehorse",
            "Carnivore",
            "Saber",
        ]
    }

    property_defaults: Dict[str, Any] = {
        "FCR_RFI_removed": True,
        "NetCrewControlPriority": 0,
        "AIDisabled": False,
        "FlareBurstCount": 0,
        "FlareBurstInterval": 0,
        "FlareSalvoCount": 0,
        "FlareSalvoInterval": 0,
        "FlareProgramDelay": 0,
        "PltNVG": True,
        "CpgNVG": True,
    }

    class Properties:

        class FCR_RFI_removed:
            id = "FCR_RFI_removed"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                CPG = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class AIDisabled:
            id = "AIDisabled"

        class FlareBurstCount:
            id = "FlareBurstCount"

            class Values:
                _1 = 0
                _2 = 1
                _3 = 2
                _4 = 3
                _6 = 4
                _8 = 5

        class FlareBurstInterval:
            id = "FlareBurstInterval"

            class Values:
                _0_1 = 0
                _0_2 = 1
                _0_3 = 2
                _0_4 = 3

        class FlareSalvoCount:
            id = "FlareSalvoCount"

            class Values:
                _1 = 0
                _2 = 1
                _4 = 2
                _8 = 3
                Continuous = 4

        class FlareSalvoInterval:
            id = "FlareSalvoInterval"

            class Values:
                _1 = 0
                _2 = 1
                _3 = 2
                _4 = 3
                _5 = 4
                _8 = 5
                Random = 6

        class FlareProgramDelay:
            id = "FlareProgramDelay"

            class Values:
                _1 = 0
                _2 = 1
                _3 = 2
                _4 = 3

        class PltNVG:
            id = "PltNVG"

        class CpgNVG:
            id = "CpgNVG"

    class Liveries:

        class Combined_Joint_Task_Forces_Blue(Enum):
            default = "default"
            _1st_Attack_Helicopter_Battalion_Greece = "1st Attack Helicopter Battalion Greece"
            _301_Squadron_Redskins_Netherlands = "301 Squadron Redskins Netherlands"
            _664_Squadron_9_Regiment_UK = "664 Squadron 9 Regiment UK"
            Archangel_4_2_ARB = "Archangel 4-2 ARB"
            Avengers_1_227th_ARB = "Avengers 1-227th ARB"
            Devils_1_1_ARB = "Devils 1-1 ARB"
            The_Air_Pirates_1_211th_ARB = "The Air Pirates 1-211th ARB"
            Silver_Spurs_3_17_CAV = "Silver Spurs 3-17 CAV"
            Grim_Reapers_4_2_ARB = "Grim Reapers 4-2 ARB"
            Killer_Bees_1_130th_ARB_NCNG = "Killer Bees 1-130th ARB NCNG"
            Gunslingers_2_159th_ARB = "Gunslingers 2-159th ARB"
            Slayers_4_2_ARB = "Slayers 4-2 ARB"
            General_Attack_Recon_Battalion = "General Attack Recon Battalion"
            Wolfpack_1_82_ARB = "Wolfpack 1-82 ARB"

        class UK(Enum):
            _664_Squadron_9_Regiment_UK = "664 Squadron 9 Regiment UK"

        class TheNetherlands(Enum):
            _301_Squadron_Redskins_Netherlands = "301 Squadron Redskins Netherlands"

        class Combined_Joint_Task_Forces_Red(Enum):
            default = "default"
            _1st_Attack_Helicopter_Battalion_Greece = "1st Attack Helicopter Battalion Greece"
            _301_Squadron_Redskins_Netherlands = "301 Squadron Redskins Netherlands"
            _664_Squadron_9_Regiment_UK = "664 Squadron 9 Regiment UK"
            Archangel_4_2_ARB = "Archangel 4-2 ARB"
            Avengers_1_227th_ARB = "Avengers 1-227th ARB"
            Devils_1_1_ARB = "Devils 1-1 ARB"
            The_Air_Pirates_1_211th_ARB = "The Air Pirates 1-211th ARB"
            Silver_Spurs_3_17_CAV = "Silver Spurs 3-17 CAV"
            Grim_Reapers_4_2_ARB = "Grim Reapers 4-2 ARB"
            Killer_Bees_1_130th_ARB_NCNG = "Killer Bees 1-130th ARB NCNG"
            Gunslingers_2_159th_ARB = "Gunslingers 2-159th ARB"
            Slayers_4_2_ARB = "Slayers 4-2 ARB"
            General_Attack_Recon_Battalion = "General Attack Recon Battalion"
            Wolfpack_1_82_ARB = "Wolfpack 1-82 ARB"

        class USA(Enum):
            default = "default"
            Archangel_4_2_ARB = "Archangel 4-2 ARB"
            Avengers_1_227th_ARB = "Avengers 1-227th ARB"
            Devils_1_1_ARB = "Devils 1-1 ARB"
            The_Air_Pirates_1_211th_ARB = "The Air Pirates 1-211th ARB"
            Silver_Spurs_3_17_CAV = "Silver Spurs 3-17 CAV"
            Grim_Reapers_4_2_ARB = "Grim Reapers 4-2 ARB"
            Killer_Bees_1_130th_ARB_NCNG = "Killer Bees 1-130th ARB NCNG"
            Gunslingers_2_159th_ARB = "Gunslingers 2-159th ARB"
            Slayers_4_2_ARB = "Slayers 4-2 ARB"
            General_Attack_Recon_Battalion = "General Attack Recon Battalion"
            Wolfpack_1_82_ARB = "Wolfpack 1-82 ARB"

    class Pylon1:
        M261_MK151 = (1, Weapons.M261_MK151)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_ = (1, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk = (1, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP = (1, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP = (1, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP)
        M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M274_Hydra__6SK_ = (1, Weapons.M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M274_Hydra__6SK_)
        M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M257_Hydra__6IL_ = (1, Weapons.M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M257_Hydra__6IL_)
        M299___4_x_AGM_114K_Hellfire = (1, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___2_x_AGM_114K_Hellfire = (1, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___Empty_Launcher = (1, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (1, Weapons.Fuel_tank_230_gal)

    class Pylon2:
        M261_MK151 = (2, Weapons.M261_MK151)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_ = (2, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk = (2, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP = (2, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP = (2, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP)
        M261_Inboard_Launcher__Zone_C_M274_Hydra__6SK___Zones_D_E_M151_Hydra__6PD_ = (2, Weapons.M261_Inboard_Launcher__Zone_C_M274_Hydra__6SK___Zones_D_E_M151_Hydra__6PD_)
        M261_Inboard_Launcher__Zone_C_M257_Hydra__6IL___Zones_D_E_M151_Hydra__6PD_ = (2, Weapons.M261_Inboard_Launcher__Zone_C_M257_Hydra__6IL___Zones_D_E_M151_Hydra__6PD_)
        M299___4_x_AGM_114K_Hellfire = (2, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___2_x_AGM_114K_Hellfire = (2, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___Empty_Launcher = (2, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (2, Weapons.Fuel_tank_230_gal)

    class Pylon3:
        M261_MK151 = (3, Weapons.M261_MK151)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_ = (3, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk = (3, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP = (3, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP = (3, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP)
        M261_Inboard_Launcher__Zone_C_M274_Hydra__6SK___Zones_D_E_M151_Hydra__6PD_ = (3, Weapons.M261_Inboard_Launcher__Zone_C_M274_Hydra__6SK___Zones_D_E_M151_Hydra__6PD_)
        M261_Inboard_Launcher__Zone_C_M257_Hydra__6IL___Zones_D_E_M151_Hydra__6PD_ = (3, Weapons.M261_Inboard_Launcher__Zone_C_M257_Hydra__6IL___Zones_D_E_M151_Hydra__6PD_)
        M299___4_x_AGM_114K_Hellfire = (3, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (3, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (3, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (3, Weapons.Fuel_tank_230_gal)

    class Pylon4:
        M261_MK151 = (4, Weapons.M261_MK151)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_ = (4, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M257__Illum_)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk = (4, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M274__Smk)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP = (4, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M229__HEDP)
        M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP = (4, Weapons.M261_pod___19_x_2_75_Hydra__UnGd_Rkts_M282__MPP)
        M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M274_Hydra__6SK_ = (4, Weapons.M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M274_Hydra__6SK_)
        M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M257_Hydra__6IL_ = (4, Weapons.M261_Outboard_Launcher__Zones_A_B_M151_Hydra__6PD___Zone_E_M257_Hydra__6IL_)
        M299___4_x_AGM_114K_Hellfire = (4, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (4, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (4, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (4, Weapons.Fuel_tank_230_gal)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Mi_24P(HelicopterType):
    id = "Mi-24P"
    flyable = True
    height = 4.354
    width = 17.3
    length = 20.953
    fuel_max = 1701
    max_speed = 330
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 1
    flare_charge_size = 1

    panel_radio = {
        1: {
            "channels": {
                1: 127.5,
                2: 135,
                4: 127,
                8: 128,
                16: 132,
                17: 138,
                9: 126,
                18: 122,
                5: 125,
                10: 133,
                20: 137,
                11: 130,
                3: 136,
                6: 121,
                12: 129,
                13: 123,
                7: 141,
                14: 131,
                19: 124,
                15: 134
            },
        },
        2: {
            "channels": {
                7: 40,
                1: 21.5,
                2: 25.7,
                4: 28,
                8: 50,
                9: 55.5,
                5: 30,
                10: 59.9,
                3: 27,
                6: 32
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "ExhaustScreen": True,
        "LeftEngineResource": 90,
        "RightEngineResource": 90,
        "GunnersAISkill": 90,
        "NetCrewControlPriority": 0,
        "NS430allow": True,
        "SimplifiedAI": False,
        "HideAngleBoxes": False,
        "TrackAirTargets": True,
        "PilotNVG": True,
        "OperatorNVG": True,
    }

    class Properties:

        class ExhaustScreen:
            id = "ExhaustScreen"

        class LeftEngineResource:
            id = "LeftEngineResource"

        class RightEngineResource:
            id = "RightEngineResource"

        class GunnersAISkill:
            id = "GunnersAISkill"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Copilot_gunner = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class NS430allow:
            id = "NS430allow"

        class SimplifiedAI:
            id = "SimplifiedAI"

        class HideAngleBoxes:
            id = "HideAngleBoxes"

        class TrackAirTargets:
            id = "TrackAirTargets"

        class PilotNVG:
            id = "PilotNVG"

        class OperatorNVG:
            id = "OperatorNVG"

    class Liveries:

        class USSR(Enum):
            Russian_Air_Force = "Russian Air Force"
            AF_Standard3_Old = "AF Standard3 Old"

        class Georgia(Enum):
            Georgian_Air_Force = "Georgian Air Force"
            United_Nations = "United Nations"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Georgian_Air_Force = "Georgian Air Force"
            IQAF = "IQAF"
            Russian_Air_Force = "Russian Air Force"
            SyAAF = "SyAAF"
            Ukrainian_Army_Aviation = "Ukrainian Army Aviation"
            United_Nations = "United Nations"
            AF_Standard3_Old = "AF Standard3 Old"

        class Ukraine(Enum):
            Ukrainian_Army_Aviation = "Ukrainian Army Aviation"
            United_Nations = "United Nations"

        class United_Nations_Peacekeepers(Enum):
            United_Nations = "United Nations"

        class Syria(Enum):
            SyAAF = "SyAAF"

        class Combined_Joint_Task_Forces_Red(Enum):
            Georgian_Air_Force = "Georgian Air Force"
            IQAF = "IQAF"
            Russian_Air_Force = "Russian Air Force"
            SyAAF = "SyAAF"
            Ukrainian_Army_Aviation = "Ukrainian Army Aviation"
            United_Nations = "United Nations"
            AF_Standard3_Old = "AF Standard3 Old"

        class Russia(Enum):
            Russian_Air_Force = "Russian Air Force"
            United_Nations = "United Nations"
            AF_Standard3_Old = "AF Standard3 Old"

        class Iraq(Enum):
            IQAF = "IQAF"

    class Pylon1:
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (1, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT = (1, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE = (1, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag = (1, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag)
        _9M114_Shturm_V_2_Rack = (1, Weapons._9M114_Shturm_V_2_Rack)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        UB_32A_24_pod___32_x_S_5KO = (2, Weapons.UB_32A_24_pod___32_x_S_5KO)
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (2, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT = (2, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE = (2, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag = (2, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (2, Weapons.Fuel_tank_PTB_450)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        APU_68___S_24B = (2, Weapons.APU_68___S_24B)
        GUV_VOG = (2, Weapons.GUV_VOG)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        UB_32A_24_pod___32_x_S_5KO = (3, Weapons.UB_32A_24_pod___32_x_S_5KO)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (3, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (3, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (3, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (3, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Fuel_tank_PTB_450 = (3, Weapons.Fuel_tank_PTB_450)
        APU_68___S_24B = (3, Weapons.APU_68___S_24B)
        GUV_YakB_GSHP = (3, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (3, Weapons.GUV_VOG)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        UB_32A_24_pod___32_x_S_5KO = (4, Weapons.UB_32A_24_pod___32_x_S_5KO)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (4, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (4, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (4, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP = (4, Weapons.RBK_500_255___30_x_PTAB_10_5__500kg_CBU_Heavy_HEAT_AP)
        RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP = (4, Weapons.RBK_500___268_x_PTAB_1M__500kg_CBU_Light_HEAT_AP)
        RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag = (4, Weapons.RBK_500U___126_x_OAB_2_5RT__500kg_CBU_HE_Frag)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        Fuel_tank_PTB_450 = (4, Weapons.Fuel_tank_PTB_450)
        APU_68___S_24B = (4, Weapons.APU_68___S_24B)
        GUV_YakB_GSHP = (4, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (4, Weapons.GUV_VOG)

    class Pylon5:
        B_8V20A_CM = (5, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (5, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (5, Weapons.B_8V20A_OM)
        UB_32A_24_pod___32_x_S_5KO = (5, Weapons.UB_32A_24_pod___32_x_S_5KO)
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (5, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT = (5, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE = (5, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag = (5, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (5, Weapons.Fuel_tank_PTB_450)
        B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8V20A_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        APU_68___S_24B = (5, Weapons.APU_68___S_24B)
        GUV_VOG = (5, Weapons.GUV_VOG)

    class Pylon6:
        _9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS = (6, Weapons._9M114_Shturm_V_2__AT_6_Spiral____ATGM__SACLOS)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT = (6, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE = (6, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag = (6, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag)
        _9M114_Shturm_V_2_Rack = (6, Weapons._9M114_Shturm_V_2_Rack)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.Transport, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class SA342M(HelicopterType):
    id = "SA342M"
    flyable = True
    height = 3.192
    width = 10.5
    length = 11.97
    fuel_max = 416.33
    max_speed = 240
    chaff = 0
    flare = 32
    charge_total = 32
    chaff_charge_size = 0
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 41,
                2: 31,
                8: 50,
                3: 32,
                1: 30,
                4: 33,
                5: 40,
                7: 42
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "NS430allow": True,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

    class Liveries:

        class Israel(Enum):
            Israel_Fictional = "Israel Fictional"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Greece(Enum):
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"

        class UK(Enum):
            UK_Fictional = "UK Fictional"

        class Serbia(Enum):
            Serbia_Fictional = "Serbia Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class TheNetherlands(Enum):
            Dutch_Fictional = "Dutch Fictional"

        class Syria(Enum):
            Syria_Fictional = "Syria Fictional"

        class Combined_Joint_Task_Forces_Red(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Portugal(Enum):
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"

        class France(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"

        class USA(Enum):
            US_Marines_Fictional = "US Marines Fictional"

        class Russia(Enum):
            Russia_Fictional = "Russia Fictional"

        class Germany(Enum):
            Germany_Fictional = "Germany Fictional"

    class Pylon1:
        HOT3_ = (1, Weapons.HOT3_)

    class Pylon2:
        HOT3 = (2, Weapons.HOT3)

    class Pylon3:
        HOT3_ = (3, Weapons.HOT3_)

    class Pylon4:
        HOT3 = (4, Weapons.HOT3)

    class Pylon5:
        Sand_Filter = (5, Weapons.Sand_Filter)

    class Pylon6:
        IR_Deflector = (6, Weapons.IR_Deflector)

    class Pylon7:
        Dipole_Antanna__aesthetic_ = (7, Weapons.Dipole_Antanna__aesthetic_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.CAS


class SA342L(HelicopterType):
    id = "SA342L"
    flyable = True
    height = 3.192
    width = 10.5
    length = 11.97
    fuel_max = 416.33
    max_speed = 240
    chaff = 0
    flare = 32
    charge_total = 32
    chaff_charge_size = 0
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 41,
                2: 31,
                8: 50,
                3: 32,
                1: 30,
                4: 33,
                5: 40,
                7: 42
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "NS430allow": True,
        "SA342RemoveDoors": False,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

        class SA342RemoveDoors:
            id = "SA342RemoveDoors"

    class Liveries:

        class Israel(Enum):
            Israel_Fictional = "Israel Fictional"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Greece(Enum):
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"

        class UK(Enum):
            UK_Fictional = "UK Fictional"

        class Serbia(Enum):
            Serbia_Fictional = "Serbia Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class TheNetherlands(Enum):
            Dutch_Fictional = "Dutch Fictional"

        class Syria(Enum):
            Syria_Fictional = "Syria Fictional"

        class Combined_Joint_Task_Forces_Red(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Portugal(Enum):
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"

        class France(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"

        class USA(Enum):
            US_Marines_Fictional = "US Marines Fictional"

        class Russia(Enum):
            Russia_Fictional = "Russia Fictional"

        class Germany(Enum):
            Germany_Fictional = "Germany Fictional"
#ERRR {GIAT_M621G}

    class Pylon2:
        LAU_SNEB68G___8xSNEB68_EAP = (2, Weapons.LAU_SNEB68G___8xSNEB68_EAP)
        LAU_SNEB68G___8xSNEB68_WP = (2, Weapons.LAU_SNEB68G___8xSNEB68_WP)

    class Pylon5:
        Sand_Filter = (5, Weapons.Sand_Filter)

    class Pylon6:
        IR_Deflector = (6, Weapons.IR_Deflector)

    class Pylon7:
        Dipole_Antanna__aesthetic_ = (7, Weapons.Dipole_Antanna__aesthetic_)

    pylons: Set[int] = {1, 2, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.CAS


class SA342Mistral(HelicopterType):
    id = "SA342Mistral"
    flyable = True
    height = 3.192
    width = 10.5
    length = 11.97
    fuel_max = 416.33
    max_speed = 240
    chaff = 0
    flare = 32
    charge_total = 32
    chaff_charge_size = 0
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 41,
                2: 31,
                8: 50,
                3: 32,
                1: 30,
                4: 33,
                5: 40,
                7: 42
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "NS430allow": True,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

    class Liveries:

        class Israel(Enum):
            Israel_Fictional = "Israel Fictional"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Greece(Enum):
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"

        class UK(Enum):
            UK_Fictional = "UK Fictional"

        class Serbia(Enum):
            Serbia_Fictional = "Serbia Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class TheNetherlands(Enum):
            Dutch_Fictional = "Dutch Fictional"

        class Syria(Enum):
            Syria_Fictional = "Syria Fictional"

        class Combined_Joint_Task_Forces_Red(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Portugal(Enum):
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"

        class France(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"

        class USA(Enum):
            US_Marines_Fictional = "US Marines Fictional"

        class Russia(Enum):
            Russia_Fictional = "Russia Fictional"

        class Germany(Enum):
            Germany_Fictional = "Germany Fictional"

    class Pylon1:
        Mistral_ = (1, Weapons.Mistral_)

    class Pylon2:
        Mistral = (2, Weapons.Mistral)

    class Pylon3:
        Mistral_ = (3, Weapons.Mistral_)

    class Pylon4:
        Mistral = (4, Weapons.Mistral)

    class Pylon5:
        Sand_Filter = (5, Weapons.Sand_Filter)

    class Pylon6:
        IR_Deflector = (6, Weapons.IR_Deflector)

    class Pylon7:
        Dipole_Antanna__aesthetic_ = (7, Weapons.Dipole_Antanna__aesthetic_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.Escort


class SA342Minigun(HelicopterType):
    id = "SA342Minigun"
    flyable = True
    height = 3.192
    width = 10.5
    length = 11.97
    fuel_max = 416.33
    max_speed = 240
    chaff = 0
    flare = 32
    charge_total = 32
    chaff_charge_size = 0
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 41,
                2: 31,
                8: 50,
                3: 32,
                1: 30,
                4: 33,
                5: 40,
                7: 42
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "NS430allow": True,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

    class Liveries:

        class Israel(Enum):
            Israel_Fictional = "Israel Fictional"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Greece(Enum):
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"

        class UK(Enum):
            UK_Fictional = "UK Fictional"

        class Serbia(Enum):
            Serbia_Fictional = "Serbia Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class TheNetherlands(Enum):
            Dutch_Fictional = "Dutch Fictional"

        class Syria(Enum):
            Syria_Fictional = "Syria Fictional"

        class Combined_Joint_Task_Forces_Red(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Cyprus_air_force = "Cyprus air force"
            Germany_Fictional = "Germany Fictional"
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"
            Israel_Fictional = "Israel Fictional"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Dutch_Fictional = "Dutch Fictional"
            Russia_Fictional = "Russia Fictional"
            Serbia_Fictional = "Serbia Fictional"
            Syria_Fictional = "Syria Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"
            UK_Fictional = "UK Fictional"
            US_Marines_Fictional = "US Marines Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class Portugal(Enum):
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"

        class France(Enum):
            Combat = "Combat"
            Combat_sable = "Combat sable"
            Portuguese_Modern_Fictional = "Portuguese Modern Fictional"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"
            Training_EALAT = "Training EALAT"

        class USA(Enum):
            US_Marines_Fictional = "US Marines Fictional"

        class Russia(Enum):
            Russia_Fictional = "Russia Fictional"

        class Germany(Enum):
            Germany_Fictional = "Germany Fictional"
#ERRR {MINIGUN}

    class Pylon5:
        Sand_Filter = (5, Weapons.Sand_Filter)

    class Pylon6:
        IR_Deflector = (6, Weapons.IR_Deflector)

    pylons: Set[int] = {1, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.CAS


helicopter_map = {
    "Ka-50": Ka_50,
    "Mi-24V": Mi_24V,
    "Mi-8MT": Mi_8MT,
    "Mi-26": Mi_26,
    "Ka-27": Ka_27,
    "UH-60A": UH_60A,
    "CH-53E": CH_53E,
    "CH-47D": CH_47D,
    "SH-3W": SH_3W,
    "AH-64A": AH_64A,
    "AH-64D": AH_64D,
    "AH-1W": AH_1W,
    "SH-60B": SH_60B,
    "UH-1H": UH_1H,
    "Mi-28N": Mi_28N,
    "OH-58D": OH_58D,
    "AH-64D_BLK_II": AH_64D_BLK_II,
    "Mi-24P": Mi_24P,
    "SA342M": SA342M,
    "SA342L": SA342L,
    "SA342Mistral": SA342Mistral,
    "SA342Minigun": SA342Minigun,
}
