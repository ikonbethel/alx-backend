#!/usr/bin/python3
'''LRUCache Caching System'''
from base_caching import BaseCaching
import time


class LRUCache(BaseCaching):
    '''LRUCache Caching System'''
    __d_count = {}

    def put(self, key, item):
        '''assigns to the dictionary self.cache_data
        the item value for the key key'''
        if not key or not item:
            return
        self.cache_data[key] = item
        LRUCache.__d_count[key] = time.time()
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min = time.time()
            l_diff = 0
            minkey = None
            for k, v in LRUCache.__d_count.items():
                diff = min - v
                if k == key:
                    continue
                if diff > l_diff:
                    l_diff = v
                    minkey = k
            if minkey:
                del self.cache_data[minkey]
                del LRUCache.__d_count[minkey]
            print(f"DISCARD: {minkey}")

    def get(self, key):
        ''' returns the value in self.cache_data linked to key.'''
        if key:
            if key not in self.cache_data.keys():
                return
            del LRUCache.__d_count[key]
            LRUCache.__d_count[key] = time.time()
            return self.cache_data[key]
