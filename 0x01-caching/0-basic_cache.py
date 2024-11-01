#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from BaseCaching
and is a caching system:

Must use self.cache_data - dictionary from the parent
class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value
for the key key.
If key or item is None, method should not do anything.
def get(self, key):Must return the value in self.cache_data
linked to key. If key is None or if the key doesn’t exist in
self.cache_data, return None.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that inherits from BaseCaching which allows
    storing and retrieving items from a dictionary
    """
    def put(self, key, item):
        """Assign items to the cache dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key"""
        return self.cache_data.get(key, None)
