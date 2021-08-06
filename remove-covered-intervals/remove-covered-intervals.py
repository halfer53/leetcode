class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        i = j = 0
        n = len(intervals)
        ret = n
        while i < n:
            start, end = intervals[i]
            j = i + 1
            while j < n:
                s2, e2 = intervals[j]
                if start <= s2 and e2 <= end:
                    ret -= 1
                    j += 1
                else:
                    break
            i = j
        return ret