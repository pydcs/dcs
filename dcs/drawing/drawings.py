from dataclasses import dataclass
from typing import List

from dcs.drawing.layer import Layer

@dataclass()
class Options:
    # TODO: Implement an API to generate defaults
    hiddenOnF10Map: dict[str, dict[str, bool]]

    def load_from_dict(self, data):
        self.hiddenOnF10Map = data["hiddenOnF10Map"]

    def dict(self):
        d = {}
        d["hiddenOnF10Map"] = self.hiddenOnF10Map
        return d


class Drawings:
    options: Options
    layers: List[Layer]

    def __init__(self):
        # TODO: Default structures for options and layers
        self.options = Options({})
        self.layers = []

    def load_from_dict(self, data):
        self.options.load_from_dict(data["options"])
        for layer_index in sorted(data["layers"].keys()):
            layer_data = data["layers"][layer_index]
            layer = Layer(True, "", [])
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