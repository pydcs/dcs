# This file is generated from pydcs_export.lua

import dcs.unittype as unittype


class Artillery:

    class X_2B11_mortar(unittype.VehicleType):
        id = "2B11 mortar"
        name = "Mortar 2B11 120mm"
        detection_range = 0
        threat_range = 7000
        air_weapon_dist = 7000

    class SAU_Gvozdika(unittype.VehicleType):
        id = "SAU Gvozdika"
        name = "SPH 2S1 Gvozdika 122mm"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class SAU_Msta(unittype.VehicleType):
        id = "SAU Msta"
        name = "SPH 2S19 Msta 152mm"
        detection_range = 0
        threat_range = 23500
        air_weapon_dist = 23500

    class SAU_Akatsia(unittype.VehicleType):
        id = "SAU Akatsia"
        name = "SPH 2S3 Akatsia 152mm"
        detection_range = 0
        threat_range = 17000
        air_weapon_dist = 17000

    class SAU_2_C9(unittype.VehicleType):
        id = "SAU 2-C9"
        name = "SPM 2S9 Nona 120mm M"
        detection_range = 0
        threat_range = 7000
        air_weapon_dist = 7000

    class M_109(unittype.VehicleType):
        id = "M-109"
        name = "SPH M109 Paladin 155mm"
        detection_range = 0
        threat_range = 22000
        air_weapon_dist = 22000
        eplrs = True

    class SpGH_Dana(unittype.VehicleType):
        id = "SpGH_Dana"
        name = "SPH Dana vz77 152mm"
        detection_range = 0
        threat_range = 18700
        air_weapon_dist = 18700

    class Grad_FDDM(unittype.VehicleType):
        id = "Grad_FDDM"
        name = "Grad MRL FDDM (FC)"
        detection_range = 0
        threat_range = 1000
        air_weapon_dist = 1000

    class MLRS_FDDM(unittype.VehicleType):
        id = "MLRS FDDM"
        name = "MRLS FDDM (FC)"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class Grad_URAL(unittype.VehicleType):
        id = "Grad-URAL"
        name = "MLRS BM-21 Grad 122mm"
        detection_range = 0
        threat_range = 19000
        air_weapon_dist = 19000

    class Uragan_BM_27(unittype.VehicleType):
        id = "Uragan_BM-27"
        name = "MLRS 9K57 Uragan BM-27 220mm"
        detection_range = 0
        threat_range = 35800
        air_weapon_dist = 35800

    class Smerch(unittype.VehicleType):
        id = "Smerch"
        name = "MLRS 9A52 Smerch CM 300mm"
        detection_range = 0
        threat_range = 70000
        air_weapon_dist = 70000

    class Smerch_HE(unittype.VehicleType):
        id = "Smerch_HE"
        name = "MLRS 9A52 Smerch HE 300mm"
        detection_range = 0
        threat_range = 70000
        air_weapon_dist = 70000

    class MLRS(unittype.VehicleType):
        id = "MLRS"
        name = "MLRS M270 227mm"
        detection_range = 0
        threat_range = 32000
        air_weapon_dist = 32000
        eplrs = True

    class L118_Unit(unittype.VehicleType):
        id = "L118_Unit"
        name = "L118 Light Artillery Gun"
        detection_range = 500
        threat_range = 17200
        air_weapon_dist = 17200

    class HL_B8M1(unittype.VehicleType):
        id = "HL_B8M1"
        name = "MLRS HL with B8M1 80mm"
        detection_range = 5000
        threat_range = 5000
        air_weapon_dist = 5000

    class Tt_B8M1(unittype.VehicleType):
        id = "tt_B8M1"
        name = "MLRS LC with B8M1 80mm"
        detection_range = 5000
        threat_range = 5000
        air_weapon_dist = 5000

    class T155_Firtina(unittype.VehicleType):
        id = "T155_Firtina"
        name = "SPH T155 Firtina 155mm"
        detection_range = 0
        threat_range = 41000
        air_weapon_dist = 41000

    class PLZ05(unittype.VehicleType):
        id = "PLZ05"
        name = "PLZ-05"
        detection_range = 0
        threat_range = 23500
        air_weapon_dist = 23500
        eplrs = True

    class Wespe124(unittype.VehicleType):
        id = "Wespe124"
        name = "SPH Sd.Kfz.124 Wespe 105mm"
        detection_range = 0
        threat_range = 10500
        air_weapon_dist = 0

    class Pak40(unittype.VehicleType):
        id = "Pak40"
        name = "FH Pak 40 75mm"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class LeFH_18_40_105(unittype.VehicleType):
        id = "LeFH_18-40-105"
        name = "FH LeFH-18 105mm"
        detection_range = 0
        threat_range = 10500
        air_weapon_dist = 0

    class M12_GMC(unittype.VehicleType):
        id = "M12_GMC"
        name = "SPH M12 GMC 155mm"
        detection_range = 0
        threat_range = 18300
        air_weapon_dist = 0

    class M2A1_105(unittype.VehicleType):
        id = "M2A1-105"
        name = "FH M2A1 105mm"
        detection_range = 0
        threat_range = 11500
        air_weapon_dist = 0


class Infantry:

    class Paratrooper_RPG_16(unittype.VehicleType):
        id = "Paratrooper RPG-16"
        name = "Paratrooper RPG-16"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Paratrooper_AKS_74(unittype.VehicleType):
        id = "Paratrooper AKS-74"
        name = "Paratrooper AKS"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_AK_Ins(unittype.VehicleType):
        id = "Infantry AK Ins"
        name = "Insurgent AK-74"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_AK(unittype.VehicleType):
        id = "Soldier AK"
        name = "Infantry AK-74"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_AK(unittype.VehicleType):
        id = "Infantry AK"
        name = "Infantry AK-74 Rus ver1"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_M249(unittype.VehicleType):
        id = "Soldier M249"
        name = "Infantry M249"
        detection_range = 0
        threat_range = 700
        air_weapon_dist = 700

    class Soldier_M4(unittype.VehicleType):
        id = "Soldier M4"
        name = "Infantry M4"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_M4_GRG(unittype.VehicleType):
        id = "Soldier M4 GRG"
        name = "Infantry M4 Georgia"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_RPG(unittype.VehicleType):
        id = "Soldier RPG"
        name = "Infantry RPG"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_AK_ver2(unittype.VehicleType):
        id = "Infantry AK ver2"
        name = "Infantry AK-74 Rus ver2"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_AK_ver3(unittype.VehicleType):
        id = "Infantry AK ver3"
        name = "Infantry AK-74 Rus ver3"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class JTAC(unittype.VehicleType):
        id = "JTAC"
        name = "JTAC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class Soldier_mauser98(unittype.VehicleType):
        id = "soldier_mauser98"
        name = "Infantry Mauser 98"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_wwii_br_01(unittype.VehicleType):
        id = "soldier_wwii_br_01"
        name = "Infantry SMLE No.4 Mk-1"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_wwii_us(unittype.VehicleType):
        id = "soldier_wwii_us"
        name = "Infantry M1 Garand"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500


class AirDefence:

    class X_2S6_Tunguska(unittype.VehicleType):
        id = "2S6 Tunguska"
        name = "SAM SA-19 Tunguska \"Grison\" "
        detection_range = 18000
        threat_range = 8000
        air_weapon_dist = 8000

    class Kub_2P25_ln(unittype.VehicleType):
        id = "Kub 2P25 ln"
        name = "SAM SA-6 Kub \"Gainful\" TEL"
        detection_range = 0
        threat_range = 25000
        air_weapon_dist = 25000

    class X_5p73_s_125_ln(unittype.VehicleType):
        id = "5p73 s-125 ln"
        name = "SAM SA-3 S-125 \"Goa\" LN"
        detection_range = 0
        threat_range = 18000
        air_weapon_dist = 18000

    class SA_11_Buk_LN_9A310M1(unittype.VehicleType):
        id = "SA-11 Buk LN 9A310M1"
        name = "SAM SA-11 Buk \"Gadfly\" Fire Dome TEL"
        detection_range = 50000
        threat_range = 35000
        air_weapon_dist = 35000

    class Osa_9A33_ln(unittype.VehicleType):
        id = "Osa 9A33 ln"
        name = "SAM SA-8 Osa \"Gecko\" TEL"
        detection_range = 30000
        threat_range = 10300
        air_weapon_dist = 10300

    class Tor_9A331(unittype.VehicleType):
        id = "Tor 9A331"
        name = "SAM SA-15 Tor \"Gauntlet\""
        detection_range = 25000
        threat_range = 12000
        air_weapon_dist = 12000

    class Strela_10M3(unittype.VehicleType):
        id = "Strela-10M3"
        name = "SAM SA-13 Strela 10M3 \"Gopher\" TEL"
        detection_range = 8000
        threat_range = 5000
        air_weapon_dist = 5000

    class Strela_1_9P31(unittype.VehicleType):
        id = "Strela-1 9P31"
        name = "SAM SA-9 Strela 1 \"Gaskin\" TEL"
        detection_range = 5000
        threat_range = 4200
        air_weapon_dist = 4200

    class SA_11_Buk_CC_9S470M1(unittype.VehicleType):
        id = "SA-11 Buk CC 9S470M1"
        name = "SAM SA-11 Buk \"Gadfly\" C2 "
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Patriot_AMG(unittype.VehicleType):
        id = "Patriot AMG"
        name = "SAM Patriot CR (AMG AN/MRC-137)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Patriot_ECS(unittype.VehicleType):
        id = "Patriot ECS"
        name = "SAM Patriot ECS"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class Gepard(unittype.VehicleType):
        id = "Gepard"
        name = "SPAAA Gepard"
        detection_range = 15000
        threat_range = 4000
        air_weapon_dist = 4000

    class Hawk_pcp(unittype.VehicleType):
        id = "Hawk pcp"
        name = "SAM Hawk Platoon Command Post (PCP)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Vulcan(unittype.VehicleType):
        id = "Vulcan"
        name = "SPAAA Vulcan M163"
        detection_range = 5000
        threat_range = 2000
        air_weapon_dist = 2000
        eplrs = True

    class Hawk_ln(unittype.VehicleType):
        id = "Hawk ln"
        name = "SAM Hawk LN M192"
        detection_range = 0
        threat_range = 45000
        air_weapon_dist = 45000

    class M48_Chaparral(unittype.VehicleType):
        id = "M48 Chaparral"
        name = "SAM Chaparral M48"
        detection_range = 10000
        threat_range = 8500
        air_weapon_dist = 8500
        eplrs = True

    class M6_Linebacker(unittype.VehicleType):
        id = "M6 Linebacker"
        name = "SAM Linebacker - Bradley M6"
        detection_range = 8000
        threat_range = 4500
        air_weapon_dist = 4500
        eplrs = True

    class Patriot_ln(unittype.VehicleType):
        id = "Patriot ln"
        name = "SAM Patriot LN"
        detection_range = 0
        threat_range = 100000
        air_weapon_dist = 100000

    class M1097_Avenger(unittype.VehicleType):
        id = "M1097 Avenger"
        name = "SAM Avenger (Stinger)"
        detection_range = 5200
        threat_range = 4500
        air_weapon_dist = 4500
        eplrs = True

    class Patriot_EPP(unittype.VehicleType):
        id = "Patriot EPP"
        name = "SAM Patriot EPP-III"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Patriot_cp(unittype.VehicleType):
        id = "Patriot cp"
        name = "SAM Patriot C2 ICC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Roland_ADS(unittype.VehicleType):
        id = "Roland ADS"
        name = "SAM Roland ADS"
        detection_range = 12000
        threat_range = 8000
        air_weapon_dist = 8000

    class Soldier_stinger(unittype.VehicleType):
        id = "Soldier stinger"
        name = "MANPADS Stinger"
        detection_range = 5000
        threat_range = 4500
        air_weapon_dist = 4500

    class Stinger_comm_dsr(unittype.VehicleType):
        id = "Stinger comm dsr"
        name = "MANPADS Stinger C2 Desert"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class Stinger_comm(unittype.VehicleType):
        id = "Stinger comm"
        name = "MANPADS Stinger C2"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class ZSU_23_4_Shilka(unittype.VehicleType):
        id = "ZSU-23-4 Shilka"
        name = "SPAAA ZSU-23-4 Shilka \"Gun Dish\""
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class ZU_23_Emplacement_Closed(unittype.VehicleType):
        id = "ZU-23 Emplacement Closed"
        name = "AAA ZU-23 Closed Emplacement"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class ZU_23_Emplacement(unittype.VehicleType):
        id = "ZU-23 Emplacement"
        name = "AAA ZU-23 Emplacement"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class Ural_375_ZU_23(unittype.VehicleType):
        id = "Ural-375 ZU-23"
        name = "AAA ZU-23 on Ural-4320"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class ZU_23_Closed_Insurgent(unittype.VehicleType):
        id = "ZU-23 Closed Insurgent"
        name = "AAA ZU-23 Insurgent Closed Emplacement"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class Ural_375_ZU_23_Insurgent(unittype.VehicleType):
        id = "Ural-375 ZU-23 Insurgent"
        name = "AAA ZU-23 on Ural-4320 Insurgent"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class ZU_23_Insurgent(unittype.VehicleType):
        id = "ZU-23 Insurgent"
        name = "AAA ZU-23 Insurgent Emplacement"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class SA_18_Igla_manpad(unittype.VehicleType):
        id = "SA-18 Igla manpad"
        name = "MANPADS SA-18 Igla \"Grouse\""
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class SA_18_Igla_comm(unittype.VehicleType):
        id = "SA-18 Igla comm"
        name = "MANPADS SA-18 Igla \"Grouse\" C2"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class SA_18_Igla_S_manpad(unittype.VehicleType):
        id = "SA-18 Igla-S manpad"
        name = "MANPADS SA-18 Igla-S \"Grouse\""
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class SA_18_Igla_S_comm(unittype.VehicleType):
        id = "SA-18 Igla-S comm"
        name = "MANPADS SA-18 Igla-S \"Grouse\" C2"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class Igla_manpad_INS(unittype.VehicleType):
        id = "Igla manpad INS"
        name = "MANPADS SA-18 Igla \"Grouse\" Ins"
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class X_1L13_EWR(unittype.VehicleType):
        id = "1L13 EWR"
        name = "EWR 1L13"
        detection_range = 300000
        threat_range = 0
        air_weapon_dist = 0

    class Kub_1S91_str(unittype.VehicleType):
        id = "Kub 1S91 str"
        name = "SAM SA-6 Kub \"Straight Flush\" STR"
        detection_range = 70000
        threat_range = 0
        air_weapon_dist = 0

    class X_55G6_EWR(unittype.VehicleType):
        id = "55G6 EWR"
        name = "EWR 55G6"
        detection_range = 400000
        threat_range = 0
        air_weapon_dist = 0

    class SA_11_Buk_SR_9S18M1(unittype.VehicleType):
        id = "SA-11 Buk SR 9S18M1"
        name = "SAM SA-11 Buk \"Gadfly\" Snow Drift SR"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class Dog_Ear_radar(unittype.VehicleType):
        id = "Dog Ear radar"
        name = "MCC-SR Sborka \"Dog Ear\" SR"
        detection_range = 35000
        threat_range = 0
        air_weapon_dist = 0

    class Hawk_tr(unittype.VehicleType):
        id = "Hawk tr"
        name = "SAM Hawk TR (AN/MPQ-46)"
        detection_range = 90000
        threat_range = 0
        air_weapon_dist = 0

    class Hawk_sr(unittype.VehicleType):
        id = "Hawk sr"
        name = "SAM Hawk SR (AN/MPQ-50)"
        detection_range = 90000
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class Patriot_str(unittype.VehicleType):
        id = "Patriot str"
        name = "SAM Patriot STR"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class Hawk_cwar(unittype.VehicleType):
        id = "Hawk cwar"
        name = "SAM Hawk CWAR AN/MPQ-55"
        detection_range = 70000
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class P_19_s_125_sr(unittype.VehicleType):
        id = "p-19 s-125 sr"
        name = "SAM SA-2/3/5 P19 \"Flat Face\" SR "
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class Roland_Radar(unittype.VehicleType):
        id = "Roland Radar"
        name = "SAM Roland EWR"
        detection_range = 35000
        threat_range = 0
        air_weapon_dist = 0

    class Snr_s_125_tr(unittype.VehicleType):
        id = "snr s-125 tr"
        name = "SAM SA-3 S-125 \"Low Blow\" TR"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class HEMTT_C_RAM_Phalanx(unittype.VehicleType):
        id = "HEMTT_C-RAM_Phalanx"
        name = "LPWS C-RAM"
        detection_range = 10000
        threat_range = 2000
        air_weapon_dist = 2000
        eplrs = True

    class S_300PS_5P85C_ln(unittype.VehicleType):
        id = "S-300PS 5P85C ln"
        name = "SAM SA-10 S-300 \"Grumble\" TEL C"
        detection_range = 0
        threat_range = 120000
        air_weapon_dist = 120000

    class S_300PS_5P85D_ln(unittype.VehicleType):
        id = "S-300PS 5P85D ln"
        name = "SAM SA-10 S-300 \"Grumble\" TEL D"
        detection_range = 0
        threat_range = 120000
        air_weapon_dist = 120000

    class S_300PS_54K6_cp(unittype.VehicleType):
        id = "S-300PS 54K6 cp"
        name = "SAM SA-10 S-300 \"Grumble\" C2"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class S_300PS_40B6M_tr(unittype.VehicleType):
        id = "S-300PS 40B6M tr"
        name = "SAM SA-10 S-300 \"Grumble\" Flap Lid-A TR"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class S_300PS_64H6E_sr(unittype.VehicleType):
        id = "S-300PS 64H6E sr"
        name = "SAM SA-10 S-300 \"Grumble\" Big Bird SR"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class S_300PS_40B6MD_sr_19J6(unittype.VehicleType):
        id = "S-300PS 40B6MD sr_19J6"
        name = "SAM SA-10 S-300 \"Grumble\" Tin Shield SR"
        detection_range = 150000
        threat_range = 0
        air_weapon_dist = 0

    class S_300PS_5H63C_30H6_tr(unittype.VehicleType):
        id = "S-300PS 5H63C 30H6_tr"
        name = "SAM SA-10 S-300 \"Grumble\" Flap Lid-B TR"
        detection_range = 120000
        threat_range = 0
        air_weapon_dist = 0

    class S_300PS_40B6MD_sr(unittype.VehicleType):
        id = "S-300PS 40B6MD sr"
        name = "SAM SA-10 S-300 \"Grumble\" Clam Shell SR"
        detection_range = 60000
        threat_range = 0
        air_weapon_dist = 0

    class KS_19(unittype.VehicleType):
        id = "KS-19"
        name = "AAA KS-19 100mm"
        detection_range = 0
        threat_range = 20000
        air_weapon_dist = 20000

    class SON_9(unittype.VehicleType):
        id = "SON_9"
        name = "AAA Fire Can SON-9"
        detection_range = 55000
        threat_range = 0
        air_weapon_dist = 0

    class HL_ZU_23(unittype.VehicleType):
        id = "HL_ZU-23"
        name = "SPAAA HL with ZU-23"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class Tt_ZU_23(unittype.VehicleType):
        id = "tt_ZU-23"
        name = "SPAAA LC with ZU-23"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 0

    class NASAMS_Radar_MPQ64F1(unittype.VehicleType):
        id = "NASAMS_Radar_MPQ64F1"
        name = "SAM NASAMS SR MPQ64F1"
        detection_range = 50000
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class NASAMS_Command_Post(unittype.VehicleType):
        id = "NASAMS_Command_Post"
        name = "SAM NASAMS C2"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class NASAMS_LN_B(unittype.VehicleType):
        id = "NASAMS_LN_B"
        name = "SAM NASAMS LN AIM-120B"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class NASAMS_LN_C(unittype.VehicleType):
        id = "NASAMS_LN_C"
        name = "SAM NASAMS LN AIM-120C"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class FPS_117_Dome(unittype.VehicleType):
        id = "FPS-117 Dome"
        name = "EWR AN/FPS-117 Radar (domed)"
        detection_range = 400000
        threat_range = 0
        air_weapon_dist = 0

    class FPS_117_ECS(unittype.VehicleType):
        id = "FPS-117 ECS"
        name = "EWR AN/FPS-117 ECS"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class FPS_117(unittype.VehicleType):
        id = "FPS-117"
        name = "EWR AN/FPS-117 Radar"
        detection_range = 463000
        threat_range = 0
        air_weapon_dist = 0

    class RD_75(unittype.VehicleType):
        id = "RD_75"
        name = "SAM SA-2 S-75 RD-75 Amazonka RF"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class S_75M_Volhov(unittype.VehicleType):
        id = "S_75M_Volhov"
        name = "SAM SA-2 S-75 \"Guideline\" LN"
        detection_range = 0
        threat_range = 43000
        air_weapon_dist = 43000

    class SNR_75V(unittype.VehicleType):
        id = "SNR_75V"
        name = "SAM SA-2 S-75 \"Fan Song\" TR"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class RLS_19J6(unittype.VehicleType):
        id = "RLS_19J6"
        name = "SAM SA-5 S-200 ST-68U \"Tin Shield\" SR"
        detection_range = 150000
        threat_range = 0
        air_weapon_dist = 0

    class RPC_5N62V(unittype.VehicleType):
        id = "RPC_5N62V"
        name = "SAM SA-5 S-200 \"Square Pair\" TR"
        detection_range = 400000
        threat_range = 0
        air_weapon_dist = 0

    class S_200_Launcher(unittype.VehicleType):
        id = "S-200_Launcher"
        name = "SAM SA-5 S-200 \"Gammon\" LN"
        detection_range = 0
        threat_range = 255000
        air_weapon_dist = 255000

    class ZSU_57_2(unittype.VehicleType):
        id = "ZSU_57_2"
        name = "SPAAA ZSU-57-2"
        detection_range = 5000
        threat_range = 7000
        air_weapon_dist = 7000

    class S_60_Type59_Artillery(unittype.VehicleType):
        id = "S-60_Type59_Artillery"
        name = "AAA S-60 57mm"
        detection_range = 5000
        threat_range = 6000
        air_weapon_dist = 6000

    class Generator_5i57(unittype.VehicleType):
        id = "generator_5i57"
        name = "Diesel Power Station 5I57A"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Rapier_fsa_launcher(unittype.VehicleType):
        id = "rapier_fsa_launcher"
        name = "SAM Rapier LN"
        detection_range = 30000
        threat_range = 6800
        air_weapon_dist = 6800

    class Rapier_fsa_optical_tracker_unit(unittype.VehicleType):
        id = "rapier_fsa_optical_tracker_unit"
        name = "SAM Rapier Tracker"
        detection_range = 20000
        threat_range = 0
        air_weapon_dist = 0

    class Rapier_fsa_blindfire_radar(unittype.VehicleType):
        id = "rapier_fsa_blindfire_radar"
        name = "SAM Rapier Blindfire TR"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class Bofors40(unittype.VehicleType):
        id = "bofors40"
        name = "AAA Bofors 40mm"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 4000

    class Flak18(unittype.VehicleType):
        id = "flak18"
        name = "AAA 8,8cm Flak 18"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 5000

    class HQ_7_LN_SP(unittype.VehicleType):
        id = "HQ-7_LN_SP"
        name = "HQ-7 Self-Propelled LN"
        detection_range = 8000
        threat_range = 12000
        air_weapon_dist = 12000

    class HQ_7_LN_P(unittype.VehicleType):
        id = "HQ-7_LN_P"
        name = "HQ-7 LN (Player)"
        detection_range = 8000
        threat_range = 12000
        air_weapon_dist = 12000

    class HQ_7_STR_SP(unittype.VehicleType):
        id = "HQ-7_STR_SP"
        name = "HQ-7 Self-Propelled STR"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class Flak30(unittype.VehicleType):
        id = "flak30"
        name = "AAA Flak 38 20mm"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class Flak36(unittype.VehicleType):
        id = "flak36"
        name = "AAA 8,8cm Flak 36"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 5000

    class Flak37(unittype.VehicleType):
        id = "flak37"
        name = "AAA 8,8cm Flak 37"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 5000

    class Flak38(unittype.VehicleType):
        id = "flak38"
        name = "AAA Flak-Vierling 38 Quad 20mm"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class KDO_Mod40(unittype.VehicleType):
        id = "KDO_Mod40"
        name = "AAA Kdo.G.40"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class Flakscheinwerfer_37(unittype.VehicleType):
        id = "Flakscheinwerfer_37"
        name = "SL Flakscheinwerfer 37"
        detection_range = 15000
        threat_range = 15000
        air_weapon_dist = 0

    class Maschinensatz_33(unittype.VehicleType):
        id = "Maschinensatz_33"
        name = "Maschinensatz 33 Gen"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Flak41(unittype.VehicleType):
        id = "flak41"
        name = "AAA 8,8cm Flak 41"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 5000

    class FuMG_401(unittype.VehicleType):
        id = "FuMG-401"
        name = "EWR FuMG-401 Freya LZ"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class FuSe_65(unittype.VehicleType):
        id = "FuSe-65"
        name = "EWR FuSe-65 Würzburg-Riese"
        detection_range = 60000
        threat_range = 0
        air_weapon_dist = 0

    class QF_37_AA(unittype.VehicleType):
        id = "QF_37_AA"
        name = "AAA QF 3.7\""
        detection_range = 0
        threat_range = 9000
        air_weapon_dist = 9000

    class Allies_Director(unittype.VehicleType):
        id = "Allies_Director"
        name = "Allies Rangefinder (DRT)"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class M45_Quadmount(unittype.VehicleType):
        id = "M45_Quadmount"
        name = "AAA M45 Quadmount HB 12.7mm"
        detection_range = 0
        threat_range = 1500
        air_weapon_dist = 1500

    class M1_37mm(unittype.VehicleType):
        id = "M1_37mm"
        name = "AAA M1 37mm"
        detection_range = 0
        threat_range = 5700
        air_weapon_dist = 5700


class Fortification:

    class Bunker(unittype.VehicleType):
        id = "Bunker"
        name = "Bunker 2"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Sandbox(unittype.VehicleType):
        id = "Sandbox"
        name = "Bunker 1"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class House1arm(unittype.VehicleType):
        id = "house1arm"
        name = "Barracks armed"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class House2arm(unittype.VehicleType):
        id = "house2arm"
        name = "Watch tower armed"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Outpost_road(unittype.VehicleType):
        id = "outpost_road"
        name = "Road outpost"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Outpost_road_l(unittype.VehicleType):
        id = "outpost_road_l"
        name = "Road outpost_L"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Outpost_road_r(unittype.VehicleType):
        id = "outpost_road_r"
        name = "Road outpost-R"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Outpost(unittype.VehicleType):
        id = "outpost"
        name = "Outpost"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class HouseA_arm(unittype.VehicleType):
        id = "houseA_arm"
        name = "Building armed"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class TACAN_beacon(unittype.VehicleType):
        id = "TACAN_beacon"
        name = "Beacon TACAN Portable TTS 3030"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SK_C_28_naval_gun(unittype.VehicleType):
        id = "SK_C_28_naval_gun"
        name = "Gun 15cm SK C/28 Naval in Bunker"
        detection_range = 0
        threat_range = 20000
        air_weapon_dist = 0

    class Fire_control(unittype.VehicleType):
        id = "fire_control"
        name = "Bunker with Fire Control Center"
        detection_range = 0
        threat_range = 1100
        air_weapon_dist = 1100


class Unarmed:

    class Ural_4320_APA_5D(unittype.VehicleType):
        id = "Ural-4320 APA-5D"
        name = "GPU APA-5D on Ural 4320"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ATMZ_5(unittype.VehicleType):
        id = "ATMZ-5"
        name = "Refueler ATMZ-5"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ATZ_10(unittype.VehicleType):
        id = "ATZ-10"
        name = "Refueler ATZ-10"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class GAZ_3307(unittype.VehicleType):
        id = "GAZ-3307"
        name = "Truck GAZ-3307"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class GAZ_3308(unittype.VehicleType):
        id = "GAZ-3308"
        name = "Truck GAZ-3308"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class GAZ_66(unittype.VehicleType):
        id = "GAZ-66"
        name = "Truck GAZ-66"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class M978_HEMTT_Tanker(unittype.VehicleType):
        id = "M978 HEMTT Tanker"
        name = "Refueler M978 HEMTT"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class HEMTT_TFFT(unittype.VehicleType):
        id = "HEMTT TFFT"
        name = "Firefighter HEMMT TFFT"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class IKARUS_Bus(unittype.VehicleType):
        id = "IKARUS Bus"
        name = "Bus IKARUS-280"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class KAMAZ_Truck(unittype.VehicleType):
        id = "KAMAZ Truck"
        name = "Truck KAMAZ 43101"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LAZ_Bus(unittype.VehicleType):
        id = "LAZ Bus"
        name = "Bus LAZ-695"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LiAZ_Bus(unittype.VehicleType):
        id = "LiAZ Bus"
        name = "Bus LiAZ-677"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Hummer(unittype.VehicleType):
        id = "Hummer"
        name = "LUV HMMWV Jeep"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class M_818(unittype.VehicleType):
        id = "M 818"
        name = "Truck M939 Heavy"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class MAZ_6303(unittype.VehicleType):
        id = "MAZ-6303"
        name = "Truck MAZ-6303"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Predator_GCS(unittype.VehicleType):
        id = "Predator GCS"
        name = "MCC Predator UAV CP & GCS"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Predator_TrojanSpirit(unittype.VehicleType):
        id = "Predator TrojanSpirit"
        name = "MCC-COMM Predator UAV CL"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Suidae(unittype.VehicleType):
        id = "Suidae"
        name = "Suidae"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tigr_233036(unittype.VehicleType):
        id = "Tigr_233036"
        name = "LUV Tigr"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Trolley_bus(unittype.VehicleType):
        id = "Trolley bus"
        name = "ZIU-9 Trolley"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class UAZ_469(unittype.VehicleType):
        id = "UAZ-469"
        name = "LUV UAZ-469 Jeep"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Ural_ATsP_6(unittype.VehicleType):
        id = "Ural ATsP-6"
        name = "Firefighter Ural ATsP-6"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Ural_4320_31(unittype.VehicleType):
        id = "Ural-4320-31"
        name = "Truck Ural-4320-31 Arm'd"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Ural_4320T(unittype.VehicleType):
        id = "Ural-4320T"
        name = "Truck Ural-4320T"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Ural_375_PBU(unittype.VehicleType):
        id = "Ural-375 PBU"
        name = "Truck Ural-4320 MCC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Ural_375(unittype.VehicleType):
        id = "Ural-375"
        name = "Truck Ural-4320"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class VAZ_Car(unittype.VehicleType):
        id = "VAZ Car"
        name = "Car VAZ-2109"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ZiL_131_APA_80(unittype.VehicleType):
        id = "ZiL-131 APA-80"
        name = "GPU APA-80 on ZIL-131"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SKP_11(unittype.VehicleType):
        id = "SKP-11"
        name = "Truck SKP-11 Mobile ATC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ZIL_131_KUNG(unittype.VehicleType):
        id = "ZIL-131 KUNG"
        name = "Truck ZIL-131 (C2)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ZIL_4331(unittype.VehicleType):
        id = "ZIL-4331"
        name = "Truck ZIL-4331"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class KrAZ6322(unittype.VehicleType):
        id = "KrAZ6322"
        name = "Truck KrAZ-6322 6x6"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class TugHarlan_drivable(unittype.VehicleType):
        id = "TugHarlan_drivable"
        name = "M92 Tug Harlan drivable"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class B600_drivable(unittype.VehicleType):
        id = "B600_drivable"
        name = "M92 B600 drivable"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class MJ_1_drivable(unittype.VehicleType):
        id = "MJ-1_drivable"
        name = "M92 MJ-1 drivable"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class P20_drivable(unittype.VehicleType):
        id = "P20_drivable"
        name = "M92 P20 drivable"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class R11_volvo_drivable(unittype.VehicleType):
        id = "r11_volvo_drivable"
        name = "M92 R11 Volvo drivable"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tacr2a(unittype.VehicleType):
        id = "tacr2a"
        name = "Firefighter RAF Rescue"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LARC_V(unittype.VehicleType):
        id = "LARC-V"
        name = "Truck LARC-V"
        detection_range = 500
        threat_range = 0
        air_weapon_dist = 0

    class ATZ_5(unittype.VehicleType):
        id = "ATZ-5"
        name = "Refueler ATZ-5"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class AA8(unittype.VehicleType):
        id = "AA8"
        name = "Firefighter Vehicle AA-7.2/60"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class TZ_22_KrAZ(unittype.VehicleType):
        id = "TZ-22_KrAZ"
        name = "Refueler TZ-22 Tractor (KrAZ-258B1)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ATZ_60_Maz(unittype.VehicleType):
        id = "ATZ-60_Maz"
        name = "Refueler ATZ-60 Tractor (MAZ-7410)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ZIL_135(unittype.VehicleType):
        id = "ZIL-135"
        name = "Truck ZIL-135"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class S_75_ZIL(unittype.VehicleType):
        id = "S_75_ZIL"
        name = "S-75 Tractor (ZIL-131)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Bedford_MWD(unittype.VehicleType):
        id = "Bedford_MWD"
        name = "Truck Bedford"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Land_Rover_101_FC(unittype.VehicleType):
        id = "Land_Rover_101_FC"
        name = "Truck Land Rover 101 FC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Land_Rover_109_S3(unittype.VehicleType):
        id = "Land_Rover_109_S3"
        name = "LUV Land Rover 109"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Blitz_36_6700A(unittype.VehicleType):
        id = "Blitz_36-6700A"
        name = "Truck Opel Blitz"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Kubelwagen_82(unittype.VehicleType):
        id = "Kubelwagen_82"
        name = "LUV Kubelwagen Jeep"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Sd_Kfz_2(unittype.VehicleType):
        id = "Sd_Kfz_2"
        name = "LUV Kettenrad"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Sd_Kfz_7(unittype.VehicleType):
        id = "Sd_Kfz_7"
        name = "Tractor Sd.Kfz.7 Art'y Tractor"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Horch_901_typ_40_kfz_21(unittype.VehicleType):
        id = "Horch_901_typ_40_kfz_21"
        name = "LUV Horch 901 Staff Car"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class CCKW_353(unittype.VehicleType):
        id = "CCKW_353"
        name = "Truck GMC \"Jimmy\" 6x6"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Willys_MB(unittype.VehicleType):
        id = "Willys_MB"
        name = "Car Willys Jeep"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class M30_CC(unittype.VehicleType):
        id = "M30_CC"
        name = "Ammo M30 Cargo Carrier"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0


class Armor:

    class AAV7(unittype.VehicleType):
        id = "AAV7"
        name = "APC AAV-7 Amphibious"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200

    class BMD_1(unittype.VehicleType):
        id = "BMD-1"
        name = "IFV BMD-1"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 1000

    class BMP_1(unittype.VehicleType):
        id = "BMP-1"
        name = "IFV BMP-1"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 1000

    class BMP_2(unittype.VehicleType):
        id = "BMP-2"
        name = "IFV BMP-2"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 2000

    class BMP_3(unittype.VehicleType):
        id = "BMP-3"
        name = "IFV BMP-3"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 1000

    class BRDM_2(unittype.VehicleType):
        id = "BRDM-2"
        name = "Scout BRDM-2"
        detection_range = 0
        threat_range = 1600
        air_weapon_dist = 1600

    class BTR_D(unittype.VehicleType):
        id = "BTR_D"
        name = "APC BTR-RD"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 1000

    class Cobra(unittype.VehicleType):
        id = "Cobra"
        name = "Scout Cobra"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200

    class LAV_25(unittype.VehicleType):
        id = "LAV-25"
        name = "IFV LAV-25"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class M1043_HMMWV_Armament(unittype.VehicleType):
        id = "M1043 HMMWV Armament"
        name = "Scout HMMWV"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class M1045_HMMWV_TOW(unittype.VehicleType):
        id = "M1045 HMMWV TOW"
        name = "ATGM HMMWV"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 0
        eplrs = True

    class M1126_Stryker_ICV(unittype.VehicleType):
        id = "M1126 Stryker ICV"
        name = "IFV M1126 Stryker ICV"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class M_113(unittype.VehicleType):
        id = "M-113"
        name = "APC M113"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class M1134_Stryker_ATGM(unittype.VehicleType):
        id = "M1134 Stryker ATGM"
        name = "ATGM Stryker"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 1000
        eplrs = True

    class M_2_Bradley(unittype.VehicleType):
        id = "M-2 Bradley"
        name = "IFV M2A2 Bradley"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 2500
        eplrs = True

    class MCV_80(unittype.VehicleType):
        id = "MCV-80"
        name = "IFV Warrior "
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class MTLB(unittype.VehicleType):
        id = "MTLB"
        name = "APC MTLB"
        detection_range = 0
        threat_range = 1000
        air_weapon_dist = 1000

    class Marder(unittype.VehicleType):
        id = "Marder"
        name = "IFV Marder"
        detection_range = 0
        threat_range = 1500
        air_weapon_dist = 1500

    class TPZ(unittype.VehicleType):
        id = "TPZ"
        name = "APC TPz Fuchs "
        detection_range = 0
        threat_range = 1000
        air_weapon_dist = 1000

    class Challenger2(unittype.VehicleType):
        id = "Challenger2"
        name = "MBT Challenger II"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class Leclerc(unittype.VehicleType):
        id = "Leclerc"
        name = "MBT Leclerc"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class M_60(unittype.VehicleType):
        id = "M-60"
        name = "MBT M60A3 Patton"
        detection_range = 0
        threat_range = 8000
        air_weapon_dist = 1500

    class M1128_Stryker_MGS(unittype.VehicleType):
        id = "M1128 Stryker MGS"
        name = "SPG Stryker MGS"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 1200
        eplrs = True

    class T_55(unittype.VehicleType):
        id = "T-55"
        name = "MBT T-55"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 1200

    class T_72B(unittype.VehicleType):
        id = "T-72B"
        name = "MBT T-72B"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 3500

    class T_80UD(unittype.VehicleType):
        id = "T-80UD"
        name = "MBT T-80U"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 3500

    class T_90(unittype.VehicleType):
        id = "T-90"
        name = "MBT T-90"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 3500

    class Leopard1A3(unittype.VehicleType):
        id = "Leopard1A3"
        name = "MBT Leopard 1A3"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 1500

    class Merkava_Mk4(unittype.VehicleType):
        id = "Merkava_Mk4"
        name = "MBT Merkava IV"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1200

    class M1A2C_SEP_V3(unittype.VehicleType):
        id = "M1A2C_SEP_V3"
        name = "MBT M1A2C SEP v3 Abrams"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1200
        eplrs = True

    class M_1_Abrams(unittype.VehicleType):
        id = "M-1 Abrams"
        name = "MBT M1A2 Abrams"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1200
        eplrs = True

    class MaxxPro_MRAP(unittype.VehicleType):
        id = "MaxxPro_MRAP"
        name = "APC MRAP MaxxPro"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class HL_DSHK(unittype.VehicleType):
        id = "HL_DSHK"
        name = "Scout HL with DSHK 12.7mm"
        detection_range = 5000
        threat_range = 1200
        air_weapon_dist = 1200

    class HL_KORD(unittype.VehicleType):
        id = "HL_KORD"
        name = "Scout HL with KORD 12.7mm"
        detection_range = 5000
        threat_range = 1200
        air_weapon_dist = 1200

    class Tt_DSHK(unittype.VehicleType):
        id = "tt_DSHK"
        name = "Scout LC with DSHK 12.7mm"
        detection_range = 5000
        threat_range = 1200
        air_weapon_dist = 1200

    class Tt_KORD(unittype.VehicleType):
        id = "tt_KORD"
        name = "Scout LC with KORD 12.7mm"
        detection_range = 5000
        threat_range = 1200
        air_weapon_dist = 1200

    class M4_Sherman(unittype.VehicleType):
        id = "M4_Sherman"
        name = "Tk M4 Sherman"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class M2A1_halftrack(unittype.VehicleType):
        id = "M2A1_halftrack"
        name = "APC M2A1 Halftrack"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0

    class BTR_80(unittype.VehicleType):
        id = "BTR-80"
        name = "APC BTR-80"
        detection_range = 0
        threat_range = 1600
        air_weapon_dist = 1600

    class T_72B3(unittype.VehicleType):
        id = "T-72B3"
        name = "MBT T-72B3"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 3500

    class PT_76(unittype.VehicleType):
        id = "PT_76"
        name = "LT PT-76"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 1000

    class BTR_82A(unittype.VehicleType):
        id = "BTR-82A"
        name = "IFV BTR-82A"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 2000

    class Chieftain_mk3(unittype.VehicleType):
        id = "Chieftain_mk3"
        name = "MBT Chieftain Mk.3"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class Pz_IV_H(unittype.VehicleType):
        id = "Pz_IV_H"
        name = "Tk PzIV H"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Leopard_2A5(unittype.VehicleType):
        id = "Leopard-2A5"
        name = "MBT Leopard-2A5"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class Leopard_2(unittype.VehicleType):
        id = "Leopard-2"
        name = "MBT Leopard-2A6M"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class Leopard_2A4(unittype.VehicleType):
        id = "leopard-2A4"
        name = "MBT Leopard-2A4"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class Leopard_2A4_trs(unittype.VehicleType):
        id = "leopard-2A4_trs"
        name = "MBT Leopard-2A4 Trs"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class Sd_Kfz_251(unittype.VehicleType):
        id = "Sd_Kfz_251"
        name = "APC Sd.Kfz.251 Halftrack"
        detection_range = 0
        threat_range = 1100
        air_weapon_dist = 0

    class VAB_Mephisto(unittype.VehicleType):
        id = "VAB_Mephisto"
        name = "ATGM VAB Mephisto"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 3800
        eplrs = True

    class ZTZ96B(unittype.VehicleType):
        id = "ZTZ96B"
        name = "ZTZ-96B"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 3500
        eplrs = True

    class ZBD04A(unittype.VehicleType):
        id = "ZBD04A"
        name = "ZBD-04A"
        detection_range = 0
        threat_range = 4800
        air_weapon_dist = 0
        eplrs = True

    class TYPE_59(unittype.VehicleType):
        id = "TYPE-59"
        name = "MT Type 59"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 1200

    class Tiger_I(unittype.VehicleType):
        id = "Tiger_I"
        name = "Tk Tiger 1"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Tiger_II_H(unittype.VehicleType):
        id = "Tiger_II_H"
        name = "Tk Tiger II"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class Pz_V_Panther_G(unittype.VehicleType):
        id = "Pz_V_Panther_G"
        name = "Tk Panther G (Pz V)"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Jagdpanther_G1(unittype.VehicleType):
        id = "Jagdpanther_G1"
        name = "SPG Jagdpanther TD"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 0

    class JagdPz_IV(unittype.VehicleType):
        id = "JagdPz_IV"
        name = "SPG Jagdpanzer IV TD"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Stug_IV(unittype.VehicleType):
        id = "Stug_IV"
        name = "SPG StuG IV AG"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class SturmPzIV(unittype.VehicleType):
        id = "SturmPzIV"
        name = "SPG Brummbaer AG"
        detection_range = 0
        threat_range = 4500
        air_weapon_dist = 2500

    class Sd_Kfz_234_2_Puma(unittype.VehicleType):
        id = "Sd_Kfz_234_2_Puma"
        name = "Scout Puma AC"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class Stug_III(unittype.VehicleType):
        id = "Stug_III"
        name = "SPG StuG III G AG"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Elefant_SdKfz_184(unittype.VehicleType):
        id = "Elefant_SdKfz_184"
        name = "SPG Elefant TD"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class Cromwell_IV(unittype.VehicleType):
        id = "Cromwell_IV"
        name = "Tk Cromwell IV"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class M4A4_Sherman_FF(unittype.VehicleType):
        id = "M4A4_Sherman_FF"
        name = "Tk M4A4 Sherman Firefly"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Centaur_IV(unittype.VehicleType):
        id = "Centaur_IV"
        name = "Tk Centaur IV CS"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class Churchill_VII(unittype.VehicleType):
        id = "Churchill_VII"
        name = "Tk Churchill VII"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Daimler_AC(unittype.VehicleType):
        id = "Daimler_AC"
        name = "Car Daimler Armored"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class Tetrarch(unittype.VehicleType):
        id = "Tetrarch"
        name = "Tk Tetrach"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class M10_GMC(unittype.VehicleType):
        id = "M10_GMC"
        name = "SPG M10 GMC TD"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class M8_Greyhound(unittype.VehicleType):
        id = "M8_Greyhound"
        name = "Scout M8 Greyhound AC"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class M4_Tractor(unittype.VehicleType):
        id = "M4_Tractor"
        name = "Tractor M4 High Speed"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0


class MissilesSS:

    class Scud_B(unittype.VehicleType):
        id = "Scud_B"
        name = "SSM SS-1C Scud-B"
        detection_range = 0
        threat_range = 285000
        air_weapon_dist = 285000

    class Hy_launcher(unittype.VehicleType):
        id = "hy_launcher"
        name = "AShM SS-N-2 Silkworm"
        detection_range = 100000
        threat_range = 100000
        air_weapon_dist = 100000

    class Silkworm_SR(unittype.VehicleType):
        id = "Silkworm_SR"
        name = "AShM Silkworm SR"
        detection_range = 200000
        threat_range = 0
        air_weapon_dist = 0

    class V1_launcher(unittype.VehicleType):
        id = "v1_launcher"
        name = "V-1 Launch Ramp"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0


class Locomotive:

    class Electric_locomotive(unittype.VehicleType):
        id = "Electric locomotive"
        name = "Loco VL80 Electric"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Locomotive(unittype.VehicleType):
        id = "Locomotive"
        name = "Loco CHME3T"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ES44AH(unittype.VehicleType):
        id = "ES44AH"
        name = "Loco ES44AH"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class DRG_Class_86(unittype.VehicleType):
        id = "DRG_Class_86"
        name = "Loco DRG Class 86"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0


class Carriage:

    class Coach_cargo(unittype.VehicleType):
        id = "Coach cargo"
        name = "Freight Van"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_cargo_open(unittype.VehicleType):
        id = "Coach cargo open"
        name = "Open Wagon"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_a_tank_blue(unittype.VehicleType):
        id = "Coach a tank blue"
        name = "Tank Car blue"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_a_tank_yellow(unittype.VehicleType):
        id = "Coach a tank yellow"
        name = "Tank Car yellow"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_a_passenger(unittype.VehicleType):
        id = "Coach a passenger"
        name = "Passenger Car"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_a_platform(unittype.VehicleType):
        id = "Coach a platform"
        name = "Coach Platform"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Boxcartrinity(unittype.VehicleType):
        id = "Boxcartrinity"
        name = "Flatcar"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tankcartrinity(unittype.VehicleType):
        id = "Tankcartrinity"
        name = "Tank Cartrinity"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Wellcarnsc(unittype.VehicleType):
        id = "Wellcarnsc"
        name = "Well Car"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class DR_50Ton_Flat_Wagon(unittype.VehicleType):
        id = "DR_50Ton_Flat_Wagon"
        name = "DR 50-ton flat wagon"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class German_covered_wagon_G10(unittype.VehicleType):
        id = "German_covered_wagon_G10"
        name = "Wagon G10 (Germany)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class German_tank_wagon(unittype.VehicleType):
        id = "German_tank_wagon"
        name = "Tank Car (Germany)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

vehicle_map = {
    "2B11 mortar": Artillery.X_2B11_mortar,
    "SAU Gvozdika": Artillery.SAU_Gvozdika,
    "SAU Msta": Artillery.SAU_Msta,
    "SAU Akatsia": Artillery.SAU_Akatsia,
    "SAU 2-C9": Artillery.SAU_2_C9,
    "M-109": Artillery.M_109,
    "SpGH_Dana": Artillery.SpGH_Dana,
    "AAV7": Armor.AAV7,
    "BMD-1": Armor.BMD_1,
    "BMP-1": Armor.BMP_1,
    "BMP-2": Armor.BMP_2,
    "BMP-3": Armor.BMP_3,
    "BRDM-2": Armor.BRDM_2,
    "BTR_D": Armor.BTR_D,
    "Cobra": Armor.Cobra,
    "LAV-25": Armor.LAV_25,
    "M1043 HMMWV Armament": Armor.M1043_HMMWV_Armament,
    "M1045 HMMWV TOW": Armor.M1045_HMMWV_TOW,
    "M1126 Stryker ICV": Armor.M1126_Stryker_ICV,
    "M-113": Armor.M_113,
    "M1134 Stryker ATGM": Armor.M1134_Stryker_ATGM,
    "M-2 Bradley": Armor.M_2_Bradley,
    "MCV-80": Armor.MCV_80,
    "MTLB": Armor.MTLB,
    "Marder": Armor.Marder,
    "TPZ": Armor.TPZ,
    "Grad_FDDM": Artillery.Grad_FDDM,
    "Bunker": Fortification.Bunker,
    "Paratrooper RPG-16": Infantry.Paratrooper_RPG_16,
    "Paratrooper AKS-74": Infantry.Paratrooper_AKS_74,
    "Infantry AK Ins": Infantry.Infantry_AK_Ins,
    "Sandbox": Fortification.Sandbox,
    "Soldier AK": Infantry.Soldier_AK,
    "Infantry AK": Infantry.Infantry_AK,
    "Soldier M249": Infantry.Soldier_M249,
    "Soldier M4": Infantry.Soldier_M4,
    "Soldier M4 GRG": Infantry.Soldier_M4_GRG,
    "Soldier RPG": Infantry.Soldier_RPG,
    "MLRS FDDM": Artillery.MLRS_FDDM,
    "Infantry AK ver2": Infantry.Infantry_AK_ver2,
    "Infantry AK ver3": Infantry.Infantry_AK_ver3,
    "Grad-URAL": Artillery.Grad_URAL,
    "Uragan_BM-27": Artillery.Uragan_BM_27,
    "Smerch": Artillery.Smerch,
    "Smerch_HE": Artillery.Smerch_HE,
    "MLRS": Artillery.MLRS,
    "2S6 Tunguska": AirDefence.X_2S6_Tunguska,
    "Kub 2P25 ln": AirDefence.Kub_2P25_ln,
    "5p73 s-125 ln": AirDefence.X_5p73_s_125_ln,
    "SA-11 Buk LN 9A310M1": AirDefence.SA_11_Buk_LN_9A310M1,
    "Osa 9A33 ln": AirDefence.Osa_9A33_ln,
    "Tor 9A331": AirDefence.Tor_9A331,
    "Strela-10M3": AirDefence.Strela_10M3,
    "Strela-1 9P31": AirDefence.Strela_1_9P31,
    "SA-11 Buk CC 9S470M1": AirDefence.SA_11_Buk_CC_9S470M1,
    "Patriot AMG": AirDefence.Patriot_AMG,
    "Patriot ECS": AirDefence.Patriot_ECS,
    "Gepard": AirDefence.Gepard,
    "Hawk pcp": AirDefence.Hawk_pcp,
    "Vulcan": AirDefence.Vulcan,
    "Hawk ln": AirDefence.Hawk_ln,
    "M48 Chaparral": AirDefence.M48_Chaparral,
    "M6 Linebacker": AirDefence.M6_Linebacker,
    "Patriot ln": AirDefence.Patriot_ln,
    "M1097 Avenger": AirDefence.M1097_Avenger,
    "Patriot EPP": AirDefence.Patriot_EPP,
    "Patriot cp": AirDefence.Patriot_cp,
    "Roland ADS": AirDefence.Roland_ADS,
    "Soldier stinger": AirDefence.Soldier_stinger,
    "Stinger comm dsr": AirDefence.Stinger_comm_dsr,
    "Stinger comm": AirDefence.Stinger_comm,
    "ZSU-23-4 Shilka": AirDefence.ZSU_23_4_Shilka,
    "ZU-23 Emplacement Closed": AirDefence.ZU_23_Emplacement_Closed,
    "ZU-23 Emplacement": AirDefence.ZU_23_Emplacement,
    "Ural-375 ZU-23": AirDefence.Ural_375_ZU_23,
    "ZU-23 Closed Insurgent": AirDefence.ZU_23_Closed_Insurgent,
    "Ural-375 ZU-23 Insurgent": AirDefence.Ural_375_ZU_23_Insurgent,
    "ZU-23 Insurgent": AirDefence.ZU_23_Insurgent,
    "SA-18 Igla manpad": AirDefence.SA_18_Igla_manpad,
    "SA-18 Igla comm": AirDefence.SA_18_Igla_comm,
    "SA-18 Igla-S manpad": AirDefence.SA_18_Igla_S_manpad,
    "SA-18 Igla-S comm": AirDefence.SA_18_Igla_S_comm,
    "Igla manpad INS": AirDefence.Igla_manpad_INS,
    "1L13 EWR": AirDefence.X_1L13_EWR,
    "Kub 1S91 str": AirDefence.Kub_1S91_str,
    "55G6 EWR": AirDefence.X_55G6_EWR,
    "SA-11 Buk SR 9S18M1": AirDefence.SA_11_Buk_SR_9S18M1,
    "Dog Ear radar": AirDefence.Dog_Ear_radar,
    "Hawk tr": AirDefence.Hawk_tr,
    "Hawk sr": AirDefence.Hawk_sr,
    "Patriot str": AirDefence.Patriot_str,
    "Hawk cwar": AirDefence.Hawk_cwar,
    "p-19 s-125 sr": AirDefence.P_19_s_125_sr,
    "Roland Radar": AirDefence.Roland_Radar,
    "snr s-125 tr": AirDefence.Snr_s_125_tr,
    "house1arm": Fortification.House1arm,
    "house2arm": Fortification.House2arm,
    "outpost_road": Fortification.Outpost_road,
    "outpost_road_l": Fortification.Outpost_road_l,
    "outpost_road_r": Fortification.Outpost_road_r,
    "outpost": Fortification.Outpost,
    "houseA_arm": Fortification.HouseA_arm,
    "TACAN_beacon": Fortification.TACAN_beacon,
    "Challenger2": Armor.Challenger2,
    "Leclerc": Armor.Leclerc,
    "M-60": Armor.M_60,
    "M1128 Stryker MGS": Armor.M1128_Stryker_MGS,
    "T-55": Armor.T_55,
    "T-72B": Armor.T_72B,
    "T-80UD": Armor.T_80UD,
    "T-90": Armor.T_90,
    "Leopard1A3": Armor.Leopard1A3,
    "Merkava_Mk4": Armor.Merkava_Mk4,
    "Ural-4320 APA-5D": Unarmed.Ural_4320_APA_5D,
    "ATMZ-5": Unarmed.ATMZ_5,
    "ATZ-10": Unarmed.ATZ_10,
    "GAZ-3307": Unarmed.GAZ_3307,
    "GAZ-3308": Unarmed.GAZ_3308,
    "GAZ-66": Unarmed.GAZ_66,
    "M978 HEMTT Tanker": Unarmed.M978_HEMTT_Tanker,
    "HEMTT TFFT": Unarmed.HEMTT_TFFT,
    "IKARUS Bus": Unarmed.IKARUS_Bus,
    "KAMAZ Truck": Unarmed.KAMAZ_Truck,
    "LAZ Bus": Unarmed.LAZ_Bus,
    "LiAZ Bus": Unarmed.LiAZ_Bus,
    "Hummer": Unarmed.Hummer,
    "M 818": Unarmed.M_818,
    "MAZ-6303": Unarmed.MAZ_6303,
    "Predator GCS": Unarmed.Predator_GCS,
    "Predator TrojanSpirit": Unarmed.Predator_TrojanSpirit,
    "Suidae": Unarmed.Suidae,
    "Tigr_233036": Unarmed.Tigr_233036,
    "Trolley bus": Unarmed.Trolley_bus,
    "UAZ-469": Unarmed.UAZ_469,
    "Ural ATsP-6": Unarmed.Ural_ATsP_6,
    "Ural-4320-31": Unarmed.Ural_4320_31,
    "Ural-4320T": Unarmed.Ural_4320T,
    "Ural-375 PBU": Unarmed.Ural_375_PBU,
    "Ural-375": Unarmed.Ural_375,
    "VAZ Car": Unarmed.VAZ_Car,
    "ZiL-131 APA-80": Unarmed.ZiL_131_APA_80,
    "SKP-11": Unarmed.SKP_11,
    "ZIL-131 KUNG": Unarmed.ZIL_131_KUNG,
    "ZIL-4331": Unarmed.ZIL_4331,
    "KrAZ6322": Unarmed.KrAZ6322,
    "JTAC": Infantry.JTAC,
    "HEMTT_C-RAM_Phalanx": AirDefence.HEMTT_C_RAM_Phalanx,
    "S-300PS 5P85C ln": AirDefence.S_300PS_5P85C_ln,
    "S-300PS 5P85D ln": AirDefence.S_300PS_5P85D_ln,
    "S-300PS 54K6 cp": AirDefence.S_300PS_54K6_cp,
    "S-300PS 40B6M tr": AirDefence.S_300PS_40B6M_tr,
    "S-300PS 64H6E sr": AirDefence.S_300PS_64H6E_sr,
    "S-300PS 40B6MD sr_19J6": AirDefence.S_300PS_40B6MD_sr_19J6,
    "S-300PS 5H63C 30H6_tr": AirDefence.S_300PS_5H63C_30H6_tr,
    "S-300PS 40B6MD sr": AirDefence.S_300PS_40B6MD_sr,
    "M1A2C_SEP_V3": Armor.M1A2C_SEP_V3,
    "M-1 Abrams": Armor.M_1_Abrams,
    "MaxxPro_MRAP": Armor.MaxxPro_MRAP,
    "TugHarlan_drivable": Unarmed.TugHarlan_drivable,
    "B600_drivable": Unarmed.B600_drivable,
    "MJ-1_drivable": Unarmed.MJ_1_drivable,
    "P20_drivable": Unarmed.P20_drivable,
    "r11_volvo_drivable": Unarmed.R11_volvo_drivable,
    "Electric locomotive": Locomotive.Electric_locomotive,
    "Locomotive": Locomotive.Locomotive,
    "Coach cargo": Carriage.Coach_cargo,
    "Coach cargo open": Carriage.Coach_cargo_open,
    "Coach a tank blue": Carriage.Coach_a_tank_blue,
    "Coach a tank yellow": Carriage.Coach_a_tank_yellow,
    "Coach a passenger": Carriage.Coach_a_passenger,
    "Coach a platform": Carriage.Coach_a_platform,
    "L118_Unit": Artillery.L118_Unit,
    "tacr2a": Unarmed.Tacr2a,
    "LARC-V": Unarmed.LARC_V,
    "KS-19": AirDefence.KS_19,
    "SON_9": AirDefence.SON_9,
    "Scud_B": MissilesSS.Scud_B,
    "HL_DSHK": Armor.HL_DSHK,
    "HL_KORD": Armor.HL_KORD,
    "tt_DSHK": Armor.Tt_DSHK,
    "tt_KORD": Armor.Tt_KORD,
    "HL_ZU-23": AirDefence.HL_ZU_23,
    "tt_ZU-23": AirDefence.Tt_ZU_23,
    "HL_B8M1": Artillery.HL_B8M1,
    "tt_B8M1": Artillery.Tt_B8M1,
    "NASAMS_Radar_MPQ64F1": AirDefence.NASAMS_Radar_MPQ64F1,
    "NASAMS_Command_Post": AirDefence.NASAMS_Command_Post,
    "NASAMS_LN_B": AirDefence.NASAMS_LN_B,
    "NASAMS_LN_C": AirDefence.NASAMS_LN_C,
    "M4_Sherman": Armor.M4_Sherman,
    "M2A1_halftrack": Armor.M2A1_halftrack,
    "FPS-117 Dome": AirDefence.FPS_117_Dome,
    "FPS-117 ECS": AirDefence.FPS_117_ECS,
    "FPS-117": AirDefence.FPS_117,
    "BTR-80": Armor.BTR_80,
    "RD_75": AirDefence.RD_75,
    "S_75M_Volhov": AirDefence.S_75M_Volhov,
    "SNR_75V": AirDefence.SNR_75V,
    "RLS_19J6": AirDefence.RLS_19J6,
    "RPC_5N62V": AirDefence.RPC_5N62V,
    "S-200_Launcher": AirDefence.S_200_Launcher,
    "ZSU_57_2": AirDefence.ZSU_57_2,
    "S-60_Type59_Artillery": AirDefence.S_60_Type59_Artillery,
    "generator_5i57": AirDefence.Generator_5i57,
    "T-72B3": Armor.T_72B3,
    "PT_76": Armor.PT_76,
    "BTR-82A": Armor.BTR_82A,
    "ATZ-5": Unarmed.ATZ_5,
    "AA8": Unarmed.AA8,
    "TZ-22_KrAZ": Unarmed.TZ_22_KrAZ,
    "ATZ-60_Maz": Unarmed.ATZ_60_Maz,
    "ZIL-135": Unarmed.ZIL_135,
    "S_75_ZIL": Unarmed.S_75_ZIL,
    "rapier_fsa_launcher": AirDefence.Rapier_fsa_launcher,
    "rapier_fsa_optical_tracker_unit": AirDefence.Rapier_fsa_optical_tracker_unit,
    "rapier_fsa_blindfire_radar": AirDefence.Rapier_fsa_blindfire_radar,
    "bofors40": AirDefence.Bofors40,
    "Chieftain_mk3": Armor.Chieftain_mk3,
    "Bedford_MWD": Unarmed.Bedford_MWD,
    "Land_Rover_101_FC": Unarmed.Land_Rover_101_FC,
    "Land_Rover_109_S3": Unarmed.Land_Rover_109_S3,
    "hy_launcher": MissilesSS.Hy_launcher,
    "Silkworm_SR": MissilesSS.Silkworm_SR,
    "ES44AH": Locomotive.ES44AH,
    "Boxcartrinity": Carriage.Boxcartrinity,
    "Tankcartrinity": Carriage.Tankcartrinity,
    "Wellcarnsc": Carriage.Wellcarnsc,
    "flak18": AirDefence.Flak18,
    "Pz_IV_H": Armor.Pz_IV_H,
    "Leopard-2A5": Armor.Leopard_2A5,
    "Leopard-2": Armor.Leopard_2,
    "leopard-2A4": Armor.Leopard_2A4,
    "leopard-2A4_trs": Armor.Leopard_2A4_trs,
    "Sd_Kfz_251": Armor.Sd_Kfz_251,
    "Blitz_36-6700A": Unarmed.Blitz_36_6700A,
    "T155_Firtina": Artillery.T155_Firtina,
    "VAB_Mephisto": Armor.VAB_Mephisto,
    "ZTZ96B": Armor.ZTZ96B,
    "ZBD04A": Armor.ZBD04A,
    "HQ-7_LN_SP": AirDefence.HQ_7_LN_SP,
    "HQ-7_LN_P": AirDefence.HQ_7_LN_P,
    "HQ-7_STR_SP": AirDefence.HQ_7_STR_SP,
    "PLZ05": Artillery.PLZ05,
    "TYPE-59": Armor.TYPE_59,
    "Kubelwagen_82": Unarmed.Kubelwagen_82,
    "Sd_Kfz_2": Unarmed.Sd_Kfz_2,
    "Sd_Kfz_7": Unarmed.Sd_Kfz_7,
    "Horch_901_typ_40_kfz_21": Unarmed.Horch_901_typ_40_kfz_21,
    "Tiger_I": Armor.Tiger_I,
    "Tiger_II_H": Armor.Tiger_II_H,
    "Pz_V_Panther_G": Armor.Pz_V_Panther_G,
    "Jagdpanther_G1": Armor.Jagdpanther_G1,
    "JagdPz_IV": Armor.JagdPz_IV,
    "Stug_IV": Armor.Stug_IV,
    "SturmPzIV": Armor.SturmPzIV,
    "Wespe124": Artillery.Wespe124,
    "Sd_Kfz_234_2_Puma": Armor.Sd_Kfz_234_2_Puma,
    "flak30": AirDefence.Flak30,
    "flak36": AirDefence.Flak36,
    "flak37": AirDefence.Flak37,
    "flak38": AirDefence.Flak38,
    "KDO_Mod40": AirDefence.KDO_Mod40,
    "Flakscheinwerfer_37": AirDefence.Flakscheinwerfer_37,
    "Maschinensatz_33": AirDefence.Maschinensatz_33,
    "soldier_mauser98": Infantry.Soldier_mauser98,
    "SK_C_28_naval_gun": Fortification.SK_C_28_naval_gun,
    "fire_control": Fortification.Fire_control,
    "Stug_III": Armor.Stug_III,
    "Elefant_SdKfz_184": Armor.Elefant_SdKfz_184,
    "flak41": AirDefence.Flak41,
    "v1_launcher": MissilesSS.V1_launcher,
    "FuMG-401": AirDefence.FuMG_401,
    "FuSe-65": AirDefence.FuSe_65,
    "Pak40": Artillery.Pak40,
    "LeFH_18-40-105": Artillery.LeFH_18_40_105,
    "Cromwell_IV": Armor.Cromwell_IV,
    "M4A4_Sherman_FF": Armor.M4A4_Sherman_FF,
    "soldier_wwii_br_01": Infantry.Soldier_wwii_br_01,
    "Centaur_IV": Armor.Centaur_IV,
    "Churchill_VII": Armor.Churchill_VII,
    "Daimler_AC": Armor.Daimler_AC,
    "Tetrarch": Armor.Tetrarch,
    "QF_37_AA": AirDefence.QF_37_AA,
    "Allies_Director": AirDefence.Allies_Director,
    "CCKW_353": Unarmed.CCKW_353,
    "Willys_MB": Unarmed.Willys_MB,
    "M12_GMC": Artillery.M12_GMC,
    "M30_CC": Unarmed.M30_CC,
    "soldier_wwii_us": Infantry.Soldier_wwii_us,
    "M10_GMC": Armor.M10_GMC,
    "M8_Greyhound": Armor.M8_Greyhound,
    "M2A1-105": Artillery.M2A1_105,
    "M4_Tractor": Armor.M4_Tractor,
    "M45_Quadmount": AirDefence.M45_Quadmount,
    "M1_37mm": AirDefence.M1_37mm,
    "DR_50Ton_Flat_Wagon": Carriage.DR_50Ton_Flat_Wagon,
    "DRG_Class_86": Locomotive.DRG_Class_86,
    "German_covered_wagon_G10": Carriage.German_covered_wagon_G10,
    "German_tank_wagon": Carriage.German_tank_wagon,
}
