from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any, Dict

from dcs.drawing.layer import Layer
from dcs.drawing.options import Options

if TYPE_CHECKING:
    from dcs.terrain import Terrain


class StandardLayer(Enum):
    Red = "Red"
    Blue = "Blue"
    Neutral = "Neutral"
    Common = "Common"
    Author = "Author"


class Drawings:
    def __init__(self, terrain: Terrain) -> None:
        self._terrain = terrain
        self.options = Options()
        self.layers = [
            Layer(True, StandardLayer.Red.value, [], terrain),
            Layer(True, StandardLayer.Blue.value, [], terrain),
            Layer(True, StandardLayer.Neutral.value, [], terrain),
            Layer(True, StandardLayer.Common.value, [], terrain),
            Layer(True, StandardLayer.Author.value, [], terrain),
        ]

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        self.options.load_from_dict(data["options"])
        self.layers = []
        for layer_index in sorted(data["layers"].keys()):
            layer_data = data["layers"][layer_index]
            layer = Layer(True, "", [], self._terrain)
            layer.load_from_dict(layer_data)
            self.layers.append(layer)

    def dict(self):
        d = {}
        d["options"] = self.options.dict()

        d["layers"] = {}
        i = 1
        for layer in self.layers:
            d["layers"][i] = layer.dict()
            i += 1

        return d

    def get_layer_by_name(self, layer_name: str):
        for layer in self.layers:
            if layer.name == layer_name:
                return layer

    def get_layer(self, layer: StandardLayer):
        return self.get_layer_by_name(layer.value)
