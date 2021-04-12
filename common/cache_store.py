from typing import Any
import time
import pickle

class CacheStore:
    '''
        Implement a key/value store/cache.
        Working only with args which can have 'method' and 'path' attributes
    '''

    def __init__(self, capacity:int=2, ttl:int=5) -> None:
        '''
            cache - dict where save all data 
            capacity - length cache store
            ttl - time live key value in store
        '''
        self.cache: dict = {}
        self.capacity: int = capacity
        self.ttl: int = ttl

    def get(self, func, args) -> dict:
        '''
            func - function to implement
            args - parameters send to func
        '''
        key: str = f'{args.method}_{args.path}'
        if key not in self.cache or self.cache[key][1]<time.time():
            response = func(args)
            self.put(key, response)
            return response
        return self.cache[key][0]

    def put(self, key, value):
        '''
            put value into dict
        '''
        if self.capacity < len(self.cache):
            self.cache.pop()
        self.cache[key]: tuple = (self._write_to(value), time.time()+self.ttl)

    def _write_to(self, value: Any):
        '''
            serializer, depending on the requirement
        '''
        return value
 
cache = CacheStore()

