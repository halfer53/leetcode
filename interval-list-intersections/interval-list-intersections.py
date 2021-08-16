class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        i = j = 0
        ret = []
        while i < m and j < n:
            x = max(firstList[i][0], secondList[j][0])
            y = min(firstList[i][1], secondList[j][1])
            if x <= y:
                ret.append([x, y])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ret