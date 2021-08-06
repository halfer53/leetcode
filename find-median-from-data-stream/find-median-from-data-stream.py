class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) >= len(self.large):
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, -(heapq.heappop(self.small)))
        else:
            heapq.heappush(self.large, num)
            heapq.heappush(self.small, -(heapq.heappop(self.large)))
        
    def findMedian(self) -> float:
        m = len(self.small)
        n = len(self.large)
        
        ret = 0
        if m == n:
            ret = ((-self.small[0]) + self.large[0]) / 2
        elif m > n:
            ret = -self.small[0]
        else:
            ret = self.large[0]
        return ret
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()