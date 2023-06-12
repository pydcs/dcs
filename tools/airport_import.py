"""
This script imports airport data, that was previously exported by a lua function.

Copy the following lua function into me_map_window.lua and call the function in the
createAircraft() function. Then open DCS, create a new mission in the editor for the map
you want to export, and place an aircraft (any aircraft will do, the code will run when
the aircraft is placed).

function dumpairportdata()
    local S	= require('Serializer')
    local airdromedump = {}
    for k, v in base.pairs(base.MapWindow.listAirdromes) do
        --MapWindow.listAirdromes[unit.boss.route.points[1].airdromeId].roadnet
        local sList = Terrain.getStandList(v.roadnet, {"SHELTER","FOR_HELICOPTERS","FOR_AIRPLANES","WIDTH","LENGTH","HEIGHT"})
        info = {}
        info["airport"] = v
        info["standlist"] = sList
        info["frequencies"] = AirdromeData.getAirdrome(AirdromeData.getAirdromeId(k))
        airdromedump[k] = info
    end
    local f = base.io.open("C:\\standlist.lua", 'w')
    if f then
            local s = S.new(f)
            s:serialize_simple2('airports', airdromedump)
            f:close()
    else
        showWarningMessageBox(_('Error saving standlist'))
    end
end

If you are unable to place aircraft in the ME (clicking does nothing), there is probably
something wrong with the script. Check the DCS log for info.

Once you've done that, C:\standlist.lua will have been written. Run the following to
generate the data for pydcs:

    .\tools\airport_import.py -t $TERRAIN_NAME C:\standlist.lua

This will generate the airport list to the source directory.

See https://github.com/pydcs/dcs/issues/36
"""

import argparse
import codecs
from collections import defaultdict
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple

import dcs.lua
from dcs.atcradio import AtcRadio
from dcs.beacons import AirportBeacon, RunwayBeacon
from dcs.terrain.terrain import Runway, RunwayBeaconMapping


THIS_DIR = Path(__file__).parent.resolve()
TERRAINS_DIR = THIS_DIR.parent / "dcs/terrain"


def safename(name: str) -> str:
    return name.replace(' ', '_').replace('-', '_').replace('.', '_').replace("'", '_')


def parse_beacons(
    each_beacon: Iterable[Dict[str, Any]]
) -> Tuple[List[AirportBeacon], RunwayBeaconMapping]:
    airport_beacons = []
    runway_beacons: RunwayBeaconMapping = defaultdict(lambda: defaultdict(list))
    for data in each_beacon:
        # Example data:
        #
        # {
        #     ["runwayName"] = "04-22",
        #     ["runwayId"] = 1,
        #     ["runwaySide"] = "22",
        #     ["beaconId"] = "airfield12_1",
        # }
        #
        # Some beacons have only a beaconId.
        if "runwayId" in data:
            beacon = RunwayBeacon.from_lua(data)
            # -1 shows up for some runway IDs in the runways section. I assume those
            # will never have beacons. If this assertion fails, we may need to fall back
            # to name indexing.
            assert beacon.runway_id != -1
            runway_beacons[beacon.runway_id][beacon.runway_side].append(beacon)
        else:
            airport_beacons.append(AirportBeacon.from_lua(data))
    return airport_beacons, runway_beacons


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terrain", required=True, help="Name of the terrain.")
    parser.add_argument("airportinfofile")

    args = parser.parse_args()

    with codecs.open(args.airportinfofile, "r", "utf-8") as f:
        data = dcs.lua.loads(f.read())

    output_path = TERRAINS_DIR / args.terrain.lower() / "airports.py"
    with output_path.open("w") as output:
        print("# flake8: noqa", file=output)
        print("from typing import List, Type", file=output)
        print(file=output)
        print("from dcs import mapping", file=output)
        print("from dcs.atcradio import AtcRadio", file=output)
        print("from dcs.beacons import AirportBeacon, RunwayBeacon", file=output)
        print("from dcs.terrain import Airport, ParkingSlot, Runway, RunwayApproach, Terrain", file=output)

        airport_class_names: list[str] = []
        for id_ in sorted(data["airports"]):
            airport = data["airports"][id_]
            name = airport['airport']['display_name']
            
            tacan = airport.get("tacan", None)
            tacan = '"' + tacan + '"' if tacan else None
            sname = safename(airport['airport']['display_name'])
            civ = airport["airport"].get("civilian", True)
            x = airport["airport"]["reference_point"]["x"]
            y = airport["airport"]["reference_point"]["y"]

            atc_freqs = [v[1] for v in airport["frequencies"]["frequencyList"].values()]
            if atc_freqs:
                hf, vhf_low, vhf_high, uhf = sorted(atc_freqs)
                atc_radio = AtcRadio(
                    hf_hz=hf,
                    vhf_low_hz=vhf_low,
                    vhf_high_hz=vhf_high,
                    uhf_hz=uhf,
                )
            else:
                atc_radio = None

            airport_class_names.append(sname)

            airport_beacons, runway_beacons = parse_beacons(
                airport["airport"]["beacons"].values()
            )
            # The default runway value is, as far as I can tell, only needed for a
            # single airport in the game: CaletaTortel on the Falklands map. Other
            # airports in the game that have no runways include an empty list of
            # runways, but for CaletaTortel the field is absent. The airport has other
            # quirks. It appears to be farther north than the northern extent of the
            # map. This might be a bug in the DCS data, but the ME will use the airport
            # ID in the warehouses file of the miz, and we shouldn't be skipping errors
            # when parsing that file, so we need to at least have some record of the
            # airport even if it's probably bogus.
            runways = [Runway.from_lua(data, runway_beacons)
                       for data in airport["airport"].get("runways", {}).values()]

            # Ditto.
            standlist = airport.get("standlist", {})

            print(f"""

class {sname}(Airport):
    id = {id_}
    name = "{name}"
    tacan = {tacan}
    unit_zones: List[mapping.Rectangle] = []
    civilian = {civ}
    slot_version = 2
    atc_radio = {repr(atc_radio)}

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point({x}, {y}, terrain), terrain)
""", file=output)

            for beacon in airport_beacons:
                print(f"        self.beacons.append({repr(beacon)})", file=output)
            for runway in runways:
                print(f"        self.runways.append({repr(runway)})", file=output)

            for standid in sorted(standlist):
                slot = standlist[standid]
                large_bit = 1 << 3
                large = slot["flag"] & large_bit == large_bit
                height = float(slot["params"]["HEIGHT"]) if slot["params"]["HEIGHT"] else None
                print("""        self.parking_slots.append(ParkingSlot(
                crossroad_idx={crossidx}, position=mapping.Point({x}, {y}, self._terrain), large={large}, heli={heli},
                airplanes={airplanes}, slot_name='{name}', length={length}, width={width}, height={height}, shelter={shelter}))""".format(
                    crossidx=slot["crossroad_index"], x=slot["x"], y=slot["y"],
                    large=large,
                    heli=slot["params"]["FOR_HELICOPTERS"] == "1",
                    airplanes=slot["params"]["FOR_AIRPLANES"] == "1",
                    name=slot["name"],
                    length=float(slot["params"]["LENGTH"]), width=float(slot["params"]["WIDTH"]), height=height,
                    shelter=slot["params"]["SHELTER"] == "1"
                ), file=output)

        print(file=output)
        print(file=output)
        print("ALL_AIRPORTS: List[Type[Airport]] = [", file=output)
        print("\n".join(f"    {n}," for n in airport_class_names), file=output)
        print("]", file=output)
        print(file=output)


if __name__ == "__main__":
    main()
