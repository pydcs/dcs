from __future__ import annotations

import copy
from enum import Enum
import math
from typing import TYPE_CHECKING, Any, Callable, Dict, Type, Union, Optional

from dcs.unittype import UnitType, StaticType, ShipType, VehicleType
import dcs.mapping as mapping

if TYPE_CHECKING:
    from dcs.terrain.terrain import Terrain


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
    def __init__(self, _id, terrain: Terrain, name: Optional[str] = None, type="") -> None:
        if type == "":
            breakpoint()
        self.type = type
        self._terrain = terrain
        self.position = mapping.Point(0, 0, self._terrain)
        self.heading = 0.0
        self.id = _id
        self.skill: Optional[Skill] = Skill.Average
        self.name: str = name if name else ""
        self.livery_id: Optional[str] = None

    def load_from_dict(self, d: Dict[str, Any]) -> None:
        self.position = mapping.Point(d["x"], d["y"], self._terrain)
        self.heading = math.degrees(d["heading"])
        self.skill = Skill(d.get("skill")) if d.get("skill") else None
        self.livery_id = d.get("livery_id")

    def clone(self, _id):
        new = copy.copy(self)
        new.id = _id
        return new

    def dict(self):
        if not isinstance(self.name, str):
            raise TypeError("Point name expected to be `str`")
        d = {
            "type": self.type,
            "x": self.position.x,
            "y": self.position.y,
            "heading": round(math.radians(self.heading), 13),
            "unitId": self.id,
            "name": self.name
        }
        if self.livery_id:
            d["livery_id"] = self.livery_id
        if self.skill is not None:
            d["skill"] = self.skill.value
        return d

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.dict()) + ')'


class Vehicle(Unit):
    def __init__(self, terrain: Terrain, id: Optional[int] = None, name: Optional[str] = None, _type="Sandbox"):
        super().__init__(id, terrain, name, _type)
        self.player_can_drive = False

    def load_from_dict(self, d: Dict[str, Any]) -> None:
        super().load_from_dict(d)
        self.player_can_drive = d["playerCanDrive"]

    def dict(self):
        d = super(Vehicle, self).dict()
        d["playerCanDrive"] = self.player_can_drive
        return d


class Ship(Unit):
    def __init__(self, terrain: Terrain, id=None, name: Optional[str] = None, _type=None):
        super().__init__(id, terrain, name, _type.id)
        self.frequency = 127500000

    def set_frequency(self, frequency: int) -> None:
        """Sets the communications frequency for this unit.

        Args:
            frequency: The frequency of the communications channel in hertz.
        """
        self.frequency = frequency

    def load_from_dict(self, d: Dict[str, Any]) -> None:
        super().load_from_dict(d)
        self.frequency = d.get("frequency", self.frequency)

    def dict(self):
        d = super(Ship, self).dict()
        d["frequency"] = self.frequency
        return d


class Static(Unit):
    def __init__(self, unit_id: int, name: Optional[str], _type: Union[str, Type[UnitType]], terrain: Terrain) -> None:
        from .planes import PlaneType
        from .helicopters import HelicopterType

        if isinstance(_type, str):
            _id = _type
        else:
            _id = _type.id

        super().__init__(unit_id, terrain, name, _id)
        self.skill: Optional[Skill] = None
        self.shape_name: Optional[str] = None
        self.rate: Optional[int] = None
        self.mass: Optional[int] = None
        self.category: Optional[str] = None
        self.can_cargo: Optional[bool] = None
        self.effect_preset: Optional[int] = None
        self.effect_transparency: Optional[float] = None

        if not isinstance(_type, str):
            if issubclass(_type, StaticType):
                self.category = _type.category
                self.can_cargo = _type.can_cargo
                self.shape_name = _type.shape_name
                self.rate = _type.rate
                self.mass = 1000 if _type.can_cargo else None
            elif issubclass(_type, PlaneType):
                self.category = "Planes"
                self.can_cargo = False
            elif issubclass(_type, HelicopterType):
                self.category = "Helicopters"
                self.can_cargo = False
            elif issubclass(_type, ShipType):
                self.category = "Ships"
                self.can_cargo = False
            elif issubclass(_type, VehicleType):
                self.category = "Vehicles"
                self.can_cargo = False

    def load_from_dict(self, d: Dict[str, Any]) -> None:
        super().load_from_dict(d)
        self.can_cargo = d.get("canCargo", False)
        self.category = d.get("category", None)
        self.shape_name = d.get("shape_name", None)
        self.rate = d.get("rate")
        self.mass = d.get("mass")
        self.effect_preset = d.get("effectPreset", None)
        self.effect_transparency = d.get("effectTransparency", None)

    def dict(self):
        d = super(Static, self).dict()
        fields = [
            (self.category, "category"),
            (self.can_cargo, "canCargo"),
            (self.shape_name, "shape_name"),
            (self.rate, "rate"),
            (self.mass, "mass"),
            (self.effect_preset, "effectPreset"),
            (self.effect_transparency, "effectTransparency")
        ]
        for attr, keyName in fields:
            if attr is not None:
                d[keyName] = attr
        return d


class BaseFARP(Static):
    def __init__(self, unit_id, name: Optional[str], _type: Union[str, Type[UnitType]], shape_name: str, frequency: float,
                 modulation: int, callsign_id: int, terrain: Terrain) -> None:
        super().__init__(unit_id, name, _type, terrain)
        self.category = "Heliports"
        self.shape_name = shape_name
        self.heliport_frequency = frequency
        self.heliport_modulation = modulation
        self.heliport_callsign_id = callsign_id
        self.can_cargo = False


class FARP(BaseFARP):
    def __init__(
        self,
        terrain: Terrain,
        unit_id=None,
        name: Optional[str] = None,
        frequency=127.5,
        modulation=0,
        callsign_id=1
    ) -> None:
        super().__init__(unit_id, name, "FARP", "FARPS", frequency, modulation, callsign_id, terrain)

    def load_from_dict(self, d):
        super(FARP, self).load_from_dict(d)
        self.heliport_frequency = float(d.get("heliport_frequency", 127.5))
        self.heliport_modulation = d.get("heliport_modulation", 0)
        self.heliport_callsign_id = d.get("heliport_callsign_id", 0)

    def dict(self):
        d = super(FARP, self).dict()
        d["heliport_frequency"] = self.heliport_frequency
        d["heliport_modulation"] = self.heliport_modulation
        d["heliport_callsign_id"] = self.heliport_callsign_id

        return d


class SingleHeliPad(BaseFARP):
    def __init__(
        self,
        terrain: Terrain,
        unit_id=None,
        name: Optional[str] = None,
        frequency=127.5,
        modulation=0,
        callsign_id=1
    ) -> None:
        super().__init__(unit_id, name, "SINGLE_HELIPAD", "FARP", frequency, modulation, callsign_id, terrain)

    def load_from_dict(self, d):
        super(SingleHeliPad, self).load_from_dict(d)
        self.heliport_frequency = float(d.get("heliport_frequency", 127.5))
        self.heliport_modulation = d.get("heliport_modulation", 0)
        self.heliport_callsign_id = d.get("heliport_callsign_id", 0)

    def dict(self):
        d = super(SingleHeliPad, self).dict()
        d["heliport_frequency"] = self.heliport_frequency
        d["heliport_modulation"] = self.heliport_modulation
        d["heliport_callsign_id"] = self.heliport_callsign_id

        return d


class InvisibleFARP(BaseFARP):
    def __init__(self, terrain: Terrain, unit_id=None, name=None, frequency=127.5, modulation=0, callsign_id=1):
        super().__init__(unit_id, name, "Invisible FARP", "invisiblefarp", frequency, modulation, callsign_id, terrain)

    def load_from_dict(self, d):
        super(InvisibleFARP, self).load_from_dict(d)
        self.heliport_frequency = float(d.get("heliport_frequency", 127.5))
        self.heliport_modulation = d.get("heliport_modulation", 0)
        self.heliport_callsign_id = d.get("heliport_callsign_id", 0)

    def dict(self):
        d = super(InvisibleFARP, self).dict()
        d["heliport_frequency"] = self.heliport_frequency
        d["heliport_modulation"] = self.heliport_modulation
        d["heliport_callsign_id"] = self.heliport_callsign_id

        return d


farp_mapping: Dict[str, Callable[[Terrain, Optional[int], Optional[str], float, int, int], BaseFARP]] = {
    "FARP": FARP,
    "SingleHeliPad": SingleHeliPad,
    "InvisibleFARP": InvisibleFARP,
}
