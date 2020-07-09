class LRUCache:
    def __init__(self, capacity: int): 
		self.cache = OrderedDict() 
		self.capacity = capacity

    def get(self, key: int) -> int: 
		if key not in self.cache: 
			return -1
		else: 
			self.cache.move_to_end(key) 
			return self.cache[key] 