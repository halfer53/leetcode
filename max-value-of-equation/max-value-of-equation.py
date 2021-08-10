class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = []
        ret = -float('inf')
        stack = collections.deque([])
        n = len(points)
        for i in range(n):
            x, y = points[i]
            if len(q):
                while len(q) and x - q[0][1]> k:
                    heapq.heappop(q)
                if len(q):
                    val = -q[0][0] + x + y
                    ret = max(ret, val)
            heapq.heappush(q, (x - y, x, y))
        return ret