class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @cache
        def dfs(i: int, turn: bool) -> int:
            if i >= n:
                return 0
            if turn:
                r1 = r2 = r3 = -float('inf')
                r1 = dfs(i+1, not turn) + stoneValue[i]
                if i < n - 1:
                    r2 = dfs(i + 2, not turn) + sum(stoneValue[i:i+2])
                if i < n - 2:
                    r3 = dfs(i + 3, not turn) + sum(stoneValue[i:i+3])
                return max(r1, r2, r3)
            else:
                r1 = r2 = r3 = float('inf')
                r1 = dfs(i + 1, not turn) - stoneValue[i]
                if i < n - 1:
                    r2 = dfs(i + 2, not turn) - sum(stoneValue[i:i+2])
                if i < n - 2:
                    r3 = dfs(i + 3, not turn) - sum(stoneValue[i:i+3])
                return min(r1, r2, r3)
        ret = dfs(0, True)
        if ret > 0:
            return 'Alice'
        elif ret < 0:
            return 'Bob'
        else:
            return 'Tie'