from dataclasses import dataclass

from dcs.drawing.drawing import Drawing, LineStyle


@dataclass()
class LineDrawing(Drawing):
    line_thickness: float  # ?
    line_style: LineStyle


@dataclass()
class LineSegment(LineDrawing):
    pass


@dataclass()
class LineSegments(LineDrawing):
    pass


@dataclass()
class FreeFormLine(LineDrawing):
    pass
