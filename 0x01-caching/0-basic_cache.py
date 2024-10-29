#!/usr/bin/python3
'''Simple BasicCache'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache class'''
    def put(self, key, item):
        '''assigns to the dictionary self.cache_data
        the item value for the key key'''
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' returns the value in self.cache_data linked to key.'''
        if key:
            if key not in self.cache_data.keys():
                return
            return self.cache_data[key]
