from typing import Optional, Set


class Livery:
    def __init__(
        self, path_id: str, name: str, order: int, countries: Optional[Set[str]]
    ) -> None:
        # ID to be used in the miz.
        self.id = path_id
        # Display name.
        self.name = name
        # UI sort order.
        self.order = order
        # List of countries that may use this livery. If None, all countries may use the
        # livery. The elements in this list are short names for countries, e.g. "USA"
        # or "RUS".
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
