class Solution:
    def numTrees(self, n: int) -> int:
        self.m = [[0] * (n+1) for _ in range(n+1)]
        return self.count(1, n)
    
    def count(self, low: int, high: int) -> int:
        ret = 0
        if low >= high:
            return 1
        if self.m[low][high]:
            return self.m[low][high]
        for i in range(low, high + 1):
            left = self.count(low, i - 1)
            right = self.count(i + 1, high)
            ret += left * right
        self.m[low][high] = ret
        return ret