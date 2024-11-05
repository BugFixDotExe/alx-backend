#!/usr/bin/env python3
'''
A Python script that  that inherits from BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
    LFUCache a class that inherits BaseCaching
    '''
    def __init__(self) -> None:
        '''
        initializing the parent constructor so as to have
        access to the internal cache dict
        '''
        super().__init__()
        self.internal_dict = {}
    
        
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
            val_based_sort = {k: v for k, v in sorted(self.internal_dict.items(), key=lambda item: item[1])}
            for internal_key, internal_value in val_based_sort.items():
                del self.cache_data[internal_key]
                del self.internal_dict[internal_key]
                print(f'DISCARD: {internal_key}')
                break
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
            if self.internal_dict.get(key) is not None:
                self.internal_dict[key] += 1
            return self.cache_data.get(key)
