class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = collections.deque([])
        indegree = [0] * numCourses
        nextcourses = collections.defaultdict(list)
        for pre, course in prerequisites:
            indegree[course] += 1
            nextcourses[pre].append(course)
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                numCourses -= 1
        if numCourses <= 0:
            return True
        while len(queue):
            node = queue.popleft()
            for course in nextcourses[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
                    numCourses -= 1
                    if numCourses == 0:
                        return True
        return False