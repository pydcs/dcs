from dataclasses import dataclass

from dcs.drawing.drawing import Drawing, LineStyle, Rgba


@dataclass()
class PolygonDrawing(Drawing):
    fill: Rgba
    line_thickness: float  # ?
    line_style: LineStyle
    angle: float  # ?


@dataclass()
class Circle(PolygonDrawing):
    radius: float  # ?


@dataclass()
class Oval(PolygonDrawing):
    radius1: float  # ?
    radius2: float  # ?


@dataclass()
class Rectangle(PolygonDrawing):
    width: float  # ?
    height: float  # ?


@dataclass()
class FreeFormPolygon(PolygonDrawing):
    pass


@dataclass()
class Arrow(PolygonDrawing):
    pass
