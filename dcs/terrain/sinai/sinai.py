import dcs.mapping as mapping
from dcs.terrain.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Sinai(Terrain):
    center = {"lat": 31.0, "long": 32.0}
    temperature = [
        (2, 8),
        (3, 11),
        (6, 15),
        (10, 21),
        (15, 27),
        (18, 32),
        (22, 35),
        (22, 35),
        (19, 32),
        (14, 26),
        (7, 17),
        (4, 10)
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(-450000, -280000, 500000, 560000, self)
        super().__init__(
            "Sinai",
            PARAMETERS,
            bounds,
            map_view_default=MapView(bounds.center(), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}

    @property
    def miz_theatre_name(self) -> str:
        return "SinaiMap"
