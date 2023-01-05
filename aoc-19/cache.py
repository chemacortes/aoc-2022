from collections.abc import Hashable
from typing import TypeVar

T = TypeVar("T")


class Cache(dict[Hashable, T | None]):
    def __init__(self):
        self._cache: dict[Hashable, T] = {}
        self._cache_info = {"hits": 0}

    @property
    def cache_info(self) -> str:
        return f"Cache<hits={self._cache_info['hits']}>"

    def clear(self):
        self._cache.clear()

    def __getitem__(self, key: Hashable) -> T | None:
        res: T | None = self._cache.get(key, None)
        if res is not None:
            self._cache_info["hits"] += 1
        return res

    def __setitem__(self, key: Hashable, value: T | None):
        match value:
            case None:
                if key in self._cache:
                    del self._cache[key]
            case _:
                self._cache[key] = value

    def __delitem__(self, key: Hashable):
        if key in self._cache:
            del self._cache[key]
