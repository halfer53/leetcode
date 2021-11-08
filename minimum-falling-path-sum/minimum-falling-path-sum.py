class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ret = float('inf')
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i > 0:
                    if j == 0:
                        matrix[i][j] = min(matrix[i-1][j+1], matrix[i-1][j]) + matrix[i][j]
                    elif j == n - 1:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j]) + matrix[i][j]
                    else:
                        matrix[i][j] = min(matrix[i-1][j+1], matrix[i-1][j], matrix[i-1][j-1]) + matrix[i][j]
                if i == n-1:
                    ret = min(ret, matrix[i][j])
        return ret