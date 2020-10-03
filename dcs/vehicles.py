# This file is generated from pydcs_export.lua

import dcs.unittype as unittype


class Artillery:

    class _2B11_mortar(unittype.VehicleType):
        id = "2B11 mortar"
        name = "2B11 mortar"
        detection_range = 0
        threat_range = 7000
        air_weapon_dist = 7000

    class SPH_2S1_Gvozdika(unittype.VehicleType):
        id = "SAU Gvozdika"
        name = "SPH 2S1 Gvozdika"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class SPH_2S19_Msta(unittype.VehicleType):
        id = "SAU Msta"
        name = "SPH 2S19 Msta"
        detection_range = 0
        threat_range = 23500
        air_weapon_dist = 23500

    class SPH_2S3_Akatsia(unittype.VehicleType):
        id = "SAU Akatsia"
        name = "SPH 2S3 Akatsia"
        detection_range = 0
        threat_range = 17000
        air_weapon_dist = 17000

    class SPH_2S9_Nona(unittype.VehicleType):
        id = "SAU 2-C9"
        name = "SPH 2S9 Nona"
        detection_range = 0
        threat_range = 7000
        air_weapon_dist = 7000

    class SPH_M109_Paladin(unittype.VehicleType):
        id = "M-109"
        name = "SPH M109 Paladin"
        detection_range = 0
        threat_range = 22000
        air_weapon_dist = 22000
        eplrs = True

    class SpGH_Dana(unittype.VehicleType):
        id = "SpGH_Dana"
        name = "SpGH Dana"
        detection_range = 0
        threat_range = 18700
        air_weapon_dist = 18700

    class MLRS_FDDM(unittype.VehicleType):
        id = "MLRS FDDM"
        name = "MLRS FDDM"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class MLRS_BM_21_Grad(unittype.VehicleType):
        id = "Grad-URAL"
        name = "MLRS BM-21 Grad"
        detection_range = 0
        threat_range = 19000
        air_weapon_dist = 19000

    class MLRS_9K57_Uragan_BM_27(unittype.VehicleType):
        id = "Uragan_BM-27"
        name = "MLRS 9K57 Uragan BM-27"
        detection_range = 0
        threat_range = 35800
        air_weapon_dist = 35800

    class MLRS_9A52_Smerch(unittype.VehicleType):
        id = "Smerch"
        name = "MLRS 9A52 Smerch"
        detection_range = 0
        threat_range = 70000
        air_weapon_dist = 70000

    class MLRS_9A52_Smerch_HE(unittype.VehicleType):
        id = "Smerch_HE"
        name = "MLRS 9A52 Smerch HE"
        detection_range = 0
        threat_range = 70000
        air_weapon_dist = 70000

    class MLRS_M270(unittype.VehicleType):
        id = "MLRS"
        name = "MLRS M270"
        detection_range = 0
        threat_range = 32000
        air_weapon_dist = 32000
        eplrs = True

    class Sturmpanzer_IV_Brummbär(unittype.VehicleType):
        id = "SturmPzIV"
        name = "Sturmpanzer IV Brummbär"
        detection_range = 0
        threat_range = 4500
        air_weapon_dist = 2500

    class M12_GMC(unittype.VehicleType):
        id = "M12_GMC"
        name = "M12 GMC"
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

    class Infantry_Soldier_Insurgents(unittype.VehicleType):
        id = "Infantry AK Ins"
        name = "Infantry Soldier Insurgents"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_AK(unittype.VehicleType):
        id = "Soldier AK"
        name = "Soldier AK"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Infantry_Soldier_Rus(unittype.VehicleType):
        id = "Infantry AK"
        name = "Infantry Soldier Rus"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_M249(unittype.VehicleType):
        id = "Soldier M249"
        name = "Soldier M249"
        detection_range = 0
        threat_range = 700
        air_weapon_dist = 700

    class Infantry_M4(unittype.VehicleType):
        id = "Soldier M4"
        name = "Infantry M4"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Georgian_soldier_with_M4(unittype.VehicleType):
        id = "Soldier M4 GRG"
        name = "Georgian soldier with M4"
        detection_range = 0
        threat_range = 500
        air_weapon_dist = 500

    class Soldier_RPG(unittype.VehicleType):
        id = "Soldier RPG"
        name = "Soldier RPG"
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

    class SAM_SA_19_Tunguska_2S6(unittype.VehicleType):
        id = "2S6 Tunguska"
        name = "SAM SA-19 Tunguska 2S6"
        detection_range = 18000
        threat_range = 8000
        air_weapon_dist = 8000

    class SAM_SA_6_Kub_LN_2P25(unittype.VehicleType):
        id = "Kub 2P25 ln"
        name = "SAM SA-6 Kub LN 2P25"
        detection_range = 0
        threat_range = 25000
        air_weapon_dist = 25000

    class SAM_SA_3_S_125_LN_5P73(unittype.VehicleType):
        id = "5p73 s-125 ln"
        name = "SAM SA-3 S-125 LN 5P73"
        detection_range = 0
        threat_range = 18000
        air_weapon_dist = 18000

    class SAM_SA_10_S_300PS_LN_5P85C(unittype.VehicleType):
        id = "S-300PS 5P85C ln"
        name = "SAM SA-10 S-300PS LN 5P85C"
        detection_range = 0
        threat_range = 120000
        air_weapon_dist = 120000

    class SAM_SA_10_S_300PS_LN_5P85D(unittype.VehicleType):
        id = "S-300PS 5P85D ln"
        name = "SAM SA-10 S-300PS LN 5P85D"
        detection_range = 0
        threat_range = 120000
        air_weapon_dist = 120000

    class SAM_SA_11_Buk_LN_9A310M1(unittype.VehicleType):
        id = "SA-11 Buk LN 9A310M1"
        name = "SAM SA-11 Buk LN 9A310M1"
        detection_range = 50000
        threat_range = 35000
        air_weapon_dist = 35000

    class SAM_SA_8_Osa_9A33(unittype.VehicleType):
        id = "Osa 9A33 ln"
        name = "SAM SA-8 Osa 9A33"
        detection_range = 30000
        threat_range = 10300
        air_weapon_dist = 10300

    class SAM_SA_15_Tor_9A331(unittype.VehicleType):
        id = "Tor 9A331"
        name = "SAM SA-15 Tor 9A331"
        detection_range = 25000
        threat_range = 12000
        air_weapon_dist = 12000

    class SAM_SA_13_Strela_10M3_9A35M3(unittype.VehicleType):
        id = "Strela-10M3"
        name = "SAM SA-13 Strela-10M3 9A35M3"
        detection_range = 8000
        threat_range = 5000
        air_weapon_dist = 5000

    class SAM_SA_9_Strela_1_9P31(unittype.VehicleType):
        id = "Strela-1 9P31"
        name = "SAM SA-9 Strela-1 9P31"
        detection_range = 5000
        threat_range = 4200
        air_weapon_dist = 4200

    class SAM_SA_11_Buk_CC_9S470M1(unittype.VehicleType):
        id = "SA-11 Buk CC 9S470M1"
        name = "SAM SA-11 Buk CC 9S470M1"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_8_Osa_LD_9T217(unittype.VehicleType):
        id = "SA-8 Osa LD 9T217"
        name = "SAM SA-8 Osa LD 9T217"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Patriot_AMG_AN_MRC_137(unittype.VehicleType):
        id = "Patriot AMG"
        name = "SAM Patriot AMG AN/MRC-137"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Patriot_ECS_AN_MSQ_104(unittype.VehicleType):
        id = "Patriot ECS"
        name = "SAM Patriot ECS AN/MSQ-104"
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

    class SAM_Hawk_PCP(unittype.VehicleType):
        id = "Hawk pcp"
        name = "SAM Hawk PCP"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class AAA_Vulcan_M163(unittype.VehicleType):
        id = "Vulcan"
        name = "AAA Vulcan M163"
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

    class SAM_Linebacker_M6(unittype.VehicleType):
        id = "M6 Linebacker"
        name = "SAM Linebacker M6"
        detection_range = 8000
        threat_range = 4500
        air_weapon_dist = 4500
        eplrs = True

    class SAM_Patriot_LN_M901(unittype.VehicleType):
        id = "Patriot ln"
        name = "SAM Patriot LN M901"
        detection_range = 0
        threat_range = 100000
        air_weapon_dist = 100000

    class SAM_Avenger_M1097(unittype.VehicleType):
        id = "M1097 Avenger"
        name = "SAM Avenger M1097"
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

    class SAM_Patriot_ICC(unittype.VehicleType):
        id = "Patriot cp"
        name = "SAM Patriot ICC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Roland_ADS(unittype.VehicleType):
        id = "Roland ADS"
        name = "SAM Roland ADS"
        detection_range = 12000
        threat_range = 8000
        air_weapon_dist = 8000

    class SAM_SA_10_S_300PS_CP_54K6(unittype.VehicleType):
        id = "S-300PS 54K6 cp"
        name = "SAM SA-10 S-300PS CP 54K6"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Stinger_MANPADS(unittype.VehicleType):
        id = "Soldier stinger"
        name = "Stinger MANPADS"
        detection_range = 5000
        threat_range = 4500
        air_weapon_dist = 4500

    class SAM_Stinger_comm_dsr(unittype.VehicleType):
        id = "Stinger comm dsr"
        name = "SAM Stinger comm dsr"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Stinger_comm(unittype.VehicleType):
        id = "Stinger comm"
        name = "SAM Stinger comm"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class SPAAA_ZSU_23_4_Shilka(unittype.VehicleType):
        id = "ZSU-23-4 Shilka"
        name = "SPAAA ZSU-23-4 Shilka"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Closed(unittype.VehicleType):
        id = "ZU-23 Emplacement Closed"
        name = "AAA ZU-23 Closed"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Emplacement(unittype.VehicleType):
        id = "ZU-23 Emplacement"
        name = "AAA ZU-23 Emplacement"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_on_Ural_375(unittype.VehicleType):
        id = "Ural-375 ZU-23"
        name = "AAA ZU-23 on Ural-375"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Insurgent_Closed(unittype.VehicleType):
        id = "ZU-23 Closed Insurgent"
        name = "AAA ZU-23 Insurgent Closed"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Insurgent_on_Ural_375(unittype.VehicleType):
        id = "Ural-375 ZU-23 Insurgent"
        name = "AAA ZU-23 Insurgent on Ural-375"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_ZU_23_Insurgent(unittype.VehicleType):
        id = "ZU-23 Insurgent"
        name = "AAA ZU-23 Insurgent"
        detection_range = 5000
        threat_range = 2500
        air_weapon_dist = 2500

    class SAM_SA_18_Igla_MANPADS(unittype.VehicleType):
        id = "SA-18 Igla manpad"
        name = "SAM SA-18 Igla MANPADS"
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class SAM_SA_18_Igla_comm(unittype.VehicleType):
        id = "SA-18 Igla comm"
        name = "SAM SA-18 Igla comm"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_18_Igla_S_MANPADS(unittype.VehicleType):
        id = "SA-18 Igla-S manpad"
        name = "SAM SA-18 Igla-S MANPADS"
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class SAM_SA_18_Igla_S_comm(unittype.VehicleType):
        id = "SA-18 Igla-S comm"
        name = "SAM SA-18 Igla-S comm"
        detection_range = 5000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_18_Igla_MANPADS(unittype.VehicleType):
        id = "Igla manpad INS"
        name = "SAM SA-18 Igla MANPADS"
        detection_range = 5000
        threat_range = 5200
        air_weapon_dist = 5200

    class EWR_1L13(unittype.VehicleType):
        id = "1L13 EWR"
        name = "EWR 1L13"
        detection_range = 120000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_6_Kub_STR_9S91(unittype.VehicleType):
        id = "Kub 1S91 str"
        name = "SAM SA-6 Kub STR 9S91"
        detection_range = 70000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_10_S_300PS_TR_30N6(unittype.VehicleType):
        id = "S-300PS 40B6M tr"
        name = "SAM SA-10 S-300PS TR 30N6"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_10_S_300PS_SR_5N66M(unittype.VehicleType):
        id = "S-300PS 40B6MD sr"
        name = "SAM SA-10 S-300PS SR 5N66M"
        detection_range = 60000
        threat_range = 0
        air_weapon_dist = 0

    class EWR_55G6(unittype.VehicleType):
        id = "55G6 EWR"
        name = "EWR 55G6"
        detection_range = 120000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_10_S_300PS_SR_64H6E(unittype.VehicleType):
        id = "S-300PS 64H6E sr"
        name = "SAM SA-10 S-300PS SR 64H6E"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_11_Buk_SR_9S18M1(unittype.VehicleType):
        id = "SA-11 Buk SR 9S18M1"
        name = "SAM SA-11 Buk SR 9S18M1"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class CP_9S80M1_Sborka(unittype.VehicleType):
        id = "Dog Ear radar"
        name = "CP 9S80M1 Sborka"
        detection_range = 35000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Hawk_TR_AN_MPQ_46(unittype.VehicleType):
        id = "Hawk tr"
        name = "SAM Hawk TR AN/MPQ-46"
        detection_range = 90000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Hawk_SR_AN_MPQ_50(unittype.VehicleType):
        id = "Hawk sr"
        name = "SAM Hawk SR AN/MPQ-50"
        detection_range = 90000
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class SAM_Patriot_STR_AN_MPQ_53(unittype.VehicleType):
        id = "Patriot str"
        name = "SAM Patriot STR AN/MPQ-53"
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

    class SAM_SR_P_19(unittype.VehicleType):
        id = "p-19 s-125 sr"
        name = "SAM SR P-19"
        detection_range = 160000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_Roland_EWR(unittype.VehicleType):
        id = "Roland Radar"
        name = "SAM Roland EWR"
        detection_range = 35000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_3_S_125_TR_SNR(unittype.VehicleType):
        id = "snr s-125 tr"
        name = "SAM SA-3 S-125 TR SNR"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class SAM_SA_2_LN_SM_90(unittype.VehicleType):
        id = "S_75M_Volhov"
        name = "SAM SA-2 LN SM-90"
        detection_range = 0
        threat_range = 43000
        air_weapon_dist = 43000

    class SAM_SA_2_TR_SNR_75_Fan_Song(unittype.VehicleType):
        id = "SNR_75V"
        name = "SAM SA-2 TR SNR-75 Fan Song"
        detection_range = 100000
        threat_range = 0
        air_weapon_dist = 0

    class Rapier_FSA_Launcher(unittype.VehicleType):
        id = "rapier_fsa_launcher"
        name = "Rapier FSA Launcher"
        detection_range = 30000
        threat_range = 6800
        air_weapon_dist = 6800

    class Rapier_FSA_Optical_Tracker(unittype.VehicleType):
        id = "rapier_fsa_optical_tracker_unit"
        name = "Rapier FSA Optical Tracker"
        detection_range = 20000
        threat_range = 0
        air_weapon_dist = 0

    class Rapier_FSA_Blindfire_Tracker(unittype.VehicleType):
        id = "rapier_fsa_blindfire_radar"
        name = "Rapier FSA Blindfire Tracker"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

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

    class AAA_8_8cm_Flak_18(unittype.VehicleType):
        id = "flak18"
        name = "AAA 8,8cm Flak 18"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class AAA_Flak_38(unittype.VehicleType):
        id = "flak30"
        name = "AAA Flak 38"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_8_8cm_Flak_36(unittype.VehicleType):
        id = "flak36"
        name = "AAA 8,8cm Flak 36"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class AAA_8_8cm_Flak_37(unittype.VehicleType):
        id = "flak37"
        name = "AAA 8,8cm Flak 37"
        detection_range = 0
        threat_range = 15000
        air_weapon_dist = 15000

    class AAA_Flak_Vierling_38(unittype.VehicleType):
        id = "flak38"
        name = "AAA Flak-Vierling 38"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class AAA_Kdo_G_40(unittype.VehicleType):
        id = "KDO_Mod40"
        name = "AAA Kdo.G.40"
        detection_range = 30000
        threat_range = 0
        air_weapon_dist = 0

    class Flak_Searchlight_37(unittype.VehicleType):
        id = "Flakscheinwerfer_37"
        name = "Flak Searchlight 37"
        detection_range = 8000
        threat_range = 6000
        air_weapon_dist = 0

    class Maschinensatz_33(unittype.VehicleType):
        id = "Maschinensatz_33"
        name = "Maschinensatz_33"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class AAA_8_8cm_Flak_41(unittype.VehicleType):
        id = "flak41"
        name = "AAA 8,8cm Flak 41"
        detection_range = 0
        threat_range = 20000
        air_weapon_dist = 20000

    class AAA_Bofors_40mm(unittype.VehicleType):
        id = "bofors40"
        name = "AAA Bofors 40mm"
        detection_range = 0
        threat_range = 7160
        air_weapon_dist = 7160


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

    class Armed_house(unittype.VehicleType):
        id = "houseA_arm"
        name = "Armed house"
        detection_range = 0
        threat_range = 800
        air_weapon_dist = 800

    class TACAN_Beacon__Man_Portable__TTS_3030(unittype.VehicleType):
        id = "TACAN_beacon"
        name = "TACAN Beacon (Man Portable) TTS 3030"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Bunker_with_SK_C_28_15cm_naval_gun(unittype.VehicleType):
        id = "SK_C_28_naval_gun"
        name = "Bunker with SK C/28 15cm naval gun"
        detection_range = 0
        threat_range = 20000
        air_weapon_dist = 0

    class Fire_control_bunker(unittype.VehicleType):
        id = "fire_control"
        name = "Fire control bunker"
        detection_range = 0
        threat_range = 1100
        air_weapon_dist = 1100


class Unarmed:

    class GPU_APA_5D_on_Ural_4320(unittype.VehicleType):
        id = "Ural-4320 APA-5D"
        name = "GPU APA-5D on Ural-4320"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Fuel_Truck_ATMZ_5(unittype.VehicleType):
        id = "ATMZ-5"
        name = "Fuel Truck ATMZ-5"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Fuel_Truck_ATZ_10(unittype.VehicleType):
        id = "ATZ-10"
        name = "Fuel Truck ATZ-10"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_GAZ_3307(unittype.VehicleType):
        id = "GAZ-3307"
        name = "Transport GAZ-3307"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_GAZ_3308(unittype.VehicleType):
        id = "GAZ-3308"
        name = "Transport GAZ-3308"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_GAZ_66(unittype.VehicleType):
        id = "GAZ-66"
        name = "Transport GAZ-66"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tanker_M978_HEMTT(unittype.VehicleType):
        id = "M978 HEMTT Tanker"
        name = "Tanker M978 HEMTT"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class HEMTT_TFFT(unittype.VehicleType):
        id = "HEMTT TFFT"
        name = "HEMTT TFFT"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_IKARUS_280(unittype.VehicleType):
        id = "IKARUS Bus"
        name = "Transport IKARUS-280"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_KAMAZ_43101(unittype.VehicleType):
        id = "KAMAZ Truck"
        name = "Transport KAMAZ-43101"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_LAZ_695(unittype.VehicleType):
        id = "LAZ Bus"
        name = "Transport LAZ-695"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class APC_M1025_HMMWV(unittype.VehicleType):
        id = "Hummer"
        name = "APC M1025 HMMWV"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0
        eplrs = True

    class Transport_M818(unittype.VehicleType):
        id = "M 818"
        name = "Transport M818"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_MAZ_6303(unittype.VehicleType):
        id = "MAZ-6303"
        name = "Transport MAZ-6303"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class CP_Predator_GCS(unittype.VehicleType):
        id = "Predator GCS"
        name = "CP Predator GCS"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class CP_Predator_TrojanSpirit(unittype.VehicleType):
        id = "Predator TrojanSpirit"
        name = "CP Predator TrojanSpirit"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Suidae(unittype.VehicleType):
        id = "Suidae"
        name = "Suidae"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class APC_Tigr_233036(unittype.VehicleType):
        id = "Tigr_233036"
        name = "APC Tigr 233036"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_ZIU_9(unittype.VehicleType):
        id = "Trolley bus"
        name = "Transport ZIU-9"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_UAZ_469(unittype.VehicleType):
        id = "UAZ-469"
        name = "Transport UAZ-469"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_fire_engine_Ural_ATsP_6(unittype.VehicleType):
        id = "Ural ATsP-6"
        name = "Transport fire-engine Ural ATsP-6"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_Ural_4320_31_Armored(unittype.VehicleType):
        id = "Ural-4320-31"
        name = "Transport Ural-4320-31 Armored"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_Ural_4320T(unittype.VehicleType):
        id = "Ural-4320T"
        name = "Transport Ural-4320T"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class CP_Ural_375_PBU(unittype.VehicleType):
        id = "Ural-375 PBU"
        name = "CP Ural-375 PBU"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_Ural_375(unittype.VehicleType):
        id = "Ural-375"
        name = "Transport Ural-375"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_VAZ_2109(unittype.VehicleType):
        id = "VAZ Car"
        name = "Transport VAZ-2109"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class GPU_APA_80_on_ZiL_131(unittype.VehicleType):
        id = "ZiL-131 APA-80"
        name = "GPU APA-80 on ZiL-131"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class CP_SKP_11_ATC_Mobile_Command_Post(unittype.VehicleType):
        id = "SKP-11"
        name = "CP SKP-11 ATC Mobile Command Post"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_ZIL_131_KUNG(unittype.VehicleType):
        id = "ZIL-131 KUNG"
        name = "Transport ZIL-131 KUNG"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_ZIL_4331(unittype.VehicleType):
        id = "ZIL-4331"
        name = "Transport ZIL-4331"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Transport_KrAZ_6322(unittype.VehicleType):
        id = "KrAZ6322"
        name = "Transport KrAZ-6322"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Land_Rover_101_FC(unittype.VehicleType):
        id = "Land_Rover_101_FC"
        name = "Land Rover 101 FC"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Land_Rover_109_S3(unittype.VehicleType):
        id = "Land_Rover_109_S3"
        name = "Land Rover 109 S3"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Kübelwagen_82(unittype.VehicleType):
        id = "Kubelwagen_82"
        name = "Kübelwagen 82"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Blitz_3_6_6700A(unittype.VehicleType):
        id = "Blitz_36-6700A"
        name = "Blitz 3.6-6700A"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Sd_Kfz_2(unittype.VehicleType):
        id = "Sd_Kfz_2"
        name = "Sd.Kfz.2"
        detection_range = 0
        threat_range = None
        air_weapon_dist = 0

    class Sd_Kfz_7(unittype.VehicleType):
        id = "Sd_Kfz_7"
        name = "Sd.Kfz.7"
        detection_range = 0
        threat_range = None
        air_weapon_dist = 0

    class Horch_901_typ_40(unittype.VehicleType):
        id = "Horch_901_typ_40_kfz_21"
        name = "Horch 901 typ 40"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Bedford_MWD(unittype.VehicleType):
        id = "Bedford_MWD"
        name = "Bedford MWD"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class CCKW_353(unittype.VehicleType):
        id = "CCKW_353"
        name = "CCKW 353"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Willys_MB(unittype.VehicleType):
        id = "Willys_MB"
        name = "Willys MB"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0


class Armor:

    class APC_AAV_7(unittype.VehicleType):
        id = "AAV7"
        name = "APC AAV-7"
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

    class ARV_BRDM_2(unittype.VehicleType):
        id = "BRDM-2"
        name = "ARV BRDM-2"
        detection_range = 0
        threat_range = 1600
        air_weapon_dist = 1600

    class APC_BTR_80(unittype.VehicleType):
        id = "BTR-80"
        name = "APC BTR-80"
        detection_range = 0
        threat_range = 1600
        air_weapon_dist = 1600

    class ARV_BTR_RD(unittype.VehicleType):
        id = "BTR_D"
        name = "ARV BTR-RD"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 1000

    class APC_Cobra(unittype.VehicleType):
        id = "Cobra"
        name = "APC Cobra"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200

    class IFV_LAV_25(unittype.VehicleType):
        id = "LAV-25"
        name = "IFV LAV-25"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 2500

    class APC_M1043_HMMWV_Armament(unittype.VehicleType):
        id = "M1043 HMMWV Armament"
        name = "APC M1043 HMMWV Armament"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 1200
        eplrs = True

    class ATGM_M1045_HMMWV_TOW(unittype.VehicleType):
        id = "M1045 HMMWV TOW"
        name = "ATGM M1045 HMMWV TOW"
        detection_range = 0
        threat_range = 3800
        air_weapon_dist = 0
        eplrs = True

    class APC_M1126_Stryker_ICV(unittype.VehicleType):
        id = "M1126 Stryker ICV"
        name = "APC M1126 Stryker ICV"
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

    class ATGM_M1134_Stryker(unittype.VehicleType):
        id = "M1134 Stryker ATGM"
        name = "ATGM M1134 Stryker"
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

    class IFV_MCV_80(unittype.VehicleType):
        id = "MCV-80"
        name = "IFV MCV-80"
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

    class TPz_Fuchs(unittype.VehicleType):
        id = "TPZ"
        name = "TPz Fuchs"
        detection_range = 0
        threat_range = 1000
        air_weapon_dist = 1000

    class FDDM_Grad(unittype.VehicleType):
        id = "Grad_FDDM"
        name = "FDDM Grad"
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
        name = "MBT Leopard-2"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1500

    class MBT_M60A3_Patton(unittype.VehicleType):
        id = "M-60"
        name = "MBT M60A3 Patton"
        detection_range = 0
        threat_range = 2500
        air_weapon_dist = 1500

    class SPG_M1128_Stryker_MGS(unittype.VehicleType):
        id = "M1128 Stryker MGS"
        name = "SPG M1128 Stryker MGS"
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

    class MBT_Merkava_Mk__4(unittype.VehicleType):
        id = "Merkava_Mk4"
        name = "MBT Merkava Mk. 4"
        detection_range = 0
        threat_range = 3500
        air_weapon_dist = 1200

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

    class HT_Pz_Kpfw_VI_Ausf__B__Tiger_II(unittype.VehicleType):
        id = "Tiger_II_H"
        name = "HT Pz.Kpfw.VI Ausf. B 'Tiger II'"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class MT_Pz_Kpfw_V_Panther_Ausf_G(unittype.VehicleType):
        id = "Pz_V_Panther_G"
        name = "MT Pz.Kpfw.V Panther Ausf.G"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class MT_Pz_Kpfw_IV_Ausf_H(unittype.VehicleType):
        id = "Pz_IV_H"
        name = "MT Pz.Kpfw.IV Ausf.H"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class TD_Jagdpanther_G1(unittype.VehicleType):
        id = "Jagdpanther_G1"
        name = "TD Jagdpanther G1"
        detection_range = 0
        threat_range = 5000
        air_weapon_dist = 0

    class TD_Jagdpanzer_IV(unittype.VehicleType):
        id = "JagdPz_IV"
        name = "TD Jagdpanzer IV"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class StuG_IV(unittype.VehicleType):
        id = "Stug_IV"
        name = "StuG IV"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class IFV_Sd_Kfz_234_2_Puma(unittype.VehicleType):
        id = "Sd_Kfz_234_2_Puma"
        name = "IFV Sd.Kfz.234/2 Puma"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0

    class APC_Sd_Kfz_251(unittype.VehicleType):
        id = "Sd_Kfz_251"
        name = "APC Sd.Kfz.251"
        detection_range = 0
        threat_range = 1100
        air_weapon_dist = 0

    class StuG_III_Ausf__G(unittype.VehicleType):
        id = "Stug_III"
        name = "StuG III Ausf. G"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class Sd_Kfz_184_Elefant(unittype.VehicleType):
        id = "Elefant_SdKfz_184"
        name = "Sd.Kfz.184 Elefant"
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

    class ST_Centaur_IV(unittype.VehicleType):
        id = "Centaur_IV"
        name = "ST Centaur IV"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class HIT_Churchill_VII(unittype.VehicleType):
        id = "Churchill_VII"
        name = "HIT Churchill_VII"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class MT_M4_Sherman(unittype.VehicleType):
        id = "M4_Sherman"
        name = "MT M4 Sherman"
        detection_range = 0
        threat_range = 3000
        air_weapon_dist = 0

    class M30_Cargo_Carrier(unittype.VehicleType):
        id = "M30_CC"
        name = "M30 Cargo Carrier"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0

    class APC_M2A1(unittype.VehicleType):
        id = "M2A1_halftrack"
        name = "APC M2A1"
        detection_range = 0
        threat_range = 1200
        air_weapon_dist = 0

    class TD_M10_GMC(unittype.VehicleType):
        id = "M10_GMC"
        name = "TD M10 GMC"
        detection_range = 0
        threat_range = 6000
        air_weapon_dist = 0

    class LAC_M8_Greyhound(unittype.VehicleType):
        id = "M8_Greyhound"
        name = "LAC M8 Greyhound"
        detection_range = 0
        threat_range = 2000
        air_weapon_dist = 0


class MissilesSS:

    class SRBM_SS_1C_Scud_B_9K72_LN_9P117M(unittype.VehicleType):
        id = "Scud_B"
        name = "SRBM SS-1C Scud-B 9K72 LN 9P117M"
        detection_range = 0
        threat_range = 460000
        air_weapon_dist = 460000

    class SS_N_2_Silkworm(unittype.VehicleType):
        id = "hy_launcher"
        name = "SS-N-2 Silkworm"
        detection_range = 100000
        threat_range = 100000
        air_weapon_dist = 100000

    class Silkworm_Radar(unittype.VehicleType):
        id = "Silkworm_SR"
        name = "Silkworm Radar"
        detection_range = 200000
        threat_range = 0
        air_weapon_dist = 0

    class V_1_ramp(unittype.VehicleType):
        id = "v1_launcher"
        name = "V-1 ramp"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0


class Locomotive:

    class Electric_locomotive_VL80(unittype.VehicleType):
        id = "Electric locomotive"
        name = "Electric locomotive VL80"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Locomotive_CHME3T(unittype.VehicleType):
        id = "Locomotive"
        name = "Locomotive CHME3T"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class ES44AH(unittype.VehicleType):
        id = "ES44AH"
        name = "ES44AH"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class DRG_Class_86(unittype.VehicleType):
        id = "DRG_Class_86"
        name = "DRG Class 86"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0


class Carriage:

    class Coach_for_cargo(unittype.VehicleType):
        id = "Coach cargo"
        name = "Coach for cargo"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_for_open_cargo(unittype.VehicleType):
        id = "Coach cargo open"
        name = "Coach for open cargo"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_a_tank_blue(unittype.VehicleType):
        id = "Coach a tank blue"
        name = "Coach a tank blue"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_a_tank_yellow(unittype.VehicleType):
        id = "Coach a tank yellow"
        name = "Coach a tank yellow"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_for_passengers(unittype.VehicleType):
        id = "Coach a passenger"
        name = "Coach for passengers"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Coach_flatbed(unittype.VehicleType):
        id = "Coach a platform"
        name = "Coach flatbed"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Boxcartrinity(unittype.VehicleType):
        id = "Boxcartrinity"
        name = "Boxcartrinity"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Tankcartrinity(unittype.VehicleType):
        id = "Tankcartrinity"
        name = "Tankcartrinity"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class Wellcarnsc(unittype.VehicleType):
        id = "Wellcarnsc"
        name = "Wellcarnsc"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class DR_50_ton_flat_wagon(unittype.VehicleType):
        id = "DR_50Ton_Flat_Wagon"
        name = "DR 50-ton flat wagon"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class German_covered_wagon_G10(unittype.VehicleType):
        id = "German_covered_wagon_G10"
        name = "German covered wagon G10"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

    class German_tank_wagon(unittype.VehicleType):
        id = "German_tank_wagon"
        name = "German tank wagon"
        detection_range = 0
        threat_range = 0
        air_weapon_dist = 0

vehicle_map = {
    "2B11 mortar": Artillery._2B11_mortar,
    "SAU Gvozdika": Artillery.SPH_2S1_Gvozdika,
    "SAU Msta": Artillery.SPH_2S19_Msta,
    "SAU Akatsia": Artillery.SPH_2S3_Akatsia,
    "SAU 2-C9": Artillery.SPH_2S9_Nona,
    "M-109": Artillery.SPH_M109_Paladin,
    "SpGH_Dana": Artillery.SpGH_Dana,
    "AAV7": Armor.APC_AAV_7,
    "BMD-1": Armor.IFV_BMD_1,
    "BMP-1": Armor.IFV_BMP_1,
    "BMP-2": Armor.IFV_BMP_2,
    "BMP-3": Armor.IFV_BMP_3,
    "BRDM-2": Armor.ARV_BRDM_2,
    "BTR-80": Armor.APC_BTR_80,
    "BTR_D": Armor.ARV_BTR_RD,
    "Cobra": Armor.APC_Cobra,
    "LAV-25": Armor.IFV_LAV_25,
    "M1043 HMMWV Armament": Armor.APC_M1043_HMMWV_Armament,
    "M1045 HMMWV TOW": Armor.ATGM_M1045_HMMWV_TOW,
    "M1126 Stryker ICV": Armor.APC_M1126_Stryker_ICV,
    "M-113": Armor.APC_M113,
    "M1134 Stryker ATGM": Armor.ATGM_M1134_Stryker,
    "M-2 Bradley": Armor.IFV_M2A2_Bradley,
    "MCV-80": Armor.IFV_MCV_80,
    "MTLB": Armor.APC_MTLB,
    "Marder": Armor.IFV_Marder,
    "TPZ": Armor.TPz_Fuchs,
    "Grad_FDDM": Armor.FDDM_Grad,
    "Bunker": Fortification.Bunker_2,
    "Paratrooper RPG-16": Infantry.Paratrooper_RPG_16,
    "Paratrooper AKS-74": Infantry.Paratrooper_AKS,
    "Infantry AK Ins": Infantry.Infantry_Soldier_Insurgents,
    "Sandbox": Fortification.Bunker_1,
    "Soldier AK": Infantry.Soldier_AK,
    "Infantry AK": Infantry.Infantry_Soldier_Rus,
    "Soldier M249": Infantry.Soldier_M249,
    "Soldier M4": Infantry.Infantry_M4,
    "Soldier M4 GRG": Infantry.Georgian_soldier_with_M4,
    "Soldier RPG": Infantry.Soldier_RPG,
    "MLRS FDDM": Artillery.MLRS_FDDM,
    "Grad-URAL": Artillery.MLRS_BM_21_Grad,
    "Uragan_BM-27": Artillery.MLRS_9K57_Uragan_BM_27,
    "Smerch": Artillery.MLRS_9A52_Smerch,
    "Smerch_HE": Artillery.MLRS_9A52_Smerch_HE,
    "MLRS": Artillery.MLRS_M270,
    "2S6 Tunguska": AirDefence.SAM_SA_19_Tunguska_2S6,
    "Kub 2P25 ln": AirDefence.SAM_SA_6_Kub_LN_2P25,
    "5p73 s-125 ln": AirDefence.SAM_SA_3_S_125_LN_5P73,
    "S-300PS 5P85C ln": AirDefence.SAM_SA_10_S_300PS_LN_5P85C,
    "S-300PS 5P85D ln": AirDefence.SAM_SA_10_S_300PS_LN_5P85D,
    "SA-11 Buk LN 9A310M1": AirDefence.SAM_SA_11_Buk_LN_9A310M1,
    "Osa 9A33 ln": AirDefence.SAM_SA_8_Osa_9A33,
    "Tor 9A331": AirDefence.SAM_SA_15_Tor_9A331,
    "Strela-10M3": AirDefence.SAM_SA_13_Strela_10M3_9A35M3,
    "Strela-1 9P31": AirDefence.SAM_SA_9_Strela_1_9P31,
    "SA-11 Buk CC 9S470M1": AirDefence.SAM_SA_11_Buk_CC_9S470M1,
    "SA-8 Osa LD 9T217": AirDefence.SAM_SA_8_Osa_LD_9T217,
    "Patriot AMG": AirDefence.SAM_Patriot_AMG_AN_MRC_137,
    "Patriot ECS": AirDefence.SAM_Patriot_ECS_AN_MSQ_104,
    "Gepard": AirDefence.SPAAA_Gepard,
    "Hawk pcp": AirDefence.SAM_Hawk_PCP,
    "Vulcan": AirDefence.AAA_Vulcan_M163,
    "Hawk ln": AirDefence.SAM_Hawk_LN_M192,
    "M48 Chaparral": AirDefence.SAM_Chaparral_M48,
    "M6 Linebacker": AirDefence.SAM_Linebacker_M6,
    "Patriot ln": AirDefence.SAM_Patriot_LN_M901,
    "M1097 Avenger": AirDefence.SAM_Avenger_M1097,
    "Patriot EPP": AirDefence.SAM_Patriot_EPP_III,
    "Patriot cp": AirDefence.SAM_Patriot_ICC,
    "Roland ADS": AirDefence.SAM_Roland_ADS,
    "S-300PS 54K6 cp": AirDefence.SAM_SA_10_S_300PS_CP_54K6,
    "Soldier stinger": AirDefence.Stinger_MANPADS,
    "Stinger comm dsr": AirDefence.SAM_Stinger_comm_dsr,
    "Stinger comm": AirDefence.SAM_Stinger_comm,
    "ZSU-23-4 Shilka": AirDefence.SPAAA_ZSU_23_4_Shilka,
    "ZU-23 Emplacement Closed": AirDefence.AAA_ZU_23_Closed,
    "ZU-23 Emplacement": AirDefence.AAA_ZU_23_Emplacement,
    "Ural-375 ZU-23": AirDefence.AAA_ZU_23_on_Ural_375,
    "ZU-23 Closed Insurgent": AirDefence.AAA_ZU_23_Insurgent_Closed,
    "Ural-375 ZU-23 Insurgent": AirDefence.AAA_ZU_23_Insurgent_on_Ural_375,
    "ZU-23 Insurgent": AirDefence.AAA_ZU_23_Insurgent,
    "SA-18 Igla manpad": AirDefence.SAM_SA_18_Igla_MANPADS,
    "SA-18 Igla comm": AirDefence.SAM_SA_18_Igla_comm,
    "SA-18 Igla-S manpad": AirDefence.SAM_SA_18_Igla_S_MANPADS,
    "SA-18 Igla-S comm": AirDefence.SAM_SA_18_Igla_S_comm,
    "Igla manpad INS": AirDefence.SAM_SA_18_Igla_MANPADS,
    "1L13 EWR": AirDefence.EWR_1L13,
    "Kub 1S91 str": AirDefence.SAM_SA_6_Kub_STR_9S91,
    "S-300PS 40B6M tr": AirDefence.SAM_SA_10_S_300PS_TR_30N6,
    "S-300PS 40B6MD sr": AirDefence.SAM_SA_10_S_300PS_SR_5N66M,
    "55G6 EWR": AirDefence.EWR_55G6,
    "S-300PS 64H6E sr": AirDefence.SAM_SA_10_S_300PS_SR_64H6E,
    "SA-11 Buk SR 9S18M1": AirDefence.SAM_SA_11_Buk_SR_9S18M1,
    "Dog Ear radar": AirDefence.CP_9S80M1_Sborka,
    "Hawk tr": AirDefence.SAM_Hawk_TR_AN_MPQ_46,
    "Hawk sr": AirDefence.SAM_Hawk_SR_AN_MPQ_50,
    "Patriot str": AirDefence.SAM_Patriot_STR_AN_MPQ_53,
    "Hawk cwar": AirDefence.SAM_Hawk_CWAR_AN_MPQ_55,
    "p-19 s-125 sr": AirDefence.SAM_SR_P_19,
    "Roland Radar": AirDefence.SAM_Roland_EWR,
    "snr s-125 tr": AirDefence.SAM_SA_3_S_125_TR_SNR,
    "house1arm": Fortification.Barracks_armed,
    "house2arm": Fortification.Watch_tower_armed,
    "outpost_road": Fortification.Road_outpost,
    "outpost": Fortification.Outpost,
    "houseA_arm": Fortification.Armed_house,
    "TACAN_beacon": Fortification.TACAN_Beacon__Man_Portable__TTS_3030,
    "Challenger2": Armor.MBT_Challenger_II,
    "Leclerc": Armor.MBT_Leclerc,
    "Leopard-2": Armor.MBT_Leopard_2,
    "M-60": Armor.MBT_M60A3_Patton,
    "M1128 Stryker MGS": Armor.SPG_M1128_Stryker_MGS,
    "M-1 Abrams": Armor.MBT_M1A2_Abrams,
    "T-55": Armor.MBT_T_55,
    "T-72B": Armor.MBT_T_72B,
    "T-80UD": Armor.MBT_T_80U,
    "T-90": Armor.MBT_T_90,
    "Leopard1A3": Armor.MBT_Leopard_1A3,
    "Merkava_Mk4": Armor.MBT_Merkava_Mk__4,
    "Ural-4320 APA-5D": Unarmed.GPU_APA_5D_on_Ural_4320,
    "ATMZ-5": Unarmed.Fuel_Truck_ATMZ_5,
    "ATZ-10": Unarmed.Fuel_Truck_ATZ_10,
    "GAZ-3307": Unarmed.Transport_GAZ_3307,
    "GAZ-3308": Unarmed.Transport_GAZ_3308,
    "GAZ-66": Unarmed.Transport_GAZ_66,
    "M978 HEMTT Tanker": Unarmed.Tanker_M978_HEMTT,
    "HEMTT TFFT": Unarmed.HEMTT_TFFT,
    "IKARUS Bus": Unarmed.Transport_IKARUS_280,
    "KAMAZ Truck": Unarmed.Transport_KAMAZ_43101,
    "LAZ Bus": Unarmed.Transport_LAZ_695,
    "Hummer": Unarmed.APC_M1025_HMMWV,
    "M 818": Unarmed.Transport_M818,
    "MAZ-6303": Unarmed.Transport_MAZ_6303,
    "Predator GCS": Unarmed.CP_Predator_GCS,
    "Predator TrojanSpirit": Unarmed.CP_Predator_TrojanSpirit,
    "Suidae": Unarmed.Suidae,
    "Tigr_233036": Unarmed.APC_Tigr_233036,
    "Trolley bus": Unarmed.Transport_ZIU_9,
    "UAZ-469": Unarmed.Transport_UAZ_469,
    "Ural ATsP-6": Unarmed.Transport_fire_engine_Ural_ATsP_6,
    "Ural-4320-31": Unarmed.Transport_Ural_4320_31_Armored,
    "Ural-4320T": Unarmed.Transport_Ural_4320T,
    "Ural-375 PBU": Unarmed.CP_Ural_375_PBU,
    "Ural-375": Unarmed.Transport_Ural_375,
    "VAZ Car": Unarmed.Transport_VAZ_2109,
    "ZiL-131 APA-80": Unarmed.GPU_APA_80_on_ZiL_131,
    "SKP-11": Unarmed.CP_SKP_11_ATC_Mobile_Command_Post,
    "ZIL-131 KUNG": Unarmed.Transport_ZIL_131_KUNG,
    "ZIL-4331": Unarmed.Transport_ZIL_4331,
    "KrAZ6322": Unarmed.Transport_KrAZ_6322,
    "Electric locomotive": Locomotive.Electric_locomotive_VL80,
    "Locomotive": Locomotive.Locomotive_CHME3T,
    "Coach cargo": Carriage.Coach_for_cargo,
    "Coach cargo open": Carriage.Coach_for_open_cargo,
    "Coach a tank blue": Carriage.Coach_a_tank_blue,
    "Coach a tank yellow": Carriage.Coach_a_tank_yellow,
    "Coach a passenger": Carriage.Coach_for_passengers,
    "Coach a platform": Carriage.Coach_flatbed,
    "Scud_B": MissilesSS.SRBM_SS_1C_Scud_B_9K72_LN_9P117M,
    "S_75M_Volhov": AirDefence.SAM_SA_2_LN_SM_90,
    "SNR_75V": AirDefence.SAM_SA_2_TR_SNR_75_Fan_Song,
    "rapier_fsa_launcher": AirDefence.Rapier_FSA_Launcher,
    "rapier_fsa_optical_tracker_unit": AirDefence.Rapier_FSA_Optical_Tracker,
    "rapier_fsa_blindfire_radar": AirDefence.Rapier_FSA_Blindfire_Tracker,
    "Land_Rover_101_FC": Unarmed.Land_Rover_101_FC,
    "Land_Rover_109_S3": Unarmed.Land_Rover_109_S3,
    "hy_launcher": MissilesSS.SS_N_2_Silkworm,
    "Silkworm_SR": MissilesSS.Silkworm_Radar,
    "ES44AH": Locomotive.ES44AH,
    "Boxcartrinity": Carriage.Boxcartrinity,
    "Tankcartrinity": Carriage.Tankcartrinity,
    "Wellcarnsc": Carriage.Wellcarnsc,
    "ZTZ96B": Armor.ZTZ_96B,
    "ZBD04A": Armor.ZBD_04A,
    "HQ-7_LN_SP": AirDefence.HQ_7_Self_Propelled_LN,
    "HQ-7_STR_SP": AirDefence.HQ_7_Self_Propelled_STR,
    "Kubelwagen_82": Unarmed.Kübelwagen_82,
    "Blitz_36-6700A": Unarmed.Blitz_3_6_6700A,
    "Sd_Kfz_2": Unarmed.Sd_Kfz_2,
    "Sd_Kfz_7": Unarmed.Sd_Kfz_7,
    "Horch_901_typ_40_kfz_21": Unarmed.Horch_901_typ_40,
    "Tiger_I": Armor.HT_Pz_Kpfw_VI_Tiger_I,
    "Tiger_II_H": Armor.HT_Pz_Kpfw_VI_Ausf__B__Tiger_II,
    "Pz_V_Panther_G": Armor.MT_Pz_Kpfw_V_Panther_Ausf_G,
    "Pz_IV_H": Armor.MT_Pz_Kpfw_IV_Ausf_H,
    "Jagdpanther_G1": Armor.TD_Jagdpanther_G1,
    "JagdPz_IV": Armor.TD_Jagdpanzer_IV,
    "Stug_IV": Armor.StuG_IV,
    "SturmPzIV": Artillery.Sturmpanzer_IV_Brummbär,
    "Sd_Kfz_234_2_Puma": Armor.IFV_Sd_Kfz_234_2_Puma,
    "Sd_Kfz_251": Armor.APC_Sd_Kfz_251,
    "flak18": AirDefence.AAA_8_8cm_Flak_18,
    "flak30": AirDefence.AAA_Flak_38,
    "flak36": AirDefence.AAA_8_8cm_Flak_36,
    "flak37": AirDefence.AAA_8_8cm_Flak_37,
    "flak38": AirDefence.AAA_Flak_Vierling_38,
    "KDO_Mod40": AirDefence.AAA_Kdo_G_40,
    "Flakscheinwerfer_37": AirDefence.Flak_Searchlight_37,
    "Maschinensatz_33": AirDefence.Maschinensatz_33,
    "soldier_mauser98": Infantry.Infantry_Mauser_98,
    "SK_C_28_naval_gun": Fortification.Bunker_with_SK_C_28_15cm_naval_gun,
    "fire_control": Fortification.Fire_control_bunker,
    "Stug_III": Armor.StuG_III_Ausf__G,
    "Elefant_SdKfz_184": Armor.Sd_Kfz_184_Elefant,
    "flak41": AirDefence.AAA_8_8cm_Flak_41,
    "v1_launcher": MissilesSS.V_1_ramp,
    "Bedford_MWD": Unarmed.Bedford_MWD,
    "Cromwell_IV": Armor.CT_Cromwell_IV,
    "M4A4_Sherman_FF": Armor.MT_M4A4_Sherman_Firefly,
    "bofors40": AirDefence.AAA_Bofors_40mm,
    "soldier_wwii_br_01": Infantry.Infantry_SMLE_No_4_Mk_1,
    "Centaur_IV": Armor.ST_Centaur_IV,
    "Churchill_VII": Armor.HIT_Churchill_VII,
    "CCKW_353": Unarmed.CCKW_353,
    "Willys_MB": Unarmed.Willys_MB,
    "M4_Sherman": Armor.MT_M4_Sherman,
    "M12_GMC": Artillery.M12_GMC,
    "M30_CC": Armor.M30_Cargo_Carrier,
    "M2A1_halftrack": Armor.APC_M2A1,
    "soldier_wwii_us": Infantry.Infantry_M1_Garand,
    "M10_GMC": Armor.TD_M10_GMC,
    "M8_Greyhound": Armor.LAC_M8_Greyhound,
    "DR_50Ton_Flat_Wagon": Carriage.DR_50_ton_flat_wagon,
    "DRG_Class_86": Locomotive.DRG_Class_86,
    "German_covered_wagon_G10": Carriage.German_covered_wagon_G10,
    "German_tank_wagon": Carriage.German_tank_wagon,
}
