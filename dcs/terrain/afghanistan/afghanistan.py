import datetime

from dcs import mapping
from dcs.terrain import Terrain, MapView
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Afghanistan(Terrain):

    # Kabul-area climate, (min, max) deg C per month; only seeds the mission editor's default weather.
    temperature = [
        (-7, 5),
        (-5, 7),
        (1, 13),
        (6, 19),
        (9, 24),
        (13, 30),
        (16, 32),
        (15, 31),
        (10, 27),
        (4, 21),
        (-1, 13),
        (-5, 7),
    ]
    assert len(temperature) == 12

    def __init__(self):
        # SW_bound / NE_bound from the terrain's own config (km), read through the mission editor's terrainDATA
        bounds = mapping.Rectangle(532000, -534000, -1180000, 757000, self)
        super().__init__(
            "Afghanistan",
            PARAMETERS,
            bounds=bounds,
            map_view_default=MapView(bounds.center(), self, 1000000),
            utc_offset=datetime.timezone(datetime.timedelta(hours=4, minutes=30))
        )
        # defaultBullseye from the terrain config
        self.bullseye_blue = {"x": -258000, "y": -42500}
        self.bullseye_red = {"x": 41660, "y": -372200}

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}
