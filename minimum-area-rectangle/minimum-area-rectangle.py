class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        ret = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    val = abs(x1 - x2) * abs(y1 - y2)
                    if val:
                        ret = min(ret, val)
            
            seen.add((x1, y1))
        return ret if ret != float('inf') else 0