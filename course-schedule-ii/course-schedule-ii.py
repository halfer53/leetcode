class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret = []
        indegree = [0] * numCourses
        neighbour = collections.defaultdict(list)
        queue = collections.deque([])
        for course, pre in prerequisites:
            indegree[course] += 1
            neighbour[pre].append(course)
            
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                numCourses -= 1
        while len(queue):
            node = queue.popleft()
            ret.append(node)
            for nextcourse in neighbour[node]:
                indegree[nextcourse] -= 1
                if indegree[nextcourse] == 0:
                    queue.append(nextcourse)
                    numCourses -= 1
        return ret if numCourses == 0 else []