from dcs.countries import Russia, USA
import dcs.unit as unit
from dcs.mission import Mission
import dcs.mapping as mapping
import dcs.vehicles


class VehicleTemplate:
    class Russia:
        @staticmethod
        def sa10_site(mission: Mission, position: mapping.Point, heading, prefix="", skill=unit.Skill.Average):
            russia = mission.country("Russia")
            vg = mission.vehicle_group(russia, prefix + "SA10 site",
                                       Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_CP_54K6, position, heading)
            u = mission.vehicle("Operator 1", Russia.Vehicle.Infantry.Infantry_Soldier_Rus)
            u.position = position.point_from_heading(heading + 180, 10)
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 3):  # 3 launchers
                u = mission.vehicle("launcher #" + str(i+1), Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_LN_5P85C)
                u.position = position.point_from_heading(heading + hdg, 50)
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            u = mission.vehicle("radar", Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_TR_30N6)
            u.position = position.point_from_heading(heading, 80)
            u.heading = heading
            vg.add_unit(u)

            u = mission.vehicle("radar", Russia.Vehicle.AirDefence.SAM_SA_10_S_300PS_SR_64H6E)
            u.position = position.point_from_heading(heading + 180, 100)
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill

            return vg

    class USA:
        @staticmethod
        def patriot_site(mission: Mission, position, heading, prefix="", skill=unit.Skill.Average):
            usa = mission.country("USA")
            vg = mission.vehicle_group(
                usa,
                prefix + "Patriot site",
                USA.Vehicle.AirDefence.SAM_Patriot_ICC,
                position,
                heading)
            u = mission.vehicle("Operator 1", USA.Vehicle.Infantry.Infantry_M4)
            u.position = position.point_from_heading(heading + 180, 5)
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 2):  # 2 launchers
                u = mission.vehicle("launcher #" + str(i+1), USA.Vehicle.AirDefence.SAM_Patriot_LN_M901)
                u.position = position.point_from_heading(heading + hdg, 50)
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            u = mission.vehicle("Electronic power plant", USA.Vehicle.AirDefence.SAM_Patriot_EPP_III)
            u.position = position.point_from_heading(heading + 180, 50)
            u.heading = heading
            vg.add_unit(u)

            u = mission.vehicle("radar", USA.Vehicle.AirDefence.SAM_Patriot_STR_AN_MPQ_53)
            u.position = position.point_from_heading(heading, 80)
            u.heading = heading
            vg.add_unit(u)

            inf = mission.vehicle("Operator 2", USA.Vehicle.Infantry.Infantry_M4)
            inf.position = position.point_from_heading(heading + 270, 5)
            vg.add_unit(inf)

            u = mission.vehicle("Antenna", USA.Vehicle.AirDefence.SAM_Patriot_AMG_AN_MRC_137)
            u.position = position.point_from_heading(heading + 180, 100)
            u.heading = heading
            vg.add_unit(u)

            u = mission.vehicle("ECS", USA.Vehicle.AirDefence.SAM_Patriot_ECS_AN_MSQ_104)
            u.position = position.point_from_heading(heading + 120, 80)
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill

        @staticmethod
        def hawk_site(mission: Mission, position, heading, prefix="", skill=unit.Skill.Average):
            usa = mission.country("USA")
            vg = mission.vehicle_group(
                usa,
                prefix + "Hawk site",
                USA.Vehicle.AirDefence.SAM_Hawk_PCP,
                position,
                heading)

            u = mission.vehicle("Operator 1", USA.Vehicle.Infantry.Infantry_M4)
            u.position = position.point_from_heading(heading + 180, 5)
            u.heading = heading
            vg.add_unit(u)

            hdg = 90
            for i in range(0, 2):  # 2 launchers
                u = mission.vehicle("launcher #" + str(i+1), USA.Vehicle.AirDefence.SAM_Hawk_LN_M192)
                u.position = position.point_from_heading(heading + hdg, 50)
                u.heading = heading
                vg.add_unit(u)
                hdg += 90

            u = mission.vehicle("Radar", USA.Vehicle.AirDefence.SAM_Hawk_SR_AN_MPQ_50)
            u.position = position.point_from_heading(heading + 180, 20)
            u.heading = heading
            vg.add_unit(u)

            inf = mission.vehicle("Operator 2", USA.Vehicle.Infantry.Infantry_M4)
            inf.position = position.point_from_heading(heading + 270, 5)
            vg.add_unit(inf)

            u = mission.vehicle("Tower", USA.Vehicle.AirDefence.SAM_Hawk_TR_AN_MPQ_46)
            u.position = position.point_from_heading(heading + 80, 80)
            u.heading = heading
            vg.add_unit(u)

            u = mission.vehicle("Wave Radar", USA.Vehicle.AirDefence.SAM_Hawk_CWAR_AN_MPQ_55)
            u.position = position.point_from_heading(heading + 180, 100)
            u.heading = heading
            vg.add_unit(u)

            for u in vg.units:
                u.skill = skill

    @staticmethod
    def sa11_site(mission, country, position, heading, prefix="", skill=unit.Skill.Average):
        vg = mission.vehicle_group(country, prefix + "SA11 site",
                                   dcs.vehicles.AirDefence.SAM_SA_11_Buk_CC_9S470M1, position, heading)

        u = mission.vehicle("Operator 1", Russia.Vehicle.Infantry.Infantry_Soldier_Rus)
        u.position = position.point_from_heading(heading + 180, 10)
        u.heading = heading
        vg.add_unit(u)

        hdg = 90
        for i in range(0, 2):  # 2 launchers
            u = mission.vehicle("launcher #" + str(i + 1), dcs.vehicles.AirDefence.SAM_SA_11_Buk_LN_9A310M1)
            u.position = position.point_from_heading(heading + hdg, 50)
            u.heading = heading
            vg.add_unit(u)
            hdg += 90

        u = mission.vehicle("radar", dcs.vehicles.AirDefence.SAM_SA_11_Buk_SR_9S18M1)
        u.position = position.point_from_heading(heading, 80)
        u.heading = heading
        vg.add_unit(u)

        for u in vg.units:
            u.skill = skill

        return vg

    @staticmethod
    def sa15_site(mission, country, position, heading, prefix="", skill=unit.Skill.Average):
        vg = mission.vehicle_group(country, prefix + "SA15 site",
                                   dcs.vehicles.AirDefence.CP_9S80M1_Sborka, position, heading)

        u = mission.vehicle("Operator 1", Russia.Vehicle.Infantry.Infantry_Soldier_Rus)
        u.position = position.point_from_heading(heading + 180, 10)
        u.heading = heading
        vg.add_unit(u)

        hdg = 90
        for i in range(0, 4):  # 4 tor vehicles
            u = mission.vehicle("tor #" + str(i + 1), dcs.vehicles.AirDefence.SAM_SA_15_Tor_9A331)
            u.position = position.point_from_heading(heading + hdg, 50)
            u.heading = heading
            vg.add_unit(u)
            hdg += 90

        for u in vg.units:
            u.skill = skill

        return vg

    @staticmethod
    def sa6_site(mission, country, position, heading, prefix="", skill=unit.Skill.Average):
        vg = mission.vehicle_group(
            country,
            prefix + "SA6 site",
            dcs.vehicles.AirDefence.SAM_SA_6_Kub_STR_9S91,
            position,
            heading
        )

        u = mission.vehicle("Launcher 1", dcs.vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25)
        u.position = position.point_from_heading(heading + 140, 30)
        u.heading = heading
        vg.add_unit(u)

        u = mission.vehicle("Launcher 2", dcs.vehicles.AirDefence.SAM_SA_6_Kub_LN_2P25)
        u.position = position.point_from_heading(heading + 210, 30)
        u.heading = heading
        vg.add_unit(u)

        u = mission.vehicle("Rearm Truck", dcs.vehicles.Unarmed.Transport_Ural_375)
        u.position = position.point_from_heading(heading + 0, 40)
        u.heading = heading
        vg.add_unit(u)

        for u in vg.units:
            u.skill = skill

        return vg


class ShipTemplate:
    @staticmethod
    def kuznetsov_taskgroup(mission: dcs.mission.Mission, position, heading, prefix="", skill=unit.Skill.Average):
        kuznetsov = mission.ship_group(mission.country("Russia"), prefix + " Kuznetsov Taskgroup",
                                       dcs.ships.CV_1143_5_Admiral_Kuznetsov, position, heading)
        kuznetsov.add_unit(mission.ship("Pyotr", dcs.ships.CGN_1144_2_Pyotr_Velikiy))
        kuznetsov.add_unit(mission.ship("Neystrahsimy 1", dcs.ships.FFG_11540_Neustrashimy))
        kuznetsov.add_unit(mission.ship("Neystrahsimy 2", dcs.ships.FFG_11540_Neustrashimy))
        kuznetsov.add_unit(mission.ship("Tanker 1", dcs.ships.Tanker_Elnya_160))
        kuznetsov.add_unit(mission.ship("Tanker 2", dcs.ships.Tanker_Elnya_160))
        kuznetsov.add_unit(mission.ship("Tanker 3", dcs.ships.Tanker_Elnya_160))

        for u in kuznetsov.units:
            u.skill = skill

        kuznetsov.formation_vee(heading, 800)

        return kuznetsov
