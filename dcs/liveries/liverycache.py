from typing import Dict, Optional

from .liveryscanner import LiveryScanner
from .liveryset import LiverySet


class LiveryCache:
    _cache: Optional[Dict[str, LiverySet]] = None

    @classmethod
    def cache(cls) -> Dict[str, LiverySet]:
        if cls._cache is None:
            cls._cache = LiveryScanner().load()
        return cls._cache

    @classmethod
    def __getitem__(cls, unit: str) -> LiverySet:
        try:
            return LiveryCache.cache()[unit]
        except KeyError:
            return LiverySet(unit)
