"""
A nav target point is special type of point handled in DCS mission editor.

Two aircraft uses these special waypoints for now :
- The JF-17 Thunder
- The F-14B Tomcat


--------------------------------------------------------------------------
JF-17 :
For the JF-17 it is possible to set up "PP" waypoint and "RP" waypoint.

PP waypoints can be set by putting a comment : PP1, PP2, PP3, PP4, or PP5
RP waypoints can be set by putting a comment : RP1, RP2, RP3, RP4, or RP5

PP waypoints are preplanned target waypoints for guided bombs.
RP waypoints are special points for the C-802AKG cruise missile.

--------------------------------------------------------------------------
F-14B Tomcat :

See http://www.heatblur.se/F-14Manual/dcs.html#f-14-waypoints-in-the-mission-editor

--------------------------------------------------------------------------

"""

from dcs import mapping


class NavTargetPoint:
    def __init__(self):
        self.position = mapping.Point(0, 0)
        self.text_comment = ""
        self.index = 0

    @classmethod
    def create_from_dict(cls, d):
        t = cls()
        t.position = mapping.Point(d["x"], d["y"])
        t.text_comment = d["text_comment"]
        t.index = d["index"]
        return t

    def dict(self):
        return {
            "x": self.position.x,
            "y": self.position.y,
            "index": self.index,
            "text_comment": self.text_comment,
        }
