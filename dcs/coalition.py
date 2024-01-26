import sys
from typing import Dict, Union, List, TYPE_CHECKING, Optional
import dcs.countries as countries
from dcs.mapping import Point
import dcs.unitgroup as unitgroup
import dcs.planes as planes
import dcs.helicopters as helicopters
import dcs.ships as ships
from dcs.unit import Vehicle, Static, Ship, FARP, SingleHeliPad
from dcs.flyingunit import Plane, Helicopter
from dcs.point import MovingPoint, StaticPoint
from dcs.country import Country
from dcs.status_message import StatusMessage, MessageType, MessageSeverity
from dcs.unitgroup import Group

if TYPE_CHECKING:
    from . import Mission


class Coalition:
    def __init__(self, name, bullseye=None):
        self.name = name
        self.countries: Dict[str, Country] = {}
        self.bullseye = bullseye
        self.nav_points = []  # TODO

    @staticmethod
    def _sort_keys(points):
        keys = []
        for imp_point_idx in points:
            keys.append(int(imp_point_idx))

        keys.sort()
        return keys

    @staticmethod
    def _import_moving_point(mission, group: unitgroup.Group, imp_group) -> unitgroup.Group:
        keys = Coalition._sort_keys(imp_group["route"]["points"])

        for imp_point_idx in keys:
            imp_point = imp_group["route"]["points"][imp_point_idx]
            point = MovingPoint(Point(0, 0, mission.terrain))
            point.load_from_dict(imp_point, mission.translation)
            group.add_point(point)
        return group

    @staticmethod
    def _import_static_point(mission, group: unitgroup.Group, imp_group) -> unitgroup.Group:
        keys = Coalition._sort_keys(imp_group["route"]["points"])

        for imp_point_idx in keys:
            imp_point = imp_group["route"]["points"][imp_point_idx]
            point = StaticPoint(Point(0, 0, mission.terrain))
            point.load_from_dict(imp_point, mission.translation)
            group.add_point(point)
        return group

    @staticmethod
    def _park_unit_on_airport(
            mission: 'Mission',
            group: unitgroup.Group,
            unit: Union[Plane, Helicopter]) -> List[StatusMessage]:
        ret: List[StatusMessage] = []
        if group.points[0].airdrome_id is not None and unit.parking is not None:
            airport = mission.terrain.airport_by_id(group.points[0].airdrome_id)
            slot = airport.parking_slot(unit.parking)
            if slot is not None:
                unit.set_parking(slot)
            else:
                msg = "Parking slot id '{i}' for unit '{u}' in group '{p}' on airport '{a}' " \
                      "not valid, placing on next free".format(i=unit.parking, u=unit.name,
                                                               a=airport.name, p=group.name)
                print("WARN", msg, file=sys.stderr)
                ret.append(StatusMessage(msg, MessageType.PARKING_SLOT_NOT_VALID, MessageSeverity.WARN))
                slot = airport.free_parking_slot(unit.unit_type)
                if slot is not None:
                    unit.set_parking(slot)
                else:
                    msg = "No free parking slots for unit '{u}' in unit group '{p}' on airport '{a}', ignoring"\
                        .format(u=unit.name, a=airport.name, p=group.name)
                    print("ERRO", msg, file=sys.stderr)
                    ret.append(StatusMessage(msg, MessageType.PARKING_SLOTS_FULL, MessageSeverity.ERROR))
        return ret

    @staticmethod
    def get_name(mission: "Mission", name: str) -> str:
        # Group, unit names are not localized for missions are created in 2.7.
        if mission.version < 19:
            return str(mission.translation.get_string(name))
        else:
            return name

    def load_from_dict(self, mission, d, countries_in_coalition: Dict[int, int]) -> List[StatusMessage]:
        status: List[StatusMessage] = []
        for country_idx in d["country"]:
            imp_country = d["country"][country_idx]
            _country = countries.get_by_id(imp_country["id"])

            if "vehicle" in imp_country:
                for vgroup_idx in imp_country["vehicle"]["group"]:
                    vgroup = imp_country["vehicle"]["group"][vgroup_idx]
                    vg = unitgroup.VehicleGroup(vgroup["groupId"], self.get_name(mission, vgroup["name"]),
                                                vgroup["start_time"])
                    vg.load_from_dict(vgroup, mission.terrain)
                    mission.current_group_id = max(mission.current_group_id, vg.id)

                    Coalition._import_moving_point(mission, vg, vgroup)

                    # units
                    for imp_unit_idx in vgroup["units"]:
                        imp_unit = vgroup["units"][imp_unit_idx]
                        unit = Vehicle(
                            mission.terrain,
                            id=imp_unit["unitId"],
                            name=self.get_name(mission, imp_unit["name"]),
                            _type=imp_unit["type"])
                        unit.load_from_dict(imp_unit)

                        mission.current_unit_id = max(mission.current_unit_id, unit.id)
                        vg.add_unit(unit)
                    _country.add_vehicle_group(vg)

            if "ship" in imp_country:
                for group_idx in imp_country["ship"]["group"]:
                    imp_group = imp_country["ship"]["group"][group_idx]
                    ship_group = unitgroup.ShipGroup(imp_group["groupId"], self.get_name(mission, imp_group["name"]),
                                                     imp_group["start_time"])
                    ship_group.load_from_dict(imp_group, mission.terrain)
                    mission.current_group_id = max(mission.current_group_id, ship_group.id)

                    Coalition._import_moving_point(mission, ship_group, imp_group)

                    # units
                    for imp_unit_idx in imp_group["units"]:
                        imp_unit = imp_group["units"][imp_unit_idx]
                        ship = Ship(
                            mission.terrain,
                            id=imp_unit["unitId"],
                            name=self.get_name(mission, imp_unit["name"]),
                            _type=ships.ship_map[imp_unit["type"]])
                        ship.load_from_dict(imp_unit)

                        mission.current_unit_id = max(mission.current_unit_id, ship.id)
                        ship_group.add_unit(ship)
                    _country.add_ship_group(ship_group)

            if "plane" in imp_country:
                for pgroup_idx in imp_country["plane"]["group"]:
                    pgroup = imp_country["plane"]["group"][pgroup_idx]
                    plane_group = unitgroup.PlaneGroup(pgroup["groupId"],
                                                       self.get_name(mission, pgroup["name"]),
                                                       pgroup["start_time"])
                    plane_group.load_from_dict(pgroup, mission.terrain)
                    mission.current_group_id = max(mission.current_group_id, plane_group.id)

                    Coalition._import_moving_point(mission, plane_group, pgroup)

                    # units
                    for imp_unit_idx in pgroup["units"]:
                        imp_unit = pgroup["units"][imp_unit_idx]
                        plane = Plane(
                            mission.terrain,
                            _id=imp_unit["unitId"],
                            name=self.get_name(mission, imp_unit["name"]),
                            _type=planes.plane_map[imp_unit["type"]],
                            _country=_country)
                        plane.load_from_dict(imp_unit)

                        if _country.reserve_onboard_num(plane.onboard_num):
                            msg = "{c} Plane '{p}' already using tail number: {t}".format(
                                c=self.name.upper(), p=plane.name, t=plane.onboard_num)
                            status.append(StatusMessage(msg, MessageType.ONBOARD_NUM_DUPLICATE, MessageSeverity.WARN))
                            print("WARN:", msg, file=sys.stderr)
                        status += self._park_unit_on_airport(mission, plane_group, plane)

                        mission.current_unit_id = max(mission.current_unit_id, plane.id)
                        plane_group.add_unit(plane)

                    # check runway start
                    # if plane_group.points[0].airdrome_id is not None and plane_group.units[0].parking is None:
                    #     airport = mission.terrain.airport_by_id(plane_group.points[0].airdrome_id)
                    #     airport.occupy_runway(plane_group)
                    _country.add_plane_group(plane_group)

            if "helicopter" in imp_country:
                for pgroup_idx in imp_country["helicopter"]["group"]:
                    pgroup = imp_country["helicopter"]["group"][pgroup_idx]
                    helicopter_group = unitgroup.HelicopterGroup(
                        pgroup["groupId"],
                        self.get_name(mission, pgroup["name"]),
                        pgroup["start_time"])
                    helicopter_group.load_from_dict(pgroup, mission.terrain)
                    mission.current_group_id = max(mission.current_group_id, helicopter_group.id)

                    Coalition._import_moving_point(mission, helicopter_group, pgroup)

                    # units
                    for imp_unit_idx in pgroup["units"]:
                        imp_unit = pgroup["units"][imp_unit_idx]
                        heli = Helicopter(
                            mission.terrain,
                            _id=imp_unit["unitId"],
                            name=self.get_name(mission, imp_unit["name"]),
                            _type=helicopters.helicopter_map[imp_unit["type"]],
                            _country=_country)
                        heli.load_from_dict(imp_unit)

                        if _country.reserve_onboard_num(heli.onboard_num):
                            msg = "{c} Helicopter '{h}' already using tail number: {t}".format(
                                c=self.name.upper(), h=heli.name, t=heli.onboard_num)
                            status.append(StatusMessage(msg, MessageType.ONBOARD_NUM_DUPLICATE, MessageSeverity.WARN))
                            print("WARN:", msg, file=sys.stderr)
                        status += self._park_unit_on_airport(mission, helicopter_group, heli)

                        mission.current_unit_id = max(mission.current_unit_id, heli.id)
                        helicopter_group.add_unit(heli)

                    # check runway start
                    # if helicopter_group.points[0].airdrome_id is not None and helicopter_group.units[0].parking is None:
                    #     airport = mission.terrain.airport_by_id(helicopter_group.points[0].airdrome_id)
                    #     airport.occupy_runway(helicopter_group)
                    _country.add_helicopter_group(helicopter_group)

            if "static" in imp_country:
                for sgroup_idx in imp_country["static"]["group"]:
                    sgroup = imp_country["static"]["group"][sgroup_idx]
                    static_group = unitgroup.StaticGroup(sgroup["groupId"],
                                                         self.get_name(mission, sgroup["name"]))
                    static_group.load_from_dict(sgroup, mission.terrain)
                    mission.current_group_id = max(mission.current_group_id, static_group.id)

                    Coalition._import_static_point(mission, static_group, sgroup)

                    # units
                    for imp_unit_idx in sgroup["units"]:
                        imp_unit = sgroup["units"][imp_unit_idx]
                        static: Static
                        if imp_unit["type"] == "FARP":
                            static = FARP(
                                mission.terrain,
                                unit_id=imp_unit["unitId"],
                                name=self.get_name(mission, imp_unit["name"]))
                        elif imp_unit["type"] == "SINGLE_HELIPAD":
                            static = SingleHeliPad(
                                mission.terrain,
                                unit_id=imp_unit["unitId"],
                                name=self.get_name(mission, imp_unit["name"]))
                        else:
                            static = Static(
                                unit_id=imp_unit["unitId"],
                                name=self.get_name(mission, imp_unit["name"]),
                                _type=imp_unit["type"],
                                terrain=mission.terrain)
                        static.load_from_dict(imp_unit)

                        mission.current_unit_id = max(mission.current_unit_id, static.id)
                        static_group.add_unit(static)
                    _country.add_static_group(static_group)
            self.add_country(_country)

        # iterate over all .miz countries in coalition, even without any units
        # on the map, and add them to the respective coalition
        for country_id in countries_in_coalition.values():
            if self.country_by_id(country_id) is None:
                self.add_country(countries.get_by_id(country_id))

        return status

    def set_bullseye(self, bulls):
        self.bullseye = bulls

    def add_country(self, country):
        self.countries[country.name] = country
        return country

    def remove_country(self, name):
        return self.countries.pop(name)

    def swap_country(self, coalition, name):
        return coalition.add_country(self.remove_country(name))

    def country(self, country_name: str):
        return self.countries.get(country_name, None)

    def country_by_id(self, _id: int):
        for cn in self.countries:
            c = self.countries[cn]
            if c.id == _id:
                return c
        return None

    def find_group(self, group_name, search="exact"):
        for c in self.countries:
            g = self.countries[c].find_group(group_name, search)
            if g:
                return g

        return None

    def find_group_by_id(self, group_id: int) -> Optional[Group]:
        for c in self.countries:
            g = self.countries[c].find_group_by_id(group_id)
            if g is not None:
                return g

        return None

    def dict(self):
        d = {"name": self.name}
        if self.bullseye:
            d["bullseye"] = self.bullseye
        d["country"] = {}
        i = 1
        for country in sorted(self.countries.keys()):
            d["country"][i] = self.country(country).dict()
            i += 1
        d["nav_points"] = {}
        return d
