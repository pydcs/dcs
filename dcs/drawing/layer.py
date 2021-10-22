from dataclasses import dataclass
from typing import List

from dcs.drawing.drawing import Drawing

@dataclass()
class Layer():
    visible: bool
    name: str
    objects: List[Drawing]

    def load_from_dict(self, data):
        self.visible = data["visible"]
        self.name = data["name"]
        # TODO: Objects

    def dict(self):
        d = {}
        d["visible"] = self.visible
        d["name"] = self.name
        # TODO: Objects
        return d

    def add_drawing(drawing: Drawing):
        raise NotImplementedError()

    def remove_drawing(name: str):
        raise NotImplementedError()