from typing import List

from dcs.drawing.layer import Layer
from dcs.drawing.options import Options


class Drawings:
    options: Options
    layers: List[Layer]

    def __init__(self):
        self.options = Options()
        self.layers = [
            Layer(True, "Red", []),
            Layer(True, "Blue", []),
            Layer(True, "Neutral", []),
            Layer(True, "Common", []),
            Layer(True, "Author", []),
        ]

    def load_from_dict(self, data):
        self.options.load_from_dict(data["options"])
        self.layers = []
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