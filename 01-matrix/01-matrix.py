class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ret = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if j:
                        ret[i][j] = min(ret[i][j], ret[i][j-1] + 1)
                    if i:
                        ret[i][j] = min(ret[i][j], ret[i-1][j] + 1)
                else:
                    ret[i][j] = mat[i][j]
        for i in reversed(range( m)):
            for j in reversed(range( n)):
                if j < n - 1:
                    ret[i][j] = min(ret[i][j], ret[i][j+1] + 1)
                if i < m - 1:
                    ret[i][j] = min(ret[i][j], ret[i+1][j] + 1)
        return ret