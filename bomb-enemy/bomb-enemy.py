class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * 4 for i in range(m)] for _ in range(n)]
        ret = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 'W':
                    add = 1 if grid[i][j] == 'E' else 0
                    if i == 0 and j:
                        dp[i][j][0] = add
                        dp[i][j][1] = dp[i][j-1][1] + add
                    elif j == 0 and i:
                        dp[i][j][1] = add
                        dp[i][j][0] = dp[i-1][j][0] + add
                    elif i == 0 and j == 0:
                        dp[i][j][1] = add
                        dp[i][j][0] = add
                    else:
                        dp[i][j][0] = dp[i-1][j][0] + add
                        dp[i][j][1] = dp[i][j-1][1] + add
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if grid[i][j] != 'W':
                    add = 1 if grid[i][j] == 'E' else 0
                    if i == n-1 and j < m-1:
                        dp[i][j][2] = add
                        dp[i][j][3] = dp[i][j+1][3] + add
                    elif j == m-1 and i < n-1:
                        dp[i][j][3] = add
                        dp[i][j][2] = dp[i+1][j][2] + add
                    elif i == n-1 and j == m-1:
                        dp[i][j][2] = add
                        dp[i][j][3] = add
                    else:
                        dp[i][j][2] = dp[i+1][j][2] + add
                        dp[i][j][3] = dp[i][j+1][3] + add
                    if grid[i][j] == '0':
                        ret = max(ret, sum(dp[i][j]))
        return ret
                
                    
                    