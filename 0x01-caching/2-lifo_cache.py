#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching
and is a caching system:

Must use self.cache_data - dictionary from the parent
class BaseCaching
You can overload def __init__(self): but don’t forget to
call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item
value for the key key. If key or item is None, this
method should not do anything. If the number of items in
self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A base class that inherits from BaseCaching system that implement
    Last-In-First-Out cache algorithm
    """
    def __init__(self):
        """Initializes the LIFO cache"""
        super().__init__()

    def put(self, key, item):
        """Add item into the cache dictionary for storing and retrieval"""
        if key is None or item is None:
            return
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """Retrieve items from the cache dictionary by their key"""
        return self.cache_data.get(key, None)
