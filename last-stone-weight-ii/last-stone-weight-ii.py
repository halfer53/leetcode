class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        tsum = sum(stones)
        target = tsum // 2
        dp = [[0] * (target+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(target+1):
                if j < stones[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - stones[i-1]] + stones[i-1])
        return tsum - dp[n][target] * 2