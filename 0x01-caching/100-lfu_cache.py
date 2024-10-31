#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and
is a caching system:

Must use self.cache_data - dictionary from the parent class
BaseCaching
Can overload def __init__(self): but don’t forget to call the
parent init: super().__init__()
def put(self, key, item): Must assign to the dictionary
self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU
algorithm to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A base class that stores and retrieves item from a
    cache dictionary using the LFU algorithm
    """
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.queue = []
        self.lfu_keys = {}

    def put(self, key, item):
        """Add items to the cache dictionary"""
        if key is None or item is None:
            return
        if key and item:
            if not self.cache_data.get(key):
                if len(self.queue) + 1 > BaseCaching.MAX_ITEMS:
                    delete = self.queue.pop(0)
                    self.lfu_keys.pop(delete)
                    self.cache_data.pop(delete)
                    print("DISCARD:", delete)

            if self.cache_data.get(key):
                self.queue.remove(key)
                self.lfu_keys[key] += 1
            else:
                self.lfu_keys[key] = 0

            indx = 0
            while (indx < len(self.queue)
                    and not self.lfu_keys[self.queue[indx]]):
                indx += 1
            self.queue.insert(indx, key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves items from the cache dictionary by their key."""
        if key is not None and self.cache_data.get(key):
            self.lfu_keys[key] += 1
            if self.queue.index(key) + 1 != len(self.queue):
                while(self.queue.index(key) + 1 < len(self.queue) and
                        self.lfu_keys[key] >=
                        self.lfu_keys[self.queue[self.queue.index(key) + 1]]):
                    self.queue.insert(self.queue.index(key) + 1,
                                      self.queue.pop(self.queue.index(key)))
        return self.cache_data.get(key, None)
