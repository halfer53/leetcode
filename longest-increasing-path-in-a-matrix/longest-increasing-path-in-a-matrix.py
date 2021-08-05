class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.mem = [[0] * self.n for _ in range(self.m)]
        self.matrix = matrix
        ret = 0
        for i in range(self.m):
            for j in range(self.n):
                ret = max(ret, self.dfs(i, j))
        return ret
        
    def dfs(self, i: int, j: int) -> int:
        ret = 0
        if self.mem[i][j]:
            return self.mem[i][j]
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            x = dx + i
            y = dy + j
            if 0 <= x < self.m and 0 <= y < self.n and self.matrix[x][y] > self.matrix[i][j]:
                ret = max(ret, self.dfs(x, y))
        ret += 1
        self.mem[i][j] = ret
        return ret