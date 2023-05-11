import textwrap
import unittest
from dcs.lua.parse import loads


class TestLuaParse(unittest.TestCase):

    def test_integer(self):
        r = loads("int = 3")
        self.assertEqual(r, {"int": 3})

        r = loads("int = 193984")
        self.assertEqual(r, {"int": 193984})

        r = loads("int = -23")
        self.assertEqual(r, {"int": -23})

    def test_decimal(self):
        r = loads("dec = 666.6")
        self.assertEqual(r, {"dec": 666.6})

    def test_exponent(self):
        r = loads("dec = 666.6e10")
        self.assertEqual(r, {"dec": 666.6e10})

        r = loads("dec = 666.6e-10")
        self.assertEqual(r, {"dec": 666.6e-10})

    def test_string(self):
        s = """
mission =
{
    ["trig"] =
    {
        ["actions"] =
        {
            [1] = "a_(get(\\"ResKey_Action_62\\")); mission.trig.func[1]=nil;",
            [2] = "a_do_script_file(getValueResourceByKey(\\"ResKey_Action_64\\")); mission.trig.func[2]=nil;",
            [3] = "a_out_text_delay(getValueDictByKey(\\"DictKey_ActionText_66\\"), 10, false);a_do_script(getValueDictByKey(\\"DictKey_ActionText_255\\")); mission.trig.func[3]=nil;",
            [4] = "a_add_radio_item(getValueDictByKey(\\"Destroy Red Ground Group\\"), 1500, 1); mission.trig.func[4]=nil;",
            [5] = "a_do_script(getValueDictByKey(\\"DictKey_ActionText_213\\"));a_clear_flag(1500);",
        }, -- end of ["actions"]
    }
}
"""
        r = loads(s)

        r = loads('x = "a_do_script_file(getValueResourceByKey(\\"ResKey_Action_62\\")); mission.trig.func[1]=nil;"')
        self.assertEqual(r, {
            "x": "a_do_script_file(getValueResourceByKey(\"ResKey_Action_62\")); mission.trig.func[1]=nil;"})

    def test_object(self):
        luas = """
mission=
{
    ["trig"]=
    {
    },

    ["coalitions"]=
    {
        ["blue"]=
        {
            [1]=11,
            [2]=4,
            [3]=6
        }
    }, -- end of ["coalitions"]
    ["maxDictId"]=18,
    ["descriptionBlueTask"]="DictKey_descriptionBlueTask_3"
}
"""
        ref = {'mission': {
            'coalitions': {'blue': {1: 11.0, 2: 4.0, 3: 6.0}},
            'descriptionBlueTask': 'DictKey_descriptionBlueTask_3',
            'trig': {},
            'maxDictId': 18.0}}
        r = loads(luas)
        self.assertEqual(r, ref)

    def test_dictmix(self):
        luas = """
o =
{
    ["callsign"] =
    {
        [1] = 1,
        [2] = 1,
        [3] = 1,
        ["name"] = "Enfield11",
    } -- end of ["callsign"]
}
"""
        ref = {"o": {
            'callsign': {
                1: 1,
                2: 1,
                3: 1,
                "name": "Enfield11"
            }
        }}
        r = loads(luas)
        self.assertEqual(r, ref)

    def test_syntaxerr(self):
        with self.assertRaises(SyntaxError):
            loads("""m=
            {
                ["x"] 12
            }""")

    def test_missing_curly(self):
        with self.assertRaises(SyntaxError):
            loads("""t=
            {
                ["payload"] = {
                    ["num"] = 1
            }
            """)

    def test_object_without_keys(self):
        luas = """
local unitPayloads = {
    ["name"] = "JF-17",
    ["payloads"] = {
        {
            ["name"] = "PL-5Ex2, C802AKx2, 800L Tank",
            ["pylons"] = {
                [1] = {
                    ["CLSID"] = "DIS_C-802AK",
                    ["num"] = 5
                }
            }
        }
    }
}
        """
        ref = {'unitPayloads': {
            'name': "JF-17",
            'payloads': {
                1: {
                    'name': "PL-5Ex2, C802AKx2, 800L Tank",
                    'pylons': {
                        1: {
                            'CLSID': "DIS_C-802AK",
                            'num': 5
                        }
                    }
                }
            }
        }}
        r = loads(luas)
        self.assertEqual(r, ref)

    def test_mixed_objects(self):
        luas = """
o = {
    "x",
    ["a"]=2,
    "y"
}
"""

        ref = {'o': {1: "x", "a": 2, 2: "y"}}
        r = loads(luas)
        self.assertEqual(r, ref)

    def test_payload_var_ref(self):
        luas = """
local pylon_1A,pylon_1B,pylon_2,pylon_3,pylon_4,pylon_5,pylon_6,pylon_7,pylon_8B,pylon_8A = 1,2,3,4,5,6,7,8,9,10

local unitPayloads = {
  ["name"] = "F-14B",
  ["payloads"] = {
    {
      ["name"] = "XT*2",
      ["pylons"] = {
        [1] = {
          ["CLSID"] = "{F14-300gal}", ["num"] = pylon_7,
        },
        [2] = {
          ["CLSID"] = "{F14-300gal}", ["num"] = pylon_2,
        },
      },
      ["tasks"] = {
        [1] = Intercept,
        [2] = CAP,
        [3] = Escort,
        [4] = FighterSweep,
      },
    },
    {
      ["name"] = "AIM-54A-MK47*6, AIM-9M*2, XT*2",
      ["pylons"] = {
        [1] = {
          ["CLSID"] = "{LAU-138 wtip - AIM-9M}", ["num"] = pylon_8A,
        },
        [2] = {
          ["CLSID"] = "{SHOULDER AIM_54A_Mk47 R}", ["num"] = pylon_8B,
        },
        [3] = {
          ["CLSID"] = "{F14-300gal}", ["num"] = pylon_7,
        },
        [4] = {
          ["CLSID"] = "{AIM_54A_Mk47}", ["num"] = pylon_6,
        },
        [5] = {
          ["CLSID"] = "{AIM_54A_Mk47}", ["num"] = pylon_5,
        },
        [6] = {
          ["CLSID"] = "{AIM_54A_Mk47}", ["num"] = pylon_4,
        },
        [7] = {
          ["CLSID"] = "{AIM_54A_Mk47}", ["num"] = pylon_3,
        },
        [8] = {
          ["CLSID"] = "{F14-300gal}", ["num"] = pylon_2,
        },
        [9] = {
          ["CLSID"] = "{SHOULDER AIM_54A_Mk47 L}", ["num"] = pylon_1B,
        },
        [10] = {
          ["CLSID"] = "{LAU-138 wtip - AIM-9M}", ["num"] = pylon_1A,
        },
      },
      ["tasks"] = {
        [1] = Intercept,
        [2] = CAP,
        [3] = Escort,
        [4] = FighterSweep,
      },
    },
  },
  ["unitType"] = "F-14B",
}
return unitPayloads
"""
        r = loads(luas, {'Intercept': 'Intercept', 'CAP': 'CAP', 'Escort': 'Escort', 'FighterSweep': 'FighterSweep'})
        self.assertEqual(r['unitPayloads']['name'], 'F-14B')
        self.assertEqual(r['unitPayloads']['payloads'][1]['name'], "XT*2")
        self.assertEqual(r['unitPayloads']['payloads'][1]['pylons'][1]['num'], 8)
        self.assertEqual(r['unitPayloads']['payloads'][2]['name'], "AIM-54A-MK47*6, AIM-9M*2, XT*2")
        self.assertEqual(r['unitPayloads']['payloads'][2]['tasks'][1], "Intercept")

    def test_object_with_semicolon_entry_separator(self) -> None:
        r = loads(
            textwrap.dedent(
                """\
                livery = {
                    {"A-10C_PAINT_1-a", 0 ,"A-10C_104_1-a",true};
                    {"A-10C_PAINT_1-b", 0 ,"A-10C_104_1-b",true};
                    {"A-10C_PAINT_1-c", 0 ,"A-10C_104_1-c",true};
                    {"A-10C_PAINT_1-d", 0 ,"A-10C_104_1-d",true};
                    {"A-10C_PAINT_1-e", 0 ,"A-10C_104_1-e",true};
                    {"A-10C_PAINT_1-f", 0 ,"A-10C_104_1-f",true};
                    {"A-10C_PAINT_1-g", 0 ,"A-10C_104_1-g",true};
                    {"A-10C_PAINT_1-h", 0 ,"A-10C_104_1-h",true};
                    {"A-10C_PAINT_1-i", 0 ,"A-10C_104_1-i",true};
                    {"A-10C_PAINT_1-j", 0 ,"A-10C_104_1-j",true};
                    {"A-10C_PAINT_1-k", 0 ,"A-10C_104_1-k",true};
                    {"A-10C_PAINT_1-L", 0 ,"A-10C_104_1-L",true};
                    {"A-10_Number", 0 ,"TactNumbers-USAF-Light_black",true};
                    {"A-10_Number_Noze_F", 0 ,"TactNumbers-USAF-Light_black",true};
                    {"A-10_Number_Noze_T", 0 ,"empty",true};
                    {"A-10_Number_Wheel", 0 ,"empty",true};

                }
                """
            )
        )
        self.assertEqual(len(r["livery"]), 16)

    def test_empty_file_parses(self) -> None:
        r = loads("")
        self.assertEqual(len(r), 0)

    def test_unknown_variable_use_fails_by_default(self) -> None:
        with self.assertRaises(SyntaxError):
            loads('foo = {"AH-64D_bottom_1", DIFFUSE, false}')

    def test_unknown_variable_lookup(self) -> None:
        r = loads(
            'foo = {"AH-64D_bottom_1", DIFFUSE, false}',
            unknown_variable_lookup=lambda _: "bar"
        )
        self.assertEqual(r["foo"][2], "bar")

    def test_whitespace_can_end_with_comment_before_eof(self) -> None:
        # Regression test for a peculiar old behavior where comments could end a file if
        # and only if they were not preceded by whitespace.
        loads('\n--')

    def test_block_comment(self) -> None:
        r = loads(
            textwrap.dedent(
                """\
                --[[
                this is a comment
                --]]foo = "bar"
                """
            )
        )
        self.assertEqual(r["foo"], "bar")

        loads("--[[ Old Bort Calls For 1.5.3 and Older ]]--")

        r = loads(
            textwrap.dedent(
                """\
                --[[ Comment ]]
                foo = "bar"
                """
            )
        )
        self.assertEqual(r["foo"], "bar")

    def test_single_quoted_string(self) -> None:
        r = loads("name = 'foobar'")
        self.assertEqual(r["name"], "foobar")

    def test_mixed_quote_strings(self) -> None:
        r = loads("name = 'foo \"bar\" baz'")
        self.assertEqual(r["name"], 'foo "bar" baz')

        r = loads("name = \"foo 'bar' baz\"")
        self.assertEqual(r["name"], "foo 'bar' baz")

    def test_useless_semicolon(self) -> None:
        r = loads(
            textwrap.dedent(
                """\
                name = "foo";
                other_name = "bar";
                """
            )
        )
        self.assertEqual(r["name"], "foo")
        self.assertEqual(r["other_name"], "bar")

    def test_float_beginning_with_dot(self) -> None:
        r = loads("num = .1")
        self.assertEqual(r["num"], 0.1)


if __name__ == '__main__':
    unittest.main()
