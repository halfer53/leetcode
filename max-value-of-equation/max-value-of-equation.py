class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = []
        ret = -float('inf')
        for xj, yj in points:
            while len(q) and xj - q[0][1] > k:
                heapq.heappop(q)
            if len(q):
                ret = max(ret, -q[0][0] + xj + yj)
            heapq.heappush(q, (-(yj - xj), xj))
        return ret