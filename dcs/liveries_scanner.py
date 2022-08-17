import json
import logging
import os
import re
import zipfile

from dcs.installation import get_dcs_install_directory, get_dcs_saved_games_directory
from typing import Optional, Dict, Iterator, Set, Tuple

campaign_livery_aliases = {  # Known aliases in campaign liveries
    "FW-190D-9": "FW-190D9",  # The Big Show
}

skip_units = {  # Known obsolete units in specific locations
    "leopard-2": "Bazar",
    "Zil_135l": "Bazar",
}


def regex_group_extractor(regex: str, text: str, fallback=None):
    match = re.search(regex, text, re.MULTILINE)
    if match is not None:
        return match.group(1)
    else:
        return fallback


def read_liberation_preferences() -> Tuple[str, str]:
    install = ""
    saved_games = ""
    pref_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "DCSLiberation")
    pref_path = os.path.join(pref_path, "liberation_preferences.json")
    if os.path.exists(pref_path):
        with open(pref_path, "r") as file:
            json_dict = json.load(file)
            if "dcs_install_dir" in json_dict:
                install = json_dict["dcs_install_dir"]
            if "saved_game_dir" in json_dict:
                saved_games = json_dict["saved_game_dir"]
    return install, saved_games


def safe_name(string: str) -> str:
    safe_name = re.sub(r'[-()/., *\'+`#%\[\]]', "_", string)
    safe_name = re.sub(r'_*$|"|&', '', safe_name)
    safe_name = re.sub(r'^(\d)', r'x_\1', safe_name)
    safe_name = re.sub(r'[\u0080-\uFFFF]', '_', safe_name)
    return safe_name


def generate_stub() -> None:
    if __name__ != "__main__":
        print("Stub should not be generated externally!")
        return
    Liveries()  # initialize in case that hasn't happened yet.
    with open("liveries_scanner.pyi", 'w', encoding="utf8") as file:
        with open("stub templates/liveries_scanner.pyi", 'r', encoding="utf8") as template:
            file.write(template.read())
        for unit in Liveries.map:
            file.write(f"\n    class {safe_name(unit)}(LiverySet):\n")
            safe_value = unit.replace('\'', '\\\'').replace('\"', '\"')
            file.write(f"        unit_livery_id = '{safe_value}'\n\n")
            for livery in sorted(Liveries.map[unit]):
                file.write(f"        {safe_name(livery.id)}: Livery\n")


def _attempt_read_from_filestream(filestream: bytes) -> Optional[str]:
    encodes = ["utf-8", "ansi"]
    for enc in encodes:
        try:
            code = filestream.decode(enc)
        except UnicodeDecodeError:
            continue
        return code
    return None


class Livery:
    id: str = ""
    """ID of the livery, corresponds with the folder-name of the livery. To be used in mission file!"""

    name: str = ""
    """Name of the livery as displayed in DCS"""

    order: int = 0
    """Order of the livery used to sort like DCS"""

    countries: Optional[Set[str]] = None
    """Set of short names indicating valid countries, with 'None' indicating all countries."""

    def __init__(self, path_id: str, name: str, order: int, countries: Optional[Set[str]]) -> None:
        self.id = path_id
        self.name = name
        self.order = order
        self.countries = countries

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        if self.order == other.order:
            return self.name < other.name
        if self.order is None:
            return True
        return False if other.order is None else self.order < other.order

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def valid_for_country(self, country: str) -> bool:
        return self.countries is None or country in self.countries


class LiverySet(set):
    unit_livery_id: Optional[str] = None

    def __init__(self, unit_livery_id: Optional[str] = None) -> None:
        super().__init__()
        self.unit_livery_id = unit_livery_id

    def __str__(self) -> str:
        return f"{self.unit_livery_id} => {super().__str__()}"

    def add(self, element: Livery) -> None:
        if isinstance(element, Livery):
            super().add(element)
        else:
            raise TypeError(f"{element} is not a Livery.")


class Liveries:
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
        if len(Liveries.map) == 0:
            install, saved_games = read_liberation_preferences()
            Liveries.initialize(install, saved_games)

    def __getitem__(self, unit: str) -> LiverySet:
        liveries = Liveries.map.get(unit)
        return liveries if liveries is not None else LiverySet(unit)

    def __setitem__(self, unit: str, liveries: LiverySet) -> None:
        if unit in Liveries.map:
            Liveries.map[unit].update(liveries)
        else:
            Liveries.map[unit] = liveries

    def __delitem__(self, unit: str) -> None:
        del Liveries.map[unit]

    def __iter__(self) -> Iterator[str]:
        return Liveries.map.__iter__()

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
        Liveries.map.clear()
        Liveries.scan_dcs_installation(install)
        Liveries.scan_custom_liveries(saved_games)

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
        path_id = path.split('\\')[-1].replace(".zip", "")
        if path_id == "placeholder":
            return
        livery_name = regex_group_extractor(r'^name\s*=\s*"(.*)"\s*(?:--.*)?$', luacode, path_id)

        regex = r'^countries\s*=\s*(\{\s*"[A-Z]+"\s*(?:,\s*"[A-Z]+"\s*)*\s*,?\s*\})\s*(?:--.*)?$'
        countries = regex_group_extractor(regex, luacode)
        if countries is not None:
            exec(f"country_list = {countries}")
            countries = set(filter(lambda x: x != "", locals()['country_list']))

        order = regex_group_extractor(r'^order\s*=\s*(-?[0-9]+)\s*(?:--.*)?$', luacode, 0)
        order = None if path_id == "default" else order
        if order is not None and not isinstance(order, int):
            try:
                order = int(order)
            except ValueError:
                order = 0

        livery = Livery(path_id, livery_name, order, countries)
        Liveries.map[unit].add(livery)
        setattr(Liveries.map[unit], safe_name(livery.id), livery)

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
                Liveries.scan_lua_code(code, path, unit)

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
            with zipfile.ZipFile(path, 'r') as zf:
                if "description.lua" in zf.namelist():
                    with zf.open("description.lua", "r") as file:
                        code = _attempt_read_from_filestream(file.read())
                        if code is None:
                            logging.warning(f" Unknown encoding found in '{path}/description.lua'")
                            return
                        Liveries.scan_lua_code(code, path, unit)

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
            if unit not in Liveries.map:
                Liveries.map[unit] = LiverySet(unit)
                setattr(Liveries, safe_name(unit), Liveries.map[unit])
            for livery in os.listdir(liveries_path):
                livery_path = os.path.join(liveries_path, livery)
                if os.path.isdir(livery_path):
                    Liveries.scan_lua_description(livery_path, unit)
                elif os.path.isfile(livery_path) and ".zip" in livery_path:
                    Liveries.scan_zip_file(livery_path, unit)

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
                Liveries.scan_liveries(liveries_path)

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
                Liveries.scan_liveries(liveries_path, campaign_path=True)

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

        Liveries.scan_mods_path(path1)
        Liveries.scan_mods_path(path2)
        Liveries.scan_liveries(path3)
        Liveries.scan_campaign_liveries(path4)
        Liveries.scan_mods_path(path5)
        Liveries.scan_liveries(path6)

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

        Liveries.scan_liveries(path1)
        Liveries.scan_mods_path(path2)


if __name__ == "__main__":
    generate_stub()  # generates the stub file for auto-completion

    # from planes import FA_18C_hornet, F_16C_50, F_14B, F_15E, A_10C_2, Liveries
    # # for some reason 'Liveries' in the current scope is a different object
    #
    # f18 = FA_18C_hornet()
    # print(f18.livery_name, sorted(f18.Liveries))
    # print(f18.default_livery("CAN"))
    # print(f18.default_livery("ISR"))
    # print(f18.default_livery("USA"))
    #
    # f14 = F_14B()
    # print(f14.livery_name, sorted(f14.Liveries))
    # print(f14.default_livery("USA"))
    # print(f14.default_livery("IRN"))
    # print(f14.default_livery("GRC"))
    # print(f14.default_livery("POL"))
    #
    # f15 = F_15E()
    # print(f15.livery_name, sorted(f15.Liveries))
    # print(f15.default_livery("USA"))
    # print(f15.default_livery("ISR"))
    # print(f15.default_livery("GRC"))
    # print(f15.default_livery("POL"))
    #
    # a10c2 = A_10C_2()
    # print(a10c2.livery_name, sorted(a10c2.Liveries))
    # print(a10c2.default_livery("USA"))
    # print(a10c2.default_livery("ISR"))
    # print(a10c2.default_livery("GRC"))
    # print(a10c2.default_livery("POL"))
    #
    # f16 = F_16C_50()
    # print(f16.livery_name, sorted(f16.Liveries))
    # print(f16.default_livery("USA"))
    # print(f16.default_livery("ISR"))
    # print(f16.default_livery("GRC"))
    # print(f16.default_livery("POL"))
    #
    # from helicopters import AH_64D_BLK_II
    # ah64 = AH_64D_BLK_II()
    # print(ah64.livery_name, sorted(ah64.Liveries))
    # print(ah64.default_livery("USA"))
    # print(ah64.default_livery("ISR"))
    #
    # print(Liveries.A_10A)
    # print(Liveries.F_16C_50.x14th_Fighter_Squadron)
    # print(Liveries.F_16C_50.x14th_Fighter_Squadron.order)
    # print(Liveries.F_16C_50.x14th_Fighter_Squadron.countries)
    # print(Liveries.map[Liveries.LEOPARD_2.unit_livery_id])
    #
    # from dcs.liveries_scanner import Livery
    # tester = Livery("Test_ID", "___TEST NAME___", 0, None)
    # Liveries.AH_64D_BLK_II.add(tester)
    # Liveries.AH_64D_BLK_II.add(Livery("Test_ID", "___TEST NAME___", 0, None))
    # print(Liveries.AH_64D_BLK_II)
    # print()
    # for livery in Liveries.LEOPARD_2:
    #     print(livery.id, livery.name, livery.order, livery.countries)
    # print()
    # for livery in Liveries.FA_18C_HORNET:
    #     print(livery.id, livery.name, livery.order, livery.countries)

    # skins = Liveries()
    # for u in skins:
    #     print(u)
    #     for liv in sorted(skins[u]):
    #         print("\t", liv, liv.countries)
