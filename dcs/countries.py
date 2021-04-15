# This file is generated from pydcs_export.lua

from dcs.country import Country
import dcs.vehicles as vehicles
import dcs.planes as planes
import dcs.helicopters as helicopters
import dcs.ships as ships


class Russia(Country):
    id = 0
    name = "Russia"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm

        class Infantry:
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            APC_Tigr = vehicles.Unarmed.APC_Tigr
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            MBT_T_90 = vehicles.Armor.MBT_T_90
            MBT_T_72B3 = vehicles.Armor.MBT_T_72B3
            APC_BTR_82A = vehicles.Armor.APC_BTR_82A

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Su_33 = planes.Su_33
        Su_25 = planes.Su_25
        MiG_29S = planes.MiG_29S
        MiG_29A = planes.MiG_29A
        Su_27 = planes.Su_27
        Su_25TM = planes.Su_25TM
        Su_25T = planes.Su_25T
        MiG_31 = planes.MiG_31
        MiG_27K = planes.MiG_27K
        Su_30 = planes.Su_30
        Tu_160 = planes.Tu_160
        Su_34 = planes.Su_34
        Tu_95MS = planes.Tu_95MS
        Tu_142 = planes.Tu_142
        MiG_25PD = planes.MiG_25PD
        Tu_22M3 = planes.Tu_22M3
        A_50 = planes.A_50
        Yak_40 = planes.Yak_40
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        Su_17M4 = planes.Su_17M4
        MiG_23MLD = planes.MiG_23MLD
        MiG_25RBT = planes.MiG_25RBT
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        IL_78M = planes.IL_78M
        IL_76MD = planes.IL_76MD
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Yak_52 = planes.Yak_52
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Su_33,
        Plane.Su_25,
        Plane.MiG_29S,
        Plane.MiG_29A,
        Plane.Su_27,
        Plane.Su_25TM,
        Plane.Su_25T,
        Plane.MiG_31,
        Plane.MiG_27K,
        Plane.Su_30,
        Plane.Tu_160,
        Plane.Su_34,
        Plane.Tu_95MS,
        Plane.Tu_142,
        Plane.MiG_25PD,
        Plane.Tu_22M3,
        Plane.A_50,
        Plane.Yak_40,
        Plane.An_26B,
        Plane.An_30M,
        Plane.Su_17M4,
        Plane.MiG_23MLD,
        Plane.MiG_25RBT,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.IL_78M,
        Plane.IL_76MD,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Yak_52,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        Ka_27 = helicopters.Ka_27
        Mi_28N = helicopters.Mi_28N
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.Ka_27,
        Helicopter.Mi_28N,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        Cruiser_1164_Moskva = ships.Cruiser_1164_Moskva
        Battlecruiser_1144_2_Pyotr_Velikiy = ships.Battlecruiser_1144_2_Pyotr_Velikiy
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        SSK_636_Improved_Kilo = ships.SSK_636_Improved_Kilo
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        Frigate_11540_Neustrashimy = ships.Frigate_11540_Neustrashimy
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Russia, self).__init__(Russia.id, Russia.name)


class Ukraine(Country):
    id = 1
    name = "Ukraine"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm

        class Infantry:
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Su_27 = planes.Su_27
        MiG_29A = planes.MiG_29A
        MiG_29S = planes.MiG_29S
        Su_17M4 = planes.Su_17M4
        Tu_95MS = planes.Tu_95MS
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        MiG_25PD = planes.MiG_25PD
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        MiG_23MLD = planes.MiG_23MLD
        IL_78M = planes.IL_78M
        IL_76MD = planes.IL_76MD
        MiG_27K = planes.MiG_27K
        Tu_22M3 = planes.Tu_22M3
        MiG_25RBT = planes.MiG_25RBT
        Yak_40 = planes.Yak_40
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Su_27,
        Plane.MiG_29A,
        Plane.MiG_29S,
        Plane.Su_17M4,
        Plane.Tu_95MS,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.MiG_25PD,
        Plane.An_26B,
        Plane.An_30M,
        Plane.MiG_23MLD,
        Plane.IL_78M,
        Plane.IL_76MD,
        Plane.MiG_27K,
        Plane.Tu_22M3,
        Plane.MiG_25RBT,
        Plane.Yak_40,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        Ka_27 = helicopters.Ka_27
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.Ka_27,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Ukraine, self).__init__(Ukraine.id, Ukraine.name)


class USA(Country):
    id = 2
    name = "USA"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class Infantry:
            Infantry_M249 = vehicles.Infantry.Infantry_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand

        class AirDefence:
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_Linebacker___Bradley_M6 = vehicles.AirDefence.SAM_Linebacker___Bradley_M6
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford

        class Armor:
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            APC_M113 = vehicles.Armor.APC_M113
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            IFV_M1126_Stryker_ICV = vehicles.Armor.IFV_M1126_Stryker_ICV
            SPG_Stryker_MGS = vehicles.Armor.SPG_Stryker_MGS
            ATGM_Stryker = vehicles.Armor.ATGM_Stryker
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch

        class Locomotive:
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Well_Car = vehicles.Carriage.Well_Car
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        A_10A = planes.A_10A
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        C_130 = planes.C_130
        C_17A = planes.C_17A
        E_2C = planes.E_2C
        E_3A = planes.E_3A
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        F_16A = planes.F_16A
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_A_18C = planes.F_A_18C
        KC_135 = planes.KC_135
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        RQ_1A_Predator = planes.RQ_1A_Predator
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        An_26B = planes.An_26B
        B_17G = planes.B_17G
        F_16A_MLU = planes.F_16A_MLU
        F_16C_bl_50 = planes.F_16C_bl_50
        F_4E = planes.F_4E
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        F_A_18A = planes.F_A_18A
        FA_18C_hornet = planes.FA_18C_hornet
        KC135MPRS = planes.KC135MPRS
        L_39C = planes.L_39C
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        MQ_9_Reaper = planes.MQ_9_Reaper
        Christen_Eagle_II = planes.Christen_Eagle_II
        AV8BNA = planes.AV8BNA
        Hawk = planes.Hawk
        KC130 = planes.KC130
        A_10C_2 = planes.A_10C_2
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        A_20G = planes.A_20G
        AJS37 = planes.AJS37
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.A_10A,
        Plane.B_1B,
        Plane.B_52H,
        Plane.C_130,
        Plane.C_17A,
        Plane.E_2C,
        Plane.E_3A,
        Plane.F_117A,
        Plane.F_14A,
        Plane.F_15C,
        Plane.F_15E,
        Plane.F_16A,
        Plane.F_16C_bl_52d,
        Plane.F_A_18C,
        Plane.KC_135,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.RQ_1A_Predator,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.An_26B,
        Plane.B_17G,
        Plane.F_16A_MLU,
        Plane.F_16C_bl_50,
        Plane.F_4E,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.F_A_18A,
        Plane.FA_18C_hornet,
        Plane.KC135MPRS,
        Plane.L_39C,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.MQ_9_Reaper,
        Plane.Christen_Eagle_II,
        Plane.AV8BNA,
        Plane.Hawk,
        Plane.KC130,
        Plane.A_10C_2,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.A_20G,
        Plane.AJS37,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        AH_1W = helicopters.AH_1W
        UH_60A = helicopters.UH_60A
        CH_47D = helicopters.CH_47D
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E
        OH_58D = helicopters.OH_58D
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.AH_1W,
        Helicopter.UH_60A,
        Helicopter.CH_47D,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
        Helicopter.OH_58D,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        CG_Ticonderoga = ships.CG_Ticonderoga
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins
        LST_Mk_II = ships.LST_Mk_II
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        DDG_Arleigh_Burke_IIa = ships.DDG_Arleigh_Burke_IIa
        CVN_71_Theodore_Roosevelt = ships.CVN_71_Theodore_Roosevelt
        CVN_72_Abraham_Lincoln = ships.CVN_72_Abraham_Lincoln
        CVN_73_George_Washington = ships.CVN_73_George_Washington
        CVN_75_Harry_S__Truman = ships.CVN_75_Harry_S__Truman
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(USA, self).__init__(USA.id, USA.name)


class Turkey(Country):
    id = 3
    name = "Turkey"

    class Vehicle:

        class Artillery:
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm

        class AirDefence:
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        F_16C_bl_50 = planes.F_16C_bl_50
        F_4E = planes.F_4E
        C_130 = planes.C_130
        P_51D = planes.P_51D
        KC_135 = planes.KC_135
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        KC135MPRS = planes.KC135MPRS
        RQ_1A_Predator = planes.RQ_1A_Predator
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MQ_9_Reaper = planes.MQ_9_Reaper
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.F_16C_bl_50,
        Plane.F_4E,
        Plane.C_130,
        Plane.P_51D,
        Plane.KC_135,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.KC135MPRS,
        Plane.RQ_1A_Predator,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MQ_9_Reaper,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        Mi_8MT = helicopters.Mi_8MT
        AH_1W = helicopters.AH_1W
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.Mi_8MT,
        Helicopter.AH_1W,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Turkey, self).__init__(Turkey.id, Turkey.name)


class UK(Country):
    id = 4
    name = "UK"

    class Vehicle:

        class Artillery:
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class Infantry:
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo

        class Armor:
            IFV_Warrior = vehicles.Armor.IFV_Warrior
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Tornado_GR4 = planes.Tornado_GR4
        C_130 = planes.C_130
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        MQ_9_Reaper = planes.MQ_9_Reaper
        AV8BNA = planes.AV8BNA
        Hawk = planes.Hawk
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        B_17G = planes.B_17G
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.Tornado_GR4,
        Plane.C_130,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.MQ_9_Reaper,
        Plane.AV8BNA,
        Plane.Hawk,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.B_17G,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        LST_Mk_II = ships.LST_Mk_II
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Solex = "Solex"
        Image = "Image"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Solex,
            CallsignAWACS.Image
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(UK, self).__init__(UK.id, UK.name)


class France(Country):
    id = 5
    name = "France"

    class Vehicle:

        class Artillery:
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo

        class Armor:
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Mirage_2000_5 = planes.Mirage_2000_5
        C_130 = planes.C_130
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        E_2C = planes.E_2C
        E_3A = planes.E_3A
        KC_135 = planes.KC_135
        KC135MPRS = planes.KC135MPRS
        L_39C = planes.L_39C
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        MQ_9_Reaper = planes.MQ_9_Reaper
        M_2000C = planes.M_2000C
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Mirage_2000_5,
        Plane.C_130,
        Plane.P_51D,
        Plane.C_17A,
        Plane.E_2C,
        Plane.E_3A,
        Plane.KC_135,
        Plane.KC135MPRS,
        Plane.L_39C,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.MQ_9_Reaper,
        Plane.M_2000C,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Cyrano = "Cyrano"
        Roxanne = "Roxanne"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Cyrano,
            CallsignAWACS.Roxanne
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(France, self).__init__(France.id, France.name)


class Germany(Country):
    id = 6
    name = "Germany"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            IFV_Marder = vehicles.Armor.IFV_Marder
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH

        class Carriage:
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car

    class Plane:
        A_10C = planes.A_10C
        MiG_29G = planes.MiG_29G
        F_4E = planes.F_4E
        Tornado_IDS = planes.Tornado_IDS
        P_51D = planes.P_51D
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        Su_17M4 = planes.Su_17M4
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        MiG_29A = planes.MiG_29A
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.MiG_29G,
        Plane.F_4E,
        Plane.Tornado_IDS,
        Plane.P_51D,
        Plane.An_26B,
        Plane.C_17A,
        Plane.E_3A,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.Su_17M4,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.MiG_29A,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Germany, self).__init__(Germany.id, Germany.name)


class USAFAggressors(Country):
    id = 7
    name = "USAF Aggressors"

    class Vehicle:

        class Artillery:
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            PLZ_05 = vehicles.Artillery.PLZ_05

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_AK_74 = vehicles.Infantry.Infantry_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG
            Infantry_M249 = vehicles.Infantry.Infantry_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M4_Georgia = vehicles.Infantry.Infantry_M4_Georgia
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            AAA_ZU_23_Closed_Emplacement_Insurgent = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            MANPADS_SA_18_Igla_Grouse_Ins = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_Ins
            SAM_Linebacker___Bradley_M6 = vehicles.AirDefence.SAM_Linebacker___Bradley_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            APC_Tigr = vehicles.Unarmed.APC_Tigr

        class Armor:
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_T_72B3 = vehicles.Armor.MBT_T_72B3
            APC_BTR_82A = vehicles.Armor.APC_BTR_82A
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_IV = vehicles.Armor.MBT_Merkava_IV
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            IFV_M1126_Stryker_ICV = vehicles.Armor.IFV_M1126_Stryker_ICV
            SPG_Stryker_MGS = vehicles.Armor.SPG_Stryker_MGS
            ATGM_Stryker = vehicles.Armor.ATGM_Stryker
            IFV_Warrior = vehicles.Armor.IFV_Warrior

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        J_11A = planes.J_11A
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        P_51D_30_NA = planes.P_51D_30_NA
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        Mirage_2000_5 = planes.Mirage_2000_5
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        KJ_2000 = planes.KJ_2000
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.J_11A,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.P_51D_30_NA,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.Mirage_2000_5,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.KJ_2000,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        SSK_636_Improved_Kilo = ships.SSK_636_Improved_Kilo
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Cruiser_1164_Moskva = ships.Cruiser_1164_Moskva
        Frigate_11540_Neustrashimy = ships.Frigate_11540_Neustrashimy
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Battlecruiser_1144_2_Pyotr_Velikiy = ships.Battlecruiser_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        CG_Ticonderoga = ships.CG_Ticonderoga
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        DDG_Arleigh_Burke_IIa = ships.DDG_Arleigh_Burke_IIa
        CVN_71_Theodore_Roosevelt = ships.CVN_71_Theodore_Roosevelt
        CVN_72_Abraham_Lincoln = ships.CVN_72_Abraham_Lincoln
        CVN_73_George_Washington = ships.CVN_73_George_Washington
        CVN_75_Harry_S__Truman = ships.CVN_75_Harry_S__Truman

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(USAFAggressors, self).__init__(USAFAggressors.id, USAFAggressors.name)


class Canada(Country):
    id = 8
    name = "Canada"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        F_A_18C = planes.F_A_18C
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.F_A_18C,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        LST_Mk_II = ships.LST_Mk_II
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Canada, self).__init__(Canada.id, Canada.name)


class Spain(Country):
    id = 9
    name = "Spain"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm

        class AirDefence:
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        F_A_18C = planes.F_A_18C
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_4E = planes.F_4E
        F_86F_Sabre = planes.F_86F_Sabre
        MQ_9_Reaper = planes.MQ_9_Reaper
        AV8BNA = planes.AV8BNA
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        I_16 = planes.I_16
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        KC135MPRS = planes.KC135MPRS
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.F_A_18C,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_4E,
        Plane.F_86F_Sabre,
        Plane.MQ_9_Reaper,
        Plane.AV8BNA,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.I_16,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.KC135MPRS,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Spain, self).__init__(Spain.id, Spain.name)


class TheNetherlands(Country):
    id = 10
    name = "The Netherlands"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo

        class Armor:
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH

        class Carriage:
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        F_16C_bl_50 = planes.F_16C_bl_50
        MQ_9_Reaper = planes.MQ_9_Reaper
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.F_16C_bl_50,
        Plane.MQ_9_Reaper,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(TheNetherlands, self).__init__(TheNetherlands.id, TheNetherlands.name)


class Belgium(Country):
    id = 11
    name = "Belgium"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Belgium, self).__init__(Belgium.id, Belgium.name)


class Norway(Country):
    id = 12
    name = "Norway"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC

        class AirDefence:
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        F_86F_Sabre = planes.F_86F_Sabre
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.F_86F_Sabre,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Norway, self).__init__(Norway.id, Norway.name)


class Denmark(Country):
    id = 13
    name = "Denmark"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC

        class AirDefence:
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        B_17G = planes.B_17G
        C_17A = planes.C_17A
        F_16A = planes.F_16A
        F_86F_Sabre = planes.F_86F_Sabre
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.B_17G,
        Plane.C_17A,
        Plane.F_16A,
        Plane.F_86F_Sabre,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Denmark, self).__init__(Denmark.id, Denmark.name)


class Israel(Country):
    id = 15
    name = "Israel"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC

        class AirDefence:
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_Merkava_IV = vehicles.Armor.MBT_Merkava_IV
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        F_16C_bl_52d = planes.F_16C_bl_52d
        C_130 = planes.C_130
        F_4E = planes.F_4E
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        B_17G = planes.B_17G
        E_2C = planes.E_2C
        F_16A = planes.F_16A
        F_16C_bl_50 = planes.F_16C_bl_50
        MiG_21Bis = planes.MiG_21Bis
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_15C,
        Plane.F_15E,
        Plane.F_16C_bl_52d,
        Plane.C_130,
        Plane.F_4E,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.B_17G,
        Plane.E_2C,
        Plane.F_16A,
        Plane.F_16C_bl_50,
        Plane.MiG_21Bis,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        UH_60A = helicopters.UH_60A
        AH_64D = helicopters.AH_64D
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.UH_60A,
        Helicopter.AH_64D,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Israel, self).__init__(Israel.id, Israel.name)


class Georgia(Country):
    id = 16
    name = "Georgia"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class Infantry:
            Infantry_M4_Georgia = vehicles.Infantry.Infantry_M4_Georgia
            Infantry_RPG = vehicles.Infantry.Infantry_RPG

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Su_25 = planes.Su_25
        An_26B = planes.An_26B
        Su_25T = planes.Su_25T
        L_39ZA = planes.L_39ZA
        Yak_40 = planes.Yak_40
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4
        TF_51D = planes.TF_51D

    planes = [
        Plane.A_10C,
        Plane.Su_25,
        Plane.An_26B,
        Plane.Su_25T,
        Plane.L_39ZA,
        Plane.Yak_40,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
        Plane.TF_51D,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        Mi_8MT = helicopters.Mi_8MT
        Mi_24V = helicopters.Mi_24V
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.Mi_8MT,
        Helicopter.Mi_24V,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Georgia, self).__init__(Georgia.id, Georgia.name)


class Insurgents(Country):
    id = 17
    name = "Insurgents"

    class Vehicle:

        class Artillery:
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm

        class Infantry:
            Infantry_AK_74 = vehicles.Infantry.Infantry_AK_74
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG

        class AirDefence:
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            AAA_ZU_23_Closed_Emplacement_Insurgent = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent
            SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375
            MANPADS_SA_18_Igla_Grouse_Ins = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_Ins
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        P_51D = planes.P_51D
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C = planes.A_10C
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.P_51D,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Insurgents, self).__init__(Insurgents.id, Insurgents.name)


class Abkhazia(Country):
    id = 18
    name = "Abkhazia"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class Infantry:
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_AK_74 = vehicles.Infantry.Infantry_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG

        class AirDefence:
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        Su_25 = planes.Su_25
        An_26B = planes.An_26B
        L_39ZA = planes.L_39ZA
        P_51D = planes.P_51D
        L_39C = planes.L_39C
        Yak_52 = planes.Yak_52
        TF_51D = planes.TF_51D
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C = planes.A_10C
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.Su_25,
        Plane.An_26B,
        Plane.L_39ZA,
        Plane.P_51D,
        Plane.L_39C,
        Plane.Yak_52,
        Plane.TF_51D,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Abkhazia, self).__init__(Abkhazia.id, Abkhazia.name)


class SouthOssetia(Country):
    id = 19
    name = "South Ossetia"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class Infantry:
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_AK_74 = vehicles.Infantry.Infantry_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG

        class AirDefence:
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C = planes.A_10C
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(SouthOssetia, self).__init__(SouthOssetia.id, SouthOssetia.name)


class Italy(Country):
    id = 20
    name = "Italy"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm

        class AirDefence:
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        Tornado_IDS = planes.Tornado_IDS
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        Yak_40 = planes.Yak_40
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.Tornado_IDS,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.Yak_40,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Italy, self).__init__(Italy.id, Italy.name)


class Australia(Country):
    id = 21
    name = "Australia"

    class Vehicle:

        class Artillery:
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            APC_M113 = vehicles.Armor.APC_M113
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Well_Car = vehicles.Carriage.Well_Car
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        F_A_18C = planes.F_A_18C
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_17A = planes.C_17A
        F_4E = planes.F_4E
        F_A_18A = planes.F_A_18A
        MQ_9_Reaper = planes.MQ_9_Reaper
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.F_A_18C,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_17A,
        Plane.F_4E,
        Plane.F_A_18A,
        Plane.MQ_9_Reaper,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Australia, self).__init__(Australia.id, Australia.name)


class Switzerland(Country):
    id = 22
    name = "Switzerland"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm

        class AirDefence:
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_M113 = vehicles.Armor.APC_M113

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        F_A_18C = planes.F_A_18C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        F_5E_3 = planes.F_5E_3
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_A_18C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.F_5E_3,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Switzerland, self).__init__(Switzerland.id, Switzerland.name)


class Austria(Country):
    id = 23
    name = "Austria"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH

        class Carriage:
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Austria, self).__init__(Austria.id, Austria.name)


class Belarus(Country):
    id = 24
    name = "Belarus"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm

        class Infantry:
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            APC_Tigr = vehicles.Unarmed.APC_Tigr

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_72B3 = vehicles.Armor.MBT_T_72B3

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Su_25 = planes.Su_25
        MiG_29S = planes.MiG_29S
        MiG_29A = planes.MiG_29A
        Su_27 = planes.Su_27
        Yak_40 = planes.Yak_40
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        IL_76MD = planes.IL_76MD
        L_39C = planes.L_39C
        MiG_25PD = planes.MiG_25PD
        Su_30 = planes.Su_30
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.Su_25,
        Plane.MiG_29S,
        Plane.MiG_29A,
        Plane.Su_27,
        Plane.Yak_40,
        Plane.An_26B,
        Plane.An_30M,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.IL_76MD,
        Plane.L_39C,
        Plane.MiG_25PD,
        Plane.Su_30,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Belarus, self).__init__(Belarus.id, Belarus.name)


class Bulgaria(Country):
    id = 25
    name = "Bulgaria"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_25RBT = planes.MiG_25RBT
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        Su_25 = planes.Su_25
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.C_17A,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_25RBT,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.Su_25,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Bulgaria, self).__init__(Bulgaria.id, Bulgaria.name)


class CzechRepublic(Country):
    id = 26
    name = "Czech Republic"

    class Vehicle:

        class Artillery:
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        C_17A = planes.C_17A
        L_39C = planes.L_39C
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        Su_25 = planes.Su_25
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.C_17A,
        Plane.L_39C,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.Su_25,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(CzechRepublic, self).__init__(CzechRepublic.id, CzechRepublic.name)


class China(Country):
    id = 27
    name = "China"

    class Vehicle:

        class Artillery:
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            PLZ_05 = vehicles.Artillery.PLZ_05

        class AirDefence:
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_Tigr = vehicles.Unarmed.APC_Tigr

        class Armor:
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B

        class MissilesSS:
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Well_Car = vehicles.Carriage.Well_Car
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Su_27 = planes.Su_27
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        MiG_15bis = planes.MiG_15bis
        Su_30 = planes.Su_30
        I_16 = planes.I_16
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        WingLoong_I = planes.WingLoong_I
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.Su_27,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.An_26B,
        Plane.An_30M,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.MiG_15bis,
        Plane.Su_30,
        Plane.I_16,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.WingLoong_I,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        Ka_27 = helicopters.Ka_27
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.Ka_27,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(China, self).__init__(China.id, China.name)


class Croatia(Country):
    id = 28
    name = "Croatia"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_17A = planes.C_17A
        MiG_21Bis = planes.MiG_21Bis
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_17A,
        Plane.MiG_21Bis,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        OH_58D = helicopters.OH_58D
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.OH_58D,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Croatia, self).__init__(Croatia.id, Croatia.name)


class Egypt(Country):
    id = 29
    name = "Egypt"

    class Vehicle:

        class Artillery:
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Well_Car = vehicles.Carriage.Well_Car
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        E_2C = planes.E_2C
        F_16A = planes.F_16A
        F_4E = planes.F_4E
        MiG_15bis = planes.MiG_15bis
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        M_2000C = planes.M_2000C
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.E_2C,
        Plane.F_16A,
        Plane.F_4E,
        Plane.MiG_15bis,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.M_2000C,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Egypt, self).__init__(Egypt.id, Egypt.name)


class Finland(Country):
    id = 30
    name = "Finland"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        F_A_18C = planes.F_A_18C
        MiG_21Bis = planes.MiG_21Bis
        Hawk = planes.Hawk
        I_16 = planes.I_16
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_A_18C,
        Plane.MiG_21Bis,
        Plane.Hawk,
        Plane.I_16,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Finland, self).__init__(Finland.id, Finland.name)


class Greece(Country):
    id = 31
    name = "Greece"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class Infantry:
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M249 = vehicles.Infantry.Infantry_M249

        class AirDefence:
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            APC_M113 = vehicles.Armor.APC_M113
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_4E = planes.F_4E
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        Mirage_2000_5 = planes.Mirage_2000_5
        Yak_40 = planes.Yak_40
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        M_2000C = planes.M_2000C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_4E,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.Mirage_2000_5,
        Plane.Yak_40,
        Plane.P_51D,
        Plane.C_17A,
        Plane.M_2000C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64A = helicopters.AH_64A
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        SH_60B = helicopters.SH_60B
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64A,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.SH_60B,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Greece, self).__init__(Greece.id, Greece.name)


class Hungary(Country):
    id = 32
    name = "Hungary"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_MTLB = vehicles.Armor.APC_MTLB
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.C_17A,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Hungary, self).__init__(Hungary.id, Hungary.name)


class India(Country):
    id = 33
    name = "India"

    class Vehicle:

        class Artillery:
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6

        class Armor:
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        A_50 = planes.A_50
        C_130 = planes.C_130
        C_17A = planes.C_17A
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Su_30 = planes.Su_30
        Tu_142 = planes.Tu_142
        MQ_9_Reaper = planes.MQ_9_Reaper
        M_2000C = planes.M_2000C
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.A_50,
        Plane.C_130,
        Plane.C_17A,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Su_30,
        Plane.Tu_142,
        Plane.MQ_9_Reaper,
        Plane.M_2000C,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(India, self).__init__(India.id, India.name)


class Iran(Country):
    id = 34
    name = "Iran"

    class Vehicle:

        class Artillery:
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class Infantry:
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG

        class AirDefence:
            AAA_ZU_23_Closed_Emplacement_Insurgent = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent
            SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            MANPADS_SA_18_Igla_Grouse_Ins = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_Ins
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_55 = vehicles.Armor.MBT_T_55
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        MiG_29A = planes.MiG_29A
        Su_25 = planes.Su_25
        Su_24M = planes.Su_24M
        IL_76MD = planes.IL_76MD
        MiG_21Bis = planes.MiG_21Bis
        A_50 = planes.A_50
        F_14A = planes.F_14A
        F_4E = planes.F_4E
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        Su_25T = planes.Su_25T
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.MiG_29A,
        Plane.Su_25,
        Plane.Su_24M,
        Plane.IL_76MD,
        Plane.MiG_21Bis,
        Plane.A_50,
        Plane.F_14A,
        Plane.F_4E,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.Su_25T,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_1W = helicopters.AH_1W
        OH_58D = helicopters.OH_58D
        Mi_8MT = helicopters.Mi_8MT
        CH_47D = helicopters.CH_47D
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_1W,
        Helicopter.OH_58D,
        Helicopter.Mi_8MT,
        Helicopter.CH_47D,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Iran, self).__init__(Iran.id, Iran.name)


class Iraq(Country):
    id = 35
    name = "Iraq"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement_Insurgent = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        MiG_25PD = planes.MiG_25PD
        MiG_29A = planes.MiG_29A
        Su_24M = planes.Su_24M
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.MiG_25PD,
        Plane.MiG_29A,
        Plane.Su_24M,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_28N = helicopters.Mi_28N
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_28N,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Iraq, self).__init__(Iraq.id, Iraq.name)


class Japan(Country):
    id = 36
    name = "Japan"

    class Vehicle:

        class Artillery:
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car

        class Armor:
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        E_2C = planes.E_2C
        F_15C = planes.F_15C
        F_86F_Sabre = planes.F_86F_Sabre
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.E_2C,
        Plane.F_15C,
        Plane.F_86F_Sabre,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D = helicopters.AH_64D
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Japan, self).__init__(Japan.id, Japan.name)


class Kazakhstan(Country):
    id = 37
    name = "Kazakhstan"

    class Vehicle:

        class Artillery:
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            APC_Tigr = vehicles.Unarmed.APC_Tigr

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_55 = vehicles.Armor.MBT_T_55
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            APC_BTR_82A = vehicles.Armor.APC_BTR_82A

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Well_Car = vehicles.Carriage.Well_Car
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Su_25 = planes.Su_25
        MiG_29S = planes.MiG_29S
        MiG_29A = planes.MiG_29A
        Su_27 = planes.Su_27
        MiG_31 = planes.MiG_31
        Su_30 = planes.Su_30
        Yak_40 = planes.Yak_40
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        IL_76MD = planes.IL_76MD
        L_39C = planes.L_39C
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.Su_25,
        Plane.MiG_29S,
        Plane.MiG_29A,
        Plane.Su_27,
        Plane.MiG_31,
        Plane.Su_30,
        Plane.Yak_40,
        Plane.An_26B,
        Plane.An_30M,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.IL_76MD,
        Plane.L_39C,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        Mi_8MT = helicopters.Mi_8MT
        Mi_26 = helicopters.Mi_26
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.Mi_8MT,
        Helicopter.Mi_26,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Kazakhstan, self).__init__(Kazakhstan.id, Kazakhstan.name)


class NorthKorea(Country):
    id = 38
    name = "North Korea"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        MiG_29S = planes.MiG_29S
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.MiG_29S,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(NorthKorea, self).__init__(NorthKorea.id, NorthKorea.name)


class Pakistan(Country):
    id = 39
    name = "Pakistan"

    class Vehicle:

        class Artillery:
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class MissilesSS:
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Well_Car = vehicles.Carriage.Well_Car
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        IL_78M = planes.IL_78M
        WingLoong_I = planes.WingLoong_I
        JF_17 = planes.JF_17
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.IL_78M,
        Plane.WingLoong_I,
        Plane.JF_17,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Pakistan, self).__init__(Pakistan.id, Pakistan.name)


class Poland(Country):
    id = 40
    name = "Poland"

    class Vehicle:

        class Artillery:
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH

        class Carriage:
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car

    class Plane:
        A_10C = planes.A_10C
        F_16C_bl_50 = planes.F_16C_bl_50
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        An_26B = planes.An_26B
        C_130 = planes.C_130
        C_17A = planes.C_17A
        F_16C_bl_52d = planes.F_16C_bl_52d
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29G = planes.MiG_29G
        Yak_40 = planes.Yak_40
        I_16 = planes.I_16
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_16C_bl_50,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.An_26B,
        Plane.C_130,
        Plane.C_17A,
        Plane.F_16C_bl_52d,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29G,
        Plane.Yak_40,
        Plane.I_16,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Poland, self).__init__(Poland.id, Poland.name)


class Romania(Country):
    id = 41
    name = "Romania"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        C_17A = planes.C_17A
        F_16A_MLU = planes.F_16A_MLU
        L_39ZA = planes.L_39ZA
        MiG_15bis = planes.MiG_15bis
        MiG_29A = planes.MiG_29A
        Yak_52 = planes.Yak_52
        I_16 = planes.I_16
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_21Bis = planes.MiG_21Bis
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.C_17A,
        Plane.F_16A_MLU,
        Plane.L_39ZA,
        Plane.MiG_15bis,
        Plane.MiG_29A,
        Plane.Yak_52,
        Plane.I_16,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_21Bis,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Romania, self).__init__(Romania.id, Romania.name)


class SaudiArabia(Country):
    id = 42
    name = "Saudi Arabia"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class AirDefence:
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        Tornado_IDS = planes.Tornado_IDS
        C_130 = planes.C_130
        E_3A = planes.E_3A
        KC_135 = planes.KC_135
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        KC130 = planes.KC130
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_15C,
        Plane.F_15E,
        Plane.Tornado_IDS,
        Plane.C_130,
        Plane.E_3A,
        Plane.KC_135,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.KC130,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        UH_1H = helicopters.UH_1H
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        CH_47D = helicopters.CH_47D
        AH_64A = helicopters.AH_64A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.UH_1H,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.CH_47D,
        Helicopter.AH_64A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(SaudiArabia, self).__init__(SaudiArabia.id, SaudiArabia.name)


class Serbia(Country):
    id = 43
    name = "Serbia"

    class Vehicle:

        class Artillery:
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_55 = vehicles.Armor.MBT_T_55
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        MiG_29A = planes.MiG_29A
        MiG_21Bis = planes.MiG_21Bis
        An_26B = planes.An_26B
        MiG_29S = planes.MiG_29S
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        WingLoong_I = planes.WingLoong_I
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.MiG_29A,
        Plane.MiG_21Bis,
        Plane.An_26B,
        Plane.MiG_29S,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.WingLoong_I,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Serbia, self).__init__(Serbia.id, Serbia.name)


class Slovakia(Country):
    id = 44
    name = "Slovakia"

    class Vehicle:

        class Artillery:
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class AirDefence:
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_Tigr = vehicles.Unarmed.APC_Tigr
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109

        class Armor:
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        L_39C = planes.L_39C
        MiG_29A = planes.MiG_29A
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.C_17A,
        Plane.L_39C,
        Plane.MiG_29A,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Slovakia, self).__init__(Slovakia.id, Slovakia.name)


class SouthKorea(Country):
    id = 45
    name = "South Korea"

    class Vehicle:

        class Artillery:
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_130 = planes.C_130
        F_15E = planes.F_15E
        F_4E = planes.F_4E
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_130,
        Plane.F_15E,
        Plane.F_4E,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(SouthKorea, self).__init__(SouthKorea.id, SouthKorea.name)


class Sweden(Country):
    id = 46
    name = "Sweden"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        B_17G = planes.B_17G
        C_130 = planes.C_130
        AJS37 = planes.AJS37
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.B_17G,
        Plane.C_130,
        Plane.AJS37,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Sweden, self).__init__(Sweden.id, Sweden.name)


class Syria(Country):
    id = 47
    name = "Syria"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_Tigr = vehicles.Unarmed.APC_Tigr
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            MBT_T_72B3 = vehicles.Armor.MBT_T_72B3
            APC_BTR_82A = vehicles.Armor.APC_BTR_82A

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_29A = planes.MiG_29A
        Su_24M = planes.Su_24M
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_29A,
        Plane.Su_24M,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Syria, self).__init__(Syria.id, Syria.name)


class Yemen(Country):
    id = 48
    name = "Yemen"

    class Vehicle:

        class Artillery:
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        L_39C = planes.L_39C
        MiG_29S = planes.MiG_29S
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.L_39C,
        Plane.MiG_29S,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Yemen, self).__init__(Yemen.id, Yemen.name)


class Vietnam(Country):
    id = 49
    name = "Vietnam"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        Su_17M4 = planes.Su_17M4
        Su_27 = planes.Su_27
        Su_30 = planes.Su_30
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.Su_17M4,
        Plane.Su_27,
        Plane.Su_30,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Vietnam, self).__init__(Vietnam.id, Vietnam.name)


class Venezuela(Country):
    id = 50
    name = "Venezuela"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm

        class AirDefence:
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_86F_Sabre = planes.F_86F_Sabre
        Su_30 = planes.Su_30
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_86F_Sabre,
        Plane.Su_30,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_26 = helicopters.Mi_26
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_26,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Venezuela, self).__init__(Venezuela.id, Venezuela.name)


class Tunisia(Country):
    id = 51
    name = "Tunisia"

    class Vehicle:

        class AirDefence:
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Tunisia, self).__init__(Tunisia.id, Tunisia.name)


class Thailand(Country):
    id = 52
    name = "Thailand"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        L_39ZA = planes.L_39ZA
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.L_39ZA,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Thailand, self).__init__(Thailand.id, Thailand.name)


class Sudan(Country):
    id = 53
    name = "Sudan"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        MiG_29S = planes.MiG_29S
        Su_24M = planes.Su_24M
        Su_25 = planes.Su_25
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.MiG_29S,
        Plane.Su_24M,
        Plane.Su_25,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Sudan, self).__init__(Sudan.id, Sudan.name)


class Philippines(Country):
    id = 54
    name = "Philippines"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Philippines, self).__init__(Philippines.id, Philippines.name)


class Morocco(Country):
    id = 55
    name = "Morocco"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class AirDefence:
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Morocco, self).__init__(Morocco.id, Morocco.name)


class Mexico(Country):
    id = 56
    name = "Mexico"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        E_2C = planes.E_2C
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.E_2C,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Mexico, self).__init__(Mexico.id, Mexico.name)


class Malaysia(Country):
    id = 57
    name = "Malaysia"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Su_30 = planes.Su_30
        Hawk = planes.Hawk
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Su_30,
        Plane.Hawk,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Malaysia, self).__init__(Malaysia.id, Malaysia.name)


class Libya(Country):
    id = 58
    name = "Libya"

    class Vehicle:

        class Artillery:
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        IL_78M = planes.IL_78M
        MiG_21Bis = planes.MiG_21Bis
        Su_24M = planes.Su_24M
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.IL_78M,
        Plane.MiG_21Bis,
        Plane.Su_24M,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Libya, self).__init__(Libya.id, Libya.name)


class Jordan(Country):
    id = 59
    name = "Jordan"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            IFV_Marder = vehicles.Armor.IFV_Marder
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Hawk = planes.Hawk
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Hawk,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_26 = helicopters.Mi_26
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_26,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Jordan, self).__init__(Jordan.id, Jordan.name)


class Indonesia(Country):
    id = 60
    name = "Indonesia"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6

        class Armor:
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_Marder = vehicles.Armor.IFV_Marder
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        C_130 = planes.C_130
        F_16A = planes.F_16A
        F_16A_MLU = planes.F_16A_MLU
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Su_27 = planes.Su_27
        Su_30 = planes.Su_30
        Hawk = planes.Hawk
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.C_130,
        Plane.F_16A,
        Plane.F_16A_MLU,
        Plane.F_16C_bl_52d,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Su_27,
        Plane.Su_30,
        Plane.Hawk,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Indonesia, self).__init__(Indonesia.id, Indonesia.name)


class Honduras(Country):
    id = 61
    name = "Honduras"

    class Vehicle:

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Honduras, self).__init__(Honduras.id, Honduras.name)


class Ethiopia(Country):
    id = 62
    name = "Ethiopia"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        L_39C = planes.L_39C
        MiG_21Bis = planes.MiG_21Bis
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.L_39C,
        Plane.MiG_21Bis,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_24V = helicopters.Mi_24V
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_24V,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Ethiopia, self).__init__(Ethiopia.id, Ethiopia.name)


class Chile(Country):
    id = 63
    name = "Chile"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm

        class AirDefence:
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            IFV_Marder = vehicles.Armor.IFV_Marder
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        P_51D = planes.P_51D
        KC_135 = planes.KC_135
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        KC135MPRS = planes.KC135MPRS
        C_130 = planes.C_130
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.P_51D,
        Plane.KC_135,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.KC135MPRS,
        Plane.C_130,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Chile, self).__init__(Chile.id, Chile.name)


class Brazil(Country):
    id = 64
    name = "Brazil"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm

        class Infantry:
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M249 = vehicles.Infantry.Infantry_M249

        class AirDefence:
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Well_Car = vehicles.Carriage.Well_Car
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        B_17G = planes.B_17G
        C_130 = planes.C_130
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        M_2000C = planes.M_2000C
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.B_17G,
        Plane.C_130,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.M_2000C,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Brazil, self).__init__(Brazil.id, Brazil.name)


class Bahrain(Country):
    id = 65
    name = "Bahrain"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC

        class Infantry:
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M249 = vehicles.Infantry.Infantry_M249

        class AirDefence:
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            APC_M113 = vehicles.Armor.APC_M113
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Bahrain, self).__init__(Bahrain.id, Bahrain.name)


class ThirdReich(Country):
    id = 66
    name = "Third Reich"

    class Vehicle:

        class Artillery:
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car

        class Armor:
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(ThirdReich, self).__init__(ThirdReich.id, ThirdReich.name)


class Yugoslavia(Country):
    id = 67
    name = "Yugoslavia"

    class Vehicle:

        class Artillery:
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class AirDefence:
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(Yugoslavia, self).__init__(Yugoslavia.id, Yugoslavia.name)


class USSR(Country):
    id = 68
    name = "USSR"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm

        class Infantry:
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH

        class Carriage:
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Freight_Van = vehicles.Carriage.Freight_Van
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car

    class Plane:
        A_10C = planes.A_10C
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        I_16 = planes.I_16
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        M_2000C = planes.M_2000C
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.I_16,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.M_2000C,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        SSK_636_Improved_Kilo = ships.SSK_636_Improved_Kilo
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Cruiser_1164_Moskva = ships.Cruiser_1164_Moskva
        Frigate_11540_Neustrashimy = ships.Frigate_11540_Neustrashimy
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins

    class CallsignHelipad:
        Otkrytka = "Otkrytka"
        Vetka = "Vetka"
        Yunga = "Yunga"
        Shpora = "Shpora"
        Kalitka = "Kalitka"
        Torba = "Torba"
        Kaemka = "Kaemka"
        Podkova = "Podkova"
        Skala = "Skala"
        Kapel = "Kapel"

    class CallsignGrassAirfield:
        A01 = "A01"
        B01 = "B01"

    callsign = {
        "Helipad": [
            CallsignHelipad.Otkrytka,
            CallsignHelipad.Vetka,
            CallsignHelipad.Yunga,
            CallsignHelipad.Shpora,
            CallsignHelipad.Kalitka,
            CallsignHelipad.Torba,
            CallsignHelipad.Kaemka,
            CallsignHelipad.Podkova,
            CallsignHelipad.Skala,
            CallsignHelipad.Kapel
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.A01,
            CallsignGrassAirfield.B01
        ],
    }

    def __init__(self):
        super(USSR, self).__init__(USSR.id, USSR.name)


class ItalianSocialRepublic(Country):
    id = 69
    name = "Italian Social Republic"

    class Vehicle:

        class Artillery:
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car

        class Armor:
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(ItalianSocialRepublic, self).__init__(ItalianSocialRepublic.id, ItalianSocialRepublic.name)


class Algeria(Country):
    id = 70
    name = "Algeria"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm

        class Infantry:
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            APC_Tigr = vehicles.Unarmed.APC_Tigr
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331

        class Armor:
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        MiG_21Bis = planes.MiG_21Bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_25RBT = planes.MiG_25RBT
        MiG_25PD = planes.MiG_25PD
        MiG_29S = planes.MiG_29S
        MiG_27K = planes.MiG_27K
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Su_30 = planes.Su_30
        L_39ZA = planes.L_39ZA
        IL_78M = planes.IL_78M
        IL_76MD = planes.IL_76MD
        C_130 = planes.C_130
        Yak_40 = planes.Yak_40
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        WingLoong_I = planes.WingLoong_I
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.MiG_21Bis,
        Plane.MiG_23MLD,
        Plane.MiG_25RBT,
        Plane.MiG_25PD,
        Plane.MiG_29S,
        Plane.MiG_27K,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Su_30,
        Plane.L_39ZA,
        Plane.IL_78M,
        Plane.IL_76MD,
        Plane.C_130,
        Plane.Yak_40,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.WingLoong_I,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_28N = helicopters.Mi_28N
        Ka_27 = helicopters.Ka_27
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_28N,
        Helicopter.Ka_27,
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Algeria, self).__init__(Algeria.id, Algeria.name)


class Kuwait(Country):
    id = 71
    name = "Kuwait"

    class Vehicle:

        class Artillery:
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm

        class AirDefence:
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_Warrior = vehicles.Armor.IFV_Warrior
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        C_17A = planes.C_17A
        F_A_18C = planes.F_A_18C
        Hawk = planes.Hawk
        KC130 = planes.KC130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.C_17A,
        Plane.F_A_18C,
        Plane.Hawk,
        Plane.KC130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        AH_64D = helicopters.AH_64D
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.AH_64D,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Kuwait, self).__init__(Kuwait.id, Kuwait.name)


class Qatar(Country):
    id = 72
    name = "Qatar"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep

        class Armor:
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_17A = planes.C_17A
        Mirage_2000_5 = planes.Mirage_2000_5
        M_2000C = planes.M_2000C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_17A,
        Plane.Mirage_2000_5,
        Plane.M_2000C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Qatar, self).__init__(Qatar.id, Qatar.name)


class Oman(Country):
    id = 73
    name = "Oman"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm

        class AirDefence:
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16C_bl_50 = planes.F_16C_bl_50
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16C_bl_52d,
        Plane.F_16C_bl_50,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Oman, self).__init__(Oman.id, Oman.name)


class UnitedArabEmirates(Country):
    id = 74
    name = "United Arab Emirates"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm

        class AirDefence:
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        F_16C_bl_52d = planes.F_16C_bl_52d
        C_130 = planes.C_130
        C_17A = planes.C_17A
        M_2000C = planes.M_2000C
        Hawk = planes.Hawk
        WingLoong_I = planes.WingLoong_I
        RQ_1A_Predator = planes.RQ_1A_Predator
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_16C_bl_52d,
        Plane.C_130,
        Plane.C_17A,
        Plane.M_2000C,
        Plane.Hawk,
        Plane.WingLoong_I,
        Plane.RQ_1A_Predator,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        AH_64D = helicopters.AH_64D
        UH_60A = helicopters.UH_60A
        CH_47D = helicopters.CH_47D
        AH_64A = helicopters.AH_64A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.AH_64D,
        Helicopter.UH_60A,
        Helicopter.CH_47D,
        Helicopter.AH_64A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(UnitedArabEmirates, self).__init__(UnitedArabEmirates.id, UnitedArabEmirates.name)


class SouthAfrica(Country):
    id = 75
    name = "South Africa"

    class Vehicle:

        class AirDefence:
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109

        class Armor:
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        C_130 = planes.C_130
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        F_86F_Sabre = planes.F_86F_Sabre
        Hawk = planes.Hawk
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.C_130,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.F_86F_Sabre,
        Plane.Hawk,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(SouthAfrica, self).__init__(SouthAfrica.id, SouthAfrica.name)


class Cuba(Country):
    id = 76
    name = "Cuba"

    class Vehicle:

        class Artillery:
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus

        class AirDefence:
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        MiG_23MLD = planes.MiG_23MLD
        MiG_29A = planes.MiG_29A
        MiG_21Bis = planes.MiG_21Bis
        An_26B = planes.An_26B
        Yak_40 = planes.Yak_40
        L_39ZA = planes.L_39ZA
        IL_76MD = planes.IL_76MD
        P_51D = planes.P_51D
        P_51D_30_NA = planes.P_51D_30_NA
        TF_51D = planes.TF_51D
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_23MLD = planes.MiG_23MLD
        MiG_23MLD = planes.MiG_23MLD
        MiG_23MLD = planes.MiG_23MLD
        MiG_19P = planes.MiG_19P
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.MiG_23MLD,
        Plane.MiG_29A,
        Plane.MiG_21Bis,
        Plane.An_26B,
        Plane.Yak_40,
        Plane.L_39ZA,
        Plane.IL_76MD,
        Plane.P_51D,
        Plane.P_51D_30_NA,
        Plane.TF_51D,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_23MLD,
        Plane.MiG_23MLD,
        Plane.MiG_23MLD,
        Plane.MiG_19P,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.M_2000C,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        Mi_24V = helicopters.Mi_24V
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.Mi_24V,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Cuba, self).__init__(Cuba.id, Cuba.name)


class Portugal(Country):
    id = 77
    name = "Portugal"

    class Vehicle:

        class Artillery:
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm

        class AirDefence:
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed

        class Armor:
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        F_16A_MLU = planes.F_16A_MLU
        F_16A = planes.F_16A
        F_16C_bl_50 = planes.F_16C_bl_50
        F_86F_Sabre = planes.F_86F_Sabre
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        B_17G = planes.B_17G
        C_17A = planes.C_17A
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.F_16A_MLU,
        Plane.F_16A,
        Plane.F_16C_bl_50,
        Plane.F_86F_Sabre,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.B_17G,
        Plane.C_17A,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Portugal, self).__init__(Portugal.id, Portugal.name)


class GDR(Country):
    id = 78
    name = "GDR"

    class Vehicle:

        class Artillery:
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm

        class Infantry:
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus

        class AirDefence:
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2

        class Armor:
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class MissilesSS:
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29A = planes.MiG_29A
        Su_17M4 = planes.Su_17M4
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29A,
        Plane.Su_17M4,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(GDR, self).__init__(GDR.id, GDR.name)


class Lebanon(Country):
    id = 79
    name = "Lebanon"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm

        class Infantry:
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_M249 = vehicles.Infantry.Infantry_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6

        class Armor:
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_M113 = vehicles.Armor.APC_M113
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        Mirage_2000_5 = planes.Mirage_2000_5
        M_2000C = planes.M_2000C
        RQ_1A_Predator = planes.RQ_1A_Predator
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.Mirage_2000_5,
        Plane.M_2000C,
        Plane.RQ_1A_Predator,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Lebanon, self).__init__(Lebanon.id, Lebanon.name)


class CombinedJointTaskForcesBlue(Country):
    id = 80
    name = "Combined Joint Task Forces Blue"

    class Vehicle:

        class Artillery:
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            PLZ_05 = vehicles.Artillery.PLZ_05

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_AK_74 = vehicles.Infantry.Infantry_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG
            Infantry_M249 = vehicles.Infantry.Infantry_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M4_Georgia = vehicles.Infantry.Infantry_M4_Georgia
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            AAA_ZU_23_Closed_Emplacement_Insurgent = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            MANPADS_SA_18_Igla_Grouse_Ins = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_Ins
            SAM_Linebacker___Bradley_M6 = vehicles.AirDefence.SAM_Linebacker___Bradley_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            APC_Tigr = vehicles.Unarmed.APC_Tigr

        class Armor:
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_T_72B3 = vehicles.Armor.MBT_T_72B3
            APC_BTR_82A = vehicles.Armor.APC_BTR_82A
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_IV = vehicles.Armor.MBT_Merkava_IV
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            IFV_M1126_Stryker_ICV = vehicles.Armor.IFV_M1126_Stryker_ICV
            SPG_Stryker_MGS = vehicles.Armor.SPG_Stryker_MGS
            ATGM_Stryker = vehicles.Armor.ATGM_Stryker
            IFV_Warrior = vehicles.Armor.IFV_Warrior

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        P_51D_30_NA = planes.P_51D_30_NA
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        Mirage_2000_5 = planes.Mirage_2000_5
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.P_51D_30_NA,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.Mirage_2000_5,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        SSK_636_Improved_Kilo = ships.SSK_636_Improved_Kilo
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Cruiser_1164_Moskva = ships.Cruiser_1164_Moskva
        Frigate_11540_Neustrashimy = ships.Frigate_11540_Neustrashimy
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Battlecruiser_1144_2_Pyotr_Velikiy = ships.Battlecruiser_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        CG_Ticonderoga = ships.CG_Ticonderoga
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        DDG_Arleigh_Burke_IIa = ships.DDG_Arleigh_Burke_IIa
        CVN_71_Theodore_Roosevelt = ships.CVN_71_Theodore_Roosevelt
        CVN_72_Abraham_Lincoln = ships.CVN_72_Abraham_Lincoln
        CVN_73_George_Washington = ships.CVN_73_George_Washington
        CVN_75_Harry_S__Truman = ships.CVN_75_Harry_S__Truman

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(CombinedJointTaskForcesBlue, self).__init__(CombinedJointTaskForcesBlue.id, CombinedJointTaskForcesBlue.name)


class CombinedJointTaskForcesRed(Country):
    id = 81
    name = "Combined Joint Task Forces Red"

    class Vehicle:

        class Artillery:
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            PLZ_05 = vehicles.Artillery.PLZ_05

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_AK_74 = vehicles.Infantry.Infantry_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG
            Infantry_M249 = vehicles.Infantry.Infantry_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M4_Georgia = vehicles.Infantry.Infantry_M4_Georgia
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            AAA_ZU_23_Closed_Emplacement_Insurgent = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            MANPADS_SA_18_Igla_Grouse_Ins = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_Ins
            SAM_Linebacker___Bradley_M6 = vehicles.AirDefence.SAM_Linebacker___Bradley_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            APC_Tigr = vehicles.Unarmed.APC_Tigr

        class Armor:
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_T_72B3 = vehicles.Armor.MBT_T_72B3
            APC_BTR_82A = vehicles.Armor.APC_BTR_82A
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_IV = vehicles.Armor.MBT_Merkava_IV
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            IFV_M1126_Stryker_ICV = vehicles.Armor.IFV_M1126_Stryker_ICV
            SPG_Stryker_MGS = vehicles.Armor.SPG_Stryker_MGS
            ATGM_Stryker = vehicles.Armor.ATGM_Stryker
            IFV_Warrior = vehicles.Armor.IFV_Warrior

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        P_51D_30_NA = planes.P_51D_30_NA
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        Mirage_2000_5 = planes.Mirage_2000_5
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.P_51D_30_NA,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.Mirage_2000_5,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        SSK_636_Improved_Kilo = ships.SSK_636_Improved_Kilo
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Cruiser_1164_Moskva = ships.Cruiser_1164_Moskva
        Frigate_11540_Neustrashimy = ships.Frigate_11540_Neustrashimy
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Battlecruiser_1144_2_Pyotr_Velikiy = ships.Battlecruiser_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        CG_Ticonderoga = ships.CG_Ticonderoga
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        DDG_Arleigh_Burke_IIa = ships.DDG_Arleigh_Burke_IIa
        CVN_71_Theodore_Roosevelt = ships.CVN_71_Theodore_Roosevelt
        CVN_72_Abraham_Lincoln = ships.CVN_72_Abraham_Lincoln
        CVN_73_George_Washington = ships.CVN_73_George_Washington
        CVN_75_Harry_S__Truman = ships.CVN_75_Harry_S__Truman

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(CombinedJointTaskForcesRed, self).__init__(CombinedJointTaskForcesRed.id, CombinedJointTaskForcesRed.name)


class UnitedNationsPeacekeepers(Country):
    id = 82
    name = "United Nations Peacekeepers"

    class Vehicle:

        class Artillery:
            SPG_Sturmpanzer_IV_Brummbar = vehicles.Artillery.SPG_Sturmpanzer_IV_Brummbar
            Mortar_2B11_120mm = vehicles.Artillery.Mortar_2B11_120mm
            Grad_MRL_FDDM__FC = vehicles.Artillery.Grad_MRL_FDDM__FC
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_2S9_Nona_120mm_M = vehicles.Artillery.SPH_2S9_Nona_120mm_M
            SPH_2S3_Akatsia_152mm = vehicles.Artillery.SPH_2S3_Akatsia_152mm
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm
            SPH_2S19_Msta_152mm = vehicles.Artillery.SPH_2S19_Msta_152mm
            MLRS_9A52_Smerch_CM_300mm = vehicles.Artillery.MLRS_9A52_Smerch_CM_300mm
            MLRS_9A52_Smerch_HE_300mm = vehicles.Artillery.MLRS_9A52_Smerch_HE_300mm
            MLRS_BM_27_Uragan_220mm = vehicles.Artillery.MLRS_BM_27_Uragan_220mm
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm
            SPG_M12_GMC_155mm = vehicles.Artillery.SPG_M12_GMC_155mm
            SPH_M109_Paladin_155mm = vehicles.Artillery.SPH_M109_Paladin_155mm
            MLRS_M270_227mm = vehicles.Artillery.MLRS_M270_227mm
            HUMVEE_JTAC = vehicles.Artillery.HUMVEE_JTAC
            PLZ_05 = vehicles.Artillery.PLZ_05

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_AK_74_Rus = vehicles.Infantry.Infantry_AK_74_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Insurgent_AK_74 = vehicles.Infantry.Insurgent_AK_74
            Infantry_AK_74 = vehicles.Infantry.Infantry_AK_74
            Infantry_RPG = vehicles.Infantry.Infantry_RPG
            Infantry_M249 = vehicles.Infantry.Infantry_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M4_Georgia = vehicles.Infantry.Infantry_M4_Georgia
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38_20mm = vehicles.AirDefence.AAA_Flak_38_20mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38_Quad_20mm = vehicles.AirDefence.AAA_Flak_Vierling_38_Quad_20mm
            AAA_SP_Kdo_G_40 = vehicles.AirDefence.AAA_SP_Kdo_G_40
            SL_Flakscheinwerfer_37 = vehicles.AirDefence.SL_Flakscheinwerfer_37
            PU_Maschinensatz_33 = vehicles.AirDefence.PU_Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_FuMG_401_Freya_LZ = vehicles.AirDefence.EWR_FuMG_401_Freya_LZ
            EWR_FuSe_65_Würzburg_Riese = vehicles.AirDefence.EWR_FuSe_65_Würzburg_Riese
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_Grison = vehicles.AirDefence.SAM_SA_19_Tunguska_Grison
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_Goa_LN = vehicles.AirDefence.SAM_SA_3_S_125_Goa_LN
            MCC_SR_Sborka_Dog_Ear_SR = vehicles.AirDefence.MCC_SR_Sborka_Dog_Ear_SR
            SAM_SA_6_Kub_Long_Track_STR = vehicles.AirDefence.SAM_SA_6_Kub_Long_Track_STR
            SAM_SA_6_Kub_Gainful_TEL = vehicles.AirDefence.SAM_SA_6_Kub_Gainful_TEL
            SAM_SA_8_Osa_Gecko_TEL = vehicles.AirDefence.SAM_SA_8_Osa_Gecko_TEL
            SAM_P19_Flat_Face_SR__SA_2_3 = vehicles.AirDefence.SAM_P19_Flat_Face_SR__SA_2_3
            SAM_SA_2_S_75_Guideline_LN = vehicles.AirDefence.SAM_SA_2_S_75_Guideline_LN
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            MANPADS_SA_18_Igla_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_C2
            MANPADS_SA_18_Igla_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse
            SAM_SA_3_S_125_Low_Blow_TR = vehicles.AirDefence.SAM_SA_3_S_125_Low_Blow_TR
            SAM_SA_2_S_75_Fan_Song_TR = vehicles.AirDefence.SAM_SA_2_S_75_Fan_Song_TR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            SAM_SA_13_Strela_10M3_Gopher_TEL = vehicles.AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            SPAAA_ZSU_23_4_Shilka_Gun_Dish = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            AAA_S_60_57mm = vehicles.AirDefence.AAA_S_60_57mm
            SPAAA_ZSU_57_2 = vehicles.AirDefence.SPAAA_ZSU_57_2
            AAA_QF_3_7 = vehicles.AirDefence.AAA_QF_3_7
            AAA_M45_Quadmount_HB_12_7mm = vehicles.AirDefence.AAA_M45_Quadmount_HB_12_7mm
            AAA_M1_37mm = vehicles.AirDefence.AAA_M1_37mm
            SPAAA_Vulcan_M163 = vehicles.AirDefence.SPAAA_Vulcan_M163
            SAM_Hawk_TR__AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR__AN_MPQ_46
            SAM_Hawk_SR__AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR__AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_Generator__PCP = vehicles.AirDefence.SAM_Hawk_Generator__PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse
            MANPADS_SA_18_Igla_S_Grouse_C2 = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2
            AAA_ZU_23_Closed_Emplacement_Insurgent = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375
            SAM_Avenger__Stinger = vehicles.AirDefence.SAM_Avenger__Stinger
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger
            MANPADS_Stinger_C2 = vehicles.AirDefence.MANPADS_Stinger_C2
            MANPADS_Stinger_C2_Desert = vehicles.AirDefence.MANPADS_Stinger_C2_Desert
            SAM_Rapier_LN = vehicles.AirDefence.SAM_Rapier_LN
            SAM_Rapier_Tracker = vehicles.AirDefence.SAM_Rapier_Tracker
            SAM_Rapier_Blindfire_TR = vehicles.AirDefence.SAM_Rapier_Blindfire_TR
            SAM_Patriot_CR__AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137
            SAM_Patriot_ECS = vehicles.AirDefence.SAM_Patriot_ECS
            SAM_Patriot_LN = vehicles.AirDefence.SAM_Patriot_LN
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_C2_ICC = vehicles.AirDefence.SAM_Patriot_C2_ICC
            SAM_Patriot_STR = vehicles.AirDefence.SAM_Patriot_STR
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            MANPADS_SA_18_Igla_Grouse_Ins = vehicles.AirDefence.MANPADS_SA_18_Igla_Grouse_Ins
            SAM_Linebacker___Bradley_M6 = vehicles.AirDefence.SAM_Linebacker___Bradley_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Gun_15cm_SK_C_28_Naval_in_Bunker = vehicles.Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker
            Bunker_with_Fire_Control_Center = vehicles.Fortification.Bunker_with_Fire_Control_Center

        class Unarmed:
            Truck_Opel_Blitz = vehicles.Unarmed.Truck_Opel_Blitz
            LUV_Kubelwagen_82 = vehicles.Unarmed.LUV_Kubelwagen_82
            LUV_Kettenrad = vehicles.Unarmed.LUV_Kettenrad
            Carrier_Sd_Kfz_7_Tractor = vehicles.Unarmed.Carrier_Sd_Kfz_7_Tractor
            LUV_Horch_901_Staff_Car = vehicles.Unarmed.LUV_Horch_901_Staff_Car
            Refueler_ATMZ_5 = vehicles.Unarmed.Refueler_ATMZ_5
            Refueler_ATZ_10 = vehicles.Unarmed.Refueler_ATZ_10
            Truck_GAZ_3307 = vehicles.Unarmed.Truck_GAZ_3307
            Truck_GAZ_66 = vehicles.Unarmed.Truck_GAZ_66
            Bus_IKARUS_280 = vehicles.Unarmed.Bus_IKARUS_280
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Bus_LAZ_695 = vehicles.Unarmed.Bus_LAZ_695
            Bus_LiAZ_677 = vehicles.Unarmed.Bus_LiAZ_677
            Truck_SKP_11_Mobile_ATC = vehicles.Unarmed.Truck_SKP_11_Mobile_ATC
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley
            LUV_UAZ_469_Jeep = vehicles.Unarmed.LUV_UAZ_469_Jeep
            Truck_Ural_ATsP_6_Firefighter = vehicles.Unarmed.Truck_Ural_ATsP_6_Firefighter
            Truck_Ural_375_Mobile_C2 = vehicles.Unarmed.Truck_Ural_375_Mobile_C2
            Truck_Ural_375 = vehicles.Unarmed.Truck_Ural_375
            GPU_APA_5D = vehicles.Unarmed.GPU_APA_5D
            Truck_Ural_4320_31_Arm_d = vehicles.Unarmed.Truck_Ural_4320_31_Arm_d
            Truck_Ural_4320T = vehicles.Unarmed.Truck_Ural_4320T
            Car_VAZ_2109 = vehicles.Unarmed.Car_VAZ_2109
            GPU_APA_80_on_ZIL_131 = vehicles.Unarmed.GPU_APA_80_on_ZIL_131
            Truck_ZIL_131__C2 = vehicles.Unarmed.Truck_ZIL_131__C2
            Truck_ZIL_4331 = vehicles.Unarmed.Truck_ZIL_4331
            Car_Willys_Jeep = vehicles.Unarmed.Car_Willys_Jeep
            Truck_Bedford = vehicles.Unarmed.Truck_Bedford
            Truck_GMC_Jimmy_6x6_Truck = vehicles.Unarmed.Truck_GMC_Jimmy_6x6_Truck
            Carrier_M30_Cargo = vehicles.Unarmed.Carrier_M30_Cargo
            Tractor_M4_Hi_Speed = vehicles.Unarmed.Tractor_M4_Hi_Speed
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_KrAZ_6322_6x6 = vehicles.Unarmed.Truck_KrAZ_6322_6x6
            Truck_GAZ_3308 = vehicles.Unarmed.Truck_GAZ_3308
            Truck_MAZ_6303 = vehicles.Unarmed.Truck_MAZ_6303
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_Land_Rover_101_FC = vehicles.Unarmed.Truck_Land_Rover_101_FC
            LUV_Land_Rover_109 = vehicles.Unarmed.LUV_Land_Rover_109
            MCC_Predator_UAV_CP__GCS = vehicles.Unarmed.MCC_Predator_UAV_CP__GCS
            MCC_COMM_Predator_UAV_CL = vehicles.Unarmed.MCC_COMM_Predator_UAV_CL
            APC_Tigr = vehicles.Unarmed.APC_Tigr

        class Armor:
            MT_PzIV_H = vehicles.Armor.MT_PzIV_H
            APC_Sd_Kfz_251_Halftrack = vehicles.Armor.APC_Sd_Kfz_251_Halftrack
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B_Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            SPG_Jagdpanther_G1 = vehicles.Armor.SPG_Jagdpanther_G1
            SPG_Jagdpanzer_IV = vehicles.Armor.SPG_Jagdpanzer_IV
            SPG_StuG_IV = vehicles.Armor.SPG_StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            SPG_StuG_III_Ausf__G = vehicles.Armor.SPG_StuG_III_Ausf__G
            SPG_Sd_Kfz_184_Elefant = vehicles.Armor.SPG_Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_BTR_RD = vehicles.Armor.APC_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            CT_Centaur_IV = vehicles.Armor.CT_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            SPG_M10_GMC = vehicles.Armor.SPG_M10_GMC
            LT_Mk_VII_Tetrarch = vehicles.Armor.LT_Mk_VII_Tetrarch
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            Car_Daimler_Armored = vehicles.Armor.Car_Daimler_Armored
            Car_M8_Greyhound_Armored = vehicles.Armor.Car_M8_Greyhound_Armored
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_T_72B3 = vehicles.Armor.MBT_T_72B3
            APC_BTR_82A = vehicles.Armor.APC_BTR_82A
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            APC_TPz_Fuchs = vehicles.Armor.APC_TPz_Fuchs
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_IV = vehicles.Armor.MBT_Merkava_IV
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            IFV_M1126_Stryker_ICV = vehicles.Armor.IFV_M1126_Stryker_ICV
            SPG_Stryker_MGS = vehicles.Armor.SPG_Stryker_MGS
            ATGM_Stryker = vehicles.Armor.ATGM_Stryker
            IFV_Warrior = vehicles.Armor.IFV_Warrior

        class MissilesSS:
            SSM_V_1_Launcher = vehicles.MissilesSS.SSM_V_1_Launcher
            SSM_SS_1C_Scud_B = vehicles.MissilesSS.SSM_SS_1C_Scud_B
            AShM_SS_N_2_Silkworm = vehicles.MissilesSS.AShM_SS_N_2_Silkworm
            AShM_Silkworm_SR = vehicles.MissilesSS.AShM_Silkworm_SR

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4
        A_50 = planes.A_50
        An_26B = planes.An_26B
        An_30M = planes.An_30M
        B_17G = planes.B_17G
        FW_190D9 = planes.FW_190D9
        IL_76MD = planes.IL_76MD
        IL_78M = planes.IL_78M
        MiG_23MLD = planes.MiG_23MLD
        MiG_25PD = planes.MiG_25PD
        MiG_25RBT = planes.MiG_25RBT
        MiG_27K = planes.MiG_27K
        MiG_29A = planes.MiG_29A
        MiG_31 = planes.MiG_31
        P_51D = planes.P_51D
        TF_51D = planes.TF_51D
        Su_17M4 = planes.Su_17M4
        Su_24M = planes.Su_24M
        Su_24MR = planes.Su_24MR
        Su_25 = planes.Su_25
        Su_25T = planes.Su_25T
        Su_27 = planes.Su_27
        Tu_142 = planes.Tu_142
        Tu_160 = planes.Tu_160
        Tu_22M3 = planes.Tu_22M3
        Tu_95MS = planes.Tu_95MS
        Yak_40 = planes.Yak_40
        C_130 = planes.C_130
        MiG_29S = planes.MiG_29S
        F_16C_bl_50 = planes.F_16C_bl_50
        F_16C_bl_52d = planes.F_16C_bl_52d
        F_16A_MLU = planes.F_16A_MLU
        Tornado_IDS = planes.Tornado_IDS
        P_51D_30_NA = planes.P_51D_30_NA
        C_17A = planes.C_17A
        E_3A = planes.E_3A
        F_16A = planes.F_16A
        MQ_9_Reaper = planes.MQ_9_Reaper
        RQ_1A_Predator = planes.RQ_1A_Predator
        F_A_18C = planes.F_A_18C
        F_4E = planes.F_4E
        WingLoong_I = planes.WingLoong_I
        Su_33 = planes.Su_33
        Su_25TM = planes.Su_25TM
        Su_30 = planes.Su_30
        Su_34 = planes.Su_34
        L_39ZA = planes.L_39ZA
        F_15C = planes.F_15C
        F_15E = planes.F_15E
        KC_135 = planes.KC_135
        Mirage_2000_5 = planes.Mirage_2000_5
        E_2C = planes.E_2C
        MiG_29G = planes.MiG_29G
        F_A_18A = planes.F_A_18A
        J_11A = planes.J_11A
        KJ_2000 = planes.KJ_2000
        B_1B = planes.B_1B
        B_52H = planes.B_52H
        F_117A = planes.F_117A
        F_14A = planes.F_14A
        S_3B_Tanker = planes.S_3B_Tanker
        S_3B = planes.S_3B
        F_14B = planes.F_14B
        F_14A_135_GR = planes.F_14A_135_GR
        Tornado_GR4 = planes.Tornado_GR4

    planes = [
        Plane.A_10C,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
        Plane.A_50,
        Plane.An_26B,
        Plane.An_30M,
        Plane.B_17G,
        Plane.FW_190D9,
        Plane.IL_76MD,
        Plane.IL_78M,
        Plane.MiG_23MLD,
        Plane.MiG_25PD,
        Plane.MiG_25RBT,
        Plane.MiG_27K,
        Plane.MiG_29A,
        Plane.MiG_31,
        Plane.P_51D,
        Plane.TF_51D,
        Plane.Su_17M4,
        Plane.Su_24M,
        Plane.Su_24MR,
        Plane.Su_25,
        Plane.Su_25T,
        Plane.Su_27,
        Plane.Tu_142,
        Plane.Tu_160,
        Plane.Tu_22M3,
        Plane.Tu_95MS,
        Plane.Yak_40,
        Plane.C_130,
        Plane.MiG_29S,
        Plane.F_16C_bl_50,
        Plane.F_16C_bl_52d,
        Plane.F_16A_MLU,
        Plane.Tornado_IDS,
        Plane.P_51D_30_NA,
        Plane.C_17A,
        Plane.E_3A,
        Plane.F_16A,
        Plane.MQ_9_Reaper,
        Plane.RQ_1A_Predator,
        Plane.F_A_18C,
        Plane.F_4E,
        Plane.WingLoong_I,
        Plane.Su_33,
        Plane.Su_25TM,
        Plane.Su_30,
        Plane.Su_34,
        Plane.L_39ZA,
        Plane.F_15C,
        Plane.F_15E,
        Plane.KC_135,
        Plane.Mirage_2000_5,
        Plane.E_2C,
        Plane.MiG_29G,
        Plane.F_A_18A,
        Plane.J_11A,
        Plane.KJ_2000,
        Plane.B_1B,
        Plane.B_52H,
        Plane.F_117A,
        Plane.F_14A,
        Plane.S_3B_Tanker,
        Plane.S_3B,
        Plane.F_14B,
        Plane.F_14A_135_GR,
        Plane.Tornado_GR4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Ka_27 = helicopters.Ka_27
        Mi_24V = helicopters.Mi_24V
        Mi_26 = helicopters.Mi_26
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        CH_47D = helicopters.CH_47D
        UH_60A = helicopters.UH_60A
        Mi_28N = helicopters.Mi_28N
        AH_64D = helicopters.AH_64D
        OH_58D = helicopters.OH_58D
        AH_64A = helicopters.AH_64A
        AH_1W = helicopters.AH_1W
        SH_60B = helicopters.SH_60B
        CH_53E = helicopters.CH_53E

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Ka_27,
        Helicopter.Mi_24V,
        Helicopter.Mi_26,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.CH_47D,
        Helicopter.UH_60A,
        Helicopter.Mi_28N,
        Helicopter.AH_64D,
        Helicopter.OH_58D,
        Helicopter.AH_64A,
        Helicopter.AH_1W,
        Helicopter.SH_60B,
        Helicopter.CH_53E,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        U_boat_VIIC_U_flak = ships.U_boat_VIIC_U_flak
        Boat_Schnellboot_type_S130 = ships.Boat_Schnellboot_type_S130
        Corvette_1124_4_Grisha = ships.Corvette_1124_4_Grisha
        SSK_877V_Kilo = ships.SSK_877V_Kilo
        SSK_636_Improved_Kilo = ships.SSK_636_Improved_Kilo
        Bulker_Yakushev = ships.Bulker_Yakushev
        Cargo_Ivanov = ships.Cargo_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya
        Cruiser_1164_Moskva = ships.Cruiser_1164_Moskva
        Frigate_11540_Neustrashimy = ships.Frigate_11540_Neustrashimy
        Frigate_1135M_Rezky = ships.Frigate_1135M_Rezky
        Boat_Zvezdny_type = ships.Boat_Zvezdny_type
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        Boat_LCVP_Higgins = ships.Boat_LCVP_Higgins
        Bulker_Handy_Wind = ships.Bulker_Handy_Wind
        FFG_Oliver_Hazzard_Perry = ships.FFG_Oliver_Hazzard_Perry
        Battlecruiser_1144_2_Pyotr_Velikiy = ships.Battlecruiser_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        CG_Ticonderoga = ships.CG_Ticonderoga
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        DDG_Arleigh_Burke_IIa = ships.DDG_Arleigh_Burke_IIa
        CVN_71_Theodore_Roosevelt = ships.CVN_71_Theodore_Roosevelt
        CVN_72_Abraham_Lincoln = ships.CVN_72_Abraham_Lincoln
        CVN_73_George_Washington = ships.CVN_73_George_Washington
        CVN_75_Harry_S__Truman = ships.CVN_75_Harry_S__Truman

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(UnitedNationsPeacekeepers, self).__init__(UnitedNationsPeacekeepers.id, UnitedNationsPeacekeepers.name)


class Argentina(Country):
    id = 83
    name = "Argentina"

    class Vehicle:

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Bus_ZIU_9_Trolley = vehicles.Unarmed.Bus_ZIU_9_Trolley

        class Armor:
            APC_AAV_7_Amphibious = vehicles.Armor.APC_AAV_7_Amphibious
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1_Halftrack = vehicles.Armor.APC_M2A1_Halftrack
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        KC130 = planes.KC130
        B_17G = planes.B_17G
        F_86F_Sabre = planes.F_86F_Sabre
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.KC130,
        Plane.B_17G,
        Plane.F_86F_Sabre,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        CH_47D = helicopters.CH_47D
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        UH_60A = helicopters.UH_60A
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.CH_47D,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.UH_60A,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Argentina, self).__init__(Argentina.id, Argentina.name)


class Cyprus(Country):
    id = 84
    name = "Cyprus"

    class Vehicle:

        class Artillery:
            MLRS_BM_21_Grad_122mm = vehicles.Artillery.MLRS_BM_21_Grad_122mm
            SPH_Dana_vz77_152mm = vehicles.Artillery.SPH_Dana_vz77_152mm

        class Infantry:
            Infantry_M4 = vehicles.Infantry.Infantry_M4

        class AirDefence:
            AAA_40mm_Bofors = vehicles.AirDefence.AAA_40mm_Bofors
            SAM_SA_10_S_300_Grumble_Flap_Lid_TR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR
            SAM_SA_10_S_300_Grumble_Clam_Shell_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR
            SAM_SA_10_S_300_Grumble_C2 = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_C2
            SAM_SA_10_S_300_Grumble_TEL_D = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_D
            SAM_SA_10_S_300_Grumble_TEL_C = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_TEL_C
            SAM_SA_10_S_300_Grumble_Big_Bird_SR = vehicles.AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR
            SAM_SA_11_Buk_Gadfly_C2 = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_C2
            SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL
            SAM_SA_11_Buk_Gadfly_Snow_Drift_SR = vehicles.AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR
            SAM_SA_15_Tor_Gauntlet = vehicles.AirDefence.SAM_SA_15_Tor_Gauntlet
            AAA_ZU_23_Closed_Emplacement = vehicles.AirDefence.AAA_ZU_23_Closed_Emplacement
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SPAAA_ZU_23_2_Mounted_Ural_375 = vehicles.AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375
            MANPADS_Stinger = vehicles.AirDefence.MANPADS_Stinger

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_KAMAZ_43101 = vehicles.Unarmed.Truck_KAMAZ_43101
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire

        class Armor:
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            MBT_T_80U = vehicles.Armor.MBT_T_80U

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        C_130 = planes.C_130
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.C_130,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun
        Mi_8MT = helicopters.Mi_8MT

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
        Helicopter.Mi_8MT,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Cyprus, self).__init__(Cyprus.id, Cyprus.name)


class Slovenia(Country):
    id = 85
    name = "Slovenia"

    class Vehicle:

        class Artillery:
            SPH_2S1_Gvozdika_122mm = vehicles.Artillery.SPH_2S1_Gvozdika_122mm

        class Infantry:
            Infantry_M249 = vehicles.Infantry.Infantry_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4

        class AirDefence:
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_SA_9_Strela_1_Gaskin_TEL = vehicles.AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL
            MANPADS_SA_18_Igla_S_Grouse = vehicles.AirDefence.MANPADS_SA_18_Igla_S_Grouse

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Building_armed = vehicles.Fortification.Building_armed
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030
            Beacon_TACAN_Portable_TTS_3030 = vehicles.Fortification.Beacon_TACAN_Portable_TTS_3030

        class Unarmed:
            Truck_M818_6x6 = vehicles.Unarmed.Truck_M818_6x6
            Truck_HEMMT_TFFT_Fire = vehicles.Unarmed.Truck_HEMMT_TFFT_Fire
            APC_HMMWV_Jeep = vehicles.Unarmed.APC_HMMWV_Jeep
            Refueler_M978_HEMTT = vehicles.Unarmed.Refueler_M978_HEMTT

        class Armor:
            IFV_BRDM_2 = vehicles.Armor.IFV_BRDM_2
            APC_Cobra__Scout = vehicles.Armor.APC_Cobra__Scout
            APC_HMMWV__Scout = vehicles.Armor.APC_HMMWV__Scout
            ATGM_HMMWV = vehicles.Armor.ATGM_HMMWV
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class Locomotive:
            Loco_VL80_Electric = vehicles.Locomotive.Loco_VL80_Electric
            Loco_CHME3T = vehicles.Locomotive.Loco_CHME3T
            Loco_ES44AH = vehicles.Locomotive.Loco_ES44AH
            Loco_DRG_Class_86 = vehicles.Locomotive.Loco_DRG_Class_86

        class Carriage:
            Freight_Van = vehicles.Carriage.Freight_Van
            Open_Wagon = vehicles.Carriage.Open_Wagon
            Tank_Car_blue = vehicles.Carriage.Tank_Car_blue
            Tank_Car_yellow = vehicles.Carriage.Tank_Car_yellow
            Passenger_Car = vehicles.Carriage.Passenger_Car
            Coach_Platform = vehicles.Carriage.Coach_Platform
            Flatcar = vehicles.Carriage.Flatcar
            Tank_Cartrinity = vehicles.Carriage.Tank_Cartrinity
            Well_Car = vehicles.Carriage.Well_Car
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            Wagon_G10__Germany = vehicles.Carriage.Wagon_G10__Germany
            Tank_Car__Germany = vehicles.Carriage.Tank_Car__Germany

    class Plane:
        A_10C = planes.A_10C
        P_51D = planes.P_51D
        C_17A = planes.C_17A
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_20G = planes.A_20G
        A_10A = planes.A_10A
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_5E = planes.F_5E
        F_5E_3 = planes.F_5E_3
        F_86F_Sabre = planes.F_86F_Sabre
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.P_51D,
        Plane.C_17A,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_20G,
        Plane.A_10A,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_5E,
        Plane.F_5E_3,
        Plane.F_86F_Sabre,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.Ju_88A4,
    ]

    class Helicopter:
        Ka_50 = helicopters.Ka_50
        Mi_8MT = helicopters.Mi_8MT
        UH_1H = helicopters.UH_1H
        SA342M = helicopters.SA342M
        SA342L = helicopters.SA342L
        SA342Mistral = helicopters.SA342Mistral
        SA342Minigun = helicopters.SA342Minigun

    helicopters = [
        Helicopter.Ka_50,
        Helicopter.Mi_8MT,
        Helicopter.UH_1H,
        Helicopter.SA342M,
        Helicopter.SA342L,
        Helicopter.SA342Mistral,
        Helicopter.SA342Minigun,
    ]

    class Ship:
        Boat_Armed_Hi_speed = ships.Boat_Armed_Hi_speed
        Corvette_1241_1_Molniya = ships.Corvette_1241_1_Molniya

    class CallsignAWACS:
        Overlord = "Overlord"
        Magic = "Magic"
        Wizard = "Wizard"
        Focus = "Focus"
        Darkstar = "Darkstar"

    class CallsignTankers:
        Texaco = "Texaco"
        Arco = "Arco"
        Shell = "Shell"

    class CallsignAir:
        Enfield = "Enfield"
        Springfield = "Springfield"
        Uzi = "Uzi"
        Colt = "Colt"
        Dodge = "Dodge"
        Ford = "Ford"
        Chevy = "Chevy"
        Pontiac = "Pontiac"

    class CallsignHelipad:
        London = "London"
        Dallas = "Dallas"
        Paris = "Paris"
        Moscow = "Moscow"
        Berlin = "Berlin"
        Rome = "Rome"
        Madrid = "Madrid"
        Warsaw = "Warsaw"
        Dublin = "Dublin"
        Perth = "Perth"

    class CallsignGroundUnits:
        Axeman = "Axeman"
        Darknight = "Darknight"
        Warrior = "Warrior"
        Pointer = "Pointer"
        Eyeball = "Eyeball"
        Moonbeam = "Moonbeam"
        Whiplash = "Whiplash"
        Finger = "Finger"
        Pinpoint = "Pinpoint"
        Ferret = "Ferret"
        Shaba = "Shaba"
        Playboy = "Playboy"
        Hammer = "Hammer"
        Jaguar = "Jaguar"
        Deathstar = "Deathstar"
        Anvil = "Anvil"
        Firefly = "Firefly"
        Mantis = "Mantis"
        Badger = "Badger"

    class CallsignGrassAirfield:
        New_York = "New York"

    callsign = {
        "AWACS": [
            CallsignAWACS.Overlord,
            CallsignAWACS.Magic,
            CallsignAWACS.Wizard,
            CallsignAWACS.Focus,
            CallsignAWACS.Darkstar
        ],
        "Tankers": [
            CallsignTankers.Texaco,
            CallsignTankers.Arco,
            CallsignTankers.Shell
        ],
        "Air": [
            CallsignAir.Enfield,
            CallsignAir.Springfield,
            CallsignAir.Uzi,
            CallsignAir.Colt,
            CallsignAir.Dodge,
            CallsignAir.Ford,
            CallsignAir.Chevy,
            CallsignAir.Pontiac
        ],
        "Helipad": [
            CallsignHelipad.London,
            CallsignHelipad.Dallas,
            CallsignHelipad.Paris,
            CallsignHelipad.Moscow,
            CallsignHelipad.Berlin,
            CallsignHelipad.Rome,
            CallsignHelipad.Madrid,
            CallsignHelipad.Warsaw,
            CallsignHelipad.Dublin,
            CallsignHelipad.Perth
        ],
        "GroundUnits": [
            CallsignGroundUnits.Axeman,
            CallsignGroundUnits.Darknight,
            CallsignGroundUnits.Warrior,
            CallsignGroundUnits.Pointer,
            CallsignGroundUnits.Eyeball,
            CallsignGroundUnits.Moonbeam,
            CallsignGroundUnits.Whiplash,
            CallsignGroundUnits.Finger,
            CallsignGroundUnits.Pinpoint,
            CallsignGroundUnits.Ferret,
            CallsignGroundUnits.Shaba,
            CallsignGroundUnits.Playboy,
            CallsignGroundUnits.Hammer,
            CallsignGroundUnits.Jaguar,
            CallsignGroundUnits.Deathstar,
            CallsignGroundUnits.Anvil,
            CallsignGroundUnits.Firefly,
            CallsignGroundUnits.Mantis,
            CallsignGroundUnits.Badger
        ],
        "GrassAirfield": [
            CallsignGrassAirfield.New_York
        ],
    }

    def __init__(self):
        super(Slovenia, self).__init__(Slovenia.id, Slovenia.name)


country_dict = {
    Russia.id: Russia,
    Ukraine.id: Ukraine,
    USA.id: USA,
    Turkey.id: Turkey,
    UK.id: UK,
    France.id: France,
    Germany.id: Germany,
    USAFAggressors.id: USAFAggressors,
    Canada.id: Canada,
    Spain.id: Spain,
    TheNetherlands.id: TheNetherlands,
    Belgium.id: Belgium,
    Norway.id: Norway,
    Denmark.id: Denmark,
    Israel.id: Israel,
    Georgia.id: Georgia,
    Insurgents.id: Insurgents,
    Abkhazia.id: Abkhazia,
    SouthOssetia.id: SouthOssetia,
    Italy.id: Italy,
    Australia.id: Australia,
    Switzerland.id: Switzerland,
    Austria.id: Austria,
    Belarus.id: Belarus,
    Bulgaria.id: Bulgaria,
    CzechRepublic.id: CzechRepublic,
    China.id: China,
    Croatia.id: Croatia,
    Egypt.id: Egypt,
    Finland.id: Finland,
    Greece.id: Greece,
    Hungary.id: Hungary,
    India.id: India,
    Iran.id: Iran,
    Iraq.id: Iraq,
    Japan.id: Japan,
    Kazakhstan.id: Kazakhstan,
    NorthKorea.id: NorthKorea,
    Pakistan.id: Pakistan,
    Poland.id: Poland,
    Romania.id: Romania,
    SaudiArabia.id: SaudiArabia,
    Serbia.id: Serbia,
    Slovakia.id: Slovakia,
    SouthKorea.id: SouthKorea,
    Sweden.id: Sweden,
    Syria.id: Syria,
    Yemen.id: Yemen,
    Vietnam.id: Vietnam,
    Venezuela.id: Venezuela,
    Tunisia.id: Tunisia,
    Thailand.id: Thailand,
    Sudan.id: Sudan,
    Philippines.id: Philippines,
    Morocco.id: Morocco,
    Mexico.id: Mexico,
    Malaysia.id: Malaysia,
    Libya.id: Libya,
    Jordan.id: Jordan,
    Indonesia.id: Indonesia,
    Honduras.id: Honduras,
    Ethiopia.id: Ethiopia,
    Chile.id: Chile,
    Brazil.id: Brazil,
    Bahrain.id: Bahrain,
    ThirdReich.id: ThirdReich,
    Yugoslavia.id: Yugoslavia,
    USSR.id: USSR,
    ItalianSocialRepublic.id: ItalianSocialRepublic,
    Algeria.id: Algeria,
    Kuwait.id: Kuwait,
    Qatar.id: Qatar,
    Oman.id: Oman,
    UnitedArabEmirates.id: UnitedArabEmirates,
    SouthAfrica.id: SouthAfrica,
    Cuba.id: Cuba,
    Portugal.id: Portugal,
    GDR.id: GDR,
    Lebanon.id: Lebanon,
    CombinedJointTaskForcesBlue.id: CombinedJointTaskForcesBlue,
    CombinedJointTaskForcesRed.id: CombinedJointTaskForcesRed,
    UnitedNationsPeacekeepers.id: UnitedNationsPeacekeepers,
    Argentina.id: Argentina,
    Cyprus.id: Cyprus,
    Slovenia.id: Slovenia,
}


def get_by_id(_id: int):
    """Returns a new country object for the given country id

    Args:
        _id: id for the country

    Returns:
        Country: a new country object
    """
    return country_dict[_id]()
