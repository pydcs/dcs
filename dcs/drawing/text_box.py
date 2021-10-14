from dataclasses import dataclass

from dcs.drawing.drawing import Drawing, Rgba


@dataclass()
class TextBox(Drawing):
    text: str
    font_size: int  # ?
    angle: float  # ?
    line_thickness: int  # ?
    fill: Rgba
