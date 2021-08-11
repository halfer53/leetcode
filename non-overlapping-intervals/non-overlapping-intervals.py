class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ret = 0
        intervals.sort(key= lambda x: (x[1], x[0]))
        n = len(intervals)
        i = j = 0
        while i < n:
            x, y = intervals[i]
            j = i + 1
            while j < n:
                xx, yy = intervals[j]
                if xx < y:
                    ret += 1
                    j += 1
                else:
                    break
            i = j
        return ret
            