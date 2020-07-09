class LRUCache:
    def __init__(self, capacity: int): 
		self.cache = OrderedDict() 
		self.capacity = capacity 