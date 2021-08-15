class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        deadends = set(deadends)
        visited.add('0000')
        q = collections.deque([])
        q.append('0000')
        step = 0
        while len(q):
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr in deadends:
                    continue
                if curr == target:
                    return step
                for i in range(4):
                    for direction in [-1, 1]:
                        c = int(curr[i])
                        newc = (c + direction) % 10
                        newstr = curr[:i] + str(newc) + curr[i+1:]
                        if newstr not in visited:
                            visited.add(newstr)
                            q.append(newstr)
            step += 1
        return -1
    
        