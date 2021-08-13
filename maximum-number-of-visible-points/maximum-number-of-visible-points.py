class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        extra = 0
        x, y = location
        arr = []
        for xx, yy in points:
            if xx == x and yy == y:
                extra += 1
                continue
            arr.append(math.atan2(xx - x, yy - y))
        arr.sort()
        arr += [x + math.pi * 2.0 for x in arr]
        angle = angle / 180 * math.pi
        ret = 0
        right = left = 0
        n = len(arr)
        while right < n:
            while right < n and left <= right and arr[right] - arr[left] > angle:
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        return ret + extra