#!/usr/bin/env python3
'''
A Python script that  that inherits from BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    LIFOCache a class that inherits BaseCaching
    '''
    def __init__(self) -> None:
        '''
        initializing the parent constructor so as to have
        access to the internal cache dict
        '''
        super().__init__()

    def put(self, key, item):
        '''
        put: A method that inserts items into the dict
        Args:
            key(String): The key to the item
            item(Any): The Value to be stored
        Returns:
            Nothing
        '''
        if key is None or item is None:
            return
        if len(list(self.cache_data)) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data)[-1]
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''
        get: A method when given a key fetches the value
        Args:
            key(string): A valid key
        Returns:
            The value attached to the key or None
        '''
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
