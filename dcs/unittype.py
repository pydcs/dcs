import dcs.lua as lua
import dcs.installation as installation
import os
import re
import sys
from typing import Optional, Type, Any


class UnitType:
    id = None
    name = None


class VehicleType(UnitType):
    eplrs = False


class ShipType(UnitType):
    helicopter_num = 0
    plane_num = 0
    parking = 0


class StaticType(UnitType):
    shape_name = None
    rate = 0
    category = "Fortifications"
    sea_object = False
    can_cargo = False
    mass = None


class LiveryOverwrites:
    map = {
        "M-2000C.France": "AdA Chasse 2-5"
    }


class FlyingType(UnitType):
    flyable = False
    group_size_max = 4
    large_parking_slot = False
    helicopter = False
    fuel_max = 0
    max_speed = 500
    height = 0
    width = 0
    length = 0
    ammo_type = None
    chaff = 0
    flare = 0
    charge_total = 0
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Air"

    tacan = False
    eplrs = False

    radio_frequency = 251
    panel_radio = None

    property_defaults = None

    pylons = {}
    Liveries: Optional[Type[Any]] = None
    payloads = None
    dcs_dir = installation.get_dcs_install_directory()
    payload_dirs = []
    dcs_aircraft_dir = os.path.join(dcs_dir, "CoreMods", "aircraft")
    if os.path.exists(dcs_aircraft_dir):
        payload_dirs = [dcs_dir + os.path.join("MissionEditor", "data", "scripts", "UnitPayloads")]
        for entry in os.scandir(dcs_aircraft_dir):
            add_dir = os.path.join(dcs_aircraft_dir, entry.name, "UnitPayloads")
            if entry.is_dir() and os.path.exists(add_dir):
                payload_dirs.append(add_dir)
    payload_dirs += [
        os.path.join(installation.get_dcs_saved_games_directory(), "MissionEditor", "UnitPayloads"),
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "payloads")
    ]

    tasks = ['Nothing']
    task_default = None

    _payload_cache = None
    _UnitPayloadGlobals = None

    @classmethod
    def scan_payload_dir(cls):
        if FlyingType._payload_cache:
            return
        FlyingType._payload_cache = {}
        for payload_dir in FlyingType.payload_dirs:
            if not os.path.exists(payload_dir):
                continue
            files = [file for file in os.listdir(payload_dir) if file.endswith('.lua')]
            for file in files:
                payload_filename = os.path.join(payload_dir, file)
                if payload_filename not in FlyingType._payload_cache:
                    with open(payload_filename, 'r', encoding='utf-8') as payloadfile:
                        for line in payloadfile:
                            g = re.search(r'\["unitType"]\s*=\s*"([^"]*)', line)
                            if g:
                                FlyingType._payload_cache[payload_filename] = g.group(1)
                                break

    @classmethod
    def load_payloads(cls):
        # avoid cyclic dependency
        if FlyingType._UnitPayloadGlobals is None:
            from . import task
            FlyingType._UnitPayloadGlobals = {v.internal_name: v.id for k, v in task.MainTask.map.items()}

        FlyingType.scan_payload_dir()
        if cls.payloads:
            return cls.payloads

        for payload_dir in FlyingType.payload_dirs:
            if not os.path.exists(payload_dir):
                continue
            files = [file for file in os.listdir(payload_dir) if file.endswith('.lua')]
            for file in files:
                payload_filename = os.path.join(payload_dir, file)
                if FlyingType._payload_cache[payload_filename] == cls.id and os.path.exists(payload_filename):
                    with open(payload_filename, 'r', encoding='utf-8') as payload:
                        try:
                            payload_main = lua.loads(payload.read(), _globals=FlyingType._UnitPayloadGlobals)
                            pays = payload_main["unitPayloads"]
                            if pays["unitType"] == cls.id:
                                if cls.payloads:
                                    highestkey = max(pays["payloads"].keys()) + 1
                                    for load in pays["payloads"]:
                                        x = [x for x in cls.payloads["payloads"]
                                             if cls.payloads["payloads"][x]["name"] == pays["payloads"][load]["name"]]
                                        if x:
                                            cls.payloads["payloads"][x[0]] = pays["payloads"][load]
                                        else:
                                            cls.payloads["payloads"][highestkey] = pays["payloads"][load]
                                            highestkey += 1
                                else:
                                    cls.payloads = pays
                        except SyntaxError as se:
                            print("Error parsing lua file '{f}'".format(f=payload_filename), file=sys.stderr)
                            raise se

        return cls.payloads

    @classmethod
    def loadout(cls, _task):
        if cls.payloads:
            for p in cls.payloads["payloads"]:
                payload = cls.payloads["payloads"][p]
                tasks = [payload["tasks"][x] for x in payload["tasks"]]
                if _task.id in tasks:
                    pylons = payload["pylons"]
                    r = [(pylons[x]["num"], {"clsid": pylons[x]["CLSID"]}) for x in pylons]
                    return r
        return None

    @classmethod
    def loadout_by_name(cls, loadout_name):
        if cls.payloads:
            for p in cls.payloads["payloads"]:
                payload = cls.payloads["payloads"][p]
                if payload["name"] == loadout_name:
                    pylons = payload["pylons"]
                    r = [(pylons[x]["num"], {"clsid": pylons[x]["CLSID"]}) for x in pylons]
                    return r
        return None

    @classmethod
    def default_livery(cls, country_name) -> str:
        if cls.id + "." + country_name in LiveryOverwrites.map:
            return LiveryOverwrites.map[cls.id + "." + country_name]
        else:
            liveries = cls.Liveries
            if liveries is not None:
                for x in liveries.__dict__:
                    clas = liveries.__dict__[x]
                    if clas and getattr(clas, "__name__", "") == country_name:
                        return list(clas)[0].value
        return ""
