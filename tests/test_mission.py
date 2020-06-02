import unittest
import os
import dcs


class BasicTests(unittest.TestCase):

    def setUp(self):
        os.makedirs('missions', exist_ok=True)

    def test_basic_keys(self):
        m = dcs.mission.Mission()
        d = m.dict()
        self.assertIn("version", d)
        self.assertIn("map", d)
        self.assertGreaterEqual(d["start_time"], 0)

    def test_finding(self):
        m = dcs.mission.Mission()

        usa = m.country("USA")
        caucasus = m.terrain  # type: dcs.terrain.Caucasus
        batumi = caucasus.batumi()
        self.assertIsNotNone(usa)
        pos = batumi.random_unit_zone().center()
        vg = m.vehicle_group(usa, "Tanks", dcs.countries.USA.Vehicle.Armor.MBT_M1A2_Abrams, pos)
        self.assertIsInstance(vg, dcs.unitgroup.VehicleGroup)
        pg = m.flight_group_inflight(usa, "Airgroup 1", dcs.planes.A_10C, dcs.Point(pos.x + 200, pos.y + 200), 2000)
        self.assertIsInstance(pg, dcs.unitgroup.PlaneGroup)
        pg = m.flight_group_inflight(usa, "Airgroup 2", dcs.planes.M_2000C, dcs.Point(pos.x + 200, pos.y + 200), 2000)
        self.assertIsInstance(pg, dcs.unitgroup.PlaneGroup)
        found_g = m.find_group("Tanks", "exact")
        self.assertIsInstance(found_g, dcs.unitgroup.VehicleGroup)

        found_g = m.find_group("Tank", "exact")
        self.assertIsNone(found_g)

        found_g = m.find_group("Tank", "match")
        self.assertIsInstance(found_g, dcs.unitgroup.VehicleGroup)

        found_g = m.find_group("Airgroup")
        self.assertIsNone(found_g)

        found_g = m.find_group("Airgroup", "match")
        self.assertIsInstance(found_g, dcs.unitgroup.PlaneGroup)

        found_g = m.find_group("Airgroup 1")
        self.assertIsInstance(found_g, dcs.unitgroup.PlaneGroup)
        self.assertEqual(found_g.units[0].unit_type, dcs.planes.A_10C)

    def test_basic_mission(self):
        m = dcs.mission.Mission()
        kobuleti = m.terrain.airports["Kobuleti"]
        kobuleti.set_blue()
        batumi = m.terrain.airports["Batumi"]
        batumi.set_blue()

        usa = m.coalition["blue"].country("USA")
        self.assertIsNotNone(usa)

        house = m.static_group(usa, "house", dcs.statics.Fortification.Small_house_1A,
                       batumi.unit_zones[0].random_point(), 230)
        self.assertEqual(str(house.name), "house")

        pg = m.flight_group_from_airport(usa, "Airgroup", dcs.planes.A_10C, kobuleti,
                                         start_type=dcs.mission.StartType.Warm)
        pg.units[0].set_player()

        pg.add_runway_waypoint(kobuleti)

        pg.add_runway_waypoint(batumi, batumi.runways[0], 8000)
        pg.land_at(batumi)

        awacs = m.awacs_flight(usa, "AWACS", dcs.planes.E_3A, batumi, batumi.position, race_distance=120 * 1000,
                               heading=90)
        self.assertIsNotNone(awacs)
        self.assertIsNotNone(awacs.points[0].find_task(dcs.task.AWACSTaskAction))

        soganlug = m.terrain.soganlug()
        soganlug.set_blue()
        tanker = m.refuel_flight(usa, "Tanker", dcs.planes.KC_135, None, soganlug.position, race_distance=120 * 1000,
                                 heading=270)
        self.assertIsNotNone(tanker)
        self.assertIsNotNone(tanker.points[0].find_task(dcs.task.Tanker))

        ustanks = m.vehicle_group(usa, "DefTanks", dcs.countries.USA.Vehicle.Armor.MBT_M1A2_Abrams,
                                  dcs.mapping.Point(-283177.42857144, 659188), 300, 3)
        ustanks.add_unit(m.vehicle("airdef", dcs.countries.USA.Vehicle.AirDefence.SAM_Avenger_M1097))
        ustanks.add_unit(m.vehicle("aaa", dcs.countries.USA.Vehicle.AirDefence.AAA_Vulcan_M163))
        ustanks.units[-1].skill = dcs.unit.Skill.High
        ustanks.formation(heading=310)

        heli = m.flight_group_inflight(usa, "heli", dcs.helicopters.UH_60A,
                                       dcs.mapping.Point(batumi.position.x + 1000 * 5, batumi.position.y),
                                       300, speed=150)
        heli.add_runway_waypoint(kobuleti)
        heli.land_at(kobuleti)

        apache = m.flight_group_from_airport(usa, "AirCav", dcs.helicopters.AH_64A, kobuleti, group_size=2)
        apache.load_loadout("8xAGM-114, 38xHYDRA-70 WP")
        apache.add_runway_waypoint(kobuleti)
        apache.add_waypoint(ustanks.position, 300, 200)

        senaki = m.terrain.senaki_kolkhi()
        senaki.set_red()
        russia = m.coalition["red"].country("Russia")
        bg = m.vehicle_group(russia, "Tanks", dcs.countries.Russia.Vehicle.Armor.MBT_T_90,
                             dcs.mapping.Point(-281599.97853068, 645570.27528559), 180, 4,
                             move_formation=dcs.point.PointAction.OnRoad)
        bg.add_waypoint(dcs.mapping.Point(-317423.36510278, 636737.32119577), dcs.point.PointAction.OnRoad, 50)

        mozdok = m.terrain.airports["Mozdok"]
        mozdok.set_red()
        rfighter = m.flight_group_from_airport(russia, "Migs", dcs.planes.MiG_29A, mozdok, group_size=2)
        last_wp = rfighter.add_runway_waypoint(mozdok)
        rfighter.add_waypoint(dcs.mapping.Point(last_wp.position.x - 1000 * 80, last_wp.position.y - 1000 * 150), 6000,
                              800)

        sukhumi = m.terrain.sukhumi_babushara()
        sukhumi.set_red()
        su25 = m.flight_group_from_airport(russia, "Su25 attack", dcs.planes.Su_25T, sukhumi,
                                           start_type=dcs.mission.StartType.Runway, group_size=2)
        su25.load_loadout("APU-8 Vikhr-M*2,Kh-25ML,R-73*2,SPPU-22*2,Mercury LLTV Pod,MPS-410")

        last_wp = su25.add_runway_waypoint(sukhumi)
        heading = last_wp.position.heading_between_point(ustanks.position)
        distance = last_wp.position.distance_to_point(ustanks.position)
        p = last_wp.position.point_from_heading(heading, distance - 1000)
        last_wp = su25.add_waypoint(p, 3000)
        last_wp.tasks.append(dcs.task.CAS.EnrouteTasks.EngageGroup(ustanks.id))
        last_wp = su25.add_waypoint(dcs.mapping.Point(last_wp.position.x + 1000 * 10, last_wp.position.y), 3000)
        su25.add_runway_waypoint(sukhumi)
        su25.land_at(sukhumi)

        sg = m.ship_group(russia, "TaskForce", dcs.ships.CG_1164_Moskva,
                          dcs.mapping.Point(-209571.42857143, 500728.57142858), 0)
        wp = sg.add_waypoint(dcs.mapping.Point(sg.x - 1000 * 60, sg.y + 1000 * 10))

        seapoint = batumi.unit_zones[0].random_point()
        seapoint.y -= 10 * 1000

        # carrier with aircraft
        sg = m.ship_group(usa, "CVN", dcs.countries.USA.Ship.CVN_70_Carl_Vinson, seapoint)
        m.flight_group_from_unit(usa, "F18 Carrier", dcs.planes.F_A_18C, sg, group_size=4)

        # some statics
        m.static_group(usa, "Static", dcs.statics.Fortification.Cafe, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SPlane", dcs.planes.B_1B, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SHeli", dcs.countries.USA.Helicopter.Mi_8MT, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SVehicle", dcs.countries.USA.Vehicle.Armor.IFV_LAV_25, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SShip", dcs.countries.USA.Ship.Oliver_Hazzard_Perry_class,
                       dcs.Rectangle.from_point(seapoint, 10000).random_point())

        batumi_zone = m.triggers.add_triggerzone(batumi.position, 200, False, "batumi zone")

        goal = dcs.goals.Goal("land at batumi")

        gr = dcs.condition.UnitInZone(pg.units[0].id, batumi_zone.id)
        goal.rules.append(gr)
        goal.rules.append(dcs.condition.UnitAlive(pg.units[0].id))
        m.goals.add_offline(goal)

        t = dcs.triggers.TriggerStart(comment='start test')
        t.actions.append(dcs.action.MessageToAll(m.string('Hi there fellow flyers!')))
        m.triggerrules.triggers.append(t)

        m.save('missions/basic_mission.miz')

    def test_nav_target_points(self):

        m = dcs.Mission()
        batumi = m.terrain.batumi()
        batumi.set_blue()
        usa = m.country("USA")

        jeff = m.flight_group_from_airport(usa, "JF17", dcs.planes.JF_17, group_size=2, airport=m.terrain.batumi())
        jeff.set_client()
        jeff.add_waypoint(m.terrain.batumi().position.point_from_heading(-90, 10000), 600)

        pp1_pos = batumi.position.point_from_heading(-90, 12000)
        jeff.add_nav_target_point(batumi.position.point_from_heading(-90, 12000), "PP1")
        jeff.add_nav_target_point(batumi.position.point_from_heading(-90, 14000), "PP2")
        jeff.add_nav_target_point(batumi.position.point_from_heading(-90, 16000), "PP3")
        jeff.add_nav_target_point(batumi.position.point_from_heading(-90, 18000), "PP4")

        # Test pydcs model
        self.assertEqual(len(jeff.nav_target_points), 4)
        self.assertEqual(jeff.nav_target_points[0].text_comment, "PP1")
        self.assertEqual(jeff.nav_target_points[0].position.x, pp1_pos.x)
        self.assertEqual(jeff.nav_target_points[0].position.y, pp1_pos.y)
        self.assertEqual(jeff.nav_target_points[0].index, 1)

        # Test dict representation
        self.assertTrue("NavTargetPoints" in jeff.dict().keys())
        self.assertTrue(jeff.dict()["NavTargetPoints"][0]["text_comment"] == "PP1")
        self.assertTrue(jeff.dict()["NavTargetPoints"][0]["x"] == pp1_pos.x)
        self.assertTrue(jeff.dict()["NavTargetPoints"][0]["y"] == pp1_pos.y)
        self.assertTrue(jeff.dict()["NavTargetPoints"][0]["index"] == 1)

        m.save("missions/mission_with_nav_target_points.miz")

        # load the mission back
        m2 = dcs.mission.Mission()
        self.assertTrue(m2.load_file("missions/mission_with_nav_target_points.miz"))
        jeff_miz = usa.find_group("JF17")

        # Test pydcs model from loaded mission
        self.assertEqual(len(jeff_miz.nav_target_points), 4)
        self.assertEqual(jeff_miz.nav_target_points[0].text_comment, "PP1")
        self.assertEqual(jeff_miz.nav_target_points[0].position.x, pp1_pos.x)
        self.assertEqual(jeff_miz.nav_target_points[0].position.y, pp1_pos.y)
        self.assertEqual(jeff_miz.nav_target_points[0].index, 1)


    def test_loadmission(self):
        m = dcs.mission.Mission()
        self.assertTrue(m.load_file('tests/loadtest.miz'))

        usa = m.country(dcs.countries.USA.name)

        # find single heli pad
        single_farp_group = usa.find_static_group("HeliSingle")
        single_farp: dcs.unit.SingleHeliPad = single_farp_group.units[0]
        self.assertIsNotNone(single_farp)
        self.assertEqual(single_farp_group.heading, 0)
        self.assertEqual(single_farp.heading, 0)
        self.assertEqual(single_farp.heliport_callsign_id, 1)
        self.assertEqual(single_farp.heliport_frequency, 127.5)

        # check blue farp
        blue_farp_group = usa.find_static_group("FARP")
        blue_farp: dcs.unit.FARP = blue_farp_group.units[0]
        self.assertIsNotNone(blue_farp)
        self.assertEqual(int(blue_farp.heading), 62)
        self.assertEqual(blue_farp.heliport_callsign_id, 2)
        self.assertEqual(blue_farp.heliport_frequency, 128.5)

        m.save('missions/loadtest.miz')
