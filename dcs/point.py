from dcs.translation import String
import dcs.task as task
import dcs.mapping as mapping
from typing import List, Optional
from enum import Enum


class PointAction(Enum):
    None_ = ""
    TurningPoint = "Turning Point"
    FlyOverPoint = "Fly Over Point"
    FromParkingArea = "From Parking Area"
    FromParkingAreaHot = "From Parking Area Hot"
    FromRunway = "From Runway"
    Landing = "Landing"
    OnRoad = "On Road"
    OffRoad = "Off Road"
    LineAbreast = "Rank"
    Cone = "Cone"
    Vee = "Vee"
    Diamond = "Diamond"
    EchelonLeft = "EchelonL"
    EchelonRight = "EchelonR"
    FromGroundArea = "From Ground Area"
    FromGroundAreaHot = "From Ground Area Hot"
    Custom = "Custom"


class StaticPoint:
    def __init__(self):
        self.alt = 0
        self.type = ""
        self.name = String()
        self.position = mapping.Point(0, 0)
        self.speed = 0
        self.formation_template = ""
        self.action = PointAction.None_  # type: PointAction

    def load_from_dict(self, d, translation):
        self.alt = d["alt"]
        self.type = d["type"]
        self.position.x = d["x"]
        self.position.y = d["y"]
        self.action = PointAction(d["action"])
        self.formation_template = d["formation_template"]
        self.speed = d["speed"]
        self.name = translation.get_string(d["name"])

    def dict(self):
        return {
            "alt": self.alt,
            "type": self.type,
            "name": self.name.id,
            "x": self.position.x,
            "y": self.position.y,
            "speed": round(self.speed, 13),
            "formation_template": self.formation_template,
            "action": self.action.value
        }


class VNav(Enum):
    V2D = 0
    V3D = 1
    VNone = 2


class Scale(Enum):
    Enroute = 0
    Terminal = 1
    Approach = 2
    HighAcc = 3
    None_ = 4


class Steer(Enum):
    ToFrom = 0
    Direct = 1
    ToTo = 2
    None_ = 3


class PointProperties:
    def __init__(self, vnav: VNav = VNav.V2D, scale: Scale = Scale.Enroute, steer: Steer = Steer.ToTo, angle=None):
        self.vnav = vnav
        self.scale = scale
        self.steer = steer
        if angle is not None:
            self.angle = 1
            self.vangle = angle
        else:
            self.angle = 0
            self.vangle = 0

    def load_from_dict(self, d):
        self.vnav = VNav(d.get("vnav", VNav.VNone.value))
        self.scale = Scale(d.get("scale", Scale.None_.value))
        self.steer = Steer(d.get("steer", Steer.None_.value))
        self.angle = d.get("angle")
        self.vangle = d.get("vangle")

    def dict(self):
        return {
            "vnav": self.vnav.value,
            "scale": self.scale.value,
            "angle": self.angle,
            "vangle": self.vangle,
            "steer": self.steer.value
        }


class MovingPoint(StaticPoint):
    def __init__(self):
        super(MovingPoint, self).__init__()
        self.type = "Turning Point"
        self.action: PointAction = PointAction.TurningPoint
        self.alt_type = "BARO"
        self.ETA = 0
        self.ETA_locked = True
        self.speed_locked = True
        self.tasks: List[task.Task] = []
        self.properties: Optional[PointProperties] = None
        self.airdrome_id = None
        self.helipad_id = None
        self.link_unit = None

    def load_from_dict(self, d, translation):
        super(MovingPoint, self).load_from_dict(d, translation)
        self.alt_type = d.get("alt_type", None)
        self.ETA_locked = d["ETA_locked"]
        self.ETA = d["ETA"]
        self.speed_locked = d["speed_locked"]
        task_keys = sorted(d["task"]["params"]["tasks"].keys())
        for t in task_keys:
            self.tasks.append(task._create_from_dict(d["task"]["params"]["tasks"][t]))
        self.airdrome_id = d.get("airdromeId", None)
        self.helipad_id = d.get("helipadId", None)
        self.link_unit = d.get("linkUnit", None)
        if d.get("properties"):
            self.properties = PointProperties()
            self.properties.load_from_dict(d.get("properties"))
        else:
            self.properties = None

    def find_task(self, task_type):
        """Searches tasks in this point for the given task class

        :param task_type: task class to search, :py:mod:`dcs.task`
        :return: task instance if found, else None
        """
        for t in self.tasks:
            if isinstance(t, task_type):
                return t
        return None

    def add_task(self, task_: task.Task):
        self.tasks.append(task_)

    def dict(self):
        d = super(MovingPoint, self).dict()
        d["alt_type"] = self.alt_type
        d["ETA"] = self.ETA
        d["ETA_locked"] = self.ETA_locked
        d["speed_locked"] = self.speed_locked
        tasks = {}
        for i in range(0, len(self.tasks)):
            self.tasks[i].number = i+1
            tasks[i+1] = self.tasks[i].dict()
        d["task"] = {
            "id": "ComboTask",
            "params": {
                "tasks": {i+1: self.tasks[i].dict() for i in range(0, len(self.tasks))}
            }
        }
        if self.airdrome_id is not None:
            d["airdromeId"] = self.airdrome_id
        if self.helipad_id is not None:
            d["helipadId"] = self.helipad_id
        if self.link_unit is not None:
            d["linkUnit"] = self.link_unit
        if self.properties is not None:
            d["properties"] = self.properties.dict()
        return d
