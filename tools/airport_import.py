"""
This script imports airport data, that was previously exported by a lua function.

The lua function to export is just beneath this comment block, insert it somewhere in the mission editor
and call it somewhere

See https://github.com/pydcs/dcs/issues/36
"""

"""
function dumpairportdata()
    local S	= require('Serializer')
    local airdromedump = {}
    for k, v in base.pairs(base.MapWindow.listAirdromes) do
        --MapWindow.listAirdromes[unit.boss.route.points[1].airdromeId].roadnet
        local sList = Terrain.getStandList(v.roadnet, {"SHELTER","FOR_HELICOPTERS","FOR_AIRPLANES","WIDTH","LENGTH","HEIGHT"})
        info = {}
        info["airport"] = v
        info["standlist"] = sList
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
"""

import argparse
import dcs.lua
import codecs


def safename(name):
    return name.replace(' ', '_').replace('-', '_')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terrain", choices=["caucasus", "nevada", "normandy", "persiangulf", "thechannel", "syria"], default="caucasus")
    parser.add_argument("airportinfofile")

    args = parser.parse_args()

    with codecs.open(args.airportinfofile, "r", "utf-8") as f:
        data = dcs.lua.loads(f.read())

        for id in sorted(data["airports"]):
            airport = data["airports"][id]
            tacan = None  #airports[id].get("tacan", None)
            tacan = '"' + tacan + '"' if tacan else None
            print(
"""

class {sname}(Airport):
    id = {id}
    name = "{name}"
    position = mapping.Point({x}, {y})
    tacan = {tacan}
    unit_zones = []
    civilian = {civ}
    slot_version = {slot_version}

    def __init__(self):
        super({sname}, self).__init__()
""".format(sname=safename(airport['airport']['display_name']), name=airport['airport']['display_name'], id=id, x=airport["airport"]["reference_point"]["x"],
           y=airport["airport"]["reference_point"]["y"], tacan=tacan,
#           freq=", ".join(map(str, airport["airport"]["frequency"].values())),
           civ=airport["airport"].get("civilian", True),
           slot_version=2)
            )

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
                crossroad_idx={crossidx}, position=mapping.Point({x}, {y}), large={large}, heli={heli},
                airplanes={airplanes}, slot_name='{name}', length={length}, width={width}, height={height}, shelter={shelter}))""".format(
                    crossidx=slot["crossroad_index"], x=slot["x"], y=slot["y"],
                    large=large, heli=slot["params"]["FOR_HELICOPTERS"] == "1", airplanes=slot["params"]["FOR_AIRPLANES"] == "1",
                    name=slot["name"],
                    length=float(slot["params"]["LENGTH"]), width=float(slot["params"]["WIDTH"]), height=height,
                    shelter=slot["params"]["SHELTER"] == "1"
                ))

        for id in sorted(data["airports"]):
            airport = data["airports"][id]
            sname = safename(airport['airport']['display_name'])
            keyname = airport['airport']['display_name']
            print("self.airports['{keyname}'] = {name}()".format(keyname=keyname, name=sname))

        for id in sorted(data["airports"]):
            airport = data["airports"][id]
            sname = safename(airport['airport']['display_name']).lower()
            keyname = airport['airport']['display_name']
            print("""
    def {name}(self) -> Airport:
        return self.airports["{keyname}"]""".format(keyname=keyname, name=sname))


if __name__ == "__main__":
    main()
