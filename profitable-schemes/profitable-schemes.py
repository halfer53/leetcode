class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        grouplen = len(group)
        dp = [[[0] * (minProfit+1) for i in range(n+1)] for j in range(grouplen+1)]
        dp[0][0][0] = 1
        for k in range(1, grouplen+1):
            g = group[k-1]
            p = profit[k-1]
            for i in range(n+1):
                for j in range(minProfit+1):
                    dp[k][i][j] = dp[k-1][i][j]
                    if i >= g:
                        dp[k][i][j] += dp[k-1][i - g][max(0,j - p)]
        return sum([dp[grouplen][i][minProfit] for i in range(n+1)]) % (10**9 + 7)
        