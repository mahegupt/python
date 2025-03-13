from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity:int) :
        self.cache = OrderedDict() 
        self.capacity = capacity
    
    def get(self, key: int) -> int :
        #If key exist, move it to end to make sure it is being recently used and return value.
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    #Update the val if key exist in cache, if cache is full, remove least recent used key and add value to cache.
    def put(self, key: int, val:int) ->None:
        #If key exit, move it to end to make sure it is being used and update the value.
        if key in self.cache:
            self.cache.move_to_end(key)
        #If cache is full, remove the least recent used(first element)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        ## Update the value in cache for key.
        self.cache[key] = val

lru = LRUCache(2)
lru.put(1, 1)   # Cache: {1: 1}
lru.put(2, 2)   # Cache: {1: 1, 2: 2}
print(lru.get(1))  # Access key 1, Output: 1. Cache: {2: 2, 1: 1}
lru.put(3, 3)   # Add key 3, evicts key 2. Cache: {1: 1, 3: 3}
print(lru.get(2))  # Key 2 is not found. Output: -1