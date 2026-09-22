"""Airport and parking data for the DCS Afghanistan terrain.

The bundled ``airports.json`` was exported from DCS 2.9.19.13478 by the
DCS Web Editor project.  It contains runway, ATC, and parking-stand data for
the 25 usable airfields available in that build.  Keeping the source export
alongside this loader preserves every stand instead of maintaining a large,
lossy generated Python module.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Iterator

from dcs import mapping
from dcs.atcradio import AtcRadio
from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain


_DATA_FILE = Path(__file__).with_name("airports.json")


def _opposite_runway(designator: int) -> str:
    """Return the reciprocal two-digit runway designator."""
    return f"{(designator + 17) % 36 + 1:02d}"


class AfghanistanAirport(Airport):
    """An airport hydrated from DCS's exported Afghanistan terrain data."""

    unit_zones: list[mapping.Rectangle] = []
    slot_version = 2

    def __init__(self, data: dict[str, Any], terrain: Terrain) -> None:
        self.id = int(data["ID"])
        self.name = str(data["displayName"])
        self.tacan = None
        self.civilian = bool(data["airdromeData"].get("civilian", True))

        atc_frequencies = data["airdromeData"].get("ATC", [])
        self.atc_radio = (
            AtcRadio(*sorted(atc_frequencies)) if len(atc_frequencies) == 4 else None
        )
        self.frequencies = atc_frequencies

        reference_point = data["pos"]["DCS"]
        super().__init__(
            mapping.Point(reference_point["x"], reference_point["z"], terrain), terrain
        )

        for runway in data.get("runways", []):
            designator = int(runway["Name"])
            main = f"{designator:02d}"
            opposite = _opposite_runway(designator)
            # DCS reports the course counter-clockwise from north; pydcs stores
            # ordinary clockwise headings.
            heading = round((-math.degrees(runway["course"])) % 360)
            self.runways.append(
                Runway(
                    id=int(runway["id"]),
                    name=f"{main}-{opposite}",
                    main=RunwayApproach(name=main, heading=heading, beacons=[]),
                    opposite=RunwayApproach(
                        name=opposite, heading=(heading + 180) % 360, beacons=[]
                    ),
                )
            )

        for stand in data.get("stands", []):
            params = stand["params"]
            flags = int(stand["flag"])
            height = params["HEIGHT"]
            self.parking_slots.append(
                ParkingSlot(
                    crossroad_idx=int(stand["crossroad_index"]),
                    position=mapping.Point(stand["x"], stand["y"], terrain),
                    large=bool(flags & (1 << 3)),
                    heli=params["FOR_HELICOPTERS"] == "1",
                    airplanes=params["FOR_AIRPLANES"] == "1",
                    slot_name=stand["name"],
                    length=float(params["LENGTH"]),
                    width=float(params["WIDTH"]),
                    height=float(height) if height else None,
                    shelter=params["SHELTER"] == "1",
                )
            )


def all_airports(terrain: Terrain) -> Iterator[AfghanistanAirport]:
    """Construct each usable DCS Afghanistan airfield exactly once.

    The export includes a duplicate FOB Salerno record and three editor-only
    FOB placeholders with no position, runway, or stands.  They cannot be
    represented as pydcs airports, so deliberately exclude them.
    """
    seen_ids: set[int] = set()
    for data in json.loads(_DATA_FILE.read_text(encoding="utf-8")):
        airport_id = int(data["ID"])
        if airport_id in seen_ids or not data.get("stands"):
            continue
        seen_ids.add(airport_id)
        yield AfghanistanAirport(data, terrain)
