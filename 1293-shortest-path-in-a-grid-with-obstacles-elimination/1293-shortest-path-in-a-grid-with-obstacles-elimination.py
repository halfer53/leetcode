class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque([])
        m = len(grid)
        n = len(grid[0])
        q.append((0, 0, k))
        visited = set([(0, 0, k)])
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y, obstacles = q.popleft()
                if x == m - 1 and y == n - 1:
                    return steps
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    xx = x + dx
                    yy = y + dy
                    obstacles_left = obstacles
                    if (0 <= xx < m) and (0 <= yy < n):
                        if grid[xx][yy] == 1:
                            obstacles_left -= 1
                        if obstacles_left >= 0 and (xx, yy, obstacles_left) not in visited:
                            visited.add((xx, yy, obstacles_left))
                            q.append((xx, yy, obstacles_left))
            steps += 1
        return -1