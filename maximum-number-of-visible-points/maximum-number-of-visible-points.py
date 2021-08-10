class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        extra = 0
        ret = 0
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
        l = r = 0
        while r < len(arr):
            while r < len(arr) and l <= r and arr[r] - arr[l] > angle:
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret + extra