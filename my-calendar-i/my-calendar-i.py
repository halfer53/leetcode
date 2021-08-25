class MyCalendar:

    def __init__(self):
        self.li = []

    def book(self, start: int, end: int) -> bool:
        i = 0
        # print(self.li)
        if not self.li:
            self.li.append([start, end])
            return True
        while i < len(self.li):
            if start >= self.li[i][1]:
                j = i + 1
                if j >= len(self.li) or end <= self.li[j][0]:
                    self.li.insert(j, [start, end])
                    return True
            elif end <= self.li[i][0]:
                j = i - 1
                if j < 0 or start >= self.li[j][1]:
                    self.li.insert(i, [start, end])
                    return True
            i += 1
        return False
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)