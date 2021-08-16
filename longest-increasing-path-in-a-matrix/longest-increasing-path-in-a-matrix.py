class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.visited = set()
        ret = 0
        m = len(matrix)
        n = len(matrix[0])
        
        @cache
        def dfs(i: int, j: int) -> int:
            result = 1
            for x,y in [[i-1, j], [i+1,j], [i,j+1], [i, j-1]]:
                if not (0 <= x < m and 0 <= y < n):
                    continue
                if matrix[x][y] > matrix[i][j]:
                    result = max(result, dfs(x, y) + 1)
            return result
        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i, j))
        return ret
            