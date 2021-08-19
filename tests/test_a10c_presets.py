import unittest

from dcs.a10c_presets import A10CPresets


class A10CPresetTests(unittest.TestCase):
    def test_set_preset(self) -> None:
        a10c_presets = A10CPresets()

        self.assertEqual(a10c_presets.presets[1], 305000000)
        self.assertEqual(a10c_presets.presets[20], 266000000)

        a10c_presets.set_preset(1, 306.55)
        self.assertEqual(a10c_presets.presets[1], 306550000)

        a10c_presets.set_preset(20, 256.10)
        self.assertEqual(a10c_presets.presets[20], 256100000)

    def test_get_preset(self) -> None:
        a10c_presets = A10CPresets()

        self.assertEqual(a10c_presets.get_preset(1), 305.0)

        a10c_presets.set_preset(1, 306.55)
        self.assertEqual(a10c_presets.get_preset(1), 306.55)

        a10c_presets.set_preset(20, 256.10)
        self.assertEqual(a10c_presets.get_preset(20), 256.10)

