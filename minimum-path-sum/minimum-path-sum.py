class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ret = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i and j == 0:
                    grid[i][j] += grid[i-1][j]
                elif j and i == 0:
                    grid[i][j] += grid[i][j-1]
                elif i and j:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]