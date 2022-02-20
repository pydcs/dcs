from dataclasses import dataclass
from enum import Enum
from typing import List

from dcs.drawing.drawing import Drawing, LineStyle, Rgba
from dcs.mapping import Point
from dcs.terrain import Terrain


class PolygonMode(Enum):
    Circle = "circle"
    Oval = "oval"
    Rectangle = "rect"
    Free = "free"
    Arrow = "arrow"


@dataclass
class PolygonDrawing(Drawing):
    fill: Rgba
    line_thickness: float
    line_style: LineStyle

    def dict(self):
        d = super().dict()
        d["primitiveType"] = "Polygon"
        d["fillColorString"] = self.fill.to_color_string()
        d["thickness"] = self.line_thickness
        d["style"] = self.line_style.value
        return d


@dataclass
class Circle(PolygonDrawing):
    radius: float

    def dict(self):
        d = super().dict()
        d["polygonMode"] = PolygonMode.Circle.value
        d["radius"] = self.radius
        return d


@dataclass
class Oval(PolygonDrawing):
    radius1: float
    radius2: float
    angle: float

    def dict(self):
        d = super().dict()
        d["polygonMode"] = PolygonMode.Oval.value
        d["r1"] = self.radius1
        d["r2"] = self.radius2
        d["angle"] = self.angle
        return d


@dataclass
class Rectangle(PolygonDrawing):
    width: float
    height: float
    angle: float

    def dict(self):
        d = super().dict()
        d["polygonMode"] = PolygonMode.Rectangle.value
        d["width"] = self.width
        d["height"] = self.height
        d["angle"] = self.angle
        return d


@dataclass
class FreeFormPolygon(PolygonDrawing):
    points: List[Point]

    def dict(self):
        d = super().dict()
        d["polygonMode"] = PolygonMode.Free.value
        d["points"] = super().points_to_dict(self.points)
        return d


@dataclass
class Arrow(PolygonDrawing):
    length: float
    angle: float
    points: List[Point]

    def dict(self):
        d = super().dict()
        d["polygonMode"] = PolygonMode.Arrow.value
        d["length"] = self.length
        d["angle"] = self.angle
        d["points"] = super().points_to_dict(self.points)
        return d

    @staticmethod
    def get_default_arrow_points(terrain: Terrain) -> List[Point]:
        return [
            Point(976.01054900139, 0, terrain),
            Point(976.01054900139, 5205.3895946741, terrain),
            Point(2602.694797337, 5205.3895946741, terrain),
            Point(0, 7808.0843920111, terrain),
            Point(-2602.694797337, 5205.3895946741, terrain),
            Point(-976.01054900139, 5205.3895946741, terrain),
            Point(-976.01054900139, 0, terrain),
            Point(976.01054900139, 0, terrain),
        ]
