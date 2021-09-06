class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = collections.deque([(0, 0)])
        visited = set()
        visited.add((0, 0))
        n = len(grid)
        step = 0
        if grid[0][0] == 1:
            return -1
        elif n == 1:
            return 1
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in [[-1,0],[-1,-1], [-1,1], [0, -1], [1,-1], [1,0], [1,1], [0, 1]]:
                    x = i + di
                    y = j + dj
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x,y) not in visited:
                        if x == n - 1 and y == n - 1:
                            return step + 2
                        q.append((x, y))
                        visited.add((x, y))
            step += 1
        return -1
                        