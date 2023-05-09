"""
This utility classes provides methods to check players installed DCS environment.

TODO : add method 'is_using_open_beta', 'is_using_stable'
TODO : [NICE to have] add method to check list of installed DCS modules
       (could be done either through windows registry, or through filesystem analysis ?)
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Optional

from dcs.winreg import read_current_user_value

STEAM_REGISTRY_KEY_NAME = "Software\\Valve\\Steam"
DCS_STABLE_REGISTRY_KEY_NAME = "Software\\Eagle Dynamics\\DCS World"
DCS_BETA_REGISTRY_KEY_NAME = "Software\\Eagle Dynamics\\DCS World OpenBeta"


def get_dcs_install_directory() -> str:
    """
    Get the DCS World install directory for this computer
    :return DCS World install directory
    """
    standalone_stable_path = read_current_user_value(
        DCS_STABLE_REGISTRY_KEY_NAME, "Path", Path
    )
    if standalone_stable_path is not None:
        return f"{standalone_stable_path}{os.path.sep}"
    standalone_beta_path = read_current_user_value(
        DCS_BETA_REGISTRY_KEY_NAME, "Path", Path
    )
    if standalone_beta_path is not None:
        return f"{standalone_beta_path}{os.path.sep}"
    steam_path = _dcs_steam_path()
    if steam_path is not None:
        return f"{steam_path}{os.path.sep}"

    print("Couldn't detect any installed DCS World version", file=sys.stderr)
    return ""


def get_dcs_saved_games_directory():
    """
    Get the save game directory for DCS World
    :return: Save game directory as string
    """
    saved_games = os.path.join(os.path.expanduser("~"), "Saved Games", "DCS")
    dcs_variant = os.path.join(get_dcs_install_directory(), "dcs_variant.txt")
    if os.path.exists(dcs_variant):
        # read from the file, append first line to saved games, e.g.: DCS.openbeta
        with open(dcs_variant, "r") as file:
            suffix = re.sub(r"[^\w\d-]", "", file.read())
            saved_games = saved_games + "." + suffix
    return saved_games


def _steam_library_directories() -> List[Path]:
    """
    Get the installation directory for Steam games
    :return List of Steam library folders where games can be installed
    """
    steam_dir = read_current_user_value(STEAM_REGISTRY_KEY_NAME, "SteamPath", Path)
    if steam_dir is None:
        return []
    """
    For reference here is what the vdf file is supposed to look like :

    "LibraryFolders"
    {
        "TimeNextStatsReport"        "1561832478"
        "ContentStatsID"        "-158337411110787451"
        "1"        "D:\\Games\\Steam"
        "2"        "E:\\Steam"
    }
    """
    contents = (steam_dir / "steamapps/libraryfolders.vdf").read_text()
    return [
        Path(line.split('"')[3])
        for line in contents.splitlines()[1:]
        if ":\\\\" in line
    ]


def _dcs_steam_path() -> Optional[Path]:
    """
    Find the DCS install directory for DCS World Steam Edition
    :return: Install directory as string, empty string if not found
    """
    for library_folder in _steam_library_directories():
        folder = library_folder / "steamapps/common/DCSWorld"
        if folder.is_dir():
            return folder
    return None


if __name__ == "__main__":
    print("DCS Installation directory : " + get_dcs_install_directory())
    print("DCS saved games directory : " + get_dcs_saved_games_directory())
