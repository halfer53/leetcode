class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        i = j = 0
        m = len(firstList)
        n = len(secondList)
        
        while i < m and j < n:
            fx, fy = firstList[i]
            sx, sy = secondList[j]
            if fx <= sy and sx <= fy:
                interval = [max(fx, sx), min(fy, sy)]
                ret.append(interval)
            if fy < sy:
                i += 1
            else:
                j += 1
        return ret
        