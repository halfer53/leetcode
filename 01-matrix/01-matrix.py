class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if i:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
                else:
                    dp[i][j] = mat[i][j]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if mat[i][j]:
                    if i < m -1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                    if j < n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        return dp