class Solution:
    def rob(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], nums[i])
            if i >= 2:
                for j in range(i - 1):
                    dp[i] = max(dp[i], dp[j] + nums[i])
        return dp[n-1]