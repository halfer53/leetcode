class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        @lru_cache(None)
        def fn(k):
            """Return True if there is a winning strategy with k stones left."""
            if k <= 3: return True 
            for kk in range(1, 4):
                if not fn(k - kk): 
                    return True #opponent cannot win 
            return False 
        return fn(n)
                
        