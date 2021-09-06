class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s2, e2 in self.overlaps:
            if s2 < end and start < e2:
                return False
        for s2, e2 in self.calendar:
            if start < e2 and s2 < end:
                self.overlaps.append((max(start, s2), min(e2, end)))
        self.calendar.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)