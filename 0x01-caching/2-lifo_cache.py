#!/usr/bin/python3
'''LIFOCache Caching System'''
from base_caching import BaseCaching
import time


class LIFOCache(BaseCaching):
    '''LIFOCache Caching System'''

    def __init__(self):
        super().__init__()
        self.d_time = {}

    def put(self, key, item):
        '''assigns to the dictionary self.cache_data
        the item value for the key key'''
        if not key or not item:
            return
        self.cache_data[key] = item
        self.d_time[key] = time.time()
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            max_time = max(list(v for k, v
                                in self.d_time.items() if k is not key))
            lasts = [k for k, v in self.d_time.items() if v == max_time]
            last_key = lasts[0]
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")

    def get(self, key):
        ''' returns the value in self.cache_data linked to key.'''
        if key:
            if key not in self.cache_data.keys():
                return
            return self.cache_data[key]
