class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0] * (n+1)
        queue = collections.deque([])
        graph = collections.defaultdict(list)
        
        for prev, nex in relations:
            indegree[nex] += 1
            graph[prev].append(nex)
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x = queue.popleft()
                for y in graph[x]:
                    indegree[y] -= 1
                    if indegree[y] == 0:
                        queue.append(y)
            step += 1
        for i in range(1, n+1):
            if indegree[i]:
                return -1
        return step