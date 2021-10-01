class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tsum = sum(nums)
        n = len(nums)
        if (tsum + target) % 2 != 0 or tsum < abs(target):
            return 0
        s1 = (tsum + target) // 2
        dp = [[0] * (s1+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range( s1+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j - nums[i-1]] + dp[i-1][j]
        return dp[n][s1]
        
        