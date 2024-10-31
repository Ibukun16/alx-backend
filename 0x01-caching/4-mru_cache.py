#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from BaseCaching
and is a caching system:

Must use self.cache_data - dictionary from the parent
class BaseCaching
Can overload def __init__(self): but don’t forget to
call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value
for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following
by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A base class that allows storing and retrieving items from a
    dictionary with an MRU mechanism
    """
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adding items to the cache dictionary"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """Retrieves items from the dictionary by their key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
