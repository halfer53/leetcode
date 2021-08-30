import sortedcontainers
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.l = sortedcontainers.SortedList()
        self.q = collections.deque()
        self.s = -1
        self.n = self.m - self.k * 2

    def addElement(self, num: int) -> None:
        self.q.append(num)
        if len(self.q) == self.m:
            self.l = sortedcontainers.SortedList(self.q)
            self.s = sum(self.l[self.k:-self.k])
        if len(self.q) > self.m:
            idx = bisect.bisect_left(self.l, num)
            if self.k <= idx <= self.m - self.k:
                self.s += num
            elif idx < self.k:
                self.s += self.l[self.k - 1]
            elif idx > self.m - self.k:
                self.s += self.l[self.m - self.k]
            self.l.add(num)
            
            d = self.q.popleft()
            didx = bisect.bisect_left(self.l, d)
            if self.k <= didx <= self.m - self.k:
                self.s -= d
            elif didx < self.k:
                self.s -= self.l[self.k]
            elif didx > self.m - self.k:
                self.s -= self.l[self.m - self.k]
            self.l.remove(d)
            

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        return self.s // self.n


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()