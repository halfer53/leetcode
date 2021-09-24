class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * n
        suffix[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = piles[i] + suffix[i+1]
        @cache
        def dfs(i: int, m: int) -> int:
            if i >= n:
                return 0
            nextplayer = suffix[i]
            for x in range(1, 2*m+1):
                nextplayer = min(nextplayer, dfs(i+x, max(x, m)) )
            return suffix[i] - nextplayer
        return dfs(0, 1)
            