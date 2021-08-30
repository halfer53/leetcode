class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = collections.defaultdict(int)
        for t in transactions:
            m[t[0]] -= t[2]
            m[t[1]] += t[2]
        debt = list(m.values())
        
        def dfs(s: int) -> int:
            while s < len(debt) and debt[s] == 0:
                s += 1
            if s >= len(debt):
                return 0
            ret = float('inf')
            for i in range(s+1, len(debt)):
                if debt[i] * debt[s] < 0:
                    debt[i] += debt[s]
                    ret = min(ret, dfs(s + 1) + 1)
                    debt[i] -= debt[s]
            return ret
        return dfs(0)