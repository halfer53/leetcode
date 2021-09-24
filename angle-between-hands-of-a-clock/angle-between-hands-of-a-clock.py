class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = minutes / 60 * 30 + (hour % 12) * 30
        minute_angle = minutes / 60 * 360
        r1 = abs(hour_angle - minute_angle)
        return min(r1, 360 - r1)
        