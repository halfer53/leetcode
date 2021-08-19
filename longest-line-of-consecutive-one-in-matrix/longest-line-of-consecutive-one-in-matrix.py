class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        line = copy.deepcopy(mat)
        vertical = copy.deepcopy(mat)
        diagonal = copy.deepcopy(mat)
        antidiagonal = copy.deepcopy(mat)
        ret = mat[0][0]
        for i in range(m):
            for j in range(n):
                if line[i][j] and i:
                    line[i][j] = max(line[i][j], line[i-1][j] + 1)
                    ret = max(ret, line[i][j])
        for i in range(m):
            for j in range(n):
                if vertical[i][j] and j:
                    vertical[i][j] = max(vertical[i][j], vertical[i][j-1] + 1)
                    ret = max(ret, vertical[i][j])
        for i in range(m):
            for j in range(n):
                if diagonal[i][j] and i and j:
                    diagonal[i][j] = max(diagonal[i][j], diagonal[i-1][j-1] + 1)
                    ret = max(ret, diagonal[i][j])
        for i in range(m):
            for j in range(n):
                if antidiagonal[i][j] and i and j < n - 1:
                    antidiagonal[i][j] = max(antidiagonal[i][j], antidiagonal[i-1][j+1] + 1)
                    ret = max(ret, antidiagonal[i][j])
        return ret