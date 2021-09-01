class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q = []
        for i, t in enumerate(tasks):
            heapq.heappush(q, (t[0], t[1], i))
        ret = []
        available = []
        time = 1
        while q or available:
            while q and time >= q[0][0]:
                enque, process, idx = heapq.heappop(q)
                heapq.heappush(available, (process, idx))
            if available:
                process, idx = heapq.heappop(available)
                ret.append(idx)
                time += process
            elif q:
                time = q[0][0]
        return ret