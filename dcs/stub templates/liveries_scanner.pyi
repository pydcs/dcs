from typing import Dict, Set, Optional, Iterator


class Livery:
    id: str = ""
    name: str = ""
    order: int = 0
    countries: set[str] | None = None

    def __init__(self, path_id: str, name: str, order: int, countries: Optional[Set[str]]) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def __lt__(self, other) -> bool:
        pass

    def __eq__(self, other) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def valid_for_country(self, country: str) -> bool:
        pass


class LiverySet(set):
    unit_livery_id: str = ""

    def __init__(self, unit_livery_id: Optional[str] = None) -> None:
        pass

    def __str__(self) -> str:
        pass

    def add(self, element: Livery) -> None:
        pass


class Liveries:
    map: Dict[str, LiverySet] = {}

    def __init__(self) -> None:
        pass

    def __getitem__(self, unit: str) -> LiverySet:
        pass

    def __setitem__(self, unit: str, liveries: LiverySet) -> None:
        pass

    def __delitem__(self, unit: str) -> None:
        pass

    def __iter__(self) -> Iterator[str]:
        pass

    @staticmethod
    def initialize(install: str, saved_games: str) -> None:
        pass

    @staticmethod
    def scan_lua_code(code: str, path: str, unit: str) -> None:
        pass

    @staticmethod
    def scan_dcs_installation(install: str) -> None:
        pass

    @staticmethod
    def scan_custom_liveries(saved_games: str) -> None:
        pass

    @staticmethod
    def scan_lua_description(livery_path: str, unit: str) -> None:
        pass

    @staticmethod
    def scan_zip_file(livery_path: str, unit: str) -> None:
        pass

    @staticmethod
    def scan_liveries(liveries_path: str, campaign_path: bool = False) -> None:
        pass

    @staticmethod
    def scan_mods_path(path: str) -> None:
        pass

    @staticmethod
    def scan_campaign_liveries(path: str) -> None:
        pass
