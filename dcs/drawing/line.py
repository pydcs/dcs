from dataclasses import dataclass
from enum import Enum
from typing import List

from dcs.drawing.drawing import Drawing, LineStyle
from dcs.mapping import Point


class LineMode(Enum):
    Segment = "segment"
    Segments = "segments"
    Free = "free"


@dataclass
class LineDrawing(Drawing):
    closed: bool
    line_thickness: float
    line_style: LineStyle
    line_mode: LineMode
    points: List[Point]

    def dict(self):
        d = super().dict()
        d["primitiveType"] = "Line"
        d["closed"] = self.closed
        d["thickness"] = self.line_thickness
        d["style"] = self.line_style.value
        d["lineMode"] = self.line_mode.value
        d["points"] = super().points_to_dict(self.points)
        return d
