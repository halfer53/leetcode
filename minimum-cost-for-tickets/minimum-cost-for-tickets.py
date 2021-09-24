class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if i == n - 1:
                return min(costs)
            r1 = costs[0] + dfs(i+1)
            j = i
            while j < n and days[j] - days[i] <= 6:
                j += 1
            r2 = costs[1] + dfs(j)
            j = i
            while j < n and days[j] - days[i] <= 29:
                j += 1
            r3 = costs[2] + dfs(j)
            return min(r1, r2, r3)
        return dfs(0)