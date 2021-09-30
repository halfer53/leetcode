class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(i: int, curr: int) -> int:
            if i >= n and curr == target:
                return 1
            if i >= n:
                return 0
            positive = dfs(i+1, curr + nums[i])
            negative = dfs(i+1, curr - nums[i])
            return positive + negative
        return dfs(0, 0)
        