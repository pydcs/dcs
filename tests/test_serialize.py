import unittest
from dcs.lua.parse import loads
from dcs.lua.serialize import dumps

class TestLuaSerialize(unittest.TestCase):

    def test_all_keys_are_ints_should_arrange_in_numeric_sequence(self):
        original = {9: 9, 10: 10 }
        
        dumped = dumps(original, 'v')

        self.assertEqual('v={[9]=9,[10]=10}', dumped)

    def test_all_keys_are_string_should_arrange_in_alphabetical_order(self):
        original = {"z": 1, "a": 2, "b": 3, "y": 4}

        dumped = dumps(original, 'v')

        self.assertEqual('v={["a"]=2,["b"]=3,["y"]=4,["z"]=1}', dumped)

    def test_some_key_is_string_should_arrange_in_alphabetical_order(self):
        original = {3: 2, 10:3, "x": 4, 1: 1}

        dumped = dumps(original, 'v')

        self.assertEqual('v={[1]=1,[10]=3,[3]=2,["x"]=4}', dumped)

    def test_round_trip_of_large_and_small_floats(self):
        original = {"a": 1e20, "b": -1.5e300, "c": 2.5e-300, "d": 12345678901234567890}

        self.assertEqual(original, loads(dumps(original, 'v'))['v'])

    def test_infinity_round_trips_and_nan_is_rejected(self):
        original = {"a": float("inf"), "b": float("-inf")}

        self.assertEqual(original, loads(dumps(original, 'v'))['v'])
        with self.assertRaises(ValueError):
            dumps({"a": float("nan")}, 'v')

    def test_special_characters_in_strings_and_keys(self):
        original = {'quote"key': 'a"b', 'back\\slash': 'c\\d', 'cr\rlf\n': 'line1\r\nline2'}

        dumped = dumps(original, 'v')

        self.assertNotIn('\r', dumped)
        self.assertEqual(original, loads(dumped)['v'])

