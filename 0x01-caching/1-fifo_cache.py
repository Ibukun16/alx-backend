#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching
Use self.cache_data - dictionary from the parent class BaseCaching
Can overload def __init__(self): but must remeber to call
the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, do nothing.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
Must discard the first item put in cache (FIFO algorithm)
Must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    A class that represent an object that allows the stroring and retrieval
    of items from a dictionary with a FIFO removal mechanism when the limit is
    reached
    """
    def __init__(self):
        """Initializing the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves the items store in the dictionary by their key"""
        return self.cache_data.get(key, None)
