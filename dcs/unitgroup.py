import math
import random
import copy
from enum import Enum
from typing import List, Union, Optional

from dcs.unit import Unit, Skill
from dcs.flyingunit import FlyingUnit, Plane, Helicopter
from dcs.unittype import FlyingType
from dcs.planes import PlaneType
from dcs.helicopters import HelicopterType
from dcs.point import StaticPoint, MovingPoint, PointAction, PointProperties
from dcs.translation import String
from dcs.terrain import Airport, Runway
from dcs.nav_target_point import NavTargetPoint
import dcs.planes as planes
import dcs.helicopters as helicopters
import dcs.triggers as triggers
import dcs.action as action
import dcs.condition as condition
import dcs.task as task
import dcs.mapping as mapping


class Group:
    class Formation(Enum):
        Line = 1
        Star = 2
        Rectangle = 3
        Scattered = 4
        Vee = 5

    def __init__(self, _id: int, name=None):
        if not isinstance(_id, int):
            raise TypeError("id must be an integer")
        self.id = _id
        self.hidden = False
        self.units = []  # type: List[Unit]
        self.points = []  # type: List[Union[StaticPoint, MovingPoint]]
        self.name = name if name else String()

    def __str__(self):
        return "Group: " + str(self.name)

    def load_from_dict(self, d):
        self.hidden = d.get("hidden")

    def add_unit(self, unit: Unit):
        self.units.append(unit)

    def add_point(self, point: StaticPoint):
        self.points.append(point)

    @property
    def x(self):
        if len(self.units) > 0:
            return self.units[0].position.x
        return None

    @property
    def y(self):
        if len(self.units) > 0:
            return self.units[0].position.y
        return None

    @property
    def position(self) -> mapping.Point:
        return self.units[0].position

    def formation_line(self, heading, distance=20):
        pos = self.units[0].position
        for i in range(1, len(self.units)):
            unit = self.units[i]
            unit.position = pos.point_from_heading(heading + 90, i * distance)
            unit.heading = heading

    def formation_star(self, heading, distance=20):
        pos = self.units[0].position
        units_count = len(self.units)
        iterations = math.ceil(units_count / 8)
        u_idx = 1
        for i in range(0, iterations):
            sx = pos.x - (i + 1) * distance
            sy = pos.y - (i + 1) * distance
            for j in range(0, 3):
                dx = distance * (i + 1) * j
                for k in range(0, 3):
                    dy = distance * (i + 1) * k
                    if u_idx >= units_count:
                        break
                    u = self.units[u_idx]
                    u.position.x = sx + dx
                    u.position.y = sy + dy
                    u.heading = heading

                    if not (j == 1 and k == 1):
                        u_idx += 1

    def formation_rectangle(self, heading, distance=20):
        units_count = len(self.units)
        size = math.ceil(math.sqrt(units_count))
        sx = self.units[0].position.x
        sy = self.units[0].position.y
        u_idx = 0
        for i in range(0, size):
            dx = distance * i
            for j in range(0, size):
                dy = distance * j
                if u_idx >= units_count:
                    break
                u = self.units[u_idx]
                u.position.x = sx - dx
                u.position.y = sy + dy
                u.heading = heading
                u_idx += 1

    def formation_scattered(self, heading=0, max_radius=None):
        unit_count = len(self.units)
        max_r = max_radius if max_radius else random.randrange(15, unit_count * 20)
        max_r = 15 if max_r < 15 else max_r
        start_pos = self.units[0].position

        for i in range(1, unit_count):
            while True:
                pos = start_pos.point_from_heading(random.randrange(0, 360), random.randrange(14, max_r))

                collision = False
                for j in range(0, i):
                    test_unit = self.units[j]
                    unit_rect = mapping.Rectangle.from_point(test_unit.position, 14)

                    if unit_rect.point_in_rect(pos):
                        collision = True

                if not collision:
                    u = self.units[i]
                    u.position = copy.copy(pos)
                    u.heading = heading
                    break
            i += 1

    def formation_vee(self, heading=0, distance=20):
        unit_count = len(self.units)
        size = math.ceil((unit_count - 1) / 2)

        start_pos = self.units[0].position

        u_idx = 1
        for i in range(0, size):
            self.units[u_idx].position = start_pos.point_from_heading(heading + 225, distance * (i + 1))
            self.units[u_idx].heading = self.units[0].heading

            u_idx += 1

            if u_idx <= unit_count:
                self.units[u_idx].position = start_pos.point_from_heading(heading - 225, distance * (i + 1))
                self.units[u_idx].heading = self.units[0].heading
                u_idx += 1

    def formation(self, _type=Formation.Line, heading=0):
        form_map = {
            VehicleGroup.Formation.Line: self.formation_line,
            VehicleGroup.Formation.Star: self.formation_star,
            VehicleGroup.Formation.Rectangle: self.formation_rectangle,
            VehicleGroup.Formation.Scattered: self.formation_scattered,
            VehicleGroup.Formation.Vee: self.formation_vee
        }

        form_map[_type](heading)

        return True

    def set_skill(self, skill: Skill):
        for u in self.units:
            u.skill = skill

    def dict(self):
        d = {
            "name": self.name.id,
            "groupId": self.id
        }
        if self.hidden is not None:
            d["hidden"] = self.hidden
        if self.units:
            d["x"] = self.units[0].position.x
            d["y"] = self.units[0].position.y
            d["units"] = {}
            i = 1
            for unit in self.units:
                d["units"][i] = unit.dict()
                dunit = d["units"][i]
                if len(self.points) > 1:
                    use_manual_heading = getattr(self, "manualHeading", False)
                    if not use_manual_heading:
                        hdg = self.points[0].position.heading_between_point(self.points[1].position)
                    else:
                        hdg = unit.heading
                    rhdg = math.radians(hdg)
                    dunit["heading"] = round(rhdg, 13)
                    if "psi" in dunit:
                        dunit["psi"] = round(rhdg * -1, 13)
                i += 1
        if self.points:
            d["route"] = {"points": {}}
            i = 1
            for point in self.points:
                d["route"]["points"][i] = point.dict()
                i += 1
        return d


class MovingGroup(Group):
    def __init__(self, _id, name=None, start_time=0):
        super(MovingGroup, self).__init__(_id, name)
        self.task = ""
        self.tasks = []
        self.start_time = start_time
        self.frequency = 251
        self.task_selected = True
        self.spawn_probability = 1.0
        self.late_activation = False

    def load_from_dict(self, d):
        super(MovingGroup, self).load_from_dict(d)
        self.frequency = d.get("frequency")
        self.task = d.get("task")  # ships don't have a task
        self.spawn_probability = d.get("probability", 1.0)
        for t in sorted(d.get("tasks", [])):
            task_dict = d["tasks"][t]
            self.tasks.append(task._create_from_dict(task_dict))

        self.task_selected = d.get("taskSelected", False)
        self.late_activation = d.get("lateActivation", False)

    def add_trigger_action(self, action: task.Task):
        self.tasks.append(action)

    def waypoint(self, name: str) -> Optional[MovingPoint]:
        for p in self.points:
            if p.name and str(p.name) == name:
                return p
        return None

    def dict(self):
        d = super(MovingGroup, self).dict()
        if self.task:
            d["task"] = self.task
        d["tasks"] = {i+1: self.tasks[i].dict() for i in range(0, len(self.tasks))}
        d["start_time"] = self.start_time
        if self.frequency:
            d["frequency"] = self.frequency
        if self.task_selected:
            d["taskSelected"] = self.task_selected
        if self.spawn_probability != 1.0:
            d["probability"] = self.spawn_probability
        if self.late_activation:
            d["lateActivation"] = self.late_activation
        return d


class VehicleGroup(MovingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(VehicleGroup, self).__init__(_id, name, start_time)
        self.task = "Ground Nothing"
        self.modulation = 0
        self.communication = False
        self.frequency = None
        self.visible = False  # visible before start flag
        self.spans = []
        self.manualHeading = False

    def load_from_dict(self, d):
        super(VehicleGroup, self).load_from_dict(d)
        self.modulation = d.get("modulation")
        self.communication = d.get("communication", False)
        self.visible = d.get("visible", False)
        self.manualHeading = d.get("manualHeading", False)

    def add_span(self, position: mapping.Point):
        self.spans.append({"x": position.x, "y": position.y})

    def add_waypoint(self, position: mapping.Point,
                     move_formation: PointAction=PointAction.OffRoad, speed=32) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = move_formation
        mp.position = copy.copy(position)
        mp.speed = speed / 3.6
        mp.ETA_locked = False

        self.add_point(mp)
        return mp

    def dict(self):
        d = super(VehicleGroup, self).dict()
        if self.communication:
            d["modulation"] = self.modulation
            d["communication"] = self.communication
            d["frequency"] = self.frequency
        d["visible"] = self.visible
        d["manualHeading"] = self.manualHeading
        if self.spans is not None:
            # spans
            d["route"]["spans"] = {}
            i = 1
            for spawn in self.spans:
                d["route"]["spans"][i] = spawn
                i += 1
        return d


class FlyingGroup(MovingGroup):

    def __init__(self, _id, name=None, start_time=0):
        super(FlyingGroup, self).__init__(_id, name, start_time)
        self.modulation = 0
        self.communication = True
        self.uncontrolled = False
        self.radio_set = False
        self.task = "CAS"
        self.units = []  # type: List[FlyingUnit]
        self.nav_target_points = []  # type: List[NavTargetPoint]

    def starts_from_airport(self) -> bool:
        return self.points[0].airdrome_id if self.points else False

    def airport_id(self) -> int:
        return self.points[0].airdrome_id if self.points else None

    def flight_type(self) -> FlyingType:
        t = planes.plane_map.get(self.units[0].type)
        if not t:
            t = helicopters.helicopter_map.get(self.units[0].type)
        return t

    def load_from_dict(self, d):
        super(FlyingGroup, self).load_from_dict(d)
        self.modulation = d.get("modulation")
        self.communication = d.get("communication", False)
        self.uncontrolled = d["uncontrolled"]
        self.radio_set = d.get("radioSet", False)
        self.nav_target_points = []
        for n in d.get("NavTargetPoints", []):
            nav_target_point_dict = d["NavTargetPoints"][n]
            self.nav_target_points.append(NavTargetPoint.create_from_dict(nav_target_point_dict))

    def add_nav_target_point(self, pos: mapping.Point, text_comment: str):
        nt = NavTargetPoint()
        nt.position = mapping.Point(pos.x, pos.y)
        nt.text_comment = text_comment
        nt.index = len(self.nav_target_points) + 1

        self.nav_target_points.append(nt)
        return nt

    def add_waypoint(self, pos: mapping.Point, altitude, speed=600, name: String=None) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = PointAction.TurningPoint
        mp.name = name if name else String()
        mp.position = mapping.Point(pos.x, pos.y)
        mp.alt = altitude
        mp.speed = speed / 3.6
        mp.ETA_locked = False
        mp.properties = PointProperties()

        self.add_point(mp)
        return mp

    def add_runway_waypoint(self, airport: Airport, runway: Runway=None,
                            distance=random.randrange(6000, 8000, 100)) -> MovingPoint:
        """Adds a waypoint parallel to the given runway heading, for start or approach.

        :param airport: start airport object
        :param runway: runway for heading direction, if None first(default) airport runway will be used.
        :param distance: distance of the waypoint from the airport
        :return: MovePoint object describing the waypoint
        """
        runway = runway if runway else airport.runways[0]

        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = PointAction.TurningPoint
        mp.alt_type = "RADIO"
        mp.position = airport.position.point_from_heading(runway.heading, distance)
        mp.alt = 300
        mp.speed = 200 / 3.6
        mp.ETA_locked = False
        mp.properties = PointProperties()

        self.add_point(mp)
        return mp

    def land_at(self, airport: Airport) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Land"
        mp.action = PointAction.Landing
        mp.position = copy.copy(airport.position)
        mp.airdrome_id = airport.id
        mp.alt = 0
        mp.speed = 0
        mp.ETA_locked = False
        mp.properties = PointProperties()

        self.add_point(mp)
        return mp

    def delay_start(self, mission, seconds):
        """Delay group to become active.

        Args:
            mission: The mission object, need to add trigger actions
            seconds: Seconds how long to delay the activation

        Returns:
            The Group itself
        """
        self.add_trigger_action(task.StartCommand())
        self.uncontrolled = True

        activate_trigger = triggers.TriggerContinious(comment="{name} delay trigger".format(name=self.name))
        activate_trigger.add_condition(condition.TimeAfter(seconds))
        activate_trigger.add_action(action.AITaskPush(self.id, 1))
        mission.triggerrules.triggers.append(activate_trigger)

        return self

    def load_task_default_loadout(self, task):
        task_payload = self.units[0].unit_type.loadout(task)
        if task_payload:
            for p in self.units:
                for x in task_payload:
                    p.load_pylon(x)

    def load_loadout(self, name: str):
        """Load a defined loadout from the mission editor.

        This method will try to load the given loadout name and set pylons of all units in the
        group accordingly.
        Args:
            name: Name of the loadout in the mission editor

        Returns:
            None
        """
        payload = self.units[0].unit_type.loadout_by_name(name)
        if payload:
            for p in self.units:
                p.pylons.clear()

                for x in payload:
                    p.load_pylon(x)

    def load_pylon(self, weapon, pylon=None):
        for u in self.units:
            u.load_pylon(weapon, pylon)

        return True

    def load_loadout_from_file(self, filename):
        for u in self.units:
            u.load_loadout(filename)

        return True

    def set_client(self):
        for u in self.units:
            u.set_client()

    def has_human(self):
        for u in self.units:
            if u.is_human():
                return True
        return False

    def reset_loadout(self):
        for u in self.units:
            u.reset_loadout()

    def set_frequency(self, frequency: float, radio_id: int = 1) -> None:
        """Sets the intra-flight frequency.

        This is equivalent to setting the frequency field of the aircraft group
        in the mission editor. The primary use is in determining which frequency
        an AI pilot will listen/transmit on for intra-flight communication.

        The first channel of the first compatible radio will automatically be
        set to this value by DCS. Any calls to
        FlyingUnit.set_radio_channel_preset for that radio will have no effect.

        Args:
            frequency: The intra-flight frequency to assign to the group.
            radio_id: The index of the radio that should be used for
                intra-flight communications. Typically it is okay to use the
                default value of 1, but for some cases (such as a VHF
                intra-flight channel for the F-16), another radio should be
                used.
        """
        self.frequency = frequency
        self.radio_set = True
        for u in self.units:
            if u.skill in [Skill.Client, Skill.Player]:
                u.set_radio_channel_preset(radio_id, 1, self.frequency)

    def dict(self):
        d = super(FlyingGroup, self).dict()
        d["modulation"] = self.modulation
        d["communication"] = self.communication
        d["uncontrolled"] = self.uncontrolled
        d["radioSet"] = self.radio_set

        if self.nav_target_points:
            d["NavTargetPoints"] = [n.dict() for n in self.nav_target_points]

        return d


class PlaneGroup(FlyingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(PlaneGroup, self).__init__(_id, name, start_time)

    def add_unit(self, unit: Plane):
        if not issubclass(unit.unit_type, PlaneType):
            print(unit.unit_type)
            raise TypeError("unit.unit_type is not a plane")
        super(PlaneGroup, self).add_unit(unit)


class HelicopterGroup(FlyingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(HelicopterGroup, self).__init__(_id, name, start_time)
        self.frequency = 127.5

    def add_unit(self, unit: Helicopter):
        if not issubclass(unit.unit_type, HelicopterType):
            raise TypeError("unit.unit_type is not a helicopter")
        super(HelicopterGroup, self).add_unit(unit)


class ShipGroup(MovingGroup):
    def __init__(self, _id, name=None, start_time=0):
        super(ShipGroup, self).__init__(_id, name, start_time)
        self.task = None
        self.frequency = None
        self.spans = None
        self.visible = False  # visible before start flag

    def add_waypoint(self, position: mapping.Point, speed=20) -> MovingPoint:
        mp = MovingPoint()
        mp.type = "Turning Point"
        mp.action = PointAction.TurningPoint
        mp.position = copy.copy(position)
        mp.speed = speed / 3.6
        mp.ETA_locked = False

        self.add_point(mp)
        return mp

    def set_frequency(self, frequency: int) -> None:
        """Sets the communications frequency for each unit in the group.

        Args:
            frequency: The frequency of the communications channel in hertz.
        """
        for unit in self.units:
            unit.set_frequency(frequency)

    def dict(self):
        d = super(ShipGroup, self).dict()
        d["visible"] = self.visible
        return d


class StaticGroup(Group):
    def __init__(self, _id, name=None):
        super(StaticGroup, self).__init__(_id, name)
        self.dead = False
        self.heading = 0
        self.link_offset: Optional[bool] = False

    def load_from_dict(self, d):
        super(StaticGroup, self).load_from_dict(d)
        self.heading = math.degrees(d["heading"])
        self.dead = d["dead"]
        self.link_offset = d.get("linkOffset")

    def dict(self):
        d = super(StaticGroup, self).dict()
        d["dead"] = self.dead
        d["heading"] = round(math.radians(self.heading), 13)
        if self.link_offset is not None:
            d["linkOffset"] = self.link_offset
        return d
