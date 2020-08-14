from dcs.unitgroup import VehicleGroup, ShipGroup, PlaneGroup, StaticGroup, HelicopterGroup, FlyingGroup, Group
from typing import List, Dict


def find_exact(group_name, find_name):
    return group_name == find_name


def find_match(group_name, find_name):
    return find_name in group_name


find_map = {
    "exact": find_exact,
    "match": find_match
}


class Country:
    callsign = {}
    planes = []
    helicopters = []

    def __init__(self, _id, name):
        self.id = _id
        self.name = name
        self.vehicle_group = []  # type: List[VehicleGroup]
        self.ship_group = []  # type: List[ShipGroup]
        self.plane_group = []  # type: List[PlaneGroup]
        self.helicopter_group = []  # type: List[HelicopterGroup]
        self.static_group = []  # type: List[StaticGroup]
        self.current_callsign_id = 99
        self.current_callsign_category = {}  # type: Dict[str,int]

    def add_vehicle_group(self, vgroup):
        self.vehicle_group.append(vgroup)

    def add_ship_group(self, sgroup):
        self.ship_group.append(sgroup)

    def add_plane_group(self, pgroup):
        self.plane_group.append(pgroup)

    def add_helicopter_group(self, hgroup):
        self.helicopter_group.append(hgroup)

    def add_aircraft_group(self, group: FlyingGroup):
        if group.units[0].unit_type.helicopter:
            self.helicopter_group.append(group)
        else:
            self.plane_group.append(group)

    def add_static_group(self, sgroup):
        self.static_group.append(sgroup)

    def remove_static_group(self, sgroup):
        for i in range(0, len(self.static_group)):
            if sgroup.id == self.static_group[i].id:
                del self.static_group[i]
                return True

        return False

    def find_group(self, group_name, search="exact"):
        groups = [self.vehicle_group,
                  self.ship_group,
                  self.plane_group,
                  self.helicopter_group,
                  self.static_group]
        for search_group in groups:
            for group in search_group:
                if find_map[search](group.name.str(), group_name):
                    return group
        return None

    def find_vehicle_group(self, name: str, search="exact"):
        for group in self.vehicle_group:
            if find_map[search](group.name.str(), name):
                return group
        return None

    def find_ship_group(self, name: str, search="exact"):
        for group in self.ship_group:
            if find_map[search](group.name.str(), name):
                return group
        return None

    def find_plane_group(self, name: str, search="exact"):
        for group in self.plane_group:
            if find_map[search](group.name.str(), name):
                return group

    def find_helicopter_group(self, name: str, search="exact"):
        for group in self.helicopter_group:
            if find_map[search](group.name.str(), name):
                return group

    def find_static_group(self, name: str, search="exact"):
        for group in self.static_group:
            if find_map[search](group.name.str(), name):
                return group
        return None

    def vehicle_group_within(self, point, distance) -> List[Group]:
        """Return all vehicle groups within the radius of a given point.

        Args:
            point(mapping.Point): Center of circle
            distance: Distance to the point

        Returns:
            Sequence of vehicle groups within range.
        """
        return [x for x in self.vehicle_group if x.position.distance_to_point(point) < distance]

    def static_group_within(self, point, distance) -> List[Group]:
        """Return all static groups within the radius of a given point.

        Args:
            point(mapping.Point): Center of circle
            distance: Distance to the point

        Returns:
            Sequence of static groups within range.
        """
        return [x for x in self.static_group if x.position.distance_to_point(point) < distance]

    def next_callsign_id(self):
        self.current_callsign_id += 1
        return self.current_callsign_id

    def next_callsign_category(self, category):
        if category not in self.current_callsign_category:
            self.current_callsign_category[category] = 0
            return self.callsign.get(category)[0]

        self.current_callsign_category[category] += 1
        if self.current_callsign_category[category] >= len(self.callsign[category]):
            self.current_callsign_category[category] = 0
        return self.callsign.get(category)[self.current_callsign_category[category]]

    def dict(self):
        d = {
            "name": self.name,
            "id": self.id
        }

        if self.vehicle_group:
            d["vehicle"] = {"group": {}}
            i = 1
            for vgroup in self.vehicle_group:
                d["vehicle"]["group"][i] = vgroup.dict()
                i += 1

        if self.ship_group:
            d["ship"] = {"group": {}}
            i = 1
            for group in self.ship_group:
                d["ship"]["group"][i] = group.dict()
                i += 1

        if self.plane_group:
            d["plane"] = {"group": {}}
            i = 1
            for plane_group in self.plane_group:
                d["plane"]["group"][i] = plane_group.dict()
                i += 1

        if self.helicopter_group:
            d["helicopter"] = {"group": {}}
            i = 1
            for group in self.helicopter_group:
                d["helicopter"]["group"][i] = group.dict()
                i += 1

        if self.static_group:
            d["static"] = {"group": {}}
            i = 1
            for static_group in self.static_group:
                d["static"]["group"][i] = static_group.dict()
                i += 1
        return d

    def __str__(self):
        return str(self.id) + "," + self.name + "," + str(self.vehicle_group)
