#!/usr/bin/env python3
'''
A Python script that inherits from BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    MRUCache a class that inherits BaseCaching
    '''
    def __init__(self) -> None:
        '''
        initializing the parent constructor so as to have
        access to the internal cache dict
        '''
        super().__init__()
        self.key_tracker = []
        # This behaves like a stack to track MRU keys

    def put(self, key, item):
        '''
        put: A method that inserts items into the cache_data dict
        Args:
            key (String): The key to the item
            item (Any): The value to be stored
        Returns:
            Nothing
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.key_tracker.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is full, remove the most recently used item
            if self.key_tracker:
                mru_key = self.key_tracker.pop()
                del self.cache_data[mru_key]
                print(f'DISCARD: {mru_key}')

        # Insert the new item and update the key_tracker for MRU status
        self.cache_data[key] = item
        self.key_tracker.append(key)

    def get(self, key):
        '''
        get: A method to fetch the value of the given key from cache_data
        Args:
            key (String): A valid key
        Returns:
            The value attached to the key or None if the key doesn't exist
        '''
        if key is None or key not in self.cache_data:
            return None

        # If the key is found, update its status in the MRU tracker
        if key in self.key_tracker:
            self.key_tracker.remove(key)
        self.key_tracker.append(key)
        return self.cache_data[key]
