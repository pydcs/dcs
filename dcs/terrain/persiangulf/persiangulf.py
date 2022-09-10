from dcs.terrain.terrain import Terrain, MapView
import dcs.mapping as mapping
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class PersianGulf(Terrain):
    center = {"lat": 0, "long": 0}
    temperature = [
        (10, 20),
        (11, 20),
        (13, 22),
        (16, 26),
        (18, 30),
        (20, 36),
        (24, 39),
        (25, 40),
        (22, 37),
        (20, 32),
        (16, 26),
        (12, 22)
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(-218768.750000, -392081.937500, 197357.906250, 333129.125000, self)
        super().__init__(
            "PersianGulf",
            PARAMETERS,
            bounds,
            map_view_default=MapView(bounds.center(), self, 1000000)
        )
        self.bullseye_blue = {"x": self.bounds.center().x, "y": self.bounds.center().y}
        self.bullseye_red = {"x": self.bounds.center().x, "y": self.bounds.center().y}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
