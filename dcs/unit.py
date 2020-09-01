from dcs.translation import String
from dcs.unittype import UnitType, StaticType, ShipType, VehicleType
import dcs.mapping as mapping
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
        self.frequency = 127500000

    def set_frequency(self, frequency: int) -> None:
        """Sets the communications frequency for this unit.

        Args:
            frequency: The frequency of the communications channel in hertz.
        """
        self.frequency = frequency

    def load_from_dict(self, d):
        super(Ship, self).load_from_dict(d)
        self.frequency = d.get("frequency", self.frequency)
        self.transportable = d["transportable"]

    def dict(self):
        d = super(Ship, self).dict()
        d["frequency"] = self.frequency
        d["transportable"] = self.transportable
        return d


class Static(Unit):
    def __init__(self, unit_id=None, name=None, _type: Union[str, Type[UnitType]] = None):
        from .planes import PlaneType
        from .helicopters import HelicopterType

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
        self.heliport_frequency: float = frequency
        self.heliport_modulation = modulation
        self.heliport_callsign_id: int = callsign_id
        self.can_cargo = False

    def load_from_dict(self, d):
        super(FARP, self).load_from_dict(d)
        self.heliport_frequency = float(d.get("heliport_frequency", 127.5))
        self.heliport_modulation = d.get("heliport_modulation")
        self.heliport_callsign_id = d.get("heliport_callsign_id", 0)

    def dict(self):
        d = super(FARP, self).dict()
        d["heliport_frequency"] = self.heliport_frequency
        d["heliport_modulation"] = self.heliport_modulation
        d["heliport_callsign_id"] = self.heliport_callsign_id

        return d


class SingleHeliPad(Static):
    def __init__(self, unit_id=None, name=None, frequency=127.5, modulation=0, callsign_id=1):
        super(SingleHeliPad, self).__init__(unit_id, name, "SINGLE_HELIPAD")
        self.category = "Heliports"
        self.shape_name = "FARP"
        self.heliport_frequency: float = frequency
        self.heliport_modulation = modulation
        self.heliport_callsign_id: int = callsign_id
        self.can_cargo = False

    def load_from_dict(self, d):
        super(SingleHeliPad, self).load_from_dict(d)
        self.heliport_frequency = float(d.get("heliport_frequency", 127.5))
        self.heliport_modulation = d.get("heliport_modulation")
        self.heliport_callsign_id = d.get("heliport_callsign_id", 0)

    def dict(self):
        d = super(SingleHeliPad, self).dict()
        d["heliport_frequency"] = self.heliport_frequency
        d["heliport_modulation"] = self.heliport_modulation
        d["heliport_callsign_id"] = self.heliport_callsign_id

        return d
