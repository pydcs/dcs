from .unit import Unit, Skill
from .unittype import FlyingType
from .terrain import ParkingSlot
from .planes import PlaneType, A_10C
from .helicopters import HelicopterType, Ka_50

import json
from typing import Type


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