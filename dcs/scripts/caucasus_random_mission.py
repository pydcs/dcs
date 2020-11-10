import sys
import dcs
import dcs.mission
import dcs.task
import dcs.mapping
import dcs.point
from dcs.mapping import Point, Polygon
import dcs.terrain
import dcs.unittype
import dcs.vehicles
from dcs.countries import USA, Russia
import random
import argparse
import os
from typing import List, Tuple, Type


class BasicScenario:
    battle_zones = {
        "zugidi": Polygon([Point(-270285.71428571, 609257.14285714), Point(-264342.85714286, 614142.85714286),
                           Point(-257428.57142857, 619485.71428571), Point(-250857.14285714, 625171.42857143),
                           Point(-248342.85714286, 627457.14285714), Point(-244600, 628800),
                           Point(-238685.71428571, 635371.42857143), Point(-235257.14285714, 639942.85714285),
                           Point(-238685.71428571, 640771.42857143), Point(-239342.85714286, 642714.28571428),
                           Point(-235971.42857143, 644742.85714285), Point(-236600, 646142.85714285),
                           Point(-234085.71428571, 650142.85714285), Point(-239200, 656428.57142857),
                           Point(-249828.57142857, 653000), Point(-264400, 650000),
                           Point(-264828.57142857, 644171.42857142),
                           Point(-269885.71428571, 634542.85714285), Point(-273600, 635428.57142857),
                           Point(-273657.14285714, 642571.42857142), Point(-285771.42857143, 640828.57142857),
                           Point(-285800, 625514.28571428), Point(-279771.42857143, 625285.71428571),
                           Point(-273942.85714286, 629371.42857142), Point(-272428.57142857, 624828.57142857),
                           Point(-273342.85714286, 612285.71428571)]),
        "gori": Polygon([Point(-258542.85714286, 803857.14285714), Point(-258371.42857143, 805685.71428571),
                         Point(-264771.42857143, 808828.57142857), Point(-262342.85714286, 814571.42857143),
                         Point(-271342.85714286, 823057.14285714), Point(-282085.71428571, 837771.42857142),
                         Point(-283885.71428571, 853599.99999999), Point(-303228.57142857, 860571.42857142),
                         Point(-297314.28571429, 836971.42857142), Point(-291142.85714286, 819942.85714285),
                         Point(-292200, 805999.99999999), Point(-292142.85714286, 794714.28571428),
                         Point(-298371.42857143, 772085.71428571), Point(-288257.14285715, 772657.14285713),
                         Point(-277028.57142857, 785628.57142856), Point(-276685.71428572, 797399.99999999),
                         Point(-263771.42857143, 804914.28571428)])
    }

    air_zones = {
        "abkhazia": Polygon([Point(-187092.85714285, 460857.14285714), Point(-149378.57142856, 476285.71428571),
                             Point(-147664.28571428, 520000), Point(-175378.57142856, 599714.28571429),
                             Point(-174521.42857142, 644000), Point(-199664.28571428, 624000),
                             Point(-233949.99999999, 632857.14285714), Point(-271092.85714285, 596000)]),
        "nato": Polygon([Point(-283950, 568092.85714286), Point(-267949.99999999, 608950),
                         Point(-235092.85714285, 638950), Point(-208521.42857142, 672950),
                         Point(-225949.99999999, 738950), Point(-242521.42857142, 820950),
                         Point(-223092.85714285, 908857.14285714), Point(-283664.28571428, 953428.57142858),
                         Point(-389092.85714285, 904571.42857143), Point(-385092.85714285, 599714.28571429)]),
        "russia_west": Polygon([Point(-177092.85714285, 463428.57142857), Point(-33664.285714277, 224571.42857143),
                                Point(24621.428571437, 239714.28571429), Point(27192.857142866, 495714.28571429),
                                Point(-152235.7142857, 538571.42857143), Point(-146521.42857142, 474285.71428572)]),
        "russia_center": Polygon([Point(-154807.14285713, 539428.57142858), Point(-19664.285714275, 541714.28571429),
                                  Point(-20521.428571418, 688571.42857144), Point(-173949.99999999, 688857.14285715)]),
        "russia_east": Polygon([Point(-169949.99999999, 693714.28571429), Point(-24235.714285703, 694285.71428571),
                                Point(-94807.142857132, 945714.28571429), Point(-209949.99999999, 932571.42857143),
                                Point(-225092.85714285, 801142.85714286)])
    }

    red_force = {
        "Armor": {
            "Tank Platoon": (Russia.name, [
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90
            ]),
            "Tank Platoon 2": (Russia.name, [
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90,
                Russia.Vehicle.Armor.MBT_T_90
            ])
        },
        "LightArmor": {
            "Light Armor 01": (Russia.name, [
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3
            ]),
            "Light Armor 02": (Russia.name, [
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3
            ]),
            "Light Armor 03": (Russia.name, [
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3,
                Russia.Vehicle.Armor.IFV_BMP_3
            ])
        },
        "Artillery": {
            "Artillery": (Russia.name, [
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Artillery.SPH_2S1_Gvozdika,
                Russia.Vehicle.Unarmed.Transport_Ural_4320T,
                Russia.Vehicle.AirDefence.SAM_SA_19_Tunguska_2S6
            ])
        },
        "AirDefence": {
            "Air Defense": (Russia.name, [
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_LN_2P25,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_STR_9S91,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_LN_2P25,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_STR_9S91,
                Russia.Vehicle.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            ]),
            "Air Defense 02": (Russia.name, [
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_LN_2P25,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_STR_9S91,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_LN_2P25,
                Russia.Vehicle.AirDefence.SAM_SA_6_Kub_STR_9S91,
                Russia.Vehicle.Unarmed.CP_SKP_11_ATC_Mobile_Command_Post
            ])
        },
        "Supply": {
            "Russia Supply": (Russia.name, [
                Russia.Vehicle.Unarmed.Transport_GAZ_66,
                Russia.Vehicle.Unarmed.Fuel_Truck_ATZ_10,
                Russia.Vehicle.Unarmed.Transport_GAZ_3308,
                Russia.Vehicle.Unarmed.Transport_GAZ_3308,
                Russia.Vehicle.Unarmed.Transport_GAZ_3308
            ])
        }
    }

    blue_force = {
        "Armor": {
            "1st Tank Platoon 01": (USA.name, [
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams,
                USA.Vehicle.Armor.MBT_M1A2_Abrams
            ])
        },
        "LightArmor": {
            "1st Light Armor Brigade 01": (USA.name, [
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
                USA.Vehicle.Armor.IFV_M2A2_Bradley,
            ])
        },
        "Artillery": {
            "1st Artillery Corps 01": (USA.name, [
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Artillery.SPH_M109_Paladin,
                USA.Vehicle.Unarmed.HEMTT_TFFT,
                USA.Vehicle.AirDefence.SAM_Stinger_comm,
                USA.Vehicle.AirDefence.Stinger_MANPADS
            ])
        },
        "AirDefence": {
            "Air Defense Battery 01": (USA.name, [
                USA.Vehicle.Unarmed.APC_M1025_HMMWV,
                USA.Vehicle.Unarmed.APC_M1025_HMMWV,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097,
                USA.Vehicle.AirDefence.SAM_Avenger_M1097
            ])
        },
        "Supply": {
            "US Supply": (USA.name, [
                USA.Vehicle.Unarmed.Transport_M818,
                USA.Vehicle.Unarmed.Transport_M818,
                USA.Vehicle.Unarmed.Tanker_M978_HEMTT,
                USA.Vehicle.Unarmed.HEMTT_TFFT
            ])
        }
    }

    def __init__(self, hide=True):
        self.hide = hide
        self.m = dcs.Mission()

        self.m.coalition["red"].swap_country(self.m.coalition["blue"], dcs.countries.Ukraine.name)

        self.red_airports = []  # type: List[dcs.terrain.Airport]
        self.blue_airports = []  # type: List[dcs.terrain.Airport]
        self.setup_airports()

    def dynamic_weather(self, baricsystem: str):
        if baricsystem == "dyncyclone":
            self.m.weather.dynamic_weather(dcs.weather.Weather.BaricSystem.Cyclone, 2)
        elif baricsystem == "dynanti":
            self.m.weather.dynamic_weather(dcs.weather.Weather.BaricSystem.AntiCyclone, 2)
        elif baricsystem == "dynnone":
            self.m.weather.dynamic_weather(dcs.weather.Weather.BaricSystem.None_, 2)
        else:
            self.m.random_weather = True

    def daytime(self, period):
        self.m.random_date()
        self.m.random_daytime(period)

    def setup_airports(self):
        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus
        self.red_airports = caucasus.default_red_airports()
        for a in self.red_airports:
            self.setup_airport(a, "red", [dcs.vehicles.AirDefence.SAM_SA_19_Tunguska_2S6,
                                          dcs.vehicles.AirDefence.SPAAA_ZSU_23_4_Shilka])

        self.blue_airports = caucasus.default_blue_airports()
        for a in self.blue_airports:
            self.setup_airport(a, "blue", [dcs.vehicles.AirDefence.SAM_Avenger_M1097,
                                           dcs.vehicles.AirDefence.AAA_Vulcan_M163])

    def setup_airport(
            self,
            airport: dcs.terrain.Airport,
            side: str,
            air_def_units: List[Type[dcs.unittype.VehicleType]]):
        airport.set_coalition(side)

        if not airport.civilian:
            if airport.is_red():
                vg = dcs.templates.VehicleTemplate.Russia.sa10_site(self.m, airport.random_unit_zone().center(), 180)
                vg.hidden = self.hide
            elif airport.is_blue():
                dcs.templates.VehicleTemplate.USA.patriot_site(self.m, airport.random_unit_zone().center(), 330)
        else:
            slots = len(airport.parking_slots)
            airdef = int(round(random.random() + slots / 20, 0))
            if airdef:
                vg = self.m.vehicle_group(
                    self.m.country("Russia") if airport.is_red() else self.m.country("USA"),
                    airport.name + " Air Defense",
                    air_def_units[random.randrange(0, len(air_def_units))],
                    airport.random_unit_zone().random_point(), 180)
                if airport.is_red():
                    vg.hidden = self.hide

                for i in range(1, airdef):
                    _type = air_def_units[random.randrange(0, len(air_def_units))]
                    u = self.m.vehicle(airport.name + " Air Defense #" + str(i), _type)
                    vg.add_unit(u)
                vg.formation_scattered(random.randrange(0, 359))

        return airport

    def add_civil_airtraffic(self, planes=(10, 20), helicopters=(0, 10), hidden=True):
        p_count = random.randrange(planes[0], planes[1])
        h_count = random.randrange(helicopters[0], helicopters[1])

        c_count = 1

        def civil_flight(countries, airports):
            country_str = countries[random.randrange(0, len(countries))]
            country = self.m.country(country_str)

            airport = airports[random.randrange(0, len(airports))]

            transports = [x for x in country.planes if x.task_default == dcs.task.Transport]
            ptype = random.choice(transports)

            slots = airport.free_parking_slot(ptype)

            x = random.randrange(dcs.terrain.Caucasus.bounds.bottom + 100 * 1000,
                                 dcs.terrain.Caucasus.bounds.top - 100 * 1000)
            y = random.randrange(dcs.terrain.Caucasus.bounds.left + 600 * 1000,
                                 dcs.terrain.Caucasus.bounds.right - 130 * 1000)

            pos = dcs.mapping.Point(x, y)
            name = "Civil " + str(c_count)
            rand = random.random()
            if 0.3 < rand < 0.5 and slots:
                pg = self.m.flight_group_from_airport(
                    country, name, ptype, airport,
                    start_type=random.choice([dcs.mission.StartType.Cold, dcs.mission.StartType.Warm]))
                pg.add_runway_waypoint(airport, distance=random.randrange(6000, 8000, 100))
                pg.add_waypoint(pos, random.randrange(5000, 8000, 100), 400)
            elif 0.5 < rand and slots:
                pg = self.m.flight_group_from_airport(country, name, ptype, airport)
                pg.uncontrolled = True
            else:
                bound = dcs.mapping.Rectangle(dcs.terrain.Caucasus.bounds.top - 100 * 1000,
                                              dcs.terrain.Caucasus.bounds.left + 200 * 1000,
                                              dcs.terrain.Caucasus.bounds.bottom + 100 * 1000,
                                              dcs.terrain.Caucasus.bounds.right - 130 * 1000)
                point = bound.random_point()

                pg = self.m.flight_group_inflight(
                    country, name, ptype, point, random.randrange(5000, 8000, 100), 400
                )
                tmp = pg.add_waypoint(dcs.mapping.Point(0, 0), pg.points[0].alt)
                wp = pg.add_runway_waypoint(airport, distance=random.randrange(6000, 8000, 100))
                heading = wp.position.heading_between_point(point)
                tmp.position = wp.position.point_from_heading(heading, 30 * 1000)
                pg.land_at(airport)
            pg.set_frequency(240)
            return pg

        def heli_transport_flight(countries, airports: List[dcs.terrain.Airport]):
            country_str = countries[random.randrange(0, len(countries))]
            country = self.m.country(country_str)

            transports = [x for x in country.helicopters
                          if x.task_default == dcs.task.Transport]
            htype = random.choice(transports)

            start_airport = random.choice(airports)
            rand = random.random()
            name = "Helicopter Transport " + str(c_count)
            if 0.7 < rand:
                bound = dcs.mapping.Rectangle.from_point(start_airport.position, 100 * 1000)
                pos = bound.random_point()
                hg = self.m.flight_group_inflight(country, name, htype, pos, random.randrange(800, 1500, 100), 200)
                hg.add_runway_waypoint(start_airport)
                hg.land_at(start_airport)
            elif 0.4 < rand < 0.7:
                hg = self.m.flight_group_from_airport(country, name, htype, start_airport)
                hg.uncontrolled = True
            else:
                while True:
                    dest_airport = airports[random.randrange(0, len(airports))]
                    if dest_airport != start_airport:
                        break

                hg = self.m.flight_group_from_airport(
                    country, name, htype, start_airport, start_type=random.choice(list(dcs.mission.StartType))
                )
                hg.add_runway_waypoint(start_airport)
                hg.add_runway_waypoint(dest_airport)
                hg.land_at(dest_airport)
            return hg

        # red
        red_countries = [dcs.countries.Russia.name]
        for i in range(0, int(p_count / 2)):
            cf = civil_flight(red_countries, self.red_airports)
            cf.hidden = hidden
            cf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

        for i in range(0, int(h_count / 2)):
            hf = heli_transport_flight(red_countries, self.red_airports)
            hf.hidden = hidden
            hf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

        # blue
        blue_countries = [dcs.countries.USA.name, dcs.countries.Ukraine.name, dcs.countries.Georgia.name]
        for i in range(0, int(p_count / 2)):
            cf = civil_flight(blue_countries, self.blue_airports)
            cf.hidden = hidden
            cf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

        for i in range(0, int(h_count / 2)):
            hf = heli_transport_flight(blue_countries, self.blue_airports)
            hf.hidden = hidden
            hf.points[0].tasks.append(dcs.task.SetInvisibleCommand())
            c_count += 1

    def add_uncontrolled_military_planes(self, airports: List[dcs.terrain.Airport],
                                         planes: List[Tuple[str, Type[dcs.unittype.FlyingType], int]], hidden=True):

        g_idx = 1
        while planes:
            country, ptype, group_size = planes.pop()

            while True:
                airport = random.choice(airports)

                slots = airport.free_parking_slots(ptype)
                if len(slots) >= group_size:
                    break

            c = self.m.country(country)
            pg = self.m.flight_group_from_airport(c, ptype.id + " Flight #" + str(g_idx),
                                                  ptype, airport, parking_slots=slots, group_size=group_size)
            pg.uncontrolled = True
            pg.hidden = hidden
            g_idx += 1

    def place_players(self, start, aircraft_types: List[Tuple[str, str]],
                      airports: List[dcs.terrain.Airport],
                      group_size,
                      maintask,
                      placement_rect=None) -> List[dcs.unitgroup.FlyingGroup]:

        aircraft_groups = []  # type: List[dcs.unitgroup.FlyingGroup]
        name = "Airmaster "
        c = 1
        for _type in aircraft_types:
            country = self.m.country(_type[0])
            aircraft_type = _type[1]
            aircraft_type = dict(dcs.planes.plane_map, **dcs.helicopters.helicopter_map)[aircraft_type]

            airport = airports[random.randrange(0, len(airports))]
            if start == "inflight":
                rp = placement_rect.random_point() if placement_rect else dcs.mapping.Rectangle.from_point(
                    airport.position, 20 * 1000).random_point()
                altitude = random.randrange(300, 1000, 100) \
                    if aircraft_type.helicopter else random.randrange(2000, 5000, 100)
                pg = self.m.flight_group_inflight(
                    country, name + str(c), aircraft_type, rp, altitude,
                    maintask=maintask, group_size=group_size)
            else:
                pg = self.m.flight_group_from_airport(
                    country, name + str(c), aircraft_type, airport,
                    maintask=maintask, start_type=dcs.mission.StartType.from_string(start), group_size=group_size
                )
                pg.add_runway_waypoint(airport)
            aircraft_groups.append(pg)

            for u in pg.units:
                u.set_client()
            c += 1

        if group_size == 1:
            aircraft_groups[0].units[0].set_player()

        return aircraft_groups

    def save(self, filename, stats):
        self.m.save(filename)
        if stats:
            self.m.print_stats(self.m.stats())


class Refueling(BasicScenario):
    air_force = {
        "red": {
            "CAS": {
                "Hindis": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 10,
                    "type": dcs.helicopters.Mi_24V,
                    "loadout": "4x9M114, 80xS-8"
                },
                "Blackies": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 10,
                    "type": Russia.Helicopter.Ka_50,
                    "loadout": None
                }
            },
            "CAP": {
                "Mig 21": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 40,
                    "type": dcs.planes.MiG_21Bis,
                    "loadout": None
                },
                "Mig 15": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 20,
                    "type": dcs.planes.MiG_15bis,
                    "loadout": None
                },
                "Mig 29": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 70,
                    "type": dcs.planes.MiG_29A,
                    "loadout": None
                },
                "Su 33": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 80,
                    "type": dcs.planes.Su_33,
                    "loadout": "R-73*2,R-27ET*2,R-27ER*6,ECM"
                }
            }
        }
    }

    def __init__(self, aircraft_types: List[Tuple[str, str]], playercount: int, start: str, unhide):
        super(Refueling, self).__init__()

        self.add_civil_airtraffic(hidden=not unhide)

        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus

        usa = self.m.country(dcs.countries.USA.name)
        ukraine = self.m.country(dcs.countries.Ukraine.name)

        batumi = caucasus.batumi()
        vaziani = caucasus.vaziani()

        kutaisi = caucasus.kutaisi()
        kobuleti = caucasus.kobuleti()
        blue_military = [kutaisi, kobuleti]

        planes = [
            (dcs.countries.USA.name, dcs.countries.USA.Plane.F_16C_bl_52d, 4),
            (dcs.countries.USA.name, dcs.countries.USA.Plane.F_15E, 2),
            (dcs.countries.USA.name, dcs.countries.USA.Plane.F_A_18C, 4),
            (dcs.countries.Georgia.name, dcs.countries.Georgia.Plane.Su_25T, 4)
        ]

        self.add_uncontrolled_military_planes(blue_military, planes, False)

        frequency = 140
        orbit_rect = dcs.mapping.Rectangle(
            int(batumi.position.x + 120 * 1000),
            int(batumi.position.y - 100 * 1000),
            int(batumi.position.x),
            int(vaziani.position.y))

        pos, heading, race_dist = Refueling.random_orbit(orbit_rect)
        awacs = self.m.awacs_flight(
            usa,
            "AWACS",
            plane_type=dcs.planes.E_3A,
            airport=None,
            position=pos,
            race_distance=race_dist, heading=heading,
            altitude=random.randrange(4000, 5500, 100), frequency=frequency)

        self.m.escort_flight(usa, "AWACS Escort", dcs.countries.USA.Plane.F_15E, None, awacs, group_size=2)

        pos, heading, race_dist = Refueling.random_orbit(orbit_rect)
        refuel_net = self.m.refuel_flight(
            ukraine,
            "Tanker KC_130",
            dcs.planes.KC130,
            airport=None,
            position=pos,
            race_distance=race_dist, heading=heading,
            altitude=random.randrange(4000, 5500, 100), speed=750, frequency=frequency)

        pos, heading, race_dist = Refueling.random_orbit(orbit_rect)
        refuel_rod = self.m.refuel_flight(
            usa,
            "Tanker KC_135",
            dcs.planes.KC_135,
            airport=None,
            position=pos,
            race_distance=race_dist, heading=heading,
            altitude=random.randrange(4000, 5500, 100), frequency=frequency, tacanchannel="12X")

        i = 0
        for zone in ["russia_east", "russia_west"]:
            rcaps = list(self.air_force["red"]["CAP"].keys())
            rcap = self.air_force["red"]["CAP"][random.choice(rcaps)]
            cap_country = self.m.country(rcap["country"])
            p1, p2 = self.air_zones[zone].outbound_rectangle().resize(0.6).random_distant_points(80 * 1000)
            pf = self.m.patrol_flight(cap_country, cap_country.name + " CAP " + str(i), rcap["type"], None,
                                      p1, p2, group_size=rcap["size"])
            pf.hidden = not unhide
            if rcap["loadout"]:
                pf.load_loadout(rcap["loadout"])
            i += 1

        player_groups = self.place_players(start, aircraft_types, blue_military,
                                           placement_rect=orbit_rect,
                                           group_size=playercount, maintask=None)

        if start == "inflight":
            fuel_percent = 0.2
        else:
            fuel_percent = 0.3

        for pg in player_groups:
            airport = self.m.terrain.airport_by_id(pg.points[0].airdrome_id)
            if not airport:
                airport = random.choice(blue_military)

            for u in pg.units:
                u.fuel *= fuel_percent

            if pg.units[0].unit_type in [dcs.planes.A_10C]:
                pg.add_waypoint(refuel_rod.points[1].position, 4000)
            else:
                pg.add_waypoint(refuel_net.points[1].position, 4000)

            pg.add_runway_waypoint(airport)
            pg.land_at(airport)
            pg.load_loadout("Combat Air Patrol")

        goal = dcs.goals.Goal("home and alive")
        goal.rules.append(dcs.condition.UnitAlive(pg.units[0].id))
        tz = self.m.triggers.add_triggerzone(airport.position, 1000, name="home")
        goal.rules.append((dcs.condition.UnitInZone(pg.units[0].id, tz.id)))
        self.m.goals.add_offline(goal)

        self.m.set_sortie_text("Refuel your plane")
        self.m.set_description_text("""Random generated refueling test mission.
{count} {type} are/is prepared for a refueling training mission.""".format(
            count=playercount, type=", ".join([x[1] for x in aircraft_types])))
        self.m.set_description_bluetask_text("""Find your tanker and do a full refuel.
Afterwards land at your designated homebase.

AWACS and Tankers are reachable on {freq} Mhz VHF-AM.
KC-135 Tanker has TACAN 10X activated.""".format(freq=frequency))

    @staticmethod
    def random_orbit(rect: dcs.mapping.Rectangle):
        x1 = random.randrange(rect.bottom, rect.top)
        sy = rect.left
        y1 = random.randrange(sy, rect.right)
        heading = 90 if y1 < (sy + (rect.right - sy) / 2) else 270
        heading = random.randrange(heading - 20, heading + 20)
        race_dist = random.randrange(80 * 1000, 120 * 1000)
        return dcs.mapping.Point(x1, y1), heading, race_dist


class CAS(BasicScenario):
    air_force = {
        "blue": {
            "SEAD": {
                "SEAD 01": (USA.name, 2, dcs.planes.F_16C_bl_52d)
            },
            "CAP": {
                "Air Patrol": (USA.name, 2, dcs.planes.F_15C)
            },
            "CAS": {
                "AirCav": (USA.name, 2, dcs.helicopters.AH_64D)
            }
        },
        "red": {
            "CAS": {
                "Hindis": (Russia.name, 2, dcs.helicopters.Mi_24V)
            }
        }
    }

    nato_airspace = Polygon([
        Point(-272807.14285714, 563521.42857143), Point(-267949.99999999, 608950), Point(-235092.85714285, 638950),
        Point(-208521.42857142, 672950), Point(-225949.99999999, 738950), Point(-242521.42857142, 820950),
        Point(-243092.85714285, 912857.14285714), Point(-273949.99999999, 963714.28571429),
        Point(-415664.28571428, 963714.28571429), Point(-392807.14285714, 569142.85714286)])

    def __init__(self, aircraft_types: List[Tuple[str, str]], playercount: int, start: str, unhide):
        super(CAS, self).__init__(not unhide)

        caucasus = self.m.terrain  # type: dcs.terrain.Caucasus

        kutaisi = caucasus.kutaisi()
        kobuleti = caucasus.kobuleti()
        blue_military_airport = [kutaisi, kobuleti]

        red_military_airport = [caucasus.sochi_adler()]

        battle_point = BasicScenario.battle_zones["zugidi"].random_point()

        front_hdg = 30
        isred = False
        for force in [self.blue_force, self.red_force]:
            attack_hdg = (300 + (180 if isred else 0)) % 360
            defense_hdg = (attack_hdg + 180) % 360
            rp = battle_point.point_from_heading(defense_hdg, 7 * 1000)
            for force_type in force:
                for conf in force[force_type]:
                    dist_hdg = front_hdg if random.getrandbits(1) else front_hdg + 180
                    rp = rp.point_from_heading(dist_hdg, random.randrange(100, 1000))
                    if force_type in ["Artillery", "Supply"]:
                        rp = rp.point_from_heading(
                            random.randrange(defense_hdg - 30, defense_hdg + 30),
                            random.randrange(500, 3000))
                    else:
                        rp = rp.point_from_heading(
                            random.randrange(attack_hdg - 30, attack_hdg + 30),
                            random.randrange(0, 500))

                    plat = force[force_type][conf]
                    c = self.m.country(plat[0])
                    g = self.m.vehicle_group_platoon(c, conf, plat[1], rp)
                    g.formation_scattered(attack_hdg)
                    if isred:
                        g.hidden = self.hide

                    if force_type not in ["Artillery", "Supply"] and isred:
                        wp = g.add_waypoint(g.position.point_from_heading(attack_hdg, 12000))
                        wp.action = dcs.point.PointAction.Vee
                        g.add_waypoint(wp.position.point_from_heading(
                            random.randrange(attack_hdg - 10, attack_hdg + 30),
                            5000))

                    if force_type in ["Artillery"]:
                        for x in range(0, 10):
                            rect = dcs.mapping.Rectangle.from_point(
                                battle_point.point_from_heading(attack_hdg, 7000), 2000)
                            g.points[0].tasks.append(dcs.task.FireAtPoint(rect.random_point(), 30, 30))
            isred = True

        # rp = dcs.mapping.Rectangle.from_point(rp, 200).random_point()
        # fac = self.m.vehicle_group(usa, "FAC", USA.Vehicle.Armor.APC_M1126_Stryker_ICV, rp)
        # fac.points[0].tasks.append(dcs.task.EPLRS(1))
        # fac.points[0].tasks.append(dcs.task.FAC())
        # fac.points[0].tasks.append(dcs.task.SetInvisibleCommand())
        # fac.points[0].tasks.append(dcs.task.OptROE(dcs.task.OptROE.Values.WeaponHold))

        for air_force_idx in self.air_force:
            air_force = self.air_force[air_force_idx]
            airports = blue_military_airport if air_force_idx == "blue" else red_military_airport
            for force_type in air_force:
                for conf in air_force[force_type]:
                    conf_data = air_force[force_type][conf]
                    airport = random.choice(airports)
                    country = self.m.country(conf_data[0])
                    if force_type == "CAP":
                        nato_rect = self.nato_airspace.outbound_rectangle()
                        pp1, pp2 = nato_rect.random_distant_points(nato_rect.width() * 0.6)
                        self.m.patrol_flight(country, conf, conf_data[2], airport,
                                             pp1, pp2,
                                             group_size=conf_data[1])
                    else:
                        try:
                            pg = self.m.flight_group_from_airport(
                                country, conf, conf_data[2], airport, dcs.task.MainTask.map[force_type],
                                dcs.mission.StartType.Runway, group_size=conf_data[1]
                            )
                        except dcs.terrain.RunwayOccupiedError:
                            pg = self.m.flight_group_from_airport(
                                country, conf, conf_data[2], airport, dcs.task.MainTask.map[force_type],
                                dcs.mission.StartType.Warm, group_size=conf_data[1]
                            )
                        pg.add_runway_waypoint(airport)
                        if air_force_idx == "red":
                            pg.hidden = self.hide

                        if force_type in ["SEAD", "CAS"]:
                            pg.add_waypoint(battle_point, 1000)

        player_groups = self.place_players(start, aircraft_types, blue_military_airport, playercount, dcs.task.CAS)
        for pg in player_groups:
            pg.add_waypoint(battle_point, 0)

        self.m.set_sortie_text("Random CAS")
        self.m.set_description_text("""Random generated CAS test mission.""")
        self.m.set_description_bluetask_text("""Support your ground troops at waypoint 2.
Take care of enemy air defense.

2 F-16 are supporting you with a SEAD strike""")


class CAP(BasicScenario):
    air_force = {
        "red": {
            "CAS": {
                "Hindis": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 10,
                    "type": dcs.helicopters.Mi_24V,
                    "loadout": "4x9M114, 80xS-8"
                },
                "Blackies": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 10,
                    "type": Russia.Helicopter.Ka_50,
                    "loadout": None
                }
            },
            "CAP": {
                "Mig 21": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 40,
                    "type": dcs.planes.MiG_21Bis,
                    "loadout": None
                },
                "Mig 15": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 20,
                    "type": dcs.planes.MiG_15bis,
                    "loadout": None
                },
                "Mig 29": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 70,
                    "type": dcs.planes.MiG_29A,
                    "loadout": None
                },
                "Su 33": {
                    "country": Russia.name,
                    "size": 2,
                    "rating": 80,
                    "type": dcs.planes.Su_33,
                    "loadout": "R-73*2,R-27ET*2,R-27ER*6,ECM"
                }
            }
        }
    }

    def __init__(self, aircraft_types: List[Tuple[str, str]], playercount: int, start: str, unhide=False):
        super(CAP, self).__init__(not unhide)

        caucasus = self.m.terrain
        blue_military_airport = [caucasus.kobuleti(), caucasus.kutaisi()]

        player_groups = self.place_players(start, aircraft_types, blue_military_airport, playercount, dcs.task.CAP)
        patrol_zone = self.air_zones["nato"].outbound_rectangle().resize(0.7)
        p1, p2 = patrol_zone.random_distant_points(patrol_zone.width() * 0.6)
        for pg in player_groups:
            pg.load_loadout("Combat Air Patrol")
            pg.add_waypoint(p1, 5000)
            pg.add_waypoint(p2, 5000)

        vhf_am = 140

        usa = self.m.country("USA")
        ukraine = self.m.country(dcs.countries.Ukraine.name)
        race_dist = random.randrange(80 * 1000, 120 * 1000, 1000)
        p1, p2 = patrol_zone.random_distant_points(race_dist)
        p1.heading_between_point(p2)
        awacs = self.m.awacs_flight(
            usa,
            "AWACS",
            plane_type=dcs.planes.E_3A,
            airport=None,
            position=p1,
            race_distance=race_dist, heading=p1.heading_between_point(p2),
            altitude=random.randrange(4000, 5500, 100), frequency=vhf_am)

        self.m.escort_flight(usa, "AWACS Escort", dcs.countries.USA.Plane.F_15E,
                             None, awacs, dcs.mission.StartType.Warm)

        race_dist = random.randrange(80 * 1000, 120 * 1000, 1000)
        p1, p2 = patrol_zone.random_distant_points(race_dist)
        p1.heading_between_point(p2)
        self.m.refuel_flight(
            ukraine,
            "Tanker IL",
            dcs.planes.IL_78M,
            airport=None,
            position=p1,
            race_distance=race_dist, heading=p1.heading_between_point(p2),
            altitude=random.randrange(4000, 5500, 100), speed=750, frequency=vhf_am)

        i = 0
        for zone in ["russia_east", "russia_west"]:
            rcaps = list(self.air_force["red"]["CAP"].keys())
            rcap = self.air_force["red"]["CAP"][random.choice(rcaps)]
            cap_country = self.m.country(rcap["country"])
            p1, p2 = self.air_zones[zone].outbound_rectangle().resize(0.6).random_distant_points(80 * 1000)
            pf = self.m.patrol_flight(cap_country, cap_country.name + " CAP " + str(i), rcap["type"], None,
                                      p1, p2, group_size=rcap["size"])
            pf.hidden = not unhide
            if rcap["loadout"]:
                pf.load_loadout(rcap["loadout"])
            i += 1

        # for attack_type in self.air_force["red"].keys():
        for x in range(0, random.randrange(1, 3)):
            attack_type = random.choice(list(self.air_force["red"].keys()))
            af = self.air_force["red"][attack_type][random.choice(list(self.air_force["red"][attack_type].keys()))]
            spawn_rect = self.air_zones["russia_east"].outbound_rectangle()
            spawn_rect = dcs.mapping.Rectangle(spawn_rect.bottom + 40000, spawn_rect.left,
                                               spawn_rect.bottom, spawn_rect.right)
            att_country = self.m.country(af["country"])
            start_airport = caucasus.sochi() if af["type"].helicopter else random.choice(self.red_airports)
            attack_airport = random.choice(self.blue_airports)

            pos = attack_airport.position.point_from_heading(
                random.randrange(290, 410), 60 * 1000) if af["type"].helicopter else spawn_rect.random_point()
            attack_flight = self.m.flight_group(
                att_country,
                att_country.name + " " + attack_type,
                af["type"], None if start == "inflight" else start_airport, pos, random.randrange(2000, 4000, 100),
                maintask=dcs.task.MainTask.map[attack_type], group_size=af["size"])
            attack_flight.hidden = not unhide
            if attack_flight.starts_from_airport():
                attack_flight.add_runway_waypoint(start_airport)

            if af["loadout"]:
                attack_flight.load_loadout(af["loadout"])
            if attack_type == "CAS":
                wp = attack_flight.add_waypoint(attack_airport.position, 2000)
                wp.tasks.append(dcs.task.EngageTargetsInZone(attack_airport.position))
            else:
                attack_flight.add_waypoint(awacs.position, 6000)

            attack_flight.add_runway_waypoint(start_airport)
            attack_flight.land_at(start_airport)

        self.m.set_sortie_text("Random CAP")
        self.m.set_description_text("""Random generated CAP test mission.""")
        self.m.set_description_bluetask_text("""Protect your AWACS and Tanker

AWACS and tanker are reachable on VHF-AM {freq} Mhz.""".format(freq=vhf_am))


def main():

    types = [
        (dcs.countries.USA.name, dcs.planes.A_10C.id),
        (dcs.countries.Georgia.name, dcs.planes.Su_25T.id),
        (dcs.countries.USA.name, dcs.planes.M_2000C.id),
        (dcs.countries.USA.name, dcs.helicopters.Ka_50.id),
        (dcs.countries.USA.name, USA.Plane.MiG_21Bis.id)
    ]
    aircraft_types = [x[1] for x in types]
    parser = argparse.ArgumentParser(description="Random DCS mission generator")

    parser.add_argument("-a", "--aircrafttype", default=dcs.planes.Su_25T.id,
                        choices=aircraft_types,
                        help="Player aircraft type")
    parser.add_argument("-p", "--playercount", default=1, type=int)
    parser.add_argument("-s", "--start", default="inflight", choices=["inflight", "runway", "warm", "cold"])
    parser.add_argument("-t", "--missiontype", default="main", choices=["main", "CAS", "CAP", "refuel"])
    parser.add_argument("-d", "--daytime", choices=["random", "day", "night", "dusk", "dawn", "noon"], default="random")
    parser.add_argument(
        "-w", "--weather", choices=["dynamic", "dyncyclone", "dynanti", "dynone", "clear"], default="dynamic")
    parser.add_argument("-u", "--unhide", action="store_true", default=False, help="Show enemy pre mission")
    parser.add_argument("--show-stats", action="store_true", default=False, help="Show generated missions stats")
    parser.add_argument("-o", "--output", help="Name and path of the generated mission",
                        default=os.path.join(os.path.expanduser("~"), "Saved Games\\DCS\\Missions\\random.miz"))

    args = parser.parse_args()
    missiontype = args.missiontype
    if args.aircrafttype in [
            dcs.planes.Su_25T.id,
            dcs.helicopters.Ka_50.id,
            dcs.planes.A_10C.id] and args.missiontype == "main":
        missiontype = "CAS"
    if args.aircrafttype in [dcs.planes.M_2000C.id, dcs.planes.MiG_21Bis.id] and args.missiontype == "main":
        missiontype = "CAP"
    if args.aircrafttype == dcs.planes.A_10C.id:
        if args.missiontype not in ["CAS", "refuel"]:
            missiontype = "CAS"

    if missiontype == "refuel":
        supported = [dcs.planes.A_10C.id, dcs.planes.M_2000C.id]
        types = [x for x in types if x[1] in supported]\
            if args.playercount > 1 else [x for x in types if x[1] == args.aircrafttype]
        s = Refueling(types, args.playercount, args.start, args.unhide)
    elif missiontype == "CAS":
        types = types if args.playercount > 1 else [x for x in types if x[1] == args.aircrafttype]
        s = CAS(types, args.playercount, args.start, args.unhide)
    elif missiontype == "CAP":
        supported = [dcs.planes.M_2000C.id, dcs.planes.MiG_21Bis]
        types = [x for x in types if x[1] in supported]\
            if args.playercount > 1 else [x for x in types if x[1] == args.aircrafttype]
        s = CAP(types, args.playercount, args.start, args.unhide)
    else:
        raise NotImplementedError(missiontype + " not implemented")

    s.daytime(args.daytime)
    if args.weather == "dynamic":
        s.dynamic_weather(args.weather)
    s.save(args.output, args.show_stats)

    print("Mission created: " + args.output)
    return 0


if __name__ == '__main__':
    sys.exit(main())
