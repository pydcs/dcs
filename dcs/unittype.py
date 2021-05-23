import dcs.lua as lua
from dcs.payloads import PayloadDirectories
import re
import sys
from typing import Any, Dict, Optional, Type


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
    # Dict from payload name to the DCS payload structure. None if not yet initialized.
    payloads: Optional[Dict[str, Dict[str, Any]]] = None

    tasks = ['Nothing']
    task_default = None

    _payload_cache = None
    _UnitPayloadGlobals = None

    @classmethod
    def scan_payload_dir(cls):
        if FlyingType._payload_cache:
            return
        FlyingType._payload_cache = {}
        for payload_dir in PayloadDirectories.payload_dirs():
            if not payload_dir.exists():
                continue
            for payload_path in payload_dir.glob("*.lua"):
                if payload_path not in FlyingType._payload_cache:
                    with payload_path.open('r', encoding='utf-8') as payload_file:
                        for line in payload_file:
                            g = re.search(r'\["unitType"]\s*=\s*"([^"]*)', line)
                            if g:
                                FlyingType._payload_cache[payload_path] = g.group(1)
                                break

    @classmethod
    def load_payloads(cls):
        # avoid cyclic dependency
        if FlyingType._UnitPayloadGlobals is None:
            from . import task
            FlyingType._UnitPayloadGlobals = {v.internal_name: v.id for k, v in task.MainTask.map.items()}

        FlyingType.scan_payload_dir()
        if cls.payloads is not None:
            return cls.payloads
        cls.payloads = {}

        for payload_dir in PayloadDirectories.payload_dirs():
            if not payload_dir.exists():
                continue
            for payload_path in payload_dir.glob("*.lua"):
                if FlyingType._payload_cache[payload_path] == cls.id and payload_path.exists():
                    try:
                        payload_main = lua.loads(payload_path.read_text(), _globals=FlyingType._UnitPayloadGlobals)
                    except SyntaxError:
                        print("Error parsing lua file '{f}'".format(f=payload_path), file=sys.stderr)
                        raise
                    pays = payload_main["unitPayloads"]
                    if pays["unitType"] == cls.id:
                        for load in pays["payloads"].values():
                            name = load["name"]
                            # Payload directories are iterated in decreasing order of
                            # preference, so if we already have a payload matching the
                            # name, ignore it.
                            if name not in cls.payloads:
                                cls.payloads[load["name"]] = load

        return cls.payloads

    @classmethod
    def loadout(cls, _task):
        if cls.payloads is not None:
            for payload in cls.payloads.values():
                tasks = [payload["tasks"][x] for x in payload["tasks"]]
                if _task.id in tasks:
                    pylons = payload["pylons"]
                    r = [(pylons[x]["num"], {"clsid": pylons[x]["CLSID"]}) for x in pylons]
                    return r
        return None

    @classmethod
    def loadout_by_name(cls, loadout_name):
        if cls.payloads is not None:
            payload = cls.payloads.get(loadout_name)
            if payload is None:
                return None
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
