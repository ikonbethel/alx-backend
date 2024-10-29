#!/usr/bin/python3
'''LFUCache Caching System'''
from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    '''LFUCache Caching System'''

    def __init__(self):
        '''Init method'''
        super().__init__()
        self._d_count = {}
        self._d_time = {}

    def put(self, key, item):
        '''assigns to the dictionary self.cache_data
        the item value for the key key'''
        if not key or not item:
            return
        if key in self.cache_data.keys():
            self._d_count[key] += 1
        else:
            self._d_count[key] = 1
        self._d_time[key] = datetime.now()
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # print(self._d_count)
            min_val = min(list(v for k, v in
                               self._d_count.items() if k is not key))
            min_list = [k for k, v in
                        self._d_count.items() if v == min_val]
            minkey = min_list[0]
            # print(min_list)
            if len(min_list) > 1:
                min_time = [v for k, v in
                            self._d_time.items() if k in min_list]
                min_list = [k for k, v in
                            self._d_time.items() if v == min(min_time)]
                minkey = min_list[0]
                # print(minkey)

            del self.cache_data[minkey]
            del self._d_count[minkey]
            del self._d_time[minkey]
            print(f"DISCARD: {minkey}")

    def get(self, key):
        ''' returns the value in self.cache_data linked to key.'''
        if key:
            if key not in self.cache_data.keys():
                return
            self._d_count[key] += 1
            self._d_time[key] = datetime.now()
            return self.cache_data[key]
