"""
The mission module is the entry point to all pydcs functions.
"""
import copy
import os
import sys
import tempfile
import zipfile
import random
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from enum import Enum
from pathlib import Path
from typing import List, Dict, Union, Optional, Type

from dcs.coalition import Coalition
from dcs.terrain.terrain import Warehouses
from dcs.triggers import Triggers
import dcs.countries as countries
import dcs.helicopters as helicopters
import dcs.lua as lua
import dcs.mapping as mapping
import dcs.planes as planes
import dcs.task as task
import dcs.unitgroup as unitgroup
import dcs.unittype as unittype
import dcs.weather as weather
import dcs.triggers as triggers
import dcs.terrain as terrain_
import dcs.condition as condition
import dcs.action as action
import dcs.unit as unit
from dcs.country import Country
from dcs.forcedoptions import ForcedOptions
from dcs.goals import Goals
from dcs.groundcontrol import GroundControl
from dcs.point import StaticPoint, MovingPoint, PointAction, PointProperties
from dcs.translation import Translation, String, ResourceKey
from dcs.unit import Unit, Ship, Vehicle, Static
from dcs.flyingunit import Plane, Helicopter


class StartType(Enum):
    """Enum class for start types."""
    Cold = 1
    """Coldstart from ramp."""
    Warm = 2
    """Warmstart from ramp."""
    Runway = 3
    """Start from runway."""

    @staticmethod
    def from_string(s: str):
        """Returns the StartType enum for a string value.

        ["cold", "warm", "runway"]

        Args:
            s: string representation of the starttype

        Returns:
            the correct StartType.
        """
        st_map = {
            "cold": StartType.Cold,
            "warm": StartType.Warm,
            "runway": StartType.Runway
        }
        return st_map[s.lower()]


class Mission:
    """This class represents the whole dcs .miz file.

    A .miz file is a zip file containing all needed files to run a mission.
    example.miz:

      * mission
      * options
      * warehouses
      * i10n

        * DEFAULT
        * dictionary

          * mapResource
          * [localized resource files, .wav, .jpg, ...]

    Args:
        terrain: the used terrain for this mission.
    """
    _COUNTRY_IDS = {x for x in range(0, 13)} | {x for x in range(15, 47)}

    def __init__(self, terrain: Union[
            terrain_.Caucasus,
            terrain_.Nevada,
            terrain_.Normandy,
            terrain_.PersianGulf,
            terrain_.TheChannel,
            terrain_.Syria]=None
    ):
        if terrain is None:
            terrain = terrain_.Caucasus()

        self.current_unit_id = 0
        self.current_group_id = 0
        self.current_dict_id = 0
        self.filename = None

        self.translation = Translation(self)
        self.map_resource = MapResource(self)

        self._description_text = self.string("")
        self._description_bluetask = self.string("")
        self._description_redtask = self.string("")
        self._sortie = self.string("")
        self.pictureFileNameR = []
        self.pictureFileNameB = []
        self.version = 16
        self.currentKey = 0
        self.start_time = datetime.fromtimestamp(1306886400 + 43200, timezone.utc)  # 01-06-2011 12:00:00 UTC
        self.random_weather = False
        """If set to True a random weather will be generated"""
        self.terrain = terrain
        self.triggerrules = triggers.Rules()
        self.triggers = Triggers()
        self.init_script_file = None
        self.init_script = None
        self.options = Options()
        self.warehouses = Warehouses(self.terrain)
        self.goals = Goals()
        blue = Coalition("blue")
        blue.add_country(countries.Australia())
        blue.add_country(countries.Belgium())
        blue.add_country(countries.Canada())
        blue.add_country(countries.Croatia())
        blue.add_country(countries.CzechRepublic())
        blue.add_country(countries.Denmark())
        blue.add_country(countries.France())
        blue.add_country(countries.Georgia())
        blue.add_country(countries.Germany())
        blue.add_country(countries.Israel())
        blue.add_country(countries.Italy())
        blue.add_country(countries.Norway())
        blue.add_country(countries.Poland())
        blue.add_country(countries.SouthKorea())
        blue.add_country(countries.Spain())
        blue.add_country(countries.TheNetherlands())
        blue.add_country(countries.UK())
        blue.add_country(countries.USA())
        blue.add_country(countries.Turkey())

        red = Coalition("red")
        red.add_country(countries.Abkhazia())
        red.add_country(countries.Belarus())
        red.add_country(countries.China())
        red.add_country(countries.Iran())
        red.add_country(countries.Kazakhstan())
        red.add_country(countries.NorthKorea())
        red.add_country(countries.Russia())
        red.add_country(countries.Serbia())
        red.add_country(countries.SouthOssetia())
        red.add_country(countries.Syria())
        red.add_country(countries.Ukraine())

        blue.bullseye = terrain.bullseye_blue
        red.bullseye = terrain.bullseye_red

        self.coalition = {"blue": blue, "red": red}  # type: Dict[str, Coalition]

        self.map = self.terrain.map_view_default  # type: terrain_.MapView

        self.failures = {}
        self.groundControl = GroundControl()
        self.forced_options = ForcedOptions()
        self.resourceCounter = {}  # keep default or empty, old format
        self.needModules = {}
        self.weather = weather.Weather(self.terrain)
        # TODO used modules
        self.usedModules = {
            'Su-25A by Eagle Dynamics': True,
            'MiG-21Bis AI by Leatherneck Simulations': True,
            'UH-1H Huey by Belsimtek': True,
            'Su-25T by Eagle Dynamics': True,
            'F-86F Sabre by Belsimtek': True,
            'Su-27 Flanker by Eagle Dynamics': True,
            'Hawk T.1A AI by VEAO Simulations': True,
            'MiG-15bis AI by Eagle Dynamics': True,
            'Ka-50 Black Shark by Eagle Dynamics': True,
            'Combined Arms by Eagle Dynamics': True,
            'L-39C/ZA by Eagle Dynamics': True,
            'A-10C Warthog by Eagle Dynamics': True,
            'F-5E/E-3 by Belsimtek': True,
            'C-101 Aviojet': True,
            'TF-51D Mustang by Eagle Dynamics': True,
            './CoreMods/aircraft/MQ-9 Reaper': True,
            'C-101 Aviojet by AvioDev': True,
            'P-51D Mustang by Eagle Dynamics': True,
            'A-10A by Eagle Dynamics': True,
            'L-39C': True,
            'World War II AI Units by Eagle Dynamics': True,
            'MiG-15bis by Belsimtek': True,
            'F-15C': True,
            'Flaming Cliffs by Eagle Dynamics': True,
            'Bf 109 K-4 by Eagle Dynamics': True,
            'Mi-8MTV2 Hip by Belsimtek': True,
            'MiG-21Bis by Leatherneck Simulations': True,
            'M-2000C by RAZBAM Sims': True,
            'M-2000C AI by RAZBAM Sims': True,
            'FW-190D9 Dora by Eagle Dynamics': True,
            'Caucasus': True,
            'Hawk T.1A by VEAO Simulations': True,
            'F-86F Sabre AI by Eagle Dynamics': True
        }

        self.aircraft_kneeboards: Dict[unittype.FlyingType, List[Path]] = defaultdict(list)

    def load_file(self, filename: str):
        """Load a mission file (.miz) file, replacing all current data.

        Args:
            filename: path to the mission(.miz) file.

        Returns:
            bool: True if everything loaded correctly

        Raises:
            RuntimeError: if an unknown value is encountered
        """
        self.filename = filename
        self.current_unit_id = 0
        self.current_group_id = 0
        self.current_dict_id = 0
        mission_dict = {}
        options_dict = {}
        warehouse_dict = {}
        dictionary_dict = {}

        def loaddict(fname, mizfile, reserved_files):
            reserved_files.append(fname)
            with mizfile.open(fname) as mfile:
                data = mfile.read()
                data = data.decode()
                return lua.loads(data)

        with zipfile.ZipFile(filename, 'r') as miz:
            reserved_files = []
            mission_dict = loaddict('mission', miz, reserved_files)

            if mission_dict["mission"]["version"] < 16:
                print("Mission file is using an old format, be aware!", file=sys.stderr)
            options_dict = loaddict('options', miz, reserved_files)
            warehouse_dict = loaddict('warehouses', miz, reserved_files)
            dictionary_dict = loaddict('l10n/DEFAULT/dictionary', miz, reserved_files)

            if 'l10n/DEFAULT/mapResource' in miz.namelist():
                mapresource_dict = loaddict('l10n/DEFAULT/mapResource', miz, reserved_files)
                self.map_resource.load_from_dict(mapresource_dict, miz)

            self.map_resource.load_binary_files(miz, reserved_files)

        imp_mission = mission_dict["mission"]

        # import translations
        self.translation = Translation(self)
        translation_dict = dictionary_dict["dictionary"]
        for sid in translation_dict:
            self.translation.set_string(sid, translation_dict[sid], 'DEFAULT')

        self.current_dict_id = imp_mission["maxDictId"]

        # print(self.translation)

        # setup terrain_
        if imp_mission["theatre"] == 'Caucasus':
            self.terrain = terrain_.Caucasus()
        elif imp_mission["theatre"] == 'Nevada':
            self.terrain = terrain_.Nevada()
        elif imp_mission["theatre"] == 'PersianGulf':
            self.terrain = terrain_.PersianGulf()
        elif imp_mission["theatre"] == 'Normandy':
            self.terrain = terrain_.Normandy()
        elif imp_mission["theatre"] == 'TheChannel':
            self.terrain = terrain_.TheChannel()
        elif imp_mission["theatre"] == 'Syria':
            self.terrain = terrain_.Syria()
        else:
            raise RuntimeError("Unknown theatre: '{theatre}'".format(theatre=imp_mission["theatre"]))

        # import options
        self.options = Options()
        self.options.load_from_dict(options_dict["options"])

        # import warehouses
        self.warehouses = Warehouses(self.terrain)
        self.warehouses.load_dict(warehouse_dict["warehouses"])

        # import base values
        self._description_text = self.translation.get_string(imp_mission["descriptionText"])
        self._description_bluetask = self.translation.get_string(imp_mission["descriptionBlueTask"])
        self._description_redtask = self.translation.get_string(imp_mission["descriptionRedTask"])
        self._sortie = self.translation.get_string(imp_mission["sortie"])
        for pic in sorted(imp_mission["pictureFileNameR"]):
            self.pictureFileNameR.append(imp_mission["pictureFileNameR"][pic])
        for pic in sorted(imp_mission["pictureFileNameB"]):
            self.pictureFileNameB.append(imp_mission["pictureFileNameB"][pic])
        self.version = imp_mission["version"]
        self.currentKey = imp_mission["currentKey"]
        imp_date = imp_mission.get("date", {"Year": 2011, "Month": 6, "Day": 1})
        hour = int(imp_mission["start_time"] / 3600)
        minutes = int(imp_mission["start_time"] / 60) - hour * 60
        if self.version > 11:
            self.start_time = datetime(
                year=imp_date["Year"],
                month=imp_date["Month"],
                day=imp_date["Day"],
                hour=hour,
                minute=minutes,
                second=imp_mission["start_time"] % 60
            )
        else:
            self.start_time = datetime.fromtimestamp(1306886400 + imp_mission["start_time"], timezone.utc)
        self.usedModules = imp_mission.get("usedModules", None)
        self.needModules = imp_mission.get("needModules", None)

        # groundControl
        self.groundControl = GroundControl()
        self.groundControl.load_from_dict(imp_mission.get("groundControl"))

        # goals
        self.goals = Goals()
        self.goals.load_from_dict(imp_mission["goals"])

        self.init_script_file = imp_mission.get("initScriptFile")
        self.init_script = imp_mission.get("initScript")

        # triggers
        self.triggers = Triggers()
        self.triggers.load_from_dict(imp_mission["triggers"])

        # this will import trigrules and trig
        self.triggerrules.load_from_dict(self, imp_mission["trigrules"])

        # failures
        self.failures = imp_mission["failures"]  # TODO

        # forced options
        self.forced_options.load_from_dict(imp_mission["forcedOptions"])

        # map
        self.map.load_from_dict(imp_mission["map"])

        # weather
        self.random_weather = False
        imp_weather = imp_mission["weather"]
        self.weather = weather.Weather(self.terrain)
        self.weather.load_from_dict(imp_weather)

        # import coalition with countries and units
        for col_name in ["blue", "red", "neutral"]:
            if col_name in imp_mission["coalition"]:
                self.coalition[col_name] = Coalition(col_name, imp_mission["coalition"][col_name]["bullseye"])
                self.coalition[col_name].load_from_dict(self, imp_mission["coalition"][col_name])

        return True

    def sortie_text(self) -> str:
        """Returns the mission sortie text.

        Returns:
            the mission sortie text
        """
        return str(self._sortie)

    def set_sortie_text(self, text: str):
        """Sets the mission sortie text.

        Args:
            text: text to set.
        """
        self._sortie.set(text)

    def description_text(self) -> str:
        """Returns the mission description text.

        Returns:
            the mission description text
        """
        return str(self._description_text)

    def set_description_text(self, text: str):
        """Sets the mission descsription text.

        Args:
            text: text to set.
        """
        self._description_text.set(text)

    def description_bluetask_text(self) -> str:
        """Returns the blue task description text.

        Returns:
            the blue task description text
        """
        return str(self._description_bluetask)

    def set_description_bluetask_text(self, text: str):
        """Sets the red coalitions task description text.

        Args:
            text: text to set.
        """
        self._description_bluetask.set(text)

    def description_redtask_text(self) -> str:
        """Returns the red task description text.

        Returns:
            the red task description text
        """
        return str(self._description_redtask)

    def set_description_redtask_text(self, text: str):
        """Sets the red coalitions task description text.

        Args:
            text: text to set.
        """
        self._description_redtask.set(text)

    def add_picture_red(self, filepath: str) -> ResourceKey:
        """Adds a new briefing picture to the red coalition.

        Args:
            filepath: path to the image, jpg or bmp.

        Returns:
            the resource key of the picture
        """
        reskey = self.map_resource.add_resource_file(filepath)
        self.pictureFileNameR.append(reskey)
        return reskey

    def add_picture_blue(self, filepath: str) -> ResourceKey:
        """Adds a new briefing picture to the blue coalition.

        Args:
            filepath: path to the image, jpg or bmp.

        Returns:
            the resource key of the picture
        """
        reskey = self.map_resource.add_resource_file(filepath)
        self.pictureFileNameB.append(reskey)
        return reskey

    def next_group_id(self):
        """Get the next free group id

        Returns:
            a new group id
        """
        self.current_group_id += 1
        return self.current_group_id

    def next_unit_id(self):
        """Get the next free unit id

        Returns:
            a new unit id
        """
        self.current_unit_id += 1
        return self.current_unit_id

    def next_dict_id(self):
        """Get the next free dictionary id

        Returns:
            a new dictionary id
        """
        self.current_dict_id += 1
        return self.current_dict_id

    def eplrs_for(self, group: str) -> Dict[int, int]:
        """Searches all vehicle eplrs using groups and writes them in a mapping

        Args:
            group: which group to look for eplrs task, ["helicopter", "plane", "vehicle"]

        Returns:
            a dict mapping groups to used eplrs id
        """
        eplrs_map = {}
        for col in self.coalition:
            for c_name, country in self.coalition[col].countries.items():
                search_group = []
                if group == "helicopter":
                    search_group = country.helicopter_group
                elif group == "plane":
                    search_group = country.plane_group
                elif group == "vehicle":
                    search_group = country.vehicle_group
                for grp in search_group:
                    if grp.points:
                        eplrs = grp.points[0].find_task(task.EPLRS)
                        if eplrs:
                            eplrs_map[grp.id] = eplrs.eplrs
        return eplrs_map

    def next_eplrs(self, group_type: str) -> int:
        """Get next eplrs for the given group type.

        Args:
            group_type: one of "vehicle", "helicopter" or "plane"

        Returns:
            int: the next eplrs id to use
        """
        eplrs_usage = self.eplrs_for(group_type)
        eplrs_id = 1
        for ep_id in [eplrs_usage[x] for x in eplrs_usage]:
            if ep_id != eplrs_id:
                return eplrs_id
            eplrs_id += 1
        return eplrs_id

    def string(self, s: str, lang: str = 'DEFAULT') -> String:
        """Create a new String() object for translation

        Args:
            s: string for lang
            lang: language for s

        Returns:
            String: A new String() object for string s
        """
        return self.translation.create_string(s, lang)

    def static(self, name, _type: Type[unittype.UnitType]) -> Static:
        """Creates a plain static object to be added to a group

        Args:
            name: of the static object
            _type(StaticType): type of the static

        Returns:
            Static: a new static object
        """
        return Static(self.next_unit_id(), self.string(name), _type)

    def static_group(self, country, name, _type: Type[unittype.UnitType], position: mapping.Point,
                     heading=0, hidden=False, dead=False):
        """Add a static group with 1 static object.

        Args:
            country(Country): the object belongs too
            name: name of the group
            _type: what kind of object
            position(dcs.mapping.Point): where to place the object
            heading: of the object
            hidden: should the object be hidden on the map
            dead: should the object be rendered as dead

        Returns:
            StaticGroup: the new static group
        """
        sg = unitgroup.StaticGroup(self.next_group_id(), self.string(name))

        s = self.static(name + " object", _type)
        s.position = copy.copy(position)
        s.heading = heading
        sg.add_unit(s)

        sg.hidden = hidden
        sg.dead = dead

        sp = StaticPoint()
        sp.position = s.position
        sg.add_point(sp)

        country.add_static_group(sg)
        return sg

    def farp(self,
             country,
             name,
             position: mapping.Point,
             frequency=127.5,
             modulation=task.Modulation.AM.value,
             callsign_id=1,
             heading=0,
             hidden=False,
             dead=False):
        """Add a static group with 1 static object.

        Args:
            country(Country): the object belongs too
            name: name of the farp
            position(dcs.mapping.Point): where to place the object
            frequency: radio frequency for ATC operation
            modulation: AM or FM
            callsign_id: index of the callsign to use
            heading: of the object
            hidden: should the object be hidden on the map
            dead: should the object be rendered as dead

        Returns:
            StaticGroup: the new farp group
        """
        sg = unitgroup.StaticGroup(self.next_group_id(), self.string(name))

        s = unit.FARP(self.next_unit_id(), self.string(name), frequency, modulation, callsign_id)
        s.position = copy.copy(position)
        s.heading = heading
        sg.add_unit(s)

        sg.hidden = hidden
        sg.dead = dead

        sp = StaticPoint()
        sp.position = s.position
        sg.add_point(sp)

        country.add_static_group(sg)
        return sg

    def vehicle(self, name, _type: Type[unittype.VehicleType]) -> Vehicle:
        """Creates a plain vehicle unit to be added to a group

        Args:
            name: of the vehicle
            _type: vehicle type

        Returns:
            Vehicle: a new vehicle unit.
        """
        if not issubclass(_type, unittype.VehicleType):
            raise TypeError("_type not a unittype.VehicleType class: " + repr(_type))
        return Vehicle(self.next_unit_id(), self.string(name), _type.id)

    def vehicle_group(self, country, name, _type: Type[unittype.VehicleType], position: mapping.Point,
                      heading=0, group_size=1,
                      formation=unitgroup.VehicleGroup.Formation.Line,
                      move_formation: PointAction=PointAction.OffRoad) -> unitgroup.VehicleGroup:
        """Adds a new vehicle group to the given country.

        Args:
                country(Country):which the vehicle group will belong too
            name: of the vehicle group
            _type: type of vehicle
            position: :py:class:`dcs.mapping.Point` where the new group will be placed
            heading: initial heading of the group, only used if no additional waypoints
            group_size: how many vehicles to add
            formation: formation in which the group should be placed
            move_formation: formation the group should use for moving

        Returns:
            VehicleGroup: the new vehicle group object
        """
        vg = unitgroup.VehicleGroup(self.next_group_id(), self.string(name))

        for i in range(1, group_size + 1):
            v = self.vehicle(name + " Unit #{nr}".format(nr=i), _type)
            v.position.x = position.x
            v.position.y = position.y + (i - 1) * 20
            v.heading = heading
            vg.add_unit(v)

        wp = vg.add_waypoint(vg.units[0].position, move_formation, 0)
        wp.ETA_locked = True
        if _type.eplrs:
            wp.tasks.append(task.EPLRS(self.next_eplrs("vehicle")))

        vg.formation(formation, heading)

        country.add_vehicle_group(vg)
        return vg

    def vehicle_group_platoon(self, country, name,
                              types: List[Type[unittype.VehicleType]],
                              position: mapping.Point,
                              heading=0,
                              formation=unitgroup.VehicleGroup.Formation.Line,
                              move_formation: PointAction=PointAction.OffRoad) -> unitgroup.VehicleGroup:
        """Adds a new vehicle group to the given country and given vehicle types.

        Args:
                country(Country):which the vehicle group will belong too
            name: of the vehicle group
            types: a list of vehicle types that will be used the units
            position: :py:class:`dcs.mapping.Point` where the new group will be placed
            heading: initial heading of the group, only used if no additional waypoints
            formation: formation in which the group should be placed
            move_formation: formation the group should use for moving

        Returns:
            VehicleGroup: the new vehicle group object
        """
        vg = unitgroup.VehicleGroup(self.next_group_id(), self.string(name))

        eplrs = False
        for i in range(0, len(types)):
            utype = types[i]
            v = self.vehicle(name + " Unit #{nr}".format(nr=i + 1), utype)
            v.position.x = position.x
            v.position.y = position.y + i * 20
            v.heading = heading
            if utype.eplrs:
                eplrs = True
            vg.add_unit(v)

        wp = vg.add_waypoint(vg.units[0].position, move_formation, 0)
        wp.ETA_locked = True
        if eplrs:
            wp.tasks.append(task.EPLRS(self.next_eplrs("vehicle")))

        vg.formation(formation, heading)

        country.add_vehicle_group(vg)
        return vg

    def ship(self, name, _type: Type[unittype.ShipType]) -> Ship:
        """Creates a plain ship unit to be added to a group

        Args:
            name: of the ship
            _type: ship type

        Returns:
            Ship: a new ship unit.
        """
        return Ship(self.next_unit_id(), self.string(name), _type)

    def ship_group(self, country, name, _type: Type[unittype.ShipType],
                   position: mapping.Point, heading=0, group_size=1) -> unitgroup.ShipGroup:
        """Adds a ship group to the given country.

        Args:
            country(Country): which the ship group will belong too
            name: of the ship group
            _type: which kind of ship to add
            position(dcs.mapping.Point): where the new group will be placed
            heading: initial heading of the group, only used if no additional waypoints
            group_size: how many ships of _type

        Returns:
            ShipGroup: the new ship group object
        """
        sg = unitgroup.ShipGroup(self.next_group_id(), self.string(name))

        for i in range(1, group_size + 1):
            v = self.ship(name + " Unit #{nr}".format(nr=i), _type)
            v.position.x = position.x
            v.position.y = position.y + (i - 1) * 20
            v.heading = heading
            sg.add_unit(v)

        wp = sg.add_waypoint(position, 20)
        wp.ETA_locked = True

        country.add_ship_group(sg)
        return sg

    def plane_group(self, name) -> unitgroup.PlaneGroup:
        """This creates a plain plane group without any units or starting points.

        This method is a advanced interface method not intended for simple use.
        For adding full featured plane group see

         * :py:meth:`flight_group`
         * :py:meth:`flight_group_inflight`
         * :py:meth:`flight_group_from_airport`

        Args:
            name: Group name

        Returns:
            PlaneGroup: A new :py:class:`dcs.unitgroup.PlaneGroup`
        """
        return unitgroup.PlaneGroup(self.next_group_id(), self.string(name))

    def remove_plane_group(self, pgroup: unitgroup.PlaneGroup):
        for coln, col in self.coalition.items():
            for cn in col.countries:
                c = col.countries[cn]
                for i in range(0, len(c.plane_group)):
                    if c.plane_group[i].id == pgroup.id:
                        self.clear_parking_slots(c.plane_group[i])
                        del c.plane_group[i]
                        return True
        return False

    def clear_parking_slots(self, pgroup: unitgroup.PlaneGroup):
        if pgroup.airport_id():
            airport = self.terrain.airport_by_id(pgroup.airport_id())
            for u in pgroup.units:
                airport.clear_parking_slot(u.parking)
            return True

        return False

    def plane(self, name, _type: Type[planes.PlaneType], country: Country):
        """Creates a new plane unit.

        This method is a advanced interface method not intended for simple usage.
        For adding full a featured plane group see

         * :py:meth:`flight_group`
         * :py:meth:`flight_group_inflight`
         * :py:meth:`flight_group_from_airport`

        Args:
            name: unit name
            _type: type of the plane
            country(Country): the plane belongs, needed for default liveries

        Return:
            Plane: A new :py:class:`dcs.unit.Plane`
        """
        return Plane(self.next_unit_id(), self.string(name), _type, country)

    def helicopter(self, name, _type: Type[helicopters.HelicopterType], country: Country):
        """Creates a new helicopter unit.

        This method is a advanced interface method not intended for simple usage.
        For adding full a featured helicopter group see

         * :py:meth:`flight_group`
         * :py:meth:`flight_group_inflight`
         * :py:meth:`flight_group_from_airport`

        Args:
            name: unit name
            _type: type of the helicopter
            country(Country): the helicopter belongs, needed for default liveries

        Returns:
            Helicopter: A new :py:class:`dcs.unit.Helicopter`
        """
        return Helicopter(self.next_unit_id(), self.string(name), _type, country)

    def aircraft(self, name, _type: Type[unittype.FlyingType], country: Country) -> Union[Plane, Helicopter]:
        """Creates a new plane or helicopter unit, depending on the _type.

        This method is a advanced interface method not intended for simple usage.
        For adding full a featured plane/helicopter group see

         * :py:meth:`flight_group`
         * :py:meth:`flight_group_inflight`
         * :py:meth:`flight_group_from_airport`

        Args:
            name: unit name
            _type: type of the aircraft
            country(Country): the aircraft belongs, needed for default liveries

        Returns:
            Helicopter: A new :py:class:`dcs.unit.Plane` or :py:class:`dcs.unit.Helicopter`
        """
        if _type.helicopter:
            return Helicopter(self.next_unit_id(), self.string(name), _type, country)
        return Plane(self.next_unit_id(), self.string(name), _type, country)

    def helicopter_group(self, name) -> unitgroup.HelicopterGroup:
        """Creates a plain helicopter group without any units or starting points.

        This method is a advanced interface method not intended for simple usage.
        For adding a full featured helicopter group see

         * :py:meth:`flight_group`
         * :py:meth:`flight_group_inflight`
         * :py:meth:`flight_group_from_airport`

        Args:
             name: Group name

        Returns:
            HelicopterGroup: A new :py:class:`dcs.unitgroup.HelicopterGroup`
        """
        return unitgroup.HelicopterGroup(self.next_group_id(), self.string(name))

    @classmethod
    def _assign_callsign(cls, _country, group: unitgroup.FlyingGroup):
        callsign_name = None
        category = "Air" if group.units[0].unit_type.category == "Interceptor" else group.units[0].unit_type.category
        if category in _country.callsign:
            callsign_name = _country.next_callsign_category(category)

        i = 1
        for unit in group.units:
            if category in _country.callsign:
                unit.callsign_dict["name"] = callsign_name + str(1) + str(i)
                unit.callsign_dict[3] = i
            else:
                unit.callsign = _country.next_callsign_id()
            i += 1

    @staticmethod
    def _load_tasks(mp: MovingPoint, maintask: task.MainTask):
        for t in maintask.perform_task:
            ptask = t()
            ptask.auto = True
            mp.tasks.append(ptask)
        return mp

    def _flying_group_from_airport(self, _country, group: unitgroup.FlyingGroup,
                                   maintask: task.MainTask,
                                   airport: terrain_.Airport,
                                   start_type: StartType=StartType.Cold,
                                   parking_slots: List[terrain_.ParkingSlot] = None) -> unitgroup.FlyingGroup:

        for unit in group.units:
            spos = airport.position
            if start_type != StartType.Runway:
                parking_slot = parking_slots.pop(0) if parking_slots else airport.free_parking_slot(
                    unit.unit_type)
                if parking_slot is None:
                    raise terrain_.NoParkingSlotError(
                        "No free parking slot at {airport} for {craft}".format(
                            airport=airport.name,
                            craft=unit.unit_type.id))
                spos = parking_slot.position
                unit.set_parking(parking_slot)
            unit.position = copy.copy(spos)

        # if start_type == StartType.Runway:
        #     airport.occupy_runway(group)

        group.load_task_default_loadout(maintask)

        self._assign_callsign(_country, group)

        point_start_type_map = {
            StartType.Cold: ("TakeOffParking", PointAction.FromParkingArea),
            StartType.Warm: ("TakeOffParkingHot", PointAction.FromParkingAreaHot),
            StartType.Runway: ("TakeOff", PointAction.FromRunway)
        }
        mp = MovingPoint()
        mp.type = point_start_type_map[start_type][0]
        mp.action = point_start_type_map[start_type][1]
        mp.position = copy.copy(group.units[0].position)
        mp.airdrome_id = airport.id
        mp.alt = group.units[0].alt
        mp.properties = PointProperties()
        Mission._load_tasks(mp, maintask)
        first_unit = group.units[0]
        if first_unit.unit_type.eplrs:
            mp.tasks.append(task.EPLRS(self.next_eplrs("helicopter" if first_unit.unit_type.helicopter else "plane")))

        group.add_point(mp)

        return group

    def _flying_group_inflight(self, _country, group: unitgroup.FlyingGroup,
                               maintask: task.MainTask, altitude, speed) -> unitgroup.FlyingGroup:

        i = 0
        for unit in group.units:
            unit.alt = altitude
            unit.position.x += i * 10
            unit.speed = speed / 3.6
            i += 1

        self._assign_callsign(_country, group)

        group.load_task_default_loadout(maintask)

        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = PointAction.TurningPoint
        mp.position = copy.copy(group.units[0].position)
        mp.alt = altitude
        mp.speed = speed / 3.6
        mp.properties = PointProperties()

        Mission._load_tasks(mp, maintask)
        first_unit = group.units[0]
        if first_unit.unit_type.eplrs:
            mp.tasks.append(task.EPLRS(self.next_eplrs("helicopter" if first_unit.unit_type.helicopter else "plane")))

        group.add_point(mp)

        return group

    def flight_group_inflight(self,
                              country,
                              name: str,
                              aircraft_type: Type[unittype.FlyingType],
                              position: mapping.Point,
                              altitude: int,
                              speed=None,
                              maintask: Optional[Type[task.MainTask]] = None,
                              group_size: int = 1
                              ) -> Union[unitgroup.PlaneGroup, unitgroup.HelicopterGroup]:
        """Add a new Plane/Helicopter group inflight.

        The type of the resulting group depends on the given aircraft_type.

        Args:
            country(Country): the new group will belong to
            name: of the new group
            aircraft_type(FlyingType): type of all units in the group
            position(dcs.mapping.Point): where the new group will be placed
            altitude: of the new group
            speed: of the new group, if none a default will be picked
            maintask(MainTask): if none the default task for the aircraft_type wil be used
            group_size: number of units in the group(maximum 4 or 1 for certain types)

        Returns:
            FlyingGroup: a new :py:class:`dcs.unitgroup.PlaneGroup` or :py:class:`dcs.unitgroup.HelicopterGroup`
        """
        if maintask is None:
            maintask = aircraft_type.task_default

        if aircraft_type.helicopter:
            ag = self.helicopter_group(name)
            speed = speed if speed else 200
        else:
            ag = self.plane_group(name)
            speed = speed if speed else 600
        ag.task = maintask.name
        group_size = min(group_size, aircraft_type.group_size_max)

        for i in range(1, group_size + 1):
            p = self.aircraft(name + " Pilot #{nr}".format(nr=i), aircraft_type, country)
            p.position = copy.copy(position)
            p.fuel *= 0.9
            ag.add_unit(p)

        country.add_aircraft_group(self._flying_group_inflight(country, ag, maintask, altitude, speed))
        return ag

    def flight_group_from_airport(self,
                                  country: Country,
                                  name,
                                  aircraft_type: Type[unittype.FlyingType],
                                  airport: terrain_.Airport,
                                  maintask: Type[task.MainTask] = None,
                                  start_type: StartType = StartType.Cold,
                                  group_size=1,
                                  parking_slots: List[terrain_.ParkingSlot] = None) -> \
            Union[unitgroup.PlaneGroup, unitgroup.HelicopterGroup]:
        """Add a new Plane/Helicopter group at the given airport.

        Runway, warm/cold start depends on the given start_type.

        Args:
            country(Country): Country object the plane group belongs to
            name: Name of the aircraft group
            maintask(MainTask): Task of the aircraft group
            aircraft_type(FlyingType): FlyingType class that describes the aircraft_type
            airport(terrain_.Airport): Airport object on which to spawn the helicopter
            start_type(StartType): Start from runway, cold or warm parking position
            parking_slots: List of parking slots to use for aircrafts
            group_size: number of units in the group(maximum 4 or 1 for certain types)

        Returns:
            FlyingGroup: a new :py:class:`dcs.unitgroup.PlaneGroup` or :py:class:`dcs.unitgroup.HelicopterGroup`
        """
        if maintask is None:
            maintask = aircraft_type.task_default

        ag = self.helicopter_group(name) if aircraft_type.helicopter else self.plane_group(name)
        ag.task = maintask.name
        group_size = min(group_size, aircraft_type.group_size_max)

        for i in range(1, group_size + 1):
            p = self.aircraft(name + " Pilot #{nr}".format(nr=i), aircraft_type, country)
            ag.add_unit(p)

        country.add_aircraft_group(
            self._flying_group_from_airport(country, ag, maintask, airport, start_type, parking_slots))
        return ag

    def flight_group_from_unit(self,
                               country: Country,
                               name,
                               aircraft_type: Type[unittype.FlyingType],
                               pad_group: Union[unitgroup.ShipGroup, unitgroup.StaticGroup],
                               maintask: Type[task.MainTask] = None,
                               start_type: StartType = StartType.Cold,
                               group_size=1) -> Union[unitgroup.PlaneGroup, unitgroup.HelicopterGroup]:
        """Add a new Plane/Helicopter group at the given FARP or carrier unit.

        Args:
            country(Country): Country object the plane group belongs to
            name: Name of the aircraft group
            maintask(MainTask): Task of the aircraft group
            aircraft_type(FlyingType): FlyingType class that describes the aircraft_type
            pad_group(Unit): Group(Ship, FARP) on which to spawn
            start_type(StartType): Start from runway, cold or warm parking position, ignored for now
            group_size: number of units in the group(maximum 4 or 1 for certain types)

        Returns:
            FlyingGroup: a new :py:class:`dcs.unitgroup.PlaneGroup` or :py:class:`dcs.unitgroup.HelicopterGroup`
        """
        if maintask is None:
            maintask = aircraft_type.task_default

        ag = self.helicopter_group(name) if aircraft_type.helicopter else self.plane_group(name)
        ag.task = maintask.name
        group_size = min(group_size, aircraft_type.group_size_max)

        for i in range(1, group_size + 1):
            p = self.aircraft(name + " Pilot #{nr}".format(nr=i), aircraft_type, country)
            ag.add_unit(p)

        ag.units[0].position = copy.copy(pad_group.position)
        ag.formation_rectangle(pad_group.units[0].heading, 10)

        ag.load_task_default_loadout(maintask)

        self._assign_callsign(country, ag)

        point_start_type_map = {
            StartType.Cold: ("TakeOffParking", PointAction.FromParkingArea),
            StartType.Warm: ("TakeOffParkingHot", PointAction.FromParkingAreaHot),
            StartType.Runway: ("TakeOff", PointAction.FromRunway)
        }
        mp = MovingPoint()
        mp.type = point_start_type_map[start_type][0]
        mp.action = point_start_type_map[start_type][1]
        mp.position = copy.copy(ag.units[0].position)
        mp.helipad_id = pad_group.units[0].id
        mp.link_unit = pad_group.units[0].id
        mp.alt = ag.units[0].alt
        mp.properties = PointProperties()
        Mission._load_tasks(mp, maintask)
        first_unit = ag.units[0]
        if first_unit.unit_type.eplrs:
            mp.tasks.append(task.EPLRS(self.next_eplrs("helicopter" if first_unit.unit_type.helicopter else "plane")))

        ag.add_point(mp)

        country.add_aircraft_group(ag)
        return ag

    def flight_group(self,
                     country: Country,
                     name: str,
                     aircraft_type: Type[unittype.FlyingType],
                     airport: Optional[terrain_.Airport],
                     position: Optional[mapping.Point],
                     altitude=3000,
                     speed=500,
                     maintask: Optional[Type[task.MainTask]] = None,
                     start_type: StartType = StartType.Runway,
                     group_size=1
                     ) -> unitgroup.FlyingGroup:
        """This is wrapper around flight_group_inflight and flight_group_from_airport.

        Depending on the airport parameter a flight group will added inflight or on an airport.

        Args:
            country(Country): Country object the plane group belongs to
            name: Name of the aircraft group
            aircraft_type(FlyingType): FlyingType class that describes the aircraft_type
            airport(terrain_.Airport): Airport object on which to spawn the helicopter
            position(dcs.mapping.Point): where the new group will be placed, if inflight
            altitude: initial altitude of the group if inflight
            speed: initial speed of the group if inflight
            maintask(MainTask): Task of the aircraft group
            start_type(StartType): Start from runway, cold or warm parking position
            group_size: number of units in the group(maximum 4 or 1 for certain types)

        Returns:
            FlyingGroup: a new :py:class:`dcs.unitgroup.PlaneGroup` or :py:class:`dcs.unitgroup.HelicopterGroup`
        """
        if airport:
            fg = self.flight_group_from_airport(country, name, aircraft_type,
                                                airport, maintask, start_type, group_size)
        else:
            fg = self.flight_group_inflight(country, name, aircraft_type,
                                            position, altitude, speed, maintask, group_size)

        return fg

    def awacs_flight(self,
                     country: Country,
                     name: str,
                     plane_type: Type[planes.PlaneType],
                     airport: Optional[terrain_.Airport],
                     position: mapping.Point,
                     race_distance=30 * 1000,
                     heading=90,
                     altitude=4500,
                     speed=550,
                     start_type: StartType = StartType.Cold,
                     frequency=140) -> unitgroup.PlaneGroup:
        """Add an AWACS flight group.

        This is simple way to add an AWACS flight group to your mission.
        It needs an initial orbit point, race distance and heading from this point.

        If an airport is given the AWACS flight will start from there otherwise,
        it will placed 2 km in front of the reference position.

        Args:
            country(Country): Country object the awacs group belongs to
            name: of the AWACS flight
            plane_type(PlaneType): AWACS plane type. e.g E_3A
            airport(terrain_.Airport): starting airport, use None if you want it to spawn inflight
            position(dcs.mapping.Point): reference point for the race-track
            race_distance: distance for the race-track pattern
            heading: direction from the referene position
            altitude: of the AWACS race-track
            speed: of the AWACS flight
            start_type(StartType): of the flight if starts from airport
            frequency: VHF-AM frequencey in mhz

        Returns:
            PlaneGroup: the created AWACS flight group
        """
        if airport:
            awacs = self.flight_group_from_airport(country, name, plane_type, airport, task.AWACS, start_type)
            wp = awacs.add_runway_waypoint(airport)
        else:
            p = position.point_from_heading((heading + 180) % 360, 2000)
            awacs = self.flight_group_inflight(country, name, plane_type, p, altitude, speed, task.AWACS)
            p = position.point_from_heading(heading + 180, 1000)
            wp = awacs.add_waypoint(p, altitude, speed)

        wp.tasks.append(task.SetFrequencyCommand(frequency))

        wp = awacs.add_waypoint(position, altitude, speed)
        wp.tasks.append(task.OrbitAction(altitude, speed, task.OrbitAction.OrbitPattern.RaceTrack))

        p = position.point_from_heading(heading, race_distance)
        awacs.add_waypoint(p, altitude, speed)

        return awacs

    def refuel_flight(self,
                      country,
                      name: str,
                      plane_type: Type[planes.PlaneType],
                      airport: Optional[terrain_.Airport],
                      position: mapping.Point,
                      race_distance=30 * 1000,
                      heading=90,
                      altitude=4500,
                      speed=407,
                      start_type: StartType = StartType.Cold,
                      frequency=140,
                      tacanchannel="10X") -> unitgroup.PlaneGroup:
        """Add an refuel flight group.

        This is simple way to add an refuel flight group to your mission.
        It needs an initial orbit point, race distance and heading from this point.

        If an airport is given the refuel flight will start from there otherwise,
        it will placed 2 km in front of the reference position.

        Args:
            country(Country): Country object the awacs group belongs to
            name: of the refuel flight
            plane_type(PlaneType): refuel plane type. e.g KC_135
            airport(terrain_.Airport): starting airport, use None if you want it to spawn inflight
            position(dcs.mapping.Point): reference point for the race-track
            race_distance: distance for the race-track pattern
            heading: direction from the referene position
            altitude: of the refuel race-track
            speed: of the refuel flight
            start_type(StartType): of the flight if starts from airport
            frequency: VHF-AM frequencey in mhz
            tacanchannel: if the PlaneType supports tacan this channel will be set.

        Returns:
            PlaneGroup: the created refuel flight group
        """
        if airport:
            tanker = self.flight_group_from_airport(country, name, plane_type, airport,
                                                    task.Refueling, start_type=start_type)
            wp = tanker.add_runway_waypoint(airport)
        else:
            p = position.point_from_heading((heading + 180) % 360, 2000)
            tanker = self.flight_group_inflight(country, name, plane_type, p, altitude, speed, task.Refueling)
            p = position.point_from_heading(heading + 180, 1000)
            wp = tanker.add_waypoint(p, altitude, speed)

        wp.tasks.append(task.SetFrequencyCommand(frequency))

        if plane_type.tacan:
            channel = int(tacanchannel[:-1])
            modechannel = tacanchannel[-1]
            tanker.points[0].tasks.append(task.ActivateBeaconCommand(channel, modechannel))

        wp = tanker.add_waypoint(position, altitude, speed)
        wp.tasks.append(task.OrbitAction(altitude, speed, task.OrbitAction.OrbitPattern.RaceTrack))

        p = position.point_from_heading(heading, race_distance)
        tanker.add_waypoint(p, altitude, speed)

        return tanker

    def escort_flight(self,
                      country,
                      name: str,
                      escort_type: Type[planes.PlaneType],
                      airport: Optional[terrain_.Airport],
                      group_to_escort: unitgroup.FlyingGroup,
                      start_type: StartType = StartType.Cold,
                      group_size=2) -> unitgroup.PlaneGroup:
        """Add an escort flight group to the mission.

        An escort flight is a flight group that will use the :py:class:`dcs.task.EscortTaskAction`
        to escort another flight group.

        If no airport is given, the escort flight will spawn near the group to escort.

        Args:
            country(Country): the escort flight belongs too
            name: of the flight group
            escort_type(PlaneType): PlaneType for the escort task
            airport(terrain_.Airport): starting airport, use None if you want it to spawn inflight
            group_to_escort: id of the group to escort
            start_type(StartType): of the flight if starts from airport
            group_size: how many planes should be in the escort flight

        Returns:
            PlaneGroup: the created escort group
        """
        second_point_group = group_to_escort.points[1]
        if airport:
            eg = self.flight_group_from_airport(
                country, name, escort_type, airport, task.Escort, start_type=start_type, group_size=group_size
            )
            eg.add_runway_waypoint(airport)
        else:
            eg = self.flight_group_inflight(
                country, name, escort_type,
                mapping.Point(group_to_escort.points[0].position.x - 10 * 1000, group_to_escort.points[0].position.y),
                second_point_group.alt + 200,
                maintask=task.Escort,
                group_size=group_size
            )

        eg.add_waypoint(second_point_group.position, second_point_group.alt)
        eg.points[0].tasks[0] = task.EscortTaskAction(group_to_escort.id, lastwpt=len(group_to_escort.points))

        return eg

    def patrol_flight(self,
                      country,
                      name: str,
                      patrol_type: Type[planes.PlaneType],
                      airport: Optional[terrain_.Airport],
                      pos1,
                      pos2,
                      start_type: StartType = StartType.Cold,
                      speed=600,
                      altitude=4000,
                      max_engage_distance=60*1000,
                      group_size=2) -> unitgroup.PlaneGroup:
        """Add an patrol flight group to the mission.

        A patrol flight is a flight group that will fly a orbit between 2 given points and
        will engage any incoming air threats within max_engage_distance.

        If no airport is given, the patrol flight will spawn near the first patrol point(pos1).

        Args:
            country(Country): the flight belongs too
            name: name of the patrol flight
            patrol_type(PlaneType): PlaneType for the patrol flight
            airport(terrain_.Airport): starting airport, use None if you want it to spawn inflight
            pos1(dcs.mapping.Point): first orbit waypoint
            pos2(dcs.mapping.Point): second orbit waypoint
            start_type(StartType): of the flight if starts from airport
            speed: orbit speed
            altitude: initial altitude and orbit altitude
            max_engage_distance: the distance in KM the patrol flight will respond to enemy threats
            group_size: how many planes should be in the flight group

        Returns:
            PlaneGroup: the created patrol group
        """
        if airport:
            eg = self.flight_group_from_airport(
                country, name, patrol_type, airport, maintask=task.CAP, start_type=start_type, group_size=group_size
            )
            eg.add_runway_waypoint(airport)
        else:
            eg = self.flight_group_inflight(
                country, name, patrol_type,
                mapping.Point(pos1.x - 10 * 1000, pos1.y),
                altitude,
                maintask=task.CAP,
                group_size=group_size
            )
        return self.patrol_flight_to_group(eg, pos1, pos2, speed, altitude, max_engage_distance)

    def patrol_flight_to_group(self,
                               pg: unitgroup.PlaneGroup,
                               pos1,
                               pos2,
                               speed=600,
                               altitude=4000,
                               max_engage_distance=60*1000) -> unitgroup.PlaneGroup:
        """Add patrol waypoints to an existing flying group

        A patrol flight is a flight group that will fly a orbit between 2 given points and
        will engage any incoming air threats within max_engage_distance.

        If no airport is given, the patrol flight will spawn near the first patrol point(pos1).

        Args:
            pg(unitgroup.FlyingGroup): Group to add patrol waypoints too
            pos1(dcs.mapping.Point): first orbit waypoint
            pos2(dcs.mapping.Point): second orbit waypoint
            speed: orbit speed
            altitude: initial altitude and orbit altitude
            max_engage_distance: the distance in KM the patrol flight will respond to enemy threats

        Returns:
            PlaneGroup: the created patrol group
        """
        pg.points[0].tasks[0] = task.EngageTargets(max_engage_distance, [task.Targets.All.Air])
        wp = pg.add_waypoint(pos1, altitude, speed, self.string("P1"))
        wp.tasks.append(task.OrbitAction(altitude, speed, task.OrbitAction.OrbitPattern.RaceTrack))
        pg.add_waypoint(pos2, altitude, speed, self.string("P2"))

        return pg

    def intercept_flight(self,
                         country,
                         name: str,
                         patrol_type: Type[planes.PlaneType],
                         airport: terrain_.Airport,
                         zone: triggers.TriggerZone,
                         late_activation=True,
                         start_type: StartType=StartType.Cold,
                         speed=600,
                         altitude=4000,
                         max_engage_distance=60*1000,
                         group_size=2) -> unitgroup.PlaneGroup:
        """Add an intercept flight group to the mission.

        An intercept flight group will start from the given airport and will react on air threats if they
        enter the given zone and will be activated and try to attack air threats near the zone.

        Args:
            country(Country): the flight belongs too
            name: name of the patrol flight
            patrol_type(PlaneType): PlaneType for the patrol flight
            airport(terrain_.Airport): starting airport, use None if you want it to spawn inflight
            zone(dcs.triggers.TriggerZone): zone to react on enemies
            late_activation(bool): if flight should be started, when enemy in zone
            start_type(StartType): of the flight if starts from airport
            speed: orbit speed
            altitude: initial altitude and orbit altitude
            max_engage_distance: the distance in KM the patrol flight will respond to enemy threats
            group_size: how many planes should be in the flight group

        Returns:
            PlaneGroup: the created intercept group
        """
        eg = self.flight_group_from_airport(
            country, name, patrol_type, airport, maintask=task.CAP, start_type=start_type, group_size=group_size
        )
        eg.add_trigger_action(task.StartCommand())
        eg.uncontrolled = late_activation
        eg.add_runway_waypoint(airport)

        eg.points[0].tasks[0] = task.EngageTargets(max_engage_distance, [task.Targets.All.Air])
        wp = eg.add_waypoint(zone.position, altitude, speed)
        pos2 = zone.position.point_from_heading(random.randint(0, 360), zone.radius)
        wp.tasks.append(task.OrbitAction(altitude, speed, task.OrbitAction.OrbitPattern.RaceTrack))
        eg.add_waypoint(pos2, altitude, speed)

        eg.add_runway_waypoint(airport)
        eg.land_at(airport)

        zone_check = triggers.TriggerContinious(comment="intercept trigger")
        zone_check.add_condition(condition.PartOfCoalitionInZone("blue", zone.id))
        zone_check.add_action(action.AITaskPush(eg.id, 1))
        self.triggerrules.triggers.append(zone_check)

        return eg

    def sead_flight(self,
                    country,
                    name: str,
                    plane_type: Type[planes.PlaneType],
                    target_pos: mapping.Point,
                    airport: Optional[terrain_.Airport],
                    start_type: StartType = StartType.Cold,
                    max_engage_distance=20 * 1000,
                    group_size=2) -> unitgroup.PlaneGroup:
        """Plans a sead mission at the given target position.

        Args:
            country(Country): the flight belongs too
            name: name of the patrol flight
            plane_type(PlaneType): PlaneType for the patrol flight
            airport(terrain_.Airport): starting airport, use None if you want it to spawn inflight
            target_pos(mapping.Point): AAA position
            start_type(StartType): of the flight if starts from airport
            max_engage_distance: the distance in KM to engage
            group_size: how many planes should be in the flight group

        Returns:
            PlaneGroup: the created sead group
        """
        if airport:
            eg = self.flight_group_from_airport(
                country, name, plane_type, airport,
                maintask=task.SEAD, start_type=start_type, group_size=group_size
            )
            wp = eg.add_runway_waypoint(airport)
            wp = eg.add_waypoint(airport.position.point_from_heading(airport.position.heading_between_point(target_pos), 20*1000), 5000)
        else:
            eg = self.flight_group_inflight(
                country, name, plane_type,
                mapping.Point(target_pos.x - 10 * 1000, target_pos.y),
                5000,
                maintask=task.SEAD,
                group_size=group_size
            )

        return self.sead_flight_to_group(eg, target_pos, max_engage_distance)

    def sead_flight_to_group(self,
                             sg: unitgroup.PlaneGroup,
                             target_pos: mapping.Point,
                             max_engage_distance=20 * 1000) -> unitgroup.PlaneGroup:
        """Plans a sead mission at the given target position.

        Args:
            sg(unitgroup.FlyingGroup): PlaneType for the patrol flight
            target_pos(mapping.Point): AAA position
            max_engage_distance: the distance in KM to engage

        Returns:
            PlaneGroup: the created sead group
        """

        speed = sg.flight_type().max_speed * 0.8

        attack_hdg = sg.position.heading_between_point(target_pos) + 180
        var_hdg = random.randint(-15, 15)
        wp = sg.add_waypoint(target_pos.point_from_heading(attack_hdg + var_hdg, 30000), 5000, speed)
        wp.name = self.string("IP")
        wp = sg.add_waypoint(target_pos, 0, speed)
        wp.tasks.append(task.EngageTargets(max_engage_distance, [task.Targets.All.GroundUnits.AirDefence]))
        wp.name = self.string("SEAD")
        wp = sg.add_waypoint(target_pos.point_from_heading(attack_hdg - var_hdg, 30000), 5000, speed)
        wp.name = self.string("Fence out")

        if sg.starts_from_airport():
            airport = self.terrain.airport_by_id(sg.airport_id())
            sg.add_runway_waypoint(airport)
            sg.land_at(airport)

        return sg

    def strike_flight(self,
                      country,
                      name: str,
                      _type: Type[planes.FlyingType],
                      target: Unit,
                      airport: Optional[terrain_.Airport],
                      start_type: StartType = StartType.Cold,
                      group_size=2) -> unitgroup.FlyingGroup:
        """Plans a strike mission at the given target.

        If no airport is given, the patrol flight will spawn near the first patrol point(pos1).

        Args:
            country(Country): the flight belongs too
            name: name of the patrol flight
            _type(FlyingType): FlyingType for the strike flight
            airport(terrain_.Airport): starting airport, use None if you want it to spawn inflight
            target(Unit): Unit to strike
            start_type(StartType): of the flight if starts from airport
            group_size: how many planes should be in the flight group

        Returns:
            FlyingGroup: the created strike group
        """
        altitude = 400 if _type.helicopter else 4000

        if airport:
            eg = self.flight_group_from_airport(
                country, name, _type, airport,
                maintask=task.GroundAttack, start_type=start_type, group_size=group_size
            )
            eg.add_runway_waypoint(airport)
        else:
            eg = self.flight_group_inflight(
                country, name, _type,
                mapping.Point(target.position.x - 10 * 1000, target.position.y),
                int(altitude / 2),
                maintask=task.GroundAttack,
                group_size=group_size
            )

        return self.strike_flight_to_group(eg, target)

    def strike_flight_to_group(
            self,
            sf: unitgroup.FlyingGroup,
            target: Unit) -> unitgroup.FlyingGroup:
        """Plans a strike mission at the given target.

        If no airport is given, the patrol flight will spawn near the first patrol point(pos1).

        Args:
            sf(unitgroup.FlyingGroup): FlyingGroup to add waypoints
            target(Unit): Unit to strike

        Returns:
            FlyingGroup: the created strike group
        """
        altitude = 400 if sf.flight_type().helicopter else 4000

        speed = sf.flight_type().max_speed * 0.8

        attack_hdg = sf.position.heading_between_point(target.position) + 180
        var_hdg = random.randint(-15, 15)
        wp = sf.add_waypoint(target.position.point_from_heading(attack_hdg + var_hdg, 30000), altitude, speed)
        wp.name = self.string("IP")
        wp = sf.add_waypoint(target.position, 0, speed)
        wp.name = self.string("Attack")
        wp = sf.add_waypoint(target.position.point_from_heading(attack_hdg - var_hdg, 30000), altitude, speed)
        wp.name = self.string("Fence out")

        if sf.starts_from_airport():
            airport = self.terrain.airport_by_id(sf.airport_id())
            sf.add_runway_waypoint(airport)
            sf.land_at(airport)

        return sf

    def add_aircraft_kneeboard(self, aircraft: unittype.FlyingType, page: Path):
        """Adds an aircraft specific kneeboard page to the mission.

        Note that DCS does not support flight-specific kneeboards, so the
        kneeboard page will be visible to all aircraft of the same type
        regardless of group or coalition. For PvE, make sure pages are labeled
        for their flights. For PvP, avoid including sensitive information in
        the kneeboard.

        Args:
            aircraft: The aircraft type to display the kneeboard page for.
            page: Path to the image file for the kneeboard page.
        """
        self.aircraft_kneeboards[aircraft].append(page)

    def country(self, name):
        """Returns the country object for the mission by the given string

        Args:
            name: string representation of the country

        Returns:
            Country: the object of the country, None if not found.
        """
        for k in self.coalition:
            c = self.coalition[k].country(name)
            if c:
                return c
        return None

    def country_by_id(self, _id):
        """Returns the country object for the mission by the given id

        Args:
            _id: id of the country

        Returns:
            Country: the object of the country, None if not found.
        """
        for k in self.coalition:
            c = self.coalition[k].country_by_id(_id)
            if c:
                return c
        return None

    def find_group(self, group_name, search="exact") -> Optional[unitgroup.Group]:
        """Searches a group with the given name.

        Args:
            group_name: part or exact name of the group
            search: search mode to use

                      * 'exact': whole name must match
                      * 'match': part of the name must match

        Returns:
            Group: the group found, otherwise None
        """
        for k in self.coalition:
            g = self.coalition[k].find_group(group_name, search)
            if g:
                return g
        return None

    def is_red(self, country: Country) -> bool:
        """Checks if the given country object is part o the red coalition.

        Args:
            country(Country): object to check

        Returns:
            bool: True if it is part of the red coalition, else False.
        """
        return country.name in self.coalition["red"].countries

    def is_blue(self, country: Country) -> bool:
        """Checks if the given country object is part o the blue coalition.

        Args:
                country(Country):object to check

        Returns:
            bool: True if it is part of the blue coalition, else False.
        """
        return country.name in self.coalition["blue"].countries

    def random_date(self):
        """Sets a random date for the mission"""
        self.start_time = datetime.fromtimestamp(1306886400 + 43200, timezone.utc)  # 01-06-2011 12:00:00 UTC
        self.start_time += timedelta(days=random.randrange(0, 365))

    def random_daytime(self, period):
        self.start_time = datetime(
            year=self.start_time.year,
            month=self.start_time.month,
            day=self.start_time.day,
            tzinfo=self.start_time.tzinfo)
        daytime_map = {
            "day": timedelta(minutes=random.randrange(420, 1140)),
            "night": timedelta(minutes=random.randrange(-120, 240)),
            "dusk": timedelta(minutes=random.randrange(960, 1100)),
            "dawn": timedelta(minutes=random.randrange(240, 480)),
            "noon": timedelta(hours=random.randrange(600, 840))
        }
        if period == "random":
            period = random.choice(list(daytime_map.keys()))
        self.start_time += daytime_map[period]

    def now(self):
        """Sets mission time to current time."""
        self.start_time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)

    def stats(self) -> Dict:
        """Gather some mission stats.

        This method counts up the different group types and used units
        and returns them as easy to print dict.

        Returns:
            dict containing various group and unit counts.
        """
        d = {
            "red": {},
            "blue": {},
            "unit_count": 0,
            "count": 0
        }

        def count_group(field, group):
            d[col_name]["count"] += len(group)
            d[col_name][field]["count"] += len(group)
            for g in group:
                for u in g.units:
                    _unit = d[col_name][field]["units"].get(u.type, 0)
                    d[col_name][field]["units"][u.type] = _unit + 1
                    d[col_name]["unit_count"] += 1
            d[col_name][field]["unit_count"] = sum(d[col_name][field]["units"].values())

        for col_name in ["red", "blue"]:
            d[col_name]["unit_count"] = 0
            d[col_name]["count"] = 0
            col = self.coalition[col_name]
            d[col_name]["plane_groups"] = {"count": 0, "units": {}}
            d[col_name]["helicopter_groups"] = {"count": 0, "units": {}}
            d[col_name]["vehicle_groups"] = {"count": 0, "units": {}}
            d[col_name]["ship_groups"] = {"count": 0, "units": {}}
            for k, v in col.countries.items():
                count_group("plane_groups", v.plane_group)
                count_group("helicopter_groups", v.helicopter_group)
                count_group("vehicle_groups", v.vehicle_group)
                count_group("ship_groups", v.ship_group)
            d["unit_count"] += d[col_name]["unit_count"]
            d["count"] += d[col_name]["count"]

        # import pprint
        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(d)
        return d

    def print_stats(self, d):
        """Print the given mission stats to standard output.

        Args:
            d: stats dict to print, :py:meth:`dcs.mission.Mission.stats`
        """
        print("Mission Statistics")
        print(self.start_time.strftime("%d. %b %Y %H:%M:%S"))
        print("-"*60)
        output = {"red": [], "blue": []}
        for x in ["Blue", "Red"]:
            low = x.lower()
            output[low].append("{group:<15s} groups units".format(group=x))
            output[low].append("{group:<15s} {gc:6d} {u:5d}".format(
                group="Plane",
                gc=d[low]["plane_groups"]["count"], u=d[low]["plane_groups"]["unit_count"]))
            output[low].append("{group:<15s} {gc:6d} {u:5d}".format(
                group="Helicopter",
                gc=d[low]["helicopter_groups"]["count"], u=d[low]["helicopter_groups"]["unit_count"]))
            output[low].append("{group:<15s} {gc:6d} {u:5d}".format(
                group="Vehicle",
                gc=d[low]["vehicle_groups"]["count"], u=d[low]["vehicle_groups"]["unit_count"]))
            output[low].append("{group:<15s} {gc:6d} {u:5d}".format(
                group="Ship",
                gc=d[low]["ship_groups"]["count"], u=d[low]["ship_groups"]["unit_count"]))
            output[low].append("-"*28)
            output[low].append("{group:<15s} {gc:6d} {u:5d}".format(group="Sum", gc=d[low]["count"], u=d[low]["unit_count"]))

        # merge tables
        for i in range(0, len(output["blue"])):
            print(output["blue"][i], "  ", output["red"][i])
        print("Total {g} groups with {u} units".format(g=d["count"], u=d["unit_count"]))

    def reload(self):
        """Reloads the current loaded file

        Raises:
            RuntimeError: if there is currently no file loaded.
        """
        if self.filename:
            return self.load_file(self.filename)
        raise RuntimeError("Currently no file loaded to reload.")

    def save(self, filename=None):
        """Save the current Mission object to the given file.

        Args:
            filename: filepath to save the Mission object
        """
        filename = self.filename if filename is None else filename
        if not filename:
            raise RuntimeError("No filename given.")
        self.filename = filename  # store filename

        with zipfile.ZipFile(filename, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            # options
            zipf.writestr('options', str(self.options))

            # warehouses
            zipf.writestr('warehouses', str(self.warehouses))

            # translation files
            dicttext = lua.dumps(self.translation.dict('DEFAULT'), "dictionary", 1)
            zipf.writestr('l10n/DEFAULT/dictionary', dicttext)

            mapresource = self.map_resource.store(zipf, 'DEFAULT')
            # print(mapresource)
            zipf.writestr('l10n/DEFAULT/mapResource', lua.dumps(mapresource, "mapResource", 1))

            for unit_type, pages in self.aircraft_kneeboards.items():
                directory = f'KNEEBOARD/{unit_type.id}/IMAGES/'
                for idx, page in enumerate(pages):
                    zipf.write(page, arcname=f'{directory}/{page.name}')

            zipf.writestr('mission', str(self))

        return True

    def dict(self):
        m = {
            "trig": self.triggerrules.trig(),
            "trigrules": self.triggerrules.trigrules(),
            "start_time": int((self.start_time.hour * 60 * 60) + (self.start_time.minute * 60) + self.start_time.second)
        }
        if m["start_time"] < 0:
            raise RuntimeError("Mission start time is < 0.")
        m["date"] = {
            "Year": self.start_time.year,
            "Month": self.start_time.month,
            "Day": self.start_time.day
        }
        if self.random_weather:
            self.weather.random(self.start_time, self.terrain)
        m["groundControl"] = self.groundControl.dict()
        if self.usedModules is not None:
            m["usedModules"] = self.usedModules
        m["resourceCounter"] = self.resourceCounter
        m["triggers"] = self.triggers.dict()
        m["weather"] = self.weather.dict()
        m["theatre"] = self.terrain.name
        if self.needModules:
            m["needModules"] = self.needModules
        m["map"] = self.map.dict()
        m["descriptionText"] = self._description_text.id
        m["pictureFileNameR"] = {}
        for i in range(0, len(self.pictureFileNameR)):
            m["pictureFileNameR"][i + 1] = self.pictureFileNameR[i]
        m["pictureFileNameB"] = {}
        for i in range(0, len(self.pictureFileNameB)):
            m["pictureFileNameB"][i + 1] = self.pictureFileNameB[i]
        m["descriptionBlueTask"] = self._description_bluetask.id
        m["descriptionRedTask"] = self._description_redtask.id
        if self.init_script_file is not None:
            m["initScriptFile"] = self.init_script_file
        if self.init_script is not None:
            m["initScript"] = self.init_script
        m["coalition"] = {}
        for col in self.coalition.keys():
            m["coalition"][col] = self.coalition[col].dict()
        col_blue = {self.coalition["blue"].country(x).id for x in self.coalition["blue"].countries.keys()}
        col_red = {self.coalition["red"].country(x).id for x in self.coalition["red"].countries.keys()}
        col_neutral = list(Mission._COUNTRY_IDS - col_blue - col_red)
        col_blue = list(col_blue)
        col_red = list(col_red)
        m["coalitions"] = {
            "neutral": {x + 1: col_neutral[x] for x in range(0, len(col_neutral))},
            "blue": {x + 1: col_blue[x] for x in range(0, len(col_blue))},
            "red": {x + 1: col_red[x] for x in range(0, len(col_red))}
        }
        m["sortie"] = self._sortie.id
        m["version"] = self.version
        m["goals"] = self.goals.dict()
        m["result"] = self.goals.generate_result()
        m["currentKey"] = self.currentKey
        m["maxDictId"] = self.current_dict_id
        m["forcedOptions"] = self.forced_options.dict()
        m["failures"] = self.failures

        return m

    def __str__(self):
        return lua.dumps(self.dict(), "mission", 1)

    def __repr__(self):
        rep = {"base": str(self), "options": self.options, "translation": self.translation}
        return repr(rep)


class MapResource:
    """MapResource is responsibly to manage all additional mission resource files.

    Mission resource files are briefing images, lua scripts, sound files.

    Args:
        mission(Mission): the mission this MapResource belongs too, needed for dictionary ids
    """
    def __init__(self, mission: Mission):
        self.files = {}
        self.binary_files = []
        self.added_paths = []
        self.mission = mission

    def load_from_dict(self, _dict, zipf: zipfile.ZipFile, lang='DEFAULT'):
        _dict = _dict["mapResource"]

        for key in _dict:
            filename = _dict[key]
            filepath = 'l10n/{lang}/{fn}'.format(lang=lang, fn=filename)
            self.added_paths.append(filepath)

            try:
                extractedpath = zipf.extract(filepath, tempfile.gettempdir())
                self.add_resource_file(extractedpath, lang, key)
            except KeyError as ke:
                print(ke, file=sys.stderr)

    def load_binary_files(self, zipf: zipfile.ZipFile, reserved_files: [str]):
        for filepath in zipf.namelist():
            if filepath in reserved_files or filepath in self.added_paths:
                continue

            try:
                extractedpath = zipf.extract(filepath, tempfile.gettempdir())
                self.binary_files.append({
                    "path": os.path.abspath(extractedpath),
                    "respath": filepath,
                })
            except KeyError as ke:
                print(ke, file=sys.stderr)

    def add_resource_file(self, extracted_path: str, lang: str = 'DEFAULT', key=None) -> ResourceKey:
        """Adds a file to the mission resource depot.

        Args:
            extracted_path: path to the file to add
            lang: language this file belongs too.
            key: should be None, needed for loading

        Returns:
            resource key to use in scripts
        """
        abspath = os.path.abspath(extracted_path)
        resource_key = ResourceKey(key) if key else ResourceKey("ResKey_" + str(self.mission.next_dict_id()))
        if lang not in self.files:
            self.files[lang] = {}
        self.files[lang][resource_key.key] = abspath
        return resource_key

    def get_resource_keys(self, lang: str = 'DEFAULT') -> List[ResourceKey]:
        """
        Get a list of all used resource keys

        :param lang: language used for resource
        :return: List of resource keys
        """
        return [ResourceKey(x) for x in self.files[lang]]

    def get_file_path(self, resource_key: ResourceKey, lang: str = 'DEFAULT'):
        """
        Get the relative dcs filepath for a resource key and given language
        :param resource_key:
        :param lang:
        :return:
        """
        return self.files[lang][resource_key.key][len(tempfile.gettempdir()) + len('/l10n//') + len(lang):]

    def store(self, zipf: zipfile.ZipFile, lang='DEFAULT'):
        d = {}

        for file in self.binary_files:
            zipf.write(file["path"], file["respath"])

        if lang in self.files:
            for reskey in self.files[lang]:
                filepath = self.files[lang][reskey]
                if os.path.isabs(filepath):
                    nameinzip = os.path.basename(filepath)
                    zippath = "l10n/{lang}/{name}".format(lang=lang, name=nameinzip)
                    # do not write files twice
                    # if a script is called multiple times, a resource key is duplicated for the same file
                    has_file = [x for x in zipf.filelist if x.filename == zippath]
                    if not has_file:
                        zipf.write(filepath, zippath)
                    d[reskey] = nameinzip

        return d


class OptionsDifficulty:
    def __init__(self):
        self.geffect = "realistic"
        self.padlock = False
        self.compassTape = True
        self.aircraftMode = True
        self.easyCommunication = False
        self.easyRadar = False
        self.map = True
        self.miniHUD = False
        self.controlsIndicator = True
        self.birds = 150
        self.optionsView = "optview_all"
        self.permitCrash = False
        self.immortal = False
        self.cockpitStatusBarAllowed = False
        self.cockpitVisualRM = False
        self.easyFlight = False
        self.reports = True
        self.hideStick = False
        self.radio = False
        self.userMarks = True
        self.units = "metric"
        self.avionicsLanguage = "english"
        self.spectatorExternalViews = True
        self.tips = True
        self.userSnapView = True
        self.RBDAI = True
        self.externalViews = True
        self.iconsTheme = "nato"
        self.fuel = False
        self.weapons = False
        self.setGlobal = True
        self.labels = False

    def load_from_dict(self, d):
        self.geffect = d.get("geffect", "realistic")
        self.padlock = d.get("padlock", False)
        self.compassTape = d.get("compassTape", True)
        self.aircraftMode = d.get("aircraftMode", True)
        self.easyCommunication = d.get("easyCommunication", False)
        self.easyRadar = d.get("easyRadar", False)
        self.map = d.get("map", True)
        self.miniHUD = d.get("miniHUD", False)
        self.controlsIndicator = d.get("controlsIndicator", True)
        self.birds = d.get("birds", 150)
        self.optionsView = d.get("optionsView", "optview_all")
        self.permitCrash = d.get("permitCrash", False)
        self.immortal = d.get("immortal", False)
        self.cockpitStatusBarAllowed = d.get("cockpitStatusBarAllowed", False)
        self.cockpitVisualRM = d.get("cockpitVisualRM", False)
        self.easyFlight = d.get("easyFlight", False)
        self.reports = d.get("reports", True)
        self.hideStick = d.get("hideStick", False)
        self.radio = d.get("radio", False)
        self.userMarks = d.get("userMarks", True)
        self.units = d.get("units", "metric")
        self.avionicsLanguage = d.get("avionicsLanguage", "english")
        self.spectatorExternalViews = d.get("spectatorExternalViews", True)
        self.tips = d.get("tips", True)
        self.userSnapView = d.get("userSnapView", True)
        self.RBDAI = d.get("RBDAI", True)
        self.externalViews = d.get("externalViews", True)
        self.iconsTheme = d.get("iconsTheme", "nato")
        self.fuel = d.get("fuel", False)
        self.weapons = d.get("weapons", False)
        self.setGlobal = d.get("setGlobal", True)
        self.labels = d.get("labels", False)

    def dict(self):
        return {
            "geffect": self.geffect,
            "padlock": self.padlock,
            "compassTape": self.compassTape,
            "aircraftMode": self.aircraftMode,
            "easyCommunication": self.easyCommunication,
            "easyRadar": self.easyRadar,
            "map": self.map,
            "miniHUD": self.miniHUD,
            "controlsIndicator": self.controlsIndicator,
            "birds": self.birds,
            "optionsView": self.optionsView,
            "permitCrash": self.permitCrash,
            "immortal": self.immortal,
            "cockpitStatusBarAllowed": self.cockpitStatusBarAllowed,
            "cockpitVisualRM": self.cockpitVisualRM,
            "easyFlight": self.easyFlight,
            "reports": self.reports,
            "hideStick": self.hideStick,
            "radio": self.radio,
            "userMarks": self.userMarks,
            "units": self.units,
            "avionicsLanguage": self.avionicsLanguage,
            "spectatorExternalViews": self.spectatorExternalViews,
            "tips": self.tips,
            "userSnapView": self.userSnapView,
            "RBDAI": self.RBDAI,
            "externalViews": self.externalViews,
            "iconsTheme": self.iconsTheme,
            "fuel": self.fuel,
            "weapons": self.weapons,
            "setGlobal": self.setGlobal,
            "labels": self.labels
        }


class Options:
    """Should be a representation for the mission options file
    might be removed in the future.
    """
    def __init__(self):
        self.playerName = "PyDCS"
        self.difficulty = OptionsDifficulty()
        self.options = {}

    def load_from_dict(self, d):
        self.difficulty.load_from_dict(d["difficulty"])
        self.options = d

    def __str__(self):
        d = {
            "playerName": self.playerName,
            "difficulty": self.difficulty.dict()
        }
        for k in self.options:
            if k not in d:
                d[k] = self.options[k]
        return lua.dumps(d, "options", 1)

    def __repr__(self):
        return repr(self.options)
