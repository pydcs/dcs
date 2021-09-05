import unittest
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
