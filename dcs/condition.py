from dcs.lua.serialize import dumps


class Condition:
    def __init__(self, predicate):
        self.predicate = predicate
        self.params = []

    def __repr__(self):
        return self.predicate + "(" + ",".join(map(dumps, self.params)) + ")"

    def dict(self):
        d = {
            "predicate": self.predicate
        }
        return d


class AllOfCoalitionInZone(Condition):
    predicate = "c_all_of_coalition_in_zone"

    def __init__(self, coalitionlist, zone):
        super(AllOfCoalitionInZone, self).__init__(AllOfCoalitionInZone.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["zone"])

    def dict(self):
        d = super(AllOfCoalitionInZone, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["zone"] = self.zone
        return d


class AllOfCoalitionOutsideZone(Condition):
    predicate = "c_all_of_coalition_out_zone"

    def __init__(self, coalitionlist, zone):
        super(AllOfCoalitionOutsideZone, self).__init__(AllOfCoalitionOutsideZone.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["zone"])

    def dict(self):
        d = super(AllOfCoalitionOutsideZone, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["zone"] = self.zone
        return d


class AllOfGroupInZone(Condition):
    predicate = "c_all_of_group_in_zone"

    def __init__(self, group, zone):
        super(AllOfGroupInZone, self).__init__(AllOfGroupInZone.predicate)
        self.group = group
        self.params.append(self.group)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["group"], d["zone"])

    def dict(self):
        d = super(AllOfGroupInZone, self).dict()
        d["group"] = self.group
        d["zone"] = self.zone
        return d


class AllOfGroupOutsideZone(Condition):
    predicate = "c_all_of_group_out_zone"

    def __init__(self, group, zone):
        super(AllOfGroupOutsideZone, self).__init__(AllOfGroupOutsideZone.predicate)
        self.group = group
        self.params.append(self.group)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["group"], d["zone"])

    def dict(self):
        d = super(AllOfGroupOutsideZone, self).dict()
        d["group"] = self.group
        d["zone"] = self.zone
        return d


class ArgumentInRange(Condition):
    predicate = "c_argument_in_range"

    def __init__(self, argument, _min, _max):
        super(ArgumentInRange, self).__init__(ArgumentInRange.predicate)
        self.argument = argument
        self.params.append(self.argument)
        self._min = _min
        self.params.append(self._min)
        self._max = _max
        self.params.append(self._max)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["argument"], d["_min"], d["_max"])

    def dict(self):
        d = super(ArgumentInRange, self).dict()
        d["argument"] = self.argument
        d["_min"] = self._min
        d["_max"] = self._max
        return d


class BombInZone(Condition):
    predicate = "c_bomb_in_zone"

    def __init__(self, typebomb, numbombs, zone):
        super(BombInZone, self).__init__(BombInZone.predicate)
        self.typebomb = typebomb
        self.params.append(self.typebomb)
        self.numbombs = numbombs
        self.params.append(self.numbombs)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["typebomb"], d["numbombs"], d["zone"])

    def dict(self):
        d = super(BombInZone, self).dict()
        d["typebomb"] = self.typebomb
        d["numbombs"] = self.numbombs
        d["zone"] = self.zone
        return d


class CargoUnhookedInZone(Condition):
    predicate = "c_cargo_unhooked_in_zone"

    def __init__(self, cargo, zone):
        super(CargoUnhookedInZone, self).__init__(CargoUnhookedInZone.predicate)
        self.cargo = cargo
        self.params.append(self.cargo)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["cargo"], d["zone"])

    def dict(self):
        d = super(CargoUnhookedInZone, self).dict()
        d["cargo"] = self.cargo
        d["zone"] = self.zone
        return d


class CoalitionHasAirdrome(Condition):
    predicate = "c_coalition_has_airdrome"

    def __init__(self, coalitionlist, airdromelist):
        super(CoalitionHasAirdrome, self).__init__(CoalitionHasAirdrome.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.airdromelist = airdromelist
        self.params.append(self.airdromelist)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["airdromelist"])

    def dict(self):
        d = super(CoalitionHasAirdrome, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["airdromelist"] = self.airdromelist
        return d


class CoalitionHasHelipad(Condition):
    predicate = "c_coalition_has_helipad"

    def __init__(self, coalitionlist, helipadlist):
        super(CoalitionHasHelipad, self).__init__(CoalitionHasHelipad.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.helipadlist = helipadlist
        self.params.append(self.helipadlist)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["helipadlist"])

    def dict(self):
        d = super(CoalitionHasHelipad, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["helipadlist"] = self.helipadlist
        return d


class CockpitHighlightVisible(Condition):
    predicate = "c_cockpit_highlight_visible"

    def __init__(self, highlight_id):
        super(CockpitHighlightVisible, self).__init__(CockpitHighlightVisible.predicate)
        self.highlight_id = highlight_id
        self.params.append(self.highlight_id)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["highlight_id"])

    def dict(self):
        d = super(CockpitHighlightVisible, self).dict()
        d["highlight_id"] = self.highlight_id
        return d


class CockpitParamEqual(Condition):
    predicate = "c_cockpit_param_equal_to"

    def __init__(self, cockpit_param, value_text):
        super(CockpitParamEqual, self).__init__(CockpitParamEqual.predicate)
        self.cockpit_param = cockpit_param
        self.params.append(self.cockpit_param)
        self.value_text = value_text
        self.params.append(self.value_text)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["cockpit_param"], d["value_text"])

    def dict(self):
        d = super(CockpitParamEqual, self).dict()
        d["cockpit_param"] = self.cockpit_param
        d["value_text"] = self.value_text
        return d


class CockpitParamEqualToAnother(Condition):
    predicate = "c_cockpit_param_is_equal_to_another"

    def __init__(self, cockpit_param, cockpit_param2):
        super(CockpitParamEqualToAnother, self).__init__(CockpitParamEqualToAnother.predicate)
        self.cockpit_param = cockpit_param
        self.params.append(self.cockpit_param)
        self.cockpit_param2 = cockpit_param2
        self.params.append(self.cockpit_param2)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["cockpit_param"], d["cockpit_param2"])

    def dict(self):
        d = super(CockpitParamEqualToAnother, self).dict()
        d["cockpit_param"] = self.cockpit_param
        d["cockpit_param2"] = self.cockpit_param2
        return d


class CockpitParamInRange(Condition):
    predicate = "c_cockpit_param_in_range"

    def __init__(self, cockpit_param, _min2, _max2):
        super(CockpitParamInRange, self).__init__(CockpitParamInRange.predicate)
        self.cockpit_param = cockpit_param
        self.params.append(self.cockpit_param)
        self._min2 = _min2
        self.params.append(self._min2)
        self._max2 = _max2
        self.params.append(self._max2)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["cockpit_param"], d["_min2"], d["_max2"])

    def dict(self):
        d = super(CockpitParamInRange, self).dict()
        d["cockpit_param"] = self.cockpit_param
        d["_min2"] = self._min2
        d["_max2"] = self._max2
        return d


class FlagEquals(Condition):
    predicate = "c_flag_equals"

    def __init__(self, flag=1, value=10):
        super(FlagEquals, self).__init__(FlagEquals.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"], d["value"])

    def dict(self):
        d = super(FlagEquals, self).dict()
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class FlagEqualsFlag(Condition):
    predicate = "c_flag_equals_flag"

    def __init__(self, flag=1, flag2=1):
        super(FlagEqualsFlag, self).__init__(FlagEqualsFlag.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.flag2 = flag2
        self.params.append(self.flag2)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"], d["flag2"])

    def dict(self):
        d = super(FlagEqualsFlag, self).dict()
        d["flag"] = self.flag
        d["flag2"] = self.flag2
        return d


class FlagIsFalse(Condition):
    predicate = "c_flag_is_false"

    def __init__(self, flag=1):
        super(FlagIsFalse, self).__init__(FlagIsFalse.predicate)
        self.flag = flag
        self.params.append(self.flag)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"])

    def dict(self):
        d = super(FlagIsFalse, self).dict()
        d["flag"] = self.flag
        return d


class FlagIsLess(Condition):
    predicate = "c_flag_less"

    def __init__(self, flag=1, value=10):
        super(FlagIsLess, self).__init__(FlagIsLess.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"], d["value"])

    def dict(self):
        d = super(FlagIsLess, self).dict()
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class FlagIsLessThanFlag(Condition):
    predicate = "c_flag_less_flag"

    def __init__(self, flag=1, flag2=1):
        super(FlagIsLessThanFlag, self).__init__(FlagIsLessThanFlag.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.flag2 = flag2
        self.params.append(self.flag2)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"], d["flag2"])

    def dict(self):
        d = super(FlagIsLessThanFlag, self).dict()
        d["flag"] = self.flag
        d["flag2"] = self.flag2
        return d


class FlagIsMore(Condition):
    predicate = "c_flag_more"

    def __init__(self, flag=1, value=10):
        super(FlagIsMore, self).__init__(FlagIsMore.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.value = value
        self.params.append(self.value)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"], d["value"])

    def dict(self):
        d = super(FlagIsMore, self).dict()
        d["flag"] = self.flag
        d["value"] = self.value
        return d


class FlagIsTrue(Condition):
    predicate = "c_flag_is_true"

    def __init__(self, flag=1):
        super(FlagIsTrue, self).__init__(FlagIsTrue.predicate)
        self.flag = flag
        self.params.append(self.flag)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"])

    def dict(self):
        d = super(FlagIsTrue, self).dict()
        d["flag"] = self.flag
        return d


class GroupAlive(Condition):
    predicate = "c_group_alive"

    def __init__(self, group):
        super(GroupAlive, self).__init__(GroupAlive.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["group"])

    def dict(self):
        d = super(GroupAlive, self).dict()
        d["group"] = self.group
        return d


class GroupDead(Condition):
    predicate = "c_group_dead"

    def __init__(self, group):
        super(GroupDead, self).__init__(GroupDead.predicate)
        self.group = group
        self.params.append(self.group)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["group"])

    def dict(self):
        d = super(GroupDead, self).dict()
        d["group"] = self.group
        return d


class GroupLifeLess(Condition):
    predicate = "c_group_life_less"

    def __init__(self, group, percent=10):
        super(GroupLifeLess, self).__init__(GroupLifeLess.predicate)
        self.group = group
        self.params.append(self.group)
        self.percent = percent
        self.params.append(self.percent)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["group"], d["percent"])

    def dict(self):
        d = super(GroupLifeLess, self).dict()
        d["group"] = self.group
        d["percent"] = self.percent
        return d


class IndicationTextEqual(Condition):
    predicate = "c_indication_txt_equal_to"

    def __init__(self, indicator_id, element_name, element_value):
        super(IndicationTextEqual, self).__init__(IndicationTextEqual.predicate)
        self.indicator_id = indicator_id
        self.params.append(self.indicator_id)
        self.element_name = element_name
        self.params.append(self.element_name)
        self.element_value = element_value
        self.params.append(self.element_value)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["indicator_id"], d["element_name"], d["element_value"])

    def dict(self):
        d = super(IndicationTextEqual, self).dict()
        d["indicator_id"] = self.indicator_id
        d["element_name"] = self.element_name
        d["element_value"] = self.element_value
        return d


class MissionScoreHigher(Condition):
    predicate = "c_mission_score_higher"

    def __init__(self, coalitionlist, score=50):
        super(MissionScoreHigher, self).__init__(MissionScoreHigher.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.score = score
        self.params.append(self.score)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["score"])

    def dict(self):
        d = super(MissionScoreHigher, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["score"] = self.score
        return d


class MissionScoreLower(Condition):
    predicate = "c_mission_score_lower"

    def __init__(self, coalitionlist, score=50):
        super(MissionScoreLower, self).__init__(MissionScoreLower.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.score = score
        self.params.append(self.score)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["score"])

    def dict(self):
        d = super(MissionScoreLower, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["score"] = self.score
        return d


class Or(Condition):
    predicate = "or"

    def __init__(self, ):
        super(Or, self).__init__(Or.predicate)

    @classmethod
    def create_from_dict(cls, d):
        return cls()

    def dict(self):
        d = super(Or, self).dict()

        return d


class PartOfCoalitionInZone(Condition):
    predicate = "c_part_of_coalition_in_zone"

    def __init__(self, coalitionlist, zone, unit_type="ALL"):
        super(PartOfCoalitionInZone, self).__init__(PartOfCoalitionInZone.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.zone = zone
        self.params.append(self.zone)
        self.unitType = unit_type
        self.params.append(self.unitType)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["zone"], d["unitType"] if "unitType" in d.keys() else "ALL")

    def dict(self):
        d = super(PartOfCoalitionInZone, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["zone"] = self.zone
        d["unitType"] = self.unitType
        return d


class PartOfCoalitionOutsideZone(Condition):
    predicate = "c_part_of_coalition_out_zone"

    def __init__(self, coalitionlist, zone, unit_type="ALL"):
        super(PartOfCoalitionOutsideZone, self).__init__(PartOfCoalitionOutsideZone.predicate)
        self.coalitionlist = coalitionlist
        self.params.append(self.coalitionlist)
        self.zone = zone
        self.params.append(self.zone)
        self.unitType = unit_type
        self.params.append(self.unitType)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["coalitionlist"], d["zone"], d["unitType"] if "unitType" in d.keys() else "ALL")

    def dict(self):
        d = super(PartOfCoalitionOutsideZone, self).dict()
        d["coalitionlist"] = self.coalitionlist
        d["zone"] = self.zone
        d["unitType"] = self.unitType
        return d


class PartOfGroupInZone(Condition):
    predicate = "c_part_of_group_in_zone"

    def __init__(self, group, zone):
        super(PartOfGroupInZone, self).__init__(PartOfGroupInZone.predicate)
        self.group = group
        self.params.append(self.group)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["group"], d["zone"])

    def dict(self):
        d = super(PartOfGroupInZone, self).dict()
        d["group"] = self.group
        d["zone"] = self.zone
        return d


class PartOfGroupOutsideZone(Condition):
    predicate = "c_part_of_group_out_zone"

    def __init__(self, group, zone):
        super(PartOfGroupOutsideZone, self).__init__(PartOfGroupOutsideZone.predicate)
        self.group = group
        self.params.append(self.group)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["group"], d["zone"])

    def dict(self):
        d = super(PartOfGroupOutsideZone, self).dict()
        d["group"] = self.group
        d["zone"] = self.zone
        return d


class PlayerScoreLess(Condition):
    predicate = "c_player_score_less"

    def __init__(self, scores=100):
        super(PlayerScoreLess, self).__init__(PlayerScoreLess.predicate)
        self.scores = scores
        self.params.append(self.scores)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["scores"])

    def dict(self):
        d = super(PlayerScoreLess, self).dict()
        d["scores"] = self.scores
        return d


class PlayerScoreMore(Condition):
    predicate = "c_player_score_more"

    def __init__(self, scores=100):
        super(PlayerScoreMore, self).__init__(PlayerScoreMore.predicate)
        self.scores = scores
        self.params.append(self.scores)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["scores"])

    def dict(self):
        d = super(PlayerScoreMore, self).dict()
        d["scores"] = self.scores
        return d


class Predicate(Condition):
    predicate = "c_predicate"

    def __init__(self, text):
        super(Predicate, self).__init__(Predicate.predicate)
        self.text = text
        self.params.append(self.text)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["text"])

    def dict(self):
        d = super(Predicate, self).dict()
        d["text"] = self.text
        return d


class Random(Condition):
    predicate = "c_random_less"

    def __init__(self, percent=10):
        super(Random, self).__init__(Random.predicate)
        self.percent = percent
        self.params.append(self.percent)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["percent"])

    def dict(self):
        d = super(Random, self).dict()
        d["percent"] = self.percent
        return d


class SignalFlareInZone(Condition):
    predicate = "c_signal_flare_in_zone"

    def __init__(self, flare_color, numflares, zone):
        super(SignalFlareInZone, self).__init__(SignalFlareInZone.predicate)
        self.flare_color = flare_color
        self.params.append(self.flare_color)
        self.numflares = numflares
        self.params.append(self.numflares)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flare_color"], d["numflares"], d["zone"])

    def dict(self):
        d = super(SignalFlareInZone, self).dict()
        d["flare_color"] = self.flare_color
        d["numflares"] = self.numflares
        d["zone"] = self.zone
        return d


class TimeAfter(Condition):
    predicate = "c_time_after"

    def __init__(self, seconds=10):
        super(TimeAfter, self).__init__(TimeAfter.predicate)
        self.seconds = seconds
        self.params.append(self.seconds)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["seconds"])

    def dict(self):
        d = super(TimeAfter, self).dict()
        d["seconds"] = self.seconds
        return d


class TimeBefore(Condition):
    predicate = "c_time_before"

    def __init__(self, seconds=10):
        super(TimeBefore, self).__init__(TimeBefore.predicate)
        self.seconds = seconds
        self.params.append(self.seconds)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["seconds"])

    def dict(self):
        d = super(TimeBefore, self).dict()
        d["seconds"] = self.seconds
        return d


class TimeSinceFlag(Condition):
    predicate = "c_time_since_flag"

    def __init__(self, flag=1, seconds=10):
        super(TimeSinceFlag, self).__init__(TimeSinceFlag.predicate)
        self.flag = flag
        self.params.append(self.flag)
        self.seconds = seconds
        self.params.append(self.seconds)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["flag"], d["seconds"])

    def dict(self):
        d = super(TimeSinceFlag, self).dict()
        d["flag"] = self.flag
        d["seconds"] = self.seconds
        return d


class UnitAlive(Condition):
    predicate = "c_unit_alive"

    def __init__(self, unit):
        super(UnitAlive, self).__init__(UnitAlive.predicate)
        self.unit = unit
        self.params.append(self.unit)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"])

    def dict(self):
        d = super(UnitAlive, self).dict()
        d["unit"] = self.unit
        return d


class UnitAltitudeHigher(Condition):
    predicate = "c_unit_altitude_higher"

    def __init__(self, unit, altitude=1):
        super(UnitAltitudeHigher, self).__init__(UnitAltitudeHigher.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.altitude = altitude
        self.params.append(self.altitude)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["altitude"])

    def dict(self):
        d = super(UnitAltitudeHigher, self).dict()
        d["unit"] = self.unit
        d["altitude"] = self.altitude
        return d


class UnitAltitudeLower(Condition):
    predicate = "c_unit_altitude_lower"

    def __init__(self, unit, altitude=1):
        super(UnitAltitudeLower, self).__init__(UnitAltitudeLower.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.altitude = altitude
        self.params.append(self.altitude)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["altitude"])

    def dict(self):
        d = super(UnitAltitudeLower, self).dict()
        d["unit"] = self.unit
        d["altitude"] = self.altitude
        return d


class UnitAltitudeHigherAGL(Condition):
    predicate = "c_unit_altitude_higher_AGL"

    def __init__(self, unit, altitude=1):
        super(UnitAltitudeHigherAGL, self).__init__(UnitAltitudeHigherAGL.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.altitude = altitude
        self.params.append(self.altitude)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["altitude"])

    def dict(self):
        d = super(UnitAltitudeHigherAGL, self).dict()
        d["unit"] = self.unit
        d["altitude"] = self.altitude
        return d


class UnitAltitudeLowerAGL(Condition):
    predicate = "c_unit_altitude_lower_AGL"

    def __init__(self, unit, altitude=1):
        super(UnitAltitudeLowerAGL, self).__init__(UnitAltitudeLowerAGL.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.altitude = altitude
        self.params.append(self.altitude)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["altitude"])

    def dict(self):
        d = super(UnitAltitudeLowerAGL, self).dict()
        d["unit"] = self.unit
        d["altitude"] = self.altitude
        return d


class UnitBankWithin(Condition):
    predicate = "c_unit_bank"

    def __init__(self, unit, min_unit_bank=-180, max_unit_bank=180):
        super(UnitBankWithin, self).__init__(UnitBankWithin.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.min_unit_bank = min_unit_bank
        self.params.append(self.min_unit_bank)
        self.max_unit_bank = max_unit_bank
        self.params.append(self.max_unit_bank)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["min_unit_bank"], d["max_unit_bank"])

    def dict(self):
        d = super(UnitBankWithin, self).dict()
        d["unit"] = self.unit
        d["min_unit_bank"] = self.min_unit_bank
        d["max_unit_bank"] = self.max_unit_bank
        return d


class UnitDamaged(Condition):
    predicate = "c_unit_damaged"

    def __init__(self, unit):
        super(UnitDamaged, self).__init__(UnitDamaged.predicate)
        self.unit = unit
        self.params.append(self.unit)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"])

    def dict(self):
        d = super(UnitDamaged, self).dict()
        d["unit"] = self.unit
        return d


class UnitDead(Condition):
    predicate = "c_unit_dead"

    def __init__(self, unit):
        super(UnitDead, self).__init__(UnitDead.predicate)
        self.unit = unit
        self.params.append(self.unit)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"])

    def dict(self):
        d = super(UnitDead, self).dict()
        d["unit"] = self.unit
        return d


class UnitHeadingWithin(Condition):
    predicate = "c_unit_heading"

    def __init__(self, unit, min_unit_heading, max_unit_heading=360):
        super(UnitHeadingWithin, self).__init__(UnitHeadingWithin.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.min_unit_heading = min_unit_heading
        self.params.append(self.min_unit_heading)
        self.max_unit_heading = max_unit_heading
        self.params.append(self.max_unit_heading)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["min_unit_heading"], d["max_unit_heading"])

    def dict(self):
        d = super(UnitHeadingWithin, self).dict()
        d["unit"] = self.unit
        d["min_unit_heading"] = self.min_unit_heading
        d["max_unit_heading"] = self.max_unit_heading
        return d


class UnitInMovingZone(Condition):
    predicate = "c_unit_in_zone_unit"

    def __init__(self, unit, zone, zoneunit):
        super(UnitInMovingZone, self).__init__(UnitInMovingZone.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.zone = zone
        self.params.append(self.zone)
        self.zoneunit = zoneunit
        self.params.append(self.zoneunit)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["zone"], d["zoneunit"])

    def dict(self):
        d = super(UnitInMovingZone, self).dict()
        d["unit"] = self.unit
        d["zone"] = self.zone
        d["zoneunit"] = self.zoneunit
        return d


class UnitInZone(Condition):
    predicate = "c_unit_in_zone"

    def __init__(self, unit, zone):
        super(UnitInZone, self).__init__(UnitInZone.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["zone"])

    def dict(self):
        d = super(UnitInZone, self).dict()
        d["unit"] = self.unit
        d["zone"] = self.zone
        return d


class UnitLifeLess(Condition):
    predicate = "c_unit_life_less"

    def __init__(self, unit, percent=10):
        super(UnitLifeLess, self).__init__(UnitLifeLess.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.percent = percent
        self.params.append(self.percent)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["percent"])

    def dict(self):
        d = super(UnitLifeLess, self).dict()
        d["unit"] = self.unit
        d["percent"] = self.percent
        return d


class UnitOutsideMovingZone(Condition):
    predicate = "c_unit_out_zone_unit"

    def __init__(self, unit, zone, zoneunit):
        super(UnitOutsideMovingZone, self).__init__(UnitOutsideMovingZone.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.zone = zone
        self.params.append(self.zone)
        self.zoneunit = zoneunit
        self.params.append(self.zoneunit)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["zone"], d["zoneunit"])

    def dict(self):
        d = super(UnitOutsideMovingZone, self).dict()
        d["unit"] = self.unit
        d["zone"] = self.zone
        d["zoneunit"] = self.zoneunit
        return d


class UnitOutsideZone(Condition):
    predicate = "c_unit_out_zone"

    def __init__(self, unit, zone):
        super(UnitOutsideZone, self).__init__(UnitOutsideZone.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.zone = zone
        self.params.append(self.zone)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["zone"])

    def dict(self):
        d = super(UnitOutsideZone, self).dict()
        d["unit"] = self.unit
        d["zone"] = self.zone
        return d


class UnitPitchWithin(Condition):
    predicate = "c_unit_pitch"

    def __init__(self, unit, min_unit_pitch=-180, max_unit_pitch=180):
        super(UnitPitchWithin, self).__init__(UnitPitchWithin.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.min_unit_pitch = min_unit_pitch
        self.params.append(self.min_unit_pitch)
        self.max_unit_pitch = max_unit_pitch
        self.params.append(self.max_unit_pitch)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["min_unit_pitch"], d["max_unit_pitch"])

    def dict(self):
        d = super(UnitPitchWithin, self).dict()
        d["unit"] = self.unit
        d["min_unit_pitch"] = self.min_unit_pitch
        d["max_unit_pitch"] = self.max_unit_pitch
        return d


class UnitSpeedHigher(Condition):
    predicate = "c_unit_speed_higher"

    def __init__(self, unit: int, speed: float = 100):
        """

        :param unit: unit id
        :param speed: in m/s
        """
        super(UnitSpeedHigher, self).__init__(UnitSpeedHigher.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.speed = speed
        self.params.append(self.speed)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["speedU"])

    def dict(self):
        d = super(UnitSpeedHigher, self).dict()
        d["unit"] = self.unit
        d["speedU"] = self.speed
        return d


class UnitSpeedLower(Condition):
    predicate = "c_unit_speed_lower"

    def __init__(self, unit: int, speed: float = 100):
        """

        :param unit: unit id
        :param speed: in m/s
        """
        super(UnitSpeedLower, self).__init__(UnitSpeedLower.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.speed = speed
        self.params.append(self.speed)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["speedU"])

    def dict(self):
        d = super(UnitSpeedLower, self).dict()
        d["unit"] = self.unit
        d["speedU"] = self.speed
        return d


class UnitVerticalSpeedWithin(Condition):
    predicate = "c_unit_vertical_speed"

    def __init__(self, unit, min_unit_vertical_speed=-300, max_unit_vertical_speed=300):
        super(UnitVerticalSpeedWithin, self).__init__(UnitVerticalSpeedWithin.predicate)
        self.unit = unit
        self.params.append(self.unit)
        self.min_unit_vertical_speed = min_unit_vertical_speed
        self.params.append(self.min_unit_vertical_speed)
        self.max_unit_vertical_speed = max_unit_vertical_speed
        self.params.append(self.max_unit_vertical_speed)

    @classmethod
    def create_from_dict(cls, d):
        return cls(d["unit"], d["min_unit_vertical_speed"], d["max_unit_vertical_speed"])

    def dict(self):
        d = super(UnitVerticalSpeedWithin, self).dict()
        d["unit"] = self.unit
        d["min_unit_vertical_speed"] = self.min_unit_vertical_speed
        d["max_unit_vertical_speed"] = self.max_unit_vertical_speed
        return d


condition_map = {
    "c_all_of_coalition_in_zone": AllOfCoalitionInZone,
    "c_all_of_coalition_out_zone": AllOfCoalitionOutsideZone,
    "c_all_of_group_in_zone": AllOfGroupInZone,
    "c_all_of_group_out_zone": AllOfGroupOutsideZone,
    "c_argument_in_range": ArgumentInRange,
    "c_bomb_in_zone": BombInZone,
    "c_cargo_unhooked_in_zone": CargoUnhookedInZone,
    "c_coalition_has_airdrome": CoalitionHasAirdrome,
    "c_coalition_has_helipad": CoalitionHasHelipad,
    "c_cockpit_highlight_visible": CockpitHighlightVisible,
    "c_cockpit_param_equal_to": CockpitParamEqual,
    "c_cockpit_param_is_equal_to_another": CockpitParamEqualToAnother,
    "c_cockpit_param_in_range": CockpitParamInRange,
    "c_flag_equals": FlagEquals,
    "c_flag_equals_flag": FlagEqualsFlag,
    "c_flag_is_false": FlagIsFalse,
    "c_flag_less": FlagIsLess,
    "c_flag_less_flag": FlagIsLessThanFlag,
    "c_flag_more": FlagIsMore,
    "c_flag_is_true": FlagIsTrue,
    "c_group_alive": GroupAlive,
    "c_group_dead": GroupDead,
    "c_group_life_less": GroupLifeLess,
    "c_indication_txt_equal_to": IndicationTextEqual,
    "c_mission_score_higher": MissionScoreHigher,
    "c_mission_score_lower": MissionScoreLower,
    "or": Or,
    "c_part_of_coalition_in_zone": PartOfCoalitionInZone,
    "c_part_of_coalition_out_zone": PartOfCoalitionOutsideZone,
    "c_part_of_group_in_zone": PartOfGroupInZone,
    "c_part_of_group_out_zone": PartOfGroupOutsideZone,
    "c_player_score_less": PlayerScoreLess,
    "c_player_score_more": PlayerScoreMore,
    "c_predicate": Predicate,
    "c_random_less": Random,
    "c_signal_flare_in_zone": SignalFlareInZone,
    "c_time_after": TimeAfter,
    "c_time_before": TimeBefore,
    "c_time_since_flag": TimeSinceFlag,
    "c_unit_alive": UnitAlive,
    "c_unit_altitude_higher": UnitAltitudeHigher,
    "c_unit_altitude_lower": UnitAltitudeLower,
    "c_unit_altitude_higher_AGL": UnitAltitudeHigherAGL,
    "c_units_altitude_lower_AGL": UnitAltitudeLowerAGL,
    "c_unit_bank": UnitBankWithin,
    "c_unit_damaged": UnitDamaged,
    "c_unit_dead": UnitDead,
    "c_unit_heading": UnitHeadingWithin,
    "c_unit_in_zone_unit": UnitInMovingZone,
    "c_unit_in_zone": UnitInZone,
    "c_unit_life_less": UnitLifeLess,
    "c_unit_out_zone_unit": UnitOutsideMovingZone,
    "c_unit_out_zone": UnitOutsideZone,
    "c_unit_pitch": UnitPitchWithin,
    "c_unit_speed_higher": UnitSpeedHigher,
    "c_unit_speed_lower": UnitSpeedLower,
    "c_unit_vertical_speed": UnitVerticalSpeedWithin,
}
