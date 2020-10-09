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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE

        class Infantry:
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            MBT_T_90 = vehicles.Armor.MBT_T_90

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        CG_1164_Moskva = ships.CG_1164_Moskva
        CGN_1144_2_Pyotr_Velikiy = ships.CGN_1144_2_Pyotr_Velikiy
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        FF_1135M_Rezky = ships.FF_1135M_Rezky
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        SSK_877 = ships.SSK_877
        SSK_641B = ships.SSK_641B
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        FFG_11540_Neustrashimy = ships.FFG_11540_Neustrashimy
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27

        class Infantry:
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        SSK_877 = ships.SSK_877
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        FF_1135M_Rezky = ships.FF_1135M_Rezky

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            M12_GMC = vehicles.Artillery.M12_GMC

        class Infantry:
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand

        class AirDefence:
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_Linebacker_M6 = vehicles.AirDefence.SAM_Linebacker_M6
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD

        class Armor:
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            APC_M113 = vehicles.Armor.APC_M113
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M1126_Stryker_ICV = vehicles.Armor.APC_M1126_Stryker_ICV
            SPG_M1128_Stryker_MGS = vehicles.Armor.SPG_M1128_Stryker_MGS
            ATGM_M1134_Stryker = vehicles.Armor.ATGM_M1134_Stryker
            APC_M2A1 = vehicles.Armor.APC_M2A1
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10C_2 = planes.A_10C_2
        AJS37 = planes.AJS37
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        F_14B = planes.F_14B
        I_16 = planes.I_16
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
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
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10C_2,
        Plane.AJS37,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.F_14B,
        Plane.I_16,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        Ticonderoga_class = ships.Ticonderoga_class
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat
        LST_Mk_II = ships.LST_Mk_II
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
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
        super(USA, self).__init__(USA.id, USA.name)


class Turkey(Country):
    id = 3
    name = "Turkey"

    class Vehicle:

        class Artillery:
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin

        class AirDefence:
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_Cobra = vehicles.Armor.APC_Cobra
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class

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
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            M12_GMC = vehicles.Artillery.M12_GMC

        class Infantry:
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            Willys_MB = vehicles.Unarmed.Willys_MB
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            CCKW_353 = vehicles.Unarmed.CCKW_353

        class Armor:
            IFV_MCV_80 = vehicles.Armor.IFV_MCV_80
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            APC_M2A1 = vehicles.Armor.APC_M2A1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            IFV_Marder = vehicles.Armor.IFV_Marder
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_MTLB = vehicles.Armor.APC_MTLB
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

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
        FW_190D9 = planes.FW_190D9
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_51D_30_NA = planes.P_51D_30_NA
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.FW_190D9,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_51D_30_NA,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Georgian_soldier_with_M4 = vehicles.Infantry.Georgian_soldier_with_M4
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            AAA_ZU_23_Insurgent_Closed = vehicles.AirDefence.AAA_ZU_23_Insurgent_Closed
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            AAA_ZU_23_Insurgent_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_Insurgent_on_Ural_375
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_Linebacker_M6 = vehicles.AirDefence.SAM_Linebacker_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036

        class Armor:
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_Cobra = vehicles.Armor.APC_Cobra
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_Mk__4 = vehicles.Armor.MBT_Merkava_Mk__4
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            APC_M1126_Stryker_ICV = vehicles.Armor.APC_M1126_Stryker_ICV
            SPG_M1128_Stryker_MGS = vehicles.Armor.SPG_M1128_Stryker_MGS
            ATGM_M1134_Stryker = vehicles.Armor.ATGM_M1134_Stryker
            IFV_MCV_80 = vehicles.Armor.IFV_MCV_80

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        A_10C_2 = planes.A_10C_2
        F_14B = planes.F_14B
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Plane.A_10C_2,
        Plane.F_14B,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        SSK_877 = ships.SSK_877
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        CG_1164_Moskva = ships.CG_1164_Moskva
        FFG_11540_Neustrashimy = ships.FFG_11540_Neustrashimy
        FF_1135M_Rezky = ships.FF_1135M_Rezky
        SSK_641B = ships.SSK_641B
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        CGN_1144_2_Pyotr_Velikiy = ships.CGN_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        Ticonderoga_class = ships.Ticonderoga_class
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            APC_M2A1 = vehicles.Armor.APC_M2A1
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class AirDefence:
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1 = vehicles.Armor.APC_M2A1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            APC_M2A1 = vehicles.Armor.APC_M2A1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_Merkava_Mk__4 = vehicles.Armor.MBT_Merkava_Mk__4
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M2A1 = vehicles.Armor.APC_M2A1
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika

        class Infantry:
            Georgian_soldier_with_M4 = vehicles.Infantry.Georgian_soldier_with_M4
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_Cobra = vehicles.Armor.APC_Cobra
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny

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
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class Infantry:
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            AAA_ZU_23_Insurgent_Closed = vehicles.AirDefence.AAA_ZU_23_Insurgent_Closed
            AAA_ZU_23_Insurgent_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_Insurgent_on_Ural_375
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        P_51D = planes.P_51D
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
        A_10C = planes.A_10C
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
        Plane.A_10C,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika

        class Infantry:
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
        A_10C = planes.A_10C
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
        Plane.A_10C,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika

        class Infantry:
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
        A_10C = planes.A_10C
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
        A_20G = planes.A_20G
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
        Plane.A_10C,
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
        Plane.A_20G,
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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class AirDefence:
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            APC_M113 = vehicles.Armor.APC_M113
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            APC_M2A1 = vehicles.Armor.APC_M2A1
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin

        class AirDefence:
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_M113 = vehicles.Armor.APC_M113

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818

        class Armor:
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE

        class Infantry:
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M113 = vehicles.Armor.APC_M113
            APC_MTLB = vehicles.Armor.APC_MTLB
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            APC_M2A1 = vehicles.Armor.APC_M2A1
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona

        class AirDefence:
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036

        class Armor:
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B

        class MissilesSS:
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        SSK_877 = ships.SSK_877
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375

        class Armor:
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            MLRS_M270 = vehicles.Artillery.MLRS_M270

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M113 = vehicles.Armor.APC_M113
            APC_MTLB = vehicles.Armor.APC_MTLB
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
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
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_M2A1 = vehicles.Armor.APC_M2A1
            APC_MTLB = vehicles.Armor.APC_MTLB
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class Infantry:
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249

        class AirDefence:
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9

        class Armor:
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            APC_M113 = vehicles.Armor.APC_M113
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_MTLB = vehicles.Armor.APC_MTLB
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        L_39ZA = planes.L_39ZA
        An_26B = planes.An_26B
        C_17A = planes.C_17A
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29S = planes.MiG_29S
        Yak_40 = planes.Yak_40
        Yak_52 = planes.Yak_52
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.L_39ZA,
        Plane.An_26B,
        Plane.C_17A,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29S,
        Plane.Yak_40,
        Plane.Yak_52,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322

        class Armor:
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        SSK_877 = ships.SSK_877
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya

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
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class Infantry:
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_RPG = vehicles.Infantry.Soldier_RPG

        class AirDefence:
            AAA_ZU_23_Insurgent_Closed = vehicles.AirDefence.AAA_ZU_23_Insurgent_Closed
            AAA_ZU_23_Insurgent_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_Insurgent_on_Ural_375
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

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
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC130 = planes.KC130
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        Christen_Eagle_II = planes.Christen_Eagle_II
        F_14B = planes.F_14B
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
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
        Plane.A_10A,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC130,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.Christen_Eagle_II,
        Plane.F_14B,
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        SSK_877 = ships.SSK_877
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Insurgent_Closed = vehicles.AirDefence.AAA_ZU_23_Insurgent_Closed
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            AAA_ZU_23_Insurgent_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_Insurgent_on_Ural_375
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M113 = vehicles.Armor.APC_M113
            APC_MTLB = vehicles.Armor.APC_MTLB
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40

        class Armor:
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_55 = vehicles.Armor.MBT_T_55
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_Cobra = vehicles.Armor.APC_Cobra

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
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
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class MissilesSS:
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        FA_18C_hornet = planes.FA_18C_hornet
        Hawk = planes.Hawk
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
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
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.FA_18C_hornet,
        Plane.Hawk,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class

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
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1 = vehicles.Armor.APC_M2A1
            APC_MTLB = vehicles.Armor.APC_MTLB
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        SSK_877 = ships.SSK_877
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        SSK_877 = ships.SSK_877
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class AirDefence:
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_Cobra = vehicles.Armor.APC_Cobra
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
        AJS37 = planes.AJS37
        AV8BNA = planes.AV8BNA
        KC135MPRS = planes.KC135MPRS
        C_101EB = planes.C_101EB
        C_101CC = planes.C_101CC
        JF_17 = planes.JF_17
        WingLoong_I = planes.WingLoong_I
        Christen_Eagle_II = planes.Christen_Eagle_II
        FA_18C_hornet = planes.FA_18C_hornet
        I_16 = planes.I_16
        L_39C = planes.L_39C
        M_2000C = planes.M_2000C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
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
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
        Plane.AJS37,
        Plane.AV8BNA,
        Plane.KC135MPRS,
        Plane.C_101EB,
        Plane.C_101CC,
        Plane.JF_17,
        Plane.WingLoong_I,
        Plane.Christen_Eagle_II,
        Plane.FA_18C_hornet,
        Plane.I_16,
        Plane.L_39C,
        Plane.M_2000C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_55 = vehicles.Armor.MBT_T_55
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class AirDefence:
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109

        class Armor:
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT

        class Armor:
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_M113 = vehicles.Armor.APC_M113
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1 = vehicles.Armor.APC_M2A1
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_90 = vehicles.Armor.MBT_T_90

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            _2B11_mortar = vehicles.Artillery._2B11_mortar

        class AirDefence:
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_AAV_7 = vehicles.Armor.APC_AAV_7

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M113 = vehicles.Armor.APC_M113
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1 = vehicles.Armor.APC_M2A1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class AirDefence:
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M2A1 = vehicles.Armor.APC_M2A1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            IFV_Marder = vehicles.Armor.IFV_Marder
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322

        class Armor:
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_M113 = vehicles.Armor.APC_M113
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_Marder = vehicles.Armor.IFV_Marder
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_M113 = vehicles.Armor.APC_M113
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin

        class AirDefence:
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            IFV_Marder = vehicles.Armor.IFV_Marder
            APC_M2A1 = vehicles.Armor.APC_M2A1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin

        class Infantry:
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249

        class AirDefence:
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT

        class Armor:
            APC_M113 = vehicles.Armor.APC_M113
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            APC_M2A1 = vehicles.Armor.APC_M2A1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class Locomotive:
            ES44AH = vehicles.Locomotive.ES44AH
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class Infantry:
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Soldier_M249 = vehicles.Infantry.Soldier_M249

        class AirDefence:
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_Cobra = vehicles.Armor.APC_Cobra
            APC_M113 = vehicles.Armor.APC_M113
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class

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
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40

        class Armor:
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            M12_GMC = vehicles.Artillery.M12_GMC

        class AirDefence:
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            Willys_MB = vehicles.Unarmed.Willys_MB

        class Armor:
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            APC_M2A1 = vehicles.Armor.APC_M2A1
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC

        class Infantry:
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353

        class Armor:
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86
            ES44AH = vehicles.Locomotive.ES44AH

        class Carriage:
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        SSK_877 = ships.SSK_877
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        CG_1164_Moskva = ships.CG_1164_Moskva
        FFG_11540_Neustrashimy = ships.FFG_11540_Neustrashimy
        FF_1135M_Rezky = ships.FF_1135M_Rezky
        SSK_641B = ships.SSK_641B
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat

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
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40

        class Armor:
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE

        class Infantry:
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16

        class AirDefence:
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331

        class Armor:
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_90 = vehicles.Armor.MBT_T_90
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        M_2000C = planes.M_2000C
        MiG_19P = planes.MiG_19P
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
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
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.M_2000C,
        Plane.MiG_19P,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        SSK_877 = ships.SSK_877
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        FF_1135M_Rezky = ships.FF_1135M_Rezky

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
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE

        class AirDefence:
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M113 = vehicles.Armor.APC_M113
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            IFV_MCV_80 = vehicles.Armor.IFV_MCV_80
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class AirDefence:
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad

        class AirDefence:
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE

        class AirDefence:
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            APC_Cobra = vehicles.Armor.APC_Cobra

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        F_16C_bl_52d = planes.F_16C_bl_52d
        C_130 = planes.C_130
        C_17A = planes.C_17A
        M_2000C = planes.M_2000C
        Hawk = planes.Hawk
        RQ_1A_Predator = planes.RQ_1A_Predator
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        I_16 = planes.I_16
        L_39C = planes.L_39C
        MiG_15bis = planes.MiG_15bis
        MiG_19P = planes.MiG_19P
        MiG_21Bis = planes.MiG_21Bis
        Yak_52 = planes.Yak_52
        A_20G = planes.A_20G
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.F_16C_bl_52d,
        Plane.C_130,
        Plane.C_17A,
        Plane.M_2000C,
        Plane.Hawk,
        Plane.RQ_1A_Predator,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.I_16,
        Plane.L_39C,
        Plane.MiG_15bis,
        Plane.MiG_19P,
        Plane.MiG_21Bis,
        Plane.Yak_52,
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3

        class Armor:
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class Infantry:
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus

        class AirDefence:
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320

        class Armor:
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov

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
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin

        class AirDefence:
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Transport_M818 = vehicles.Unarmed.Transport_M818

        class Armor:
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_M113 = vehicles.Armor.APC_M113
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia

        class Infantry:
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus

        class AirDefence:
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG

        class Armor:
            APC_MTLB = vehicles.Armor.APC_MTLB
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B

        class MissilesSS:
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        An_26B = planes.An_26B
        MiG_15bis = planes.MiG_15bis
        MiG_21Bis = planes.MiG_21Bis
        MiG_29G = planes.MiG_29G
        Su_17M4 = planes.Su_17M4
        Yak_40 = planes.Yak_40
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
        Ju_88A4 = planes.Ju_88A4

    planes = [
        Plane.A_10C,
        Plane.An_26B,
        Plane.MiG_15bis,
        Plane.MiG_21Bis,
        Plane.MiG_29G,
        Plane.Su_17M4,
        Plane.Yak_40,
        Plane.FW_190A8,
        Plane.Bf_109K_4,
        Plane.SpitfireLFMkIX,
        Plane.SpitfireLFMkIXCW,
        Plane.P_47D_30,
        Plane.P_47D_30bl1,
        Plane.P_47D_40,
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin

        class Infantry:
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4

        class AirDefence:
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030

        class Unarmed:
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            Transport_M818 = vehicles.Unarmed.Transport_M818
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV

        class Armor:
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            APC_M113 = vehicles.Armor.APC_M113
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

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
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Armed_speedboat = ships.Armed_speedboat

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
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Georgian_soldier_with_M4 = vehicles.Infantry.Georgian_soldier_with_M4
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            AAA_ZU_23_Insurgent_Closed = vehicles.AirDefence.AAA_ZU_23_Insurgent_Closed
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            AAA_ZU_23_Insurgent_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_Insurgent_on_Ural_375
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_Linebacker_M6 = vehicles.AirDefence.SAM_Linebacker_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036

        class Armor:
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_Cobra = vehicles.Armor.APC_Cobra
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_Mk__4 = vehicles.Armor.MBT_Merkava_Mk__4
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            APC_M1126_Stryker_ICV = vehicles.Armor.APC_M1126_Stryker_ICV
            SPG_M1128_Stryker_MGS = vehicles.Armor.SPG_M1128_Stryker_MGS
            ATGM_M1134_Stryker = vehicles.Armor.ATGM_M1134_Stryker
            IFV_MCV_80 = vehicles.Armor.IFV_MCV_80

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        A_10C_2 = planes.A_10C_2
        F_14B = planes.F_14B
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Plane.A_10C_2,
        Plane.F_14B,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        SSK_877 = ships.SSK_877
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        CG_1164_Moskva = ships.CG_1164_Moskva
        FFG_11540_Neustrashimy = ships.FFG_11540_Neustrashimy
        FF_1135M_Rezky = ships.FF_1135M_Rezky
        SSK_641B = ships.SSK_641B
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        CGN_1144_2_Pyotr_Velikiy = ships.CGN_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        Ticonderoga_class = ships.Ticonderoga_class
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
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
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Georgian_soldier_with_M4 = vehicles.Infantry.Georgian_soldier_with_M4
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            AAA_ZU_23_Insurgent_Closed = vehicles.AirDefence.AAA_ZU_23_Insurgent_Closed
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            AAA_ZU_23_Insurgent_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_Insurgent_on_Ural_375
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_Linebacker_M6 = vehicles.AirDefence.SAM_Linebacker_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036

        class Armor:
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_Cobra = vehicles.Armor.APC_Cobra
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_Mk__4 = vehicles.Armor.MBT_Merkava_Mk__4
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            APC_M1126_Stryker_ICV = vehicles.Armor.APC_M1126_Stryker_ICV
            SPG_M1128_Stryker_MGS = vehicles.Armor.SPG_M1128_Stryker_MGS
            ATGM_M1134_Stryker = vehicles.Armor.ATGM_M1134_Stryker
            IFV_MCV_80 = vehicles.Armor.IFV_MCV_80

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        A_10C_2 = planes.A_10C_2
        F_14B = planes.F_14B
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Plane.A_10C_2,
        Plane.F_14B,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        SSK_877 = ships.SSK_877
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        CG_1164_Moskva = ships.CG_1164_Moskva
        FFG_11540_Neustrashimy = ships.FFG_11540_Neustrashimy
        FF_1135M_Rezky = ships.FF_1135M_Rezky
        SSK_641B = ships.SSK_641B
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        CGN_1144_2_Pyotr_Velikiy = ships.CGN_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        Ticonderoga_class = ships.Ticonderoga_class
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
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
            Sturmpanzer_IV_Brummbär = vehicles.Artillery.Sturmpanzer_IV_Brummbär
            _2B11_mortar = vehicles.Artillery._2B11_mortar
            MLRS_BM_21_Grad = vehicles.Artillery.MLRS_BM_21_Grad
            SPH_2S9_Nona = vehicles.Artillery.SPH_2S9_Nona
            SPH_2S3_Akatsia = vehicles.Artillery.SPH_2S3_Akatsia
            SPH_2S1_Gvozdika = vehicles.Artillery.SPH_2S1_Gvozdika
            SPH_2S19_Msta = vehicles.Artillery.SPH_2S19_Msta
            MLRS_9A52_Smerch = vehicles.Artillery.MLRS_9A52_Smerch
            MLRS_9A52_Smerch_HE = vehicles.Artillery.MLRS_9A52_Smerch_HE
            MLRS_9K57_Uragan_BM_27 = vehicles.Artillery.MLRS_9K57_Uragan_BM_27
            SpGH_Dana = vehicles.Artillery.SpGH_Dana
            M12_GMC = vehicles.Artillery.M12_GMC
            SPH_M109_Paladin = vehicles.Artillery.SPH_M109_Paladin
            MLRS_M270 = vehicles.Artillery.MLRS_M270
            MLRS_FDDM = vehicles.Artillery.MLRS_FDDM

        class Infantry:
            Infantry_Mauser_98 = vehicles.Infantry.Infantry_Mauser_98
            Infantry_Soldier_Rus = vehicles.Infantry.Infantry_Soldier_Rus
            Paratrooper_AKS = vehicles.Infantry.Paratrooper_AKS
            Paratrooper_RPG_16 = vehicles.Infantry.Paratrooper_RPG_16
            Infantry_Soldier_Insurgents = vehicles.Infantry.Infantry_Soldier_Insurgents
            Soldier_AK = vehicles.Infantry.Soldier_AK
            Soldier_RPG = vehicles.Infantry.Soldier_RPG
            Soldier_M249 = vehicles.Infantry.Soldier_M249
            Infantry_M4 = vehicles.Infantry.Infantry_M4
            Georgian_soldier_with_M4 = vehicles.Infantry.Georgian_soldier_with_M4
            Infantry_M1_Garand = vehicles.Infantry.Infantry_M1_Garand
            Infantry_SMLE_No_4_Mk_1 = vehicles.Infantry.Infantry_SMLE_No_4_Mk_1

        class AirDefence:
            AAA_8_8cm_Flak_18 = vehicles.AirDefence.AAA_8_8cm_Flak_18
            AAA_Flak_38 = vehicles.AirDefence.AAA_Flak_38
            AAA_8_8cm_Flak_36 = vehicles.AirDefence.AAA_8_8cm_Flak_36
            AAA_8_8cm_Flak_37 = vehicles.AirDefence.AAA_8_8cm_Flak_37
            AAA_Flak_Vierling_38 = vehicles.AirDefence.AAA_Flak_Vierling_38
            AAA_Kdo_G_40 = vehicles.AirDefence.AAA_Kdo_G_40
            Flak_Searchlight_37 = vehicles.AirDefence.Flak_Searchlight_37
            Maschinensatz_33 = vehicles.AirDefence.Maschinensatz_33
            AAA_8_8cm_Flak_41 = vehicles.AirDefence.AAA_8_8cm_Flak_41
            EWR_1L13 = vehicles.AirDefence.EWR_1L13
            SAM_SA_19_Tunguska_2S6 = vehicles.AirDefence.SAM_SA_19_Tunguska_2S6
            EWR_55G6 = vehicles.AirDefence.EWR_55G6
            SAM_SA_3_S_125_LN_5P73 = vehicles.AirDefence.SAM_SA_3_S_125_LN_5P73
            CP_9S80M1_Sborka = vehicles.AirDefence.CP_9S80M1_Sborka
            SAM_SA_6_Kub_STR_9S91 = vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91
            SAM_SA_6_Kub_LN_2P25 = vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25
            SAM_SA_8_Osa_9A33 = vehicles.AirDefence.SAM_SA_8_Osa_9A33
            SAM_SR_P_19 = vehicles.AirDefence.SAM_SR_P_19
            SAM_SA_2_LN_SM_90 = vehicles.AirDefence.SAM_SA_2_LN_SM_90
            SAM_SA_10_S_300PS_TR_30N6 = vehicles.AirDefence.SAM_SA_10_S_300PS_TR_30N6
            SAM_SA_10_S_300PS_SR_5N66M = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_5N66M
            SAM_SA_10_S_300PS_CP_54K6 = vehicles.AirDefence.SAM_SA_10_S_300PS_CP_54K6
            SAM_SA_10_S_300PS_LN_5P85C = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85C
            SAM_SA_10_S_300PS_LN_5P85D = vehicles.AirDefence.SAM_SA_10_S_300PS_LN_5P85D
            SAM_SA_10_S_300PS_SR_64H6E = vehicles.AirDefence.SAM_SA_10_S_300PS_SR_64H6E
            SAM_SA_11_Buk_CC_9S470M1 = vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1
            SAM_SA_11_Buk_LN_9A310M1 = vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1
            SAM_SA_11_Buk_SR_9S18M1 = vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1
            SAM_SA_18_Igla_comm = vehicles.AirDefence.SAM_SA_18_Igla_comm
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_SA_3_S_125_TR_SNR = vehicles.AirDefence.SAM_SA_3_S_125_TR_SNR
            SAM_SA_2_TR_SNR_75_Fan_Song = vehicles.AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song
            SAM_SA_9_Strela_1_9P31 = vehicles.AirDefence.SAM_SA_9_Strela_1_9P31
            SAM_SA_13_Strela_10M3_9A35M3 = vehicles.AirDefence.SAM_SA_13_Strela_10M3_9A35M3
            SAM_SA_15_Tor_9A331 = vehicles.AirDefence.SAM_SA_15_Tor_9A331
            AAA_ZU_23_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_on_Ural_375
            SPAAA_ZSU_23_4_Shilka = vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka
            AAA_ZU_23_Closed = vehicles.AirDefence.AAA_ZU_23_Closed
            AAA_ZU_23_Emplacement = vehicles.AirDefence.AAA_ZU_23_Emplacement
            AAA_Bofors_40mm = vehicles.AirDefence.AAA_Bofors_40mm
            AAA_Vulcan_M163 = vehicles.AirDefence.AAA_Vulcan_M163
            SAM_Hawk_TR_AN_MPQ_46 = vehicles.AirDefence.SAM_Hawk_TR_AN_MPQ_46
            SAM_Hawk_SR_AN_MPQ_50 = vehicles.AirDefence.SAM_Hawk_SR_AN_MPQ_50
            SAM_Hawk_LN_M192 = vehicles.AirDefence.SAM_Hawk_LN_M192
            SAM_Hawk_CWAR_AN_MPQ_55 = vehicles.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55
            SAM_Hawk_PCP = vehicles.AirDefence.SAM_Hawk_PCP
            SAM_Chaparral_M48 = vehicles.AirDefence.SAM_Chaparral_M48
            SAM_SA_18_Igla_S_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_S_MANPADS
            SAM_SA_18_Igla_S_comm = vehicles.AirDefence.SAM_SA_18_Igla_S_comm
            AAA_ZU_23_Insurgent_Closed = vehicles.AirDefence.AAA_ZU_23_Insurgent_Closed
            AAA_ZU_23_Insurgent = vehicles.AirDefence.AAA_ZU_23_Insurgent
            AAA_ZU_23_Insurgent_on_Ural_375 = vehicles.AirDefence.AAA_ZU_23_Insurgent_on_Ural_375
            SAM_Avenger_M1097 = vehicles.AirDefence.SAM_Avenger_M1097
            SAM_Roland_ADS = vehicles.AirDefence.SAM_Roland_ADS
            SAM_Roland_EWR = vehicles.AirDefence.SAM_Roland_EWR
            Stinger_MANPADS = vehicles.AirDefence.Stinger_MANPADS
            SAM_Stinger_comm = vehicles.AirDefence.SAM_Stinger_comm
            SAM_Stinger_comm_dsr = vehicles.AirDefence.SAM_Stinger_comm_dsr
            Rapier_FSA_Launcher = vehicles.AirDefence.Rapier_FSA_Launcher
            Rapier_FSA_Optical_Tracker = vehicles.AirDefence.Rapier_FSA_Optical_Tracker
            Rapier_FSA_Blindfire_Tracker = vehicles.AirDefence.Rapier_FSA_Blindfire_Tracker
            SAM_Patriot_AMG_AN_MRC_137 = vehicles.AirDefence.SAM_Patriot_AMG_AN_MRC_137
            SAM_Patriot_ECS_AN_MSQ_104 = vehicles.AirDefence.SAM_Patriot_ECS_AN_MSQ_104
            SAM_Patriot_LN_M901 = vehicles.AirDefence.SAM_Patriot_LN_M901
            SAM_Patriot_EPP_III = vehicles.AirDefence.SAM_Patriot_EPP_III
            SAM_Patriot_ICC = vehicles.AirDefence.SAM_Patriot_ICC
            SAM_Patriot_STR_AN_MPQ_53 = vehicles.AirDefence.SAM_Patriot_STR_AN_MPQ_53
            SPAAA_Gepard = vehicles.AirDefence.SPAAA_Gepard
            HQ_7_Self_Propelled_LN = vehicles.AirDefence.HQ_7_Self_Propelled_LN
            HQ_7_Self_Propelled_STR = vehicles.AirDefence.HQ_7_Self_Propelled_STR
            SAM_SA_18_Igla_MANPADS = vehicles.AirDefence.SAM_SA_18_Igla_MANPADS
            SAM_Linebacker_M6 = vehicles.AirDefence.SAM_Linebacker_M6

        class Fortification:
            Bunker_2 = vehicles.Fortification.Bunker_2
            Bunker_1 = vehicles.Fortification.Bunker_1
            Barracks_armed = vehicles.Fortification.Barracks_armed
            Watch_tower_armed = vehicles.Fortification.Watch_tower_armed
            Road_outpost = vehicles.Fortification.Road_outpost
            Outpost = vehicles.Fortification.Outpost
            Armed_house = vehicles.Fortification.Armed_house
            TACAN_Beacon__Man_Portable__TTS_3030 = vehicles.Fortification.TACAN_Beacon__Man_Portable__TTS_3030
            Bunker_with_SK_C_28_15cm_naval_gun = vehicles.Fortification.Bunker_with_SK_C_28_15cm_naval_gun
            Fire_control_bunker = vehicles.Fortification.Fire_control_bunker

        class Unarmed:
            Kübelwagen_82 = vehicles.Unarmed.Kübelwagen_82
            Blitz_3_6_6700A = vehicles.Unarmed.Blitz_3_6_6700A
            Sd_Kfz_2 = vehicles.Unarmed.Sd_Kfz_2
            Sd_Kfz_7 = vehicles.Unarmed.Sd_Kfz_7
            Horch_901_typ_40 = vehicles.Unarmed.Horch_901_typ_40
            Fuel_Truck_ATMZ_5 = vehicles.Unarmed.Fuel_Truck_ATMZ_5
            Fuel_Truck_ATZ_10 = vehicles.Unarmed.Fuel_Truck_ATZ_10
            Transport_GAZ_3307 = vehicles.Unarmed.Transport_GAZ_3307
            Transport_GAZ_66 = vehicles.Unarmed.Transport_GAZ_66
            Transport_IKARUS_280 = vehicles.Unarmed.Transport_IKARUS_280
            Transport_KAMAZ_43101 = vehicles.Unarmed.Transport_KAMAZ_43101
            Transport_LAZ_695 = vehicles.Unarmed.Transport_LAZ_695
            CP_SKP_11_ATC_Mobile_Command_Post = vehicles.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            Transport_ZIU_9 = vehicles.Unarmed.Transport_ZIU_9
            Transport_UAZ_469 = vehicles.Unarmed.Transport_UAZ_469
            Transport_fire_engine_Ural_ATsP_6 = vehicles.Unarmed.Transport_fire_engine_Ural_ATsP_6
            CP_Ural_375_PBU = vehicles.Unarmed.CP_Ural_375_PBU
            Transport_Ural_375 = vehicles.Unarmed.Transport_Ural_375
            GPU_APA_5D_on_Ural_4320 = vehicles.Unarmed.GPU_APA_5D_on_Ural_4320
            Transport_Ural_4320_31_Armored = vehicles.Unarmed.Transport_Ural_4320_31_Armored
            Transport_Ural_4320T = vehicles.Unarmed.Transport_Ural_4320T
            Transport_VAZ_2109 = vehicles.Unarmed.Transport_VAZ_2109
            GPU_APA_80_on_ZiL_131 = vehicles.Unarmed.GPU_APA_80_on_ZiL_131
            Transport_ZIL_131_KUNG = vehicles.Unarmed.Transport_ZIL_131_KUNG
            Transport_ZIL_4331 = vehicles.Unarmed.Transport_ZIL_4331
            Willys_MB = vehicles.Unarmed.Willys_MB
            Bedford_MWD = vehicles.Unarmed.Bedford_MWD
            CCKW_353 = vehicles.Unarmed.CCKW_353
            APC_M1025_HMMWV = vehicles.Unarmed.APC_M1025_HMMWV
            Transport_KrAZ_6322 = vehicles.Unarmed.Transport_KrAZ_6322
            Transport_GAZ_3308 = vehicles.Unarmed.Transport_GAZ_3308
            Transport_MAZ_6303 = vehicles.Unarmed.Transport_MAZ_6303
            Transport_M818 = vehicles.Unarmed.Transport_M818
            HEMTT_TFFT = vehicles.Unarmed.HEMTT_TFFT
            Tanker_M978_HEMTT = vehicles.Unarmed.Tanker_M978_HEMTT
            Land_Rover_101_FC = vehicles.Unarmed.Land_Rover_101_FC
            Land_Rover_109_S3 = vehicles.Unarmed.Land_Rover_109_S3
            CP_Predator_GCS = vehicles.Unarmed.CP_Predator_GCS
            CP_Predator_TrojanSpirit = vehicles.Unarmed.CP_Predator_TrojanSpirit
            APC_Tigr_233036 = vehicles.Unarmed.APC_Tigr_233036

        class Armor:
            HT_Pz_Kpfw_VI_Tiger_I = vehicles.Armor.HT_Pz_Kpfw_VI_Tiger_I
            HT_Pz_Kpfw_VI_Ausf__B__Tiger_II = vehicles.Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II
            MT_Pz_Kpfw_V_Panther_Ausf_G = vehicles.Armor.MT_Pz_Kpfw_V_Panther_Ausf_G
            MT_Pz_Kpfw_IV_Ausf_H = vehicles.Armor.MT_Pz_Kpfw_IV_Ausf_H
            TD_Jagdpanther_G1 = vehicles.Armor.TD_Jagdpanther_G1
            TD_Jagdpanzer_IV = vehicles.Armor.TD_Jagdpanzer_IV
            StuG_IV = vehicles.Armor.StuG_IV
            IFV_Sd_Kfz_234_2_Puma = vehicles.Armor.IFV_Sd_Kfz_234_2_Puma
            APC_Sd_Kfz_251 = vehicles.Armor.APC_Sd_Kfz_251
            StuG_III_Ausf__G = vehicles.Armor.StuG_III_Ausf__G
            Sd_Kfz_184_Elefant = vehicles.Armor.Sd_Kfz_184_Elefant
            IFV_BMD_1 = vehicles.Armor.IFV_BMD_1
            IFV_BMP_1 = vehicles.Armor.IFV_BMP_1
            IFV_BMP_2 = vehicles.Armor.IFV_BMP_2
            IFV_BMP_3 = vehicles.Armor.IFV_BMP_3
            FDDM_Grad = vehicles.Armor.FDDM_Grad
            ARV_BRDM_2 = vehicles.Armor.ARV_BRDM_2
            ARV_BTR_RD = vehicles.Armor.ARV_BTR_RD
            APC_BTR_80 = vehicles.Armor.APC_BTR_80
            APC_MTLB = vehicles.Armor.APC_MTLB
            MBT_T_55 = vehicles.Armor.MBT_T_55
            MBT_T_72B = vehicles.Armor.MBT_T_72B
            MBT_T_80U = vehicles.Armor.MBT_T_80U
            APC_M2A1 = vehicles.Armor.APC_M2A1
            CT_Cromwell_IV = vehicles.Armor.CT_Cromwell_IV
            ST_Centaur_IV = vehicles.Armor.ST_Centaur_IV
            MT_M4_Sherman = vehicles.Armor.MT_M4_Sherman
            TD_M10_GMC = vehicles.Armor.TD_M10_GMC
            MT_M4A4_Sherman_Firefly = vehicles.Armor.MT_M4A4_Sherman_Firefly
            HIT_Churchill_VII = vehicles.Armor.HIT_Churchill_VII
            M30_Cargo_Carrier = vehicles.Armor.M30_Cargo_Carrier
            LAC_M8_Greyhound = vehicles.Armor.LAC_M8_Greyhound
            APC_M1043_HMMWV_Armament = vehicles.Armor.APC_M1043_HMMWV_Armament
            APC_M113 = vehicles.Armor.APC_M113
            MBT_M60A3_Patton = vehicles.Armor.MBT_M60A3_Patton
            MBT_M1A2_Abrams = vehicles.Armor.MBT_M1A2_Abrams
            ATGM_M1045_HMMWV_TOW = vehicles.Armor.ATGM_M1045_HMMWV_TOW
            MBT_T_90 = vehicles.Armor.MBT_T_90
            APC_AAV_7 = vehicles.Armor.APC_AAV_7
            MBT_Leopard_1A3 = vehicles.Armor.MBT_Leopard_1A3
            MBT_Leopard_2 = vehicles.Armor.MBT_Leopard_2
            IFV_M2A2_Bradley = vehicles.Armor.IFV_M2A2_Bradley
            TPz_Fuchs = vehicles.Armor.TPz_Fuchs
            APC_Cobra = vehicles.Armor.APC_Cobra
            IFV_LAV_25 = vehicles.Armor.IFV_LAV_25
            MBT_Merkava_Mk__4 = vehicles.Armor.MBT_Merkava_Mk__4
            IFV_Marder = vehicles.Armor.IFV_Marder
            MBT_Leclerc = vehicles.Armor.MBT_Leclerc
            ZBD_04A = vehicles.Armor.ZBD_04A
            ZTZ_96B = vehicles.Armor.ZTZ_96B
            MBT_Challenger_II = vehicles.Armor.MBT_Challenger_II
            APC_M1126_Stryker_ICV = vehicles.Armor.APC_M1126_Stryker_ICV
            SPG_M1128_Stryker_MGS = vehicles.Armor.SPG_M1128_Stryker_MGS
            ATGM_M1134_Stryker = vehicles.Armor.ATGM_M1134_Stryker
            IFV_MCV_80 = vehicles.Armor.IFV_MCV_80

        class MissilesSS:
            V_1_ramp = vehicles.MissilesSS.V_1_ramp
            SRBM_SS_1C_Scud_B_9K72_LN_9P117M = vehicles.MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M
            SS_N_2_Silkworm = vehicles.MissilesSS.SS_N_2_Silkworm
            Silkworm_Radar = vehicles.MissilesSS.Silkworm_Radar

        class Locomotive:
            Electric_locomotive_VL80 = vehicles.Locomotive.Electric_locomotive_VL80
            Locomotive_CHME3T = vehicles.Locomotive.Locomotive_CHME3T
            ES44AH = vehicles.Locomotive.ES44AH
            DRG_Class_86 = vehicles.Locomotive.DRG_Class_86

        class Carriage:
            Coach_for_cargo = vehicles.Carriage.Coach_for_cargo
            Coach_for_open_cargo = vehicles.Carriage.Coach_for_open_cargo
            Coach_a_tank_blue = vehicles.Carriage.Coach_a_tank_blue
            Coach_a_tank_yellow = vehicles.Carriage.Coach_a_tank_yellow
            Coach_for_passengers = vehicles.Carriage.Coach_for_passengers
            Coach_flatbed = vehicles.Carriage.Coach_flatbed
            Boxcartrinity = vehicles.Carriage.Boxcartrinity
            Tankcartrinity = vehicles.Carriage.Tankcartrinity
            Wellcarnsc = vehicles.Carriage.Wellcarnsc
            DR_50_ton_flat_wagon = vehicles.Carriage.DR_50_ton_flat_wagon
            German_covered_wagon_G10 = vehicles.Carriage.German_covered_wagon_G10
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon
            German_tank_wagon = vehicles.Carriage.German_tank_wagon

    class Plane:
        A_10C = planes.A_10C
        FW_190A8 = planes.FW_190A8
        Bf_109K_4 = planes.Bf_109K_4
        SpitfireLFMkIX = planes.SpitfireLFMkIX
        SpitfireLFMkIXCW = planes.SpitfireLFMkIXCW
        P_47D_30 = planes.P_47D_30
        P_47D_30bl1 = planes.P_47D_30bl1
        P_47D_40 = planes.P_47D_40
        A_10A = planes.A_10A
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
        A_20G = planes.A_20G
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
        A_10C_2 = planes.A_10C_2
        F_14B = planes.F_14B
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
        Plane.A_10A,
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
        Plane.A_20G,
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
        Plane.A_10C_2,
        Plane.F_14B,
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
        Armed_speedboat = ships.Armed_speedboat
        Uboat_VIIC_U_flak = ships.Uboat_VIIC_U_flak
        Schnellboot_type_S130 = ships.Schnellboot_type_S130
        FFL_1124_4_Grisha = ships.FFL_1124_4_Grisha
        SSK_877 = ships.SSK_877
        Bulk_cargo_ship_Yakushev = ships.Bulk_cargo_ship_Yakushev
        Dry_cargo_ship_Ivanov = ships.Dry_cargo_ship_Ivanov
        Tanker_Elnya_160 = ships.Tanker_Elnya_160
        CV_1143_5_Admiral_Kuznetsov = ships.CV_1143_5_Admiral_Kuznetsov
        FSG_1241_1MP_Molniya = ships.FSG_1241_1MP_Molniya
        CG_1164_Moskva = ships.CG_1164_Moskva
        FFG_11540_Neustrashimy = ships.FFG_11540_Neustrashimy
        FF_1135M_Rezky = ships.FF_1135M_Rezky
        SSK_641B = ships.SSK_641B
        Civil_boat_Zvezdny = ships.Civil_boat_Zvezdny
        LST_Mk_II = ships.LST_Mk_II
        LS_Samuel_Chase = ships.LS_Samuel_Chase
        LCVP__Higgins_boat = ships.LCVP__Higgins_boat
        Oliver_Hazzard_Perry_class = ships.Oliver_Hazzard_Perry_class
        CGN_1144_2_Pyotr_Velikiy = ships.CGN_1144_2_Pyotr_Velikiy
        CV_1143_5_Admiral_Kuznetsov_2017 = ships.CV_1143_5_Admiral_Kuznetsov_2017
        Type_052B_Destroyer = ships.Type_052B_Destroyer
        Type_054A_Frigate = ships.Type_054A_Frigate
        Type_052C_Destroyer = ships.Type_052C_Destroyer
        Type_093_Attack_Submarine = ships.Type_093_Attack_Submarine
        Type_071_Amphibious_Transport_Dock = ships.Type_071_Amphibious_Transport_Dock
        CVN_70_Carl_Vinson = ships.CVN_70_Carl_Vinson
        Ticonderoga_class = ships.Ticonderoga_class
        CVN_74_John_C__Stennis = ships.CVN_74_John_C__Stennis
        LHA_1_Tarawa = ships.LHA_1_Tarawa
        USS_Arleigh_Burke_IIa = ships.USS_Arleigh_Burke_IIa
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
}


def get_by_id(_id: int):
    """Returns a new country object for the given country id

    Args:
        _id: id for the country

    Returns:
        Country: a new country object
    """
    return country_dict[_id]()

