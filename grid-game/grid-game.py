class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix = copy.deepcopy(grid)
        prefix[0][0] = 0
        prefix[1][n-1] = 0
        for i in range(1, n):
            prefix[0][i] += prefix[0][i-1]
            prefix[1][i] += prefix[1][i-1]
        print(prefix)
        r1 = prefix[0][n-1]
        r2 = prefix[1][n-1]
        ret = min(r1, r2)
        for i in range(1, n-1):
            ret = min(ret, max(prefix[0][n-1] - prefix[0][i], prefix[1][i-1]))
        return ret