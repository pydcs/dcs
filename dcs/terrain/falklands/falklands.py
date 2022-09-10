from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Falklands(Terrain):
    center = {"lat": 52.468, "long": 59.173}
    temperature = [
        (5, 17),
        (5, 17),
        (2, 14),
        (2, 14),
        (2, 14),
        (-5, 11),
        (-5, 11),
        (-5, 11),
        (1, 15),
        (1, 15),
        (1, 15),
        (5, 17)
    ]
    assert len(temperature) == 12

    def __init__(self):
        super().__init__(
            "Falklands",
            PARAMETERS,
            bounds=mapping.Rectangle(74967, -114995, -129982, 129991, self),
            map_view_default=MapView(mapping.Point(0, 0, self), self, 1000000)
        )
        self.bullseye_blue = {"x": 0, "y": 0}
        self.bullseye_red = {"x": 0, "y": 0}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
