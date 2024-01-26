import os
import time
import unittest
from pathlib import Path
import zipfile
import math

import dcs
from dcs.terrain.caucasus import Caucasus
from dcs.translation import String
from dcs.status_message import MessageSeverity, MessageType
from dcs.flyingunit import FlyingUnit
from dcs.unit import Ship
from dcs.task import WWIIFollowBigFormation
from dcs.action import PictureAction
from dcs.action import PictureToAll, PictureToCoalition, PictureToCountry, PictureToGroup, PictureToUnit
from dcs.task import Task, CarpetBombing, Expend, WeaponType
from dcs.action import Coalition
from dcs.mission import Mission
from enum import IntEnum


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
        batumi = caucasus.airports["Batumi"]
        self.assertIsNotNone(usa)
        pos = batumi.random_unit_zone(caucasus).center()
        vg = m.vehicle_group(usa, "Tanks", dcs.countries.USA.Vehicle.Armor.M_1_Abrams, pos)
        self.assertIsInstance(vg, dcs.unitgroup.VehicleGroup)
        pg = m.flight_group_inflight(
            usa, "Airgroup 1", dcs.planes.A_10C, dcs.Point(pos.x + 200, pos.y + 200, caucasus), 2000)
        self.assertIsInstance(pg, dcs.unitgroup.PlaneGroup)
        pg = m.flight_group_inflight(
            usa, "Airgroup 2", dcs.planes.M_2000C, dcs.Point(pos.x + 200, pos.y + 200, caucasus), 2000)
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

    def test_basic_mission(self) -> None:
        m = dcs.mission.Mission()
        assert isinstance(m.terrain, Caucasus)
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

        soganlug = m.terrain.airports["Soganlug"]
        soganlug.set_blue()
        tanker = m.refuel_flight(usa, "Tanker", dcs.planes.KC_135, None, soganlug.position, race_distance=120 * 1000,
                                 heading=270)
        self.assertIsNotNone(tanker)
        self.assertIsNotNone(tanker.points[0].find_task(dcs.task.Tanker))

        ustanks = m.vehicle_group(usa, "DefTanks", dcs.countries.USA.Vehicle.Armor.M_1_Abrams,
                                  dcs.mapping.Point(-283177.42857144, 659188, m.terrain), 300, 3)
        ustanks.add_unit(m.vehicle("airdef", dcs.countries.USA.Vehicle.AirDefence.M1097_Avenger))
        ustanks.add_unit(m.vehicle("aaa", dcs.countries.USA.Vehicle.AirDefence.Vulcan))
        ustanks.units[-1].skill = dcs.unit.Skill.High
        ustanks.formation(heading=310)

        heli = m.flight_group_inflight(
            usa, "heli", dcs.helicopters.UH_60A,
            dcs.mapping.Point(batumi.position.x + 1000 * 5, batumi.position.y, m.terrain),
            300, speed=150)
        heli.add_runway_waypoint(kobuleti)
        heli.land_at(kobuleti)

        apache = m.flight_group_from_airport(usa, "AirCav", dcs.helicopters.AH_64A, kobuleti, group_size=2)
        apache.load_loadout("8xAGM-114, 38xHYDRA-70 WP")
        apache.add_runway_waypoint(kobuleti)
        apache.add_waypoint(ustanks.position, 300, 200)

        senaki = m.terrain.airports["Senaki-Kolkhi"]
        senaki.set_red()
        russia = m.coalition["red"].country("Russia")
        bg = m.vehicle_group(
            russia, "Tanks", dcs.countries.Russia.Vehicle.Armor.T_90,
            dcs.mapping.Point(-281599.97853068, 645570.27528559, m.terrain), 180, 4,
            move_formation=dcs.point.PointAction.OnRoad)
        bg.add_waypoint(
            dcs.mapping.Point(-317423.36510278, 636737.32119577, m.terrain),
            dcs.point.PointAction.OnRoad, 50)

        mozdok = m.terrain.airports["Mozdok"]
        mozdok.set_red()
        rfighter = m.flight_group_from_airport(russia, "Migs", dcs.planes.MiG_29A, mozdok, group_size=2)
        last_wp = rfighter.add_runway_waypoint(mozdok)
        rfighter.add_waypoint(
            dcs.mapping.Point(last_wp.position.x - 1000 * 80, last_wp.position.y - 1000 * 150, m.terrain),
            6000, 800)

        sukhumi = m.terrain.airports["Sukhumi-Babushara"]
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
        su25.add_waypoint(
            dcs.mapping.Point(last_wp.position.x + 1000 * 10, last_wp.position.y, m.terrain), 3000)
        su25.add_runway_waypoint(sukhumi)
        su25.land_at(sukhumi)

        sg = m.ship_group(russia, "TaskForce", dcs.ships.MOSCOW,
                          dcs.mapping.Point(-209571.42857143, 500728.57142858, m.terrain), 0)
        sg.add_waypoint(dcs.mapping.Point(sg.x - 1000 * 60, sg.y + 1000 * 10, m.terrain))

        seapoint = batumi.unit_zones[0].random_point()
        seapoint.y -= 10 * 1000

        # carrier with aircraft
        sg = m.ship_group(usa, "CVN", dcs.countries.USA.Ship.Stennis, seapoint)
        m.flight_group_from_unit(usa, "F18 Carrier", dcs.planes.F_A_18C, sg, group_size=4)

        # some statics
        m.static_group(usa, "Static", dcs.statics.Fortification.Cafe, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SPlane", dcs.planes.B_1B, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SHeli", dcs.countries.USA.Helicopter.Mi_8MT, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SVehicle", dcs.countries.USA.Vehicle.Armor.LAV_25, batumi.unit_zones[0].random_point())
        m.static_group(usa, "SShip", dcs.countries.USA.Ship.PERRY,
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
        batumi = m.terrain.airports["Batumi"]
        batumi.set_blue()
        usa = m.country("USA")

        jeff = m.flight_group_from_airport(usa, "JF17", dcs.planes.JF_17, group_size=2, airport=m.terrain.airports["Batumi"])
        jeff.set_client()
        jeff.add_waypoint(m.terrain.airports["Batumi"].position.point_from_heading(-90, 10000), 600)

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
        self.assertEqual(0, len(m2.load_file("missions/mission_with_nav_target_points.miz")))
        usa_miz = m2.country("USA")
        jeff_miz = usa_miz.find_group("JF17")

        # Test pydcs model from loaded mission
        self.assertEqual(len(jeff_miz.nav_target_points), 4)
        self.assertEqual(jeff_miz.nav_target_points[0].text_comment, "PP1")
        self.assertEqual(jeff_miz.nav_target_points[0].position.x, pp1_pos.x)
        self.assertEqual(jeff_miz.nav_target_points[0].position.y, pp1_pos.y)
        self.assertEqual(jeff_miz.nav_target_points[0].index, 1)

    def test_create_mission_with_marks(self):
        m = dcs.Mission()
        batumi = m.terrain.airports["Batumi"]
        batumi.set_blue()
        kutaisi = m.terrain.airports["Kutaisi"]
        kutaisi.set_red()
        usa = m.country("USA")
        rus = m.country("Russia")

        # Create some group to use if you want to check visibility of marks in game
        su25_group = m.flight_group_from_airport(usa, "SU25", dcs.planes.Su_25T,
                                                 group_size=1, airport=m.terrain.airports["Batumi"])
        su25_group.set_client()

        f15_group = m.flight_group_from_airport(usa, "F15C", dcs.planes.F_15C,
                                                group_size=1, airport=m.terrain.airports["Batumi"])
        f15_group.set_client()

        su25_red_group = m.flight_group_from_airport(rus, "SU25 RED", dcs.planes.Su_25T,
                                                     group_size=1, airport=m.terrain.airports["Kutaisi"])
        su25_red_group.set_client()

        # In DCS, you have to create a trigger zone to add a mark.
        # This mark will be visible for all (after 2 sec)
        mark_all_pos = batumi.position.point_from_heading(-90, 12000)
        mark_all_zone = m.triggers.add_triggerzone(mark_all_pos, 1, False, "MARK TO ALL ZONE")
        mark_all_trigger = dcs.triggers.TriggerOnce(comment="Create Mark for ALL")
        mark_all_trigger.add_condition(dcs.condition.TimeAfter(2))
        mark_all_trigger.add_action(dcs.action.MarkToAll(10, mark_all_zone.id, m.string("Mark to all"),
                                                         m.string("Mark to all has been added"), True))
        m.triggerrules.triggers.append(mark_all_trigger)

        # This mark will be visible for blue coalition only (after 5 sec)
        mark_blue_pos = batumi.position.point_from_heading(-90, 24000)
        mark_blue_zone = m.triggers.add_triggerzone(mark_blue_pos, 1, False, "MARK TO BLUE COALITION ZONE")
        mark_blue_trigger = dcs.triggers.TriggerOnce(comment="Create Mark for BLUE")
        mark_blue_trigger.add_condition(dcs.condition.TimeAfter(5))
        mark_blue_trigger.add_action(
            dcs.action.MarkToCoalition(11, mark_blue_zone.id, dcs.action.Coalition.Blue, m.string("Mark to Blue"),
                                       m.string("Mark to Blue coalition has been added"), True))
        m.triggerrules.triggers.append(mark_blue_trigger)

        # This mark will be visible for red coalition only (after 8 sec)
        mark_red_pos = batumi.position.point_from_heading(-90, 24000).point_from_heading(0, 5000)
        mark_red_zone = m.triggers.add_triggerzone(mark_red_pos, 1, False, "MARK TO RED COALITION ZONE")
        mark_red_trigger = dcs.triggers.TriggerOnce(comment="Create Mark for RED")
        mark_red_trigger.add_condition(dcs.condition.TimeAfter(8))
        mark_red_trigger.add_action(
            dcs.action.MarkToCoalition(12, mark_red_zone.id, dcs.action.Coalition.Red, m.string("Mark to RED"),
                                       m.string("Mark to Red coalition has been added"), True))
        m.triggerrules.triggers.append(mark_red_trigger)

        # This mark will be visible for the F15 group only (after 11 sec)
        mark_f15_pos = batumi.position.point_from_heading(-90, 12000).point_from_heading(0, 5000)
        mark_f15_zone = m.triggers.add_triggerzone(mark_f15_pos, 1, False, "MARK TO F15 ZONE")
        mark_f15_trigger = dcs.triggers.TriggerOnce(comment="Create Mark for F15")
        mark_f15_trigger.add_condition(dcs.condition.TimeAfter(11))
        mark_f15_trigger.add_action(
            dcs.action.MarkToGroup(13, mark_f15_zone.id, f15_group.id, m.string("Mark to F15"),
                                   m.string("Mark to F15 group has been added"), False))
        m.triggerrules.triggers.append(mark_f15_trigger)

        self.assertEqual(len(m.triggerrules.triggers), 4)

        self.assertEqual(mark_all_trigger.actions[0].dict()["zone"], mark_all_zone.id)
        self.assertEqual(mark_all_trigger.actions[0].dict()["value"], 10)
        self.assertEqual(mark_all_trigger.actions[0].dict()["readonly"], True)

        self.assertEqual(mark_blue_trigger.actions[0].dict()["zone"], mark_blue_zone.id)
        self.assertEqual(mark_blue_trigger.actions[0].dict()["coalitionlist"], dcs.action.Coalition.Blue.value)
        self.assertEqual(mark_blue_trigger.actions[0].dict()["value"], 11)
        self.assertEqual(mark_blue_trigger.actions[0].dict()["readonly"], True)

        self.assertEqual(mark_red_trigger.actions[0].dict()["zone"], mark_red_zone.id)
        self.assertEqual(mark_red_trigger.actions[0].dict()["coalitionlist"], dcs.action.Coalition.Red.value)
        self.assertEqual(mark_red_trigger.actions[0].dict()["value"], 12)
        self.assertEqual(mark_red_trigger.actions[0].dict()["readonly"], True)

        self.assertEqual(mark_f15_trigger.actions[0].dict()["zone"], mark_f15_zone.id)
        self.assertEqual(mark_f15_trigger.actions[0].dict()["group"], f15_group.id)
        self.assertEqual(mark_f15_trigger.actions[0].dict()["value"], 13)
        self.assertEqual(mark_f15_trigger.actions[0].dict()["readonly"], False)

        m.save("missions/mission_with_marks_triggers.miz")

    def test_create_mission_on_channel_map(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.TheChannel())

        usa = m.country("USA")
        russia = m.country("Russia")
        fw190 = m.flight_group_from_airport(russia, "FW-190", dcs.planes.FW_190D9, group_size=1,
                                            airport=m.terrain.airports["Dunkirk Mardyck"])
        fw190.add_waypoint(m.terrain.airports["Dunkirk Mardyck"].position.point_from_heading(-90, 40000), 500, 300)
        p47 = m.flight_group_from_airport(usa, "P-47", dcs.planes.P_47D_30, group_size=1,
                                          airport=m.terrain.airports["Hawkinge"])
        p47.add_waypoint(m.terrain.airports["Dunkirk Mardyck"].position.point_from_heading(-90, 40000), 500, 300)

        m.save('missions/test_mission_the_channel.miz')

        # Test load mission
        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/test_mission_the_channel.miz')))
        self.assertEqual(m2.terrain.__class__, dcs.terrain.TheChannel)

    def test_create_mission_on_syria_map(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Syria())

        usa = m.country("USA")
        russia = m.country("Russia")
        fa18 = m.flight_group_from_airport(usa, "F/A-18C", dcs.planes.FA_18C_hornet, group_size=1,
                                           airport=m.terrain.airports["Damascus"])
        fa18.add_waypoint(m.terrain.airports["Damascus"].position.point_from_heading(-90, 40000), 500, 300)
        su22 = m.flight_group_from_airport(russia, "Su22", dcs.planes.Su_17M4, group_size=1,
                                           airport=m.terrain.airports["Damascus"])
        su22.add_waypoint(m.terrain.airports["Damascus"].position.point_from_heading(-90, 40000), 500, 300)

        m.save('missions/test_mission_syria.miz')

        # Test load mission
        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/test_mission_syria.miz')))
        self.assertEqual(m2.terrain.__class__, dcs.terrain.Syria)

    def test_create_mission_with_part_of_coalition_zone_trigger(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        usa = m.country("USA")

        trigger_zone = m.triggers.add_triggerzone(m.terrain.airports["Batumi"].position.point_from_heading(90, 15000),
                                                  radius=5000, hidden=False, name="TRIGGER_ZONE")
        trigger = dcs.triggers.TriggerOnce(dcs.triggers.Event.NoEvent, "Detection of blue aircraft")
        trigger.add_condition(dcs.condition.PartOfCoalitionInZone("blue", trigger_zone.id, "AIRPLANE"))
        trigger.add_action(dcs.action.MessageToAll(text=String("Blue aircraft detected in trigger zone !")))
        m.triggerrules.triggers.append(trigger)

        trigger_zone_2 = m.triggers.add_triggerzone(m.terrain.airports["Batumi"].position, radius=5000, hidden=False,
                                                    name="BATUMI_ZONE")
        trigger_outside = dcs.triggers.TriggerOnce(dcs.triggers.Event.NoEvent, "No blue in batumi zone")
        trigger_outside.add_condition(dcs.condition.PartOfCoalitionOutsideZone("blue", trigger_zone_2.id, "AIRPLANE"))
        trigger_outside.add_action(dcs.action.MessageToAll(
            text=String("Blue aircraft are not in batumi zone anymore!")))
        m.triggerrules.triggers.append(trigger_outside)

        f15 = m.flight_group_inflight(usa, "F15", dcs.planes.F_15C, m.terrain.airports["Batumi"].position, 1000)
        f15.add_waypoint(trigger_zone.position, 500)

        m.save('missions/mission_with_part_of_coalition_zone_trigger.miz')

        # Test load mission
        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/mission_with_part_of_coalition_zone_trigger.miz')))

        self.assertEqual(m2.triggerrules.triggers[0].rules[0].unitType, "AIRPLANE")
        self.assertEqual(m2.triggerrules.triggers[0].rules[0].zone, trigger_zone.id)
        self.assertEqual(m2.triggerrules.triggers[0].rules[0].coalitionlist, "blue")

        self.assertEqual(m2.triggerrules.triggers[1].rules[0].unitType, "AIRPLANE")
        self.assertEqual(m2.triggerrules.triggers[1].rules[0].zone, trigger_zone_2.id)
        self.assertEqual(m2.triggerrules.triggers[1].rules[0].coalitionlist, "blue")

    def _assert_prepared_mission_load(self, m: dcs.mission.Mission):
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

        # check map resources
        self.assertEqual(3, len(m.map_resource.files['DEFAULT']))
        self.assertEqual("sample.lua", m.map_resource.get_file_path((m.map_resource.get_resource_keys()[0])))
        self.assertEqual("sample.lua", m.map_resource.get_file_path((m.map_resource.get_resource_keys()[1])))
        self.assertEqual("test.lua", m.map_resource.get_file_path((m.map_resource.get_resource_keys()[2])))

        # check triggers
        self.assertEqual(4, len(m.triggerrules.triggers))
        self.assertEqual("1", m.triggerrules.triggers[0].comment)
        self.assertEqual("2", m.triggerrules.triggers[1].comment)
        self.assertEqual("3", m.triggerrules.triggers[2].comment)

        # check options count
        all_task_flight = usa.find_plane_group("AllTasks")
        self.assertIsNotNone(all_task_flight)
        self.assertEqual(8, len(all_task_flight.points))
        wp1 = all_task_flight.points[1]
        self.assertTrue(all([isinstance(t, dcs.task.Option) for t in wp1.tasks]))
        self.assertEqual(18, len(wp1.tasks))
        opt_radio_silence = wp1.tasks[7]
        self.assertIsInstance(opt_radio_silence, dcs.task.OptRadioSilence)
        self.assertTrue(opt_radio_silence.value)

        # check commands
        wp8 = all_task_flight.points[7]
        self.assertEqual(11, len(wp8.tasks))
        com_immortal = wp8.tasks[7]
        self.assertIsInstance(com_immortal, dcs.task.SetImmortalCommand)
        self.assertTrue(com_immortal.value)

    def test_load_prepared_mission(self):
        m = dcs.mission.Mission()
        m.load_file('tests/loadtest.miz')

        self._assert_prepared_mission_load(m)

        m.save('missions/loadtest.miz')

        # reload mission
        m = dcs.mission.Mission()
        m.load_file('missions/loadtest.miz')

        self._assert_prepared_mission_load(m)

    def test_load_test_missions(self):
        def current_milli_time():
            return int(round(time.time() * 1000))
        test_mission_folder = os.path.join(os.path.dirname(__file__), 'missions')
        for f in os.listdir(test_mission_folder):
            if f.endswith('.miz'):
                print('-' * 10, "Loading", f)
                start = current_milli_time()
                m = dcs.mission.Mission()
                m.load_file(os.path.join(test_mission_folder, f))
                print('-' * 10, "Loaded", f, "in", current_milli_time() - start, "ms")
                print('-' * 10, "Saving", f)
                start = current_milli_time()
                self.assertTrue(m.save('missions/unittest_' + f))
                print('-' * 10, "Saved", f, "in", current_milli_time() - start, "ms")

    def test_fix_onboard_numbers(self):
        m = dcs.mission.Mission()
        msgs = m.load_file(os.path.join(os.path.dirname(__file__), 'missions', 'Forestry_Operations.miz'))
        self.assertEqual(4, len(msgs))
        self.assertTrue(all([x.severity == MessageSeverity.WARN for x in msgs]))

        m.reassign_onboard_numbers()

        save_path = os.path.join('missions', 'fix_onboard_Forestry_Operations.miz')
        m.save(save_path)
        print('-' * 10, "Saved", save_path)
        # reload mission
        m = dcs.mission.Mission()
        msgs = m.load_file(save_path)
        self.assertEqual(0, len(msgs))

    def test_kneeboard(self):
        m = dcs.mission.Mission()
        # Kneeboards need to be images for DCS, but we don't care in the test.
        kneeboard = Path("missions/kneeboard.txt")
        kneeboard.write_bytes(b"Hello, world!")
        m.add_aircraft_kneeboard(dcs.planes.F_15C, kneeboard)
        mission_file = Path('missions/kneeboard_mission.miz')
        m.save(mission_file)
        with zipfile.ZipFile(mission_file) as zipf:
            with zipf.open("KNEEBOARD/F-15C/IMAGES/kneeboard.txt") as zipkb:
                self.assertEqual(b"Hello, world!", zipkb.read())

    def test_radio_channels(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Syria())

        country_name = "USA"
        group_name = "F/A-18C"
        group = m.flight_group_from_airport(
            m.country(country_name),
            group_name,
            dcs.planes.FA_18C_hornet,
            group_size=1,
            airport=m.terrain.airports["Damascus"]
        )
        unit = group.units[0]
        unit.set_client()
        frequency = 300.0
        self.assertNotAlmostEqual(unit.radio[2]["channels"][1], frequency)
        if unit.radio is not None:
            unit.set_radio_channel_preset(2, 1, frequency)
        mission_file = Path('missions/radio_channels.miz')
        m.save(mission_file)

        m = dcs.mission.Mission()
        self.assertEqual(0, len(m.load_file('missions/radio_channels.miz')))
        group = m.country(country_name).find_group(group_name)
        self.assertIsNotNone(group)
        self.assertIsInstance(group, dcs.unitgroup.FlyingGroup)
        self.assertEqual(1, len(group.units))
        unit = group.units[0]
        self.assertIsInstance(unit, FlyingUnit)
        self.assertAlmostEqual(unit.radio[2]["channels"][1], frequency)

    def test_ship_frequency(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        country_name = "USA"
        group_name = "CVN"
        batumi = m.terrain.airports["Batumi"]
        mission_name = "ship_radios"

        seapoint = batumi.unit_zones[0].random_point()
        seapoint.y -= 10 * 1000
        group = m.ship_group(
            m.country(country_name),
            group_name,
            dcs.countries.USA.Ship.Stennis,
            seapoint
        )
        unit: Ship = group.units[0]
        frequency = 300000000
        self.assertNotEqual(unit.frequency, frequency)
        unit.set_frequency(frequency)
        self.assertEqual(unit.frequency, frequency)
        frequency = 250000000
        group.set_frequency(frequency)
        self.assertEqual(unit.frequency, frequency)
        mission_file = Path(f"missions/{mission_name}.miz")
        m.save(mission_file)

        m = dcs.mission.Mission()
        self.assertEqual(0, len(m.load_file(f"missions/{mission_name}.miz")))
        group = m.country(country_name).find_group(group_name)
        self.assertIsNotNone(group)
        self.assertIsInstance(group, dcs.unitgroup.ShipGroup)
        self.assertEqual(1, len(group.units))
        unit = group.units[0]
        self.assertIsInstance(unit, dcs.unit.Ship)
        self.assertEqual(unit.frequency, frequency)

    def test_create_scenery_destruction_zone(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        usa = m.country("USA")
        point = dcs.Point(-217283, 564863, m.terrain)  # This is a compound north of sukhmi, with buildings and trees
        m.vehicle_group(usa, "Vehicle", dcs.countries.USA.Vehicle.AirDefence.Vulcan, position=point)

        # Create trigger zone
        destruction_zone = m.triggers.add_triggerzone(point, 1000, False, "destruction zone")

        # Add destruction zone trigger
        t = dcs.triggers.TriggerOnce(comment='Destruction')
        t.actions.append(dcs.action.SceneryDestructionZone(95, destruction_zone.id))
        m.triggerrules.triggers.append(t)

        m.save('missions/test_mission_scenery_destruction.miz')

        # Test reload the mission
        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/test_mission_scenery_destruction.miz')))
        self.assertEqual(m2.terrain.__class__, dcs.terrain.Caucasus)
        self.assertTrue(type(m2.triggerrules.triggers[0].actions[0]) is dcs.action.SceneryDestructionZone)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].destruction_level, 95)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].zone, destruction_zone.id)

    def test_remove_trees_in_zone(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        usa = m.country("USA")
        point = dcs.Point(-217283, 564863, m.terrain)  # This is a compound north of sukhmi, with buildings and trees
        m.vehicle_group(usa, "Vehicle", dcs.countries.USA.Vehicle.AirDefence.Vulcan, position=point)

        # Create trigger zone
        removal_zone = m.triggers.add_triggerzone(point, 1000, False, "removal zone")

        # Add destruction zone trigger
        t = dcs.triggers.TriggerOnce(comment='Remove Trees')
        t.actions.append(dcs.action.RemoveSceneObjects(dcs.action.RemoveSceneObjectsMask.TREES_ONLY, removal_zone.id))
        m.triggerrules.triggers.append(t)

        m.save('missions/test_mission_remove_trees.miz')

        # Test reload the mission
        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/test_mission_remove_trees.miz')))
        self.assertEqual(m2.terrain.__class__, dcs.terrain.Caucasus)
        self.assertTrue(type(m2.triggerrules.triggers[0].actions[0]) is dcs.action.RemoveSceneObjects)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].objects_mask,
                         dcs.action.RemoveSceneObjectsMask.TREES_ONLY)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].zone, removal_zone.id)

    def test_remove_objects_in_zone(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        usa = m.country("USA")
        point = dcs.Point(-217283, 564863, m.terrain)  # This is a compound north of sukhmi, with buildings and trees
        m.vehicle_group(usa, "Vehicle", dcs.countries.USA.Vehicle.AirDefence.Vulcan, position=point)

        # Create trigger zone
        removal_zone = m.triggers.add_triggerzone(point, 1000, False, "removal zone")

        # Add destruction zone trigger
        t = dcs.triggers.TriggerOnce(comment='Remove Trees')
        t.actions.append(dcs.action.RemoveSceneObjects(dcs.action.RemoveSceneObjectsMask.OBJECTS_ONLY, removal_zone.id))
        m.triggerrules.triggers.append(t)

        m.save('missions/test_mission_remove_objects.miz')

        # Test reload the mission
        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/test_mission_remove_objects.miz')))
        self.assertEqual(m2.terrain.__class__, dcs.terrain.Caucasus)
        self.assertTrue(type(m2.triggerrules.triggers[0].actions[0]) is dcs.action.RemoveSceneObjects)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].objects_mask,
                         dcs.action.RemoveSceneObjectsMask.OBJECTS_ONLY)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].zone, removal_zone.id)

    def test_remove_trees_and_objects_in_zone(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        usa = m.country("USA")
        point = dcs.Point(-217283, 564863, m.terrain)  # This is a compound north of sukhmi, with buildings and trees
        m.vehicle_group(usa, "Vehicle", dcs.countries.USA.Vehicle.AirDefence.Vulcan, position=point)

        # Create trigger zone
        removal_zone = m.triggers.add_triggerzone(point, 1000, False, "removal zone")

        # Add destruction zone trigger
        t = dcs.triggers.TriggerOnce(comment='Remove Trees')
        t.actions.append(dcs.action.RemoveSceneObjects(dcs.action.RemoveSceneObjectsMask.ALL, removal_zone.id))
        m.triggerrules.triggers.append(t)

        m.save('missions/test_mission_remove_all.miz')

        # Test reload the mission
        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/test_mission_remove_all.miz')))
        self.assertEqual(m2.terrain.__class__, dcs.terrain.Caucasus)
        self.assertTrue(type(m2.triggerrules.triggers[0].actions[0]) is dcs.action.RemoveSceneObjects)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].objects_mask, dcs.action.RemoveSceneObjectsMask.ALL)
        self.assertEqual(m2.triggerrules.triggers[0].actions[0].zone, removal_zone.id)

    def test_bypass_triggers(self):
        m = dcs.mission.Mission()
        self.assertEqual(0, len(m.load_file('tests/bypass_triggers.miz', True)))

        saved_mission = 'missions/test_bypass_triggers.miz'
        m.save(saved_mission)

        # Test reload the mission
        with zipfile.ZipFile(saved_mission, 'r') as miz:
            with miz.open('mission', 'r') as mission:
                content = mission.read().decode('utf-8')
                result = content.find('["unknown_test_key"]')

        self.assertNotEqual(result, -1)

    def test_mission_with_qf17_aaa(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        usa = m.country("USA")
        caucasus = m.terrain
        batumi = caucasus.airports["Batumi"]
        m.vehicle_group(usa, "qf17", dcs.countries.USA.Vehicle.AirDefence.QF_37_AA,
                        position=batumi.random_unit_zone(caucasus).center())

        m.save('missions/test_mission_qf17.miz')

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file('missions/test_mission_qf17.miz')))

        group = m2.country("USA").find_group("qf17")
        self.assertEqual(group.units[0].type, dcs.vehicles.AirDefence.QF_37_AA.id)

    def test_mission_neutral(self):
        m = dcs.mission.Mission()
        self.assertEqual([], m.load_file('tests/loadtest.miz'))

        neutral_country_name = "Sweden"
        sweden = m.country(neutral_country_name)

        self.assertTrue(sweden is not None)
        self.assertEqual(len(sweden.ship_group), 1)
        self.assertEqual(len(sweden.plane_group), 1)

        mission_path = 'missions/test_mission_neutral.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))

        sweden2 = m.country(neutral_country_name)
        self.assertTrue(sweden2 is not None)
        self.assertEqual(len(sweden2.ship_group), 1)
        self.assertEqual(len(sweden2.plane_group), 1)

    def test_mission_save_pictureFileName(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())
        image_path = 'tests/images/blue.png'
        reskey_b = m.add_picture_blue(image_path)
        reskey_r = m.add_picture_red(image_path)
        reskey_n = m.add_picture_neutral(image_path)

        mission_path = 'missions/test_mission_pictureFileName.miz'
        m.save(mission_path)

        m2 = dcs.mission.Mission()
        self.assertEqual(0, len(m2.load_file(mission_path)))

        self.assertEqual(len(m2.pictureFileNameB), 1)
        self.assertEqual(m2.pictureFileNameB[0], reskey_b.key)
        self.assertEqual(len(m2.pictureFileNameR), 1)
        self.assertEqual(m2.pictureFileNameR[0], reskey_r.key)
        self.assertEqual(len(m2.pictureFileNameN), 1)
        self.assertEqual(m2.pictureFileNameN[0], reskey_n.key)

    def test_create_quad_point_zone(self):
        caucasus = dcs.terrain.Caucasus()
        m = dcs.mission.Mission(terrain=caucasus)

        # Create a quad trigger zone centered at Sukhumi with a diamond pattern
        #   /\
        #  /  \
        #  \  /
        #   \/
        zone_center: dcs.mapping.Point = caucasus.airports["Sukhumi-Babushara"].position
        ZONE_RADIUS_M = 10000.0
        offsets = [(ZONE_RADIUS_M, 0.0), (0.0, ZONE_RADIUS_M),
                   (-ZONE_RADIUS_M, 0.0), (0.0, -ZONE_RADIUS_M)]
        offsets = [dcs.mapping.Vector2(*o) for o in offsets]
        verts = [zone_center + o for o in offsets]
        m.triggers.add_triggerzone_quad(zone_center, verts, False, "quad zone")
        print(m.triggers.zones())
        m.save('missions/test_quad_trigger_zone.miz')

        m2 = dcs.mission.Mission()
        self.assertEqual(
            0, len(m2.load_file('missions/test_quad_trigger_zone.miz')))
        zone = m2.triggers.zones()[0]
        self.assertEqual(m2.terrain.__class__, dcs.terrain.Caucasus)
        self.assertTrue(isinstance(zone, dcs.triggers.TriggerZone))
        self.assertTrue(type(zone) == dcs.triggers.TriggerZoneQuadPoint)

        def distance(p1: dcs.mapping.Point, p2: dcs.mapping.Point) -> float:
            p = p1 - p2
            return math.sqrt(p.x**2 + p.y**2)

        sukhmi: dcs.mapping.Point = caucasus.airports["Sukhumi-Babushara"].position
        self.assertTrue(
            all(
                distance(sukhmi, v) <= ZONE_RADIUS_M + 0.001
                for v in zone.verticies))

    def test_restrict_targets(self):
        m = dcs.mission.Mission(terrain=dcs.terrain.Caucasus())

        usa = m.country("USA")
        point = dcs.Point(-217283, 564863, m.terrain)
        vulcan_group = m.vehicle_group(usa, "Vehicle", dcs.countries.USA.Vehicle.AirDefence.Vulcan, position=point)
        waypoint = vulcan_group.points[0]
        waypoint.tasks.append(dcs.task.OptRestrictTargets(dcs.task.OptRestrictTargets.Values.AirUnitsOnly))
        vg_tasks = vulcan_group.dict()['route']['points'][1]['task']
        self.assertEqual(vg_tasks['id'], 'ComboTask')
        tasks_param = vg_tasks['params']['tasks']

        def is_restrict_targets_a2a_option(d):
            p = d['params']['action']['params']
            return 'name' in p and p['name'] == 28 and p['value'] == 1

        self.assertTrue(any(is_restrict_targets_a2a_option(tasks_param[k]) for k in tasks_param.keys()))

    def test_vehicle_group_platoon(self) -> None:
        m = dcs.mission.Mission()
        usa = m.coalition["blue"].country("USA")
        batumi = m.terrain.airports["Batumi"]
        pos = batumi.random_unit_zone(m.terrain).center()
        types = [
            dcs.countries.USA.Vehicle.Armor.M_1_Abrams,
            dcs.countries.USA.Vehicle.Armor.M_2_Bradley,
            dcs.countries.USA.Vehicle.Armor.M_60
        ]
        vehicles = [
            m.vehicle(f"tank {ii:03d}", t) for ii, t in enumerate(types)
        ]
        vg1 = m.vehicle_group_platoon(usa, "tanks1", types, pos)
        vg2 = m.vehicle_group_from_vehicles(usa, "tanks2", vehicles, pos)

        self.assertIsNotNone(vg1)
        self.assertIsNotNone(vg2)

        mizname = os.path.join('missions', 'test_vehicle_group.miz')
        m.save(mizname)
        m2 = dcs.mission.Mission()
        m2.load_file(mizname)
        usa: dcs.countries.Country = m2.coalition['blue'].country('USA')
        tanks1: dcs.unitgroup.VehicleGroup = usa.find_group("tanks1")
        tanks2: dcs.unitgroup.VehicleGroup = usa.find_group("tanks2")
        self.assertIsNotNone(tanks1)
        self.assertIsNotNone(tanks2)

        for group in (tanks1, tanks2):
            self.assertEqual(len(group.units), len(types))
            for u, t in zip(group.units, types):
                self.assertEqual(u.type, t.id)

        self.assertListEqual(
            [f"tank {ii:03d}" for ii, _ in enumerate(tanks2.units)],
            [t.name for t in tanks2.units])

    def test_rail_car(self) -> None:
        m = dcs.mission.Mission()
        assert isinstance(m.terrain, Caucasus)
        usa = m.coalition["blue"].country("USA")
        batumi = m.terrain.airports["Batumi"]
        m.static_group(usa, "rail_car", "Coach a passenger",
                       batumi.unit_zones[0].center())

        mizname = "missions/test_rail_car.miz"
        m.save(mizname)
        m2 = dcs.mission.Mission()
        m2.load_file(mizname)

        self.assertTrue(
            any(g.name == "rail_car"
                for g in m2.coalition["blue"].countries["USA"].static_group))

    def test_smoke_preset(self) -> None:
        m = dcs.mission.Mission()
        usa = m.coalition["blue"].country("USA")
        batumi = m.terrain.airports["Batumi"]

        smoke = m.static_group(usa, "some smoke", "big_smoke",
                               batumi.unit_zones[0].center())
        u = smoke.units[0]
        u.effect_preset = 3
        u.category = "Effects"
        mizname = "missions/test_smoke_preset.miz"
        m.save(mizname)
        m2 = dcs.mission.Mission()
        m2.load_file(mizname)

        def preset_preserved(group: dcs.unitgroup.StaticGroup,
                             preset_number: int):
            u = group.units[0]
            is_effect = u.category == "Effects"
            return is_effect and u.effect_preset == preset_number

        static_groups = m2.coalition["blue"].countries["USA"].static_group
        self.assertTrue(any(preset_preserved(g, 3) for g in static_groups))

    def test_smoke_required_modules(self) -> None:
        mizname = "tests/missions/Mission_with_required_modules.miz"
        m = dcs.mission.Mission()
        m.load_file(mizname)
        self.assertEqual(m.required_modules, {"WWII Armour and Technics": "WWII Armour and Technics"})

        saved_miz = "tests/missions/Mission_with_required_modules_saved.miz"
        m.save(saved_miz)
        m2 = dcs.mission.Mission()
        m2.load_file(saved_miz)
        self.assertEqual(m.required_modules, m2.required_modules)

    def test_big_formation_action_leader(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[0].points[0].tasks[5], WWIIFollowBigFormation)

        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[0].points[0].tasks[5]

        self.assertNotIn("groupId", task.params)
        self.assertNotIn("lastWptIndex", task.params)
        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.COMBAT_BOX_FOR_OPEN_FORMATION)
        self.assertEqual(task.params["pos"], {"x": 0, "y": 0, "z": 0})
        self.assertTrue(task.params["lastWptIndexFlagChangedManually"])
        self.assertEqual(len(task.params), 7)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[0].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[0].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_big_formation_action_left(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[1].points[0].tasks[5], WWIIFollowBigFormation)
        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[1].points[0].tasks[5]

        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.JAVELIN_DOWN)
        self.assertEqual(task.params["pos"], {"x": -480, "y": -70, "z": -240})
        self.assertEqual(task.params["groupId"], 2)
        self.assertEqual(task.params["posInGroup"], 2)
        self.assertEqual(task.params["lastWptIndex"], 3)
        self.assertTrue(task.params["lastWptIndexFlag"])
        self.assertEqual(len(task.params), 9)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[1].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[1].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_big_formation_action_back(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[2].points[0].tasks[5], WWIIFollowBigFormation)
        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[2].points[0].tasks[5]

        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.COMBAT_BOX)
        self.assertEqual(task.params["pos"], {"x": -320, "y": -50, "z": -0})
        self.assertEqual(task.params["groupId"], 2)
        self.assertEqual(task.params["posInBox"], 3)
        self.assertEqual(task.params["lastWptIndex"], 3)
        self.assertFalse(task.params["lastWptIndexFlag"])
        self.assertEqual(len(task.params), 9)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[2].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[2].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_big_formation_action_right(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[3].points[0].tasks[5], WWIIFollowBigFormation)
        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[3].points[0].tasks[5]

        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.COMBAT_BOX_FOR_OPEN_FORMATION)
        self.assertEqual(task.params["pos"], {"x": -160, "y": 50, "z": 240})
        self.assertEqual(task.params["groupId"], 2)
        self.assertEqual(task.params["posInBox"], 1)
        self.assertEqual(task.params["lastWptIndex"], 3)
        self.assertTrue(task.params["lastWptIndexFlag"])
        self.assertEqual(len(task.params), 9)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[3].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[3].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_big_formation_action_leader(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[0].points[0].tasks[5], WWIIFollowBigFormation)

        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[0].points[0].tasks[5]

        self.assertNotIn("groupId", task.params)
        self.assertNotIn("lastWptIndex", task.params)
        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.COMBAT_BOX_FOR_OPEN_FORMATION)
        self.assertEqual(task.params["pos"], {"x": 0, "y": 0, "z": 0})
        self.assertTrue(task.params["lastWptIndexFlagChangedManually"])
        self.assertEqual(len(task.params), 7)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[0].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[0].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_big_formation_action_left(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[1].points[0].tasks[5], WWIIFollowBigFormation)
        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[1].points[0].tasks[5]

        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.JAVELIN_DOWN)
        self.assertEqual(task.params["pos"], {"x": -480, "y": -70, "z": -240})
        self.assertEqual(task.params["groupId"], 2)
        self.assertEqual(task.params["posInGroup"], 2)
        self.assertEqual(task.params["lastWptIndex"], 3)
        self.assertTrue(task.params["lastWptIndexFlag"])
        self.assertEqual(len(task.params), 9)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[1].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[1].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_big_formation_action_back(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[2].points[0].tasks[5], WWIIFollowBigFormation)
        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[2].points[0].tasks[5]

        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.COMBAT_BOX)
        self.assertEqual(task.params["pos"], {"x": -320, "y": -50, "z": -0})
        self.assertEqual(task.params["groupId"], 2)
        self.assertEqual(task.params["posInBox"], 3)
        self.assertEqual(task.params["lastWptIndex"], 3)
        self.assertFalse(task.params["lastWptIndexFlag"])
        self.assertEqual(len(task.params), 9)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[2].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[2].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_big_formation_action_right(self) -> None:
        m_name = "tests/missions/big-formation.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        assert isinstance(m.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[3].points[0].tasks[5], WWIIFollowBigFormation)
        task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[3].points[0].tasks[5]

        self.assertEqual(task.params["formationType"], WWIIFollowBigFormation.FormationType.COMBAT_BOX_FOR_OPEN_FORMATION)
        self.assertEqual(task.params["pos"], {"x": -160, "y": 50, "z": 240})
        self.assertEqual(task.params["groupId"], 2)
        self.assertEqual(task.params["posInBox"], 1)
        self.assertEqual(task.params["lastWptIndex"], 3)
        self.assertTrue(task.params["lastWptIndexFlag"])
        self.assertEqual(len(task.params), 9)

        m2_name = "missions/saved_big-formation.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.coalition['blue'].country("Combined Joint Task Forces Blue")
                          .plane_group[3].points[0].tasks[5], WWIIFollowBigFormation)
        m2_task = m.coalition['blue'].country("Combined Joint Task Forces Blue").plane_group[3].points[0].tasks[5]

        self.assertEqual(task, m2_task)

    def test_action_a_out_picture(self) -> None:
        mizname = "tests/missions/a_out_picture.miz"
        m = dcs.mission.Mission()
        m.load_file(mizname)

        assert isinstance(m.triggerrules.triggers[0].actions[0], PictureToAll)
        m_action = m.triggerrules.triggers[0].actions[0]

        self.assertEqual(m_action.seconds, 10)
        self.assertFalse(m_action.clearview)
        self.assertEqual(m_action.start_delay, 3)
        self.assertEqual(m_action.horz_alignment, PictureAction.HorzAlignment.Left)
        self.assertEqual(m_action.vert_alignment, PictureAction.VertAlignment.Top)
        self.assertEqual(m_action.size, 100)
        self.assertEqual(m_action.size_units, PictureAction.SizeUnits.OriginalSize)

        m2_name = "missions/saved_a_out_picture.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        self.assertEqual(m_action, m2.triggerrules.triggers[0].actions[0])

    def test_action_a_out_picture_s(self) -> None:
        mizname = "tests/missions/a_out_picture.miz"
        m = dcs.mission.Mission()
        m.load_file(mizname)

        assert isinstance(m.triggerrules.triggers[0].actions[1], PictureToCoalition)
        m_action = m.triggerrules.triggers[0].actions[1]

        self.assertEqual(m_action.coalition, "blue")

        m2_name = "missions/saved_a_out_picture.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        self.assertEqual(m_action, m2.triggerrules.triggers[0].actions[1])

    def test_action_a_out_picture_c(self) -> None:
        mizname = "tests/missions/a_out_picture.miz"
        m = dcs.mission.Mission()
        m.load_file(mizname)

        assert isinstance(m.triggerrules.triggers[0].actions[2], PictureToCountry)
        m_action = m.triggerrules.triggers[0].actions[2]

        self.assertEqual(m_action.country, dcs.countries.get_by_name("Ukraine"))

        m2_name = "missions/saved_a_out_picture.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        self.assertEqual(m_action, m2.triggerrules.triggers[0].actions[2])

    def test_action_a_out_picture_g(self) -> None:
        mizname = "tests/missions/a_out_picture.miz"
        m = dcs.mission.Mission()
        m.load_file(mizname)

        assert isinstance(m.triggerrules.triggers[0].actions[3], PictureToGroup)
        m_action = m.triggerrules.triggers[0].actions[3]

        self.assertEqual(m_action.group.id, 1)

        m2_name = "missions/saved_a_out_picture.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        assert isinstance(m2.triggerrules.triggers[0].actions[3], PictureToGroup)
        m2_action = m2.triggerrules.triggers[0].actions[3]

        self.assertEqual(m_action.group.id, m2_action.group.id)

    def test_action_a_out_picture_u_no_file(self) -> None:
        mizname = "tests/missions/a_out_picture.miz"
        m = dcs.mission.Mission()
        m.load_file(mizname)

        assert isinstance(m.triggerrules.triggers[0].actions[4], PictureToUnit)
        m_action = m.triggerrules.triggers[0].actions[4]

        self.assertEqual(m_action.unit_id, 1)
        self.assertEqual(m_action.file_res_key.key, "")

        m2_name = "missions/saved_a_out_picture.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        self.assertEqual(m_action, m2.triggerrules.triggers[0].actions[4])

    def test_action_a_out_picture_u(self) -> None:
        mizname = "tests/missions/a_out_picture.miz"
        m = dcs.mission.Mission()
        m.load_file(mizname)

        assert isinstance(m.triggerrules.triggers[0].actions[5], PictureToUnit)
        m_action = m.triggerrules.triggers[0].actions[5]

        self.assertEqual(m_action.unit_id, 1)

        m2_name = "missions/saved_a_out_picture.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        self.assertEqual(m_action, m2.triggerrules.triggers[0].actions[5])

    def test_resource_name_conflict_in_two_missions(self) -> None:
        m1_filename = "missions/saved.m1.miz"
        m1 = dcs.Mission(terrain=dcs.terrain.Caucasus())
        m1_img_path = 'tests/images/m1/briefing.png'
        m1.add_picture_blue(m1_img_path)
        m1.save(m1_filename)

        m2_filename = "missions/saved.m2.miz"
        m2 = dcs.Mission(terrain=dcs.terrain.Caucasus())
        m2_img_path = 'tests/images/m2/briefing.png'
        m2.add_picture_blue(m2_img_path)
        m2.save(m2_filename)

        # verify that when a mission file is loaded
        # it creates a unique temp folders for it's
        # resources. If that's not true m2, which is loaded
        # last, would overwrite resources from m1, and if m1
        # is safed after m2 is loaded, it's resources
        # would not have the right content.

        m1 = dcs.Mission()
        m1.load_file(m1_filename)
        m2 = dcs.Mission()
        m2.load_file(m2_filename)

        self.assertNotEqual(m1.tmpdir, m2.tmpdir)
        self.assertNotEqual(list(m1.map_resource.files["DEFAULT"].values()),
                            list(m2.map_resource.files["DEFAULT"].values()))

    def test_empty_mission_with_coalitions(self) -> None:
        m = dcs.mission.Mission()
        m_filename = "tests/missions/countries-without-units-on-the-map.miz"
        m.load_file(m_filename)

        m_blue_countries = m.coalition['blue'].countries
        for country in ["Australia", "UK", "USA", "USSR"]:
            self.assertIn(country, m_blue_countries)
        self.assertEqual(len(m.coalition['blue'].countries["UK"].plane_group), 1)

        m_red_countries = m.coalition['red'].countries
        for country in ["Third Reich", "Bulgaria", "Romania", "Finland"]:
            self.assertIn(country, m_red_countries)

        m2_miz_filename = "missions/saved.countries-without-units-on-the-map.miz"
        m.save(m2_miz_filename)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_miz_filename)
        m2_blue_countries = m2.coalition['blue'].countries
        m2_red_countries = m2.coalition['red'].countries
        self.assertTrue(sorted(m_blue_countries.keys()), sorted(m2_blue_countries.keys()))
        self.assertTrue(sorted(m_red_countries.keys()), sorted(m2_red_countries.keys()))
        self.assertEqual(len(m.coalition['blue'].countries["UK"].plane_group),
                         len(m2.coalition['blue'].countries["UK"].plane_group))


    def test_smoke_action_carpet_bombing(self) -> None:

        # this is fictional enum to simplify addressing as defined
        # in big-formation-carpet-bombing.miz
        class FormationPosition(IntEnum):
            Leader = 0,
            Right = 1,
            Back = 2,
            Left = 3,

        def get_task(m: Mission, coalition: Coalition, country_name: str,
                     plane_group_idx: FormationPosition, point_idx: int, task_idx: int) -> Task:
            return m.coalition[coalition.value].country(
                country_name).plane_group[plane_group_idx].points[point_idx].tasks[task_idx]

        def get_carpetbombing_task(m: Mission, coalition: Coalition, country_name: str,
                                   plane_group_idx: FormationPosition, point_idx: int, task_idx: int) -> CarpetBombing:
            task = get_task(m, coalition, country_name, plane_group_idx, point_idx, task_idx)
            assert isinstance(task, CarpetBombing)
            return task

        m_name = "tests/missions/big-formation-carpet-bombing.miz"
        m = dcs.mission.Mission()
        m.load_file(m_name)

        m2_name = "missions/saved.big-formation-carpet-bombing.miz"
        m.save(m2_name)

        m2 = dcs.mission.Mission()
        m2.load_file(m2_name)

        coalition = Coalition.Blue
        country = "USA"

        def validate_formation(m: Mission, m2: Mission, position: FormationPosition, expend: Expend,
                               weapon_type: WeaponType, altitude_enabled: bool) -> None:
            point_idx = 2
            task_idx = 0

            m_task = get_carpetbombing_task(m, coalition, country, position, point_idx, task_idx)

            self.assertEqual(m_task.params["expend"], expend)
            self.assertEqual(m_task.params["weaponType"], weapon_type)
            self.assertEqual(m_task.params["altitudeEnabled"], altitude_enabled)

            m2_task = get_carpetbombing_task(m2, coalition, country, position, point_idx, task_idx)
            self.assertEqual(m_task, m2_task)

        validate_formation(m, m2, FormationPosition.Leader, Expend.Auto, WeaponType.Auto, True)
        validate_formation(m, m2, FormationPosition.Left, Expend.Four, WeaponType.IronBombs, False)
        validate_formation(m, m2, FormationPosition.Back, Expend.Auto, WeaponType.IronBombs, False)
        validate_formation(m, m2, FormationPosition.Right, Expend.Auto, WeaponType.Auto, False)
