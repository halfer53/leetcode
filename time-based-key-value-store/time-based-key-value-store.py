class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = collections.defaultdict(list)
        self.dic = collections.defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key][timestamp] = value
        idx = bisect.bisect(self.time[key], timestamp)
        self.time[key].insert(idx, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.dic[key]:
            return self.dic[key][timestamp]
        idx = bisect.bisect_left(self.time[key], timestamp)
        if idx == 0:
            return ''
        idx -= 1
        return self.dic[key][self.time[key][idx]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)