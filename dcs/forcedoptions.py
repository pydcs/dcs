from enum import Enum
from typing import Optional


class ForcedOptions:

    class Views(Enum):
        OnlyMap = "optview_onlymap"
        MyAircraft = "optview_myaircraft"
        Allies = "optview_allies"
        OnlyAllies = "optview_onlyallies"
        All = "optview_all"

    class CivilTraffic(Enum):
        Off = ""
        Low = "low"
        Medium = "medium"
        High = "high"

    class GEffect(Enum):
        None_ = ""
        Game = "game"
        Realistic = "realistic"

    class Labels(Enum):
        None_ = 0
        Full = 1
        Abbreviate = 2
        DotOnly = 3
        NeutralDot = 4

    def __init__(self):
        # In the order they appear in the ME.
        self.permit_crash: Optional[bool] = None
        self.external_views: Optional[bool] = None
        self.options_view: Optional[ForcedOptions.Views] = None
        self.labels: Optional[ForcedOptions.Labels] = None
        self.easy_flight: Optional[bool] = None
        self.easy_radar: Optional[bool] = None
        self.immortal: Optional[bool] = None
        self.fuel: Optional[bool] = None
        self.weapons: Optional[bool] = None
        self.easy_communication: Optional[bool] = None
        self.radio: Optional[bool] = None
        self.unrestricted_satnav: Optional[bool] = None
        self.padlock: Optional[bool] = None
        self.wake_turbulence: Optional[bool] = None
        self.geffect: Optional[bool] = None
        self.accidental_failures = None
        self.mini_hud: Optional[bool] = None
        self.cockpit_visual_recon_mode: Optional[bool] = None
        self.user_marks: Optional[bool] = None
        self.civil_traffic: Optional[ForcedOptions.CivilTraffic] = None
        self.birds: Optional[int] = None
        self.cockpit_status_bar: Optional[bool] = None
        self.battle_damage_assessment: Optional[bool] = None

    def load_from_dict(self, d):
        self.fuel = d.get("fuel")
        self.easy_radar = d.get("easyRadar")
        self.mini_hud = d.get("miniHUD")
        self.accidental_failures = d.get("accidental_failures")
        if d.get("optionsView") is not None:
            self.options_view = ForcedOptions.Views(d["optionsView"])
        self.permit_crash = d.get("permitCrash")
        self.immortal = d.get("immortal")
        self.easy_communication = d.get("easyCommunication")
        self.cockpit_visual_recon_mode = d.get("cockpitVisualRM")
        self.easy_flight = d.get("easyFlight")
        self.radio = d.get("radio")
        if d.get("geffect") is not None:
            geffect = ForcedOptions.GEffect.Game.value if d["geffect"] == "reduced" else d["geffect"]
            self.geffect = ForcedOptions.GEffect(geffect)
        self.external_views = d.get("externalViews")
        self.birds = d.get("birds")
        if d.get("civTraffic") is not None:
            self.civil_traffic = ForcedOptions.CivilTraffic(d["civTraffic"])
        self.weapons = d.get("weapons")
        self.padlock = d.get("padlock")
        if "labels" in d:
            self.labels = ForcedOptions.Labels(d["labels"])
        self.unrestricted_satnav = d.get("unrestrictedSATNAV")
        self.wake_turbulence = d.get("wakeTurbulence")
        self.cockpit_status_bar = d.get("cockpitStatusBarAllowed")
        self.battle_damage_assessment = d.get("RBDAI")
        self.user_marks = d.get("userMarks")

    def dict(self):
        d = {}
        if self.fuel is not None:
            d["fuel"] = self.fuel
        if self.easy_radar is not None:
            d["easyRadar"] = self.easy_radar
        if self.mini_hud is not None:
            d["miniHUD"] = self.mini_hud
        if self.accidental_failures is not None:
            d["accidental_failures"] = self.accidental_failures
        if self.options_view is not None:
            d["optionsView"] = self.options_view.value
        if self.permit_crash is not None:
            d["permitCrash"] = self.permit_crash
        if self.immortal is not None:
            d["immortal"] = self.immortal
        if self.easy_communication is not None:
            d["easyCommunication"] = self.easy_communication
        if self.cockpit_visual_recon_mode is not None:
            d["cockpitVisualRM"] = self.cockpit_visual_recon_mode
        if self.easy_flight is not None:
            d["easyFlight"] = self.easy_flight
        if self.radio is not None:
            d["radio"] = self.radio
        if self.geffect is not None:
            d["geffect"] = self.geffect.value
        if self.external_views is not None:
            d["externalViews"] = self.external_views
        if self.birds is not None:
            d["birds"] = self.birds
        if self.civil_traffic is not None:
            d["civTraffic"] = self.civil_traffic.value
        if self.weapons is not None:
            d["weapons"] = self.weapons
        if self.padlock is not None:
            d["padlock"] = self.padlock
        if self.labels is not None:
            d["labels"] = self.labels.value
        if self.unrestricted_satnav is not None:
            d["unrestrictedSATNAV"] = self.unrestricted_satnav
        if self.wake_turbulence is not None:
            d["wakeTurbulence"] = self.wake_turbulence
        if self.cockpit_status_bar is not None:
            d["cockpitStatusBarAllowed"] = self.cockpit_status_bar
        if self.battle_damage_assessment is not None:
            d["RBDAI"] = self.battle_damage_assessment
        if self.user_marks is not None:
            d["userMarks"] = self.user_marks
        return d
