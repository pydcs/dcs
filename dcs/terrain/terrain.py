# terrain module
import dcs.mapping as mapping
import dcs.lua as lua
import dcs.point as point
import dcs.unittype as unittype
import dcs.weather as weather

import random
import pickle
import sys
from datetime import datetime
from typing import List, Dict, Optional, Tuple, Set, Type
from collections import defaultdict, deque


class ParkingSlot:
    def __init__(self,
                 crossroad_idx,
                 position: mapping.Point,
                 large=False,
                 slot_name=None,
                 heli=False,
                 airplanes=True,
                 length=None,
                 width=None,
                 height=None,
                 shelter=False):
        self.crossroad_idx = crossroad_idx
        self.position = position
        self.length = length
        self.width = width
        self.height = height
        self.helicopter = heli
        self.airplanes = airplanes
        self.large = large
        self.shelter = shelter
        self.unit_id = None  # type: Optional[int]
        self.slot_name = slot_name

    def __repr__(self):
        return 'ParkingSlot({id}, "{name}", large={large}, heli={heli})'.format(
            id=self.crossroad_idx, name=self.slot_name, large=self.large, heli=self.helicopter
        )


class Runway:
    def __init__(self, heading, ils=None, leftright=0):
        """

        :param heading: Compass direction of runway
        :param ils:
        :param leftright: 0 only 1 runway
                          1 left runway
                          2 right runway
        :return: None
        """
        self.heading = heading
        self.ils = ils
        self.leftright = leftright


class RunwayOccupiedError(RuntimeError):
    pass


class NoParkingSlotError(RuntimeError):
    pass


class Airport:
    id = None
    name = None
    position = None  # type: mapping.Point
    tacan = None
    frequencies = []
    unit_zones = []  # type: List[mapping.Rectangle]
    civilian = True
    slot_version = 1

    def __init__(self):
        self.runway_used = None
        self.runways = []  # type: List[Runway]
        self.parking_slots = []  # type: List[ParkingSlot]

        # warehouse values
        self.coalition = "NEUTRAL"
        self.size = 100
        self.speed = 16.666666
        self.periodicity = 30
        self.unlimited_munitions = True
        self.unlimited_aircrafts = True
        self.unlimited_fuel = True
        self.operating_level_air = 10
        self.operating_level_fuel = 10
        self.operating_level_equipment = 10
        self.aircrafts = {}
        self.weapons = {}
        self.suppliers = {}
        self.gasoline_init = 100
        self.methanol_mixture_init = 100
        self.diesel_init = 100
        self.jet_init = 100

    def load_from_dict(self, d):
        self.coalition = d["coalition"]
        self.speed = d["speed"]
        self.size = d["size"]
        self.periodicity = d["periodicity"]
        self.unlimited_munitions = d["unlimitedMunitions"]
        self.unlimited_fuel = d["unlimitedFuel"]
        self.unlimited_aircrafts = d["unlimitedAircrafts"]
        self.operating_level_air = d["OperatingLevel_Air"]
        self.operating_level_equipment = d["OperatingLevel_Eqp"]
        self.operating_level_fuel = d["OperatingLevel_Fuel"]
        self.gasoline_init = d.get("gasoline", {}).get("InitFuel", 100)
        self.diesel_init = d.get("diesel", {}).get("InitFuel", 100)
        self.jet_init = d.get("jet_fuel", {}).get("InitFuel", 100)
        self.methanol_mixture_init = d.get("methanol_mixture", {}).get("InitFuel", 100)
        self.aircrafts = d["aircrafts"]
        self.weapons = d["weapons"]

    def set_blue(self):
        self.set_coalition("BLUE")

    def set_red(self):
        self.set_coalition("RED")

    def set_neutral(self):
        self.set_coalition("NEUTRAL")

    def set_coalition(self, side):
        if side.lower() in ["red", "blue", "neutral"]:
            self.coalition = side.upper()
            return True
        return False

    def is_red(self):
        return self.coalition == "RED"

    def is_blue(self):
        return self.coalition == "BLUE"

    def random_unit_zone(self) -> mapping.Rectangle:
        if self.unit_zones:
            return self.unit_zones[random.randrange(0, len(self.unit_zones))]
        return mapping.Rectangle.from_point(mapping.Point(self.position.x + 500, self.position.y), 200)

    def occupy_runway(self, group):
        # if self.runway_used is not None:
        #     raise RunwayOccupiedError(
        #         "{a} Airport runway already in use by group {gname}, cannot assign {g} to it.".format(
        #             a=self.name, gname=self.runway_used.name, g=group.name)
        self.runway_used = group
        return self.runway_used

    def parking_slot(self, index: int) -> Optional[ParkingSlot]:
        """Searches the parking slot with the given crossroad index.

        Args:
            index: crossroad index of the parkings slot

        Returns:
            ParkingSlot: the found slot or None if not found.
        """
        for x in self.parking_slots:
            if x.crossroad_idx == index:
                return x
        return None

    def clear_parking_slot(self, index: int) -> bool:
        slot = self.parking_slot(index)
        if slot:
            slot.unit_id = None
            return True

        return False

    def _free_parking_slots_resolve_v1(self, large: bool, helicopter: bool) -> List[ParkingSlot]:
        slots_index = range(0, len(self.parking_slots))
        free_large_slots = {x for x in slots_index
                            if self.parking_slots[x].unit_id is None and
                            self.parking_slots[x].large}

        large_slots = sorted([self.parking_slots[x] for x in free_large_slots], key=lambda x: x.slot_name)
        if large:
            return large_slots

        free_heli_slots = {x for x in slots_index
                           if self.parking_slots[x].unit_id is None and
                           self.parking_slots[x].helicopter and not self.parking_slots[x].large}

        heli_slots = sorted([self.parking_slots[x] for x in free_heli_slots], key=lambda x: x.slot_name)
        if helicopter:
            return heli_slots + large_slots

        free_slots = list(self.parking_slots[x] for x in slots_index if self.parking_slots[x].unit_id is None and
                          not self.parking_slots[x].large and not self.parking_slots[x].helicopter)
        free_slots = sorted(free_slots, key=lambda x: x.slot_name)
        return free_slots + heli_slots + large_slots

    def _free_parking_slots_resolve_v2(self, aircraft_type: unittype.FlyingType) -> List[ParkingSlot]:
        free_slots = [x for x in self.parking_slots
                      if x.unit_id is None and
                      aircraft_type.width < x.width and
                      aircraft_type.height < (x.height or 1000) and
                      aircraft_type.length < x.length]

        if aircraft_type.helicopter:
            free_slots = [x for x in free_slots if x.helicopter]

        slots_sorted = sorted(free_slots, key=lambda x: (x.helicopter, x.slot_name))
        return slots_sorted

    def free_parking_slots(self, aircraft_type: unittype.FlyingType) -> List[ParkingSlot]:
        if self.slot_version == 1:
            return self._free_parking_slots_resolve_v1(aircraft_type.large_parking_slot, aircraft_type.helicopter)
        else:
            return self._free_parking_slots_resolve_v2(aircraft_type)

    def free_parking_slot(self, aircraft_type: Type[unittype.FlyingType]) -> Optional[ParkingSlot]:
        slots = self.free_parking_slots(aircraft_type)
        if slots:
            return slots[0]
        return None

    def dict(self):
        d = {
            "coalition": self.coalition,
            "speed": self.speed,
            "size": self.size,
            "periodicity": self.periodicity,
            "unlimitedMunitions": self.unlimited_munitions,
            "unlimitedFuel": self.unlimited_fuel,
            "unlimitedAircrafts": self.unlimited_aircrafts,
            "OperatingLevel_Air": self.operating_level_air,
            "OperatingLevel_Eqp": self.operating_level_equipment,
            "OperatingLevel_Fuel": self.operating_level_fuel,
            "gasoline": {"InitFuel": self.gasoline_init},
            "diesel": {"InitFuel": self.diesel_init},
            "jet_fuel": {"InitFuel": self.jet_init},
            "methanol_mixture": {"InitFuel": self.methanol_mixture_init},
            "aircrafts": self.aircrafts,
            "weapons": self.weapons,
            "suppliers": self.suppliers
        }
        return d

    def __repr__(self):
        return "Airport(" + self.name + ")"


class MapView:
    def __init__(self, center: mapping.Point, zoom=1000000):
        self.position = center
        self.zoom = zoom

    def load_from_dict(self, d):
        self.position = mapping.Point(d["centerX"], d["centerY"])
        self.zoom = d["zoom"]

    def dict(self):
        return {
            "centerX": self.position.x,
            "centerY": self.position.y,
            "zoom": self.zoom
        }


class Node:
    def __init__(self, name, rating, position: mapping.Point):
        self.name = name
        self.rating = rating
        self.position = position  # type: mapping.Point
        """Air defence positions for small arms, mostly on buildings"""
        self.air_defence_pos_small = []  # type: List[mapping.Point]

    def __repr__(self):
        return 'Node("{name}", {r})'.format(name=self.name, r=self.rating)


class Graph:
    Edge_indicators = {'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'}

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.edge_properties = {}

    def node(self, node_name) -> Node:
        for x in self.nodes:
            if x.name == node_name:
                return x
        raise RuntimeError('Node not found: ' + node_name)

    def node_names(self) -> Set[str]:
        return {x.name for x in self.nodes}

    def nearest_node(self, position: mapping.Point):
        """Find nearest node to the given point.

        Args:
            position: Point to find the nearest

        Returns:
            The nearest node to the that point
        """
        dist = sys.float_info.max
        node = None
        for x in self.nodes:
            d = position.distance_to_point(x.position)
            if d < dist:
                node = x
                dist = d

        return node

    def rated_nodes(self, min_rating=0) -> Set[Node]:
        return {x for x in self.nodes if x.rating and x.rating > min_rating}

    def nodes_within(self, polygon: mapping.Polygon) -> List[Node]:
        return [x for x in self.nodes if polygon.point_in_poly(x.position)]

    def rated_nodes_within(self, polygon: mapping.Polygon, min_rating=0) -> List[Node]:
        return [x for x in self.rated_nodes(min_rating) if polygon.point_in_poly(x.position)]

    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_edge(self, from_node: Node, to_node: Node, distance: int, on_road: bool = True):
        if to_node.name not in self.edges[from_node.name]:
            self.edges[from_node.name].append(to_node.name)
        if from_node.name not in self.edges[to_node.name]:
            self.edges[to_node.name].append(from_node.name)
        self.edge_properties[(from_node.name, to_node.name)] = (distance, on_road)

    @staticmethod
    def from_pickle(pickle_file):
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)

    def _dijkstra(self, initial):
        visited = {initial: 0}
        path = {}

        nodes = self.node_names()

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                try:
                    weight = current_weight + self.edge_properties[(min_node, edge)][0]
                except KeyError:
                    continue
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path

    def shortest_path(self, origin, destination) -> Tuple[int, List[str]]:
        visited, paths = self._dijkstra(origin)
        full_path = deque()
        _destination = paths[destination]

        while _destination != origin:
            full_path.appendleft(_destination)
            _destination = paths[_destination]

        full_path.appendleft(origin)
        full_path.append(destination)

        return visited[destination], list(full_path)

    def travel(self, vehicle_group, from_node: Node, to_node: Node, speed=32):
        distance, path = self.shortest_path(from_node.name, to_node.name)
        last = path[0]
        for p in path[1:]:
            current_node = self.node(p)
            if not self.edge_properties[(last, p)][1]:
                vehicle_group.add_waypoint(current_node.position + mapping.Point(1, 0),
                                           speed=speed,
                                           move_formation=point.PointAction.OffRoad)
                vehicle_group.add_waypoint(current_node.position,
                                           speed=speed,
                                           move_formation=point.PointAction.OnRoad)
            else:
                vehicle_group.add_waypoint(current_node.position,
                                           speed=speed,
                                           move_formation=point.PointAction.OnRoad)
            last = p
        return distance, path

    def store_pickle(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    def __str__(self):
        s = "digraph city_graph {\n"
        for x in self.nodes:
            s += '  "' + x.name + '" -> ' + ",".join(['"' + y + '"' for y in self.edges[x.name]]) + "\n"
        s += "}\n"
        return s


class Terrain:
    bounds = None  # type: mapping.Rectangle
    map_view_default = None  # type: MapView
    city_graph = Graph()  # type: Graph
    temperature = [
        (-4, 14),
        (-8, 14),
        (-6, 16),
        (0, 19),
        (1, 24),
        (8, 30),
        (12, 33),
        (12, 32),
        (10, 28),
        (2, 22),
        (-2, 14),
        (-4, 12)
    ]
    assert(len(temperature) == 12)

    def __init__(self, name: str):
        self.name = name
        self.center = {"lat": 0, "long": 0}  # WGS84 decimal
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}
        self.airports = {}  # type: Dict[str,Airport]

    def weather(self, dt: datetime, weather_: weather.Weather):
        # check if there might be the season for thunderstorms
        if 4 < dt.month < 11:
            if random.random() > 0.9:
                weather_.random_thunderstorm()
                return self.random_season_temperature(dt)

        weather_.dynamic_weather(random.choice(list(weather.Weather.BaricSystem)), random.randint(1, 4))
        return self.random_season_temperature(dt)

    def airport_by_id(self, _id: int) -> Optional[Airport]:
        for x in self.airports:
            if self.airports[x].id == _id:
                return self.airports[x]
        return None

    def airport_list(self) -> List[Airport]:
        for x in self.airports:
            yield self.airports[x]

    def nearest_airport(self, position: mapping.Point, coalition: str = None) -> Optional[Airport]:
        airports = [x for x in self.airports.values()
                    if x.coalition.lower() == coalition.lower()] if coalition else self.airports

        dist = sys.float_info.max
        airport = None
        for x in airports:
            d = position.distance_to_point(x.position)
            if d < dist:
                airport = x
                dist = d

        return airport

    def airport_within(self, position: mapping.Point, distance) -> List[Airport]:
        """Return all airports within the radius of a given point.

        Args:
            position(mapping.Point): Center of circle
            distance: Distance to the point

        Returns:
            Sequence of airports within range.
        """
        return [self.airports[x] for x in self.airports
                if self.airports[x].position.distance_to_point(position) < distance]

    def random_season_temperature(self, dt: datetime) -> int:
        return random.randint(self.temperature[dt.month - 1][0], self.temperature[dt.month - 1][1])


class Warehouses:
    def __init__(self, terrain: Terrain):
        self.terrain = terrain
        self.warehouses = {}

    def load_dict(self, data):
        for x in data.get("airports", {}):
            self.terrain.airport_by_id(x).load_from_dict(data["airports"][x])

    def __str__(self):
        airports = self.terrain.airports
        d = {
            "warehouses": self.warehouses,
            "airports": {airports[x].id: airports[x].dict() for x in airports}
        }
        return lua.dumps(d, "warehouses", 1)
