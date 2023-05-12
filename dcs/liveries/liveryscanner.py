import os
from typing import Dict

from dcs.installation import get_dcs_install_directory, get_dcs_saved_games_directory

from .liberation import read_liberation_preferences
from .livery import Livery
from .liveryset import LiverySet

campaign_livery_aliases = {  # Known aliases in campaign liveries
    "FW-190D-9": "FW-190D9",  # The Big Show
}

skip_units = {  # Known obsolete units in specific locations
    "leopard-2": "Bazar",
    "Zil_135l": "Bazar",
}


class LiveryScanner:
    """
    Class containing a map of all units with their respective liveries.
    Each livery has a set of countries to indicate applicability
    """

    def __init__(self) -> None:
        """
        Constructor only attempts to initialize if 'map' is empty.
        The first attempt to determine paths for initialization will look
        for Liberation's preferences file, as this gives us a way to initialize
        the scanner on time in Liberation. If proper initialization isn't done before
        importing modules that make use of this scanner, for example planes.py, we risk
        having those modules initialized without the proper liveries.
        If no preferences file is found, PyDCS will attempt to determine the correct paths instead.
        You can also initialize manually by calling 'Liveries.initialize(...)',
        but beware that this must happen on time in case of designs like planes.py or helicopters.py.
        """
        self.map: Dict[str, LiverySet] = {}

    def load(self) -> Dict[str, LiverySet]:
        install, saved_games = read_liberation_preferences()
        return self.load_from(install, saved_games)

    def load_from(
        self, dcs_install_path: str, dcs_saved_games_path: str
    ) -> Dict[str, LiverySet]:
        self.scan_dcs_installation(dcs_install_path)
        self.scan_custom_liveries(dcs_saved_games_path)
        return self.map

    def register_livery(self, unit: str, livery: Livery) -> None:
        self.map[unit].add(livery)

    def scan_liveries(self, path: str, campaign_path: bool = False) -> None:
        """
        Scans liveries for all units in the given path.

        :param path: A 'Liveries' path containing one or more units
        :param campaign_path: A boolean value indicating whether the path
            is special livery path for 3rd party campaigns. This is important
            because in some cases aliases are used for certain units. This would
            result in separate entries in the Liveries map, which is not good.
        """
        if not os.path.exists(path):
            return
        for unit in os.listdir(path):
            if unit in skip_units and skip_units[unit] in path:
                continue
            liveries_path = os.path.join(path, unit)
            # The unit's name for liveries is NOT case-sensitive,
            # e.g.: 'Saved Games/Liveries/f-15c' vs 'DCS-install/Bazar/Liveries/F-15C
            # thus convert 'unit' to upper/lower to make sure everything "merges properly"
            unit = unit.upper()
            if "COCKPIT" in unit or not os.path.isdir(liveries_path):
                # Some custom mods put their cockpit liveries in the same directory,
                # for the time being we don't want to load those.
                # Other than that we're looking exclusively for directories.
                continue
            if campaign_path and unit in campaign_livery_aliases:
                unit = campaign_livery_aliases[unit]
            if unit not in self.map:
                self.map[unit] = LiverySet(unit)
            for livery_name in os.listdir(liveries_path):
                livery = Livery.from_path(os.path.join(liveries_path, livery_name))
                if livery is not None:
                    self.register_livery(unit, livery)

    def scan_mods_path(self, path: str) -> None:
        """
        Scans all liveries for a certain "Mod".

        :param path: A path to a "Mod", e.g. "CoreMods", custom "Mods" in saved games, etc.
        """
        if not os.path.exists(path):
            return
        for unit in os.listdir(path):
            liveries_path = os.path.join(path, unit, "Liveries")
            if os.path.exists(liveries_path):
                self.scan_liveries(liveries_path)

    def scan_campaign_liveries(self, path: str) -> None:
        """
        Scans all extra liveries from campaigns.

        :param path: The path to 'DCS-installation/Mods/campaigns'.
        """
        if not os.path.exists(path):
            return
        for campaign in os.listdir(path):
            liveries_path = os.path.join(path, campaign, "Liveries")
            if os.path.exists(liveries_path):
                self.scan_liveries(liveries_path, campaign_path=True)

    def scan_dcs_installation(self, install: str = ""):
        """
        Scans all liveries in DCS' installation folder

        :param install: Path to DCS' installation folder,
            if an empty string or invalid path was given PyDCS will attempt to determine this.
        """
        root = install
        if root == "" or not os.path.isdir(root):
            root = get_dcs_install_directory()

        path1 = os.path.join(root, "CoreMods", "aircraft")
        path2 = os.path.join(root, "CoreMods", "WWII Units")
        path3 = os.path.join(root, "Bazar", "Liveries")
        path4 = os.path.join(root, "Mods", "campaigns")
        path5 = os.path.join(root, "CoreMods", "tech")
        path6 = os.path.join(root, "Mods", "tech", "WWII Units", "Liveries")

        self.scan_mods_path(path1)
        self.scan_mods_path(path2)
        self.scan_liveries(path3)
        self.scan_campaign_liveries(path4)
        self.scan_mods_path(path5)
        self.scan_liveries(path6)

    def scan_custom_liveries(self, saved_games: str = ""):
        """
        Scans all custom liveries & liveries of aircraft mods.

        :param saved_games: Path to Saved Games folder,
            if an empty string or invalid path was given PyDCS will attempt to determine this.
        """
        root = saved_games
        if root == "" or not os.path.isdir(root):
            root = get_dcs_saved_games_directory()

        path1 = os.path.join(root, "Liveries")
        path2 = os.path.join(root, "Mods", "aircraft")

        self.scan_liveries(path1)
        self.scan_mods_path(path2)
