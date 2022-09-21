from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class AirportBeacon:
    """A beacon attached to an airport that isn't specific to a runway."""
    # The ID of the associated beacon (at time of writing, this data is not exposed in
    # pydcs).
    # Example: airfield12_0
    id: str

    @staticmethod
    def from_lua(data: Dict[str, Any]) -> AirportBeacon:
        """Parses runway beacon information from the Lua dump.

        Example data:

        {
            ["beaconId"] = "airfield12_1",
        }
        """
        return AirportBeacon(
            data["beaconId"]
        )


@dataclass(frozen=True)
class RunwayBeacon(AirportBeacon):
    """A beacon attached to a runway."""
    # The name of the runway. Probably has no semantic value, but seems to follow the
    # form {heading0}-{heading1}.
    # Example: "04-22"
    runway_name: str
    # The numeric ID of the runway for the airport. Appears to be a lua index (1-based).
    # Example: 1
    runway_id: int
    # The side of the runway that the beacon is associated with. ILS beacons, for
    # example, only point one way.
    # Example: "22"
    runway_side: str

    @staticmethod
    def from_lua(data: Dict[str, Any]) -> RunwayBeacon:
        """Parses runway beacon information from the Lua dump.

        Example data:

        {
            ["runwayName"] = "04-22",
            ["runwayId"] = 1,
            ["runwaySide"] = "22",
            ["beaconId"] = "airfield12_1",
        }
        """
        return RunwayBeacon(
            data["beaconId"],
            data["runwayName"],
            data["runwayId"],
            data["runwaySide"],
        )
