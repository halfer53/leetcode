class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        i = 0
        n = len(intervals)
        if n == 0:
            return [newInterval]
        inserted = False
        while i < n:
            if not inserted and newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                j = i
                while j < n and intervals[j][0] <= newInterval[1]:
                    j += 1
                j -= 1
                x = min(intervals[i][0], newInterval[0])
                y = max(intervals[j][1], newInterval[1])
                ret.append([x, y])
                i = j + 1 if j > i else i + 1
                inserted = True
            else:
                ret.append(intervals[i])
                i += 1
        if not inserted:
            i = bisect.bisect(ret, newInterval)
            ret.insert(i, newInterval)
        return ret
                
            