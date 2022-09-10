from dcs.terrain.terrain import Terrain, MapView
import dcs.mapping as mapping
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Normandy(Terrain):
    center = {"lat": 41.3, "long": 0.18}
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

    def __init__(self) -> None:
        bounds = mapping.Rectangle(-132707.843750, -389942.906250, 185756.156250, 165065.078125, self)
        super().__init__(
            "Normandy",
            PARAMETERS,
            bounds,
            map_view_default=MapView(bounds.center(), self, 1000000)
        )
        self.bullseye_blue = {"x": self.bounds.center().x, "y": self.bounds.center().y}
        self.bullseye_red = {"x": self.bounds.center().x, "y": self.bounds.center().y}

        # Ignore type checking on the following line because for some reason this
        # doesn't type-check for Normandy but is fine for every other terrain.
        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}  # type: ignore
