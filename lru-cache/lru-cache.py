class LRUCache:
    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        ret = -1
        if key in self.dic:
            ret = self.dic[key]
            self.dic.move_to_end(key)
        return ret

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            evicted = self.dic.popitem(last=False)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)