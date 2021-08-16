class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: (x[0], x[1]))
        i = j = 0
        ret = []
        n = len(intervals)
        while i < n:
            j = i + 1
            x, y = intervals[i]
            while j < n:
                if intervals[j][0] <= y:
                    y = max(y, intervals[j][1])
                    j += 1
                else:
                    break
            i = j
            ret.append([x, y])
        return ret