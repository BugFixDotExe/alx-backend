#!/usr/bin/env python3
'''
A Python script that  that inherits from BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(list(self.cache_data)) >= BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data)[0]
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')
            
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        if self.cache_data[key] is None:
            return None
        return self.cache_data[key]
