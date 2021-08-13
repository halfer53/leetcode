class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: (x[1], x[0]))
        i = j = 0
        ret = 0
        n = len(points)
        while i < n:
            j = i + 1
            x, y = points[i]
            while j < n:
                if points[j][0] <= y:
                    j += 1
                else:
                    break
            ret += 1
            i = j
        return ret