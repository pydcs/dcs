from __future__ import annotations

import copy

from dcs.unit import Unit, Skill
from dcs.unittype import AircraftRadioPresets, FlyingType
from dcs.terrain import ParkingSlot
from dcs.planes import PlaneType, A_10C
from dcs.helicopters import HelicopterType, Ka_50

import json
from typing import TYPE_CHECKING, Dict, Optional, Type

if TYPE_CHECKING:
    from dcs.terrain import Terrain


class FlyingUnit(Unit):
    def __init__(
        self,
        _id,
        name: Optional[str],
        _type: Type[FlyingType],
        terrain: Terrain,
        _country=None
    ) -> None:
        super().__init__(_id, terrain, name, _type.id)
        self.unit_type = _type  # for loadout validation
        self.unit_type.load_payloads()
        self.livery_id = self.unit_type.default_livery(_country.shortname)
        self.parking = None  # crossroad idx
        self.parking_id = None  # parking slot name (01, 02, ..)
        self.psi = 0
        self.onboard_num = '9'
        self.alt = 0
        self.alt_type = "BARO"
        self.flare = _type.flare
        self.chaff = _type.chaff
        self.fuel = _type.fuel_max
        self.gun = 100
        self.ammo_type = _type.ammo_type
        self.pylons: Dict[int, Dict[str, str]] = {}
        self.callsign = None
        self.callsign_dict = {1: 1, 2: 1, 3: 1, "name": ""}
        self.speed = 0
        self.radio: Optional[AircraftRadioPresets] = None
        self.hardpoint_racks = True
        self.addpropaircraft = dict(_type.property_defaults) if _type.property_defaults else None

    def load_from_dict(self, d):
        super(FlyingUnit, self).load_from_dict(d)
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

    def set_default_preset_channel(self, freq: float) -> None:
        """Sets the frequency for channel 1 of the main radio."""
        self.set_radio_channel_preset(1, 1, freq)

    def set_radio_preset(self):
        """Resets the radio channel configuration to the airframe's default."""
        if self.unit_type.panel_radio:
            self.radio = copy.deepcopy(self.unit_type.panel_radio)

    def num_radio_channels(self, radio_id: int) -> int:
        """Returns the number of channels available for the given radio."""
        if self.radio is None:
            return 0
        return len(self.radio[radio_id]["channels"])

    def set_radio_channel_preset(self, radio_id: int, channel: int,
                                 frequency: float) -> None:
        """Sets a preset radio channel to the given frequency.

        Note that DCS will clobber the first compatible channel for the flight's
        frequency. For example, if a flight of F-16s is assigned 118 MHz, COM2
        channel 1 will be set to 118 MHz regardless of what this function sets
        it to.

        Args:
             radio_id: The index of the radio to set the channel for.
             channel: The channel number to set.
             frequency: The frequency to set the channel to, in megahertz.

        Raises:
            TypeError: Unit type has no configurable radios, or it's unsupported.
            KeyError: No such radio or channel number.
        """
        if self.radio is None:
            raise TypeError(f"{self.type} doesn't have configurable radio channels")

        radio = self.radio[radio_id]
        if channel not in radio["channels"]:
            raise KeyError
        radio["channels"][channel] = frequency

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

    @property
    def callsign_is_western(self) -> bool:
        """Returns true if this units callsign is in the Western format.

        Western callsigns have a group name and number as well as a unit number,
        whereas other callsigns are just an arbitrary integer with no group
        association.
        """
        return self.callsign is None

    def callsign_as_str(self) -> str:
        """Returns the raw callsign for the given unit.

        Note that callsigns come in one of two forms depending on the unit's
        country, as defined by <DCS>/Scripts/Database/db_callnames.lua.

        For "Western" nations, the callsign will be in the format
        `<name><group ID><unit ID>`, where the name and group ID are common to
        the whole unit group but the unit ID is unique among the group. E.g.
        "Enfield11", "Enfield12", and so on. The group ID can be between one and
        three digits, but the unit ID will always be one digit, so "Enfield1234"
        is the callsign of Enfield 123-4.

        For other nations, the callsign is just an integer and there is no group
        association.
        """
        if not self.callsign_is_western:
            return str(self.callsign)
        name = self.callsign_dict["name"]
        if not isinstance(name, str):
            raise TypeError("Expected the 'name' entry of callsign_dict to be a str")
        return name

    def dict(self):
        d = super(FlyingUnit, self).dict()
        d["alt"] = self.alt
        d["alt_type"] = self.alt_type
        if self.parking is not None:
            d["parking"] = self.parking
        if self.parking_id is not None:
            d["parking_id"] = self.parking_id
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
    def __init__(self, terrain: Terrain, _id=None, name=None, _type: Type[PlaneType] = A_10C, _country=None):
        super().__init__(_id, name, _type, terrain, _country)


class Helicopter(FlyingUnit):
    def __init__(self, terrain: Terrain, _id=None, name=None, _type: Type[HelicopterType] = Ka_50, _country=None):
        super().__init__(_id, name, _type, terrain, _country)
        self.rope_length = 15

    def load_from_dict(self, d):
        super(Helicopter, self).load_from_dict(d)
        if "ropeLength" in d:
            self.rope_length = d["ropeLength"]

    def dict(self):
        d = super(Helicopter, self).dict()
        if self.rope_length:
            d["ropeLength"] = self.rope_length
        return d
