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

    .\tools\airport_import.py C:\standlist.lua

That will generate the Python code for the map to stdout. Copy paste into the
appropriate terrain Python file.

See https://github.com/pydcs/dcs/issues/36
"""

import argparse
import codecs

import dcs.lua
from dcs.atcradio import AtcRadio


def safename(name):
    return name.replace(' ', '_').replace('-', '_')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("airportinfofile")

    args = parser.parse_args()

    with codecs.open(args.airportinfofile, "r", "utf-8") as f:
        data = dcs.lua.loads(f.read())

        for id_ in sorted(data["airports"]):
            airport = data["airports"][id_]
            tacan = airport.get("tacan", None)
            tacan = '"' + tacan + '"' if tacan else None
            sname = safename(airport['airport']['display_name'])
            name = airport['airport']['display_name']
            civ = airport["airport"].get("civilian", True)
            x = airport["airport"]["reference_point"]["x"]
            y = airport["airport"]["reference_point"]["y"]

            atc_freqs = list(airport["frequencies"]["frequencyList"].values())
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

            print(f"""

class {sname}(Airport):
    id = {id_}
    name = "{name}"
    tacan = {tacan}
    unit_zones = []
    civilian = {civ}
    slot_version = 2
    atc_radio = {repr(atc_radio)}

    def __init__(self, terrain: Terrain) -> None:
        super().__init__(mapping.Point({x}, {y}, terrain), terrain)
""")

            i = 0
            for runway in airport['airport']["runwayName"]:
                i += 1
                if not i % 2:
                    continue  # pydcs code only needs one direction runway
                runway = airport['airport']["runwayName"][runway]
                hdg = int(runway) * 10 if runway[-1].isdigit() else int(runway[:-1]) * 10
                print("        self.runways.append(Runway({hdg}))".format(hdg=hdg))

            for standid in sorted(airport["standlist"]):
                slot = airport["standlist"][standid]
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
                ))

        print()
        print("# The following section belongs in the Terrain subclass, not in the Airport")
        print()

        for id_ in sorted(data["airports"]):
            airport = data["airports"][id_]
            sname = safename(airport['airport']['display_name'])
            keyname = airport['airport']['display_name']
            print("        self.airports['{keyname}'] = {name}(self)".format(keyname=keyname, name=sname))

        for id_ in sorted(data["airports"]):
            airport = data["airports"][id_]
            sname = safename(airport['airport']['display_name']).lower()
            keyname = airport['airport']['display_name']
            print("""
    def {name}(self) -> Airport:
        return self.airports["{keyname}"]""".format(keyname=keyname, name=sname))


if __name__ == "__main__":
    main()
