from enum import Enum
from dataclasses import dataclass
import dcs.mapping as mapping


@dataclass
class Rgba:
    r: int
    g: int
    b: int
    a: int

    def to_color_string(self) -> str:
        return f"0x{int(self.r):02x}{int(self.g):02x}{int(self.b):02x}{int(self.a):02x}"

    @classmethod
    def from_color_string(cls, s: str):
        s = s.replace("#", "").replace("0x", "")
        rgba = tuple(int(s[i:i + 2], 16) for i in (0, 2, 4, 6))
        return cls(rgba[0], rgba[1], rgba[2], rgba[3])


class LineStyle(Enum):
    Solid = "solid"
    Dot = "dot"
    Dash = "dash"
    Cross = "cross"
    Square = "square"
    Triangle = "triangle"
    Wirefence = "wirefence"
    Dot2 = "dot2"
    Solid2 = "solid2"
    DotDash = "dotdash"
    StrongPoint = "strongpoint"
    WireFence = "wirefence"
    Boundry1 = "boundry1"
    Boundry2 = "boundry2"
    Boundry3 = "boundry3"
    Boundry4 = "boundry4"
    Boundry5 = "boundry5"


@dataclass
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
            d[i] = {"x": point.x, "y": point.y}
            i += 1
        return d
