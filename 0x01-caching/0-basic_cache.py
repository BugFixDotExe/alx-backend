#!/usr/bin/env python3
'''
A Python script that acts as a caching system
'''
from typing_extensions import Any
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    BasicCache a class that inherits BaseCaching
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
            pass
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
