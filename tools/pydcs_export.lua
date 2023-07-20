-- execute(dofile) this script at the end of
-- of 'DCS World\MissionEditor\modules\me_mission.lua'
-- base.dofile("C:\\Users\\peint\\Documents\\dcs\\tools\\pydcs_export.lua")

-------------------------------------------------------------------------------
-- settings
-------------------------------------------------------------------------------

-- edit export_path to your export folder
local base_path = "D:\\Work\\DCS\\dcs\\dcs\\"
local export_path = base_path .. "dcs\\"

local log_file = io.open(base_path.."export.log", "w")

-------------------------------------------------------------------------------
-- helper functions
-------------------------------------------------------------------------------
local function writeln(file, text)
    file:write(text.."\r\n")
end

local function debugln(fmt, ...)
    local msg = string.format(fmt, unpack(arg))
    writeln(log_file, msg)
end

-- https://stackoverflow.com/a/27028488/632035
local function dump(o)
    if type(o) == 'table' then
       local s = '{ '
       for k,v in pairs(o) do
          if type(k) ~= 'number' then k = '"'..k..'"' end
          s = s .. '['..k..'] = ' .. dump(v) .. ','
       end
       return s .. '} '
    else
       return tostring(o)
    end
 end

local function safe_name(name)
    local safeName = name
    safeName = string.gsub(safeName, "[-()/., *'+`#%[%]]", "_")
    safeName = string.gsub(safeName, "_*$", "")  -- strip __ from end
    safeName = string.gsub(safeName, "^([0-9])", "x_%1")
    safeName = string.gsub(safeName, '%"', '') -- Remove the " character (Example unit using it : AA gun QF 3,7")
    safeName = string.gsub(safeName, "%&", "")  -- Remove the '&' sign
    if safeName == 'None' then
        safeName = 'None_'
    end
    return safeName
end

local function safe_class_name(name)
    return safe_name(name):gsub("^%l", string.upper)
end

local function safe_display_name(name)
    local safeDisplayName = name
    safeDisplayName = string.gsub(safeDisplayName, '%"', '\\"')
    return safeDisplayName
end

local function remove_semi_colons(name)
    return string.gsub(name, ";", "_")
end

local function has_value (tab, val)
    for index, value in ipairs(tab) do
        if value == val then
            return true
        end
    end

    return false
end

function ternary ( cond , T , F )
    if cond then return T else return F end
end

local function handle_weapon(weapon, weaponKeys, weaponTable)
    if weapon.displayName == nil then
        -- There appears to be some garbage data in the weapon table where there are weapons without display names. Based on
        -- the CLSIDs, these are some duplicate copies of Hydras. Since they don't appear to be needed, and we have no names to
        -- display for them, just skip them.
        debugln("Could not process weapon %s because it does not have a displayName: %s", weapon.CLSID, dump(weapon))
        return
    end

    local pyName = weapon.displayName
    local myclsid = weapon.CLSID
    if string.sub(weapon.CLSID, 0, 1) ~= "{" then
        pyName = weapon.CLSID
    end

    -- this is all special code because, ED has for no reason some non utf8/ascii chars in their ids
    if weapon.displayName == "AT-4 SPIGOT" then
        pyName = "_9M111"
        myclsid = pyName
    elseif weapon.displayName == "AT-10 SABBER" then
        pyName = "_9M117"
        myclsid = pyName
    elseif weapon.displayName == "AT-11 SNIPER (Reflex)" then
        pyName = "REFLEX_9M119"
        myclsid = pyName
    elseif weapon.displayName == "AT-11 SNIPER (Svir')" then
        pyName = "SVIR_9M119"
        myclsid = pyName
    elseif weapon.displayName == "SA-13 GOPHER" then
        pyName = "_9M37"
        myclsid = pyName
    elseif weapon.displayName == "SA-15 GAUNTLET" then
        pyName = "_9M331"
        myclsid = pyName
    elseif weapon.displayName == "SA-11 GADFLY" then
        pyName = "_9M38"
        myclsid = pyName
    elseif weapon.displayName == "SA-18 GROUSE" then
        pyName = "_9M39"
        myclsid = pyName
    elseif weapon.displayName == "SS-N-12 SANDBOX" then
        pyName = "_4M80"
        myclsid = pyName
    elseif weapon.displayName == 'AN/AAS-38 "Nite hawk" FLIR, Laser designator & Laser spot tracker pod' then
        pyName = "_NiteHawk_FLIR"
        myclsid = pyName
    else
        pyName = string.gsub(pyName, "[-()\\/., *']", "_")
        pyName = string.gsub(pyName,"^([0-9])", "_%1")
        pyName = string.gsub(pyName,"%&", "")
        pyName = string.gsub(pyName,'%"', "")
        pyName = string.gsub(pyName,'%+', "")
        pyName = string.gsub(pyName,'%:', "")
    end

    key = pyName
    if weaponTable[key] ~= nil then
        key = pyName .. "_"
    end
    local w = "None"
    if weapon["Weight"] ~= nil then
        w = weapon["Weight"]
    end
    while weaponTable[key] ~= nil do
        key = key..'_'
    end
    weaponTable[key] = {clsid = myclsid, displayName = safe_display_name(weapon.displayName), weight = w}
    table.insert(weaponKeys, key)
    -- print("    " .. key .. " = {\"clsid\": \"" .. weapon.CLSID .. "\", \"name\": \"" .. weapon.displayName .. "\"}")
end

-------------------------------------------------------------------------------
-- prepare and export weapons data
-------------------------------------------------------------------------------

local weapons = {}
local keys = {}
-- The categories are not enumerated anywhere visible, but uses can be found in various lua files in the CoreMods directory.
-- At time of writing this list only omits the CAT_SHELLS and CAT_CLUSTER_DESC categories. CAT_SHELLS we probably don't need,
-- but CAT_CLUSTER_DESC doesn't have a Launchers entry. It's not clear if we need that category or not.
-- See https://github.com/pydcs/dcs/issues/227 for debugging help.
-- TODO: Figure out why we can't include CAT_CLUSTER_DESC.
for _, category in ipairs({CAT_BOMBS,CAT_MISSILES,CAT_ROCKETS,CAT_AIR_TO_AIR,CAT_FUEL_TANKS,CAT_PODS,CAT_TORPEDOES}) do
    for i, v in ipairs(db.Weapons.Categories[category].Launchers) do
        handle_weapon(v, keys, weapons)
	end
end

table.sort( keys )

local weapons_map = {}
local i = 1
while i <= #keys do
    local x = keys[i]
    weapons_map[weapons[x].clsid] = remove_semi_colons(x)
    i = i + 1
end

file = io.open(export_path.."weapons_data.py", "w")
file:write([[# This file is generated from pydcs_export.lua


class Weapons:
]])
local i = 1
while i <= #keys do
    local x = keys[i]

    if weapons[x].displayName ~= nil then
        writeln(file, "    " .. remove_semi_colons(x) .. " = {\"clsid\": \"" .. weapons[x].clsid
                .. "\", \"name\": \"" .. weapons[x].displayName .. "\", \"weight\": " .. weapons[x].weight .. "}")
    end
    i = i + 1
end

writeln(file, '')
writeln(file, "weapon_ids = {")
i = 1
while i <= #keys do
    local x = keys[i]
    local s = "    \"" .. weapons[x].clsid .. "\": Weapons." .. remove_semi_colons(x)
    i = i + 1
    if i <= #keys then
        s = s .. ","
    end
    writeln(file, s)
end
writeln(file, "}")
file:close()


-------------------------------------------------------------------------------
-- aircraft export planes and helicopters
-------------------------------------------------------------------------------
local flyable = {}
-- Jet engine
flyable["A-10A"] = true
flyable["A-10C"] = true
flyable["A-10C_2"] = true
flyable["AJS37"] = true
flyable["AV8BNA"] = true
flyable["C-101CC"] = true
flyable["C-101EB"] = true
flyable["F-14A-135-GR"] = true
flyable["F-14B"] = true
flyable["F-15C"] = true
flyable["F-16C_50"] = true
flyable["FA-18C_hornet"] = true
flyable["F-5E-3"] = true
flyable["F-86F Sabre"] = true
flyable["Hawk"] = true
flyable["JF-17"] = true
flyable["L-39C"] = true
flyable["L-39ZA"] = true
flyable["M-2000C"] = true
flyable["MB-339A"] = true
flyable["MB-339APAN"] = true
flyable["MiG-15bis"] = true
flyable["MiG-19P"] = true
flyable["MiG-21Bis"] = true
flyable["MiG-29A"] = true
flyable["MiG-29S"] = true
flyable["Mirage-F1CE"] = true
flyable["Su-25"] = true
flyable["Su-25T"] = true
flyable["Su-27"] = true
flyable["Su-33"] = true

-- Piston engine
flyable["Bf-109K-4"] = true
flyable["Christen Eagle II"] = true
flyable["FW-190A8"] = true
flyable["FW-190D9"] = true
flyable["I-16"] = true
flyable["MosquitoFBMkVI"] = true
flyable["P-51D"] = true
flyable["P-51D-30-NA"] = true
flyable["P-47D-30"] = true
flyable["P-47D-30bl1"] = true
flyable["P-47D-40"] = true
flyable["SpitfireLFMkIX"] = true
flyable["SpitfireLFMkIXCW"] = true
flyable["TF-51D"] = true
flyable["Yak-52"] = true

-- Helicopters
flyable["AH-64D_BLK_II"] = true
flyable["Ka-50"] = true
flyable["Ka-50_3"] = true
flyable["Mi-8MT"] = true
flyable["Mi-24P"] = true
flyable["SA342L"] = true
flyable["SA342M"] = true
flyable["SA342Minigun"] = true
flyable["SA342Mistral"] = true
flyable["UH-1H"] = true


local function export_aircraft(file, aircrafts, export_type, exportplane)
    -- generate export output
    file:write(
[[# This file is generated from pydcs_export.lua
from typing import Any, Dict, List, Set

from dcs.weapons_data import Weapons
import dcs.task as task
from dcs.unitpropertydescription import UnitPropertyDescription
from dcs.unittype import FlyingType


]])
    writeln(file, 'class '..export_type..'Type(FlyingType):')
    if exportplane then
        writeln(file, '    pass')
    else
        writeln(file, '    helicopter = True')
    end
    writeln(file, '')
    writeln(file, '')

    for i in pairs(aircrafts) do
        local plane = aircrafts[i];
        local safename = safe_name(plane.type)
        writeln(file, "class "..safename.."("..export_type.."Type):")
        writeln(file, '    id = "'..plane.type..'"')
        if plane.HumanCockpit or flyable[plane.type] ~= nil then
            writeln(file, '    flyable = True')
        end
        if plane.singleInFlight then
            writeln(file, '    group_size_max = 1')
        end
        if plane.bigParkingRamp then
            writeln(file, '    large_parking_slot = True')
        end
        writeln(file, '    height = '..plane.height)
        if exportplane then
            writeln(file, '    width = '..plane.wing_span or plane.rotor_diameter)
        else
            writeln(file, '    width = '..plane.rotor_diameter)
        end
        writeln(file, '    length = '..plane.length)
        writeln(file, '    fuel_max = '..plane.MaxFuelWeight)
        writeln(file, '    max_speed = '..plane.MaxSpeed)
        --writeln(file, '    ammo_type = '..plane.MaxFuelWeight)
        --writeln(file, '    gun_max = '..)
        if plane.passivCounterm then
            writeln(file, '    chaff = '..plane.passivCounterm.chaff.default)
            writeln(file, '    flare = '..plane.passivCounterm.flare.default)
            writeln(file, '    charge_total = '..plane.passivCounterm.SingleChargeTotal)
            writeln(file, '    chaff_charge_size = '..plane.passivCounterm.chaff.chargeSz)
            writeln(file, '    flare_charge_size = '..plane.passivCounterm.flare.chargeSz)
        end

        if plane.TACAN then
            writeln(file, '    tacan = True')
        end

        if plane.EPLRS then
            writeln(file, '    eplrs = True')
        end

        if plane.Categories and plane.Categories[1] then
            local clsid = plane.Categories[1]
            if plane.Categories[1].CLSID then
                clsid = plane.Categories[1].CLSID
            end
            local s = '    category = "'
            if clsid == "{D2BC159C-5B7D-40cf-92CD-44DF3E99FAA9}" then
                s = s..'AWACS'
            elseif clsid == "{8A302789-A55D-4897-B647-66493FA6826F}" then
                s = s..'Tankers'
            elseif clsid == "{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}" then
                s = s..'Interceptor'
            else
                s = s..'Air'
            end
            writeln(file, s..'"  #'..clsid)  -- category
        end

        -- panel radio
        if plane.HumanRadio then
            local bwritefreq = false
            if exportplane and plane.HumanRadio.frequency ~= 251 then
                bwritefreq = true
            end
            if not exportplane and plane.HumanRadio.frequency ~= 127.5 then
                bwritefreq = true
            end
            if bwritefreq and plane.HumanRadio.frequency ~= nil then
                writeln(file, '    radio_frequency = '..plane.HumanRadio.frequency)
            end
            -- modulation seems always to be nil
            -- if plane.HumanRadio.modulation ~= nil then
            --     writeln(file, '    radio_modulation = '..plane.HumanRadio.modulation)
            -- end
        end
        if plane.panelRadio then
            writeln(file, '')
            writeln(file, '    panel_radio = {')
            for j in pairs(plane.panelRadio) do
                cnt = 0
                writeln(file, '        '..j..': {')
                writeln(file, '            "channels": {')
                for c in pairs(plane.panelRadio[j]["channels"]) do
                    channel = plane.panelRadio[j]["channels"][c]
                    local s = '                '..c..': '..channel.default
                    if cnt + 1 < #plane.panelRadio[j]["channels"] then
                        s = s..','
                    end
                    writeln(file, s)
                    cnt = cnt + 1
                end
                writeln(file, '            },')
                writeln(file, '        },')
            end
            writeln(file, '    }')
        end

        if plane.SpecificCallnames then
            writeln(file, '')
            writeln(file, '    callnames: Dict[str, List[str]] = {')
            for c in pairs(plane.SpecificCallnames) do
                writeln(file, '        "'..country.by_country[c].Name..'": [')
                for n in pairs(plane.SpecificCallnames[c]) do
                    writeln(file, '            "'..plane.SpecificCallnames[c][n][1]..'",')
                end
                writeln(file, '        ]')
            end
            writeln(file, '    }')
        end

        -- Old properties API. Only queryable via reflection and has less data.
        -- TODO: Remove this at some point.

        if plane.AddPropAircraft then
            writeln(file, '')
            -- default dict
            writeln(file, '    property_defaults: Dict[str, Any] = {')
            local skip_props = {}
            for j in pairs(plane.AddPropAircraft) do
                local prop = plane.AddPropAircraft[j]
                local defval = prop.defValue
                -- A nil default value is used by DCS to implement labels in the ME. These aren't real options, so skip them.
                -- https://github.com/pydcs/dcs/issues/266
                if defval == nil then
                    skip_props[prop.id] = true
                else
                    if defval == true then
                        defval = 'True'
                    elseif defval == false then
                        defval = 'False'
                    elseif type(defval) == 'string' then
                        defval = '"'..defval..'"'
                    else
                        defval = tostring(defval)
                    end
                    writeln(file, '        "'..safe_name(prop.id)..'": '..defval..',')
                end
            end
            writeln(file, '    }')

            if plane.AddPropAircraft ~= nil and #plane.AddPropAircraft > 0 then
                writeln(file, '')
                writeln(file, '    class Properties:')
                for j in pairs(plane.AddPropAircraft) do
                    local prop = plane.AddPropAircraft[j]
                    prop_class_name = safe_name(prop.id)
                    if not skip_props[prop_class_name] then
                        writeln(file, '')
                        writeln(file, '        class '..prop_class_name..':')
                        writeln(file, '            id = "'..prop.id..'"')
                        if prop.values then
                            writeln(file, '')
                            writeln(file, '            class Values:')
                            for k, val in pairs(prop.values) do
                                if type(val.id) == 'string' then
                                    writeln(file, '                '..safe_name(val.dispName)..' = "'..tostring(val.id)..'"')
                                else
                                    writeln(file, '                '..safe_name(val.dispName)..' = '..tostring(val.id))
								end
                            end
                        end
                    end
                end
            end

            -- New API that has more data and is usable without reflection.

            function format_lua_value(v)
                -- https://www.lua.org/pil/2.html
                -- There are eight basic types in Lua: nil, boolean, number, string,
                -- userdata, function, thread, and table.
                --
                -- For property values, we only need to worry about:
                --
                -- * boolean
                -- * number
                -- * string
                if type(v) == 'boolean' then
                    if v then
                        return 'True'
                    else
                        return 'False'
                    end
                elseif type(v) == 'string' then
                    return '"'..v..'"'
                else
                    return tostring(v)
                end
            end

            -- The order of the elements of the list are the order the
            -- controls are presented in the UI, so ipairs must be used rather
            -- than pairs to ensure correct iteration order.
            writeln(file, '')
            writeln(file, '    properties = {')
            for prop_idx, prop in ipairs(plane.AddPropAircraft) do
                writeln(file, string.format('        "%s": UnitPropertyDescription(', prop.id))
                -- These three are defined by every property as far as I can
                -- tell, even the fake label "properties" (which are a hack
                -- to insert a label into the UI between other properties).
                writeln(file, string.format('            identifier="%s",', prop.id))
                writeln(file, string.format('            control="%s",', prop.control))

                -- The others appear to depend on the control, and some still
                -- are optional for each control type. Some of them (e.g.
                -- dimension) don't have a clear purpose.
                if prop.label ~= nil then
                    writeln(file, string.format('            label="%s",', prop.label))
                end
                if prop.playerOnly ~= nil then
                    writeln(file, string.format('            player_only=%s,', format_lua_value(prop.playerOnly)))
                end
                if prop.min ~= nil then
                    writeln(file, string.format('            minimum=%d,', prop.min))
                end
                if prop.max ~= nil then
                    writeln(file, string.format('            maximum=%d,', prop.max))
                end
                if prop.defValue ~= nil then
                    writeln(file, string.format('            default=%s,', format_lua_value(prop.defValue)))
                end
                if prop.weightWhenOn ~= nil then
                    writeln(file, string.format('            weight_when_on=%s,', format_lua_value(prop.weightWhenOn)))
                end
                if prop.dimension ~= nil then
                    writeln(file, string.format('            dimension="%s",', prop.dimension))
                end
                if prop.xLbl ~= nil then
                    writeln(file, string.format('            x_lbl=%d,', prop.xLbl))
                end
                if prop.wCtrl ~= nil then
                    writeln(file, string.format('            w_ctrl=%d,', prop.wCtrl))
                end
                if prop.values ~= nil then
                    -- Only valid for comboList.
                    writeln(file, '            values={')
                    for value_idx, value_desc in ipairs(prop.values) do
                        writeln(file, string.format('                %s: "%s",', format_lua_value(value_desc.id), value_desc.dispName))
                    end
                    writeln(file, '            },')
                end
                writeln(file, '        ),')
            end
            writeln(file, '    }')
        end

        writeln(file, "")
        if plane.livery_entry ~= nil then
            local name = string.upper(plane.livery_entry)
            writeln(file, '    livery_name = "'..name..'"  # from livery_entry')
        else if plane.type ~= nil then
            local name = string.upper(string.gsub(plane.type, '/', '_'))
            writeln(file, '    livery_name = "'..name..'"  # from type')
        end end

        local pylons = {}

        for j in pairs(plane.Pylons) do
            if plane.Pylons[j].Launchers ~= nil and #plane.Pylons[j].Launchers > 0 then
                table.insert(pylons, j)
                local pylons_written = false
                for k in pairs(plane.Pylons[j].Launchers) do
                    if weapons_map[plane.Pylons[j].Launchers[k].CLSID] then
                        if not pylons_written then
                            writeln(file, "")
                            writeln(file, '    class Pylon'..j..':')
                            pylons_written = true
                        end

                        local name = weapons_map[plane.Pylons[j].Launchers[k].CLSID]
                        writeln(file, '        '..name..' = ('..j..', Weapons.'..name..')')
                    else
                        if plane.Pylons[j].Launchers[k].CLSID then
                            debugln(
                                "%s has %s assigned to a pylon but no matching weapon is known",
                                plane.type,
                                plane.Pylons[j].Launchers[k].CLSID
                            )
                            writeln(file, '#ERRR '..plane.Pylons[j].Launchers[k].CLSID)
                        end
                    end
                end
            end
        end

        writeln(file, "")
        local s = ''
        for j in pairs(pylons) do
            s = s..tostring(pylons[j])
            if j < #pylons then
                s = s..', '
            end
        end

        if s == "" then
            writeln(file, '    pylons: Set[int] = set()')
        else
            writeln(file, '    pylons: Set[int] = {'..s..'}')
        end

        -- tasks
        writeln(file, "")
        tasks = {}
        for j in pairs(plane.Tasks) do
            -- For some reason some entries in this list are null. Skip those.
            if plane.Tasks[j] ~= nil then
                local objname = string.gsub(plane.Tasks[j].Name, "[-()/., *']", "")
                table.insert(tasks, 'task.'..objname..'')
            end
        end
        writeln(file, '    tasks = ['..table.concat(tasks, ', ')..']')
        local objname = string.gsub(plane.DefaultTask.Name, "[-()/., *']", "")
        writeln(file, '    task_default = task.'..objname..'')
        -- writeln(file, safename..'.load_payloads()')
        writeln(file, "")
        writeln(file, "")
    end


    writeln(file, string.lower(export_type).."_map = {")
    for i in pairs(aircrafts) do
        local plane = aircrafts[i];
        local safename = safe_name(plane.type)
        writeln(file, '    "'..plane.type..'": '..safename..',')
    end
    writeln(file, "}")
end

local file = io.open(export_path.."planes.py", "w")
export_aircraft(file, db.Units.Planes.Plane, 'Plane', true)
file:close()

aircrafts = db.Units.Helicopters.Helicopter
local file = io.open(export_path.."helicopters.py", "w")
export_aircraft(file, db.Units.Helicopters.Helicopter, 'Helicopter', false)
file:close()


-------------------------------------------------------------------------------
-- ground units
-------------------------------------------------------------------------------
local file = io.open(export_path.."vehicles.py", "w")

file:write(
[[# This file is generated from pydcs_export.lua

import dcs.unittype as unittype
]])

-- sort by categories
local unit_categories = {}
unit_categories["Unarmed"] = {}
unit_categories["AirDefence"] = {}
unit_categories["Armor"] = {}
unit_categories["Fortification"] = {}
unit_categories["Artillery"] = {}
unit_categories["Infantry"] = {}
unit_categories["Carriage"] = {}
unit_categories["Locomotive"] = {}
unit_categories["MissilesSS"] = {}

for i in pairs(db.Units.Cars.Car) do
    local unit = db.Units.Cars.Car[i]
    if unit.category == 'Air Defence' then
        table.insert(unit_categories["AirDefence"], unit)
    else
        table.insert(unit_categories[unit.category], unit)
    end
end

for i in pairs(unit_categories) do
    writeln(file, '')
    writeln(file, '')
    writeln(file, 'class '..i..':')
    for j in pairs(unit_categories[i]) do
        local unit = unit_categories[i][j]
        local safename = safe_class_name(unit.type)
        local safeDisplayName = safe_display_name(unit.DisplayName)
        local threat_range = '0'
        if unit.ThreatRange ~= nil then
            threat_range = unit.ThreatRange
        end
        local air_weapon_dist = threat_range
        if unit.airWeaponDist then
            air_weapon_dist = unit.airWeaponDist
        end
        writeln(file, '')
        writeln(file, '    class '..safename..'(unittype.VehicleType):')
        writeln(file, '        id = "'..unit.type..'"')
        writeln(file, '        name = "'..safeDisplayName..'"')
        if unit.DetectionRange ~= nil then
            writeln(file, '        detection_range = '..unit.DetectionRange)
        else
            writeln(file, '        detection_range = 0')
        end
        writeln(file, '        threat_range = '..threat_range)
        writeln(file, '        air_weapon_dist = '..air_weapon_dist)
        if unit.EPLRS then
            writeln(file, '        eplrs = True')
        end
        --writeln(file, '        category = '..i)
    end
end

writeln(file, '')
writeln(file, "vehicle_map = {")
for i in pairs(db.Units.Cars.Car) do
    local unit = db.Units.Cars.Car[i];
    local safename = safe_class_name(unit.type)
    local cat = "AirDefence"
    if unit.category ~= "Air Defence" then
        cat = unit.category
    end
    writeln(file, '    "'..unit.type..'": '..cat..'.'..safename..',')
end
writeln(file, "}")
file:close()


-------------------------------------------------------------------------------
-- static units
-------------------------------------------------------------------------------
local file = io.open(export_path.."statics.py", "w")

file:write(
[[# This file is generated from pydcs_export.lua

import dcs.unittype as unittype
]])

local function lookup_map(file, parent, arr, b_parent)
    if b_parent == nil then
        b_parent = true
    end
    writeln(file, '')
    writeln(file, string.lower(parent).."_map = {")
    for i in pairs(arr) do
        local unit = arr[i];
        local safename = safe_class_name(unit.type)
        if b_parent then
            writeln(file, '    "'..unit.type..'": '..parent..'.'..safename..',')
        else
            writeln(file, '    "'..unit.type..'": '..safename..',')
        end
    end
    writeln(file, "}")
end

writeln(file, '')
writeln(file, '')
writeln(file, 'class Fortification:')
for i in pairs(db.Units.Fortifications.Fortification) do
    local unit = db.Units.Fortifications.Fortification[i]
    local safename = safe_class_name(unit.type)
    local safeDisplayName = safe_display_name(unit.DisplayName)
    writeln(file, '')
    writeln(file, '    class '..safename..'(unittype.StaticType):')
    writeln(file, '        id = "'..unit.type..'"')
    writeln(file, '        name = "'..safeDisplayName..'"')
    if unit.ShapeName ~= nil then
        writeln(file, '        shape_name = "'..unit.ShapeName..'"')
    else
        writeln(file, '        shape_name = None')
    end
    writeln(file, '        rate = '..unit.Rate)
    if unit.SeaObject ~= nil and unit.SeaObject then
        writeln(file, '        sea_object = True')
    end
end

lookup_map(file, "Fortification", db.Units.Fortifications.Fortification)

writeln(file, '')
writeln(file, '')
writeln(file, 'class GroundObject:')
for i in pairs(db.Units.GroundObjects.GroundObject) do
    local unit = db.Units.GroundObjects.GroundObject[i]
    local safename = safe_class_name(unit.type)
    local safeDisplayName = safe_display_name(unit.DisplayName)
    writeln(file, '')
    writeln(file, '    class '..safename..'(unittype.StaticType):')
    writeln(file, '        id = "'..unit.type..'"')
    writeln(file, '        name = "'..safeDisplayName..'"')
    writeln(file, '        category = ""')
end

lookup_map(file, "GroundObject", db.Units.GroundObjects.GroundObject)

writeln(file, '')
writeln(file, '')
writeln(file, 'class Warehouse:')
for i in pairs(db.Units.Warehouses.Warehouse) do
    local unit = db.Units.Warehouses.Warehouse[i]
    local safename = safe_class_name(unit.type)
    local safeDisplayName = safe_display_name(unit.DisplayName)
    writeln(file, '')
    writeln(file, '    class '..safename..'(unittype.StaticType):')
    writeln(file, '        id = "'..unit.type..'"')
    writeln(file, '        name = "'..safeDisplayName..'"')
    writeln(file, '        shape_name = "'..unit.ShapeName..'"')
    writeln(file, '        category = "Warehouses"')
    writeln(file, '        rate = '..unit.Rate)
    if unit.SeaObject ~= nil and unit.SeaObject then
        writeln(file, '        sea_object = True')
    end
end

lookup_map(file, "Warehouse", db.Units.Warehouses.Warehouse)

writeln(file, '')
writeln(file, '')
writeln(file, 'class Cargo:')
for i in pairs(db.Units.Cargos.Cargo) do
    local unit = db.Units.Cargos.Cargo[i]
    local safename = safe_class_name(unit.type)
    local safeDisplayName = safe_display_name(unit.DisplayName)
    writeln(file, '')
    writeln(file, '    class '..safename..'(unittype.StaticType):')
    writeln(file, '        id = "'..unit.type..'"')
    writeln(file, '        name = "'..safeDisplayName..'"')
    writeln(file, '        shape_name = "'..unit.ShapeName..'"')
    writeln(file, '        category = "Cargos"')
    writeln(file, '        rate = '..unit.Rate)
    writeln(file, '        can_cargo = True')
end

lookup_map(file, "Cargo", db.Units.Cargos.Cargo)

file:close()


-------------------------------------------------------------------------------
-- ship units
-------------------------------------------------------------------------------
local file = io.open(export_path.."ships.py", "w")

file:write(
[[# This file is generated from pydcs_export.lua

import dcs.unittype as unittype
]])

for i in pairs(db.Units.Ships.Ship) do
    local unit = db.Units.Ships.Ship[i]
    local safename = safe_class_name(unit.type)
    local safeDisplayName = safe_display_name(unit.DisplayName)
    writeln(file, '')
    writeln(file, '')
    writeln(file, 'class '..safename..'(unittype.ShipType):')
    writeln(file, '    id = "'..unit.type..'"')
    writeln(file, '    name = "'..safeDisplayName..'"')
    if unit.Plane_Num_ ~= nil then
        writeln(file, '    plane_num = '..unit.Plane_Num_)
    end
    if unit.Helicopter_Num_ ~= nil then
        writeln(file, '    helicopter_num = '..unit.Helicopter_Num_)
    end
    if unit.numParking ~= nil then
        writeln(file, '    parking = '..unit.numParking)
    end
    local air_weapon_dist = unit.ThreatRange
    if unit.airWeaponDist then
        air_weapon_dist = unit.airWeaponDist
    end
    local detection_range = ternary((unit.DetectionRange ~= nil), unit.DetectionRange, 0)
    local threat_range = ternary((unit.ThreatRange ~= nil), unit.ThreatRange, 0)
    air_weapon_dist = ternary((air_weapon_dist ~= nil), air_weapon_dist, 0)
    writeln(file, '    detection_range = '..detection_range)
    writeln(file, '    threat_range = '..threat_range)
    writeln(file, '    air_weapon_dist = '..air_weapon_dist)
    --    writeln(file, '    shape_name = "'..unit.ShapeName..'"')
    --    writeln(file, '    rate = '..unit.Rate)
end

lookup_map(file, "ship", db.Units.Ships.Ship, false)

file:close()

-------------------------------------------------------------------------------
-- export country data
-------------------------------------------------------------------------------
file = io.open(export_path.."countries.py", "w")

local categories = {
    'AWACS',
    'Tankers',
    'Air',
    'Helipad',
    'Ground Units',
    'GrassAirfield'
}

local function getUnit(arr, _type)
    for i in pairs(arr) do
        local unit = arr[i]
        if unit.type == _type then
            return unit
        end
    end
    return nil
end

writeln(file, '# This file is generated from pydcs_export.lua')
writeln(file, '')
writeln(file, 'from dcs.country import Country')
writeln(file, 'import dcs.vehicles as vehicles')
writeln(file, 'import dcs.planes as planes')
writeln(file, 'import dcs.helicopters as helicopters')
writeln(file, 'import dcs.ships as ships')
local countryPlaneIgnore = {
    "F_14A_95_GR",
    "F_16C_50",
    "F_4E_new",
    "F_5E_MAC",
    "F_86F_MAC",
    "F_86F",
    "L_39_MAC",
    "MB_339A_PAN",
    "MiG_15bis_MAC",
    "Su_30MK",
    "TF_51",
}
local countryHeliIgnore = { "Mi_24P", "Ka_50_3" }
local i = 0
while i <= country.maxIndex do
    local c = country.by_idx[i]
    if c then
        local pyName = c.Name
        pyName = string.gsub(pyName, "[-()/., *']", "")
        writeln(file, '')
        writeln(file, '')
        writeln(file, 'class '..pyName..'(Country):')
        writeln(file, '    id = '..i)
        writeln(file, '    name = "'..c.Name..'"')
        writeln(file, '    shortname = "'..c.ShortName..'"')
        writeln(file, '')

        writeln(file, '    class Vehicle:')

        -- sort country vehicles by category
        local unit_categories = {}
        unit_categories["Unarmed"] = {}
        unit_categories["AirDefence"] = {}
        unit_categories["Armor"] = {}
        unit_categories["Fortification"] = {}
        unit_categories["Artillery"] = {}
        unit_categories["Infantry"] = {}
        unit_categories["Carriage"] = {}
        unit_categories["Locomotive"] = {}
        unit_categories["MissilesSS"] = {}

        local cars = c.Units.Cars.Car
        for u in pairs(cars) do
            local unit = {}
            for i in pairs(db.Units.Cars.Car) do
                unit = db.Units.Cars.Car[i]
                if unit.type == cars[u].Name then
                    break
                end
            end

            if unit.category == 'Air Defence' then
                table.insert(unit_categories["AirDefence"], unit)
            else
                table.insert(unit_categories[unit.category], unit)
            end
        end

        for i in pairs(unit_categories) do
            if #unit_categories[i] > 0 then
                writeln(file, '')
                writeln(file, '        class '..i..':')
                for j in pairs(unit_categories[i]) do
                    local unit = unit_categories[i][j]
                    local safename = safe_class_name(unit.type)
                    local safeDisplayName = safe_display_name(unit.DisplayName)
                    writeln(file, '            '..safename..' = vehicles.'..i..'.'..safename)
                end
            end
        end

        local planes = c.Units.Planes.Plane
        if #planes > 0 then
            writeln(file, '')
            writeln(file, '    class Plane:')
            for u in pairs(planes) do
                local safeName = safe_name(planes[u].Name)
                if not has_value(countryPlaneIgnore, safeName) then
                    writeln(file, '        '..safeName..' = planes.'..safeName)
                end
            end

            writeln(file, '')
            writeln(file, '    planes = [')
            for u in pairs(planes) do
                local safeName = safe_name(planes[u].Name)
                if not has_value(countryPlaneIgnore, safeName) then
                    writeln(file, '        Plane.'..safeName..',')
                end
            end
            writeln(file, '    ]')
        end

        local helis = c.Units.Helicopters.Helicopter
        if #helis > 0 then
            writeln(file, '')
            writeln(file, '    class Helicopter:')
            for u in pairs(helis) do
                local safeName = safe_name(helis[u].Name)
                if not has_value(countryHeliIgnore, safeName) then
                    writeln(file, '        '..safeName..' = helicopters.'..safeName)
                end
            end

            writeln(file, '')
            writeln(file, '    helicopters = [')
            for u in pairs(helis) do
                local safeName = safe_name(helis[u].Name)
                if not has_value(countryHeliIgnore, safeName) then
                    writeln(file, '        Helicopter.'..safeName..',')
                end
            end
            writeln(file, '    ]')
        end

        local ships = c.Units.Ships.Ship
        if #ships > 0 then
            writeln(file, '')
            writeln(file, '    class Ship:')
            for u in pairs(ships) do
                local funit = getUnit(db.Units.Ships.Ship, ships[u].Name)
                if funit ~= nil then
                    local safeName = safe_class_name(funit.type)
                    writeln(file, '        '..safeName..' = ships.'..safeName)
                end
            end
        end

        for cat in pairs(categories) do
            local call = db.getCallnames(i, categories[cat])
            if call then
                safeName = string.gsub(categories[cat], "[-()/., *']", "")
                writeln(file, '')
                writeln(file, '    class Callsign'..safeName..':')
                for j in pairs(call) do
                    callsignSafe = safe_name(call[j].Name)
                    writeln(file, '        '..callsignSafe..' = "'..call[j].Name..'"')
                end
            end
        end

        writeln(file, '')
        writeln(file, '    callsign = {')
        for cat in pairs(categories) do
            local call = db.getCallnames(i, categories[cat])
            if call then
                safeName = string.gsub(categories[cat], "[-()/., *']", "")
                writeln(file, '        "'..safeName..'": [')
                local s = ''
                for j in pairs(call) do
                    callsignSafe = safe_name(call[j].Name)
                    s = '            Callsign'..safeName..'.'..callsignSafe
                    if j < #call then
                        s = s..','
                    end
                    writeln(file, s)
                end
                writeln(file, '        ],')
            end
        end
        writeln(file, '    }')

        writeln(file, '')
        writeln(file, '    def __init__(self):')
        local nl = '\n            '
        local params = nl..pyName..'.id,'..nl..pyName..'.name,'..nl..pyName..'.shortname'..'\n        '
        writeln(file, '        super('..pyName..', self).__init__('..params..')')
    end
    i = i + 1
end

writeln(file, '')
writeln(file, '')
writeln(file, 'country_dict = {')
i = 0
while i <= country.maxIndex do
    local c = country.by_idx[i]
    if c then
        local pyName = c.Name
        pyName = string.gsub(pyName, "[-()/., *']", "")
        writeln(file, '    '..pyName..'.id: '..pyName..',')
    end
    i = i + 1
end
writeln(file, '}')

writeln(file, '')
writeln(file, '')
writeln(file, 'countries_by_name = {')
i = 0
while i <= country.maxIndex do
    local c = country.by_idx[i]
    if c then
        local pyName = c.Name
        pyName = string.gsub(pyName, "[-()/., *']", "")
        writeln(file, '    '..pyName..'.name: '..pyName..',')
    end
    i = i + 1
end
writeln(file, '}')

writeln(file, '')
writeln(file, '')
writeln(file, 'countries_by_short_name = {')
i = 0
while i <= country.maxIndex do
    local c = country.by_idx[i]
    if c then
        local pyName = c.Name
        pyName = string.gsub(pyName, "[-()/., *']", "")
        writeln(file, '    '..pyName..'.shortname: '..pyName..',')
    end
    i = i + 1
end
writeln(file, '}')

writeln(file, [[


def get_by_id(_id: int) -> Country:
    """Returns a new country object for the given country id

    Args:
        _id: id for the country

    Returns:
        Country: a new country object
    """
    return country_dict[_id]()


def get_by_name(name: str) -> Country:
    """Returns a new country object for the given country name.

    Warning: the country names may or may not be stable. *Short* names' are
    most likely stable because they're used in livery files, but" the name
    field could potentially change at the whims of ED.

    Args:
        name: name of the country

    Returns:
        Country: a new country object
    """
    return countries_by_name[name]()


def get_by_short_name(short_name: str) -> Country:
    """Returns a new country object for the given country short name.

    Args:
        short_name: short name of the country

    Returns:
        Country: a new country object
    """
    return countries_by_short_name[short_name]()]])
file:close()
