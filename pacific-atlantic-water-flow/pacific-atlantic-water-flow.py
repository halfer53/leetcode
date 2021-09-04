class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        if m == 0:
            return []
        n = len(heights[0])
        atlantic = collections.deque([])
        pacific = collections.deque([])
        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n-1))
        for j in range(n):
            pacific.append((0, j))
            atlantic.append((m-1, j))
        def bfs(queue) -> Dict:
            valid = set()
            while queue:
                i, j = queue.popleft()
                valid.add((i,j))
                for xx, yy in [[-1,0], [1, 0], [0,-1], [0,1]]:
                    x = xx + i
                    y = yy + j
                    if not (0 <= x < m and 0 <= y < n):
                        continue
                    if (x,y) in valid:
                        continue
                    if heights[x][y] < heights[i][j]:
                        continue
                    queue.append((x,y))
            return valid
        atset = bfs(atlantic)
        pacset = bfs(pacific)
        return list(atset.intersection(pacset))