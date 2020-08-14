from typing import List
import dcs.condition as condition


class Goal:
    def __init__(self, comment="", score=100):
        self.rules = []  # type: List[condition.Condition]
        self.side = "OFFLINE"
        self.score = score
        self.predicate = "score"
        self.comment = comment

    def load_from_dict(self, data):
        self.side = data["side"]
        self.score = data["score"]
        self.predicate = data["predicate"]
        self.comment = data["comment"]
        self.rules = []
        rules = data["rules"]
        for x in rules:
            gr = condition.condition_map[rules[x]["predicate"]].create_from_dict(rules[x])
            self.rules.append(gr)

    def conditions(self):
        return " and ".join(map(repr, self.rules))

    def dict(self):
        return {
            "side": self.side,
            "score": self.score,
            "predicate": self.predicate,
            "comment": self.comment,
            "rules": {i+1: self.rules[i].dict() for i in range(0, len(self.rules))}
        }


class Goals:
    def __init__(self):
        self.goals = {
            "red": [],  # type list[Goal]
            "blue": [],  # type list[Goal]
            "offline": []  # type list[Goal]
        }

    def load_from_dict(self, data):
        for x in data:
            g = Goal()
            g.load_from_dict(data[x])
            self.goals[data[x]["side"].lower()].append(g)

    def add_red(self, g: Goal):
        g.side = "RED"
        self.goals["red"].append(g)

    def add_blue(self, g: Goal):
        g.side = "BLUE"
        self.goals["blue"].append(g)

    def add_offline(self, g: Goal):
        g.side = "OFFLINE"
        self.goals["offline"].append(g)

    def generate_result(self):
        d = {
            "total": len(self.goals["blue"]) + len(self.goals["red"]) + len(self.goals["offline"]),
            "blue": {},
            "red": {},
            "offline": {}
        }
        funcstr = "if mission.result.{side}.conditions[{idx}]() then mission.result.{side}.actions[{idx}]() end"
        for side in ["blue", "red", "offline"]:
            d[side]["conditions"] = {i + 1: "return(" + self.goals[side][i].conditions() + ")"
                                     for i in range(0, len(self.goals[side]))}
            d[side]["actions"] = {i + 1: "a_set_mission_result(" + str(self.goals[side][i].score) + ")"
                                  for i in range(0, len(self.goals[side])) if self.goals[side][i].rules}
            d[side]["func"] = {
                i + 1: funcstr.format(side=side, idx=i+1)
                for i in range(0, len(self.goals[side])) if self.goals[side][i].rules}
        return d

    def dict(self):
        return {i+1: self.goals[side][i].dict()
                for side in ["blue", "red", "offline"] for i in range(0, len(self.goals[side]))}
