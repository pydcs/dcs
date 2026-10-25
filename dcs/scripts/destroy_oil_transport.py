import dcs
import sys
import os
import random
import argparse


def main():
    aircrafts = [x for x in dcs.planes.plane_map.values() if x.flyable]
    helicopters = [x for x in dcs.helicopters.helicopter_map.values() if x.flyable]
    aircraft_types = [x.id for x in aircrafts + helicopters]

    parser = argparse.ArgumentParser(description="DCS random search and destroy oil convoy")
    parser.add_argument("-a", "--aircrafttype", default=dcs.planes.A_10C.id,
                        choices=aircraft_types,
                        help="Player aircraft type")
    parser.add_argument("-u", "--unhide", action="store_true", default=False, help="Show enemy pre mission")
    parser.add_argument("-t", "--terrain", choices=["caucasus"], default='caucasus')
    parser.add_argument("-d", "--difficulty", choices=["easy", "normal", "hard", "ohno"], default='normal')
    parser.add_argument("-m", "--multiplayer", action="store_true", default=False)
    parser.add_argument("-s", "--stats", action="store_false", default=True)
    parser.add_argument("-o", "--output", help="Name and path of the generated mission", default=None)

    args = parser.parse_args()
    terrain_map = {
        "caucasus": dcs.terrain.Caucasus
    }
    difficulty_map = {
        'easy': 0.25,
        'normal': 0.5,
        'hard': 0.7,
        'ohno': 0.9
    }
    difficulty = difficulty_map[args.difficulty]

    terrain = terrain_map[args.terrain]()

    zone_abkhazia = dcs.Polygon(terrain, [
        dcs.Point(-187092.85714285, 460857.14285714, terrain),
        dcs.Point(-149378.57142856, 476285.71428571, terrain),
        dcs.Point(-147664.28571428, 520000, terrain),
        dcs.Point(-175378.57142856, 599714.28571429, terrain),
        dcs.Point(-174521.42857142, 644000, terrain),
        dcs.Point(-199664.28571428, 624000, terrain),
        dcs.Point(-233949.99999999, 632857.14285714, terrain),
        dcs.Point(-271092.85714285, 596000, terrain)
    ])

    destination_city = 'Adler'
    zone_enemy = zone_abkhazia

    if args.output is None:
        args.output = os.path.join(os.path.expanduser("~"), "Saved Games\\DCS\\Missions\\oil_transport.miz")
        if args.terrain == "caucasus":
            zone_enemy = zone_abkhazia
            destination_city = 'Adler'
    m = dcs.Mission(terrain)
    m.random_weather = True
    m.random_date()
    m.random_daytime('day')

    red_airports = [
        "Anapa-Vityazevo", "Krymsk", "Novorossiysk", "Krasnodar-Center", "Krasnodar-Pashkovsky",
        "Maykop-Khanskaya", "Gelendzhik", "Mineralnye Vody", "Mozdok", "Beslan", "Nalchik", "Sochi-Adler"
    ]
    for a in red_airports:
        m.terrain.airports[a].set_red()

    blue_airports = ["Batumi", "Vaziani", "Soganlug", "Kobuleti", "Senaki-Kolkhi", "Tbilisi-Lochini", "Kutaisi"]
    for b in blue_airports:
        m.terrain.airports[b].set_blue()

    senaki = m.terrain.airports["Senaki-Kolkhi"]

    city_graph = m.terrain.city_graph

    destination_node = city_graph.node(destination_city)

    # find a startnode far away enough
    start_node = random.choice(city_graph.rated_nodes_within(zone_enemy))
    while start_node.position.distance_to_point(destination_node.position) < 70000:
        start_node = random.choice(city_graph.rated_nodes_within(zone_enemy))

    # create the oil convoy
    abkhazia = m.country(dcs.countries.Abkhazia.name)
    convoy_vehicles = []
    for i in range(0, 1 + int(max(difficulty, random.random()) * 10)):
        convoy_vehicles.append(dcs.vehicles.Unarmed.ATZ_10)

    airdef = [
        dcs.countries.Abkhazia.Vehicle.AirDefence.Ural_375_ZU_23,
        dcs.countries.Abkhazia.Vehicle.AirDefence.ZSU_23_4_Shilka
    ]
    if random.random() < difficulty:
        convoy_vehicles.append(random.choice(airdef))

    oil_convoy = m.vehicle_group_platoon(
        abkhazia,
        "Oil Convoy",
        convoy_vehicles,
        start_node.position.random_point_within(50))
    oil_convoy.hidden = not args.unhide
    oil_convoy.points[0].tasks.append(dcs.task.OptDisparseUnderFire())
    oil_convoy.set_skill(dcs.unit.Skill.from_percentage(difficulty))
    oil_convoy.formation_scattered(0, 50)
    oil_convoy.add_waypoint(start_node.position, dcs.point.PointAction.OnRoad)
    _, path = city_graph.travel(oil_convoy, start_node, destination_node, 100)

    # add light air defence around and in cities on path
    aaa_def = [[dcs.countries.Abkhazia.Vehicle.AirDefence.ZU_23_Emplacement],
               [dcs.countries.Abkhazia.Vehicle.AirDefence.SA_18_Igla_manpad,
                dcs.countries.Abkhazia.Vehicle.AirDefence.SA_18_Igla_comm]]
    for city in city_graph.rated_nodes_within(zone_enemy, 50):
        use_building_pos = int(min(difficulty, random.random()) * len(city.air_defence_pos_small))
        small_aaa_pos = list(city.air_defence_pos_small)
        for i in range(0, use_building_pos):
            p = small_aaa_pos.pop(random.randrange(0, len(small_aaa_pos)))
            vg = m.vehicle_group_platoon(abkhazia,
                                         city.name + " AAA #" + str(len(small_aaa_pos)),
                                         random.choice(aaa_def),
                                         p,
                                         0)
            vg.set_skill(dcs.unit.Skill.from_percentage(difficulty))
            vg.hidden = not args.unhide
            vg.formation_scattered(random.randrange(0, 360), 15)

    aaa_def += [[dcs.countries.Abkhazia.Vehicle.AirDefence.ZSU_23_4_Shilka,
                 dcs.countries.Abkhazia.Vehicle.Armor.BRDM_2,
                 dcs.countries.Abkhazia.Vehicle.Armor.BRDM_2]]
    for node in city_graph.nodes_within(zone_enemy):
        if random.random() < (difficulty - 0.1):
            vg = m.vehicle_group_platoon(abkhazia,
                                         node.name,
                                         random.choice(aaa_def),
                                         node.position.random_point_within(100, 30),
                                         random.randrange(0, 360))
            vg.set_skill(dcs.unit.Skill.from_percentage(difficulty))
            vg.hidden = not args.unhide

    # add a buk site if difficulty is hard or higher
    if difficulty > 0.5:
        buk_node = random.choice(city_graph.rated_nodes_within(zone_enemy, 50))
        sa11 = dcs.templates.VehicleTemplate.sa11_site(
            m,
            abkhazia,
            buk_node.position.random_point_within(80, 30),
            120,
            skill=dcs.unit.Skill.from_percentage(difficulty))
        sa11.hidden = not args.unhide

    usa = m.country('USA')

    # place farp for helis
    zugdidi_ne = city_graph.node('Zugidi NE')
    farp = m.farp(usa, "FARP Zugdidi", zugdidi_ne.position + dcs.mapping.Point(0, 500, m.terrain), callsign_id=1)
    fg = m.flight_group_from_unit(
        usa, dcs.helicopters.Ka_50.id + " Client", dcs.helicopters.Ka_50, farp, dcs.task.CAS, group_size=2)
    fg.set_client()

    farp = m.farp(usa, "FARP Kvemo", zugdidi_ne.position + dcs.mapping.Point(0, -22 * 1000, m.terrain), callsign_id=2)
    fg = m.flight_group_from_unit(
        usa, dcs.helicopters.UH_1H.id + " Client", dcs.helicopters.UH_1H, farp, dcs.task.CAS, group_size=2)
    fg.set_client()

    # place player
    player_fg = None
    if args.multiplayer:
        # senaki first, the other blue airports take the client groups that no longer fit there
        client_airports = [senaki] + [m.terrain.airports[b] for b in blue_airports if b != "Senaki-Kolkhi"]
        for x in aircrafts:
            if dcs.task.CAS in x.tasks and x not in [dcs.planes.Su_33, dcs.planes.MiG_29A, dcs.planes.MiG_29S]:
                airport = next((a for a in client_airports if len(a.free_parking_slots(x)) >= 2), None)
                if airport is None:
                    continue
                country = m.country(dcs.countries.Georgia.name) if x in [dcs.planes.Su_25T, dcs.planes.Su_25] else usa
                fg = m.flight_group_from_airport(
                    country, x.id + " Client", x, airport, dcs.task.CAS, group_size=2)
                fg.add_runway_waypoint(airport)
                fg.set_client()
    else:
        aircraft_type = [x for x in aircrafts + helicopters if x.id == args.aircrafttype][0]
        player_fg = m.flight_group_from_airport(usa, "Player", aircraft_type, senaki, dcs.task.CAS)
        player_fg.add_runway_waypoint(senaki)
        player_fg.units[0].set_player()

    # CAP flight
    cap_type = random.choice([dcs.planes.F_16C_bl_52d, dcs.planes.F_A_18C, dcs.planes.F_15E])
    m.patrol_flight(usa, "CAP", cap_type, m.terrain.airports["Kutaisi"], zugdidi_ne.position,
                    zugdidi_ne.position.point_from_heading(random.randint(270, 350), 35 * 1000))

    notify_nodes = path[1:5]
    for i in range(0, int((1.3 - difficulty) * 3)):
        notifier_node = random.randrange(0, len(notify_nodes))
        notifier_node = city_graph.node(notify_nodes.pop(notifier_node))
        notify_zone = m.triggers.add_triggerzone(notifier_node.position, 300, hidden=False, name='notify_zone')
        notify_zone.hidden = True
        trig_notify = dcs.triggers.TriggerOnce(comment='NotifyConvoyPosition #' + str(i))
        trig_notify.rules.append(dcs.condition.PartOfGroupInZone(oil_convoy.id, notify_zone.id))
        trig_notify.actions.append(dcs.action.MessageToCoalition(
            dcs.action.Coalition.Blue,
            m.string('Intel just reported that the convoy just arrived at ' + notifier_node.name),
            20))
        m.triggerrules.triggers.append(trig_notify)

    trig_convoy_dead = dcs.triggers.TriggerOnce(dcs.triggers.Event.Destroy, comment='Convoy dead')
    trig_convoy_dead.rules.append(dcs.condition.GroupDead(oil_convoy.id))
    trig_convoy_dead.actions.append(dcs.action.MessageToCoalition(
        dcs.action.Coalition.Blue, m.string('Excellent job!\nIntelligence reports the convoy was destroyed!\nRTB'), 15))
    m.triggerrules.triggers.append(trig_convoy_dead)

    m.forced_options.civil_traffic = dcs.forcedoptions.ForcedOptions.CivilTraffic.Low

    g = dcs.goals.Goal("convoy destroyed", score=100)
    g.rules.append(dcs.condition.GroupDead(oil_convoy.id))
    if player_fg:
        g.rules.append(dcs.condition.GroupAlive(player_fg.id))
    m.goals.add_blue(g)
    m.goals.add_offline(g)

    m.set_sortie_text("Search and destroy the oil convoy")
    m.set_description_text("""Abkhazia is selling oil to Russia to silently finance their military investments.

US and Georgia forces decided to prevent these oil transports.""")
    m.set_description_bluetask_text("""You are tasked to search and destroy a current oil convoy.

The position of the convoy is unknown, but we have several agents in Abkhazia that will look out
for the current route of the oil convoy.
Last known position will be transmitted to you while in flight.
Keep in mind that there are man pads and several AAA air defences around cities in Abkazia that are just waiting
to shoot down an American or Georgian aircraft.

Mission objectives:
  * Find the convoy
  * Destroy the convoy
  * Head back in one piece to Senaki airport.""")

    if args.stats:
        m.print_stats(m.stats())
    m.save(args.output)

    return 0


if __name__ == '__main__':
    sys.exit(main())
