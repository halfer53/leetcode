class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        i = j = 0
        m = len(grid)
        n = len(grid[0])
        q = collections.deque([])
        visited = set()
        
        def dfs(k, l, val):
            if 0 <= k < m and 0 <= l < n and grid[k][l] == 1:
                grid[k][l] = val
                q.append((k,l))
                visited.add((k,l))
                dfs(k+1, l, val)
                dfs(k-1, l, val)
                dfs(k, l+1, val)
                dfs(k, l-1, val)
                
        found = False
        for k in range(m):
            for l in range(n):
                if not found and grid[k][l] == 1:
                    dfs(k, l, 2)
                    found = True
                    break
            if found:
                break
                    
        # print(q, visited)
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in visited:
                        if grid[xx][yy] == 1:
                            return step
                        if grid[xx][yy] == 0:
                            q.append((xx, yy))
                            visited.add((xx, yy))
            step += 1
        return -1