class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = collections.deque([])
        neigh = [[] for _ in range(n)]
        for i, manag in enumerate(manager):
            if manag == -1:
                q.append((i, 0))
            else:
                neigh[manag].append(i)
        ret = 0
        while q:
            for _ in range(len(q)):
                person, time = q.popleft()
                ret = max(ret, time)
                for sub in neigh[person]:
                    q.append((sub, time + informTime[person]))
        return ret