import argparse
import sys
import os
import random

import dcs


def main():
    red = [
        (dcs.countries.Germany.name, dcs.countries.Germany.Plane.Bf_109K_4.id),
        (dcs.countries.Germany.name, dcs.countries.Germany.Plane.FW_190D9.id),
    ]

    blue = [
        (dcs.countries.USA.name, dcs.countries.USA.Plane.P_51D.id)
    ]

    types = red + blue

    aircraft_types = [x[1] for x in types]

    parser = argparse.ArgumentParser(description="DCS WWII dogfight generator")
    parser.add_argument("-a", "--aircrafttype", default=dcs.planes.Bf_109K_4.id,
                        choices=aircraft_types,
                        help="Player aircraft type")
    parser.add_argument("-p", "--playercount", default=1, type=int)
    parser.add_argument("-n", "--numberplanes", default=16, type=int, help="Count of planes per side")
    parser.add_argument("-t", "--terrain", choices=["caucasus", "nevada"], default='caucasus')
    parser.add_argument("-s", "--skill", choices=[x.value for x in dcs.unit.Skill], default=dcs.unit.Skill.Average.value)
    parser.add_argument("-o", "--output", help="Name and path of the generated mission", default=None)

    args = parser.parse_args()
    terrain_map = {
        "caucasus": dcs.terrain.Caucasus,
        "nevada": dcs.terrain.Nevada
    }

    if args.output is None:
        if args.terrain == "caucasus":
            args.output = os.path.join(os.path.expanduser("~"), "Saved Games\\DCS\\Missions\\dogfight_wwii.miz")
        else:
            args.output = os.path.join(os.path.expanduser("~"), "Saved Games\\DCS.openalpha\\Missions\\dogfight_wwii.miz")

    m = dcs.Mission(terrain_map[args.terrain]())

    m.coalition["blue"].swap_country(m.coalition["red"], dcs.countries.Germany.name)

    # pick a random airport as fight reference
    airport = random.choice(list(m.terrain.airport_list()))
    battle_point = dcs.Rectangle.from_point(airport.position, 40 * 1000).random_point()
    heading = random.randrange(0, 360)

    # set editor mapview
    m.map.position = battle_point
    m.map.zoom = 100000

    # fight altitude
    altitude = random.randrange(2000, 6000, 100)

    if args.playercount == 1:
        player_country = m.country([x[0] for x in types if x[1] == args.aircrafttype][0])
        hdg = heading + 180 if m.is_blue(player_country) else heading
        fg = m.flight_group_inflight(player_country, "Player " + args.aircrafttype,
                                     dcs.planes.plane_map[args.aircrafttype],
                                     position=battle_point.point_from_heading(hdg, 10 * 800),
                                     altitude=altitude, speed=500, maintask=dcs.task.Intercept)
        fg.add_waypoint(battle_point, altitude=altitude)
        fg.units[0].set_player()
    else:
        for x in types:
            country = m.country(x[0])
            hdg = heading + 180 if m.is_blue(country) else heading
            pos = battle_point.point_from_heading(hdg, 10 * 800)
            pos = pos.point_from_heading(hdg + 90, random.randrange(-5000, 5000, 100))
            fg = m.flight_group_inflight(country, x[1] + " group",
                                         dcs.planes.plane_map[x[1]],
                                         position=pos, altitude=random.randrange(altitude - 200, altitude + 200),
                                         speed=500,
                                         maintask=dcs.task.FighterSweep,
                                         group_size=args.playercount)
            fg.set_client()
            fg.add_waypoint(battle_point, altitude=altitude)

    # spawn AI
    group_count = int(args.numberplanes / 4)
    last_group_size = args.numberplanes % 4

    for c in [red, blue]:
        gc = 1
        for x in range(0, group_count):
            planetype = random.choice(c)
            country = m.country(planetype[0])
            hdg = heading + 180 if m.is_blue(country) else heading
            pos = battle_point.point_from_heading(hdg, 10 * 800)
            pos = pos.point_from_heading(hdg + 90, random.randrange(-5000, 5000, 100))
            fg = m.flight_group_inflight(country, planetype[0] + " " + planetype[1] + " #" + str(gc),
                                         dcs.planes.plane_map[planetype[1]],
                                         position=pos, altitude=random.randrange(altitude - 400, altitude + 400, 50),
                                         speed=500,
                                         maintask=dcs.task.FighterSweep,
                                         group_size=4)
            fg.set_skill(dcs.unit.Skill(args.skill))
            fg.add_waypoint(battle_point, altitude=altitude)
            gc += 1

        if last_group_size:
            planetype = random.choice(c)
            country = m.country(planetype[0])
            hdg = heading + 180 if m.is_blue(country) else heading
            pos = battle_point.point_from_heading(hdg, 10 * 800)
            pos = pos.point_from_heading(hdg + 90, random.randrange(-5000, 5000, 100))
            fg = m.flight_group_inflight(m.country(planetype[0]), planetype[0] + " " + planetype[1] + " #" + str(gc),
                                         dcs.planes.plane_map[planetype[1]],
                                         position=pos, altitude=random.randrange(altitude - 400, altitude + 400, 50),
                                         speed=500,
                                         maintask=dcs.task.FighterSweep,
                                         group_size=last_group_size)
            fg.set_skill(dcs.unit.Skill(args.skill))
            fg.add_waypoint(battle_point, altitude=altitude)

    m.set_sortie_text("WWII dogfight")
    stats = m.stats()
    m.set_description_text("""A WWII dogfight encounter
There are {pc} planes in the air battling for life and death.""".format(
        pc=stats["red"]["plane_groups"]["unit_count"] + stats["blue"]["plane_groups"]["unit_count"]))
    m.set_description_redtask_text("Fight the other planes!")
    m.set_description_bluetask_text("Fight the other planes!")

    m.save(args.output)

    print("Mission created: " + args.output)
    return 0


if __name__ == '__main__':
    sys.exit(main())
