#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and
is a caching system:

Must use self.cache_data - dictionary from the parent class
BaseCaching
Can overload def __init__(self): but don’t forget to call the
parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for
the key key.
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
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A base class that stores and retrieves item from a
    cache dictionary using the LFU algorithm
    """
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """
        Reorders the items n the cache based on the most recently
        used item in the cache dictionary
        """
        highest = []
        mru_freq = 0
        mru_position = 0
        ins_pos = 0
        for l, k in enumerate(self.keys_freq):
            if k[0] == mru_key:
                mru_freq = k[1] + 1
                mru_pos = l
                break
            elif len(highest) == 0:
                highest.append(l)
            elif k[1] < self.keys_freq[highest[-1]][1]:
                highest.append(l)
        highest.reverse()
        for p in highest:
            if self.keys_freq[p][1] > mru_freq:
                break
            ins_pos = p
        self.keys_freq.pop(mru_position)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Add items to the cache dictionary"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, k in enumerate(self.keys_freq):
                if k[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves items from the cache dictionary by their key."""
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
