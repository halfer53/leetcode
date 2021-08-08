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
        arr += [ x + 2.0 * math.pi for x in arr]
        l = ret = r = 0
        angle = math.pi * angle / 180
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ret = max(ret, r - l + 1)
        return ret + extra