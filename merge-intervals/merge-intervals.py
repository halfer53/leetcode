class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort(key= lambda x: (x[0], -x[1]))
        i = j = 0
        n = len(intervals)
        while i < n:
            a_start, a_end = intervals[i]
            j = i + 1
            end = a_end
            start = a_start
            while j < n:
                b_start, b_end = intervals[j]
                if b_start <= end:
                    end = max(b_end, end)
                    j += 1
                else:
                    break
            ret.append([a_start, end])
            i = j
        return ret
            
        