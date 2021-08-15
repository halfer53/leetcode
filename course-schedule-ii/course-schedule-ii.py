class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = collections.deque([])
        indegree = [0] * numCourses
        neighbour = collections.defaultdict(list)
        ret = []
        for course, pre in prerequisites:
            indegree[course] += 1
            neighbour[pre].append(course)
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                numCourses -= 1
        while len(q):
            course = q.popleft()
            ret.append(course)
            for nex in neighbour[course]:
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    q.append(nex)
                    numCourses -= 1
        return ret if numCourses == 0 else []
            