from __future__ import annotations

import copy
from typing import TYPE_CHECKING, List, Dict, Any
from enum import Enum, IntEnum

from dcs import mapping
from dcs import action
from dcs import condition

if TYPE_CHECKING:
    from dcs.terrain import Terrain


class TriggerColor(str, Enum):
    Red = "0xff0000ff"
    Green = "0x00ff00ff"
    Blue = "0x0000ffff"
    Yellow = "0x00ffffff"
    White = "0xffffffff"


class TriggerZoneType(IntEnum):
    Circular = 0
    QuadPoint = 2


class TriggerZone:
    def __init__(self, _id, position: mapping.Point, hidden=False, name="", color=None, properties=None, radius=1500):
        self.id = _id
        self.radius = radius
        self.position = copy.copy(position)
        self.hidden = hidden
        self.name = name
        self.color = color if color is not None else {1: 1, 2: 1, 3: 1, 4: 0.15}
        self.properties = properties if properties is not None else {}

    def dict(self):
        return {
            "name": self.name,
            "hidden": self.hidden,
            "x": self.position.x,
            "y": self.position.y,
            "zoneId": self.id,
            "radius": self.radius,
            "color": self.color,
            "properties": self.properties
        }


class TriggerZoneCircular(TriggerZone):
    def __init__(self, _id, position: mapping.Point, radius=1500, hidden=False, name="", color=None, properties=None):
        super(TriggerZoneCircular, self).__init__(_id, position, hidden, name, color, properties, radius)
        self.type = TriggerZoneType.Circular

    def dict(self):
        d = super(TriggerZoneCircular, self).dict()
        d["type"] = int(self.type)
        return d

    def __repr__(self):
        return "TriggerZoneCircular({id}, {x}, {y}, {r}, '{m}', '{n}', '{o}')".format(
            id=self.id, x=self.position.x, y=self.position.y, r=self.radius, m=self.name, n=self.color, o=self.properties
        )


# DCS mission format misspells the plural of "vertex". We follow this convention within PyDCS.
class TriggerZoneQuadPoint(TriggerZone):
    def __init__(self, _id, position: mapping.Point, verticies: List[mapping.Point],
                 hidden=False, name="", color=None, properties=None):
        super(TriggerZoneQuadPoint, self).__init__(_id, position, hidden, name, color, properties)
        self.type = TriggerZoneType.QuadPoint
        self.verticies = copy.copy(verticies)

    def dict(self):
        d = super(TriggerZoneQuadPoint, self).dict()
        d["type"] = int(self.type)
        i = 1
        d["verticies"] = {}
        for vertex in self.verticies:
            d["verticies"][i] = {"x": vertex.x, "y": vertex.y}
            i += 1
        return d

    def __repr__(self):
        return "TriggerZoneQuadPoint({id}, {x}, {y}, '{m}', '{n}', '{o}')".format(
            id=self.id,
            x=self.position.x,
            y=self.position.y,
            m=self.name,
            n=self.color,
            o=self.properties)


class Triggers:
    def __init__(self, terrain: Terrain) -> None:
        self._terrain = terrain
        self.current_zone_id = 0
        self._zones = []  # type: List[TriggerZone]

    def _make_circular(self, imp_zone) -> TriggerZoneCircular:
        tz = TriggerZoneCircular(
            imp_zone["zoneId"],
            mapping.Point(imp_zone["x"], imp_zone["y"], self._terrain),
            imp_zone["radius"],
            imp_zone["hidden"],
            imp_zone["name"],
            imp_zone["color"],
            imp_zone.get("properties", {})
        )
        return tz

    def _make_quad(self, imp_zone) -> TriggerZoneQuadPoint:
        verticies: List[mapping.Point] = []
        for v_idx in imp_zone["verticies"]:
            v = imp_zone["verticies"][v_idx]
            verticies.append(mapping.Point(v["x"],
                                           v["y"],
                                           self._terrain))
        tz = TriggerZoneQuadPoint(
            imp_zone["zoneId"],
            mapping.Point(imp_zone["x"], imp_zone["y"], self._terrain),
            verticies,
            imp_zone["hidden"],
            imp_zone["name"],
            imp_zone["color"],
            imp_zone.get("properties", {})
        )
        return tz

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        self.current_zone_id = 0
        self._zones = []
        for x in data["zones"]:
            imp_zone = data["zones"][x]
            if "type" in imp_zone:
                tz_type = TriggerZoneType(imp_zone["type"])
            else:
                tz_type = TriggerZoneType.Circular

            if tz_type not in (TriggerZoneType.Circular, TriggerZoneType.QuadPoint):
                raise ValueError("Invalid trigger zone type {}".format(tz_type))

            is_circle = tz_type == TriggerZoneType.Circular
            tz: TriggerZone = self._make_circular(imp_zone) if is_circle else self._make_quad(imp_zone)
            self._zones.append(tz)
            self.current_zone_id = max(self.current_zone_id, tz.id)

    def add_triggerzone(self,
                        position: mapping.Point,
                        radius=1500,
                        hidden=False,
                        name="",
                        color=None,
                        properties=None
                        ) -> TriggerZoneCircular:
        self.current_zone_id += 1

        tz = TriggerZoneCircular(self.current_zone_id, position, radius, hidden, name, color, properties)
        self._zones.append(tz)
        return tz

    def add_triggerzone_quad(self,
                             position: mapping.Point,
                             verticies: List[mapping.Point],
                             hidden=False,
                             name="",
                             color=None,
                             properties=None) -> TriggerZoneQuadPoint:
        self.current_zone_id += 1
        tz = TriggerZoneQuadPoint(self.current_zone_id, position, verticies,
                                  hidden, name, color, properties)
        self._zones.append(tz)
        return tz

    def clear(self):
        self._zones.clear()

    def zones(self) -> List[TriggerZone]:
        return self._zones

    def dict(self):
        return {
            "zones": {i + 1: self._zones[i].dict() for i in range(0, len(self._zones))}
        }


class Event(Enum):
    NoEvent = ""
    Destroy = "dead"
    Shot = "shot"
    Crash = "crash"
    Eject = "eject"
    Refuel = "refuel"
    PilotDead = "pilot dead"
    BaseCaptured = "base captured"
    TookControl = "took control"
    RefuelStop = "refuel stop"
    Failure = "failure"
    MissionStart = "mission start"


class TriggerRule:
    predicate: str

    def __init__(self, event: Event, comment: str):
        self.comment: str = comment
        self.color: str = TriggerColor.White
        self.eventlist: Event = event
        self.rules: List[condition.Condition] = []
        self.actions: List[action.Action] = []

    @classmethod
    def create_from_dict(cls, mission, d) -> 'TriggerRule':
        trig = cls(Event(d["eventlist"]), d["comment"])
        actions = d["actions"]
        for a in actions:
            action_ = action.actions_map[actions[a]["predicate"]].create_from_dict(actions[a], mission)
            trig.actions.append(action_)
        rules = d["rules"]
        for r in rules:
            rule = condition.condition_map[rules[r]["predicate"]].create_from_dict(rules[r], mission)
            trig.rules.append(rule)
        return trig

    def set_color(self, color):
        self.color = color
        return self

    def add_condition(self, cond: condition.Condition):
        self.rules.append(cond)

    def add_action(self, act: action.Action):
        self.actions.append(act)

    def action_str(self, idx):
        actionstr = ";".join([repr(x) for x in self.actions]) + ";"
        if self.predicate == TriggerOnce.predicate:
            if self.eventlist != Event.NoEvent:
                actionstr += ' mission.trig.events["' + str(self.eventlist.value) + '"][' + str(idx) + ']=nil;'
            else:
                actionstr += ' mission.trig.func[' + str(idx) + ']=nil;'
        return actionstr

    def func_str(self, start, idx):
        if self.eventlist == Event.NoEvent and (start and isinstance(self, TriggerStart)
                                                or (not start and not isinstance(self, TriggerStart))):
            if isinstance(self, TriggerCondition):
                return "if mission.trig.conditions[{idx}]() then if not mission.trig.flag[{idx}" \
                       "] then mission.trig.actions[{idx}](); mission.trig.flag[{idx}" \
                       "] = true;end; else mission.trig.flag[{idx}] = false; end;".format(idx=idx)
            else:
                return "if mission.trig.conditions[{idx}]() then mission.trig.actions[{idx}]() end".format(idx=idx)
        return None

    def events_str(self, event, idx):
        if self.eventlist == event:
            return "if mission.trig.conditions[{idx}]() then mission.trig.actions[{idx}]() end".format(idx=idx)

    def dict(self):
        return {
            "comment": self.comment,
            "colorItem": self.color,
            "eventlist": self.eventlist.value,
            "predicate": self.predicate,
            "rules": {i + 1: self.rules[i].dict() for i in range(0, len(self.rules))},
            "actions": {i + 1: self.actions[i].dict() for i in range(0, len(self.actions))}
        }

    def __repr__(self):
        return self.__class__.__name__ + '(' + str(self.dict()) + ')'


class TriggerOnce(TriggerRule):
    predicate = "triggerOnce"

    def __init__(self, event: Event = Event.NoEvent, comment=""):
        super(TriggerOnce, self).__init__(event, comment)


class TriggerContinious(TriggerRule):
    predicate = "triggerContinious"

    def __init__(self, event: Event = Event.NoEvent, comment=""):
        super(TriggerContinious, self).__init__(event, comment)


class TriggerStart(TriggerRule):
    predicate = "triggerStart"

    def __init__(self, event: Event = Event.NoEvent, comment=""):
        super(TriggerStart, self).__init__(event, comment)


class TriggerCondition(TriggerRule):
    predicate = "triggerFront"

    def __init__(self, event: Event = Event.NoEvent, comment=""):
        super(TriggerCondition, self).__init__(event, comment)


trigger_map = {
    TriggerOnce.predicate: TriggerOnce,
    TriggerContinious.predicate: TriggerContinious,
    TriggerCondition.predicate: TriggerCondition,
    TriggerStart.predicate: TriggerStart
}


class Rules:
    def __init__(self):
        self.triggers: List[TriggerRule] = []

    def load_from_dict(self, mission, d: Dict[Any, Any]):
        self.triggers.clear()
        sorted_keys = sorted(d.keys())
        for x in sorted_keys:
            self.triggers.append(trigger_map[d[x]["predicate"]].create_from_dict(mission, d[x]))

    def trig(self):
        d = {}
        d["conditions"] = {i + 1: condition.Condition.condition_str(self.triggers[i].rules)
                           for i in range(0, len(self.triggers))}
        d["actions"] = {i + 1: self.triggers[i].action_str(i + 1) for i in range(0, len(self.triggers))}
        d["func"] = {i + 1: self.triggers[i].func_str(False, i + 1) for i in range(0, len(self.triggers))
                     if self.triggers[i].func_str(False, i + 1)}
        d["funcStartup"] = {i + 1: self.triggers[i].func_str(True, i + 1) for i in range(0, len(self.triggers))
                            if self.triggers[i].func_str(True, i + 1)}
        d["customStartup"] = {}
        d["events"] = {}
        for e in Event:
            if e != Event.NoEvent:
                events = {i + 1: self.triggers[i].events_str(e, i + 1)
                          for i in range(0, len(self.triggers))
                          if self.triggers[i].events_str(e, i + 1)}
                if events:
                    d["events"][e.value] = events

        d["flag"] = {i + 1: True for i in range(0, len(self.triggers))}
        return d

    def trigrules(self):
        return {i + 1: self.triggers[i].dict() for i in range(0, len(self.triggers))}

    def __str__(self):
        return str(self.trig())
