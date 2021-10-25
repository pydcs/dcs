from dataclasses import dataclass
from typing import List

from dcs.drawing.drawing import Drawing, Rgba
from dcs.mapping import Point

# TODO: Research and define std icons

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