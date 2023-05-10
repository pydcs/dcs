from pathlib import Path
from typing import Iterator, List, Optional

import dcs.installation as installation


def _find_dcs_payload_paths() -> List[Path]:
    dcs_dir = Path(installation.get_dcs_install_directory())
    dcs_aircraft_dir = dcs_dir / "CoreMods" / "aircraft"
    if not dcs_aircraft_dir.exists():
        return []

    payload_dirs = [dcs_dir / "MissionEditor" / "data" / "scripts" / "UnitPayloads"]
    for entry in dcs_aircraft_dir.iterdir():
        airframe_specific = entry / "UnitPayloads"
        if airframe_specific.exists():
            payload_dirs.append(airframe_specific)

    return payload_dirs


def _find_mod_payload_paths() -> List[Path]:
    user_dir = Path(installation.get_dcs_saved_games_directory())
    mod_aircraft_dir = user_dir / "Mods" / "Aircraft"
    if not mod_aircraft_dir.exists():
        return []

    payload_dirs = []
    for entry in mod_aircraft_dir.iterdir():
        airframe_specific = entry / "UnitPayloads"
        if airframe_specific.exists():
            payload_dirs.append(airframe_specific)

    return payload_dirs


class PayloadDirectories:
    fallback: Optional[Path] = None
    _dcs: Optional[List[Path]] = None
    _mod: Optional[List[Path]] = None
    _user: Optional[Path] = None
    preferred: Optional[Path] = None

    @classmethod
    def dcs(cls) -> List[Path]:
        if cls._dcs is None:
            cls._dcs = _find_dcs_payload_paths()
        return cls._dcs

    @classmethod
    def mod(cls) -> List[Path]:
        if cls._mod is None:
            cls._mod = _find_mod_payload_paths()
        return cls._mod

    @classmethod
    def user(cls) -> Path:
        if cls._user is None:
            cls._user = (
                Path(installation.get_dcs_saved_games_directory())
                / "MissionEditor"
                / "UnitPayloads"
            )
        return cls._user

    @classmethod
    def set_fallback(cls, path: Path) -> None:
        cls.fallback = path

    @classmethod
    def set_preferred(cls, path: Path) -> None:
        cls.preferred = path

    @classmethod
    def payload_dirs(cls) -> Iterator[Path]:
        # These are iterated in order of decreasing order of preference.
        if cls.preferred is not None:
            yield cls.preferred
        yield cls.user()
        yield from cls.dcs()
        yield from cls.mod()
        if cls.fallback:
            yield cls.fallback
