class Solution:

    def __init__(self, w: List[int]):
        self.tsum = sum(w)
        self.arr = []
        curr = 0
        for i, weight in enumerate(w):
            curr += weight
            self.arr.append((curr, i))
        self.arr.sort(key= lambda x: x[0])
        self.weight, self.idx = zip(*self.arr)
        
    def pickIndex(self) -> int:
        val = random.randint(1, self.tsum)
        idx = bisect.bisect_left(self.weight, val)
        return self.idx[idx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()