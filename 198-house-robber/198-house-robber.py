class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][i] = nums[i-1]
            for j in range(i+1, n+1):
                dp[i][j] = max(dp[i][j-1], nums[j-1] + dp[i][j - 2])
        return max(dp, key=lambda x: x[-1])[-1]