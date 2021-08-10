class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 3 for i in range(3)] for j in range(n+1) ]
        for i in range(n+1):
            for j in range(3):
                dp[i][j][0] = 0
                dp[i][j][1] = -float('inf')
        for i in range(1, n+1):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i-1])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i-1] )
        return dp[n][2][0]