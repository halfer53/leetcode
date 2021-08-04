class Solution:
    def slidingPuzzle(self, inputboard: List[List[int]]) -> int:
        visited = set([tuple(inputboard[0] + inputboard[1])])
        queue = collections.deque([])
        step = 0
        m = 2
        n = 3
        nums = [ [1, 2, 3], [4, 5, 0]]
        queue.append(copy.deepcopy(inputboard))
        while len(queue):
            sz = len(queue)
            for _ in range(sz):
                board = queue.popleft()
                x = y = 0
                match = True
                for i in range(m):
                    for j in range(n):
                        if board[i][j] != nums[i][j]:
                            match = False
                        if board[i][j] == 0:
                            x = i
                            y = j
                if match:
                    return step
                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    i = (x + dx)
                    j = (y + dy)
                    if not ( 0 <= i < m and 0 <= j < n):
                        continue
                    tboard = copy.deepcopy(board)
                    tboard[x][y] = tboard[i][j]
                    tboard[i][j] = 0
                    if tuple(tboard[0] + tboard[1]) not in visited:
                        queue.append(tboard)
                        visited.add(tuple(tboard[0] + tboard[1]))
            step += 1
        return -1
        