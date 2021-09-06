class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        ret = [[-1] * n for _ in range(m)]

        q = collections.deque([])
        visited = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    ret[i][j] = 0
                    q.append((i,j))
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                val = ret[x][y]
                for dx, dy in [[-1,0], [1,0],[0, -1], [0,1]]:
                    xx = x + dx
                    yy = y + dy 
                    if 0 <= xx < m and 0 <= yy < n and ret[xx][yy] == -1:
                        ret[xx][yy] = val + 1
                        if (xx, yy) not in visited:
                            q.append((xx, yy))
                            visited.add((xx, yy))
        return ret
                    