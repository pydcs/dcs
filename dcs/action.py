from __future__ import annotations

from typing import Any, Dict, List, Type, Optional, TYPE_CHECKING
from dcs.lua.serialize import dumps
from dcs.translation import String, ResourceKey
from enum import Enum, IntEnum
import dcs.countries as countries

if TYPE_CHECKING:
    from .mission import Mission
    from .country import Country
    from .unitgroup import Group


class Action:
    def __init__(self, predicate: str) -> None:
        self.predicate = predicate
        self.params: List[Any] = []

    def __repr__(self) -> str:
        s = []
        for x in self.params:
            if isinstance(x, String):
                s.append("getValueDictByKey({})".format(dumps(x.id)))
            elif isinstance(x, ResourceKey):
                s.append("getValueResourceByKey({})".format(dumps(x.res_key)))
            else:
                s.append(dumps(x))
        return self.predicate + "(" + ", ".join(s) + ")"

    @classmethod
    def create_from_dict(cls, d, mission):
        raise NotImplementedError

    def dict(self) -> Dict[Any, Any]:
        d = {
            "predicate": self.predicate,
        }
        return d


class TextAction(Action):
    def __init__(self, predicate: str, text: String) -> None:
        super().__init__(predicate)
        self.text = text

    def dict(self) -> Dict[Any, Any]:
        d = super().dict()
        d["KeyDict_text"] = self.text.id
        d["text"] = self.text.id
        return d


class ActivateGroup(Action):
    predicate = "a_activate_group"

    def __init__(self, group=0):
        super(ActivateGroup, self).__init__(ActivateGroup.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"])

    def dict(self):
        d = super(ActivateGroup, self).dict()
        d["group"] = self.group
        return d


class AddRadioItem(Action):
    predicate = "a_add_radio_item"

    def __init__(self, radiotext=String(), flag=1, value=1):
        super(AddRadioItem, self).__init__(AddRadioItem.predicate)
        self.radiotext = radiotext
        self.params.append(self.radiotext)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(mission.translation.get_string(d["radiotext"]), d["flag"], d["value"])

    def dict(self):
        d = super(AddRadioItem, self).dict()
        d["radiotext"] = self.radiotext.id
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class AddRadioItemForCoalition(Action):
    predicate = "a_add_radio_item_for_coalition"

    def __init__(self, coalitionlist=all, radiotext=String(), flag=1, value=1):
        super(AddRadioItemForCoalition, self).__init__(AddRadioItemForCoalition.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.radiotext = radiotext
        self.params.append(self.radiotext)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["coalitionlist"], mission.translation.get_string(d["radiotext"]), d["flag"], d["value"])

    def dict(self):
        d = super(AddRadioItemForCoalition, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["radiotext"] = self.radiotext.id
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class AddRadioItemForGroup(Action):
    predicate = "a_add_radio_item_for_group"

    def __init__(self, group=0, radiotext=String(), flag=1, value=1):
        super(AddRadioItemForGroup, self).__init__(AddRadioItemForGroup.predicate)
        self.group = group
        self.params.append(self.group)
        self.radiotext = radiotext
        self.params.append(self.radiotext)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"], mission.translation.get_string(d["radiotext"]), d["flag"], d["value"])

    def dict(self):
        d = super(AddRadioItemForGroup, self).dict()
        d["group"] = self.group
        d["radiotext"] = self.radiotext.id
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class BeginPlayingActor(Action):
    predicate = "a_cockpit_push_actor"

    def __init__(self, number=1):
        super(BeginPlayingActor, self).__init__(BeginPlayingActor.predicate)
        self.number = number
        self.params.append(self.number)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["number"])

    def dict(self):
        d = super(BeginPlayingActor, self).dict()
        d["number"] = self.number
        return d


class ClearFlag(Action):
    predicate = "a_clear_flag"

    def __init__(self, flag=1):
        super(ClearFlag, self).__init__(ClearFlag.predicate)
        self.flag = flag
        self.params.append(self.flag)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["flag"])

    def dict(self):
        d = super(ClearFlag, self).dict()
        d["flag"] = self.flag
        return d


class CockpitHighlightElement(Action):
    predicate = "a_cockpit_highlight"

    def __init__(self, highlight_id=0, element_name="", size_of_box=0):
        super(CockpitHighlightElement, self).__init__(CockpitHighlightElement.predicate)
        self.highlight_id = highlight_id
        self.params.append(self.highlight_id)
        self.element_name = element_name
        self.params.append(self.element_name)
        self.size_of_box = size_of_box
        self.params.append(self.size_of_box)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["highlight_id"], d["element_name"], d["size_of_box"])

    def dict(self):
        d = super(CockpitHighlightElement, self).dict()
        d["highlight_id"] = self.highlight_id
        d["element_name"] = self.element_name
        d["size_of_box"] = self.size_of_box
        return d


class CockpitHighlightIndication(Action):
    predicate = "a_cockpit_highlight_indication"

    def __init__(self, highlight_id=0, indicator_id=0, element_name="", size_of_box=0):
        super(CockpitHighlightIndication, self).__init__(CockpitHighlightIndication.predicate)
        self.highlight_id = highlight_id
        self.params.append(self.highlight_id)
        self.indicator_id = indicator_id
        self.params.append(self.indicator_id)
        self.element_name = element_name
        self.params.append(self.element_name)
        self.size_of_box = size_of_box
        self.params.append(self.size_of_box)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["highlight_id"], d["indicator_id"], d["element_name"], d["size_of_box"])

    def dict(self):
        d = super(CockpitHighlightIndication, self).dict()
        d["highlight_id"] = self.highlight_id
        d["indicator_id"] = self.indicator_id
        d["element_name"] = self.element_name
        d["size_of_box"] = self.size_of_box
        return d


class CockpitHighlightPosition(Action):
    predicate = "a_cockpit_highlight_position"

    def __init__(
            self,
            highlight_id=0,
            in_cockpit_position_x=1,
            in_cockpit_position_y=0,
            in_cockpit_position_z=0,
            size_of_box_x=0.1,
            size_of_box_y=0.1,
            size_of_box_z=0.1):
        super(CockpitHighlightPosition, self).__init__(CockpitHighlightPosition.predicate)
        self.highlight_id = highlight_id
        self.params.append(self.highlight_id)
        self.in_cockpit_position_x = in_cockpit_position_x
        self.params.append(self.in_cockpit_position_x)
        self.in_cockpit_position_y = in_cockpit_position_y
        self.params.append(self.in_cockpit_position_y)
        self.in_cockpit_position_z = in_cockpit_position_z
        self.params.append(self.in_cockpit_position_z)
        self.size_of_box_x = size_of_box_x
        self.params.append(self.size_of_box_x)
        self.size_of_box_y = size_of_box_y
        self.params.append(self.size_of_box_y)
        self.size_of_box_z = size_of_box_z
        self.params.append(self.size_of_box_z)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(
            d["highlight_id"],
            d["in_cockpit_position_x"],
            d["in_cockpit_position_y"],
            d["in_cockpit_position_z"],
            d["size_of_box_x"],
            d["size_of_box_y"],
            d["size_of_box_z"])

    def dict(self):
        d = super(CockpitHighlightPosition, self).dict()
        d["highlight_id"] = self.highlight_id
        d["in_cockpit_position_x"] = self.in_cockpit_position_x
        d["in_cockpit_position_y"] = self.in_cockpit_position_y
        d["in_cockpit_position_z"] = self.in_cockpit_position_z
        d["size_of_box_x"] = self.size_of_box_x
        d["size_of_box_y"] = self.size_of_box_y
        d["size_of_box_z"] = self.size_of_box_z
        return d


class CockpitParamSaveAs(Action):
    predicate = "a_cockpit_param_save_as"

    def __init__(self, source="", destination=""):
        super(CockpitParamSaveAs, self).__init__(CockpitParamSaveAs.predicate)
        self.source = source
        self.params.append(self.source)
        self.destination = destination
        self.params.append(self.destination)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["source"], d["destination"])

    def dict(self):
        d = super(CockpitParamSaveAs, self).dict()
        d["source"] = self.source
        d["destination"] = self.destination
        return d


class CockpitPerformClickableAction(Action):
    predicate = "a_cockpit_perform_clickable_action"

    def __init__(self, cockpit_device=0, command=3001, value=0):
        super(CockpitPerformClickableAction, self).__init__(CockpitPerformClickableAction.predicate)
        self.cockpit_device = cockpit_device
        self.params.append(self.cockpit_device)
        self.command = command
        self.params.append(self.command)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["cockpit_device"], d["command"], d["value"])

    def dict(self):
        d = super(CockpitPerformClickableAction, self).dict()
        d["cockpit_device"] = self.cockpit_device
        d["command"] = self.command
        d["value"] = self.value
        return d


class CockpitRemoveHighlight(Action):
    predicate = "a_cockpit_remove_highlight"

    def __init__(self, highlight_id=0):
        super(CockpitRemoveHighlight, self).__init__(CockpitRemoveHighlight.predicate)
        self.highlight_id = highlight_id
        self.params.append(self.highlight_id)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["highlight_id"])

    def dict(self):
        d = super(CockpitRemoveHighlight, self).dict()
        d["highlight_id"] = self.highlight_id
        return d


class DeactivateGroup(Action):
    predicate = "a_deactivate_group"

    def __init__(self, group=0):
        super(DeactivateGroup, self).__init__(DeactivateGroup.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"])

    def dict(self):
        d = super(DeactivateGroup, self).dict()
        d["group"] = self.group
        return d


class DecreaseFlag(Action):
    predicate = "a_dec_flag"

    def __init__(self, flag=1, value=10):
        super(DecreaseFlag, self).__init__(DecreaseFlag.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["flag"], d["value"])

    def dict(self):
        d = super(DecreaseFlag, self).dict()
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class DoScript(TextAction):
    predicate = "a_do_script"

    def __init__(self, text: String = String()) -> None:
        super().__init__(DoScript.predicate, text)
        self.params.append(self.text)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "DoScript":
        return cls(mission.translation.get_string(d["text"]))


class DoScriptFile(Action):
    predicate = "a_do_script_file"

    def __init__(self, file_res_key: Optional[ResourceKey] = None):
        super(DoScriptFile, self).__init__(DoScriptFile.predicate)
        if file_res_key:
            self.file_res_key = file_res_key
            self.params.append(self.file_res_key)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(ResourceKey(d["file"]))

    def dict(self):
        d = super(DoScriptFile, self).dict()
        d["file"] = self.file_res_key.key
        return d


class EndMission(TextAction):
    predicate = "a_end_mission"

    def __init__(self, winner="", text: String = String()) -> None:
        super().__init__(EndMission.predicate, text)
        self.winner = winner
        self.params.append(self.winner)
        self.params.append(self.text)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "EndMission":
        return cls(d["winner"], mission.translation.get_string(d["text"]))

    def dict(self) -> Dict[Any, Any]:
        d = super().dict()
        d["winner"] = self.winner
        return d


class ExplodeUnit(Action):
    predicate = "a_explosion_unit"

    def __init__(self, unit="", volume=1000):
        super(ExplodeUnit, self).__init__(ExplodeUnit.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.volume = volume
        self.params.append(self.volume)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"], d["volume"])

    def dict(self):
        d = super(ExplodeUnit, self).dict()
        d["unit"] = self.unit
        d["volume"] = self.volume
        return d


class ExplodeWPMarker(Action):
    predicate = "a_explosion_marker"

    def __init__(self, zone="", altitude=1, color=0):
        super(ExplodeWPMarker, self).__init__(ExplodeWPMarker.predicate)
        self.zone = zone
        self.params.append(self.zone)
        self.altitude = altitude
        self.params.append(self.altitude)
        self.color = color
        self.params.append(self.color)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["zone"], d["altitude"], d["color"])

    def dict(self):
        d = super(ExplodeWPMarker, self).dict()
        d["zone"] = self.zone
        d["altitude"] = self.altitude
        d["color"] = self.color
        return d


class ExplodeWPMarkerOnUnit(Action):
    predicate = "a_explosion_marker_unit"

    def __init__(self, unit="", color=0):
        super(ExplodeWPMarkerOnUnit, self).__init__(ExplodeWPMarkerOnUnit.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.color = color
        self.params.append(self.color)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"], d["color"])

    def dict(self):
        d = super(ExplodeWPMarkerOnUnit, self).dict()
        d["unit"] = self.unit
        d["color"] = self.color
        return d


class Explosion(Action):
    predicate = "a_explosion"

    def __init__(self, zone="", altitude=1, volume=1000):
        super(Explosion, self).__init__(Explosion.predicate)
        self.zone = zone
        self.params.append(self.zone)
        self.altitude = altitude
        self.params.append(self.altitude)
        self.volume = volume
        self.params.append(self.volume)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["zone"], d["altitude"], d["volume"])

    def dict(self):
        d = super(Explosion, self).dict()
        d["zone"] = self.zone
        d["altitude"] = self.altitude
        d["volume"] = self.volume
        return d


class Smoke(Action):
    predicate = "a_effect_smoke"

    def __init__(self, zone="", density=1, preset=1):
        super(Smoke, self).__init__(Smoke.predicate)
        self.zone = zone
        self.params.append(self.zone)
        self.density = density
        self.params.append(self.density)
        self.preset = preset
        self.params.append(self.preset)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["zone"], d["density"], d["preset"])

    def dict(self):
        d = super(Smoke, self).dict()
        d["zone"] = self.zone
        d["density"] = self.density
        d["preset"] = self.preset
        return d


class FallInTemplate(Action):
    predicate = "a_fall_in_template"

    def __init__(self, group=0, template=""):
        super(FallInTemplate, self).__init__(FallInTemplate.predicate)
        self.group = group
        self.params.append(self.group)
        self.template = template
        self.params.append(self.template)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"], d["template"])

    def dict(self):
        d = super(FallInTemplate, self).dict()
        d["group"] = self.group
        d["template"] = self.template
        return d


class GroupAIOff(Action):
    predicate = "a_group_off"

    def __init__(self, group=0):
        super(GroupAIOff, self).__init__(GroupAIOff.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"])

    def dict(self):
        d = super(GroupAIOff, self).dict()
        d["group"] = self.group
        return d


class GroupAIOn(Action):
    predicate = "a_group_on"

    def __init__(self, group=0):
        super(GroupAIOn, self).__init__(GroupAIOn.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"])

    def dict(self):
        d = super(GroupAIOn, self).dict()
        d["group"] = self.group
        return d


class GroupResume(Action):
    predicate = "a_group_resume"

    def __init__(self, group=0):
        super(GroupResume, self).__init__(GroupResume.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"])

    def dict(self):
        d = super(GroupResume, self).dict()
        d["group"] = self.group
        return d


class GroupStop(Action):
    predicate = "a_group_stop"

    def __init__(self, group=0):
        super(GroupStop, self).__init__(GroupStop.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"])

    def dict(self):
        d = super(GroupStop, self).dict()
        d["group"] = self.group
        return d


class IlluminatingBomb(Action):
    predicate = "a_illumination_bomb"

    def __init__(self, zone="", altitude=1):
        super(IlluminatingBomb, self).__init__(IlluminatingBomb.predicate)
        self.zone = zone
        self.params.append(self.zone)
        self.altitude = altitude
        self.params.append(self.altitude)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["zone"], d["altitude"])

    def dict(self):
        d = super(IlluminatingBomb, self).dict()
        d["zone"] = self.zone
        d["altitude"] = self.altitude
        return d


class IncreaseFlag(Action):
    predicate = "a_inc_flag"

    def __init__(self, flag=1, value=10):
        super(IncreaseFlag, self).__init__(IncreaseFlag.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["flag"], d["value"])

    def dict(self):
        d = super(IncreaseFlag, self).dict()
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class LoadMission(Action):
    predicate = "a_load_mission"

    def __init__(self, file=""):
        super(LoadMission, self).__init__(LoadMission.predicate)
        self.file = file
        self.params.append(self.file)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["file"])

    def dict(self):
        d = super(LoadMission, self).dict()
        d["file"] = self.file
        return d


class Coalition(Enum):
    Blue = "blue"
    Red = "red"
    Neutral = "neutral"


class MarkToAll(TextAction):
    predicate = "a_mark_to_all"

    def __init__(self, value: int, zone: int, text: String = String(),
                 comment: String = String(), readonly: bool = True) -> None:
        super().__init__(MarkToAll.predicate, text)
        self.value = value
        self.params.append(self.value)
        self.zone = zone
        self.params.append(self.zone)
        self.params.append(self.text)
        self.comment = comment
        self.params.append(self.comment)
        self.readonly = readonly
        self.params.append(self.readonly)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "MarkToAll":
        return cls(d["value"], d["zone"], mission.translation.get_string(d["text"]),
                   mission.translation.get_string(d["comment"]), d["readonly"])

    def dict(self) -> Dict[Any, Any]:
        d = super().dict()
        d["value"] = self.value
        d["zone"] = self.zone
        d["comment"] = self.comment.id
        d["readonly"] = self.readonly
        return d


class MarkToCoalition(TextAction):
    predicate = "a_mark_to_coalition"

    def __init__(self, value: int, zone: int,
                 coalitionlist: Coalition = Coalition.Blue,
                 text: String = String(), comment: String = String(),
                 readonly: bool = True) -> None:
        super().__init__(MarkToCoalition.predicate, text)
        self.value = value
        self.params.append(self.value)
        self.zone = zone
        self.params.append(self.zone)
        if not isinstance(coalitionlist, Coalition):
            raise TypeError("Unexpected type for coalitionlist")
        self.coalitionlist = coalitionlist.value
        self.params.append(self.coalitionlist)
        self.params.append(self.text)
        self.comment = comment
        self.params.append(self.comment)
        self.readonly = readonly
        self.params.append(self.readonly)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "MarkToCoalition":
        return cls(d["value"], d["zone"], Coalition(d["coalitionlist"]),
                   mission.translation.get_string(d["text"]),
                   mission.translation.get_string(d["comment"]),
                   d["readonly"])

    def dict(self):
        d = super().dict()
        d["value"] = self.value
        d["zone"] = self.zone
        d["coalitionlist"] = self.coalitionlist
        d["comment"] = self.comment.id
        d["readonly"] = self.readonly
        return d


class MarkToGroup(TextAction):
    predicate = "a_mark_to_group"

    def __init__(self, value: int, zone: int, group: int = 0,
                 text: String = String(), comment: String = String(),
                 readonly: bool = True) -> None:
        super(MarkToGroup, self).__init__(MarkToGroup.predicate, text)
        self.value = value
        self.params.append(self.value)
        self.zone = zone
        self.params.append(self.zone)
        self.group = group
        self.params.append(self.group)
        self.params.append(self.text)
        self.comment = comment
        self.params.append(self.comment)
        self.readonly = readonly
        self.params.append(self.readonly)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "MarkToGroup":
        return cls(d["value"], d["zone"], d["group"], mission.translation.get_string(d["text"]),
                   mission.translation.get_string(d["comment"]), d["readonly"])

    def dict(self) -> Dict[Any, Any]:
        d = super().dict()
        d["value"] = self.value
        d["zone"] = self.zone
        d["group"] = self.group
        d["comment"] = self.comment.id
        d["readonly"] = self.readonly
        return d


class MessageToAll(TextAction):
    predicate = "a_out_text_delay"

    def __init__(self, text: String = String(), seconds: int = 10,
                 clearview: bool = False) -> None:
        super().__init__(MessageToAll.predicate, text)
        self.params.append(self.text)
        self.seconds = seconds
        self.params.append(self.seconds)
        self.clearview = clearview
        self.params.append(self.clearview)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "MessageToAll":
        return cls(mission.translation.get_string(d["text"]), d["seconds"],
                   d["clearview"])

    def dict(self) -> Dict[Any, Any]:
        d = super().dict()
        d["seconds"] = self.seconds
        d["clearview"] = self.clearview
        return d


class MessageToCoalition(TextAction):
    predicate = "a_out_text_delay_s"

    def __init__(self, coalitionlist: Coalition = Coalition.Blue,
                 text: String = String(), seconds: int = 10,
                 clearview: bool = False) -> None:
        super().__init__(MessageToCoalition.predicate, text)
        if not isinstance(coalitionlist, Coalition):
            raise TypeError("Unexpected type for coalitionlist")
        self.coalitionlist = coalitionlist.value
        self.params.append(self.coalitionlist)
        self.params.append(self.text)
        self.seconds = seconds
        self.params.append(self.seconds)
        self.clearview = clearview
        self.params.append(self.clearview)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any],
                         mission) -> "MessageToCoalition":
        return cls(Coalition(d["coalitionlist"]),
                   mission.translation.get_string(d["text"]), d["seconds"],
                   d["clearview"])

    def dict(self) -> Dict[Any, Any]:
        d = super(MessageToCoalition, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["seconds"] = self.seconds
        d["clearview"] = self.clearview
        return d


class MessageToCountry(TextAction):
    predicate = "a_out_text_delay_c"

    def __init__(self, countrylist: str = "", text: String = String(),
                 seconds: int = 10, clearview: bool = False) -> None:
        super().__init__(MessageToCountry.predicate, text)
        self.countrylist = countrylist
        self.params.append(self.countrylist)
        self.params.append(self.text)
        self.seconds = seconds
        self.params.append(self.seconds)
        self.clearview = clearview
        self.params.append(self.clearview)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "MessageToCountry":
        return cls(d["countrylist"], mission.translation.get_string(d["text"]),
                   d["seconds"], d["clearview"])

    def dict(self) -> Dict[Any, Any]:
        d = super(MessageToCountry, self).dict()
        d["countrylist"] = self.countrylist
        d["seconds"] = self.seconds
        d["clearview"] = self.clearview
        return d


class MessageToGroup(TextAction):
    predicate = "a_out_text_delay_g"

    def __init__(self, group: int = 0, text: String = String(),
                 seconds: int = 10, clearview: bool = False) -> None:
        super().__init__(MessageToGroup.predicate, text)
        self.group = group
        self.params.append(self.group)
        self.params.append(self.text)
        self.seconds = seconds
        self.params.append(self.seconds)
        self.clearview = clearview
        self.params.append(self.clearview)

    @classmethod
    def create_from_dict(cls, d: Dict[Any, Any], mission) -> "MessageToGroup":
        return cls(d["group"], mission.translation.get_string(d["text"]),
                   d["seconds"], d["clearview"])

    def dict(self):
        d = super(MessageToGroup, self).dict()
        d["group"] = self.group
        d["seconds"] = self.seconds
        d["clearview"] = self.clearview
        return d


class PlayArgument(Action):
    predicate = "a_play_argument"

    def __init__(self, object="", argument=0, start=0, stop=1, speed=1):
        super(PlayArgument, self).__init__(PlayArgument.predicate)
        self.object = object
        self.params.append(self.object)
        self.argument = argument
        self.params.append(self.argument)
        self.start = start
        self.params.append(self.start)
        self.stop = stop
        self.params.append(self.stop)
        self.speed = speed
        self.params.append(self.speed)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["object"], d["argument"], d["start"], d["stop"], d["speed"])

    def dict(self):
        d = super(PlayArgument, self).dict()
        d["object"] = self.object
        d["argument"] = self.argument
        d["start"] = self.start
        d["stop"] = self.stop
        d["speed"] = self.speed
        return d


class PreventControlsSynchronization(Action):
    predicate = "a_prevent_controls_synchronization"

    def __init__(self, value=False):
        super(PreventControlsSynchronization, self).__init__(PreventControlsSynchronization.predicate)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["value"])

    def dict(self):
        d = super(PreventControlsSynchronization, self).dict()
        d["value"] = self.value
        return d


class RadioTransmission(Action):
    predicate = "a_radio_transmission"

    def __init__(self, file="", zone="", modulation=False, loop=False, frequency=124000, power=100, name=""):
        super(RadioTransmission, self).__init__(RadioTransmission.predicate)
        self.file = file
        self.params.append(self.file)
        self.zone = zone
        self.params.append(self.zone)
        self.modulation = modulation
        self.params.append(self.modulation)
        self.loop = loop
        self.params.append(self.loop)
        self.frequency = frequency
        self.params.append(self.frequency)
        self.power = power
        self.params.append(self.power)
        self.name = name
        self.params.append(self.name)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["file"], d["zone"], d["modulation"], d["loop"], d["frequency"], d["power"], d["name"])

    def dict(self):
        d = super(RadioTransmission, self).dict()
        d["file"] = self.file
        d["zone"] = self.zone
        d["modulation"] = self.modulation
        d["loop"] = self.loop
        d["frequency"] = self.frequency
        d["power"] = self.power
        d["name"] = self.name
        return d


class RemoveRadioItem(Action):
    predicate = "a_remove_radio_item"

    def __init__(self, radiotext=String()):
        super(RemoveRadioItem, self).__init__(RemoveRadioItem.predicate)
        self.radiotext = radiotext
        self.params.append(self.radiotext)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(mission.translation.get_string(d["radiotext"]))

    def dict(self):
        d = super(RemoveRadioItem, self).dict()
        d["radiotext"] = self.radiotext.id
        return d


class RemoveRadioItemForCoalition(Action):
    predicate = "a_remove_radio_item_for_coalition"

    def __init__(self, coalitionlist=all, radiotext=String()):
        super(RemoveRadioItemForCoalition, self).__init__(RemoveRadioItemForCoalition.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.radiotext = radiotext
        self.params.append(self.radiotext)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["coalitionlist"], mission.translation.get_string(d["radiotext"]))

    def dict(self):
        d = super(RemoveRadioItemForCoalition, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["radiotext"] = self.radiotext.id
        return d


class RemoveRadioItemForGroup(Action):
    predicate = "a_remove_radio_item_for_group"

    def __init__(self, group=0, radiotext=String()):
        super(RemoveRadioItemForGroup, self).__init__(RemoveRadioItemForGroup.predicate)
        self.group = group
        self.params.append(self.group)
        self.radiotext = radiotext
        self.params.append(self.radiotext)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"], mission.translation.get_string(d["radiotext"]))

    def dict(self):
        d = super(RemoveRadioItemForGroup, self).dict()
        d["group"] = self.group
        d["radiotext"] = self.radiotext.id
        return d


class SetActiveHelperGateToPoint(Action):
    predicate = "a_route_gates_set_current_point"

    def __init__(self, unit="", number=1):
        super(SetActiveHelperGateToPoint, self).__init__(SetActiveHelperGateToPoint.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.number = number
        self.params.append(self.number)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"], d["number"])

    def dict(self):
        d = super(SetActiveHelperGateToPoint, self).dict()
        d["unit"] = self.unit
        d["number"] = self.number
        return d


class SetCommand(Action):
    predicate = "a_set_command"

    def __init__(self, command=0):
        super(SetCommand, self).__init__(SetCommand.predicate)
        self.command = command
        self.params.append(self.command)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["command"])

    def dict(self):
        d = super(SetCommand, self).dict()
        d["command"] = self.command
        return d


class SetCommandWithValue(Action):
    predicate = "a_set_command_with_value"

    def __init__(self, command=0, value=0):
        super(SetCommandWithValue, self).__init__(SetCommandWithValue.predicate)
        self.command = command
        self.params.append(self.command)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["command"], d["value"])

    def dict(self):
        d = super(SetCommandWithValue, self).dict()
        d["command"] = self.command
        d["value"] = self.value
        return d


class SetFailure(Action):
    predicate = "a_set_failure"

    def __init__(self, failure="", probability=100, random_pause=0):
        super(SetFailure, self).__init__(SetFailure.predicate)
        self.failure = failure
        self.params.append(self.failure)
        self.probability = probability
        self.params.append(self.probability)
        self.random_pause = random_pause
        self.params.append(self.random_pause)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["failure"], d["probability"], d["random_pause"])

    def dict(self):
        d = super(SetFailure, self).dict()
        d["failure"] = self.failure
        d["probability"] = self.probability
        d["random_pause"] = self.random_pause
        return d


class SetFlag(Action):
    predicate = "a_set_flag"

    def __init__(self, flag=1):
        super(SetFlag, self).__init__(SetFlag.predicate)
        self.flag = flag
        self.params.append(self.flag)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["flag"])

    def dict(self):
        d = super(SetFlag, self).dict()
        d["flag"] = self.flag
        return d


class SetFlagRandom(Action):
    predicate = "a_set_flag_random"

    def __init__(self, flag=1, min_value=0, max_value=100):
        super(SetFlagRandom, self).__init__(SetFlagRandom.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.min_value = min_value
        self.params.append(self.min_value)
        self.max_value = max_value
        self.params.append(self.max_value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["flag"], d["min_value"], d["max_value"])

    def dict(self):
        d = super(SetFlagRandom, self).dict()
        d["flag"] = self.flag
        d["min_value"] = self.min_value
        d["max_value"] = self.max_value
        return d


class SetFlagValue(Action):
    predicate = "a_set_flag_value"

    def __init__(self, flag=1, value=1):
        super(SetFlagValue, self).__init__(SetFlagValue.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["flag"], d["value"])

    def dict(self):
        d = super(SetFlagValue, self).dict()
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class SetInternalCargo(Action):
    predicate = "a_set_internal_cargo"

    def __init__(self, cargo_mass=100):
        super(SetInternalCargo, self).__init__(SetInternalCargo.predicate)
        self.cargo_mass = cargo_mass
        self.params.append(self.cargo_mass)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["cargo_mass"])

    def dict(self):
        d = super(SetInternalCargo, self).dict()
        d["cargo_mass"] = self.cargo_mass
        return d


class ShowHelperGate(Action):
    predicate = "a_show_helper_gate"

    def __init__(self, x=0, z=0, y=0, course=0):
        super(ShowHelperGate, self).__init__(ShowHelperGate.predicate)
        self.x = x
        self.params.append(self.x)
        self.z = z
        self.params.append(self.z)
        self.y = y
        self.params.append(self.y)
        self.course = course
        self.params.append(self.course)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["x"], d["z"], d["y"], d["course"])

    def dict(self):
        d = super(ShowHelperGate, self).dict()
        d["x"] = self.x
        d["z"] = self.z
        d["y"] = self.y
        d["course"] = self.course
        return d


class ShowHelperGatesForUnit(Action):
    predicate = "a_show_route_gates_for_unit"

    def __init__(self, unit="", flag=1):
        super(ShowHelperGatesForUnit, self).__init__(ShowHelperGatesForUnit.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.flag = flag
        self.params.append(self.flag)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"], d["flag"])

    def dict(self):
        d = super(ShowHelperGatesForUnit, self).dict()
        d["unit"] = self.unit
        d["flag"] = self.flag
        return d


class SignalFlare(Action):
    predicate = "a_signal_flare"

    def __init__(self, zone="", altitude=1, color=0, bearing=0):
        super(SignalFlare, self).__init__(SignalFlare.predicate)
        self.zone = zone
        self.params.append(self.zone)
        self.altitude = altitude
        self.params.append(self.altitude)
        self.color = color
        self.params.append(self.color)
        self.bearing = bearing
        self.params.append(self.bearing)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["zone"], d["altitude"], d["color"], d["bearing"])

    def dict(self):
        d = super(SignalFlare, self).dict()
        d["zone"] = self.zone
        d["altitude"] = self.altitude
        d["color"] = self.color
        d["bearing"] = self.bearing
        return d


class SignalFlareOnUnit(Action):
    predicate = "a_signal_flare_unit"

    def __init__(self, unit="", color=0, bearing=0):
        super(SignalFlareOnUnit, self).__init__(SignalFlareOnUnit.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.color = color
        self.params.append(self.color)
        self.bearing = bearing
        self.params.append(self.bearing)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"], d["color"], d["bearing"])

    def dict(self):
        d = super(SignalFlareOnUnit, self).dict()
        d["unit"] = self.unit
        d["color"] = self.color
        d["bearing"] = self.bearing
        return d


class SoundToAll(Action):
    predicate = "a_out_sound"

    def __init__(self, file_res_key: Optional[ResourceKey] = None):
        super(SoundToAll, self).__init__(SoundToAll.predicate)
        if file_res_key:
            self.file_res_key = file_res_key
            self.params.append(self.file_res_key)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(ResourceKey(d["file"]))

    def dict(self):
        d = super(SoundToAll, self).dict()
        d["file"] = self.file_res_key.key
        return d


class SoundToCoalition(Action):
    predicate = "a_out_sound_s"

    def __init__(self, coalitionlist="", file_res_key: Optional[ResourceKey] = None):
        super(SoundToCoalition, self).__init__(SoundToCoalition.predicate)
        self.coalitionlist = coalitionlist
        if file_res_key:
            self.params.append(self.coalitionlist)
            self.file_res_key = file_res_key
            self.params.append(self.file_res_key)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["coalitionlist"], ResourceKey(d["file"]))

    def dict(self):
        d = super(SoundToCoalition, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["file"] = self.file_res_key.key
        return d


class SoundToCountry(Action):
    predicate = "a_out_sound_c"

    def __init__(self, countrylist="", file_res_key: Optional[ResourceKey] = None):
        super(SoundToCountry, self).__init__(SoundToCountry.predicate)
        self.countrylist = countrylist
        if file_res_key:
            self.params.append(self.countrylist)
            self.file_res_key = file_res_key
            self.params.append(self.file_res_key)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["countrylist"], ResourceKey(d["file"]))

    def dict(self):
        d = super(SoundToCountry, self).dict()
        d["countrylist"] = self.countrylist
        d["file"] = self.file_res_key.key
        return d


class SoundToGroup(Action):
    predicate = "a_out_sound_g"

    def __init__(self, group=0, file_res_key: Optional[ResourceKey] = None):
        super(SoundToGroup, self).__init__(SoundToGroup.predicate)
        self.group = group
        if file_res_key:
            self.params.append(self.group)
            self.file_res_key = file_res_key
            self.params.append(self.file_res_key)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["group"], ResourceKey(d["file"]))

    def dict(self):
        d = super(SoundToGroup, self).dict()
        d["group"] = self.group
        d["file"] = self.file_res_key.key
        return d


class SoundToUnit(Action):
    predicate = "a_out_sound_u"

    def __init__(self, unit="", file_res_key: Optional[ResourceKey] = None):
        super(SoundToUnit, self).__init__(SoundToUnit.predicate)
        self.unit = unit
        if file_res_key:
            self.params.append(self.unit)
            self.file_res_key = file_res_key
            self.params.append(self.file_res_key)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"], ResourceKey(d["file"]))

    def dict(self):
        d = super(SoundToUnit, self).dict()
        d["unit"] = self.unit
        d["file"] = self.file_res_key.key
        return d


class StartListenCockpitEvent(Action):
    predicate = "a_start_listen_event"

    def __init__(self, event="", flag=1):
        super(StartListenCockpitEvent, self).__init__(StartListenCockpitEvent.predicate)
        self.event = event
        self.params.append(self.event)
        self.flag = flag
        self.params.append(self.flag)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["event"], d["flag"])

    def dict(self):
        d = super(StartListenCockpitEvent, self).dict()
        d["event"] = self.event
        d["flag"] = self.flag
        return d


class StartListenCommand(Action):
    predicate = "a_start_listen_command"

    def __init__(self, command=0, flag=1, hit_count=0, min_value=-1000000, max_value=1000000, cockpit_device=0):
        super(StartListenCommand, self).__init__(StartListenCommand.predicate)
        self.command = command
        self.params.append(self.command)
        self.flag = flag
        self.params.append(self.flag)
        self.hit_count = hit_count
        self.params.append(self.hit_count)
        self.min_value = min_value
        self.params.append(self.min_value)
        self.max_value = max_value
        self.params.append(self.max_value)
        self.cockpit_device = cockpit_device
        self.params.append(self.cockpit_device)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["command"], d["flag"], d["hit_count"], d["min_value"], d["max_value"], d["cockpit_device"])

    def dict(self):
        d = super(StartListenCommand, self).dict()
        d["command"] = self.command
        d["flag"] = self.flag
        d["hit_count"] = self.hit_count
        d["min_value"] = self.min_value
        d["max_value"] = self.max_value
        d["cockpit_device"] = self.cockpit_device
        return d


class StartPlayerSeatLock(Action):
    predicate = "a_cockpit_lock_player_seat"

    def __init__(self, number=1):
        super(StartPlayerSeatLock, self).__init__(StartPlayerSeatLock.predicate)
        self.number = number
        self.params.append(self.number)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["number"])

    def dict(self):
        d = super(StartPlayerSeatLock, self).dict()
        d["number"] = self.number
        return d


class StartWaitUserResponse(Action):
    predicate = "c_start_wait_for_user"

    def __init__(self, flag=1, flag_black=999):
        super(StartWaitUserResponse, self).__init__(StartWaitUserResponse.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.flag_black = flag_black
        self.params.append(self.flag_black)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["flag"], d["flag_black"])

    def dict(self):
        d = super(StartWaitUserResponse, self).dict()
        d["flag"] = self.flag
        d["flag_black"] = self.flag_black
        return d


class StopLastSound(Action):
    predicate = "a_out_sound_stop"

    def __init__(self, ):
        super(StopLastSound, self).__init__(StopLastSound.predicate)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls()

    def dict(self):
        d = super(StopLastSound, self).dict()

        return d


class StopPlayerSeatLock(Action):
    predicate = "a_cockpit_unlock_player_seat"

    def __init__(self, ):
        super(StopPlayerSeatLock, self).__init__(StopPlayerSeatLock.predicate)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls()

    def dict(self):
        d = super(StopPlayerSeatLock, self).dict()

        return d


class StopPlayingActor(Action):
    predicate = "a_cockpit_pop_actor"

    def __init__(self, ):
        super(StopPlayingActor, self).__init__(StopPlayingActor.predicate)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls()

    def dict(self):
        d = super(StopPlayingActor, self).dict()

        return d


class StopRadioTransmission(Action):
    predicate = "a_stop_radio_transmission"

    def __init__(self, name=""):
        super(StopRadioTransmission, self).__init__(StopRadioTransmission.predicate)
        self.name = name
        self.params.append(self.name)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["name"])

    def dict(self):
        d = super(StopRadioTransmission, self).dict()
        d["name"] = self.name
        return d


class StopWaitUserResponse(Action):
    predicate = "c_stop_wait_for_user"

    def __init__(self, ):
        super(StopWaitUserResponse, self).__init__(StopWaitUserResponse.predicate)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls()

    def dict(self):
        d = super(StopWaitUserResponse, self).dict()

        return d


class AITaskPush(Action):
    predicate = "a_ai_task"

    def __init__(self, groupid, task_index):
        super(AITaskPush, self).__init__(AITaskPush.predicate)
        self.groupid = groupid
        self.task_index = task_index
        self.params.extend([self.groupid, self.task_index])

    @classmethod
    def create_from_dict(cls, d, mission):
        values = list(d["ai_task"].values())
        return cls(values[0], values[1])

    def dict(self):
        d = super(AITaskPush, self).dict()
        d["ai_task"] = [self.groupid, self.task_index]
        return d


class AITaskSet(Action):
    predicate = "a_set_ai_task"

    def __init__(self, groupid, task_index):
        super(AITaskSet, self).__init__(AITaskSet.predicate)
        self.groupid = groupid
        self.task_index = task_index
        self.params.extend([self.groupid, self.task_index])

    @classmethod
    def create_from_dict(cls, d, mission):
        # Not sure if this used to be 0/1 in older missions, if
        # so this needs a conditional.
        return cls(d["set_ai_task"][1], d["set_ai_task"][2])

    def dict(self):
        d = super(AITaskSet, self).dict()
        d["set_ai_task"] = [self.groupid, self.task_index]
        return d


class UnitAIOff(Action):
    predicate = "a_unit_off"

    def __init__(self, unit=""):
        super(UnitAIOff, self).__init__(UnitAIOff.predicate)
        self.unit = unit
        self.params.append(self.unit)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"])

    def dict(self):
        d = super(UnitAIOff, self).dict()
        d["unit"] = self.unit
        return d


class UnitAIOn(Action):
    predicate = "a_unit_on"

    def __init__(self, unit=""):
        super(UnitAIOn, self).__init__(UnitAIOn.predicate)
        self.unit = unit
        self.params.append(self.unit)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"])

    def dict(self):
        d = super(UnitAIOn, self).dict()
        d["unit"] = self.unit
        return d


class UnitEmissionOff(Action):
    predicate = "a_unit_emission_off"

    def __init__(self, unit=""):
        super(UnitEmissionOff, self).__init__(UnitEmissionOff.predicate)
        self.unit = unit
        self.params.append(self.unit)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"])

    def dict(self):
        d = super(UnitEmissionOff, self).dict()
        d["unit"] = self.unit
        return d


class UnitEmissionOn(Action):
    predicate = "a_unit_emission_on"

    def __init__(self, unit=""):
        super(UnitEmissionOn, self).__init__(UnitEmissionOn.predicate)
        self.unit = unit
        self.params.append(self.unit)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["unit"])

    def dict(self):
        d = super(UnitEmissionOn, self).dict()
        d["unit"] = self.unit
        return d


class RemoveSceneObjectsMask(IntEnum):
    ALL = 0
    TREES_ONLY = 1
    OBJECTS_ONLY = 2


class RemoveSceneObjects(Action):
    predicate = "a_remove_scene_objects"

    def __init__(self, objects_mask: RemoveSceneObjectsMask = RemoveSceneObjectsMask.ALL, zone=""):
        super(RemoveSceneObjects, self).__init__(RemoveSceneObjects.predicate)
        self.objects_mask = objects_mask
        self.params.append(self.objects_mask)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(RemoveSceneObjectsMask(d["objects_mask"]), d["zone"])

    def dict(self):
        d = super(RemoveSceneObjects, self).dict()
        d["objects_mask"] = self.objects_mask.value
        d["zone"] = self.zone
        return d


class SceneryDestructionZone(Action):
    predicate = "a_scenery_destruction_zone"

    def __init__(self, destruction_level=100, zone=""):
        super(SceneryDestructionZone, self).__init__(SceneryDestructionZone.predicate)
        self.destruction_level = destruction_level
        self.params.append(self.destruction_level)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["destruction_level"], d["zone"])

    def dict(self):
        d = super(SceneryDestructionZone, self).dict()
        d["destruction_level"] = self.destruction_level
        d["zone"] = self.zone
        return d


class ZoneIncrementResize(Action):
    predicate = "a_zone_increment_resize"

    def __init__(self, zone="", meters=1000) -> None:
        super().__init__(ZoneIncrementResize.predicate)
        self.zone = zone
        self.params.append(self.zone)
        self.meters = meters
        self.params.append(self.meters)

    @classmethod
    def create_from_dict(cls, d, mission):
        return cls(d["zone"], d["meters"])

    def dict(self):
        d = super().dict()
        d["zone"] = self.zone
        d["meters"] = self.meters
        return d


class PictureAction(Action):

    class HorzAlignment(Enum):
        Left = "0"
        Center = "1"
        Right = "2"

        def __eq__(self, other: Any) -> bool:
            if isinstance(other, str):
                return self.value == other
            return self == other

    class VertAlignment(Enum):
        Top = "0"
        Center = "1"
        Bottom = "2"

        def __eq__(self, other: Any) -> bool:
            if isinstance(other, str):
                return self.value == other
            return self == other

    class SizeUnits(Enum):
        OriginalSize = "0"
        WindowSize = "1"

        def __eq__(self, other: Any) -> bool:
            if isinstance(other, str):
                return self.value == other
            return self == other

    def __init__(self, predicate: str, file_res_key: ResourceKey, seconds: int,
                 clearview: bool, start_delay: int,
                 horz_alignment: HorzAlignment, vert_alignment: VertAlignment,
                 size: int, size_units: SizeUnits) -> None:
        super().__init__(predicate)
        self.file_res_key = file_res_key
        self.seconds = seconds
        self.clearview = clearview
        self.start_delay = start_delay
        self.horz_alignment = horz_alignment
        self.vert_alignment = vert_alignment
        self.size_units = size_units
        self.size = size
        if size not in range(1, 101):
            raise ValueError

    def dict(self) -> Dict[str, Any]:
        d = super().dict()
        d["file"] = self.file_res_key.key
        d["seconds"] = self.seconds
        d["clearview"] = self.clearview
        d["start_delay"] = self.start_delay
        d["horzAlignment"] = self.horz_alignment
        d["vertAlignment"] = self.vert_alignment
        d["size_units"] = self.size_units
        d["size"] = self.size
        return d

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False


class PictureToAll(PictureAction):
    predicate = "a_out_picture"

    def __init__(self, file_res_key: ResourceKey, seconds: int,
                 clearview: bool, start_delay: int,
                 horz_alignment: PictureAction.HorzAlignment, vert_alignment: PictureAction.VertAlignment,
                 size: int, size_units: PictureAction.SizeUnits) -> None:
        super().__init__(predicate=self.predicate, file_res_key=file_res_key,
                         seconds=seconds, clearview=clearview,
                         start_delay=start_delay, horz_alignment=horz_alignment,
                         vert_alignment=vert_alignment, size=size, size_units=size_units)
        self.params = [self.file_res_key, seconds, clearview, start_delay,
                       horz_alignment, vert_alignment, size, size_units]

    @classmethod
    def create_from_dict(cls, d: Dict[str, Any], mission: Mission) -> PictureToAll:
        return cls(ResourceKey(d["file"]), d["seconds"], d["clearview"], d["start_delay"],
                   d["horzAlignment"], d["vertAlignment"], d["size"], d["size_units"])


class PictureToCoalition(PictureAction):
    predicate = "a_out_picture_s"

    def __init__(self, coalition: Coalition, file_res_key: ResourceKey, seconds: int,
                 clearview: bool, start_delay: int,
                 horz_alignment: PictureAction.HorzAlignment, vert_alignment: PictureAction.VertAlignment,
                 size: int, size_units: PictureAction.SizeUnits) -> None:
        super().__init__(predicate=self.predicate, file_res_key=file_res_key,
                         seconds=seconds, clearview=clearview,
                         start_delay=start_delay, horz_alignment=horz_alignment,
                         vert_alignment=vert_alignment, size=size, size_units=size_units)
        self.coalition = coalition
        self.params = [self.coalition, self.file_res_key, seconds, clearview,
                       start_delay, horz_alignment, vert_alignment, size, size_units]

    @classmethod
    def create_from_dict(cls, d: Dict[str, Any], mission: Mission) -> PictureToCoalition:
        return cls(d["coalitionlist"], ResourceKey(d["file"]), d["seconds"], d["clearview"], d["start_delay"],
                   d["horzAlignment"], d["vertAlignment"], d["size"], d["size_units"])

    def dict(self) -> Dict[str, Any]:
        d = super().dict()
        d["coalitionlist"] = self.coalition
        return d


class PictureToCountry(PictureAction):
    predicate = "a_out_picture_c"

    def __init__(self, country: Country, file_res_key: ResourceKey, seconds: int,
                 clearview: bool, start_delay: int,
                 horz_alignment: PictureAction.HorzAlignment, vert_alignment: PictureAction.VertAlignment,
                 size: int, size_units: PictureAction.SizeUnits) -> None:
        super().__init__(predicate=self.predicate, file_res_key=file_res_key,
                         seconds=seconds, clearview=clearview,
                         start_delay=start_delay, horz_alignment=horz_alignment,
                         vert_alignment=vert_alignment, size=size, size_units=size_units)
        self.country = country
        self.params = [self.country.id, self.file_res_key, seconds, clearview,
                       start_delay, horz_alignment, vert_alignment, size, size_units]

    @classmethod
    def create_from_dict(cls, d: Dict[str, Any], mission: Mission) -> PictureToCountry:
        return cls(countries.get_by_id(d["countrylist"]), ResourceKey(d["file"]),
                   d["seconds"], d["clearview"], d["start_delay"],
                   d["horzAlignment"], d["vertAlignment"], d["size"], d["size_units"])

    def dict(self) -> Dict[str, Any]:
        d = super().dict()
        d["countrylist"] = self.country.id
        return d


class PictureToGroup(PictureAction):
    predicate = "a_out_picture_g"

    def __init__(self, group: Group, file_res_key: ResourceKey, seconds: int,
                 clearview: bool, start_delay: int,
                 horz_alignment: PictureAction.HorzAlignment, vert_alignment: PictureAction.VertAlignment,
                 size: int, size_units: PictureAction.SizeUnits) -> None:
        super().__init__(predicate=self.predicate, file_res_key=file_res_key,
                         seconds=seconds, clearview=clearview,
                         start_delay=start_delay, horz_alignment=horz_alignment,
                         vert_alignment=vert_alignment, size=size, size_units=size_units)
        self.group = group
        self.params = [self.group.id, self.file_res_key, seconds, clearview,
                       start_delay, horz_alignment, vert_alignment, size, size_units]

    @classmethod
    def create_from_dict(cls, d: Dict[str, Any], mission: Mission) -> PictureToGroup:
        group = mission.find_group_by_id(d["group"])
        if group is None:
            raise RuntimeError("Group id {} found in PictureToGroup action, "
                               "but it does not exist in the mission.".format(d["group"]))
        return cls(group, ResourceKey(d["file"]), d["seconds"], d["clearview"], d["start_delay"],
                   d["horzAlignment"], d["vertAlignment"], d["size"], d["size_units"])

    def dict(self) -> Dict[str, Any]:
        d = super().dict()
        d["group"] = self.group.id
        return d


class PictureToUnit(PictureAction):
    predicate = "a_out_picture_u"

    def __init__(self, unit_id: int, file_res_key: ResourceKey, seconds: int,
                 clearview: bool, start_delay: int,
                 horz_alignment: PictureAction.HorzAlignment, vert_alignment: PictureAction.VertAlignment,
                 size: int, size_units: PictureAction.SizeUnits) -> None:
        super().__init__(predicate=self.predicate, file_res_key=file_res_key,
                         seconds=seconds, clearview=clearview,
                         start_delay=start_delay, horz_alignment=horz_alignment,
                         vert_alignment=vert_alignment, size=size, size_units=size_units)
        self.unit_id = unit_id
        self.params = [self.unit_id, self.file_res_key, seconds, clearview,
                       start_delay, horz_alignment, vert_alignment, size, size_units]

    @classmethod
    def create_from_dict(cls, d: Dict[str, Any], mission: Mission) -> PictureToUnit:
        return cls(d["unit"], ResourceKey(d["file"]), d["seconds"], d["clearview"], d["start_delay"],
                   d["horzAlignment"], d["vertAlignment"], d["size"], d["size_units"])

    def dict(self) -> Dict[str, Any]:
        d = super().dict()
        d["unit"] = self.unit_id
        return d


actions_map: Dict[str, Type[Action]] = {
    "a_activate_group": ActivateGroup,
    "a_add_radio_item": AddRadioItem,
    "a_add_radio_item_for_coalition": AddRadioItemForCoalition,
    "a_add_radio_item_for_group": AddRadioItemForGroup,
    "a_cockpit_push_actor": BeginPlayingActor,
    "a_clear_flag": ClearFlag,
    "a_cockpit_highlight": CockpitHighlightElement,
    "a_cockpit_highlight_indication": CockpitHighlightIndication,
    "a_cockpit_highlight_position": CockpitHighlightPosition,
    "a_cockpit_param_save_as": CockpitParamSaveAs,
    "a_cockpit_perform_clickable_action": CockpitPerformClickableAction,
    "a_cockpit_remove_highlight": CockpitRemoveHighlight,
    "a_deactivate_group": DeactivateGroup,
    "a_dec_flag": DecreaseFlag,
    "a_do_script": DoScript,
    "a_do_script_file": DoScriptFile,
    "a_end_mission": EndMission,
    "a_explosion_unit": ExplodeUnit,
    "a_explosion_marker": ExplodeWPMarker,
    "a_explosion_marker_unit": ExplodeWPMarkerOnUnit,
    "a_explosion": Explosion,
    "a_effect_smoke": Smoke,
    "a_fall_in_template": FallInTemplate,
    "a_group_off": GroupAIOff,
    "a_group_on": GroupAIOn,
    "a_group_resume": GroupResume,
    "a_group_stop": GroupStop,
    "a_illumination_bomb": IlluminatingBomb,
    "a_inc_flag": IncreaseFlag,
    "a_load_mission": LoadMission,
    "a_mark_to_all": MarkToAll,
    "a_mark_to_coalition": MarkToCoalition,
    "a_mark_to_group": MarkToGroup,
    "a_out_text_delay": MessageToAll,
    "a_out_text_delay_s": MessageToCoalition,
    "a_out_text_delay_c": MessageToCountry,
    "a_out_text_delay_g": MessageToGroup,
    "a_play_argument": PlayArgument,
    "a_prevent_controls_synchronization": PreventControlsSynchronization,
    "a_radio_transmission": RadioTransmission,
    "a_remove_radio_item": RemoveRadioItem,
    "a_remove_radio_item_for_coalition": RemoveRadioItemForCoalition,
    "a_remove_radio_item_for_group": RemoveRadioItemForGroup,
    "a_route_gates_set_current_point": SetActiveHelperGateToPoint,
    "a_set_command": SetCommand,
    "a_set_command_with_value": SetCommandWithValue,
    "a_set_failure": SetFailure,
    "a_set_flag": SetFlag,
    "a_set_flag_random": SetFlagRandom,
    "a_set_flag_value": SetFlagValue,
    "a_set_internal_cargo": SetInternalCargo,
    "a_show_helper_gate": ShowHelperGate,
    "a_show_route_gates_for_unit": ShowHelperGatesForUnit,
    "a_signal_flare": SignalFlare,
    "a_signal_flare_unit": SignalFlareOnUnit,
    "a_out_sound": SoundToAll,
    "a_out_sound_s": SoundToCoalition,
    "a_out_sound_c": SoundToCountry,
    "a_out_sound_g": SoundToGroup,
    "a_out_sound_u": SoundToUnit,
    "a_start_listen_event": StartListenCockpitEvent,
    "a_start_listen_command": StartListenCommand,
    "a_cockpit_lock_player_seat": StartPlayerSeatLock,
    "c_start_wait_for_user": StartWaitUserResponse,
    "a_out_sound_stop": StopLastSound,
    "a_cockpit_unlock_player_seat": StopPlayerSeatLock,
    "a_cockpit_pop_actor": StopPlayingActor,
    "a_stop_radio_transmission": StopRadioTransmission,
    "c_stop_wait_for_user": StopWaitUserResponse,
    "a_unit_off": UnitAIOff,
    "a_unit_on": UnitAIOn,
    "a_unit_emission_off": UnitEmissionOff,
    "a_unit_emission_on": UnitEmissionOn,
    "a_ai_task": AITaskPush,
    "a_set_ai_task": AITaskSet,
    "a_remove_scene_objects": RemoveSceneObjects,
    "a_scenery_destruction_zone": SceneryDestructionZone,
    "a_zone_increment_resize": ZoneIncrementResize,
    "a_out_picture": PictureToAll,
    "a_out_picture_s": PictureToCoalition,
    "a_out_picture_c": PictureToCountry,
    "a_out_picture_g": PictureToGroup,
    "a_out_picture_u": PictureToUnit,
}
