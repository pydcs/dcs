from enum import Enum, auto
from dataclasses import dataclass
import dcs.mapping as mapping


@dataclass()
class Rgba:
    r: int
    g: int
    b: int
    a: int


class LineStyle(Enum):
    # TODO: Values
    Solid = auto()
    Dot = auto()
    Dash = auto()
    Cross = auto()
    Square = auto()
    Triangle = auto()


@dataclass()
class Drawing:
    position: mapping.Point
    name: str
    color: Rgba
