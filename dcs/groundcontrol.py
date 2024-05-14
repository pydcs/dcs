from __future__ import annotations

from enum import Enum
from typing import Dict, Any, List, Tuple, Optional
from dcs.action import Coalition
from dcs.password import password_hash


class GroundControlRole(Enum):
    GAME_MASTER = "instructor"
    TACTICAL_COMMANDER = "artillery_commander"
    JTAC = "forward_observer"
    OBSERVER = "observer"


GroundControlPasswordsEntries = Dict[Coalition, Any]


class GroundControlPasswords:
    def __init__(self, d: Optional[Dict[str, Any]] = None) -> None:
        self.game_masters: GroundControlPasswordsEntries = {}
        self.tactical_commander: GroundControlPasswordsEntries = {}
        self.jtac: GroundControlPasswordsEntries = {}
        self.observer: GroundControlPasswordsEntries = {}

        if d is not None:
            for coalition in [Coalition.Red, Coalition.Blue, Coalition.Neutral]:
                for miz_role, role_password in self.get_role_to_attr_mapping():
                    if miz_role.value in d and coalition.value in d[miz_role.value]:
                        role_password[coalition] = d[miz_role.value][coalition.value]

    @classmethod
    def create_from_dict(cls, d: Dict[str, Any]) -> GroundControlPasswords:
        return GroundControlPasswords(d)

    def get_role_to_attr_mapping(self) -> List[Tuple[GroundControlRole, GroundControlPasswordsEntries]]:
        return [(GroundControlRole.GAME_MASTER, self.game_masters),
                (GroundControlRole.TACTICAL_COMMANDER, self.tactical_commander),
                (GroundControlRole.JTAC, self.jtac),
                (GroundControlRole.OBSERVER, self.observer)]

    def _find_role_password(self, role: GroundControlRole) -> GroundControlPasswordsEntries:
        for miz_role, role_password in self.get_role_to_attr_mapping():
            if role == miz_role:
                return role_password
        raise RuntimeError(f"Unable to find passwords for {role.value} role")

    def lock(self, coalition: Coalition, role: GroundControlRole, password: str) -> None:
        role_password = self._find_role_password(role)
        role_password[coalition] = password_hash(password)

    def unlock(self, coalition: Coalition, role: GroundControlRole) -> None:
        role_password = self._find_role_password(role)
        role_password[coalition] = None

    def is_locked(self, coalition: Coalition, role: GroundControlRole) -> bool:
        role_password = self._find_role_password(role)
        return coalition in role_password and role_password[coalition] is not None

    def dict(self) -> Dict[str, Dict[str, str]]:
        d: Dict[str, Any] = {}
        for coalition in [Coalition.Red, Coalition.Blue, Coalition.Neutral]:
            for miz_role, role_password in self.get_role_to_attr_mapping():
                if coalition in role_password and role_password[coalition] is not None:
                    if miz_role.value not in d:
                        d[miz_role.value] = {}
                    d[miz_role.value][coalition.value] = role_password[coalition]
        return d


class GroundControl:
    def __init__(self):
        self.pilot_can_control_vehicles = False
        self.red_game_masters = 0
        self.red_tactical_commander = 0
        self.red_jtac = 0
        self.red_observer = 0

        self.blue_game_masters = 0
        self.blue_tactical_commander = 0
        self.blue_jtac = 0
        self.blue_observer = 0

        self.neutrals_game_masters = 0
        self.neutrals_tactical_commander = 0
        self.neutrals_jtac = 0
        self.neutrals_observer = 0

        self.passwords = GroundControlPasswords()

    def load_from_dict(self, d):
        if d is None:
            return
        self.pilot_can_control_vehicles = d["isPilotControlVehicles"]

        self.red_game_masters = int(d["roles"]["instructor"]["red"])
        self.red_tactical_commander = int(d["roles"]["artillery_commander"]["red"])
        self.red_jtac = int(d["roles"]["forward_observer"]["red"])
        self.red_observer = int(d["roles"]["observer"]["red"])

        self.blue_game_masters = int(d["roles"]["instructor"]["blue"])
        self.blue_tactical_commander = int(d["roles"]["artillery_commander"]["blue"])
        self.blue_jtac = int(d["roles"]["forward_observer"]["blue"])
        self.blue_observer = int(d["roles"]["observer"]["blue"])

        self.neutrals_game_masters = int(d["roles"]["instructor"].get("neutrals", 0))
        self.neutrals_tactical_commander = int(d["roles"]["artillery_commander"].get("neutrals", 0))
        self.neutrals_jtac = int(d["roles"]["forward_observer"].get("neutrals", 0))
        self.neutrals_observer = int(d["roles"]["observer"].get("neutrals", 0))

        if "passwords" in d:
            self.passwords = GroundControlPasswords.create_from_dict(d["passwords"])
        else:
            self.passwords = GroundControlPasswords()

    def lock(self, coalition: Coalition, role: GroundControlRole, password: str) -> None:
        self.passwords.lock(coalition, role, password)

    def unlock(self, coalition: Coalition, role: GroundControlRole) -> None:
        self.passwords.unlock(coalition, role)

    def is_locked(self, coalition: Coalition, role: GroundControlRole) -> bool:
        return self.passwords.is_locked(coalition, role)

    def dict(self):
        return {
            "isPilotControlVehicles": self.pilot_can_control_vehicles,
            "passwords": self.passwords.dict(),
            "roles": {
                "instructor": {
                    "red": self.red_game_masters,
                    "blue": self.blue_game_masters,
                    "neutrals": self.neutrals_game_masters
                },
                "artillery_commander": {
                    "red": self.red_tactical_commander,
                    "blue": self.blue_tactical_commander,
                    "neutrals": self.neutrals_tactical_commander
                },
                "forward_observer": {
                    "red": self.red_jtac,
                    "blue": self.blue_jtac,
                    "neutrals": self.neutrals_jtac
                },
                "observer": {
                    "red": self.red_observer,
                    "blue": self.blue_observer,
                    "neutrals": self.neutrals_observer
                },
            }
        }
