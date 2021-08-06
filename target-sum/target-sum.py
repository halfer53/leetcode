class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.target = target
        self.nums = nums
        self.n = len(nums)
        self.mem = dict()
        return self.backtrack(0, 0)
        
    def backtrack(self, i: int, curr: int):
        if i >= self.n:
            if curr == self.target:
                return 1
            return 0
        if (i, curr) in self.mem:
            return self.mem[(i, curr)]
        num = self.nums[i]
        r1 = self.backtrack(i + 1, curr - num)
        r2 = self.backtrack(i + 1, curr + num)
        ret = r1 + r2
        self.mem[(i,curr)] = ret
        return ret