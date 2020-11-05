import unittest

from dcs.mission import Mission
from dcs.triggers import Rules
from dcs import lua


class TriggerTests(unittest.TestCase):

    DICT_TRIGRULES = lua.loads("""trigrules = 
    {
        [1] = 
        {
            ["rules"] = 
            {
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "init",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 300,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 0,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 301,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 11,
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 302,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 12,
                }, -- end of [3]
                [4] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 303,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 13,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 304,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 14,
                }, -- end of [5]
                [6] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 305,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 15,
                }, -- end of [6]
                [7] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 306,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 16,
                }, -- end of [7]
                [8] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 307,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 17,
                }, -- end of [8]
                [9] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 308,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_value",
                    ["value"] = 18,
                }, -- end of [9]
            }, -- end of ["actions"]
            ["predicate"] = "triggerStart",
            ["colorItem"] = "0x0080ffff",
        }, -- end of [1]
        [2] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["seconds"] = 180,
                    ["predicate"] = "c_time_after",
                    ["zone"] = "",
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "Uzi1 Startup",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = "",
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 40,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
        }, -- end of [2]
        [3] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["seconds"] = 10800,
                    ["predicate"] = "c_time_after",
                    ["zone"] = 104,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "SAR End of VUL",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 104,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 47,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
        }, -- end of [3]
        [4] = 
        {
            ["rules"] = 
            {
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Spawn Template",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = "",
                    ["text"] = "DictKey_ActionText_450",
                    ["meters"] = 1000,
                    ["KeyDict_text"] = "DictKey_ActionText_450",
                    ["predicate"] = "a_do_script",
                }, -- end of [1]
                [2] = 
                {
                    ["meters"] = 1000,
                    ["file"] = "ResKey_Action_456",
                    ["predicate"] = "a_do_script_file",
                    ["zone"] = "",
                }, -- end of [2]
            }, -- end of ["actions"]
            ["predicate"] = "triggerStart",
            ["colorItem"] = "0x008080ff",
        }, -- end of [4]
        [5] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["predicate"] = "c_flag_is_true",
                    ["zone"] = "",
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["seconds"] = 7200,
                    ["predicate"] = "c_time_after",
                    ["zone"] = 312,
                }, -- end of [3]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Clear Deck",
            ["actions"] = 
            {
                [1] = 
                {
                    ["meters"] = 1000,
                    ["file"] = "ResKey_Action_457",
                    ["predicate"] = "a_do_script_file",
                    ["zone"] = "",
                }, -- end of [1]
                [2] = 
                {
                    ["file"] = "ResKey_Action_458",
                    ["meters"] = 1000,
                    ["predicate"] = "a_do_script_file",
                    ["zone"] = "",
                }, -- end of [2]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x008080ff",
        }, -- end of [5]
        [6] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 582,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 582,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 583,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["unit"] = 648,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 649,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 586,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 587,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 588,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 589,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["comment"] = "Clear the Deck - Uzi2'1",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x008080ff",
        }, -- end of [6]
        [7] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 583,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 582,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 583,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 648,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["unit"] = 649,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["unit"] = 586,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["unit"] = 587,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["unit"] = 588,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["unit"] = 589,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Clear the Deck - Uzi2'2",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x008080ff",
        }, -- end of [7]
        [8] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 648,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 582,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 583,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["unit"] = 648,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 649,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 586,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 587,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 588,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 589,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["comment"] = "Clear the Deck - Uzi2'3",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x008080ff",
        }, -- end of [8]
        [9] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 649,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 582,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 583,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 648,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["unit"] = 649,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["unit"] = 586,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["unit"] = 587,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["unit"] = 588,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["unit"] = 589,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Clear the Deck - Uzi2'4",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x008080ff",
        }, -- end of [9]
        [10] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 586,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 582,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 583,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["unit"] = 648,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 649,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 586,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 587,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 588,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 589,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["comment"] = "Clear the Deck - Colt2'1",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x008080ff",
        }, -- end of [10]
        [11] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 587,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 582,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 583,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 648,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["unit"] = 649,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["unit"] = 586,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["unit"] = 587,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["unit"] = 588,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["unit"] = 589,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Clear the Deck - Colt2'2",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x008080ff",
        }, -- end of [11]
        [12] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 588,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 582,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 583,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["unit"] = 648,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 649,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 586,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 587,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 588,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 589,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["comment"] = "Clear the Deck - Colt2'3",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x008080ff",
        }, -- end of [12]
        [13] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["altitude"] = 1000,
                    ["unit"] = 589,
                    ["predicate"] = "c_unit_altitude_higher",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 582,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 583,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zoneunit"] = 1,
                    ["unit"] = 648,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["unit"] = 649,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["unit"] = 586,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["unit"] = 587,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["unit"] = 588,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["unit"] = 589,
                    ["zoneunit"] = 1,
                    ["predicate"] = "c_unit_out_zone_unit",
                    ["zone"] = 416,
                }, -- end of [9]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Clear the Deck - Colt2'4",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["zone"] = 312,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x008080ff",
        }, -- end of [13]
        [14] = 
        {
            ["rules"] = 
            {
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "EMERGENCY - Clear Deck Radio Item Add",
            ["predicate"] = "triggerStart",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 195,
                    ["radiotext"] = "DictKey_ActionRadioText_2251",
                    ["KeyDict_radiotext"] = "DictKey_ActionRadioText_2251",
                    ["zone"] = 416,
                    ["value"] = 1,
                    ["meters"] = 1000,
                    ["predicate"] = "a_add_radio_item_for_group",
                    ["flag"] = 2,
                }, -- end of [1]
                [2] = 
                {
                    ["flag"] = 2,
                    ["predicate"] = "a_add_radio_item_for_group",
                    ["meters"] = 1000,
                    ["zone"] = 416,
                    ["group"] = 194,
                    ["KeyDict_radiotext"] = "DictKey_ActionRadioText_2428",
                    ["radiotext"] = "DictKey_ActionRadioText_2428",
                    ["value"] = 1,
                }, -- end of [2]
            }, -- end of ["actions"]
            ["colorItem"] = "0x008080ff",
        }, -- end of [14]
        [15] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 2,
                    ["predicate"] = "c_flag_is_true",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "EMERGENCY - Clear Deck",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["file"] = "ResKey_Action_2248",
                    ["meters"] = 1000,
                    ["predicate"] = "a_do_script_file",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["meters"] = 1000,
                    ["file"] = "ResKey_Action_2249",
                    ["predicate"] = "a_do_script_file",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["KeyDict_radiotext"] = "DictKey_ActionRadioText_2250",
                    ["radiotext"] = "DictKey_ActionRadioText_2250",
                    ["predicate"] = "a_remove_radio_item",
                }, -- end of [3]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x008080ff",
        }, -- end of [15]
        [16] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["group"] = 194,
                    ["predicate"] = "c_group_alive",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "STRIKE Scaler #001",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 300,
                    ["meters"] = 1000,
                    ["predicate"] = "a_inc_flag",
                    ["value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x808000ff",
        }, -- end of [16]
        [17] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["group"] = 199,
                    ["predicate"] = "c_group_alive",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "STRIKE Scaler #003",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 300,
                    ["meters"] = 1000,
                    ["predicate"] = "a_inc_flag",
                    ["value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x808000ff",
        }, -- end of [17]
        [18] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["group"] = 195,
                    ["predicate"] = "c_group_alive",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "STRIKE Scaler #002",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 300,
                    ["meters"] = 1000,
                    ["predicate"] = "a_inc_flag",
                    ["value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x808000ff",
        }, -- end of [18]
        [19] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["group"] = 201,
                    ["predicate"] = "c_group_alive",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "STRIKE Scaler #004",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["flag"] = 300,
                    ["meters"] = 1000,
                    ["predicate"] = "a_inc_flag",
                    ["value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x808000ff",
        }, -- end of [19]
        [20] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 621,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Kerman Activate",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 143,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 145,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["group"] = 144,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["group"] = 185,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [4]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [20]
        [21] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 620,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 323,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["predicate"] = "or",
                }, -- end of [3]
                [4] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 929,
                }, -- end of [4]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "SCRAMCAP Kerman #001 Start",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 143,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [21]
        [22] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["unit"] = 321,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 620,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 322,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 620,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 929,
                }, -- end of [5]
            }, -- end of ["rules"]
            ["comment"] = "SCRAMCAP Kerman #002 Start",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 145,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [22]
        [23] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 724,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "Shiraz Activate",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 148,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 149,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["group"] = 150,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["group"] = 171,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [4]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [23]
        [24] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 723,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 334,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["predicate"] = "or",
                }, -- end of [3]
                [4] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 930,
                }, -- end of [4]
            }, -- end of ["rules"]
            ["comment"] = "SCRAMCAP Shiraz #001 Start",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 148,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [24]
        [25] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["unit"] = 330,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 620,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 331,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 620,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 930,
                }, -- end of [5]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "SCRAMCAP Shiraz #002 Start",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 149,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [25]
        [26] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 827,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Kish Activate",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 151,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 152,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["group"] = 153,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["group"] = 140,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [4]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [26]
        [27] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 826,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 339,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["predicate"] = "or",
                }, -- end of [3]
                [4] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 931,
                }, -- end of [4]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "SCRAMCAP Kish #001 Start",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 151,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [27]
        [28] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["unit"] = 335,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 620,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 336,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 620,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 931,
                }, -- end of [5]
            }, -- end of ["rules"]
            ["comment"] = "SCRAMCAP Kish #002 Start",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 152,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [28]
        [29] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1034,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "Abbas Activate",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 155,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 156,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["group"] = 130,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["group"] = 131,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["group"] = 132,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["group"] = 141,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["group"] = 142,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["group"] = 207,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["group"] = 208,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["group"] = 213,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [10]
                [11] = 
                {
                    ["group"] = 214,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [11]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [29]
        [30] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1033,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 234,
                }, -- end of [2]
                [3] = 
                {
                    ["predicate"] = "or",
                }, -- end of [3]
                [4] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1137,
                }, -- end of [4]
                [5] = 
                {
                    ["unit"] = 319,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1138,
                }, -- end of [7]
                [8] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 320,
                }, -- end of [8]
                [9] = 
                {
                    ["predicate"] = "or",
                }, -- end of [9]
                [10] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1035,
                }, -- end of [10]
            }, -- end of ["rules"]
            ["comment"] = "SCRAMCAP Abbas #001 Start",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 155,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [30]
        [31] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_damaged",
                    ["unit"] = 341,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 342,
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1035,
                }, -- end of [5]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "SCRAMCAP Abbas #002 Start",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 156,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [31]
        [32] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1549,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Bushehr Activate",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 178,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 179,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["group"] = 180,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["group"] = 181,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["group"] = 182,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["group"] = 183,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["group"] = 184,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [7]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [32]
        [33] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1651,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "Southwest Activate",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 169,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [33]
        [34] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1033,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 234,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["predicate"] = "or",
                }, -- end of [3]
                [4] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1137,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 319,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1138,
                }, -- end of [7]
                [8] = 
                {
                    ["unit"] = 320,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["predicate"] = "or",
                }, -- end of [9]
                [10] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 620,
                }, -- end of [10]
                [11] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 323,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 826,
                }, -- end of [13]
                [14] = 
                {
                    ["unit"] = 339,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [14]
                [15] = 
                {
                    ["predicate"] = "or",
                }, -- end of [15]
                [16] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 723,
                }, -- end of [16]
                [17] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 334,
                }, -- end of [17]
                [18] = 
                {
                    ["predicate"] = "or",
                }, -- end of [18]
                [19] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1344,
                }, -- end of [19]
                [20] = 
                {
                    ["unit"] = 392,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [20]
                [21] = 
                {
                    ["predicate"] = "or",
                }, -- end of [21]
                [22] = 
                {
                    ["group"] = 96,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [22]
                [23] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 486,
                }, -- end of [23]
                [24] = 
                {
                    ["predicate"] = "or",
                }, -- end of [24]
                [25] = 
                {
                    ["group"] = 96,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [25]
                [26] = 
                {
                    ["unit"] = 497,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [26]
                [27] = 
                {
                    ["predicate"] = "or",
                }, -- end of [27]
                [28] = 
                {
                    ["group"] = 96,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [28]
                [29] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 508,
                }, -- end of [29]
                [30] = 
                {
                    ["predicate"] = "or",
                }, -- end of [30]
                [31] = 
                {
                    ["group"] = 96,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [31]
                [32] = 
                {
                    ["unit"] = 519,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [32]
                [33] = 
                {
                    ["predicate"] = "or",
                }, -- end of [33]
                [34] = 
                {
                    ["group"] = 96,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [34]
                [35] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 530,
                }, -- end of [35]
                [36] = 
                {
                    ["predicate"] = "or",
                }, -- end of [36]
                [37] = 
                {
                    ["group"] = 96,
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [37]
                [38] = 
                {
                    ["unit"] = 475,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [38]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [2]
                [3] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [5]
                [6] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [7]
                [8] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [8]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["comment"] = "INTERCEPT Start",
        }, -- end of [34]
        [35] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_damaged",
                    ["unit"] = 366,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 367,
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 416,
                }, -- end of [3]
            }, -- end of ["rules"]
            ["comment"] = "INTERCEPT Kerman #003 Init",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["flag"] = 143,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0x008000ff",
        }, -- end of [35]
        [36] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 143,
                    ["seconds"] = 900,
                    ["predicate"] = "c_time_since_flag",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "INTERCEPT Kerman #003 Start",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 143,
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x008000ff",
        }, -- end of [36]
        [37] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["unit"] = 368,
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_damaged",
                    ["unit"] = 369,
                }, -- end of [3]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "INTERCEPT Shiraz #003 Init",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["flag"] = 43,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 196,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff00ffff",
        }, -- end of [37]
        [38] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 43,
                    ["seconds"] = 900,
                    ["predicate"] = "c_time_since_flag",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "INTERCEPT Shiraz #003 Start",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 143,
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff00ffff",
        }, -- end of [38]
        [39] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_damaged",
                    ["unit"] = 370,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["unit"] = 371,
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 416,
                }, -- end of [3]
            }, -- end of ["rules"]
            ["comment"] = "INTERCEPT Kish #002 Init",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["flag"] = 212,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 197,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xffff00ff",
        }, -- end of [39]
        [40] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 212,
                    ["seconds"] = 900,
                    ["predicate"] = "c_time_since_flag",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "INTERCEPT Kish #002 Start",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 143,
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0xffff00ff",
        }, -- end of [40]
        [41] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["unit"] = 372,
                    ["predicate"] = "c_unit_damaged",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_damaged",
                    ["unit"] = 373,
                }, -- end of [3]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "INTERCEPT Abbas #002 Init",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag",
                    ["flag"] = 292,
                }, -- end of [1]
                [2] = 
                {
                    ["group"] = 198,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [2]
            }, -- end of ["actions"]
            ["colorItem"] = "0xff0000ff",
        }, -- end of [41]
        [42] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 292,
                    ["seconds"] = 900,
                    ["predicate"] = "c_time_since_flag",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "INTERCEPT Abbas #002 Start",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 143,
                    ["zone"] = 416,
                    ["group"] = 193,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 1,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["colorItem"] = "0xff0000ff",
        }, -- end of [42]
        [43] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 620,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 323,
                }, -- end of [2]
            }, -- end of ["rules"]
            ["comment"] = "INTERCEPT Vector Kerman",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
                [2] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                }, -- end of [3]
                [4] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                }, -- end of [5]
                [6] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 197,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                }, -- end of [8]
                [9] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                }, -- end of [9]
                [10] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [10]
                [11] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                }, -- end of [11]
                [12] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 2,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [12]
            }, -- end of ["actions"]
            ["predicate"] = "triggerFront",
        }, -- end of [43]
        [44] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1033,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 234,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["predicate"] = "or",
                }, -- end of [3]
                [4] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1137,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 319,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1138,
                }, -- end of [7]
                [8] = 
                {
                    ["unit"] = 320,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [8]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["predicate"] = "triggerFront",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                }, -- end of [2]
                [3] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                }, -- end of [4]
                [5] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 197,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                }, -- end of [6]
                [7] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                }, -- end of [7]
                [8] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                }, -- end of [10]
                [11] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 3,
                    }, -- end of ["ai_task"]
                }, -- end of [12]
            }, -- end of ["actions"]
            ["comment"] = "INTERCEPT Vector Abbas",
        }, -- end of [44]
        [45] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 826,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 339,
                }, -- end of [2]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "INTERCEPT Vector Kish",
            ["predicate"] = "triggerFront",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
                [2] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                }, -- end of [3]
                [4] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                }, -- end of [5]
                [6] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 197,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                }, -- end of [8]
                [9] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                }, -- end of [9]
                [10] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [10]
                [11] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                }, -- end of [11]
                [12] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 4,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [12]
            }, -- end of ["actions"]
        }, -- end of [45]
        [46] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 723,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 334,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [2]
            }, -- end of ["rules"]
            ["comment"] = "INTERCEPT Vector Shiraz",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                }, -- end of [2]
                [3] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                }, -- end of [4]
                [5] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                }, -- end of [6]
                [7] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 197,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                }, -- end of [8]
                [9] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                }, -- end of [9]
                [10] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [10]
                [11] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 5,
                    }, -- end of ["ai_task"]
                }, -- end of [12]
            }, -- end of ["actions"]
            ["predicate"] = "triggerFront",
            ["eventlist"] = "",
        }, -- end of [46]
        [47] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1344,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 392,
                }, -- end of [2]
            }, -- end of ["rules"]
            ["comment"] = "INTERCEPT Vector Southwest",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
                [2] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                }, -- end of [3]
                [4] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                }, -- end of [5]
                [6] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                }, -- end of [7]
                [8] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 197,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                }, -- end of [10]
                [11] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                }, -- end of [11]
                [12] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 6,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [12]
            }, -- end of ["actions"]
            ["predicate"] = "triggerFront",
        }, -- end of [47]
        [48] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["coalitionlist"] = "blue",
                    ["unitType"] = "ALL",
                    ["zone"] = 1345,
                }, -- end of [1]
                [2] = 
                {
                    ["unit"] = 391,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [2]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["predicate"] = "triggerFront",
            ["actions"] = 
            {
                [1] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                }, -- end of [2]
                [3] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                }, -- end of [4]
                [5] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                }, -- end of [6]
                [7] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 197,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                }, -- end of [8]
                [9] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                }, -- end of [9]
                [10] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [10]
                [11] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 7,
                    }, -- end of ["ai_task"]
                }, -- end of [12]
            }, -- end of ["actions"]
            ["comment"] = "INTERCEPT Vector Jask",
        }, -- end of [48]
        [49] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 486,
                }, -- end of [2]
                [3] = 
                {
                    ["predicate"] = "or",
                }, -- end of [3]
                [4] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [4]
                [5] = 
                {
                    ["unit"] = 497,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [7]
                [8] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 508,
                }, -- end of [8]
                [9] = 
                {
                    ["predicate"] = "or",
                }, -- end of [9]
                [10] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [10]
                [11] = 
                {
                    ["unit"] = 519,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [13]
                [14] = 
                {
                    ["zone"] = 416,
                    ["predicate"] = "c_unit_alive",
                    ["unit"] = 530,
                }, -- end of [14]
                [15] = 
                {
                    ["predicate"] = "or",
                }, -- end of [15]
                [16] = 
                {
                    ["coalitionlist"] = "blue",
                    ["predicate"] = "c_part_of_coalition_in_zone",
                    ["zone"] = 1753,
                }, -- end of [16]
                [17] = 
                {
                    ["unit"] = 475,
                    ["predicate"] = "c_unit_alive",
                    ["zone"] = 416,
                }, -- end of [17]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "INTERCEPT Vector Bushehr",
            ["predicate"] = "triggerFront",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 161,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                }, -- end of [1]
                [2] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 187,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 193,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                }, -- end of [3]
                [4] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 162,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 186,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                }, -- end of [5]
                [6] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 196,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [6]
                [7] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 163,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                }, -- end of [7]
                [8] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 197,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [8]
                [9] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 164,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 198,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                }, -- end of [10]
                [11] = 
                {
                    ["zone"] = 416,
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["ai_task"] = 
                    {
                        [1] = 165,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                }, -- end of [11]
                [12] = 
                {
                    ["ai_task"] = 
                    {
                        [1] = 166,
                        [2] = 8,
                    }, -- end of ["ai_task"]
                    ["meters"] = 1000,
                    ["predicate"] = "a_ai_task",
                    ["zone"] = 416,
                }, -- end of [12]
            }, -- end of ["actions"]
        }, -- end of [49]
        [50] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 1,
                    ["flag"] = 300,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 301,
                    ["zone"] = 416,
                    ["max_value"] = 8,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["comment"] = "if 300 = 1, 301 rand 1-8",
        }, -- end of [50]
        [51] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 300,
                    ["value"] = 2,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "if 300 = 2, 302 rand 1-8",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["meters"] = 1000,
                    ["zone"] = 416,
                    ["flag"] = 302,
                    ["min_value"] = 1,
                    ["predicate"] = "a_set_flag_random",
                    ["max_value"] = 8,
                }, -- end of [1]
            }, -- end of ["actions"]
        }, -- end of [51]
        [52] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 3,
                    ["flag"] = 300,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "if 300 = 3, 303 rand 1-8",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 303,
                    ["zone"] = 416,
                    ["max_value"] = 8,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["eventlist"] = "",
        }, -- end of [52]
        [53] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 300,
                    ["value"] = 4,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "if 300 = 4, 304 rand 1-8",
            ["actions"] = 
            {
                [1] = 
                {
                    ["meters"] = 1000,
                    ["zone"] = 416,
                    ["flag"] = 304,
                    ["min_value"] = 1,
                    ["predicate"] = "a_set_flag_random",
                    ["max_value"] = 8,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
        }, -- end of [53]
        [54] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 5,
                    ["flag"] = 300,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 305,
                    ["zone"] = 416,
                    ["max_value"] = 8,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["comment"] = "if 300 = 5, 305 rand 1-8",
        }, -- end of [54]
        [55] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 300,
                    ["value"] = 6,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "if 300 = 6, 305 rand 1-8",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["meters"] = 1000,
                    ["zone"] = 416,
                    ["flag"] = 306,
                    ["min_value"] = 1,
                    ["predicate"] = "a_set_flag_random",
                    ["max_value"] = 8,
                }, -- end of [1]
            }, -- end of ["actions"]
        }, -- end of [55]
        [56] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 7,
                    ["flag"] = 300,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "if 300 = 7, 307 rand 1-8",
            ["actions"] = 
            {
                [1] = 
                {
                    ["flag"] = 307,
                    ["zone"] = 416,
                    ["max_value"] = 8,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["eventlist"] = "",
        }, -- end of [56]
        [57] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 300,
                    ["value"] = 8,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "if 300 = 8, 308 rand 1-8",
            ["actions"] = 
            {
                [1] = 
                {
                    ["meters"] = 1000,
                    ["zone"] = 416,
                    ["flag"] = 308,
                    ["min_value"] = 1,
                    ["predicate"] = "a_set_flag_random",
                    ["max_value"] = 8,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
        }, -- end of [57]
        [58] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 1,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag"] = 302,
                    ["value"] = 1,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["value"] = 1,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag"] = 304,
                    ["value"] = 1,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["value"] = 1,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag"] = 306,
                    ["value"] = 1,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["value"] = 1,
                    ["flag"] = 307,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["flag"] = 308,
                    ["value"] = 1,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 161,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["comment"] = "Intercept Kerman Activate",
        }, -- end of [58]
        [59] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 301,
                    ["value"] = 2,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["value"] = 2,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag"] = 303,
                    ["value"] = 2,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["value"] = 2,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag"] = 305,
                    ["value"] = 2,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["value"] = 2,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag"] = 307,
                    ["value"] = 2,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["value"] = 2,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["comment"] = "Intercept Shiraz Activate",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 162,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
        }, -- end of [59]
        [60] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 3,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag"] = 302,
                    ["value"] = 3,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["value"] = 3,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag"] = 304,
                    ["value"] = 3,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["value"] = 3,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag"] = 306,
                    ["value"] = 3,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["value"] = 3,
                    ["flag"] = 307,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["flag"] = 308,
                    ["value"] = 3,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["comment"] = "Intercept Kish Activate",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 163,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["eventlist"] = "",
        }, -- end of [60]
        [61] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 301,
                    ["value"] = 4,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["value"] = 4,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag"] = 303,
                    ["value"] = 4,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["value"] = 4,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag"] = 305,
                    ["value"] = 4,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["value"] = 4,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag"] = 307,
                    ["value"] = 4,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["value"] = 4,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["comment"] = "Intercept Abbas Activate",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 164,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
        }, -- end of [61]
        [62] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 5,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag"] = 302,
                    ["value"] = 5,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["value"] = 5,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag"] = 304,
                    ["value"] = 5,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["value"] = 5,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag"] = 306,
                    ["value"] = 5,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["value"] = 5,
                    ["flag"] = 307,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["flag"] = 308,
                    ["value"] = 5,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 165,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["comment"] = "Intercept Jiroft Activate",
        }, -- end of [62]
        [63] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 301,
                    ["value"] = 6,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["value"] = 6,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag"] = 303,
                    ["value"] = 6,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["value"] = 6,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag"] = 305,
                    ["value"] = 6,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["value"] = 6,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag"] = 307,
                    ["value"] = 6,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["value"] = 6,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["comment"] = "Intercept Lar Activate",
            ["eventlist"] = "",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 166,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
        }, -- end of [63]
        [64] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["value"] = 7,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag"] = 302,
                    ["value"] = 7,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["value"] = 7,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag"] = 304,
                    ["value"] = 7,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["value"] = 7,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag"] = 306,
                    ["value"] = 7,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["value"] = 7,
                    ["flag"] = 307,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["flag"] = 308,
                    ["value"] = 7,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["comment"] = "Intercept Shiraz #002 Activate",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 186,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
            ["eventlist"] = "",
        }, -- end of [64]
        [65] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag"] = 301,
                    ["value"] = 8,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["value"] = 8,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag"] = 303,
                    ["value"] = 8,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["value"] = 8,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag"] = 305,
                    ["value"] = 8,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["value"] = 8,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag"] = 307,
                    ["value"] = 8,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [13]
                [14] = 
                {
                    ["predicate"] = "or",
                }, -- end of [14]
                [15] = 
                {
                    ["value"] = 8,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals",
                    ["zone"] = 416,
                }, -- end of [15]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "Intercept Kerman #002 Activate",
            ["predicate"] = "triggerOnce",
            ["actions"] = 
            {
                [1] = 
                {
                    ["group"] = 187,
                    ["meters"] = 1000,
                    ["predicate"] = "a_activate_group",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
        }, -- end of [65]
        [66] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag2"] = 302,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag2"] = 303,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag2"] = 304,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag2"] = 305,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag2"] = 306,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag2"] = 307,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag2"] = 308,
                    ["flag"] = 301,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [13]
            }, -- end of ["rules"]
            ["comment"] = "if 301 = 3xx",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["min_value"] = 1,
                    ["zone"] = 416,
                    ["flag"] = 301,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["max_value"] = 8,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerContinious",
            ["colorItem"] = "0x8000ffff",
        }, -- end of [66]
        [67] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag2"] = 301,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag2"] = 303,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag2"] = 304,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag2"] = 305,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag2"] = 306,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag2"] = 307,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag2"] = 308,
                    ["flag"] = 302,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [13]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "if 302 = 3xx",
            ["actions"] = 
            {
                [1] = 
                {
                    ["max_value"] = 8,
                    ["zone"] = 416,
                    ["flag"] = 302,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerContinious",
            ["colorItem"] = "0x8000ffff",
        }, -- end of [67]
        [68] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag2"] = 301,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag2"] = 302,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag2"] = 304,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag2"] = 305,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag2"] = 306,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag2"] = 307,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag2"] = 308,
                    ["flag"] = 303,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [13]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "if 303 = 3xx",
            ["predicate"] = "triggerContinious",
            ["actions"] = 
            {
                [1] = 
                {
                    ["min_value"] = 1,
                    ["zone"] = 416,
                    ["flag"] = 303,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["max_value"] = 8,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x8000ffff",
        }, -- end of [68]
        [69] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag2"] = 301,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag2"] = 302,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag2"] = 303,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag2"] = 305,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag2"] = 306,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag2"] = 307,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag2"] = 308,
                    ["flag"] = 304,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [13]
            }, -- end of ["rules"]
            ["comment"] = "if 304 = 3xx",
            ["eventlist"] = "",
            ["predicate"] = "triggerContinious",
            ["actions"] = 
            {
                [1] = 
                {
                    ["max_value"] = 8,
                    ["zone"] = 416,
                    ["flag"] = 304,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x8000ffff",
        }, -- end of [69]
        [70] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag2"] = 301,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag2"] = 302,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag2"] = 303,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag2"] = 304,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag2"] = 306,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag2"] = 307,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag2"] = 308,
                    ["flag"] = 305,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [13]
            }, -- end of ["rules"]
            ["comment"] = "if 305 = 3xx",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["min_value"] = 1,
                    ["zone"] = 416,
                    ["flag"] = 305,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["max_value"] = 8,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerContinious",
            ["colorItem"] = "0x8000ffff",
        }, -- end of [70]
        [71] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag2"] = 301,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag2"] = 302,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag2"] = 303,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag2"] = 304,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag2"] = 305,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag2"] = 307,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag2"] = 308,
                    ["flag"] = 306,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [13]
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["comment"] = "if 306 = 3xx",
            ["actions"] = 
            {
                [1] = 
                {
                    ["max_value"] = 8,
                    ["zone"] = 416,
                    ["flag"] = 306,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["predicate"] = "triggerContinious",
            ["colorItem"] = "0x8000ffff",
        }, -- end of [71]
        [72] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["flag2"] = 301,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [1]
                [2] = 
                {
                    ["predicate"] = "or",
                }, -- end of [2]
                [3] = 
                {
                    ["flag2"] = 302,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [3]
                [4] = 
                {
                    ["predicate"] = "or",
                }, -- end of [4]
                [5] = 
                {
                    ["flag2"] = 303,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [5]
                [6] = 
                {
                    ["predicate"] = "or",
                }, -- end of [6]
                [7] = 
                {
                    ["flag2"] = 304,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [7]
                [8] = 
                {
                    ["predicate"] = "or",
                }, -- end of [8]
                [9] = 
                {
                    ["flag2"] = 305,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [9]
                [10] = 
                {
                    ["predicate"] = "or",
                }, -- end of [10]
                [11] = 
                {
                    ["flag2"] = 306,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [11]
                [12] = 
                {
                    ["predicate"] = "or",
                }, -- end of [12]
                [13] = 
                {
                    ["flag2"] = 307,
                    ["flag"] = 308,
                    ["predicate"] = "c_flag_equals_flag",
                    ["zone"] = 416,
                }, -- end of [13]
            }, -- end of ["rules"]
            ["comment"] = "if 308 = 3xx",
            ["eventlist"] = "",
            ["predicate"] = "triggerContinious",
            ["actions"] = 
            {
                [1] = 
                {
                    ["max_value"] = 8,
                    ["zone"] = 416,
                    ["flag"] = 308,
                    ["meters"] = 1000,
                    ["predicate"] = "a_set_flag_random",
                    ["min_value"] = 1,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["colorItem"] = "0x8000ffff",
        }, -- end of [72]
        [73] = 
        {
            ["rules"] = 
            {
                [1] = 
                {
                    ["seconds"] = 5,
                    ["predicate"] = "c_time_after",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["rules"]
            ["comment"] = "Destroyed Units",
            ["eventlist"] = "",
            ["actions"] = 
            {
                [1] = 
                {
                    ["zone"] = 416,
                    ["volume"] = 1000,
                    ["meters"] = 1000,
                    ["predicate"] = "a_explosion_unit",
                    ["unit"] = 391,
                }, -- end of [1]
                [2] = 
                {
                    ["zone"] = 416,
                    ["volume"] = 1000,
                    ["meters"] = 1000,
                    ["predicate"] = "a_explosion_unit",
                    ["unit"] = 234,
                }, -- end of [2]
                [3] = 
                {
                    ["zone"] = 416,
                    ["volume"] = 1000,
                    ["meters"] = 1000,
                    ["predicate"] = "a_explosion_unit",
                    ["unit"] = 223,
                }, -- end of [3]
                [4] = 
                {
                    ["zone"] = 416,
                    ["volume"] = 1000,
                    ["meters"] = 1000,
                    ["predicate"] = "a_explosion_unit",
                    ["unit"] = 319,
                }, -- end of [4]
                [5] = 
                {
                    ["zone"] = 416,
                    ["volume"] = 1000,
                    ["meters"] = 1000,
                    ["predicate"] = "a_explosion_unit",
                    ["unit"] = 320,
                }, -- end of [5]
            }, -- end of ["actions"]
            ["predicate"] = "triggerOnce",
        }, -- end of [73]
        [74] = 
        {
            ["rules"] = 
            {
            }, -- end of ["rules"]
            ["eventlist"] = "",
            ["predicate"] = "triggerStart",
            ["actions"] = 
            {
                [1] = 
                {
                    ["file"] = "ResKey_Action_4398",
                    ["meters"] = 1000,
                    ["predicate"] = "a_do_script_file",
                    ["zone"] = 416,
                }, -- end of [1]
            }, -- end of ["actions"]
            ["comment"] = "Load IADS",
        }, -- end of [74]
    }
""")

    DICT_TRIG = lua.loads("""trig = 
    {
        ["actions"] = 
        {
            [1] = "a_set_flag_value(300, 0);a_set_flag_value(301, 11);a_set_flag_value(302, 12);a_set_flag_value(303, 13);a_set_flag_value(304, 14);a_set_flag_value(305, 15);a_set_flag_value(306, 16);a_set_flag_value(307, 17);a_set_flag_value(308, 18);",
            [2] = "a_ai_task(40, 1); mission.trig.func[2]=nil;",
            [3] = "a_ai_task(47, 1); mission.trig.func[3]=nil;",
            [4] = "a_do_script(getValueDictByKey(\\"DictKey_ActionText_450\\"));a_do_script_file(getValueResourceByKey(\\"ResKey_Action_456\\"));",
            [5] = "a_do_script_file(getValueResourceByKey(\\"ResKey_Action_457\\"));a_do_script_file(getValueResourceByKey(\\"ResKey_Action_458\\")); mission.trig.func[5]=nil;",
            [6] = "a_set_flag(1); mission.trig.func[6]=nil;",
            [7] = "a_set_flag(1); mission.trig.func[7]=nil;",
            [8] = "a_set_flag(1); mission.trig.func[8]=nil;",
            [9] = "a_set_flag(1); mission.trig.func[9]=nil;",
            [10] = "a_set_flag(1); mission.trig.func[10]=nil;",
            [11] = "a_set_flag(1); mission.trig.func[11]=nil;",
            [12] = "a_set_flag(1); mission.trig.func[12]=nil;",
            [13] = "a_set_flag(1); mission.trig.func[13]=nil;",
            [14] = "a_add_radio_item_for_group(195, getValueDictByKey(\\"DictKey_ActionRadioText_2251\\"), 2, 1);a_add_radio_item_for_group(194, getValueDictByKey(\\"DictKey_ActionRadioText_2428\\"), 2, 1);",
            [15] = "a_do_script_file(getValueResourceByKey(\\"ResKey_Action_2248\\"));a_do_script_file(getValueResourceByKey(\\"ResKey_Action_2249\\"));a_remove_radio_item(getValueDictByKey(\\"DictKey_ActionRadioText_2250\\")); mission.trig.func[15]=nil;",
            [16] = "a_inc_flag(300, 1); mission.trig.func[16]=nil;",
            [17] = "a_inc_flag(300, 1); mission.trig.func[17]=nil;",
            [18] = "a_inc_flag(300, 1); mission.trig.func[18]=nil;",
            [19] = "a_inc_flag(300, 1); mission.trig.func[19]=nil;",
            [20] = "a_activate_group(143);a_activate_group(145);a_activate_group(144);a_activate_group(185); mission.trig.func[20]=nil;",
            [21] = "a_ai_task(143, 1); mission.trig.func[21]=nil;",
            [22] = "a_ai_task(145, 1); mission.trig.func[22]=nil;",
            [23] = "a_activate_group(148);a_activate_group(149);a_activate_group(150);a_activate_group(171); mission.trig.func[23]=nil;",
            [24] = "a_ai_task(148, 1); mission.trig.func[24]=nil;",
            [25] = "a_ai_task(149, 1); mission.trig.func[25]=nil;",
            [26] = "a_activate_group(151);a_activate_group(152);a_activate_group(153);a_activate_group(140); mission.trig.func[26]=nil;",
            [27] = "a_ai_task(151, 1); mission.trig.func[27]=nil;",
            [28] = "a_ai_task(152, 1); mission.trig.func[28]=nil;",
            [29] = "a_activate_group(155);a_activate_group(156);a_activate_group(130);a_activate_group(131);a_activate_group(132);a_activate_group(141);a_activate_group(142);a_activate_group(207);a_activate_group(208);a_activate_group(213);a_activate_group(214); mission.trig.func[29]=nil;",
            [30] = "a_ai_task(155, 1); mission.trig.func[30]=nil;",
            [31] = "a_ai_task(156, 1); mission.trig.func[31]=nil;",
            [32] = "a_activate_group(178);a_activate_group(179);a_activate_group(180);a_activate_group(181);a_activate_group(182);a_activate_group(183);a_activate_group(184); mission.trig.func[32]=nil;",
            [33] = "a_activate_group(169); mission.trig.func[33]=nil;",
            [34] = "a_ai_task(161, 1);a_ai_task(187, 1);a_ai_task(162, 1);a_ai_task(186, 1);a_ai_task(163, 1);a_ai_task(164, 1);a_ai_task(165, 1);a_ai_task(166, 1); mission.trig.func[34]=nil;",
            [35] = "a_set_flag(143);a_activate_group(193); mission.trig.func[35]=nil;",
            [36] = "a_ai_task(193, 1); mission.trig.func[36]=nil;",
            [37] = "a_set_flag(43);a_activate_group(196); mission.trig.func[37]=nil;",
            [38] = "a_ai_task(196, 1); mission.trig.func[38]=nil;",
            [39] = "a_set_flag(212);a_activate_group(197); mission.trig.func[39]=nil;",
            [40] = "a_ai_task(163, 1); mission.trig.func[40]=nil;",
            [41] = "a_set_flag(292);a_activate_group(198); mission.trig.func[41]=nil;",
            [42] = "a_ai_task(198, 1); mission.trig.func[42]=nil;",
            [43] = "a_ai_task(161, 2);a_ai_task(187, 2);a_ai_task(193, 2);a_ai_task(162, 2);a_ai_task(163, 2);a_ai_task(197, 2);a_ai_task(164, 2);a_ai_task(198, 2);a_ai_task(165, 2);a_ai_task(166, 2);a_ai_task(186, 2);a_ai_task(196, 2);",
            [44] = "a_ai_task(161, 3);a_ai_task(187, 3);a_ai_task(193, 3);a_ai_task(162, 3);a_ai_task(163, 3);a_ai_task(197, 3);a_ai_task(164, 3);a_ai_task(198, 3);a_ai_task(165, 3);a_ai_task(166, 3);a_ai_task(186, 3);a_ai_task(196, 3);",
            [45] = "a_ai_task(161, 4);a_ai_task(187, 4);a_ai_task(193, 4);a_ai_task(162, 4);a_ai_task(163, 4);a_ai_task(197, 4);a_ai_task(164, 4);a_ai_task(198, 4);a_ai_task(165, 4);a_ai_task(166, 4);a_ai_task(186, 4);a_ai_task(196, 4);",
            [46] = "a_ai_task(161, 5);a_ai_task(187, 5);a_ai_task(193, 5);a_ai_task(162, 5);a_ai_task(186, 5);a_ai_task(196, 5);a_ai_task(163, 5);a_ai_task(197, 5);a_ai_task(164, 5);a_ai_task(198, 5);a_ai_task(165, 5);a_ai_task(166, 5);",
            [47] = "a_ai_task(161, 6);a_ai_task(187, 6);a_ai_task(193, 6);a_ai_task(162, 6);a_ai_task(186, 6);a_ai_task(196, 6);a_ai_task(163, 6);a_ai_task(197, 6);a_ai_task(164, 6);a_ai_task(198, 6);a_ai_task(165, 6);a_ai_task(166, 6);",
            [48] = "a_ai_task(161, 7);a_ai_task(187, 7);a_ai_task(193, 7);a_ai_task(162, 7);a_ai_task(186, 7);a_ai_task(196, 7);a_ai_task(163, 7);a_ai_task(197, 7);a_ai_task(164, 7);a_ai_task(198, 7);a_ai_task(165, 7);a_ai_task(166, 7);",
            [49] = "a_ai_task(161, 8);a_ai_task(187, 8);a_ai_task(193, 8);a_ai_task(162, 8);a_ai_task(186, 8);a_ai_task(196, 8);a_ai_task(163, 8);a_ai_task(197, 8);a_ai_task(164, 8);a_ai_task(198, 8);a_ai_task(165, 8);a_ai_task(166, 8);",
            [50] = "a_set_flag_random(301, 1, 8); mission.trig.func[50]=nil;",
            [51] = "a_set_flag_random(302, 1, 8); mission.trig.func[51]=nil;",
            [52] = "a_set_flag_random(303, 1, 8); mission.trig.func[52]=nil;",
            [53] = "a_set_flag_random(304, 1, 8); mission.trig.func[53]=nil;",
            [54] = "a_set_flag_random(305, 1, 8); mission.trig.func[54]=nil;",
            [55] = "a_set_flag_random(306, 1, 8); mission.trig.func[55]=nil;",
            [56] = "a_set_flag_random(307, 1, 8); mission.trig.func[56]=nil;",
            [57] = "a_set_flag_random(308, 1, 8); mission.trig.func[57]=nil;",
            [58] = "a_activate_group(161); mission.trig.func[58]=nil;",
            [59] = "a_activate_group(162); mission.trig.func[59]=nil;",
            [60] = "a_activate_group(163); mission.trig.func[60]=nil;",
            [61] = "a_activate_group(164); mission.trig.func[61]=nil;",
            [62] = "a_activate_group(165); mission.trig.func[62]=nil;",
            [63] = "a_activate_group(166); mission.trig.func[63]=nil;",
            [64] = "a_activate_group(186); mission.trig.func[64]=nil;",
            [65] = "a_activate_group(187); mission.trig.func[65]=nil;",
            [66] = "a_set_flag_random(301, 1, 8);",
            [67] = "a_set_flag_random(302, 1, 8);",
            [68] = "a_set_flag_random(303, 1, 8);",
            [69] = "a_set_flag_random(304, 1, 8);",
            [70] = "a_set_flag_random(305, 1, 8);",
            [71] = "a_set_flag_random(306, 1, 8);",
            [72] = "a_set_flag_random(308, 1, 8);",
            [73] = "a_explosion_unit(391, 1000);a_explosion_unit(234, 1000);a_explosion_unit(223, 1000);a_explosion_unit(319, 1000);a_explosion_unit(320, 1000); mission.trig.func[73]=nil;",
            [74] = "a_do_script_file(getValueResourceByKey(\\"ResKey_Action_4398\\"));",
        }, -- end of ["actions"]
        ["events"] = 
        {
        }, -- end of ["events"]
        ["custom"] = 
        {
        }, -- end of ["custom"]
        ["func"] = 
        {
            [2] = "if mission.trig.conditions[2]() then mission.trig.actions[2]() end",
            [3] = "if mission.trig.conditions[3]() then mission.trig.actions[3]() end",
            [5] = "if mission.trig.conditions[5]() then mission.trig.actions[5]() end",
            [6] = "if mission.trig.conditions[6]() then mission.trig.actions[6]() end",
            [7] = "if mission.trig.conditions[7]() then mission.trig.actions[7]() end",
            [8] = "if mission.trig.conditions[8]() then mission.trig.actions[8]() end",
            [9] = "if mission.trig.conditions[9]() then mission.trig.actions[9]() end",
            [10] = "if mission.trig.conditions[10]() then mission.trig.actions[10]() end",
            [11] = "if mission.trig.conditions[11]() then mission.trig.actions[11]() end",
            [12] = "if mission.trig.conditions[12]() then mission.trig.actions[12]() end",
            [13] = "if mission.trig.conditions[13]() then mission.trig.actions[13]() end",
            [15] = "if mission.trig.conditions[15]() then mission.trig.actions[15]() end",
            [16] = "if mission.trig.conditions[16]() then mission.trig.actions[16]() end",
            [17] = "if mission.trig.conditions[17]() then mission.trig.actions[17]() end",
            [18] = "if mission.trig.conditions[18]() then mission.trig.actions[18]() end",
            [19] = "if mission.trig.conditions[19]() then mission.trig.actions[19]() end",
            [20] = "if mission.trig.conditions[20]() then mission.trig.actions[20]() end",
            [21] = "if mission.trig.conditions[21]() then mission.trig.actions[21]() end",
            [22] = "if mission.trig.conditions[22]() then mission.trig.actions[22]() end",
            [23] = "if mission.trig.conditions[23]() then mission.trig.actions[23]() end",
            [24] = "if mission.trig.conditions[24]() then mission.trig.actions[24]() end",
            [25] = "if mission.trig.conditions[25]() then mission.trig.actions[25]() end",
            [26] = "if mission.trig.conditions[26]() then mission.trig.actions[26]() end",
            [27] = "if mission.trig.conditions[27]() then mission.trig.actions[27]() end",
            [28] = "if mission.trig.conditions[28]() then mission.trig.actions[28]() end",
            [29] = "if mission.trig.conditions[29]() then mission.trig.actions[29]() end",
            [30] = "if mission.trig.conditions[30]() then mission.trig.actions[30]() end",
            [31] = "if mission.trig.conditions[31]() then mission.trig.actions[31]() end",
            [32] = "if mission.trig.conditions[32]() then mission.trig.actions[32]() end",
            [33] = "if mission.trig.conditions[33]() then mission.trig.actions[33]() end",
            [34] = "if mission.trig.conditions[34]() then mission.trig.actions[34]() end",
            [35] = "if mission.trig.conditions[35]() then mission.trig.actions[35]() end",
            [36] = "if mission.trig.conditions[36]() then mission.trig.actions[36]() end",
            [37] = "if mission.trig.conditions[37]() then mission.trig.actions[37]() end",
            [38] = "if mission.trig.conditions[38]() then mission.trig.actions[38]() end",
            [39] = "if mission.trig.conditions[39]() then mission.trig.actions[39]() end",
            [40] = "if mission.trig.conditions[40]() then mission.trig.actions[40]() end",
            [41] = "if mission.trig.conditions[41]() then mission.trig.actions[41]() end",
            [42] = "if mission.trig.conditions[42]() then mission.trig.actions[42]() end",
            [43] = "if mission.trig.conditions[43]() then if not mission.trig.flag[43] then mission.trig.actions[43](); mission.trig.flag[43] = true;end; else mission.trig.flag[43] = false; end;",
            [44] = "if mission.trig.conditions[44]() then if not mission.trig.flag[44] then mission.trig.actions[44](); mission.trig.flag[44] = true;end; else mission.trig.flag[44] = false; end;",
            [45] = "if mission.trig.conditions[45]() then if not mission.trig.flag[45] then mission.trig.actions[45](); mission.trig.flag[45] = true;end; else mission.trig.flag[45] = false; end;",
            [46] = "if mission.trig.conditions[46]() then if not mission.trig.flag[46] then mission.trig.actions[46](); mission.trig.flag[46] = true;end; else mission.trig.flag[46] = false; end;",
            [47] = "if mission.trig.conditions[47]() then if not mission.trig.flag[47] then mission.trig.actions[47](); mission.trig.flag[47] = true;end; else mission.trig.flag[47] = false; end;",
            [48] = "if mission.trig.conditions[48]() then if not mission.trig.flag[48] then mission.trig.actions[48](); mission.trig.flag[48] = true;end; else mission.trig.flag[48] = false; end;",
            [49] = "if mission.trig.conditions[49]() then if not mission.trig.flag[49] then mission.trig.actions[49](); mission.trig.flag[49] = true;end; else mission.trig.flag[49] = false; end;",
            [50] = "if mission.trig.conditions[50]() then mission.trig.actions[50]() end",
            [51] = "if mission.trig.conditions[51]() then mission.trig.actions[51]() end",
            [52] = "if mission.trig.conditions[52]() then mission.trig.actions[52]() end",
            [53] = "if mission.trig.conditions[53]() then mission.trig.actions[53]() end",
            [54] = "if mission.trig.conditions[54]() then mission.trig.actions[54]() end",
            [55] = "if mission.trig.conditions[55]() then mission.trig.actions[55]() end",
            [56] = "if mission.trig.conditions[56]() then mission.trig.actions[56]() end",
            [57] = "if mission.trig.conditions[57]() then mission.trig.actions[57]() end",
            [58] = "if mission.trig.conditions[58]() then mission.trig.actions[58]() end",
            [59] = "if mission.trig.conditions[59]() then mission.trig.actions[59]() end",
            [60] = "if mission.trig.conditions[60]() then mission.trig.actions[60]() end",
            [61] = "if mission.trig.conditions[61]() then mission.trig.actions[61]() end",
            [62] = "if mission.trig.conditions[62]() then mission.trig.actions[62]() end",
            [63] = "if mission.trig.conditions[63]() then mission.trig.actions[63]() end",
            [64] = "if mission.trig.conditions[64]() then mission.trig.actions[64]() end",
            [65] = "if mission.trig.conditions[65]() then mission.trig.actions[65]() end",
            [66] = "if mission.trig.conditions[66]() then mission.trig.actions[66]() end",
            [67] = "if mission.trig.conditions[67]() then mission.trig.actions[67]() end",
            [68] = "if mission.trig.conditions[68]() then mission.trig.actions[68]() end",
            [69] = "if mission.trig.conditions[69]() then mission.trig.actions[69]() end",
            [70] = "if mission.trig.conditions[70]() then mission.trig.actions[70]() end",
            [71] = "if mission.trig.conditions[71]() then mission.trig.actions[71]() end",
            [72] = "if mission.trig.conditions[72]() then mission.trig.actions[72]() end",
            [73] = "if mission.trig.conditions[73]() then mission.trig.actions[73]() end",
        }, -- end of ["func"]
        ["flag"] = 
        {
            [1] = true,
            [2] = true,
            [3] = true,
            [4] = true,
            [5] = true,
            [6] = true,
            [7] = true,
            [8] = true,
            [9] = true,
            [10] = true,
            [11] = true,
            [12] = true,
            [13] = true,
            [14] = true,
            [15] = true,
            [16] = true,
            [17] = true,
            [18] = true,
            [19] = true,
            [20] = true,
            [21] = true,
            [22] = true,
            [23] = true,
            [24] = true,
            [25] = true,
            [26] = true,
            [27] = true,
            [28] = true,
            [29] = true,
            [30] = true,
            [31] = true,
            [32] = true,
            [33] = true,
            [34] = true,
            [35] = true,
            [36] = true,
            [37] = true,
            [38] = true,
            [39] = true,
            [40] = true,
            [41] = true,
            [42] = true,
            [43] = true,
            [44] = true,
            [45] = true,
            [46] = true,
            [47] = true,
            [48] = true,
            [49] = true,
            [50] = true,
            [51] = true,
            [52] = true,
            [53] = true,
            [54] = true,
            [55] = true,
            [56] = true,
            [57] = true,
            [58] = true,
            [59] = true,
            [60] = true,
            [61] = true,
            [62] = true,
            [63] = true,
            [64] = true,
            [65] = true,
            [66] = true,
            [67] = true,
            [68] = true,
            [69] = true,
            [70] = true,
            [71] = true,
            [72] = true,
            [73] = true,
            [74] = true,
        }, -- end of ["flag"]
        ["conditions"] = 
        {
            [1] = "return(true)",
            [2] = "return(c_time_after(180) )",
            [3] = "return(c_time_after(10800) )",
            [4] = "return(true)",
            [5] = "return(c_flag_is_true(1) or c_time_after(7200) )",
            [6] = "return(c_unit_altitude_higher(582, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [7] = "return(c_unit_altitude_higher(583, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [8] = "return(c_unit_altitude_higher(648, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [9] = "return(c_unit_altitude_higher(649, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [10] = "return(c_unit_altitude_higher(586, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [11] = "return(c_unit_altitude_higher(587, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [12] = "return(c_unit_altitude_higher(588, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [13] = "return(c_unit_altitude_higher(589, 1000) and c_unit_out_zone_unit(582, 416, 1) and c_unit_out_zone_unit(583, 416, 1) and c_unit_out_zone_unit(648, 416, 1) and c_unit_out_zone_unit(649, 416, 1) and c_unit_out_zone_unit(586, 416, 1) and c_unit_out_zone_unit(587, 416, 1) and c_unit_out_zone_unit(588, 416, 1) and c_unit_out_zone_unit(589, 416, 1) )",
            [14] = "return(true)",
            [15] = "return(c_flag_is_true(2) )",
            [16] = "return(c_group_alive(194) )",
            [17] = "return(c_group_alive(199) )",
            [18] = "return(c_group_alive(195) )",
            [19] = "return(c_group_alive(201) )",
            [20] = "return(c_part_of_coalition_in_zone(\\"blue\\", 621, \\"ALL\\") )",
            [21] = "return(c_part_of_coalition_in_zone(\\"blue\\", 620, \\"ALL\\") and c_unit_alive(323) or c_part_of_coalition_in_zone(\\"blue\\", 929, \\"ALL\\") )",
            [22] = "return(c_unit_damaged(321) or c_unit_damaged(322) or c_part_of_coalition_in_zone(\\"blue\\", 929, \\"ALL\\") )",
            [23] = "return(c_part_of_coalition_in_zone(\\"blue\\", 724, \\"ALL\\") )",
            [24] = "return(c_part_of_coalition_in_zone(\\"blue\\", 723, \\"ALL\\") and c_unit_alive(334) or c_part_of_coalition_in_zone(\\"blue\\", 930, \\"ALL\\") )",
            [25] = "return(c_unit_damaged(330) or c_unit_damaged(331) or c_part_of_coalition_in_zone(\\"blue\\", 930, \\"ALL\\") )",
            [26] = "return(c_part_of_coalition_in_zone(\\"blue\\", 827, \\"ALL\\") )",
            [27] = "return(c_part_of_coalition_in_zone(\\"blue\\", 826, \\"ALL\\") and c_unit_alive(339) or c_part_of_coalition_in_zone(\\"blue\\", 931, \\"ALL\\") )",
            [28] = "return(c_unit_damaged(335) or c_unit_damaged(336) or c_part_of_coalition_in_zone(\\"blue\\", 931, \\"ALL\\") )",
            [29] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1034, \\"ALL\\") )",
            [30] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1033, \\"ALL\\") and c_unit_alive(234) or c_part_of_coalition_in_zone(\\"blue\\", 1137, \\"ALL\\") and c_unit_alive(319) or c_part_of_coalition_in_zone(\\"blue\\", 1138, \\"ALL\\") and c_unit_alive(320) or c_part_of_coalition_in_zone(\\"blue\\", 1035, \\"ALL\\") )",
            [31] = "return(c_unit_damaged(341) or c_unit_damaged(342) or c_part_of_coalition_in_zone(\\"blue\\", 1035, \\"ALL\\") )",
            [32] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1549, \\"ALL\\") )",
            [33] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1651, \\"ALL\\") )",
            [34] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1033, \\"ALL\\") and c_unit_alive(234) or c_part_of_coalition_in_zone(\\"blue\\", 1137, \\"ALL\\") and c_unit_alive(319) or c_part_of_coalition_in_zone(\\"blue\\", 1138, \\"ALL\\") and c_unit_alive(320) or c_part_of_coalition_in_zone(\\"blue\\", 620, \\"ALL\\") and c_unit_alive(323) or c_part_of_coalition_in_zone(\\"blue\\", 826, \\"ALL\\") and c_unit_alive(339) or c_part_of_coalition_in_zone(\\"blue\\", 723, \\"ALL\\") and c_unit_alive(334) or c_part_of_coalition_in_zone(\\"blue\\", 1344, \\"ALL\\") and c_unit_alive(392) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(486) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(497) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(508) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(519) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(530) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(475) )",
            [35] = "return(c_unit_damaged(366) or c_unit_damaged(367) )",
            [36] = "return(c_time_since_flag(143, 900) )",
            [37] = "return(c_unit_damaged(368) or c_unit_damaged(369) )",
            [38] = "return(c_time_since_flag(43, 900) )",
            [39] = "return(c_unit_damaged(370) or c_unit_damaged(371) )",
            [40] = "return(c_time_since_flag(212, 900) )",
            [41] = "return(c_unit_damaged(372) or c_unit_damaged(373) )",
            [42] = "return(c_time_since_flag(292, 900) )",
            [43] = "return(c_part_of_coalition_in_zone(\\"blue\\", 620, \\"ALL\\") and c_unit_alive(323) )",
            [44] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1033, \\"ALL\\") and c_unit_alive(234) or c_part_of_coalition_in_zone(\\"blue\\", 1137, \\"ALL\\") and c_unit_alive(319) or c_part_of_coalition_in_zone(\\"blue\\", 1138, \\"ALL\\") and c_unit_alive(320) )",
            [45] = "return(c_part_of_coalition_in_zone(\\"blue\\", 826, \\"ALL\\") and c_unit_alive(339) )",
            [46] = "return(c_part_of_coalition_in_zone(\\"blue\\", 723, \\"ALL\\") and c_unit_alive(334) )",
            [47] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1344, \\"ALL\\") and c_unit_alive(392) )",
            [48] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1345, \\"ALL\\") and c_unit_alive(391) )",
            [49] = "return(c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(486) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(497) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(508) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(519) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(530) or c_part_of_coalition_in_zone(\\"blue\\", 1753, \\"ALL\\") and c_unit_alive(475) )",
            [50] = "return(c_flag_equals(300, 1) )",
            [51] = "return(c_flag_equals(300, 2) )",
            [52] = "return(c_flag_equals(300, 3) )",
            [53] = "return(c_flag_equals(300, 4) )",
            [54] = "return(c_flag_equals(300, 5) )",
            [55] = "return(c_flag_equals(300, 6) )",
            [56] = "return(c_flag_equals(300, 7) )",
            [57] = "return(c_flag_equals(300, 8) )",
            [58] = "return(c_flag_equals(301, 1) or c_flag_equals(302, 1) or c_flag_equals(303, 1) or c_flag_equals(304, 1) or c_flag_equals(305, 1) or c_flag_equals(306, 1) or c_flag_equals(307, 1) or c_flag_equals(308, 1) )",
            [59] = "return(c_flag_equals(301, 2) or c_flag_equals(302, 2) or c_flag_equals(303, 2) or c_flag_equals(304, 2) or c_flag_equals(305, 2) or c_flag_equals(306, 2) or c_flag_equals(307, 2) or c_flag_equals(308, 2) )",
            [60] = "return(c_flag_equals(301, 3) or c_flag_equals(302, 3) or c_flag_equals(303, 3) or c_flag_equals(304, 3) or c_flag_equals(305, 3) or c_flag_equals(306, 3) or c_flag_equals(307, 3) or c_flag_equals(308, 3) )",
            [61] = "return(c_flag_equals(301, 4) or c_flag_equals(302, 4) or c_flag_equals(303, 4) or c_flag_equals(304, 4) or c_flag_equals(305, 4) or c_flag_equals(306, 4) or c_flag_equals(307, 4) or c_flag_equals(308, 4) )",
            [62] = "return(c_flag_equals(301, 5) or c_flag_equals(302, 5) or c_flag_equals(303, 5) or c_flag_equals(304, 5) or c_flag_equals(305, 5) or c_flag_equals(306, 5) or c_flag_equals(307, 5) or c_flag_equals(308, 5) )",
            [63] = "return(c_flag_equals(301, 6) or c_flag_equals(302, 6) or c_flag_equals(303, 6) or c_flag_equals(304, 6) or c_flag_equals(305, 6) or c_flag_equals(306, 6) or c_flag_equals(307, 6) or c_flag_equals(308, 6) )",
            [64] = "return(c_flag_equals(301, 7) or c_flag_equals(302, 7) or c_flag_equals(303, 7) or c_flag_equals(304, 7) or c_flag_equals(305, 7) or c_flag_equals(306, 7) or c_flag_equals(307, 7) or c_flag_equals(308, 7) )",
            [65] = "return(c_flag_equals(301, 8) or c_flag_equals(302, 8) or c_flag_equals(303, 8) or c_flag_equals(304, 8) or c_flag_equals(305, 8) or c_flag_equals(306, 8) or c_flag_equals(307, 8) or c_flag_equals(308, 8) )",
            [66] = "return(c_flag_equals_flag(301, 302) or c_flag_equals_flag(301, 303) or c_flag_equals_flag(301, 304) or c_flag_equals_flag(301, 305) or c_flag_equals_flag(301, 306) or c_flag_equals_flag(301, 307) or c_flag_equals_flag(301, 308) )",
            [67] = "return(c_flag_equals_flag(302, 301) or c_flag_equals_flag(302, 303) or c_flag_equals_flag(302, 304) or c_flag_equals_flag(302, 305) or c_flag_equals_flag(302, 306) or c_flag_equals_flag(302, 307) or c_flag_equals_flag(302, 308) )",
            [68] = "return(c_flag_equals_flag(303, 301) or c_flag_equals_flag(303, 302) or c_flag_equals_flag(303, 304) or c_flag_equals_flag(303, 305) or c_flag_equals_flag(303, 306) or c_flag_equals_flag(303, 307) or c_flag_equals_flag(303, 308) )",
            [69] = "return(c_flag_equals_flag(304, 301) or c_flag_equals_flag(304, 302) or c_flag_equals_flag(304, 303) or c_flag_equals_flag(304, 305) or c_flag_equals_flag(304, 306) or c_flag_equals_flag(304, 307) or c_flag_equals_flag(304, 308) )",
            [70] = "return(c_flag_equals_flag(305, 301) or c_flag_equals_flag(305, 302) or c_flag_equals_flag(305, 303) or c_flag_equals_flag(305, 304) or c_flag_equals_flag(305, 306) or c_flag_equals_flag(305, 307) or c_flag_equals_flag(305, 308) )",
            [71] = "return(c_flag_equals_flag(306, 301) or c_flag_equals_flag(306, 302) or c_flag_equals_flag(306, 303) or c_flag_equals_flag(306, 304) or c_flag_equals_flag(306, 305) or c_flag_equals_flag(306, 307) or c_flag_equals_flag(306, 308) )",
            [72] = "return(c_flag_equals_flag(308, 301) or c_flag_equals_flag(308, 302) or c_flag_equals_flag(308, 303) or c_flag_equals_flag(308, 304) or c_flag_equals_flag(308, 305) or c_flag_equals_flag(308, 306) or c_flag_equals_flag(308, 307) )",
            [73] = "return(c_time_after(5) )",
            [74] = "return(true)",
        }, -- end of ["conditions"]
        ["customStartup"] = 
        {
        }, -- end of ["customStartup"]
        ["funcStartup"] = 
        {
            [1] = "if mission.trig.conditions[1]() then mission.trig.actions[1]() end",
            [14] = "if mission.trig.conditions[14]() then mission.trig.actions[14]() end",
            [74] = "if mission.trig.conditions[74]() then mission.trig.actions[74]() end",
            [4] = "if mission.trig.conditions[4]() then mission.trig.actions[4]() end",
        }, -- end of ["funcStartup"]
    }""")

    def test_load_trig_conditions(self):
        m = Mission()
        r = Rules()
        r.load_from_dict(m, self.DICT_TRIGRULES['trigrules'])
        for key in self.DICT_TRIG['trig']['conditions']:
            cond = self.DICT_TRIG['trig']['conditions'][key]
            self.assertEqual(
                lua.dumps(cond),
                lua.dumps(r.trig()['conditions'][key]),
                f"Condition nr {key}")

    def test_load_trig_actions(self):
        m = Mission()
        r = Rules()
        r.load_from_dict(m, self.DICT_TRIGRULES['trigrules'])
        for key in self.DICT_TRIG['trig']['actions']:
            action = self.DICT_TRIG['trig']['actions'][key]
            self.assertEqual(
                lua.dumps(action),
                lua.dumps(r.trig()['actions'][key]),
                f"Action nr {key}")

    def test_load_trig_func(self):
        m = Mission()
        r = Rules()
        r.load_from_dict(m, self.DICT_TRIGRULES['trigrules'])
        for key in self.DICT_TRIG['trig']['func']:
            action = self.DICT_TRIG['trig']['func'][key]
            self.assertEqual(
                lua.dumps(action),
                lua.dumps(r.trig()['func'][key]),
                f"Func nr {key}")

    def test_load_trig_func_startup(self):
        m = Mission()
        r = Rules()
        r.load_from_dict(m, self.DICT_TRIGRULES['trigrules'])
        for key in self.DICT_TRIG['trig']['funcStartup']:
            action = self.DICT_TRIG['trig']['funcStartup'][key]
            self.assertEqual(
                lua.dumps(action),
                lua.dumps(r.trig()['funcStartup'][key]),
                f"FuncStartup nr {key}")
