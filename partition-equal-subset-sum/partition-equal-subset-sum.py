class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tsum = sum(nums)
        if tsum % 2 != 0:
            return False
        target = tsum // 2
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(1, target+1):
                if j >= curr:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - curr]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]