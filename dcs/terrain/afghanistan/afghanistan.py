"""DCS: Afghanistan terrain definition."""

import datetime

from dcs import mapping
from dcs.terrain import MapView, Terrain

from .airports import all_airports
from .projection import PARAMETERS


class Afghanistan(Terrain):
    """The DCS Afghanistan theatre (``Afghanistan`` in a .miz file)."""

    temperature = [
        (-10, 4),
        (-7, 7),
        (0, 14),
        (6, 22),
        (11, 29),
        (16, 35),
        (20, 37),
        (18, 35),
        (12, 30),
        (5, 23),
        (-1, 15),
        (-7, 7),
    ]
    assert len(temperature) == 12

    def __init__(self) -> None:
        # Covers the full map and every currently shipped Afghanistan airfield.
        bounds = mapping.Rectangle(-500000, -500000, 500000, 500000, self)
        super().__init__(
            "Afghanistan",
            PARAMETERS,
            bounds=bounds,
            map_view_default=MapView(bounds.center(), self, 1000000),
            utc_offset=datetime.timezone(datetime.timedelta(hours=4, minutes=30)),
        )
        self.bullseye_blue = {"x": bounds.center().x, "y": bounds.center().y}
        self.bullseye_red = {"x": bounds.center().x, "y": bounds.center().y}
        self.airports = {airport.name: airport for airport in all_airports(self)}
