class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp = [0] * n
        for j in range(2, n):
            if nums[j-2] - nums[j-1] == nums[j-1] - nums[j]:
                dp[j] = max(dp[j], dp[j-1] + 1)
        return sum(dp)