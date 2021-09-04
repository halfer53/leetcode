class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: (x[0], -x[1]))
        ret = []
        i = 0
        n = len(intervals)
        while i < n:
            j = i + 1
            x = intervals[i][0]
            y = intervals[i][1]
            while j < n:
                if intervals[j][0] <= y:
                    y = max(y, intervals[j][1])
                    j += 1
                else:
                    break
            ret.append([x,y])
            i = j
        return ret