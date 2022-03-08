class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i: int) -> int:
            if i >= n - 1:
                return 0
            ret = float('inf')
            for j in range(i+1, i+1+nums[i]):
                ret = min(ret, dfs(j) + 1)
            return ret
        return dfs(0)