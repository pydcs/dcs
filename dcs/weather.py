from datetime import datetime
import random
import math
from enum import Enum
from typing import Any, Dict, List, Optional
from dcs import mapping, terrain


class Wind:
    def __init__(self, direction=0, speed=0):
        self.direction = direction
        self.speed = speed

    def dict(self):
        return {"speed": self.speed, "dir": self.direction}


class Halo:
    class Preset(Enum):
        Off = "off"
        Auto = "auto"
        OnAllMediums = "AtmoHighClouds"
        OnHighVolumetricClouds = "VolumetricOnly"
        CirrusAndHighVolumetricClouds = "HighClouds"
        Cirrus = "CirrusOnly"

        def __str__(self) -> str:
            return str(self.value)

    class Crystals(Enum):
        '''Crystals are only required if not using Auto or Off Halo Presets.'''
        AllKinds = "AllKinds"
        BasicHaloCircle = "BasicHaloCircle"
        BasicHaloWithSundogs = "BasicHaloWithSundogs"
        BasicSundogsTangents = "BasicSundogsTangents"
        SundogsArcs = "SundogsArcs"
        Tangents = "Tangents"

        def __str__(self) -> str:
            return str(self.value)

    def __init__(self, preset: Preset = Preset.Auto, crystals: Optional[Crystals] = None) -> None:
        self.preset = preset
        self.crystals = crystals

    def validate_halo(self) -> None:
        if self.preset is (Halo.Preset.Auto or Halo.Preset.Off) and self.crystals is not None:
            raise ValueError(
                f"Halo preset: {self.preset} cannot have a crystals value.")

        if self.preset is not (Halo.Preset.Auto or Halo.Preset.Off) and self.crystals is None:
            raise ValueError(
                f"Halo preset: {self.preset} must have a crystals value.")

    def dict(self):
        if self.crystals:
            return {"crystalsPreset": f"{self.crystals}", "preset": f"{self.preset}"}
        else:
            return {"preset": f"{self.preset}"}

    def _make_halo_dict(self):
        self.validate_halo()
        return self.dict()


class Cyclone:
    def __init__(self):
        self.pressure_spread = 0.0
        self.centerZ = 0.0
        self.ellipticity = 0.0
        self.rotation = 0.0
        self.pressure_excess = 0
        self.centerX = 0.0

    def dict(self):
        d = {
            "pressure_spread": self.pressure_spread,
            "pressure_excess": self.pressure_excess,
            "centerZ": self.centerZ,
            "ellipticity": self.ellipticity,
            "rotation": self.rotation,
            "centerX": self.centerX
        }
        return d

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.dict()) + ')'


class CloudPreset:
    def __init__(self, name: str, ui_name: str, description: str, min_base: int,
                 max_base: int) -> None:
        self.name = name
        self.ui_name = ui_name
        self.description = description
        self.min_base = min_base
        self.max_base = max_base

    def validate_base(self, base: int) -> None:
        if not self.min_base <= base <= self.max_base:
            raise ValueError(
                f"Cloud base {base}m is out of range for {self.name}. Must be between "
                f"{self.min_base}m and {self.max_base}m.")

    @classmethod
    def by_name(cls, name: str) -> "CloudPreset":
        from dcs.cloud_presets import Clouds
        return Clouds.from_name(name).value


class Weather:
    class BaricSystem(Enum):
        Cyclone = 0
        AntiCyclone = 1
        None_ = 2

    class Preceptions(Enum):
        None_ = 0
        Rain = 1
        Thunderstorm = 2

    def __init__(self, terrain):
        self.terrain = terrain
        self.atmosphere_type = 0
        self.wind_at_ground = Wind()
        self.wind_at_2000 = Wind()
        self.wind_at_8000 = Wind()
        self.enable_fog = False
        self.halo = Halo()
        self.turbulence_at_ground = 0
        self.season_temperature = 20.0
        self.type_weather = 0
        self.qnh = 760.0
        self.cyclones = []
        self.name = "Summer, clean sky"
        self.fog_thickness = 0
        self.fog_visibility = 25
        self.visibility_distance = 80000
        self.clouds_preset: Optional[CloudPreset] = None
        self.clouds_thickness = 200
        self.clouds_density = 0
        self.clouds_base = 300
        self.clouds_iprecptns = Weather.Preceptions.None_

        self.enable_dust = False
        self.dust_density = 0

    def load_from_dict(self, d):
        self.atmosphere_type = d["atmosphere_type"]
        wind = d.get("wind", {})
        wind_at_ground = wind.get("atGround", {})
        wind_at_2000 = wind.get("at2000", {})
        wind_at_8000 = wind.get("at8000", {})
        self.wind_at_ground = Wind(wind_at_ground.get("dir", 0), wind_at_ground.get("speed", 0))
        self.wind_at_2000 = Wind(wind_at_2000.get("dir", 0), wind_at_2000.get("speed", 0))
        self.wind_at_8000 = Wind(wind_at_8000.get("dir", 0), wind_at_8000.get("speed", 0))
        halo = d.get("halo", {})
        halo_preset = halo.get("preset", {})
        halo_crystals_preset = halo.get("crystalsPreset", {})
        self.halo = Halo(halo_preset, halo_crystals_preset)
        self.enable_fog = d["enable_fog"]
        self.turbulence_at_ground = d.get("groundTurbulence", 0)
        season = d.get("season", {})
        self.season_temperature = season.get("temperature", 20)
        self.type_weather = d.get("type_weather", 0)
        self.qnh = d.get("qnh", 760)
        cyclones = d.get("cyclones", {})
        for x in cyclones:
            c = Cyclone()
            c.centerX = cyclones[x].get("centerX", 0)
            c.centerZ = cyclones[x].get("centerZ", 0)
            c.ellipticity = cyclones[x].get("ellipticity", 0)
            c.pressure_excess = cyclones[x].get("pressure_excess", 0)
            c.pressure_spread = cyclones[x].get("pressure_spread", 0)
            c.rotation = cyclones[x].get("rotation", 0)
            self.cyclones.append(c)
        self.name = d.get("name", "Summer, clean sky")
        fog = d.get("fog", {})
        self.fog_thickness = fog.get("thickness", 0)
        self.fog_visibility = fog.get("visibility", 25)
        visibility = d.get("visiblity", {})
        self.visibility_distance = visibility.get("distance", 80000)
        clouds = d.get("clouds", {})
        self.clouds_thickness = clouds.get("thickness", 200)
        self.clouds_density = clouds.get("density", 0)
        self.clouds_base = clouds.get("base", 300)
        self.clouds_iprecptns = Weather.Preceptions(clouds.get("iprecptns", 0))
        cloud_preset_name = clouds.get("preset")
        if cloud_preset_name is None:
            self.clouds_preset = None
        else:
            self.clouds_preset = CloudPreset.by_name(cloud_preset_name)

        self.enable_dust = d.get("enable_dust", False)
        self.dust_density = d.get("dust_density", 0)

    @staticmethod
    def random_normals() -> List[float]:
        rands = []
        for x in range(0, 3):
            r = max(0.0000001, random.random())
            fi = max(0.0000001, random.random())

            rands.append(math.cos(math.pi * 2 * fi) * math.sqrt(-2 * math.log(r)))
            rands.append(math.sin(math.pi * 2 * fi) * math.sqrt(-2 * math.log(r)))

        return rands

    @staticmethod
    def _init_cyclone(rands, idx, params, wtype, position):
        mainpeakexcessmod = 1

        if wtype == Weather.BaricSystem.None_ or (wtype != Weather.BaricSystem.None_ and idx != 1):
            x = math.cos(params['initangle'] + params['anglestep'] * (idx - 1) + params['deltaangle'] * rands[0])
            x *= params['distance'] + params['distancestddev'] * rands[1]
            y = math.sin(params['initangle'] + params['anglestep'] * (idx - 1) + params['deltaangle'] * rands[0])
            y *= params['distance'] + params['distancestddev'] * rands[1]
        else:
            mainpeakexcessmod = 0.22
            x = math.cos(params['initangle'] + params['anglestep'] * (idx - 1) + params['deltaangle'] * rands[0])
            x *= params['distancestddev'] * mainpeakexcessmod * rands[1]
            y = math.sin(params['initangle'] + params['anglestep'] * (idx - 1) + params['deltaangle'] * rands[0])
            y *= params['distancestddev'] * mainpeakexcessmod * rands[1]

        c = Cyclone()
        c.centerX = position.x + x
        c.centerZ = position.y + y
        c.ellipticity = 1 + rands[2] * params['ellipticitystddev']
        c.pressure_excess = math.floor(params['sign'] * abs(rands[3])
                                       * params['pressurestddev'] * mainpeakexcessmod + params['pressureoffset'])
        c.rotation = params['rotationstddev'] * rands[4]
        c.pressure_spread = params['spread'] + params['spreadstddev'] * mainpeakexcessmod * rands[5]

        if wtype == Weather.BaricSystem.AntiCyclone:
            c.pressure_spread *= 1.3
        return c

    def heavy_rain(self):
        self.atmosphere_type = 0
        self.clouds_base = 500
        self.clouds_thickness = 600
        self.clouds_density = 9
        self.clouds_iprecptns = Weather.Preceptions.Rain
        self.qnh = 745  # mm Hg

        self.wind_at_ground = Wind(286, 9)
        self.wind_at_2000 = Wind(52, 13)
        self.wind_at_8000 = Wind(286, 7)

        self.turbulence_at_ground = 14

        self.enable_fog = True
        self.fog_visibility = 1000
        self.fog_thickness = 300

    def dynamic_weather(self, system: BaricSystem, cyclones: int = 1):
        self.cyclones.clear()

        center: mapping.Point = self.terrain.bounds.center()
        self.atmosphere_type = 1
        self.type_weather = system.value

        params = {
            'initangle': 2 * math.pi * random.random(),
            'distance': 950000,
            'distancestddev': 150000,
            'spread': 900000,
            'spreadstddev': 150000,
            'pressureoffset': 1200,
            'pressurestddev': 500,
            'ellipticitystddev': 0.25,
            'rotationstddev': 1.0471975511965977461542144610932
        }

        if system == Weather.BaricSystem.None_:
            params['anglestep'] = 2 * math.pi * cyclones
            params['deltaangle'] = params['anglestep'] / 4

            for i in range(1, cyclones + 1):
                params['sign'] = random.randrange(0, 1) * 2 - 1
                self.cyclones.append(Weather._init_cyclone(Weather.random_normals(), i, params, system, center))

        else:
            params['anglestep'] = 2 * math.pi / (cyclones - 1) if cyclones > 1 else 0
            params['deltaangle'] = params['anglestep'] / 4

            params['sign'] = -1 if system == Weather.BaricSystem.Cyclone else 1

            for i in range(1, cyclones + 1):
                self.cyclones.append(Weather._init_cyclone(Weather.random_normals(), i, params, system, center))
                params['sign'] = random.randrange(0, 1) * 2 - 1

        min_pressure = min([x.pressure_excess for x in self.cyclones])
        max_pressure = max([x.pressure_excess for x in self.cyclones])
        pressure_diff = max_pressure - min_pressure
        # min_pressure = 0
        # for c in range(0, cyclones):
        #     # TODO ask ED, if we are allowed to use generateCyclones code
        #     c = Cyclone()
        #     pos = center.point_from_heading(random.randrange(0, 360), random.randrange(10*1000, 1000*1000, 1000))
        #     c.centerZ = pos.y
        #     c.centerX = pos.x
        #     c.pressure_spread = random.random() * 100000 + 800000
        #     c.rotation = random.random() * math.pi
        #
        #     c.pressure_excess = random.randrange(1200, 1800) if random.random() > 0.8 else random.randrange(600, 1300)
        #
        #     c.ellipticity = 1 + random.random() * 0.25
        #
        #     if system in [Weather.BaricSystem.Cyclone, Weather.BaricSystem.None_]:
        #         c.pressure_excess *= -1
        #
        #     min_pressure = min(min_pressure, c.pressure_excess)
        #
        #     self.cyclones.append(c)

        if pressure_diff < 200:
            self.turbulence_at_ground = random.randrange(0, 10)
        elif 200 <= min_pressure < 600:
            self.turbulence_at_ground = random.randrange(10, 25)
        else:
            self.turbulence_at_ground = random.randrange(25, 60)

    def random_thunderstorm(self):
        self.atmosphere_type = 0
        wind_dir = random.randrange(0, 359) + 180
        wind_speed = random.randrange(10, 30)
        self.wind_at_ground.direction = (wind_dir + random.randrange(-90, 90) - 180) % 360
        self.wind_at_ground.speed = wind_speed + random.randrange(-5, 10)
        self.wind_at_2000.direction = (wind_dir + random.randrange(-90, 90) - 180) % 360
        self.wind_at_2000.speed = wind_speed + random.randrange(-5, 10)
        self.wind_at_8000.direction = (wind_dir + random.randrange(-90, 90) - 180) % 360
        self.wind_at_8000.speed = wind_speed + random.randrange(-5, 10)

        self.clouds_iprecptns = Weather.Preceptions.Thunderstorm
        self.clouds_base = random.randrange(800, 1000)
        self.clouds_density = 10
        self.clouds_thickness = random.randrange(300, 900)

        self.turbulence_at_ground = random.randrange(30, 70)

        self.qnh = random.randrange(715, 750)
        self.visibility_distance = 80000

        fog_base = min(0.8, random.random())
        self.enable_fog = True
        self.fog_thickness = int(700 * fog_base)
        self.fog_visibility = int(5500 - (4000 * fog_base))

    def random(self, dt: datetime, terrain: 'terrain.Terrain'):
        """
        Creates a random weather from terrain values.

        :param dt: Datetime of the mission
        :param terrain: Terrain of the mission
        :return: None
        """
        self.season_temperature = terrain.weather(dt, self)

    def _make_cloud_dict(self) -> Dict[str, Any]:
        if self.clouds_preset is None:
            return {
                "thickness": self.clouds_thickness,
                "density": self.clouds_density,
                "base": self.clouds_base,
                "iprecptns": self.clouds_iprecptns.value,
            }

        self.clouds_preset.validate_base(self.clouds_base)

        # The hard coded values here seem to be the case for all presets. They are not
        # configurable in the ME and not defined by clouds.lua.
        return {
            "base": self.clouds_base,
            "density": 0,
            "preset": self.clouds_preset.name,
            "thickness": 200,
            "iprecptns": 0,
        }

    def dict(self) -> Dict[str, Any]:
        d = {}
        d["atmosphere_type"] = self.atmosphere_type
        d["wind"] = {"atGround": self.wind_at_ground.dict(),
                     "at2000": self.wind_at_2000.dict(),
                     "at8000": self.wind_at_8000.dict()}
        d["enable_fog"] = self.enable_fog
        d["halo"] = self.halo._make_halo_dict()
        d["groundTurbulence"] = self.turbulence_at_ground
        d["season"] = {"temperature": self.season_temperature}
        assert isinstance(self.type_weather, int)
        d["type_weather"] = self.type_weather
        d["qnh"] = self.qnh
        d["cyclones"] = {x + 1: self.cyclones[x].dict() for x in range(0, len(self.cyclones))}
        d["name"] = self.name
        d["fog"] = {"thickness": self.fog_thickness, "visibility": self.fog_visibility}
        d["visibility"] = {"distance": self.visibility_distance}
        d["clouds"] = self._make_cloud_dict()
        d["enable_dust"] = self.enable_dust
        d["dust_density"] = self.dust_density
        return d
