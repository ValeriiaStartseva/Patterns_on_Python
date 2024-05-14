from functools import lru_cache
import threading


class CacheSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.cache = {}
        return cls._instance

    @lru_cache(maxsize=None)
    def get_from_cache(self, key):
        with self._lock:
            return self.cache.get(key)

    def add_to_cache(self, key, value):
        with self._lock:
            self.cache[key] = value

    def remove_from_cache(self, key):
        with self._lock:
            if key in self.cache:
                del self.cache[key]

# testing


# create obj
cache = CacheSingleton()

# add data to cache
cache.add_to_cache("key1", "value1")

# get data
print(cache.get_from_cache("key1"))  # value1
