class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * n
        for i in range(n):
            w, h = envelopes[i]
            for j in range(i):
                pw, ph = envelopes[j]
                if pw < w and ph < h:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1