class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        tmax = 0
        for val in nums:
            tmax |= val
        def dfs(i: int, curr: int) -> int:
            ret = 0
            if curr == tmax:
                ret += 1
            if i >= n:
                return ret
            # print(i, curr)
            for j in range(i, n):
                ret += dfs(j+1, curr | nums[j])
            return ret
        return dfs(0, 0)
            