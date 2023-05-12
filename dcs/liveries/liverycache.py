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
    def for_unit(cls, livery_id: str) -> LiverySet:
        try:
            return LiveryCache.cache()[livery_id]
        except KeyError:
            return LiverySet(livery_id)

    @classmethod
    def __getitem__(cls, livery_id: str) -> LiverySet:
        return cls.for_unit(livery_id)
