class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        q = collections.deque([])
        fresh_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_cnt += 1
        step = 0
        fresh_reached = 0
        if fresh_cnt == 0:
            return 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    xx = x + i
                    yy = y + j
                    if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy] and grid[xx][yy] == 1:
                        q.append((xx, yy))
                        fresh_reached += 1
                        visited[xx][yy] = True
            step += 1
            if fresh_reached == fresh_cnt:
                break
        if fresh_reached != fresh_cnt:
            return -1
        return step