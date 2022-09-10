from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class MarianaIslands(Terrain):
    center = {"lat": 13.485, "long": 144.798}
    temperature = [
        # https://en.wikipedia.org/wiki/Guam#Climate
        (24, 30),
        (24, 30),
        (24, 30),
        (25, 31),
        (25, 31),
        (25, 31),
        (25, 31),
        (25, 30),
        (25, 30),
        (25, 30),
        (25, 30),
        (25, 30)
    ]

    assert len(temperature) == 12

    def __init__(self):
        super().__init__(
            "MarianaIslands",
            PARAMETERS,
            bounds=mapping.Rectangle(1000 * 10000, -1000 * 1000, -300 * 1000, 500 * 1000, self),
            map_view_default=MapView(mapping.Point(76432, 48051, self), self, 1000000)
        )

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
