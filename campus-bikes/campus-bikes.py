class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distance = []
        for wi, w in enumerate(workers):
            distance.append([])
            for bi, b in enumerate(bikes):
                dis = abs(w[0] - b[0]) + abs(w[1] - b[1])
                heapq.heappush(distance[-1], (dis, wi, bi))
        ret = [-1] * len(workers)
        heap = [heapq.heappop(x) for x in distance]
        heapq.heapify(heap)
        bikeused = set()
        while len(bikeused) < len(ret):
            dis, wi, bi = heapq.heappop(heap)
            if bi not in bikeused:
                ret[wi] = bi
                bikeused.add(bi)
            else:
                heapq.heappush(heap, heapq.heappop(distance[wi]))
        return ret