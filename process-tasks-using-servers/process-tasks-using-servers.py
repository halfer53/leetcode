class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        serverq = []
        for i, s in enumerate(servers):
            heapq.heappush(serverq, (s, i))
        processq = []
        ret = []
        i = 0
        for i, t in enumerate(tasks):
            while len(processq) and processq[0][0] <= i:
                time, serverweight, serveri = heapq.heappop(processq)
                heapq.heappush(serverq, (serverweight, serveri))
            if serverq:
                serverweight, serveri = heapq.heappop(serverq)
            else:
                i, serverweight, serveri = heapq.heappop(processq)
            ret.append(serveri)
            heapq.heappush(processq, (i + t, serverweight, serveri))
        return ret