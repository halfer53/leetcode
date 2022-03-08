class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dfs(i: int) -> bool:
            if i >= n:
                return False
            if (n - i - 1) <= nums[i]:
                return True
            for j in range(i + 1, i + nums[i] + 1):
                ret = dfs(j)
                if ret:
                    return ret
            return False
        return dfs(0)