from dataclasses import dataclass
from dcs.drawing.drawing import Drawing, Rgba


@dataclass()
class TextBox(Drawing):
    text: str
    font_size: int
    font: str
    border_thickness: float
    fill: Rgba
    angle: float

    def dict(self):
        d = super().dict()
        d["primitiveType"] = "TextBox"
        d["text"] = self.text
        d["fontSize"] = self.font_size
        d["font"] = self.font
        d["borderThickness"] = self.border_thickness
        d["fillColorString"] = self.fill.to_color_string()
        d["angle"] = self.angle
        return d
