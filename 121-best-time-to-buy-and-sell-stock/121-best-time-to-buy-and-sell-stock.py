class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        imin = float('inf')
        ret = -float('inf')
        for p in prices:
            ret = max(ret, p - imin)
            imin = min(imin, p)
        return ret if ret > 0 else 0