class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:(x[1], x[0]))
        i = j = 0
        ret = 0
        n = len(intervals)
        while i < n:
            j = i + 1
            while j < n and intervals[j][0] < intervals[i][1]:
                j += 1
                ret += 1
            i = j
        return ret