class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = collections.deque([])
        queue.append('0000')
        ret = float('inf')
        visited = set(['0000'])
        sdead = set(deadends)
        step = 0
        while len(queue):
            sz = len(queue)
            for i in range(sz):
                pos = queue.popleft()
                if pos in sdead:
                    continue
                if pos == target:
                    return step
                for j in range(4):
                    for d in [-1, 1]:
                        k = (int(pos[j]) + d ) % 10
                        val = pos[:j] + str(k) + pos[j+1:]
                        if val not in visited:
                            queue.append(val)
                            visited.add(val)
            step += 1
        return -1