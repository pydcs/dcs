# This file is generated from pydcs_export.lua

import dcs.unittype as unittype


class Artillery:

    class Mortar_2B11_120mm(unittype.VehicleType):
        id = "2B11 mortar"
        name = "Mortar 2B11 120mm"
        detection_range = 0
        threat_range = 7000
        air_weapon_dist = 7000

    class SPH_2S1_Gvozdika_122mm(unittype.VehicleType):
        id = "SAU Gvozdika"
        name = "SPH 2S1 Gvozdika 122mm"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class SPH_2S19_Msta_152mm(unittype.VehicleType):
        id = "SAU Msta"
        name = "SPH 2S19 Msta 152mm"
        detection_range = 0
        threat_range = 23500
        air_weapon_dist = 23500

    class SPH_2S3_Akatsia_152mm(unittype.VehicleType):
        id = "SAU Akatsia"
        name = "SPH 2S3 Akatsia 152mm"
        detection_range = 0
        threat_range = 17000
        air_weapon_dist = 17000

    class SPH_2S9_Nona_120mm_M(unittype.VehicleType):
        id = "SAU 2-C9"
        name = "SPH 2S9 Nona 120mm M"
        detection_range = 0
        threat_range = 7000
        air_weapon_dist = 7000

    class SPH_M109_Paladin_155mm(unittype.VehicleType):
        id = "M-109"
        name = "SPH M109 Paladin 155mm"
        detection_range = 0
        threat_range = 22000
        air_weapon_dist = 22000
        eplrs = True

    class SPH_Dana_vz77_152mm(unittype.VehicleType):
        id = "SpGH_Dana"
        name = "SPH Dana vz77 152mm"
        detection_range = 0
        threat_range = 18700
        air_weapon_dist = 18700

    class Grad_MRL_FDDM__FC(unittype.VehicleType):
        id = "Grad_FDDM"
        name = "Grad MRL FDDM (FC)"
        detection_range = 0
        threat_range = 1000
        air_weapon_dist = 1000

    class HUMVEE_JTAC(unittype.VehicleType):
        id = "MLRS FDDM"
        name = "HUMVEE JTAC"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class MLRS_BM_21_Grad_122mm(unittype.VehicleType):
        id = "Grad-URAL"
        name = "MLRS BM-21 Grad 122mm"
        detection_range = 0
        threat_range = 19000
        air_weapon_dist = 19000

    class MLRS_BM_27_Uragan_220mm(unittype.VehicleType):
        id = "Uragan_BM-27"
        name = "MLRS BM-27 Uragan 220mm"
        detection_range = 0
        threat_range = 35800
        air_weapon_dist = 35800

    class MLRS_9A52_Smerch_CM_300mm(unittype.VehicleType):
        id = "Smerch"
        name = "MLRS 9A52 Smerch CM 300mm"
        detection_range = 0
        threat_range = 70000
        air_weapon_dist = 70000

    class MLRS_9A52_Smerch_HE_300mm(unittype.VehicleType):
        id = "Smerch_HE"
        name = "MLRS 9A52 Smerch HE 300mm"
        detection_range = 0
        threat_range = 70000
        air_weapon_dist = 70000

    class MLRS_M270_227mm(unittype.VehicleType):
        id = "MLRS"
        name = "MLRS M270 227mm"
        detection_range = 0
        threat_range = 32000
        air_weapon_dist = 32000
        eplrs = True

    class PLZ_05(unittype.VehicleType):
        id = "PLZ05"
        name = "PLZ-05"
        detection_range = 0
        threat_range = 23500
        air_weapon_dist = 23500
        eplrs = True

    class SPG_Sturmpanzer_IV_Brummbar(unittype.VehicleType):
        id = "SturmPzIV"
        name = "SPG Sturmpanzer IV Brummbar"
        detection_range = 0
        threat_range = 4500
        air_weapon_dist = 2500

    class SPG_M12_GMC_155mm(unittype.VehicleType):
        id = "M12_GMC"
        name = "SPG M12 GMC 155mm"
        detection_range = 0
        threat_range = 18300
        air_weapon_dist = 0


class Infantry:

    class Paratrooper_RPG_16(unittype.VehicleType):
        id = "Paratrooper RPG-16"
        name = "Paratrooper RPG-16"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Paratrooper_AKS(unittype.VehicleType):
        id = "Paratrooper AKS-74"
        name = "Paratrooper AKS"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Insurgent_AK_74(unittype.VehicleType):
        id = "Infantry AK Ins"
        name = "Insurgent AK-74"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_AK_74(unittype.VehicleType):
        id = "Soldier AK"
        name = "Infantry AK-74"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_AK_74_Rus(unittype.VehicleType):
        id = "Infantry AK"
        name = "Infantry AK-74 Rus"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_M249(unittype.VehicleType):
        id = "Soldier M249"
        name = "Infantry M249"
        detection_range = 0
        threat_range = 700
        air_weapon_dist = 700

    class Infantry_M4(unittype.VehicleType):
        id = "Soldier M4"
        name = "Infantry M4"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_M4_Georgia(unittype.VehicleType):
        id = "Soldier M4 GRG"
        name = "Infantry M4 Georgia"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_RPG(unittype.VehicleType):
        id = "Soldier RPG"
        name = "Infantry RPG"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_Mauser_98(unittype.VehicleType):
        id = "soldier_mauser98"
        name = "Infantry Mauser 98"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_SMLE_No_4_Mk_1(unittype.VehicleType):
        id = "soldier_wwii_br_01"
        name = "Infantry SMLE No.4 Mk-1"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_M1_Garand(unittype.VehicleType):
        id = "soldier_wwii_us"
        name = "Infantry M1 Garand"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500


class AirDefence:

    class SAM_SA_19_Tunguska_Grison(unittype.VehicleType):
        id = "2S6 Tunguska"
        name = "SAM SA-19 Tunguska \"Grison\" "
        detection_range = 18000
        threat_range = 8000
        air_weapon_dist = 8000

    class SAM_SA_6_Kub_Gainful_TEL(unittype.VehicleType):
        id = "Kub 2P25 ln"
        name = "SAM SA-6 Kub \"Gainful\" TEL"
        detection_range = 0
        threat_range = 25000
        air_weapon_dist = 25000

    class SAM_SA_3_S_125_Goa_LN(unittype.VehicleType):
        id = "5p73 s-125 ln"
        name = "SAM SA-3 S-125 \"Goa\" LN"
        detection_range = 0
        threat_range = 18000
        air_weapon_dist = 18000

    class SAM_SA_10_S_300_Grumble_TEL_D(unittype.VehicleType):
        id = "S-300PS 5P85C ln"
        name = "SAM SA-10 S-300 \"Grumble\" TEL D"
        detection_range = 0
        threat_range = 120000
        air_weapon_dist = 120000

    class SAM_SA_10_S_300_Grumble_TEL_C(unittype.VehicleType):
        id = "S-300PS 5P85D ln"
        name = "SAM SA-10 S-300 \"Grumble\" TEL C"
        detection_range = 0
        threat_range = 120000
        air_weapon_dist = 120000

    class SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL(unittype.VehicleType):
        id = "SA-11 Buk LN 9A310M1"
        name = "SAM SA-11 Buk \"Gadfly\" Fire Dome TEL"
        detection_range = 50000
        threat_range = 35000
        air_weapon_dist = 35000

    class SAM_SA_8_Osa_Gecko_TEL(unittype.VehicleType):
        id = "Osa 9A33 ln"
        name = "SAM SA-8 Osa \"Gecko\" TEL"
        detection_range = 30000
        threat_range = 10300
        air_weapon_dist = 10300

    class SAM_SA_15_Tor_Gauntlet(unittype.VehicleType):
        id = "Tor 9A331"
        name = "SAM SA-15 Tor \"Gauntlet\""
        detection_range = 25000
        threat_range = 12000
        air_weapon_dist = 12000

    class SAM_SA_13_Strela_10M3_Gopher_TEL(unittype.VehicleType):
        id = "Strela-10M3"
        name = "SAM SA-13 Strela 10M3 \"Gopher\" TEL"
        detection_range = 8000
        threat_range = 5000
        air_weapon_dist = 5000

    class SAM_SA_9_Strela_1_Gaskin_TEL(unittype.VehicleType):
        id = "Strela-1 9P31"
        name = "SAM SA-9 Strela 1 \"Gaskin\" TEL"
        detection_range = 5000
        threat_range = 4200
        air_weapon_dist = 4200

    class SAM_SA_11_Buk_Gadfly_C2(unittype.VehicleType):
        id = "SA-11 Buk CC 9S470M1"
        name = "SAM SA-11 Buk \"Gadfly\" C2 "
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_8_Osa_LD_9T217(unittype.VehicleType):
        id = "SA-8 Osa LD 9T217"
        name = "SAM SA-8 Osa LD 9T217"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Patriot_CR__AMG_AN_MRC_137(unittype.VehicleType):
        id = "Patriot AMG"
        name = "SAM Patriot CR (AMG AN/MRC-137)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Patriot_ECS(unittype.VehicleType):
        id = "Patriot ECS"
        name = "SAM Patriot ECS"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class SPAAA_Gepard(unittype.VehicleType):
        id = "Gepard"
        name = "SPAAA Gepard"
        detection_range = 15000
        threat_range = 4000
        air_weapon_dist = 4000

    class SAM_Hawk_Generator__PCP(unittype.VehicleType):
        id = "Hawk pcp"
        name = "SAM Hawk Generator (PCP)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SPAAA_Vulcan_M163(unittype.VehicleType):
        id = "Vulcan"
        name = "SPAAA Vulcan M163"
        detection_range = 5000
        threat_range = 2000
        air_weapon_dist = 2000
        eplrs = True

    class SAM_Hawk_LN_M192(unittype.VehicleType):
        id = "Hawk ln"
        name = "SAM Hawk LN M192"
        detection_range = 0
        threat_range = 45000
        air_weapon_dist = 45000

    class SAM_Chaparral_M48(unittype.VehicleType):
        id = "M48 Chaparral"
        name = "SAM Chaparral M48"
        detection_range = 10000
        threat_range = 8500
        air_weapon_dist = 8500
        eplrs = True

    class SAM_Linebacker___Bradley_M6(unittype.VehicleType):
        id = "M6 Linebacker"
        name = "SAM Linebacker - Bradley M6"
        detection_range = 8000
        threat_range = 4500
        air_weapon_dist = 4500
        eplrs = True

    class SAM_Patriot_LN(unittype.VehicleType):
        id = "Patriot ln"
        name = "SAM Patriot LN"
        detection_range = 0
        threat_range = 100000
        air_weapon_dist = 100000

    class SAM_Avenger__Stinger(unittype.VehicleType):
        id = "M1097 Avenger"
        name = "SAM Avenger (Stinger)"
        detection_range = 5200
        threat_range = 4500
        air_weapon_dist = 4500
        eplrs = True

    class SAM_Patriot_EPP_III(unittype.VehicleType):
        id = "Patriot EPP"
        name = "SAM Patriot EPP-III"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Patriot_C2_ICC(unittype.VehicleType):
        id = "Patriot cp"
        name = "SAM Patriot C2 ICC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Roland_ADS(unittype.VehicleType):
        id = "Roland ADS"
        name = "SAM Roland ADS"
        detection_range = 12000
        threat_range = 8000
        air_weapon_dist = 8000

    class SAM_SA_10_S_300_Grumble_C2(unittype.VehicleType):
        id = "S-300PS 54K6 cp"
        name = "SAM SA-10 S-300 \"Grumble\" C2 "
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class MANPADS_Stinger(unittype.VehicleType):
        id = "Soldier stinger"
        name = "MANPADS Stinger"
        detection_range = 5000
        threat_range = 4500
        air_weapon_dist = 4500

    class MANPADS_Stinger_C2_Desert(unittype.VehicleType):
        id = "Stinger comm dsr"
        name = "MANPADS Stinger C2 Desert"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class MANPADS_Stinger_C2(unittype.VehicleType):
        id = "Stinger comm"
        name = "MANPADS Stinger C2"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class SPAAA_ZSU_23_4_Shilka_Gun_Dish(unittype.VehicleType):
        id = "ZSU-23-4 Shilka"
        name = "SPAAA ZSU-23-4 Shilka \"Gun Dish\""
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Closed_Emplacement(unittype.VehicleType):
        id = "ZU-23 Emplacement Closed"
        name = "AAA ZU-23 Closed Emplacement"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Emplacement(unittype.VehicleType):
        id = "ZU-23 Emplacement"
        name = "AAA ZU-23 Emplacement"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class SPAAA_ZU_23_2_Mounted_Ural_375(unittype.VehicleType):
        id = "Ural-375 ZU-23"
        name = "SPAAA ZU-23-2 Mounted Ural 375"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Closed_Emplacement_Insurgent(unittype.VehicleType):
        id = "ZU-23 Closed Insurgent"
        name = "AAA ZU-23 Closed Emplacement Insurgent"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375(unittype.VehicleType):
        id = "Ural-375 ZU-23 Insurgent"
        name = "SPAAA ZU-23-2 Insurgent Mounted Ural-375"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Insurgent(unittype.VehicleType):
        id = "ZU-23 Insurgent"
        name = "AAA ZU-23 Insurgent"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class MANPADS_SA_18_Igla_Grouse(unittype.VehicleType):
        id = "SA-18 Igla manpad"
        name = "MANPADS SA-18 Igla \"Grouse\""
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class MANPADS_SA_18_Igla_Grouse_C2(unittype.VehicleType):
        id = "SA-18 Igla comm"
        name = "MANPADS SA-18 Igla \"Grouse\" C2"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class MANPADS_SA_18_Igla_S_Grouse(unittype.VehicleType):
        id = "SA-18 Igla-S manpad"
        name = "MANPADS SA-18 Igla-S \"Grouse\""
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class MANPADS_SA_18_Igla_S_Grouse_C2(unittype.VehicleType):
        id = "SA-18 Igla-S comm"
        name = "MANPADS SA-18 Igla-S \"Grouse\" C2"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class MANPADS_SA_18_Igla_Grouse_Ins(unittype.VehicleType):
        id = "Igla manpad INS"
        name = "MANPADS SA-18 Igla \"Grouse\" Ins"
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class EWR_1L13(unittype.VehicleType):
        id = "1L13 EWR"
        name = "EWR 1L13"
        detection_range = 120000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_6_Kub_Long_Track_STR(unittype.VehicleType):
        id = "Kub 1S91 str"
        name = "SAM SA-6 Kub \"Long Track\" STR"
        detection_range = 70000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_10_S_300_Grumble_Flap_Lid_TR(unittype.VehicleType):
        id = "S-300PS 40B6M tr"
        name = "SAM SA-10 S-300 \"Grumble\" Flap Lid TR "
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_10_S_300_Grumble_Clam_Shell_SR(unittype.VehicleType):
        id = "S-300PS 40B6MD sr"
        name = "SAM SA-10 S-300 \"Grumble\" Clam Shell SR"
        detection_range = 60000
        threat_range = 0
        air_weapon_dist = 0

    class EWR_55G6(unittype.VehicleType):
        id = "55G6 EWR"
        name = "EWR 55G6"
        detection_range = 120000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_10_S_300_Grumble_Big_Bird_SR(unittype.VehicleType):
        id = "S-300PS 64H6E sr"
        name = "SAM SA-10 S-300 \"Grumble\" Big Bird SR "
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_11_Buk_Gadfly_Snow_Drift_SR(unittype.VehicleType):
        id = "SA-11 Buk SR 9S18M1"
        name = "SAM SA-11 Buk \"Gadfly\" Snow Drift SR"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class MCC_SR_Sborka_Dog_Ear_SR(unittype.VehicleType):
        id = "Dog Ear radar"
        name = "MCC-SR Sborka \"Dog Ear\" SR"
        detection_range = 35000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Hawk_TR__AN_MPQ_46(unittype.VehicleType):
        id = "Hawk tr"
        name = "SAM Hawk TR (AN/MPQ-46)"
        detection_range = 90000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Hawk_SR__AN_MPQ_50(unittype.VehicleType):
        id = "Hawk sr"
        name = "SAM Hawk SR (AN/MPQ-50)"
        detection_range = 90000
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class SAM_Patriot_STR(unittype.VehicleType):
        id = "Patriot str"
        name = "SAM Patriot STR"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Hawk_CWAR_AN_MPQ_55(unittype.VehicleType):
        id = "Hawk cwar"
        name = "SAM Hawk CWAR AN/MPQ-55"
        detection_range = 70000
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class SAM_P19_Flat_Face_SR__SA_2_3(unittype.VehicleType):
        id = "p-19 s-125 sr"
        name = "SAM P19 \"Flat Face\" SR (SA-2/3)"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Roland_EWR(unittype.VehicleType):
        id = "Roland Radar"
        name = "SAM Roland EWR"
        detection_range = 35000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_3_S_125_Low_Blow_TR(unittype.VehicleType):
        id = "snr s-125 tr"
        name = "SAM SA-3 S-125 \"Low Blow\" TR"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_2_S_75_Guideline_LN(unittype.VehicleType):
        id = "S_75M_Volhov"
        name = "SAM SA-2 S-75 \"Guideline\" LN"
        detection_range = 0
        threat_range = 43000
        air_weapon_dist = 43000

    class SAM_SA_2_S_75_Fan_Song_TR(unittype.VehicleType):
        id = "SNR_75V"
        name = "SAM SA-2 S-75 \"Fan Song\" TR"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class SPAAA_ZSU_57_2(unittype.VehicleType):
        id = "ZSU_57_2"
        name = "SPAAA ZSU-57-2"
        detection_range = 5000
        threat_range = 7000
        air_weapon_dist = 7000

    class AAA_S_60_57mm(unittype.VehicleType):
        id = "S-60_Type59_Artillery"
        name = "AAA S-60 57mm"
        detection_range = 5000
        threat_range = 7000
        air_weapon_dist = 7000

    class AAA_40mm_Bofors(unittype.VehicleType):
        id = "bofors40"
        name = "AAA 40mm Bofors"
        detection_range = 0
        threat_range = 7160
        air_weapon_dist = 7160

    class SAM_Rapier_LN(unittype.VehicleType):
        id = "rapier_fsa_launcher"
        name = "SAM Rapier LN"
        detection_range = 30000
        threat_range = 6800
        air_weapon_dist = 6800

    class SAM_Rapier_Tracker(unittype.VehicleType):
        id = "rapier_fsa_optical_tracker_unit"
        name = "SAM Rapier Tracker"
        detection_range = 20000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Rapier_Blindfire_TR(unittype.VehicleType):
        id = "rapier_fsa_blindfire_radar"
        name = "SAM Rapier Blindfire TR"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class AAA_8_8cm_Flak_18(unittype.VehicleType):
        id = "flak18"
        name = "AAA 8,8cm Flak 18"
        detection_range = 0
        threat_range = 11000
        air_weapon_dist = 11000

    class HQ_7_Self_Propelled_LN(unittype.VehicleType):
        id = "HQ-7_LN_SP"
        name = "HQ-7 Self-Propelled LN"
        detection_range = 20000
        threat_range = 12000
        air_weapon_dist = 12000

    class HQ_7_Self_Propelled_STR(unittype.VehicleType):
        id = "HQ-7_STR_SP"
        name = "HQ-7 Self-Propelled STR"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class AAA_Flak_38_20mm(unittype.VehicleType):
        id = "flak30"
        name = "AAA Flak 38 20mm"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_8_8cm_Flak_36(unittype.VehicleType):
        id = "flak36"
        name = "AAA 8,8cm Flak 36"
        detection_range = 0
        threat_range = 11000
        air_weapon_dist = 11000

    class AAA_8_8cm_Flak_37(unittype.VehicleType):
        id = "flak37"
        name = "AAA 8,8cm Flak 37"
        detection_range = 0
        threat_range = 11000
        air_weapon_dist = 11000

    class AAA_Flak_Vierling_38_Quad_20mm(unittype.VehicleType):
        id = "flak38"
        name = "AAA Flak-Vierling 38 Quad 20mm"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_SP_Kdo_G_40(unittype.VehicleType):
        id = "KDO_Mod40"
        name = "AAA SP Kdo.G.40"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class SL_Flakscheinwerfer_37(unittype.VehicleType):
        id = "Flakscheinwerfer_37"
        name = "SL Flakscheinwerfer 37"
        detection_range = 15000
        threat_range = 15000
        air_weapon_dist = 0

    class PU_Maschinensatz_33(unittype.VehicleType):
        id = "Maschinensatz_33"
        name = "PU Maschinensatz_33"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class AAA_8_8cm_Flak_41(unittype.VehicleType):
        id = "flak41"
        name = "AAA 8,8cm Flak 41"
        detection_range = 0
        threat_range = 12500
        air_weapon_dist = 12500

    class EWR_FuMG_401_Freya_LZ(unittype.VehicleType):
        id = "FuMG-401"
        name = "EWR FuMG-401 Freya LZ"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class EWR_FuSe_65_Würzburg_Riese(unittype.VehicleType):
        id = "FuSe-65"
        name = "EWR FuSe-65 Würzburg-Riese"
        detection_range = 60000
        threat_range = 0
        air_weapon_dist = 0

    class AAA_QF_3_7(unittype.VehicleType):
        id = "QF_37_AA"
        name = "AAA QF 3,7\""
        detection_range = 0
        threat_range = 9000
        air_weapon_dist = 9000

    class AAA_M45_Quadmount_HB_12_7mm(unittype.VehicleType):
        id = "M45_Quadmount"
        name = "AAA M45 Quadmount HB 12.7mm"
        detection_range = 0
        threat_range = 1500
        air_weapon_dist = 1500

    class AAA_M1_37mm(unittype.VehicleType):
        id = "M1_37mm"
        name = "AAA M1 37mm"
        detection_range = 0
        threat_range = 5700
        air_weapon_dist = 5700


class Fortification:

    class Bunker_2(unittype.VehicleType):
        id = "Bunker"
        name = "Bunker 2"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Bunker_1(unittype.VehicleType):
        id = "Sandbox"
        name = "Bunker 1"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Barracks_armed(unittype.VehicleType):
        id = "house1arm"
        name = "Barracks armed"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Watch_tower_armed(unittype.VehicleType):
        id = "house2arm"
        name = "Watch tower armed"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Road_outpost(unittype.VehicleType):
        id = "outpost_road"
        name = "Road outpost"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Outpost(unittype.VehicleType):
        id = "outpost"
        name = "Outpost"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Building_armed(unittype.VehicleType):
        id = "houseA_arm"
        name = "Building armed"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class Beacon_TACAN_Portable_TTS_3030(unittype.VehicleType):
        id = "TACAN_beacon"
        name = "Beacon TACAN Portable TTS 3030"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Gun_15cm_SK_C_28_Naval_in_Bunker(unittype.VehicleType):
        id = "SK_C_28_naval_gun"
        name = "Gun 15cm SK C/28 Naval in Bunker"
        detection_range = 0
        threat_range = 20000
        air_weapon_dist = 0

    class Bunker_with_Fire_Control_Center(unittype.VehicleType):
        id = "fire_control"
        name = "Bunker with Fire Control Center"
        detection_range = 0
        threat_range = 1100
        air_weapon_dist = 1100


class Unarmed:

    class GPU_APA_5D(unittype.VehicleType):
        id = "Ural-4320 APA-5D"
        name = "GPU APA-5D"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Refueler_ATMZ_5(unittype.VehicleType):
        id = "ATMZ-5"
        name = "Refueler ATMZ-5"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Refueler_ATZ_10(unittype.VehicleType):
        id = "ATZ-10"
        name = "Refueler ATZ-10"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_GAZ_3307(unittype.VehicleType):
        id = "GAZ-3307"
        name = "Truck GAZ-3307"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_GAZ_3308(unittype.VehicleType):
        id = "GAZ-3308"
        name = "Truck GAZ-3308"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_GAZ_66(unittype.VehicleType):
        id = "GAZ-66"
        name = "Truck GAZ-66"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Refueler_M978_HEMTT(unittype.VehicleType):
        id = "M978 HEMTT Tanker"
        name = "Refueler M978 HEMTT"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_HEMMT_TFFT_Fire(unittype.VehicleType):
        id = "HEMTT TFFT"
        name = "Truck HEMMT TFFT Fire"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Bus_IKARUS_280(unittype.VehicleType):
        id = "IKARUS Bus"
        name = "Bus IKARUS-280"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_KAMAZ_43101(unittype.VehicleType):
        id = "KAMAZ Truck"
        name = "Truck KAMAZ 43101"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Bus_LAZ_695(unittype.VehicleType):
        id = "LAZ Bus"
        name = "Bus LAZ-695"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Bus_LiAZ_677(unittype.VehicleType):
        id = "LiAZ Bus"
        name = "Bus LiAZ-677"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class APC_HMMWV_Jeep(unittype.VehicleType):
        id = "Hummer"
        name = "APC HMMWV Jeep"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class Truck_M818_6x6(unittype.VehicleType):
        id = "M 818"
        name = "Truck M818 6x6"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_MAZ_6303(unittype.VehicleType):
        id = "MAZ-6303"
        name = "Truck MAZ-6303"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class MCC_Predator_UAV_CP__GCS(unittype.VehicleType):
        id = "Predator GCS"
        name = "MCC Predator UAV CP & GCS"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class MCC_COMM_Predator_UAV_CL(unittype.VehicleType):
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

    class APC_Tigr(unittype.VehicleType):
        id = "Tigr_233036"
        name = "APC Tigr"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Bus_ZIU_9_Trolley(unittype.VehicleType):
        id = "Trolley bus"
        name = "Bus ZIU-9 Trolley"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LUV_UAZ_469_Jeep(unittype.VehicleType):
        id = "UAZ-469"
        name = "LUV UAZ-469 Jeep"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Ural_ATsP_6_Firefighter(unittype.VehicleType):
        id = "Ural ATsP-6"
        name = "Truck Ural ATsP-6 Firefighter"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Ural_4320_31_Arm_d(unittype.VehicleType):
        id = "Ural-4320-31"
        name = "Truck Ural-4320-31 Arm'd"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Ural_4320T(unittype.VehicleType):
        id = "Ural-4320T"
        name = "Truck Ural-4320T"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Ural_375_Mobile_C2(unittype.VehicleType):
        id = "Ural-375 PBU"
        name = "Truck Ural-375 Mobile C2"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Ural_375(unittype.VehicleType):
        id = "Ural-375"
        name = "Truck Ural-375"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Car_VAZ_2109(unittype.VehicleType):
        id = "VAZ Car"
        name = "Car VAZ-2109"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class GPU_APA_80_on_ZIL_131(unittype.VehicleType):
        id = "ZiL-131 APA-80"
        name = "GPU APA-80 on ZIL-131"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_SKP_11_Mobile_ATC(unittype.VehicleType):
        id = "SKP-11"
        name = "Truck SKP-11 Mobile ATC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_ZIL_131__C2(unittype.VehicleType):
        id = "ZIL-131 KUNG"
        name = "Truck ZIL-131 (C2)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_ZIL_4331(unittype.VehicleType):
        id = "ZIL-4331"
        name = "Truck ZIL-4331"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_KrAZ_6322_6x6(unittype.VehicleType):
        id = "KrAZ6322"
        name = "Truck KrAZ-6322 6x6"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Bedford(unittype.VehicleType):
        id = "Bedford_MWD"
        name = "Truck Bedford"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Land_Rover_101_FC(unittype.VehicleType):
        id = "Land_Rover_101_FC"
        name = "Truck Land Rover 101 FC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LUV_Land_Rover_109(unittype.VehicleType):
        id = "Land_Rover_109_S3"
        name = "LUV Land Rover 109"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_Opel_Blitz(unittype.VehicleType):
        id = "Blitz_36-6700A"
        name = "Truck Opel Blitz"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LUV_Kubelwagen_82(unittype.VehicleType):
        id = "Kubelwagen_82"
        name = "LUV Kubelwagen 82"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LUV_Kettenrad(unittype.VehicleType):
        id = "Sd_Kfz_2"
        name = "LUV Kettenrad"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Carrier_Sd_Kfz_7_Tractor(unittype.VehicleType):
        id = "Sd_Kfz_7"
        name = "Carrier Sd.Kfz.7 Tractor"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class LUV_Horch_901_Staff_Car(unittype.VehicleType):
        id = "Horch_901_typ_40_kfz_21"
        name = "LUV Horch 901 Staff Car"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Truck_GMC_Jimmy_6x6_Truck(unittype.VehicleType):
        id = "CCKW_353"
        name = "Truck GMC \"Jimmy\" 6x6 Truck"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Car_Willys_Jeep(unittype.VehicleType):
        id = "Willys_MB"
        name = "Car Willys Jeep"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Carrier_M30_Cargo(unittype.VehicleType):
        id = "M30_CC"
        name = "Carrier M30 Cargo"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0

    class Tractor_M4_Hi_Speed(unittype.VehicleType):
        id = "M4_Tractor"
        name = "Tractor M4 Hi-Speed"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0


class Armor:

    class APC_AAV_7_Amphibious(unittype.VehicleType):
        id = "AAV7"
        name = "APC AAV-7 Amphibious"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200

    class IFV_BMD_1(unittype.VehicleType):
        id = "BMD-1"
        name = "IFV BMD-1"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 1000

    class IFV_BMP_1(unittype.VehicleType):
        id = "BMP-1"
        name = "IFV BMP-1"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 1000

    class IFV_BMP_2(unittype.VehicleType):
        id = "BMP-2"
        name = "IFV BMP-2"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 2000

    class IFV_BMP_3(unittype.VehicleType):
        id = "BMP-3"
        name = "IFV BMP-3"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 2000

    class IFV_BRDM_2(unittype.VehicleType):
        id = "BRDM-2"
        name = "IFV BRDM-2"
        detection_range = 0
        threat_range = 1600
        air_weapon_dist = 1600

    class APC_BTR_80(unittype.VehicleType):
        id = "BTR-80"
        name = "APC BTR-80"
        detection_range = 0
        threat_range = 1600
        air_weapon_dist = 1600

    class APC_BTR_RD(unittype.VehicleType):
        id = "BTR_D"
        name = "APC BTR-RD"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 1000

    class APC_Cobra__Scout(unittype.VehicleType):
        id = "Cobra"
        name = "APC Cobra (Scout)"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200

    class IFV_LAV_25(unittype.VehicleType):
        id = "LAV-25"
        name = "IFV LAV-25"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class APC_HMMWV__Scout(unittype.VehicleType):
        id = "M1043 HMMWV Armament"
        name = "APC HMMWV (Scout)"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class ATGM_HMMWV(unittype.VehicleType):
        id = "M1045 HMMWV TOW"
        name = "ATGM HMMWV"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 0
        eplrs = True

    class IFV_M1126_Stryker_ICV(unittype.VehicleType):
        id = "M1126 Stryker ICV"
        name = "IFV M1126 Stryker ICV"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class APC_M113(unittype.VehicleType):
        id = "M-113"
        name = "APC M113"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class ATGM_Stryker(unittype.VehicleType):
        id = "M1134 Stryker ATGM"
        name = "ATGM Stryker"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 1000
        eplrs = True

    class IFV_M2A2_Bradley(unittype.VehicleType):
        id = "M-2 Bradley"
        name = "IFV M2A2 Bradley"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 2500
        eplrs = True

    class IFV_Warrior(unittype.VehicleType):
        id = "MCV-80"
        name = "IFV Warrior "
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class APC_MTLB(unittype.VehicleType):
        id = "MTLB"
        name = "APC MTLB"
        detection_range = 0
        threat_range = 1000
        air_weapon_dist = 1000

    class IFV_Marder(unittype.VehicleType):
        id = "Marder"
        name = "IFV Marder"
        detection_range = 0
        threat_range = 1500
        air_weapon_dist = 1500

    class APC_TPz_Fuchs(unittype.VehicleType):
        id = "TPZ"
        name = "APC TPz Fuchs "
        detection_range = 0
        threat_range = 1000
        air_weapon_dist = 1000

    class MBT_Challenger_II(unittype.VehicleType):
        id = "Challenger2"
        name = "MBT Challenger II"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class MBT_Leclerc(unittype.VehicleType):
        id = "Leclerc"
        name = "MBT Leclerc"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class MBT_Leopard_2(unittype.VehicleType):
        id = "Leopard-2"
        name = "MBT Leopard 2"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class MBT_M60A3_Patton(unittype.VehicleType):
        id = "M-60"
        name = "MBT M60A3 Patton"
        detection_range = 0
        threat_range = 8000
        air_weapon_dist = 1500

    class SPG_Stryker_MGS(unittype.VehicleType):
        id = "M1128 Stryker MGS"
        name = "SPG Stryker MGS"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 1200
        eplrs = True

    class MBT_M1A2_Abrams(unittype.VehicleType):
        id = "M-1 Abrams"
        name = "MBT M1A2 Abrams"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1200
        eplrs = True

    class MBT_T_55(unittype.VehicleType):
        id = "T-55"
        name = "MBT T-55"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 1200

    class MBT_T_72B(unittype.VehicleType):
        id = "T-72B"
        name = "MBT T-72B"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 3500

    class MBT_T_80U(unittype.VehicleType):
        id = "T-80UD"
        name = "MBT T-80U"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 3500

    class MBT_T_90(unittype.VehicleType):
        id = "T-90"
        name = "MBT T-90"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 3500

    class MBT_Leopard_1A3(unittype.VehicleType):
        id = "Leopard1A3"
        name = "MBT Leopard 1A3"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 1500

    class MBT_Merkava_IV(unittype.VehicleType):
        id = "Merkava_Mk4"
        name = "MBT Merkava IV"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1200

    class MT_M4_Sherman(unittype.VehicleType):
        id = "M4_Sherman"
        name = "MT M4 Sherman"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class APC_M2A1_Halftrack(unittype.VehicleType):
        id = "M2A1_halftrack"
        name = "APC M2A1 Halftrack"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0

    class MBT_T_72B3(unittype.VehicleType):
        id = "T-72B3"
        name = "MBT T-72B3"
        detection_range = 0
        threat_range = 4000
        air_weapon_dist = 3500

    class APC_BTR_82A(unittype.VehicleType):
        id = "BTR-82A"
        name = "APC BTR-82A"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 2000

    class MT_PzIV_H(unittype.VehicleType):
        id = "Pz_IV_H"
        name = "MT PzIV H"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class APC_Sd_Kfz_251_Halftrack(unittype.VehicleType):
        id = "Sd_Kfz_251"
        name = "APC Sd.Kfz.251 Halftrack"
        detection_range = 0
        threat_range = 1100
        air_weapon_dist = 0

    class ZTZ_96B(unittype.VehicleType):
        id = "ZTZ96B"
        name = "ZTZ-96B"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 3500
        eplrs = True

    class ZBD_04A(unittype.VehicleType):
        id = "ZBD04A"
        name = "ZBD-04A"
        detection_range = 0
        threat_range = 4800
        air_weapon_dist = 0
        eplrs = True

    class HT_Pz_Kpfw_VI_Tiger_I(unittype.VehicleType):
        id = "Tiger_I"
        name = "HT Pz.Kpfw.VI Tiger I"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class HT_Pz_Kpfw_VI_Ausf__B_Tiger_II(unittype.VehicleType):
        id = "Tiger_II_H"
        name = "HT Pz.Kpfw.VI Ausf. B Tiger II"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class MT_Pz_Kpfw_V_Panther_Ausf_G(unittype.VehicleType):
        id = "Pz_V_Panther_G"
        name = "MT Pz.Kpfw.V Panther Ausf.G"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class SPG_Jagdpanther_G1(unittype.VehicleType):
        id = "Jagdpanther_G1"
        name = "SPG Jagdpanther G1"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 0

    class SPG_Jagdpanzer_IV(unittype.VehicleType):
        id = "JagdPz_IV"
        name = "SPG Jagdpanzer IV"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class SPG_StuG_IV(unittype.VehicleType):
        id = "Stug_IV"
        name = "SPG StuG IV"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class IFV_Sd_Kfz_234_2_Puma(unittype.VehicleType):
        id = "Sd_Kfz_234_2_Puma"
        name = "IFV Sd.Kfz.234/2 Puma"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class SPG_StuG_III_Ausf__G(unittype.VehicleType):
        id = "Stug_III"
        name = "SPG StuG III Ausf. G"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class SPG_Sd_Kfz_184_Elefant(unittype.VehicleType):
        id = "Elefant_SdKfz_184"
        name = "SPG Sd.Kfz.184 Elefant"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class CT_Cromwell_IV(unittype.VehicleType):
        id = "Cromwell_IV"
        name = "CT Cromwell IV"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class MT_M4A4_Sherman_Firefly(unittype.VehicleType):
        id = "M4A4_Sherman_FF"
        name = "MT M4A4 Sherman Firefly"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class CT_Centaur_IV(unittype.VehicleType):
        id = "Centaur_IV"
        name = "CT Centaur IV"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class HIT_Churchill_VII(unittype.VehicleType):
        id = "Churchill_VII"
        name = "HIT Churchill VII"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Car_Daimler_Armored(unittype.VehicleType):
        id = "Daimler_AC"
        name = "Car Daimler Armored"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class LT_Mk_VII_Tetrarch(unittype.VehicleType):
        id = "Tetrarch"
        name = "LT Mk VII Tetrarch"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class SPG_M10_GMC(unittype.VehicleType):
        id = "M10_GMC"
        name = "SPG M10 GMC"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class Car_M8_Greyhound_Armored(unittype.VehicleType):
        id = "M8_Greyhound"
        name = "Car M8 Greyhound Armored"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0


class MissilesSS:

    class SSM_SS_1C_Scud_B(unittype.VehicleType):
        id = "Scud_B"
        name = "SSM SS-1C Scud-B"
        detection_range = 0
        threat_range = 320000
        air_weapon_dist = 320000

    class AShM_SS_N_2_Silkworm(unittype.VehicleType):
        id = "hy_launcher"
        name = "AShM SS-N-2 Silkworm"
        detection_range = 100000
        threat_range = 100000
        air_weapon_dist = 100000

    class AShM_Silkworm_SR(unittype.VehicleType):
        id = "Silkworm_SR"
        name = "AShM Silkworm SR"
        detection_range = 200000
        threat_range = 0
        air_weapon_dist = 0

    class SSM_V_1_Launcher(unittype.VehicleType):
        id = "v1_launcher"
        name = "SSM V-1 Launcher"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0


class Locomotive:

    class Loco_VL80_Electric(unittype.VehicleType):
        id = "Electric locomotive"
        name = "Loco VL80 Electric"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Loco_CHME3T(unittype.VehicleType):
        id = "Locomotive"
        name = "Loco CHME3T"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Loco_ES44AH(unittype.VehicleType):
        id = "ES44AH"
        name = "Loco ES44AH"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Loco_DRG_Class_86(unittype.VehicleType):
        id = "DRG_Class_86"
        name = "Loco DRG Class 86"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0


class Carriage:

    class Freight_Van(unittype.VehicleType):
        id = "Coach cargo"
        name = "Freight Van"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Open_Wagon(unittype.VehicleType):
        id = "Coach cargo open"
        name = "Open Wagon"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tank_Car_blue(unittype.VehicleType):
        id = "Coach a tank blue"
        name = "Tank Car blue"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tank_Car_yellow(unittype.VehicleType):
        id = "Coach a tank yellow"
        name = "Tank Car yellow"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Passenger_Car(unittype.VehicleType):
        id = "Coach a passenger"
        name = "Passenger Car"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_Platform(unittype.VehicleType):
        id = "Coach a platform"
        name = "Coach Platform"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Flatcar(unittype.VehicleType):
        id = "Boxcartrinity"
        name = "Flatcar"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tank_Cartrinity(unittype.VehicleType):
        id = "Tankcartrinity"
        name = "Tank Cartrinity"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Well_Car(unittype.VehicleType):
        id = "Wellcarnsc"
        name = "Well Car"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class DR_50_ton_flat_wagon(unittype.VehicleType):
        id = "DR_50Ton_Flat_Wagon"
        name = "DR 50-ton flat wagon"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Wagon_G10__Germany(unittype.VehicleType):
        id = "German_covered_wagon_G10"
        name = "Wagon G10 (Germany)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tank_Car__Germany(unittype.VehicleType):
        id = "German_tank_wagon"
        name = "Tank Car (Germany)"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

vehicle_map = {
    "2B11 mortar": Artillery.Mortar_2B11_120mm,
    "SAU Gvozdika": Artillery.SPH_2S1_Gvozdika_122mm,
    "SAU Msta": Artillery.SPH_2S19_Msta_152mm,
    "SAU Akatsia": Artillery.SPH_2S3_Akatsia_152mm,
    "SAU 2-C9": Artillery.SPH_2S9_Nona_120mm_M,
    "M-109": Artillery.SPH_M109_Paladin_155mm,
    "SpGH_Dana": Artillery.SPH_Dana_vz77_152mm,
    "AAV7": Armor.APC_AAV_7_Amphibious,
    "BMD-1": Armor.IFV_BMD_1,
    "BMP-1": Armor.IFV_BMP_1,
    "BMP-2": Armor.IFV_BMP_2,
    "BMP-3": Armor.IFV_BMP_3,
    "BRDM-2": Armor.IFV_BRDM_2,
    "BTR-80": Armor.APC_BTR_80,
    "BTR_D": Armor.APC_BTR_RD,
    "Cobra": Armor.APC_Cobra__Scout,
    "LAV-25": Armor.IFV_LAV_25,
    "M1043 HMMWV Armament": Armor.APC_HMMWV__Scout,
    "M1045 HMMWV TOW": Armor.ATGM_HMMWV,
    "M1126 Stryker ICV": Armor.IFV_M1126_Stryker_ICV,
    "M-113": Armor.APC_M113,
    "M1134 Stryker ATGM": Armor.ATGM_Stryker,
    "M-2 Bradley": Armor.IFV_M2A2_Bradley,
    "MCV-80": Armor.IFV_Warrior,
    "MTLB": Armor.APC_MTLB,
    "Marder": Armor.IFV_Marder,
    "TPZ": Armor.APC_TPz_Fuchs,
    "Grad_FDDM": Artillery.Grad_MRL_FDDM__FC,
    "Bunker": Fortification.Bunker_2,
    "Paratrooper RPG-16": Infantry.Paratrooper_RPG_16,
    "Paratrooper AKS-74": Infantry.Paratrooper_AKS,
    "Infantry AK Ins": Infantry.Insurgent_AK_74,
    "Sandbox": Fortification.Bunker_1,
    "Soldier AK": Infantry.Infantry_AK_74,
    "Infantry AK": Infantry.Infantry_AK_74_Rus,
    "Soldier M249": Infantry.Infantry_M249,
    "Soldier M4": Infantry.Infantry_M4,
    "Soldier M4 GRG": Infantry.Infantry_M4_Georgia,
    "Soldier RPG": Infantry.Infantry_RPG,
    "MLRS FDDM": Artillery.HUMVEE_JTAC,
    "Grad-URAL": Artillery.MLRS_BM_21_Grad_122mm,
    "Uragan_BM-27": Artillery.MLRS_BM_27_Uragan_220mm,
    "Smerch": Artillery.MLRS_9A52_Smerch_CM_300mm,
    "Smerch_HE": Artillery.MLRS_9A52_Smerch_HE_300mm,
    "MLRS": Artillery.MLRS_M270_227mm,
    "2S6 Tunguska": AirDefence.SAM_SA_19_Tunguska_Grison,
    "Kub 2P25 ln": AirDefence.SAM_SA_6_Kub_Gainful_TEL,
    "5p73 s-125 ln": AirDefence.SAM_SA_3_S_125_Goa_LN,
    "S-300PS 5P85C ln": AirDefence.SAM_SA_10_S_300_Grumble_TEL_D,
    "S-300PS 5P85D ln": AirDefence.SAM_SA_10_S_300_Grumble_TEL_C,
    "SA-11 Buk LN 9A310M1": AirDefence.SAM_SA_11_Buk_Gadfly_Fire_Dome_TEL,
    "Osa 9A33 ln": AirDefence.SAM_SA_8_Osa_Gecko_TEL,
    "Tor 9A331": AirDefence.SAM_SA_15_Tor_Gauntlet,
    "Strela-10M3": AirDefence.SAM_SA_13_Strela_10M3_Gopher_TEL,
    "Strela-1 9P31": AirDefence.SAM_SA_9_Strela_1_Gaskin_TEL,
    "SA-11 Buk CC 9S470M1": AirDefence.SAM_SA_11_Buk_Gadfly_C2,
    "SA-8 Osa LD 9T217": AirDefence.SAM_SA_8_Osa_LD_9T217,
    "Patriot AMG": AirDefence.SAM_Patriot_CR__AMG_AN_MRC_137,
    "Patriot ECS": AirDefence.SAM_Patriot_ECS,
    "Gepard": AirDefence.SPAAA_Gepard,
    "Hawk pcp": AirDefence.SAM_Hawk_Generator__PCP,
    "Vulcan": AirDefence.SPAAA_Vulcan_M163,
    "Hawk ln": AirDefence.SAM_Hawk_LN_M192,
    "M48 Chaparral": AirDefence.SAM_Chaparral_M48,
    "M6 Linebacker": AirDefence.SAM_Linebacker___Bradley_M6,
    "Patriot ln": AirDefence.SAM_Patriot_LN,
    "M1097 Avenger": AirDefence.SAM_Avenger__Stinger,
    "Patriot EPP": AirDefence.SAM_Patriot_EPP_III,
    "Patriot cp": AirDefence.SAM_Patriot_C2_ICC,
    "Roland ADS": AirDefence.SAM_Roland_ADS,
    "S-300PS 54K6 cp": AirDefence.SAM_SA_10_S_300_Grumble_C2,
    "Soldier stinger": AirDefence.MANPADS_Stinger,
    "Stinger comm dsr": AirDefence.MANPADS_Stinger_C2_Desert,
    "Stinger comm": AirDefence.MANPADS_Stinger_C2,
    "ZSU-23-4 Shilka": AirDefence.SPAAA_ZSU_23_4_Shilka_Gun_Dish,
    "ZU-23 Emplacement Closed": AirDefence.AAA_ZU_23_Closed_Emplacement,
    "ZU-23 Emplacement": AirDefence.AAA_ZU_23_Emplacement,
    "Ural-375 ZU-23": AirDefence.SPAAA_ZU_23_2_Mounted_Ural_375,
    "ZU-23 Closed Insurgent": AirDefence.AAA_ZU_23_Closed_Emplacement_Insurgent,
    "Ural-375 ZU-23 Insurgent": AirDefence.SPAAA_ZU_23_2_Insurgent_Mounted_Ural_375,
    "ZU-23 Insurgent": AirDefence.AAA_ZU_23_Insurgent,
    "SA-18 Igla manpad": AirDefence.MANPADS_SA_18_Igla_Grouse,
    "SA-18 Igla comm": AirDefence.MANPADS_SA_18_Igla_Grouse_C2,
    "SA-18 Igla-S manpad": AirDefence.MANPADS_SA_18_Igla_S_Grouse,
    "SA-18 Igla-S comm": AirDefence.MANPADS_SA_18_Igla_S_Grouse_C2,
    "Igla manpad INS": AirDefence.MANPADS_SA_18_Igla_Grouse_Ins,
    "1L13 EWR": AirDefence.EWR_1L13,
    "Kub 1S91 str": AirDefence.SAM_SA_6_Kub_Long_Track_STR,
    "S-300PS 40B6M tr": AirDefence.SAM_SA_10_S_300_Grumble_Flap_Lid_TR,
    "S-300PS 40B6MD sr": AirDefence.SAM_SA_10_S_300_Grumble_Clam_Shell_SR,
    "55G6 EWR": AirDefence.EWR_55G6,
    "S-300PS 64H6E sr": AirDefence.SAM_SA_10_S_300_Grumble_Big_Bird_SR,
    "SA-11 Buk SR 9S18M1": AirDefence.SAM_SA_11_Buk_Gadfly_Snow_Drift_SR,
    "Dog Ear radar": AirDefence.MCC_SR_Sborka_Dog_Ear_SR,
    "Hawk tr": AirDefence.SAM_Hawk_TR__AN_MPQ_46,
    "Hawk sr": AirDefence.SAM_Hawk_SR__AN_MPQ_50,
    "Patriot str": AirDefence.SAM_Patriot_STR,
    "Hawk cwar": AirDefence.SAM_Hawk_CWAR_AN_MPQ_55,
    "p-19 s-125 sr": AirDefence.SAM_P19_Flat_Face_SR__SA_2_3,
    "Roland Radar": AirDefence.SAM_Roland_EWR,
    "snr s-125 tr": AirDefence.SAM_SA_3_S_125_Low_Blow_TR,
    "house1arm": Fortification.Barracks_armed,
    "house2arm": Fortification.Watch_tower_armed,
    "outpost_road": Fortification.Road_outpost,
    "outpost": Fortification.Outpost,
    "houseA_arm": Fortification.Building_armed,
    "TACAN_beacon": Fortification.Beacon_TACAN_Portable_TTS_3030,
    "Challenger2": Armor.MBT_Challenger_II,
    "Leclerc": Armor.MBT_Leclerc,
    "Leopard-2": Armor.MBT_Leopard_2,
    "M-60": Armor.MBT_M60A3_Patton,
    "M1128 Stryker MGS": Armor.SPG_Stryker_MGS,
    "M-1 Abrams": Armor.MBT_M1A2_Abrams,
    "T-55": Armor.MBT_T_55,
    "T-72B": Armor.MBT_T_72B,
    "T-80UD": Armor.MBT_T_80U,
    "T-90": Armor.MBT_T_90,
    "Leopard1A3": Armor.MBT_Leopard_1A3,
    "Merkava_Mk4": Armor.MBT_Merkava_IV,
    "Ural-4320 APA-5D": Unarmed.GPU_APA_5D,
    "ATMZ-5": Unarmed.Refueler_ATMZ_5,
    "ATZ-10": Unarmed.Refueler_ATZ_10,
    "GAZ-3307": Unarmed.Truck_GAZ_3307,
    "GAZ-3308": Unarmed.Truck_GAZ_3308,
    "GAZ-66": Unarmed.Truck_GAZ_66,
    "M978 HEMTT Tanker": Unarmed.Refueler_M978_HEMTT,
    "HEMTT TFFT": Unarmed.Truck_HEMMT_TFFT_Fire,
    "IKARUS Bus": Unarmed.Bus_IKARUS_280,
    "KAMAZ Truck": Unarmed.Truck_KAMAZ_43101,
    "LAZ Bus": Unarmed.Bus_LAZ_695,
    "LiAZ Bus": Unarmed.Bus_LiAZ_677,
    "Hummer": Unarmed.APC_HMMWV_Jeep,
    "M 818": Unarmed.Truck_M818_6x6,
    "MAZ-6303": Unarmed.Truck_MAZ_6303,
    "Predator GCS": Unarmed.MCC_Predator_UAV_CP__GCS,
    "Predator TrojanSpirit": Unarmed.MCC_COMM_Predator_UAV_CL,
    "Suidae": Unarmed.Suidae,
    "Tigr_233036": Unarmed.APC_Tigr,
    "Trolley bus": Unarmed.Bus_ZIU_9_Trolley,
    "UAZ-469": Unarmed.LUV_UAZ_469_Jeep,
    "Ural ATsP-6": Unarmed.Truck_Ural_ATsP_6_Firefighter,
    "Ural-4320-31": Unarmed.Truck_Ural_4320_31_Arm_d,
    "Ural-4320T": Unarmed.Truck_Ural_4320T,
    "Ural-375 PBU": Unarmed.Truck_Ural_375_Mobile_C2,
    "Ural-375": Unarmed.Truck_Ural_375,
    "VAZ Car": Unarmed.Car_VAZ_2109,
    "ZiL-131 APA-80": Unarmed.GPU_APA_80_on_ZIL_131,
    "SKP-11": Unarmed.Truck_SKP_11_Mobile_ATC,
    "ZIL-131 KUNG": Unarmed.Truck_ZIL_131__C2,
    "ZIL-4331": Unarmed.Truck_ZIL_4331,
    "KrAZ6322": Unarmed.Truck_KrAZ_6322_6x6,
    "Electric locomotive": Locomotive.Loco_VL80_Electric,
    "Locomotive": Locomotive.Loco_CHME3T,
    "Coach cargo": Carriage.Freight_Van,
    "Coach cargo open": Carriage.Open_Wagon,
    "Coach a tank blue": Carriage.Tank_Car_blue,
    "Coach a tank yellow": Carriage.Tank_Car_yellow,
    "Coach a passenger": Carriage.Passenger_Car,
    "Coach a platform": Carriage.Coach_Platform,
    "Scud_B": MissilesSS.SSM_SS_1C_Scud_B,
    "M4_Sherman": Armor.MT_M4_Sherman,
    "M2A1_halftrack": Armor.APC_M2A1_Halftrack,
    "S_75M_Volhov": AirDefence.SAM_SA_2_S_75_Guideline_LN,
    "SNR_75V": AirDefence.SAM_SA_2_S_75_Fan_Song_TR,
    "ZSU_57_2": AirDefence.SPAAA_ZSU_57_2,
    "T-72B3": Armor.MBT_T_72B3,
    "BTR-82A": Armor.APC_BTR_82A,
    "S-60_Type59_Artillery": AirDefence.AAA_S_60_57mm,
    "Bedford_MWD": Unarmed.Truck_Bedford,
    "bofors40": AirDefence.AAA_40mm_Bofors,
    "rapier_fsa_launcher": AirDefence.SAM_Rapier_LN,
    "rapier_fsa_optical_tracker_unit": AirDefence.SAM_Rapier_Tracker,
    "rapier_fsa_blindfire_radar": AirDefence.SAM_Rapier_Blindfire_TR,
    "Land_Rover_101_FC": Unarmed.Truck_Land_Rover_101_FC,
    "Land_Rover_109_S3": Unarmed.LUV_Land_Rover_109,
    "hy_launcher": MissilesSS.AShM_SS_N_2_Silkworm,
    "Silkworm_SR": MissilesSS.AShM_Silkworm_SR,
    "ES44AH": Locomotive.Loco_ES44AH,
    "Boxcartrinity": Carriage.Flatcar,
    "Tankcartrinity": Carriage.Tank_Cartrinity,
    "Wellcarnsc": Carriage.Well_Car,
    "Pz_IV_H": Armor.MT_PzIV_H,
    "Sd_Kfz_251": Armor.APC_Sd_Kfz_251_Halftrack,
    "flak18": AirDefence.AAA_8_8cm_Flak_18,
    "Blitz_36-6700A": Unarmed.Truck_Opel_Blitz,
    "ZTZ96B": Armor.ZTZ_96B,
    "ZBD04A": Armor.ZBD_04A,
    "HQ-7_LN_SP": AirDefence.HQ_7_Self_Propelled_LN,
    "HQ-7_STR_SP": AirDefence.HQ_7_Self_Propelled_STR,
    "PLZ05": Artillery.PLZ_05,
    "Kubelwagen_82": Unarmed.LUV_Kubelwagen_82,
    "Sd_Kfz_2": Unarmed.LUV_Kettenrad,
    "Sd_Kfz_7": Unarmed.Carrier_Sd_Kfz_7_Tractor,
    "Horch_901_typ_40_kfz_21": Unarmed.LUV_Horch_901_Staff_Car,
    "Tiger_I": Armor.HT_Pz_Kpfw_VI_Tiger_I,
    "Tiger_II_H": Armor.HT_Pz_Kpfw_VI_Ausf__B_Tiger_II,
    "Pz_V_Panther_G": Armor.MT_Pz_Kpfw_V_Panther_Ausf_G,
    "Jagdpanther_G1": Armor.SPG_Jagdpanther_G1,
    "JagdPz_IV": Armor.SPG_Jagdpanzer_IV,
    "Stug_IV": Armor.SPG_StuG_IV,
    "SturmPzIV": Artillery.SPG_Sturmpanzer_IV_Brummbar,
    "Sd_Kfz_234_2_Puma": Armor.IFV_Sd_Kfz_234_2_Puma,
    "flak30": AirDefence.AAA_Flak_38_20mm,
    "flak36": AirDefence.AAA_8_8cm_Flak_36,
    "flak37": AirDefence.AAA_8_8cm_Flak_37,
    "flak38": AirDefence.AAA_Flak_Vierling_38_Quad_20mm,
    "KDO_Mod40": AirDefence.AAA_SP_Kdo_G_40,
    "Flakscheinwerfer_37": AirDefence.SL_Flakscheinwerfer_37,
    "Maschinensatz_33": AirDefence.PU_Maschinensatz_33,
    "soldier_mauser98": Infantry.Infantry_Mauser_98,
    "SK_C_28_naval_gun": Fortification.Gun_15cm_SK_C_28_Naval_in_Bunker,
    "fire_control": Fortification.Bunker_with_Fire_Control_Center,
    "Stug_III": Armor.SPG_StuG_III_Ausf__G,
    "Elefant_SdKfz_184": Armor.SPG_Sd_Kfz_184_Elefant,
    "flak41": AirDefence.AAA_8_8cm_Flak_41,
    "v1_launcher": MissilesSS.SSM_V_1_Launcher,
    "FuMG-401": AirDefence.EWR_FuMG_401_Freya_LZ,
    "FuSe-65": AirDefence.EWR_FuSe_65_Würzburg_Riese,
    "Cromwell_IV": Armor.CT_Cromwell_IV,
    "M4A4_Sherman_FF": Armor.MT_M4A4_Sherman_Firefly,
    "soldier_wwii_br_01": Infantry.Infantry_SMLE_No_4_Mk_1,
    "Centaur_IV": Armor.CT_Centaur_IV,
    "Churchill_VII": Armor.HIT_Churchill_VII,
    "Daimler_AC": Armor.Car_Daimler_Armored,
    "Tetrarch": Armor.LT_Mk_VII_Tetrarch,
    "QF_37_AA": AirDefence.AAA_QF_3_7,
    "CCKW_353": Unarmed.Truck_GMC_Jimmy_6x6_Truck,
    "Willys_MB": Unarmed.Car_Willys_Jeep,
    "M12_GMC": Artillery.SPG_M12_GMC_155mm,
    "M30_CC": Unarmed.Carrier_M30_Cargo,
    "soldier_wwii_us": Infantry.Infantry_M1_Garand,
    "M10_GMC": Armor.SPG_M10_GMC,
    "M8_Greyhound": Armor.Car_M8_Greyhound_Armored,
    "M4_Tractor": Unarmed.Tractor_M4_Hi_Speed,
    "M45_Quadmount": AirDefence.AAA_M45_Quadmount_HB_12_7mm,
    "M1_37mm": AirDefence.AAA_M1_37mm,
    "DR_50Ton_Flat_Wagon": Carriage.DR_50_ton_flat_wagon,
    "DRG_Class_86": Locomotive.Loco_DRG_Class_86,
    "German_covered_wagon_G10": Carriage.Wagon_G10__Germany,
    "German_tank_wagon": Carriage.Tank_Car__Germany,
}
