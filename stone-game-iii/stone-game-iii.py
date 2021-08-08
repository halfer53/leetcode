class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @cache
        def dfs(i: int, turn: bool) -> int:
            if i >= n:
                return 0
            
            if turn:
                v1 = r1 = v2 = r2 = v3 = r3 = -float('inf')
                v1 = stoneValue[i]
                r1 = dfs(i + 1, not turn)
                if n - i >= 2:
                    v2 = sum(stoneValue[i:i+2])
                    r2 = dfs(i + 2, not turn)
                if n - i >= 3:
                    v3 = sum(stoneValue[i:i+3])
                    r3 =  dfs(i + 3, not turn)
                return max(v1 + r1, v2 + r2, v3 + r3)
            else:
                v1 = r1 = v2 = r2 = v3 = r3 = -float('inf')
                v1 = stoneValue[i]
                r1 = dfs(i + 1, not turn)
                if n - i >= 2:
                    v2 = sum(stoneValue[i:i+2])
                    r2 = dfs(i + 2, not turn)
                if n - i >= 3:
                    v3 = sum(stoneValue[i:i+3])
                    r3 =  dfs(i + 3, not turn)
                return min(-v1 + r1, -v2 + r2, -v3 + r3)
            
        ret = dfs(0, True)
        if ret > 0:
            return 'Alice'
        elif ret < 0:
            return 'Bob'
        else:
            return 'Tie'