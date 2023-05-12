import logging
import os
import re
import zipfile
from typing import Dict, Iterator, Optional

import dcs.lua
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


def safe_name(string: str) -> str:
    safe_name = re.sub(r"[-()/., *\'+`#%\[\]]", "_", string)
    safe_name = re.sub(r'_*$|"|&', "", safe_name)
    safe_name = re.sub(r"^(\d)", r"x_\1", safe_name)
    safe_name = re.sub(r"[\u0080-\uFFFF]", "_", safe_name)
    return safe_name


def _attempt_read_from_filestream(filestream: bytes) -> Optional[str]:
    encodes = ["utf-8", "ansi"]
    for enc in encodes:
        try:
            code = filestream.decode(enc)
        except UnicodeDecodeError:
            continue
        return code
    return None


class LiveryScanner:
    """
    Class containing a map of all units with their respective liveries.
    Each livery has a set of countries to indicate applicability
    """

    map: Dict[str, LiverySet] = {}
    """
    A dictionary containing all liveries for each unit.
    Mind that the unit uses the name of the livery folder, and not the ID.
    Every livery has a set of countries for which the livery is applicable.
    In case countries is None, it indicates the livery is valid for all countries

    Unit (str) -> LiverySet
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
        if len(LiveryScanner.map) == 0:
            install, saved_games = read_liberation_preferences()
            LiveryScanner.initialize(install, saved_games)

    def __getitem__(self, unit: str) -> LiverySet:
        liveries = LiveryScanner.map.get(unit)
        return liveries if liveries is not None else LiverySet(unit)

    def __setitem__(self, unit: str, liveries: LiverySet) -> None:
        if unit in LiveryScanner.map:
            LiveryScanner.map[unit].update(liveries)
        else:
            LiveryScanner.map[unit] = liveries

    def __delitem__(self, unit: str) -> None:
        del LiveryScanner.map[unit]

    def __iter__(self) -> Iterator[str]:
        return LiveryScanner.map.__iter__()

    @staticmethod
    def initialize(install: str = "", saved_games: str = "") -> None:
        """
        Initializes the Liveries map given the root install directory for DCS
        and the path to its Saved Games folder.

        :param install: Path to DCS' installation folder,
            if empty PyDCS will attempt to determine this.
        :param saved_games: Path to the Saved Games folder,
            if empty PyDCS will attempt to determine this.
        """
        LiveryScanner.map.clear()
        LiveryScanner.scan_dcs_installation(install)
        LiveryScanner.scan_custom_liveries(saved_games)

    @staticmethod
    def scan_lua_code(luacode: str, path: str, unit: str) -> None:
        """
        Scans the given code (expecting contents from a description.lua file)
        to extract the name of the livery together with the countries for which the livery is applicable.
        If no name is found, it defaults to the folder-name like DCS would.
        If no countries are found, it means the livery is valid for all countries.
        Finally we also attempt to extract the order to sort liveries like DCS.
        If no order is found, we use a default value of 0.

        :param luacode: The contents of description.lua for the livery in question
        :param path: The path of the livery in question
        :param unit: The name of the unit as 'DCS type',
            i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
        """
        path_id = path.split("\\")[-1].replace(".zip", "")
        if path_id == "placeholder":
            return

        # Some liveries files use variables in material names. Since the files read by
        # the scanner can be arbitrarily changed by a game update (we don't want some
        # liveries to be suddenly unparseable), and so far we aren't interested in the
        # values of liveries that rely on undefined variables, just assume those are all
        # the empty string and move on.
        data = dcs.lua.loads(luacode, unknown_variable_lookup=lambda _: "")
        livery_name = data.get("name", path_id)
        countries_table = data.get("countries")
        if countries_table is None:
            countries = None
        else:
            countries = set(countries_table.values())
        order = data.get("order", 0)

        order = None if path_id == "default" else order
        if order is not None and not isinstance(order, int):
            try:
                order = int(order)
            except ValueError:
                order = 0

        livery = Livery(path_id, livery_name, order, countries)
        LiveryScanner.map[unit].add(livery)
        setattr(LiveryScanner.map[unit], safe_name(livery.id), livery)

    @staticmethod
    def scan_lua_description(path: str, unit: str) -> None:
        """
        Verifies a description file exists and reads its contents,
        passing it to 'scan_lua_code'.

        :param path: The path of the livery in question
        :param unit: The name of the unit as 'DCS type',
            i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
        """
        description_path = os.path.join(path, "description.lua")
        if os.path.exists(description_path):
            # Known encodings used for description.lua files
            with open(description_path, "rb") as file:
                code = _attempt_read_from_filestream(file.read())
                if code is None:
                    logging.warning(f" Unknown encoding found in '{description_path}'")
                    return

                try:
                    LiveryScanner.scan_lua_code(code, path, unit)
                except (IndexError, SyntaxError):
                    logging.getLogger("pydcs").exception(
                        "Failed to parse Lua code in %s", description_path
                    )
                    print("Failed to parse Lua code in {}".format(description_path))
                    raise

    @staticmethod
    def scan_zip_file(path: str, unit: str) -> None:
        """
        Some liveries are zipped, this does the same as 'scan_lua_description',
        except for the fact it needs to "open the zip" first.

        :param path: The path of the livery in question
        :param unit: The name of the unit as 'DCS type',
            i.e. name of the unit inside the Liveries folder, e.g. 'A-10CII'
        """
        if os.path.exists(path):
            with zipfile.ZipFile(path, "r") as zf:
                if "description.lua" in zf.namelist():
                    with zf.open("description.lua", "r") as file:
                        code = _attempt_read_from_filestream(file.read())
                        if code is None:
                            logging.warning(
                                f" Unknown encoding found in '{path}/description.lua'"
                            )
                            return

                        try:
                            LiveryScanner.scan_lua_code(code, path, unit)
                        except (SyntaxError, IndexError):
                            error_path = "!".join([path, "description.lua"])
                            logging.getLogger("pydcs").exception(
                                "Failed to parse Lua code in %s", error_path
                            )
                            raise

    @staticmethod
    def scan_liveries(path: str, campaign_path: bool = False) -> None:
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
            if unit not in LiveryScanner.map:
                LiveryScanner.map[unit] = LiverySet(unit)
                setattr(LiveryScanner, safe_name(unit), LiveryScanner.map[unit])
            for livery in os.listdir(liveries_path):
                livery_path = os.path.join(liveries_path, livery)
                if os.path.isdir(livery_path):
                    LiveryScanner.scan_lua_description(livery_path, unit)
                elif os.path.isfile(livery_path) and ".zip" in livery_path:
                    LiveryScanner.scan_zip_file(livery_path, unit)

    @staticmethod
    def scan_mods_path(path: str) -> None:
        """
        Scans all liveries for a certain "Mod".

        :param path: A path to a "Mod", e.g. "CoreMods", custom "Mods" in saved games, etc.
        """
        if not os.path.exists(path):
            return
        for unit in os.listdir(path):
            liveries_path = os.path.join(path, unit, "Liveries")
            if os.path.exists(liveries_path):
                LiveryScanner.scan_liveries(liveries_path)

    @staticmethod
    def scan_campaign_liveries(path: str) -> None:
        """
        Scans all extra liveries from campaigns.

        :param path: The path to 'DCS-installation/Mods/campaigns'.
        """
        if not os.path.exists(path):
            return
        for campaign in os.listdir(path):
            liveries_path = os.path.join(path, campaign, "Liveries")
            if os.path.exists(liveries_path):
                LiveryScanner.scan_liveries(liveries_path, campaign_path=True)

    @staticmethod
    def scan_dcs_installation(install: str = ""):
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

        LiveryScanner.scan_mods_path(path1)
        LiveryScanner.scan_mods_path(path2)
        LiveryScanner.scan_liveries(path3)
        LiveryScanner.scan_campaign_liveries(path4)
        LiveryScanner.scan_mods_path(path5)
        LiveryScanner.scan_liveries(path6)

    @staticmethod
    def scan_custom_liveries(saved_games: str = ""):
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

        LiveryScanner.scan_liveries(path1)
        LiveryScanner.scan_mods_path(path2)
