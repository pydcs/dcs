import datetime

from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Kola(Terrain):

    temperature = [
        (-14, 7),
        (-14, 7),
        (-3, 15),
        (-3, 15),
        (-3, 15),
        (10, 20),
        (10, 20),
        (10, 20),
        (-3, 15),
        (-3, 15),
        (-3, 15),
        (-14, 7),
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(900000, -900000, -315000, 855500, self)
        super().__init__(
            "Kola",
            PARAMETERS,
            bounds=bounds,
            map_view_default=MapView(bounds.center(), self, 1000000),
            utc_offset=datetime.zoneinfo(datetime.timedelta(hours=2))
        )
        self.bullseye_blue = {"x": bounds.center().x, "y": bounds.center().y}
        self.bullseye_red = {"x": bounds.center().x, "y": bounds.center().y}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
