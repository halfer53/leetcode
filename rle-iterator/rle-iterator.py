class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0
        self.n = len(self.encoding)

    def next(self, n: int) -> int:
        while self.i < self.n and n > self.encoding[self.i]:
            n -= self.encoding[self.i]
            self.i += 2
        if self.i >= self.n:
            return -1
        self.encoding[self.i] -= n
        return self.encoding[self.i + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)