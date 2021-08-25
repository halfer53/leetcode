class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1
        dp = [1.0] + [0.0] * n
        wsum = 1.0
        for i in range(1, n+1):
            dp[i] = wsum / maxPts
            if i < k:
                wsum += dp[i]
            if i >= maxPts:
                wsum -= dp[i - maxPts]
        return sum(dp[k:])