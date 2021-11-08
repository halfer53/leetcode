class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ret = float('inf')
        left = copy.deepcopy(grid)
        right = copy.deepcopy(grid)
        for i in range(1, n):
            leftmin = float('inf')
            rightmin = float('inf')
            for j in range(n):
                if j:
                    left[i][j] += leftmin
                leftmin = min(leftmin, left[i-1][j])
            for j in reversed(range(n)):
                if j < n - 1:
                    right[i][j] += rightmin
                rightmin = min(rightmin, right[i-1][j])
            for j in range(n):
                val = float('inf')
                if j > 0:
                    val = left[i][j]
                if j < n - 1:
                    val = min(val, right[i][j])
                grid[i][j] = val
                left[i][j] = grid[i][j]
                right[i][j] = grid[i][j]
                if i == n - 1:
                    ret = min(grid[i][j], ret)
        return ret if ret != float('inf') else min(grid[0])