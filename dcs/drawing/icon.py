from dataclasses import dataclass

from dcs.drawing.drawing import Drawing


@dataclass()
class Icon(Drawing):
    icon_type: str
