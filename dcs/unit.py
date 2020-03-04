from .terrain import ParkingSlot
from .translation import String
from .unittype import UnitType, FlyingType, StaticType, ShipType, VehicleType
from .planes import PlaneType, A_10C
from .helicopters import HelicopterType, Ka_50
from . import mapping
import json
import copy
import math
from enum import Enum
from typing import Type, Union


class Skill(Enum):
    Average = "Average"
    Good = "Good"
    High = "High"
    Excellent = "Excellent"
    Random = "Random"
    Player = "Player"
    Client = "Client"

    @staticmethod
    def from_percentage(p):
        if 0 <= p < 0.25:
            return Skill.Average
        elif 0.25 <= p < 0.5:
            return Skill.Good
        elif 0.5 <= p < 0.75:
            return Skill.High
        elif 0.75 <= p:
            return Skill.Excellent
        return Skill.Random


class Unit:
    def __init__(self, _id, name=None, type=""):
        self.type = type
        self.position = mapping.Point(0, 0)
        self.heading = 0
        self.id = _id
        self.skill = Skill.Average  # type: Skill
        self.name = name if name else String()

    def load_from_dict(self, d):
        self.position = mapping.Point(d["x"], d["y"])
        self.heading = math.degrees(d["heading"])
        self.skill = Skill(d.get("skill")) if d.get("skill") else None

    def clone(self, _id):
        new = copy.copy(self)
        new.id = _id
        return new

    def dict(self):
        d = {
            "type": self.type,
            "x": self.position.x,
            "y": self.position.y,
            "heading": round(math.radians(self.heading), 13),
            "unitId": self.id,
            "name": self.name.id
        }
        if self.skill is not None:
            d["skill"] = self.skill.value
        return d

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.dict()) + ')'


class FlyingUnit(Unit):
    def __init__(self, _id=None, name=None, _type: Type[FlyingType] = None, _country=None):
        super(FlyingUnit, self).__init__(_id, name, _type.id)
        self.unit_type = _type  # for loadout validation
        self.unit_type.load_payloads()
        self.livery_id = self.unit_type.default_livery(_country.name)
        self.parking = None  # crossroad idx
        self.parking_id = None  # parking slot name (01, 02, ..)
        self.psi = 0
        self.onboard_num = "010"
        self.alt = 0
        self.alt_type = "BARO"
        self.flare = _type.flare
        self.chaff = _type.chaff
        self.fuel = _type.fuel_max
        self.gun = 100
        self.ammo_type = _type.ammo_type
        self.pylons = {}
        self.callsign = None
        self.callsign_dict = {1: 1, 2: 1, 3: 1, "name": ""}
        self.speed = 0
        self.radio = None
        self.hardpoint_racks = True
        self.addpropaircraft = _type.property_defaults if _type.property_defaults else None

    def load_from_dict(self, d):
        super(FlyingUnit, self).load_from_dict(d)
        self.livery_id = d.get("livery_id")
        self.alt_type = d["alt_type"]
        self.alt = d["alt"]
        self.psi = d["psi"]
        self.speed = d["speed"]
        self.fuel = d["payload"]["fuel"]
        self.gun = d["payload"]["gun"]
        self.flare = d["payload"]["flare"]
        self.chaff = d["payload"]["chaff"]
        self.ammo_type = d["payload"].get("ammo_type")
        self.pylons = d["payload"]["pylons"]
        self.onboard_num = d["onboard_num"]
        if isinstance(d["callsign"], int):
            self.callsign = d["callsign"]
        else:
            self.callsign_dict = d["callsign"]
        self.parking = d.get("parking", None)
        self.parking_id = d.get("parking_id", None)
        if self.parking:
            self.parking = int(self.parking)
        self.radio = d.get("Radio")
        self.hardpoint_racks = d.get("hardpoint_racks", None)
        self.addpropaircraft = d.get("AddPropAircraft")
        return True

    def set_parking(self, parking_slot: ParkingSlot):
        parking_slot.unit_id = self.id
        self.parking = parking_slot.crossroad_idx
        self.parking_id = parking_slot.slot_name

    def set_property(self, prop_name, value):
        if self.addpropaircraft is None:
            self.addpropaircraft = {}
        self.addpropaircraft[prop_name] = value

    def load_pylon(self, weapon, pylon=None):
        if pylon is None:
            pylon = weapon[0]
        if pylon not in self.unit_type.pylons:
            raise RuntimeError("Plane {pn} has no pylon {p}.".format(pn=self.unit_type.id, p=pylon))
        if weapon is None:
            return self.pylons.pop(pylon, None)
        self.pylons[pylon] = {"CLSID": weapon[1]["clsid"]}
        return True

    def store_loadout(self, filename):
        with open(filename, 'w') as loadout:
            json.dump(self.pylons, loadout)

        return True

    def load_loadout(self, filename):
        with open(filename, 'r') as loadout:
            self.pylons = json.load(loadout)

        return True

    def reset_loadout(self):
        self.pylons = {}

    def set_default_preset_channel(self, freq):
        if self.radio:
            self.radio[1]["channels"][1] = freq

    def set_radio_preset(self):
        if self.unit_type.panel_radio:
            self.radio = self.unit_type.panel_radio

    def set_player(self):
        if not self.unit_type.flyable:
            raise RuntimeError("Unittype '{t}' is not human flyable".format(t=self.unit_type.id))
        self.skill = Skill.Player
        self.set_radio_preset()

    def set_client(self):
        if not self.unit_type.flyable:
            raise RuntimeError("Unittype '{t}' is not human flyable".format(t=self.unit_type.id))
        self.skill = Skill.Client
        self.set_radio_preset()

    def is_human(self):
        return self.skill in [Skill.Player, Skill.Client]

    def dict(self):
        d = super(FlyingUnit, self).dict()
        d["alt"] = self.alt
        d["alt_type"] = self.alt_type
        if self.parking is not None:
            d["parking"] = self.parking
        if self.parking_id is not None:
            d["parking_id"] = self.parking_id
        if self.livery_id:
            d["livery_id"] = self.livery_id
        d["psi"] = self.psi
        d["onboard_num"] = self.onboard_num
        d["speed"] = round(self.speed, 13)
        if self.hardpoint_racks is not None:
            d["hardpoint_racks"] = self.hardpoint_racks
        if self.addpropaircraft is not None:
            d["AddPropAircraft"] = self.addpropaircraft
        d["payload"] = {
            "flare": self.flare,
            "chaff": self.chaff,
            "fuel": self.fuel,
            "gun": self.gun,
            "pylons": self.pylons
        }
        if self.ammo_type:
            d["payload"]["ammo_type"] = self.ammo_type
        if self.callsign:
            d["callsign"] = self.callsign
        else:
            d["callsign"] = self.callsign_dict
        if self.radio:
            d["Radio"] = self.radio
        return d


class Plane(FlyingUnit):
    def __init__(self, _id=None, name=None, _type: Type[PlaneType] = A_10C, _country=None):
        super(Plane, self).__init__(_id, name, _type, _country)


class Helicopter(FlyingUnit):
    def __init__(self, _id=None, name=None, _type: Type[HelicopterType] = Ka_50, _country=None):
        super(Helicopter, self).__init__(_id, name, _type, _country)
        self.rope_length = 15

    def load_from_dict(self, d):
        super(Helicopter, self).load_from_dict(d)
        self.rope_length = d["ropeLength"]

    def dict(self):
        d = super(Helicopter, self).dict()
        d["ropeLength"] = self.rope_length
        return d


class Vehicle(Unit):
    def __init__(self, id=None, name=None, _type="Sandbox"):
        super(Vehicle, self).__init__(id, name, _type)
        self.player_can_drive = False
        self.transportable = {"randomTransportable": False}

    def load_from_dict(self, d):
        super(Vehicle, self).load_from_dict(d)
        self.player_can_drive = d["playerCanDrive"]
        self.transportable = d["transportable"]

    def dict(self):
        d = super(Vehicle, self).dict()
        d["playerCanDrive"] = self.player_can_drive
        d["transportable"] = self.transportable
        return d


class Ship(Unit):
    def __init__(self, id=None, name=None, _type=None):
        super(Ship, self).__init__(id, name, _type.id)
        self.transportable = {"randomTransportable": False}

    def load_from_dict(self, d):
        super(Ship, self).load_from_dict(d)
        self.transportable = d["transportable"]

    def dict(self):
        d = super(Ship, self).dict()
        d["transportable"] = self.transportable
        return d


class Static(Unit):
    def __init__(self, unit_id=None, name=None, _type: Union[str,Type[UnitType]] = None):
        if not isinstance(_type, str):
            _id = _type.id
            _class = _type
        else:
            _id = _type
            _class = str
        super(Static, self).__init__(unit_id, name, _id)
        self.skill = None
        self.shape_name = None
        self.rate = None
        self.mass = None

        if issubclass(_class, StaticType):
            self.category = _type.category
            self.can_cargo = _type.can_cargo
            self.shape_name = _type.shape_name
            self.rate = _type.rate
            self.mass = 1000 if _type.can_cargo else None
        elif issubclass(_class, PlaneType):
            self.category = "Planes"
            self.can_cargo = False
        elif issubclass(_class, HelicopterType):
            self.category = "Helicopters"
            self.can_cargo = False
        elif issubclass(_class, ShipType):
            self.category = "Ships"
            self.can_cargo = False
        elif issubclass(_class, VehicleType):
            self.category = "Vehicles"
            self.can_cargo = False

    def load_from_dict(self, d):
        super(Static, self).load_from_dict(d)
        self.can_cargo = d.get("canCargo", False)
        self.category = d["category"]
        self.shape_name = d.get("shape_name", None)
        self.rate = d.get("rate")
        self.mass = d.get("mass")

    def dict(self):
        d = super(Static, self).dict()
        d["category"] = self.category
        d["canCargo"] = self.can_cargo
        if self.shape_name is not None:
            d["shape_name"] = self.shape_name
        if self.rate is not None:
            d["rate"] = self.rate
        if self.mass is not None:
            d["mass"] = self.mass
        return d


class FARP(Static):
    def __init__(self, unit_id=None, name=None, frequency=127.5, modulation=0, callsign_id=1):
        super(FARP, self).__init__(unit_id, name, "FARP")
        self.category = "Heliports"
        self.shape_name = "FARPS"
        self.heliport_frequency = frequency
        self.heliport_modulation = modulation
        self.heliport_callsign_id = callsign_id
        self.can_cargo = False

    def load_from_dict(self, d):
        super(FARP, self).load_from_dict(d)
        self.heliport_frequency = d.get("heliport_frequency")
        self.heliport_modulation = d.get("heliport_modulation")
        self.heliport_callsign_id = d.get("heliport_callsign_id", 0)

    def dict(self):
        d = super(FARP, self).dict()
        d["heliport_frequency"] = self.heliport_frequency
        d["heliport_modulation"] = self.heliport_modulation
        d["heliport_callsign_id"] = self.heliport_callsign_id

        return d
