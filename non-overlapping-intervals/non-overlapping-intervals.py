class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ret = 0
        arr = sorted(intervals, key= lambda x: (x[1], x[0]))
        i = j = 0
        n = len(arr)
        while i < n:
            j = i + 1
            while j < n and arr[j][0] < arr[i][1]:
                j += 1
                ret += 1
            i = j
        return ret
            
            