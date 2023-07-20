# This file is generated from pydcs_export.lua
from typing import Any, Dict, List, Set

from dcs.weapons_data import Weapons
import dcs.task as task
from dcs.unitpropertydescription import UnitPropertyDescription
from dcs.unittype import FlyingType


class HelicopterType(FlyingType):
    helicopter = True


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

    livery_name = "MI-24V"  # from type

    class Pylon1:
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (1, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (2, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (2, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        Fuel_tank_PTB_450 = (2, Weapons.Fuel_tank_PTB_450)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (2, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        GUV_VOG = (2, Weapons.GUV_VOG)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (3, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (3, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (4, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (4, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
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
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (5, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (5, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (5, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        Fuel_tank_PTB_450 = (5, Weapons.Fuel_tank_PTB_450)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (5, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        GUV_VOG = (5, Weapons.GUV_VOG)

    class Pylon6:
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (6, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)

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

    properties = {
        "ExhaustScreen": UnitPropertyDescription(
            identifier="ExhaustScreen",
            control="checkbox",
            label="Exhaust IR suppressors",
            default=True,
        ),
        "LeftEngineResource": UnitPropertyDescription(
            identifier="LeftEngineResource",
            control="slider",
            label="Remaining srvc. life (lh engine)",
            player_only=True,
            minimum=40,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "RightEngineResource": UnitPropertyDescription(
            identifier="RightEngineResource",
            control="slider",
            label="Remaining srvc. life (rh engine)",
            player_only=True,
            minimum=40,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "AdditionalArmor": UnitPropertyDescription(
            identifier="AdditionalArmor",
            control="checkbox",
            label="Additional Armor",
            default=True,
        ),
        "CargoHalfdoor": UnitPropertyDescription(
            identifier="CargoHalfdoor",
            control="checkbox",
            label="Cargo halfdoor",
            default=True,
        ),
        "GunnersAISkill": UnitPropertyDescription(
            identifier="GunnersAISkill",
            control="slider",
            label="Gunners AI Skill",
            minimum=10,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "NetCrewControlPriority": UnitPropertyDescription(
            identifier="NetCrewControlPriority",
            control="comboList",
            label="Aircraft Control Priority",
            player_only=True,
            default=1,
            w_ctrl=150,
            values={
                0: "Pilot",
                1: "Instructor",
                -1: "Ask Always",
                -2: "Equally Responsible",
            },
        ),
        "NS430allow": UnitPropertyDescription(
            identifier="NS430allow",
            control="checkbox",
            label="NS 430 allow",
            default=True,
        ),
    }

    livery_name = "MI-8MT"  # from type

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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (1, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_100___100kg_GP_Bomb_LD = (1, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100MN___100_kg_Illumination_Bomb = (1, Weapons.SAB_100MN___100_kg_Illumination_Bomb)
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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (2, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        GUV_YakB_GSHP = (2, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (2, Weapons.GUV_VOG)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100MN___100_kg_Illumination_Bomb = (2, Weapons.SAB_100MN___100_kg_Illumination_Bomb)
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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (3, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (3, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100MN___100_kg_Illumination_Bomb = (3, Weapons.SAB_100MN___100_kg_Illumination_Bomb)
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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (4, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (4, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100MN___100_kg_Illumination_Bomb = (4, Weapons.SAB_100MN___100_kg_Illumination_Bomb)
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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (5, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        GUV_YakB_GSHP = (5, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (5, Weapons.GUV_VOG)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100MN___100_kg_Illumination_Bomb = (5, Weapons.SAB_100MN___100_kg_Illumination_Bomb)
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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (6, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_100___100kg_GP_Bomb_LD = (6, Weapons.FAB_100___100kg_GP_Bomb_LD)
        SAB_100MN___100_kg_Illumination_Bomb = (6, Weapons.SAB_100MN___100_kg_Illumination_Bomb)
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

    livery_name = "MI-26"  # from type

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

    livery_name = "KA-27"  # from type

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

    livery_name = "UH-60A"  # from type

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

    livery_name = "CH-53E"  # from type

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

    livery_name = "CH-47D"  # from type

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

    livery_name = "SH-3W"  # from type

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

    livery_name = "AH-64A"  # from type

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

    livery_name = "AH-64D"  # from type

    class Pylon1:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (1, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M299___4_x_AGM_114K_Hellfire = (1, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___2_x_AGM_114K_Hellfire = (1, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___Empty_Launcher = (1, Weapons.M299___Empty_Launcher)
        M299___4_x_AGM_114L_Hellfire = (1, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114L_Hellfire__Port = (1, Weapons.M299___3_x_AGM_114L_Hellfire__Port)
        M299___2_x_AGM_114L_Hellfire = (1, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114L_Hellfire__Port = (1, Weapons.M299___1_x_AGM_114L_Hellfire__Port)

    class Pylon2:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        M299___4_x_AGM_114K_Hellfire = (2, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___2_x_AGM_114K_Hellfire = (2, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___Empty_Launcher = (2, Weapons.M299___Empty_Launcher)
        M299___4_x_AGM_114L_Hellfire = (2, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114L_Hellfire__Port = (2, Weapons.M299___3_x_AGM_114L_Hellfire__Port)
        M299___2_x_AGM_114L_Hellfire = (2, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114L_Hellfire__Port = (2, Weapons.M299___1_x_AGM_114L_Hellfire__Port)

    class Pylon3:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        M299___4_x_AGM_114K_Hellfire = (3, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (3, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (3, Weapons.M299___Empty_Launcher)
        M299___4_x_AGM_114L_Hellfire = (3, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114L_Hellfire__Starboard = (3, Weapons.M299___3_x_AGM_114L_Hellfire__Starboard)
        M299___2_x_AGM_114L_Hellfire = (3, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114L_Hellfire__Starboard = (3, Weapons.M299___1_x_AGM_114L_Hellfire__Starboard)

    class Pylon4:
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        M299___4_x_AGM_114K_Hellfire = (4, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (4, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___Empty_Launcher = (4, Weapons.M299___Empty_Launcher)
        M299___4_x_AGM_114L_Hellfire = (4, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114L_Hellfire__Starboard = (4, Weapons.M299___3_x_AGM_114L_Hellfire__Starboard)
        M299___2_x_AGM_114L_Hellfire = (4, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114L_Hellfire__Starboard = (4, Weapons.M299___1_x_AGM_114L_Hellfire__Starboard)

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

    livery_name = "AH-1W"  # from type

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

    livery_name = "SH-60B"  # from type

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

    properties = {
        "ExhaustScreen": UnitPropertyDescription(
            identifier="ExhaustScreen",
            control="checkbox",
            label="Exhaust IR suppressors",
            default=True,
        ),
        "GunnersAISkill": UnitPropertyDescription(
            identifier="GunnersAISkill",
            control="slider",
            label="Gunners AI Skill",
            minimum=10,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "EngineResource": UnitPropertyDescription(
            identifier="EngineResource",
            control="slider",
            label="Engine Resource",
            player_only=True,
            minimum=0,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "SoloFlight": UnitPropertyDescription(
            identifier="SoloFlight",
            control="checkbox",
            label="Solo Flight",
            player_only=True,
            default=False,
        ),
        "NetCrewControlPriority": UnitPropertyDescription(
            identifier="NetCrewControlPriority",
            control="comboList",
            label="Aircraft Control Priority",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "Pilot",
                1: "Copilot",
                -1: "Ask Always",
                -2: "Equally Responsible",
            },
        ),
    }

    livery_name = "UH-1H"  # from type

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

    livery_name = "MI-28N"  # from type

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        _8_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (1, Weapons._8_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (1, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (1, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (1, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (1, Weapons.Fuel_tank_PTB_450)
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (1, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
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
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (2, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (2, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (3, Weapons.Fuel_tank_PTB_450)
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (3, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (3, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (3, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (4, Weapons.Fuel_tank_PTB_450)
        B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange = (4, Weapons.B_8M1___20_x_UnGd_Rkts__80_mm_S_8TsM_SM_Orange)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        _8_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (4, Weapons._8_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (4, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)

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

    livery_name = "OH-58D"  # from type

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
    fuel_max = 1140
    max_speed = 365
    chaff = 30
    flare = 60
    charge_total = 90
    chaff_charge_size = 1
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 225

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
        "PltNVG": True,
        "CpgNVG": True,
        "FlareBurstCount": 0,
        "FlareBurstInterval": 0,
        "FlareSalvoCount": 0,
        "FlareSalvoInterval": 0,
        "FlareProgramDelay": 0,
        "OverrideIFF": 0,
        "TrackAirTargets": True,
        "NetCrewControlPriority": 0,
        "AIDisabled": False,
        "HumanOrchestra": False,
    }

    class Properties:

        class FCR_RFI_removed:
            id = "FCR_RFI_removed"

        class PltNVG:
            id = "PltNVG"

        class CpgNVG:
            id = "CpgNVG"

        class FlareBurstCount:
            id = "FlareBurstCount"

            class Values:
                x_1 = 0
                x_2 = 1
                x_3 = 2
                x_4 = 3
                x_6 = 4
                x_8 = 5

        class FlareBurstInterval:
            id = "FlareBurstInterval"

            class Values:
                x_0_1 = 0
                x_0_2 = 1
                x_0_3 = 2
                x_0_4 = 3

        class FlareSalvoCount:
            id = "FlareSalvoCount"

            class Values:
                x_1 = 0
                x_2 = 1
                x_4 = 2
                x_8 = 3
                Continuous = 4

        class FlareSalvoInterval:
            id = "FlareSalvoInterval"

            class Values:
                x_1 = 0
                x_2 = 1
                x_3 = 2
                x_4 = 3
                x_5 = 4
                x_8 = 5
                Random = 6

        class FlareProgramDelay:
            id = "FlareProgramDelay"

            class Values:
                x_1 = 0
                x_2 = 1
                x_3 = 2
                x_4 = 3

        class OverrideIFF:
            id = "OverrideIFF"

            class Values:
                Auto = 0
                Simple = 1
                Label_Only = 2
                Realistic = 3

        class TrackAirTargets:
            id = "TrackAirTargets"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                CPG = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class AIDisabled:
            id = "AIDisabled"

        class HumanOrchestra:
            id = "HumanOrchestra"

    properties = {
        "FCR_RFI_removed": UnitPropertyDescription(
            identifier="FCR_RFI_removed",
            control="checkbox",
            label="FCR/RFI removed",
            default=True,
            weight_when_on=-237.23,
        ),
        "PltNVG": UnitPropertyDescription(
            identifier="PltNVG",
            control="checkbox",
            label="Allow Plt NVG",
            default=True,
        ),
        "CpgNVG": UnitPropertyDescription(
            identifier="CpgNVG",
            control="checkbox",
            label="Allow Cpg NVG",
            default=True,
        ),
        "FlareBurstCount": UnitPropertyDescription(
            identifier="FlareBurstCount",
            control="comboList",
            label="Flare Burst Count",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "1",
                1: "2",
                2: "3",
                3: "4",
                4: "6",
                5: "8",
            },
        ),
        "FlareBurstInterval": UnitPropertyDescription(
            identifier="FlareBurstInterval",
            control="comboList",
            label="Flare Burst Interval, [sec]",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "0.1",
                1: "0.2",
                2: "0.3",
                3: "0.4",
            },
        ),
        "FlareSalvoCount": UnitPropertyDescription(
            identifier="FlareSalvoCount",
            control="comboList",
            label="Flare Salvo Count",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "1",
                1: "2",
                2: "4",
                3: "8",
                4: "Continuous",
            },
        ),
        "FlareSalvoInterval": UnitPropertyDescription(
            identifier="FlareSalvoInterval",
            control="comboList",
            label="Flare Salvo Interval, [sec]",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "1",
                1: "2",
                2: "3",
                3: "4",
                4: "5",
                5: "8",
                6: "Random",
            },
        ),
        "FlareProgramDelay": UnitPropertyDescription(
            identifier="FlareProgramDelay",
            control="comboList",
            label="Flare Delay btw. Programs, [sec]",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "1",
                1: "2",
                2: "3",
                3: "4",
            },
        ),
        "mul_Label": UnitPropertyDescription(
            identifier="mul_Label",
            control="label",
            label="AI HELPER",
            x_lbl=150,
        ),
        "OverrideIFF": UnitPropertyDescription(
            identifier="OverrideIFF",
            control="comboList",
            label="AI IFF Detection Mode",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "Auto",
                1: "Simple",
                2: "Label Only",
                3: "Realistic",
            },
        ),
        "TrackAirTargets": UnitPropertyDescription(
            identifier="TrackAirTargets",
            control="checkbox",
            label="Track Air Targets",
            default=True,
        ),
        "mul_Label": UnitPropertyDescription(
            identifier="mul_Label",
            control="label",
            label="MULTIPLAYER",
            x_lbl=150,
        ),
        "NetCrewControlPriority": UnitPropertyDescription(
            identifier="NetCrewControlPriority",
            control="comboList",
            label="Aircraft Control Priority",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "Pilot",
                1: "CPG",
                -1: "Ask Always",
                -2: "Equally Responsible",
            },
        ),
        "AIDisabled": UnitPropertyDescription(
            identifier="AIDisabled",
            control="checkbox",
            label="AI Disabled",
            default=False,
        ),
        "HumanOrchestra": UnitPropertyDescription(
            identifier="HumanOrchestra",
            control="checkbox",
            label="Disable Multicrew",
            player_only=True,
            default=False,
        ),
    }

    livery_name = "AH-64D_BLK_II"  # from type

    class Pylon1:
        M261_MK151 = (1, Weapons.M261_MK151)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL = (1, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM = (1, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE = (1, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze = (1, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M274 = (1, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M274)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M257 = (1, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M257)
        M299___4_x_AGM_114K_Hellfire = (1, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___4_x_AGM_114L_Hellfire = (1, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___3_x_AGM_114L_Hellfire__Port = (1, Weapons.M299___3_x_AGM_114L_Hellfire__Port)
        M299___2_x_AGM_114K_Hellfire = (1, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___2_x_AGM_114L_Hellfire = (1, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (1, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___1_x_AGM_114L_Hellfire__Port = (1, Weapons.M299___1_x_AGM_114L_Hellfire__Port)
        M299___Empty_Launcher = (1, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (1, Weapons.Fuel_tank_230_gal)

    class Pylon2:
        M261_MK151 = (2, Weapons.M261_MK151)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL = (2, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM = (2, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE = (2, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze = (2, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M274__D_E___M151 = (2, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M274__D_E___M151)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M257__D_E___M151 = (2, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M257__D_E___M151)
        M299___4_x_AGM_114K_Hellfire = (2, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___4_x_AGM_114L_Hellfire = (2, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___3_x_AGM_114K_Hellfire__Port)
        M299___3_x_AGM_114L_Hellfire__Port = (2, Weapons.M299___3_x_AGM_114L_Hellfire__Port)
        M299___2_x_AGM_114K_Hellfire = (2, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___2_x_AGM_114L_Hellfire = (2, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Port = (2, Weapons.M299___1_x_AGM_114K_Hellfire__Port)
        M299___1_x_AGM_114L_Hellfire__Port = (2, Weapons.M299___1_x_AGM_114L_Hellfire__Port)
        M299___Empty_Launcher = (2, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (2, Weapons.Fuel_tank_230_gal)

    class Pylon3:
        M261_MK151 = (3, Weapons.M261_MK151)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL = (3, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM = (3, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE = (3, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze = (3, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M274__D_E___M151 = (3, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M274__D_E___M151)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M257__D_E___M151 = (3, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_C___M257__D_E___M151)
        M299___4_x_AGM_114K_Hellfire = (3, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___4_x_AGM_114L_Hellfire = (3, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___3_x_AGM_114L_Hellfire__Starboard = (3, Weapons.M299___3_x_AGM_114L_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (3, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___2_x_AGM_114L_Hellfire = (3, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Starboard = (3, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___1_x_AGM_114L_Hellfire__Starboard = (3, Weapons.M299___1_x_AGM_114L_Hellfire__Starboard)
        M299___Empty_Launcher = (3, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (3, Weapons.Fuel_tank_230_gal)

    class Pylon4:
        M261_MK151 = (4, Weapons.M261_MK151)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL = (4, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M257_IL)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM = (4, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M274_TP_SM)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE = (4, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M229_HE)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze = (4, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70_M151_HE__M433_RC_Fuze)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M274 = (4, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M274)
        M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M257 = (4, Weapons.M261___19_x_UnGd_Rkts__70_mm_Hydra_70__Pod_Zones_A_B___M151__E___M257)
        M299___4_x_AGM_114K_Hellfire = (4, Weapons.M299___4_x_AGM_114K_Hellfire)
        M299___4_x_AGM_114L_Hellfire = (4, Weapons.M299___4_x_AGM_114L_Hellfire)
        M299___3_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___3_x_AGM_114K_Hellfire__Starboard)
        M299___3_x_AGM_114L_Hellfire__Starboard = (4, Weapons.M299___3_x_AGM_114L_Hellfire__Starboard)
        M299___2_x_AGM_114K_Hellfire = (4, Weapons.M299___2_x_AGM_114K_Hellfire)
        M299___2_x_AGM_114L_Hellfire = (4, Weapons.M299___2_x_AGM_114L_Hellfire)
        M299___1_x_AGM_114K_Hellfire__Starboard = (4, Weapons.M299___1_x_AGM_114K_Hellfire__Starboard)
        M299___1_x_AGM_114L_Hellfire__Starboard = (4, Weapons.M299___1_x_AGM_114L_Hellfire__Starboard)
        M299___Empty_Launcher = (4, Weapons.M299___Empty_Launcher)
        Fuel_tank_230_gal = (4, Weapons.Fuel_tank_230_gal)

    class Pylon5:
        Internal_Auxiliary_Fuel_tank_100_gal_Combo_Pak = (5, Weapons.Internal_Auxiliary_Fuel_tank_100_gal_Combo_Pak)

    pylons: Set[int] = {1, 2, 3, 4, 5}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Ka_50(HelicopterType):
    id = "Ka-50"
    flyable = True
    height = 5.6
    width = 14.4
    length = 15.84
    fuel_max = 1450
    max_speed = 350
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

    livery_name = "KA-50"  # from type

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (1, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (1, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (1, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (1, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (1, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (1, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (1, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (1, Weapons.Fuel_tank_PTB_450)
        APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag = (1, Weapons.APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (2, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (2, Weapons.Fuel_tank_PTB_450)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (3, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (3, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (3, Weapons.Fuel_tank_PTB_450)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (4, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (4, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (4, Weapons.Fuel_tank_PTB_450)
        APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag = (4, Weapons.APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag)

    pylons: Set[int] = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Ka_50_3(HelicopterType):
    id = "Ka-50_3"
    flyable = True
    height = 5.6
    width = 14.4
    length = 15.84
    fuel_max = 1450
    max_speed = 350
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

    property_defaults: Dict[str, Any] = {
        "modification": "Ka-50_3",
        "Helmet_mounted_device": 0,
        "ExhaustScreen": True,
        "Realistic_INS": 1,
        "IMU_alignment_type": 3,
    }

    class Properties:

        class modification:
            id = "modification"

            class Values:
                Version_2022 = "Ka-50_3"
                Version_2011 = "Ka-50"

        class Helmet_mounted_device:
            id = "Helmet-mounted device"

            class Values:
                Auto = 0
                HMS = 1
                NVG = 2

        class ExhaustScreen:
            id = "ExhaustScreen"

        class Realistic_INS:
            id = "Realistic INS"

            class Values:
                No_alignment_and_fixtaking_needed = 0
                No_alignment_needed_but_fixtaking = 2
                Fully_realistic = 1

        class IMU_alignment_type:
            id = "IMU alignment type"

            class Values:
                Fast = 1
                Normal = 2
                Normal_with_Gyro = 3

    properties = {
        "modification": UnitPropertyDescription(
            identifier="modification",
            control="comboList",
            label="Modification",
            default="Ka-50_3",
            w_ctrl=150,
            values={
                "Ka-50_3": "Version 2022",
                "Ka-50": "Version 2011",
            },
        ),
        "Helmet-mounted device": UnitPropertyDescription(
            identifier="Helmet-mounted device",
            control="comboList",
            label="Helmet-mounted device",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "Auto",
                1: "HMS",
                2: "NVG",
            },
        ),
        "ExhaustScreen": UnitPropertyDescription(
            identifier="ExhaustScreen",
            control="checkbox",
            label="Exhaust IR suppressors",
            default=True,
        ),
        "idPlaceHolder": UnitPropertyDescription(
            identifier="idPlaceHolder",
            control="label",
            player_only=True,
        ),
        "idLabel": UnitPropertyDescription(
            identifier="idLabel",
            control="label",
            label="INS ALIGNMENT",
            player_only=True,
            x_lbl=150,
        ),
        "Realistic INS": UnitPropertyDescription(
            identifier="Realistic INS",
            control="comboList",
            label="Realism",
            player_only=True,
            default=1,
            w_ctrl=150,
            values={
                0: "No alignment and fixtaking needed",
                2: "No alignment needed but fixtaking",
                1: "Fully realistic",
            },
        ),
        "IMU alignment type": UnitPropertyDescription(
            identifier="IMU alignment type",
            control="comboList",
            label="At Hot Start",
            player_only=True,
            default=3,
            w_ctrl=150,
            values={
                1: "Fast",
                2: "Normal",
                3: "Normal with Gyro",
            },
        ),
    }

    livery_name = "KA-50_3"  # from type

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (1, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (1, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (1, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (1, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (1, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (1, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (1, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (1, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (1, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (1, Weapons.Fuel_tank_PTB_450)
        APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag = (1, Weapons.APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (2, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (2, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (2, Weapons.Fuel_tank_PTB_450)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (3, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (3, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (3, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (3, Weapons.Fuel_tank_PTB_450)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser = (4, Weapons.Kh_25ML__AS_10_Karen____300kg__ASM__Semi_Act_Laser)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (4, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (4, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod = (4, Weapons.UPK_23_250___2_x_23mm__GSh_23L_Autocannon_Pod)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (4, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (4, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        FAB_250___250kg_GP_Bomb_LD = (4, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (4, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (4, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        Fuel_tank_PTB_450 = (4, Weapons.Fuel_tank_PTB_450)
        APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag = (4, Weapons.APU_6___6_x_9M127_1_Vikhr_M_ATGM__LOSBR__Tandem_HEAT_Frag)

    class Pylon5:
        _9S846_Strelets___2_x_9M39_Igla = (5, Weapons._9S846_Strelets___2_x_9M39_Igla)
#ERRR <CLEAN>

    class Pylon6:
        _9S846_Strelets___2_x_9M39_Igla = (6, Weapons._9S846_Strelets___2_x_9M39_Igla)
#ERRR <CLEAN>

    pylons: Set[int] = {1, 2, 3, 4, 5, 6}

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
        "LeftEngineResource": 90,
        "RightEngineResource": 90,
        "ExhaustScreen": True,
        "NS430allow": True,
        "PilotNVG": True,
        "OperatorNVG": True,
        "R60equipment": True,
        "OverrideIFF": 0,
        "GunnersAISkill": 90,
        "SimplifiedAI": False,
        "HideAngleBoxes": False,
        "TrackAirTargets": True,
        "NetCrewControlPriority": 0,
        "HumanOrchestra": False,
    }

    class Properties:

        class LeftEngineResource:
            id = "LeftEngineResource"

        class RightEngineResource:
            id = "RightEngineResource"

        class ExhaustScreen:
            id = "ExhaustScreen"

        class NS430allow:
            id = "NS430allow"

        class PilotNVG:
            id = "PilotNVG"

        class OperatorNVG:
            id = "OperatorNVG"

        class R60equipment:
            id = "R60equipment"

        class OverrideIFF:
            id = "OverrideIFF"

            class Values:
                Auto = 0
                Simple = 1
                Label_Only = 2
                Realistic = 3

        class GunnersAISkill:
            id = "GunnersAISkill"

        class SimplifiedAI:
            id = "SimplifiedAI"

        class HideAngleBoxes:
            id = "HideAngleBoxes"

        class TrackAirTargets:
            id = "TrackAirTargets"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Copilot_gunner = 1
                Ask_Always = -1
                Equally_Responsible = -2

        class HumanOrchestra:
            id = "HumanOrchestra"

    properties = {
        "LeftEngineResource": UnitPropertyDescription(
            identifier="LeftEngineResource",
            control="slider",
            label="Remaining srvc. life (lh engine)",
            player_only=True,
            minimum=40,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "RightEngineResource": UnitPropertyDescription(
            identifier="RightEngineResource",
            control="slider",
            label="Remaining srvc. life (rh engine)",
            player_only=True,
            minimum=40,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "ExhaustScreen": UnitPropertyDescription(
            identifier="ExhaustScreen",
            control="checkbox",
            label="Exhaust IR suppressors",
            default=True,
        ),
        "NS430allow": UnitPropertyDescription(
            identifier="NS430allow",
            control="checkbox",
            label="NS 430 allow",
            player_only=True,
            default=True,
        ),
        "PilotNVG": UnitPropertyDescription(
            identifier="PilotNVG",
            control="checkbox",
            label="Allow Pilots NVG",
            default=True,
        ),
        "OperatorNVG": UnitPropertyDescription(
            identifier="OperatorNVG",
            control="checkbox",
            label="Allow Operators NVG",
            default=True,
        ),
        "R60equipment": UnitPropertyDescription(
            identifier="R60equipment",
            control="checkbox",
            label="R-60 equipment",
            default=True,
        ),
        "ai_Label": UnitPropertyDescription(
            identifier="ai_Label",
            control="label",
            label="AI HELPER",
            x_lbl=150,
        ),
        "OverrideIFF": UnitPropertyDescription(
            identifier="OverrideIFF",
            control="comboList",
            label="AI IFF Detection Mode",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "Auto",
                1: "Simple",
                2: "Label Only",
                3: "Realistic",
            },
        ),
        "GunnersAISkill": UnitPropertyDescription(
            identifier="GunnersAISkill",
            control="slider",
            label="Gunners AI Skill",
            minimum=10,
            maximum=100,
            default=90,
            dimension="%",
        ),
        "SimplifiedAI": UnitPropertyDescription(
            identifier="SimplifiedAI",
            control="checkbox",
            label="Simplified AI",
            default=False,
        ),
        "HideAngleBoxes": UnitPropertyDescription(
            identifier="HideAngleBoxes",
            control="checkbox",
            label="Hide boxes in Pilot AI menu",
            player_only=True,
            default=False,
        ),
        "TrackAirTargets": UnitPropertyDescription(
            identifier="TrackAirTargets",
            control="checkbox",
            label="Track Air Targets",
            default=True,
        ),
        "mul_Label": UnitPropertyDescription(
            identifier="mul_Label",
            control="label",
            label="MULTIPLAYER",
            player_only=True,
            x_lbl=150,
        ),
        "NetCrewControlPriority": UnitPropertyDescription(
            identifier="NetCrewControlPriority",
            control="comboList",
            label="Aircraft Control Priority",
            player_only=True,
            default=0,
            w_ctrl=150,
            values={
                0: "Pilot",
                1: "Copilot-gunner",
                -1: "Ask Always",
                -2: "Equally Responsible",
            },
        ),
        "HumanOrchestra": UnitPropertyDescription(
            identifier="HumanOrchestra",
            control="checkbox",
            label="Disable Multicrew",
            player_only=True,
            default=False,
        ),
    }

    livery_name = "MI-24P"  # from type

    class Pylon1:
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (1, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT = (1, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE = (1, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag = (1, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag)
        Missile_Launcher_Rack__Empty_ = (1, Weapons.Missile_Launcher_Rack__Empty_)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        UB_32A_24_pod___32_x_S_5KO = (2, Weapons.UB_32A_24_pod___32_x_S_5KO)
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT_ = (2, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT_)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT_ = (2, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT_)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE_ = (2, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE_)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag_ = (2, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag_)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (2, Weapons.Fuel_tank_PTB_450)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (2, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (2, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (2, Weapons.FAB_100___100kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (2, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        APU_68___S_24B = (2, Weapons.APU_68___S_24B)
        GUV_VOG = (2, Weapons.GUV_VOG)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red = (2, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        UB_32A_24_pod___32_x_S_5KO = (3, Weapons.UB_32A_24_pod___32_x_S_5KO)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (3, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
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
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (4, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
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
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT_ = (5, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT_)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT_ = (5, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT_)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE_ = (5, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE_)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag_ = (5, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag_)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        Fuel_tank_PTB_450 = (5, Weapons.Fuel_tank_PTB_450)
        B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag = (5, Weapons.B_8V20A___20_x_UnGd_Rkts__80_mm_S_8KOM_HEAT_Frag)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_250_M62___250kg_GP_Bomb_LD = (5, Weapons.FAB_250_M62___250kg_GP_Bomb_LD)
        FAB_100___100kg_GP_Bomb_LD = (5, Weapons.FAB_100___100kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag = (5, Weapons.RBK_250_275___150_x_AO_1SCh__250kg_CBU_HE_Frag)
        APU_68___S_24B = (5, Weapons.APU_68___S_24B)
        GUV_VOG = (5, Weapons.GUV_VOG)
        APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red = (5, Weapons.APU_60_1M_with_R_60M__AA_8_Aphid____Infra_Red)
        APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_ = (5, Weapons.APU_60_2M_with_2_x_R_60M__AA_8_Aphid____Infra_Red_)

    class Pylon6:
        _2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT = (6, Weapons._2_x_9M114_Shturm_V__AT_6_Spiral____ATGM__SACLOS__HEAT)
        _2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT = (6, Weapons._2_x_9M120_Ataka__AT_9_Spiral_2____ATGM__SACLOS__Tandem_HEAT)
        _2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE = (6, Weapons._2_x_9M120F_Ataka__AT_9_Spiral_2____AGM__SACLOS__HE)
        _2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag = (6, Weapons._2_x_9M220O_Ataka__AT_9_Spiral_2____AAM__SACLOS__Frag)
        Missile_Launcher_Rack__Empty_ = (6, Weapons.Missile_Launcher_Rack__Empty_)

    class Pylon7:
        KORD_12_7_MI24_L = (7, Weapons.KORD_12_7_MI24_L)

    class Pylon8:
        KORD_12_7_MI24_R = (8, Weapons.KORD_12_7_MI24_R)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8}

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
        "RemoveTablet": False,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

        class RemoveTablet:
            id = "RemoveTablet"

    properties = {
        "NS430allow": UnitPropertyDescription(
            identifier="NS430allow",
            control="checkbox",
            label="NS430 Allow",
            player_only=True,
            default=True,
        ),
        "RemoveTablet": UnitPropertyDescription(
            identifier="RemoveTablet",
            control="checkbox",
            label="Remove Tablet",
            player_only=True,
            default=False,
        ),
    }

    livery_name = "SA342M"  # from type

    class Pylon1:
        HOT3_x1__ = (1, Weapons.HOT3_x1__)
        HOT3_x2__ = (1, Weapons.HOT3_x2__)

    class Pylon2:
        HOT3_x1___ = (2, Weapons.HOT3_x1___)
        HOT3_x2___ = (2, Weapons.HOT3_x2___)

    class Pylon3:
        Sand_Filter = (3, Weapons.Sand_Filter)

    class Pylon4:
        IR_Deflector = (4, Weapons.IR_Deflector)

    class Pylon5:
        Dipole_Antanna__aesthetic_ = (5, Weapons.Dipole_Antanna__aesthetic_)

    class Pylon6:
        Smoke_Generator___red_ = (6, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (6, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (6, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (6, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (6, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (6, Weapons.Smoke_Generator___orange_)

    class Pylon7:
        Smoke_Generator___red_ = (7, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (7, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (7, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (7, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (7, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (7, Weapons.Smoke_Generator___orange_)

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
        "RemoveTablet": False,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

        class SA342RemoveDoors:
            id = "SA342RemoveDoors"

        class RemoveTablet:
            id = "RemoveTablet"

    properties = {
        "NS430allow": UnitPropertyDescription(
            identifier="NS430allow",
            control="checkbox",
            label="NS430 Allow",
            player_only=True,
            default=True,
        ),
        "SA342RemoveDoors": UnitPropertyDescription(
            identifier="SA342RemoveDoors",
            control="checkbox",
            label="Remove Doors",
            player_only=False,
            default=False,
        ),
        "RemoveTablet": UnitPropertyDescription(
            identifier="RemoveTablet",
            control="checkbox",
            label="Remove Tablet",
            player_only=True,
            default=False,
        ),
    }

    livery_name = "SA342L"  # from type

    class Pylon1:
        GIAT_M621__240x_Combat_mix_4x_AP_1x_HE_ = (1, Weapons.GIAT_M621__240x_Combat_mix_4x_AP_1x_HE_)
        GIAT_M621__240x_combat_mix_4x_HE_1x_AP_ = (1, Weapons.GIAT_M621__240x_combat_mix_4x_HE_1x_AP_)
        GIAT_M621__240x_HE_ = (1, Weapons.GIAT_M621__240x_HE_)
        GIAT_M621__240x_AP_ = (1, Weapons.GIAT_M621__240x_AP_)
        GIAT_M621__240x_SAPHEI_ = (1, Weapons.GIAT_M621__240x_SAPHEI_)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_250_F1B_TP_SM = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_250_F1B_TP_SM)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_251_H1_HE = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_251_H1_HE)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_252_H1_TP = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_252_H1_TP)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_253_H1_HEAT_ = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_253_H1_HEAT_)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Red = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Red)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Yellow = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Yellow)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Green = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Green)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_256_H1_HE_Frag = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_256_H1_HE_Frag)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_257_H1_HE_Frag_Lg_Whd = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_257_H1_HE_Frag_Lg_Whd)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_259E_H1_IL = (1, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_259E_H1_IL)
        FN_HMP400__400rnds_ = (1, Weapons.FN_HMP400__400rnds_)
        FN_HMP400__200rnds_ = (1, Weapons.FN_HMP400__200rnds_)
        FN_HMP400__100rnds_ = (1, Weapons.FN_HMP400__100rnds_)
        _1xMistral_ATAM_ = (1, Weapons._1xMistral_ATAM_)
        _2xMistral_ATAM = (1, Weapons._2xMistral_ATAM)
        HOT3_x1 = (1, Weapons.HOT3_x1)
        HOT3_x2 = (1, Weapons.HOT3_x2)

    class Pylon2:
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_250_F1B_TP_SM = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_250_F1B_TP_SM)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_251_H1_HE = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_251_H1_HE)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_252_H1_TP = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_252_H1_TP)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_253_H1_HEAT_ = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_253_H1_HEAT_)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Red = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Red)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Yellow = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Yellow)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Green = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_254_H1_SM_Green)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_256_H1_HE_Frag = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_256_H1_HE_Frag)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_257_H1_HE_Frag_Lg_Whd = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_257_H1_HE_Frag_Lg_Whd)
        Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_259E_H1_IL = (2, Weapons.Telson_8___8_x_UnGd_Rkts__68_mm_SNEB_Type_259E_H1_IL)
        FN_HMP400__400rnds_ = (2, Weapons.FN_HMP400__400rnds_)
        FN_HMP400__200rnds_ = (2, Weapons.FN_HMP400__200rnds_)
        FN_HMP400__100rnds_ = (2, Weapons.FN_HMP400__100rnds_)
        _2xMistral_ATAM_ = (2, Weapons._2xMistral_ATAM_)
        _1xMistral_ATAM = (2, Weapons._1xMistral_ATAM)
        HOT3_x1_ = (2, Weapons.HOT3_x1_)
        HOT3_x2_ = (2, Weapons.HOT3_x2_)

    class Pylon3:
        Sand_Filter = (3, Weapons.Sand_Filter)

    class Pylon4:
        IR_Deflector = (4, Weapons.IR_Deflector)

    class Pylon5:
        Dipole_Antanna__aesthetic_ = (5, Weapons.Dipole_Antanna__aesthetic_)

    class Pylon6:
        Smoke_Generator___red_ = (6, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (6, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (6, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (6, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (6, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (6, Weapons.Smoke_Generator___orange_)

    class Pylon7:
        Smoke_Generator___red_ = (7, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (7, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (7, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (7, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (7, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (7, Weapons.Smoke_Generator___orange_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

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
        "RemoveTablet": False,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

        class RemoveTablet:
            id = "RemoveTablet"

    properties = {
        "NS430allow": UnitPropertyDescription(
            identifier="NS430allow",
            control="checkbox",
            label="NS430 Allow",
            player_only=True,
            default=True,
        ),
        "RemoveTablet": UnitPropertyDescription(
            identifier="RemoveTablet",
            control="checkbox",
            label="Remove Tablet",
            player_only=True,
            default=False,
        ),
    }

    livery_name = "SA342MISTRAL"  # from type
#ERRR {MBDA_MistralD}
#ERRR {MBDA_MistralG}
#ERRR {MBDA_MistralD}
#ERRR {MBDA_MistralG}

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
        "RemoveTablet": False,
    }

    class Properties:

        class NS430allow:
            id = "NS430allow"

        class RemoveTablet:
            id = "RemoveTablet"

    properties = {
        "NS430allow": UnitPropertyDescription(
            identifier="NS430allow",
            control="checkbox",
            label="NS430 Allow",
            player_only=True,
            default=True,
        ),
        "RemoveTablet": UnitPropertyDescription(
            identifier="RemoveTablet",
            control="checkbox",
            label="Remove Tablet",
            player_only=True,
            default=False,
        ),
    }

    livery_name = "SA342MINIGUN"  # from type
#ERRR {MINIGUN}

    class Pylon3:
        Sand_Filter = (3, Weapons.Sand_Filter)

    class Pylon4:
        IR_Deflector = (4, Weapons.IR_Deflector)

    class Pylon5:
        Dipole_Antanna__aesthetic_ = (5, Weapons.Dipole_Antanna__aesthetic_)

    class Pylon6:
        Smoke_Generator___red_ = (6, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (6, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (6, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (6, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (6, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (6, Weapons.Smoke_Generator___orange_)

    class Pylon7:
        Smoke_Generator___red_ = (7, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (7, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (7, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (7, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (7, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (7, Weapons.Smoke_Generator___orange_)

    pylons: Set[int] = {1, 3, 4, 5, 6, 7}

    tasks = [task.CAS, task.GroundAttack, task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.CAS


helicopter_map = {
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
    "Ka-50": Ka_50,
    "Ka-50_3": Ka_50_3,
    "Mi-24P": Mi_24P,
    "SA342M": SA342M,
    "SA342L": SA342L,
    "SA342Mistral": SA342Mistral,
    "SA342Minigun": SA342Minigun,
}
