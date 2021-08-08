class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.encoding) and n > self.encoding[self.i]:
            n -= self.encoding[self.i]
            self.i += 2
        if self.i >= len(self.encoding):
            return -1
        self.encoding[self.i] -= n
        return self.encoding[self.i + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)