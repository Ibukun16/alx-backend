#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching
and is a caching system:

You must use self.cache_data - dictionary from the parent
class BaseCaching You can overload def __init__(self): but
don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value
for the key key. If key or item is None, this method should
not do anything. If the number of items in self.cache_data is
higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by
a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A base class that inherits from BaseCaching that
    allows for storing and retrieval of data items from
    a dictionary with Least Recently Used cache algorithm
    """
    def __init__(self):
        """Initializing the cache algorithm"""
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """Adding item to the cache"""
        if key is None or item is None:
            return
        if key and item:
            self.cache_data[key] = item
        if key not in self.usedKeys:
            self.usedKeys.append(key)
        else:
            self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
        if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
            lru_key = self.usedKeys.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """Retrieves items from the cache dictionary by their key"""
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
        return self.cache_data.get(key, None)
