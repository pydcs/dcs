import dcs.mapping as mapping
from dcs.terrain.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class TheChannel(Terrain):
    center = {"lat": 50.875, "long": 1.5875}
    temperature = [
        (-10, 10),
        (-9, 10),
        (-3, 12),
        (-1, 14),
        (0, 18),
        (2, 22),
        (7, 30),
        (8, 32),
        (3, 28),
        (0, 22),
        (-2, 16),
        (-8, 10)
    ]
    assert len(temperature) == 12

    def __init__(self):
        super().__init__(
            "TheChannel",
            PARAMETERS,
            bounds=mapping.Rectangle(74967, -114995, -129982, 129991, self),
            map_view_default=MapView(mapping.Point(0, 0, self), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
