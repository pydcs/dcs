from __future__ import annotations

from dataclasses import dataclass

import math
import random
import copy
from typing import TYPE_CHECKING, Any, List, Optional, Tuple, Union

if TYPE_CHECKING:
    from dcs.terrain.terrain import Terrain


def point_from_heading(_x: float, _y: float, heading: float, distance: float) -> Tuple[float, float]:
    """Calculates a point from a given point, heading and distance.

    :param _x: source point x
    :param _y: source point y
    :param heading: heading in degrees from source point
    :param distance: distance from source point
    :return: returns a tuple (x, y) of the calculated point
    """
    while heading < 0:
        heading += 360
    heading %= 360
    rad_heading = math.radians(heading)
    x = _x + math.cos(rad_heading) * distance
    y = _y + math.sin(rad_heading) * distance

    return x, y


def _distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Returns the distance between 2 points

    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    :return: distance in point units(m)
    """
    return math.hypot(x2 - x1, y2 - y1)


def heading_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
    """Returns the angle between 2 points in degrees.

    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    :return: angle in degrees
    """
    def angle_trunc(a):
        while a < 0.0:
            a += math.pi * 2
        return a
    deltax = x2 - x1
    deltay = y2 - y1
    return math.degrees(angle_trunc(math.atan2(deltay, deltax)))


@dataclass(frozen=True)
class LatLng:
    lat: float
    lng: float

    def as_list(self) -> List[float]:
        return [self.lat, self.lng]

    @staticmethod
    def _components(dimension: float) -> Tuple[int, int, float]:
        degrees = int(dimension)
        minutes = int(dimension * 60 % 60)
        seconds = dimension * 3600 % 60
        return degrees, minutes, seconds

    def _format_component(
        self, dimension: float, hemispheres: Tuple[str, str], seconds_precision: int
    ) -> str:
        hemisphere = hemispheres[0] if dimension >= 0 else hemispheres[1]
        degrees, minutes, seconds = self._components(dimension)
        return f"{degrees}°{minutes:02}'{seconds:02.{seconds_precision}f}\"{hemisphere}"

    def format_dms(self, include_decimal_seconds: bool = False) -> str:
        precision = 2 if include_decimal_seconds else 0
        return " ".join(
            [
                self._format_component(self.lat, ("N", "S"), precision),
                self._format_component(self.lng, ("E", "W"), precision),
            ]
        )


@dataclass
class Vector2:
    x: float
    y: float


class Point(Vector2):
    def __init__(self, x: float, y: float, terrain: Terrain) -> None:
        super().__init__(x, y)
        self._terrain = terrain

    def latlng(self) -> LatLng:
        lat, lon = self._terrain._point_to_ll_transformer.transform(self.x, self.y)
        return LatLng(lat, lon)

    @staticmethod
    def from_latlng(latlng: LatLng, terrain: Terrain) -> Point:
        x, y = terrain._ll_to_point_transformer.transform(latlng.lat, latlng.lng)
        return Point(x, y, terrain)

    def new_in_same_map(self, x: float, y: float) -> Point:
        return Point(x, y, self._terrain)

    def point_from_heading(self, heading: float, distance: float) -> Point:
        x, y = point_from_heading(self.x, self.y, heading, distance)
        return Point(x, y, self._terrain)

    def midpoint(self, other: Vector2) -> Point:
        return (self + other) / 2

    def lerp(self, other: Vector2, t: float) -> Point:
        def _lerp(v0: float, v1: float, t: float) -> float:
            return (1 - t) * v0 + t * v1
        return Point(_lerp(self.x, other.x, t), _lerp(self.y, other.y, t), self._terrain)

    def heading_between_point(self, point: Vector2) -> float:
        return heading_between_points(self.x, self.y, point.x, point.y)

    def distance_to_point(self, point: Point) -> float:
        return _distance(self.x, self.y, point.x, point.y)

    def random_point_within(self, distance: float, min_distance: float = 0) -> Point:
        """Returns a random point within the given distance.

        This is a shortcut for Rectangle.from_point().random_point().

        Args:
            distance: max distance for the random point.
            min_distance: minimum distance the random point should have from origin

        Returns:
            Point: a new random point within the given distance from the point.
        """
        return self.point_from_heading(random.randrange(0, 360),
                                       random.random() * (distance - min_distance) + min_distance)

    def __add__(self, other: Vector2) -> Point:
        return Point(self.x + other.x, self.y + other.y, self._terrain)

    def __radd__(self, other: Union[float, Vector2]) -> Point:
        if isinstance(other, Vector2):
            return self + other
        return Point(self.x + other, self.y + other, self._terrain)

    def __sub__(self, other: Union[float, Vector2]) -> Point:
        if isinstance(other, Vector2):
            return Point(self.x - other.x, self.y - other.y, self._terrain)
        return Point(self.x - other, self.y - other, self._terrain)

    def __mul__(self, other: float) -> Point:
        return Point(self.x * other, self.y * other, self._terrain)

    def __rmul__(self, other: float) -> Point:
        return self * other

    def __truediv__(self, other: float) -> Point:
        return self * (1 / other)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __repr__(self) -> str:
        return f"Point({self.x!r}, {self.y!r}, {self._terrain!r})"


class Triangle:
    def __init__(self, points: Tuple[Point, Point, Point]) -> None:
        self.points = points

    def area(self) -> float:
        a = (self.points[0].x * self.points[1].y + self.points[1].x * self.points[2].y
             + self.points[2].x * self.points[0].y - self.points[0].y * self.points[1].x
             - self.points[1].y * self.points[2].x - self.points[2].y * self.points[0].x)
        a /= 2
        return a

    def random_point(self) -> Point:
        r = random.random()
        s = random.random()
        if r + s >= 1:
            r = 1 - r
            s = 1 - s

        return self.points[0] + (r * (self.points[1] - self.points[0]) + s * (self.points[2] - self.points[0]))

    def __repr__(self) -> str:
        return "Triangle({points})".format(points=", ".join(map(repr, self.points)))


class Rectangle:
    def __init__(self, top: float, left: float, bottom: float, right: float, terrain: Terrain) -> None:
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        self._terrain = terrain

    @staticmethod
    def from_point(point: Point, side_length: float) -> Rectangle:
        top = point.x + side_length / 2
        left = point.y - side_length / 2
        bottom = point.x - side_length / 2
        right = point.y + side_length / 2
        return Rectangle(top, left, bottom, right, point._terrain)

    def point_in_rect(self, point: Point) -> bool:
        return self.bottom <= point.x <= self.top and self.left <= point.y <= self.right

    def height(self) -> float:
        return self.top - self.bottom

    def width(self) -> float:
        return self.right - self.left

    def center(self) -> Point:
        return Point(self.bottom + (self.height() / 2), self.left + (self.width() / 2), self._terrain)

    def resize(self, percentage: float) -> Rectangle:
        w = self.width()
        h = self.height()
        w *= percentage / 2
        h *= percentage / 2
        c = self.center()
        return Rectangle(c.x + h, c.y - w, c.x - h, c.y + w, self._terrain)

    def random_point(self) -> Point:
        x = self.bottom + random.random() * (self.top - self.bottom)
        y = self.left + random.random() * (self.right - self.left)
        return Point(x, y, self._terrain)

    def random_distant_points(self, distance: float) -> Tuple[Point, Point]:
        # determine vertical/horizontal
        if self.width() > self.height():
            axis_y = self.width()
            axis_x = self.height()
            sy = self.left
            sx = self.bottom
            hdg_start = 60
        else:
            axis_y = self.height()
            axis_x = self.width()
            sy = self.bottom
            sx = self.left
            hdg_start = 330

        d = distance if distance < axis_y else axis_y * 0.2
        sy += random.random() * (axis_y - d)
        sx += random.random() * axis_x
        p1 = Point(sx, sy, self._terrain)
        while True:
            hdg = random.random() * 60
            p2 = p1.point_from_heading(hdg_start + hdg, d)
            if self.point_in_rect(p2):
                return p1, p2

    def __eq__(self, other: Any) -> bool:
        return self.top == other.top and self.bottom == other.bottom \
            and self.left == other.left and self.right == other.right

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __repr__(self) -> str:
        t, l, b, r = (
            self.top,
            self.left,
            self.bottom,
            self.right,
        )
        return f"Rectangle({t!r}, {l!r}, {b!r}, {r!r}, {self._terrain!r})"


class Polygon:
    def __init__(self, terrain: Terrain, points: Optional[List[Point]] = None):
        self._terrain = terrain
        if points is None:
            points = []
        self.points = copy.copy(points)

    def point_in_poly(self, point: Point) -> bool:
        """Checks if the given point is within the polygon.

        :param point: Point to test
        :return: True if point is within the polygon else False
        """
        n = len(self.points)
        inside = False

        p1x = self.points[0].x
        p1y = self.points[0].y
        for i in range(n + 1):
            p = self.points[i % n]
            p2x = p.x
            p2y = p.y
            if point.y > min(p1y, p2y):
                if point.y <= max(p1y, p2y):
                    if point.x <= max(p1x, p2x):
                        xs = 0.0
                        if p1y != p2y:
                            xs = (point.y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or point.x <= xs:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

    def random_point(self) -> Point:
        """Returns a random point within this polygon object

        :return: a random point
        """
        # split polygon into triangles using ear clipping
        tris = self.triangulate()

        # calculate areas of the triangles
        areas = [(x, x.area()) for x in tris]
        full_area = sum([x[1] for x in areas])  # calculate full area
        rtri = random.random() * full_area  # get a random value from the area

        # iterate through areas until we found "ours"
        s = areas[0][1]
        i = 1
        while s <= rtri:
            s += areas[i][1]
            i += 1

        # return a random point from this triangle
        return areas[i - 1][0].random_point()

    @staticmethod
    def is_convex(a: Point, b: Point, c: Point) -> bool:
        # only convex if traversing anti-clockwise!
        crossp = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        if crossp >= 0:
            return True
        return False

    @staticmethod
    def in_triangle(a: Point, b: Point, c: Point, p: Point) -> bool:
        l_kup = [0.0, 0.0, 0.0]
        eps = 0.0000001
        # calculate barycentric coefficients for point p
        # eps is needed as error correction since for very small distances denom->0
        l_kup[0] = ((b.y - c.y) * (p.x - c.x) + (c.x - b.x) * (p.y - c.y)) / (((b.y - c.y) * (a.x - c.x)
                                                                               + (c.x - b.x) * (a.y - c.y)) + eps)
        l_kup[1] = ((c.y - a.y) * (p.x - c.x) + (a.x - c.x) * (p.y - c.y)) / (((b.y - c.y) * (a.x - c.x)
                                                                               + (c.x - b.x) * (a.y - c.y)) + eps)
        l_kup[2] = 1 - l_kup[0] - l_kup[1]
        # check if p lies in triangle (a, b, c)
        for x in l_kup:
            if x >= 1 or x <= 0:
                return False
        return True

    def is_clockwise(self) -> bool:
        poly_length = len(self.points)
        # initialize sum with last element
        sum_ = (self.points[0].x - self.points[poly_length - 1].x) * (self.points[0].y + self.points[poly_length - 1].y)
        # iterate over all other elements (0 to n-1)
        for i in range(poly_length - 1):
            sum_ += (self.points[i + 1].x - self.points[i].x) * (self.points[i + 1].y + self.points[i].y)
        return sum_ > 0

    @staticmethod
    def get_ear(poly) -> Optional[Tuple[Point, Point, Point]]:
        size = len(poly)
        if size < 3:
            return None
        if size == 3:
            tri = (poly[0], poly[1], poly[2])
            del poly[:]
            return tri
        for i in range(size):
            tritest = False
            p1 = poly[(i - 1) % size]
            p2 = poly[i % size]
            p3 = poly[(i + 1) % size]
            if Polygon.is_convex(p1, p2, p3):
                for x in poly:
                    if not (x in (p1, p2, p3)) and Polygon.in_triangle(p1, p2, p3, x):
                        tritest = True
                if not tritest:
                    del poly[i % size]
                    return p1, p2, p3
        print('GetEar(): no ear found')
        return None

    def triangulate(self) -> List[Triangle]:
        tri = []
        plist = self.points[::-1] if self.is_clockwise() else self.points[:]
        while len(plist) >= 3:
            a = self.get_ear(plist)
            if a is None:
                break
            tri.append(Triangle(a))
        return tri

    def outbound_rectangle(self) -> Rectangle:
        top = max([x.x for x in self.points])
        bot = min([x.x for x in self.points])
        right = max([x.y for x in self.points])
        left = min([x.y for x in self.points])
        return Rectangle(top, left, bot, right, self._terrain)

    def __repr__(self) -> str:
        return f"Polygon([{self._terrain!r}, {self.points!r}])"
