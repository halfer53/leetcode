class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        n = len(rods)
        for r in rods:
            curr = collections.defaultdict(int)
            for s in dp:
                curr[s+r] = max(dp[s] + r, curr[s+r])
                curr[s] = max(dp[s], curr[s])
                curr[s-r] = max(dp[s], curr[s-r])
            dp = curr
        return dp[0]
                
                    