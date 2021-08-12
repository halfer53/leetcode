class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.map = dict()
        last = size = n - len(blacklist)
        self.limit = size
        blackset = set(blacklist)
        for b in blacklist:
            if b >= size:
                continue
            while last in blackset:
                last += 1
            self.map[b] = last
            last += 1

    def pick(self) -> int:
        val = random.randint(0, self.limit - 1)
        if val in self.map:
            return self.map[val]
        return val


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()