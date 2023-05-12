from typing import Optional, Set

from .livery import Livery


class LiverySet(Set[Livery]):
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
