class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1]
        last = {}
        for i, c in enumerate(s):
            dp.append(dp[-1] * 2)
            if c in last:
                dp[-1] -= dp[last[c] ]
            last[c] = i
        return (dp[-1] - 1) % (10**9+7)