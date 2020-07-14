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

    def __init__(self):
        self.fuel = None
        self.easy_radar = None
        self.mini_hud = None
        self.accidental_failures = None
        self.options_view: Optional[ForcedOptions.Views] = None
        self.permit_crash = None
        self.immportal = None
        self.easy_communication = None
        self.cockpit_visual_recon_mode = None
        self.easy_flight = None
        self.radio = None
        self.tips = None
        self.geffect = None
        self.external_views = None
        self.birds = None
        self.civil_traffic: Optional[ForcedOptions.CivilTraffic] = None
        self.weapons = None
        self.padlock = None
        self.scenes = None
        self.labels = None

    def load_from_dict(self, d):
        self.fuel = d.get("fuel")
        self.easy_radar = d.get("easyRadar")
        self.mini_hud = d.get("miniHUD")
        self.accidental_failures = d.get("accidental_failures")
        if d.get("optionsView") is not None:
            self.options_view = ForcedOptions.Views(d["optionsView"])
        self.permit_crash = d.get("permitCrash")
        self.immportal = d.get("immortal")
        self.easy_communication = d.get("easyCommunication")
        self.cockpit_visual_recon_mode = d.get("cockpitVisualRM")
        self.easy_flight = d.get("easyFlight")
        self.radio = d.get("radio")
        self.tips = d.get("tips")
        if d.get("geffect") is not None:
            geffect = ForcedOptions.GEffect.Game.value if d["geffect"] == "reduced" else d["geffect"]
            self.geffect = ForcedOptions.GEffect(geffect)
        self.external_views = d.get("externalViews")
        self.birds = d.get("birds")
        if d.get("civTraffic") is not None:
            self.civil_traffic = ForcedOptions.CivilTraffic(d["civTraffic"])
        self.weapons = d.get("weapons")
        self.padlock = d.get("padlock")
        self.labels = d.get("labels")
        self.scenes = d.get("scenes")

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
        if self.immportal is not None:
            d["immortal"] = self.immportal
        if self.easy_communication is not None:
            d["easyCommunication"] = self.easy_communication
        if self.cockpit_visual_recon_mode is not None:
            d["cockpitVisualRM"] = self.cockpit_visual_recon_mode
        if self.easy_flight is not None:
            d["easyFlight"] = self.easy_flight
        if self.radio is not None:
            d["radio"] = self.radio
        if self.tips is not None:
            d["tips"] = self.tips
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
            d["labels"] = self.labels
        if self.scenes is not None:
            d["scenes"] = self.scenes
        return d
