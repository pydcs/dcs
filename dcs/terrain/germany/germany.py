import datetime

from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Germany(Terrain):

    temperature = [
        (-5, 5),
        (-5, 5),
        (0, 15),
        (0, 15),
        (0, 15),
        (10, 30),
        (10, 30),
        (10, 30),
        (0, 15),
        (0, 15),
        (0, 15),
        (-5, 5)
    ]
    assert len(temperature) == 12

    def __init__(self):
        bounds = mapping.Rectangle(200000, -600000, -1100000, -300000, self)
        super().__init__(
            "GermanyCW",
            PARAMETERS,
            bounds=bounds,
            map_view_default=MapView(bounds.center(), self, 1000000),
            utc_offset=datetime.zoneinfo(datetime.timedelta(hours=2))
        )
        self.bullseye_blue = {"x": bounds.center().x, "y": bounds.center().y}
        self.bullseye_red = {"x": bounds.center().x, "y": bounds.center().y}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
