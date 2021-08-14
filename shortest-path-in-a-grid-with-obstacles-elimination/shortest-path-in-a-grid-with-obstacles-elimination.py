class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        seen = set((0, 0, k))
        queue = collections.deque([])
        m = len(grid)
        n = len(grid[0])
        queue.append((0, 0, k, 0))
        ret = float('inf')
        if m == 1 and n == 1:
            return 0
        while len(queue):
            size = len(queue)
            x, y, ok, step = queue.popleft()
            for px, py in [[-1,0], [1, 0], [0, -1], [0, 1]]:
                xx = x + px
                yy = y + py
                tk = ok
                if not (0 <= xx < m and 0 <= yy < n):
                    continue
                if grid[xx][yy] == 1:
                    tk -= 1
                if tk < 0:
                    continue
                if (xx, yy, tk) in seen:
                    continue
                if xx == m -1 and yy == n - 1:
                    ret = min(ret, step + 1)
                    continue
                queue.append((xx, yy, tk, step+1))
                seen.add((xx, yy, tk))
        return ret if ret != float('inf') else -1