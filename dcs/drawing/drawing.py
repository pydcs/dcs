from enum import Enum
from dataclasses import dataclass
from pathlib import PosixPath
from dcs import drawing
import dcs.mapping as mapping


@dataclass()
class Rgba:
    r: int
    g: int
    b: int
    a: int

    def to_color_string(self) -> str:
        # TODO: Implement
        return "0x00000000"

    @staticmethod
    def from_color_string(s: str):
        # TODO: Implement
        return Rgba(0, 0, 0, 255)


class LineStyle(Enum):
    Solid = "solid"
    Dot = "dot"
    Dash = "dash"
    Cross = "cross"
    Square = "square"
    Triangle = "triangle"


@dataclass()
class Drawing:
    visible: bool
    position: mapping.Point
    name: str
    color: Rgba
    layer_name: str

    def dict(self):
        d = {}
        d["visible"] = self.visible
        d["mapX"] = self.position.x
        d["mapY"] = self.position.y
        d["name"] = self.name
        d["colorString"] = self.color.to_color_string()
        d["layerName"] = self.layer_name
        return d

    def points_to_dict(self, points):
        d = {}
        i = 1
        for point in points:
            d[i] = { "x": point.x, "y": point.y }
            i += 1
        return d