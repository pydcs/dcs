from typing import Optional, Set


class Livery:
    id: str = ""
    """ID of the livery, corresponds with the folder-name of the livery. To be used in mission file!"""

    name: str = ""
    """Name of the livery as displayed in DCS"""

    order: int = 0
    """Order of the livery used to sort like DCS"""

    countries: Optional[Set[str]] = None
    """Set of short names indicating valid countries, with 'None' indicating all countries."""

    def __init__(
        self, path_id: str, name: str, order: int, countries: Optional[Set[str]]
    ) -> None:
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
