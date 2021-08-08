class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        # 0 for sell, 1 for buy
        for i in range(n):
            dp[i][1] = -float('inf')
        for i in range(n):
            p = prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + p - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - p)
        return dp[n-1][0]