from dataclasses import dataclass
from typing import List

from dcs.drawing.drawing import Drawing, Rgba
from dcs.mapping import Point


@dataclass()
class Icon(Drawing):
    file: str
    scale: float
    angle: int

    def dict(self):
        d = super().dict()
        d["primitiveType"] = "Icon"
        d["file"] = self.file
        d["scale"] = self.scale
        d["angle"] = self.angle
        return d

    @classmethod
    def create(cls, position: Point, file: str, scale=1.0, color=Rgba(255, 0, 0, 255)):
        return cls(True, position, "An icon", color, "", file, scale, 0)