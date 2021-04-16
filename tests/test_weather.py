import unittest

from dcs.terrain import Caucasus
from dcs.weather import CloudPreset, Weather


class TriggerTests(unittest.TestCase):
    def test_validate_base(self) -> None:
        preset = CloudPreset("test preset", "", "", 2, 3)

        with self.assertRaises(ValueError):
            preset.validate_base(1)

        preset.validate_base(2)
        preset.validate_base(3)

        with self.assertRaises(ValueError):
            preset.validate_base(4)

    def test_by_name(self) -> None:
        with self.assertRaises(KeyError):
            CloudPreset.by_name("does not exist")

        self.assertIsNotNone(CloudPreset.by_name("Preset1"))

    def test_all_presets(self) -> None:
        self.assertGreater(len(CloudPreset.all_presets()), 0)


class TestWeather(unittest.TestCase):
    def test_old_clouds(self) -> None:
        weather = Weather(Caucasus())
        clouds = weather.dict()["clouds"]
        self.assertNotIn("preset", clouds)

    def test_cloud_presets(self) -> None:
        weather = Weather(Caucasus())
        weather.clouds_preset = CloudPreset.by_name("Preset1")
        weather.clouds_base = 1000
        weather_dict = weather.dict()
        clouds = weather.dict()["clouds"]

        self.assertEqual(clouds["preset"], "Preset1")
        self.assertEqual(clouds["base"], 1000)
        self.assertEqual(clouds["thickness"], 200)
        self.assertEqual(clouds["density"], 0)
        self.assertEqual(clouds["iprecptns"], 0)

        weather.clouds_base = 0
        with self.assertRaises(ValueError):
            weather.dict()

        weather_dict["clouds"]["preset"] = "Preset2"
        weather.load_from_dict(weather_dict)
        self.assertEqual(weather.clouds_preset.name, "Preset2")

        del weather_dict["clouds"]["preset"]
        weather.load_from_dict(weather_dict)
        self.assertIsNone(weather.clouds_preset)
