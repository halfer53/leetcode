class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        tsum = sum(stones)
        total = tsum // 2
        dp = [[0] * (total+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, total+1):
                if stones[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - stones[i-1]] + stones[i-1])
        return tsum - 2 * dp[n][total]