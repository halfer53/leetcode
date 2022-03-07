class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        se = collections.Counter(nums)
        n = len(nums)
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            j = i
            pt = nums[i]
            while i < n and abs(nums[i] - pt) <= 1:
                i += 1
            return max(dfs(j+1), pt * se[pt] + dfs(i))
        return dfs(0)
            