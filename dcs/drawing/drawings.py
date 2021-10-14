from dataclasses import dataclass
from typing import List

from dcs.drawing.drawing import Drawing


@dataclass()
class Drawings:
    drawings: List[Drawing]

    def load_from_dict(self, data):
        raise NotImplementedError()

    def dict(self):
        raise NotImplementedError()

    def add_drawing(drawing: Drawing):
        raise NotImplementedError()

    def remove_drawing(name: str):
        raise NotImplementedError()
