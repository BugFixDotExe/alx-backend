#!/usr/bin/env python3
'''
A Python script that  that inherits from BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''
    LRUCache a class that inherits BaseCaching
    '''
    def __init__(self) -> None:
        '''
        initializing the parent constructor so as to have
        access to the internal cache dict
        '''
        super().__init__()
        self.key_tracker = [] # This behaves like a stack
    
        
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

        if key not in self.internal_dict:
            self.internal_dict[key] = 0

        if len(list(self.cache_data)) >= BaseCaching.MAX_ITEMS:
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
