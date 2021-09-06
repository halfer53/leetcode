class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.zeros = []

    def add(self, num: int) -> None:
        if num == 0:
            self.arr.append(num)
            self.zeros.append(len(self.arr) - 1)
            return
        if self.arr[-1] == 0:
            self.arr.append(num)
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        last = self.arr[-1]
        prev = self.arr[-(k + 1)]
        # print(k, last, prev, self.arr)
        j = len(self.arr) - k
        for i in self.zeros:
            if i >= j:
                last = 0
        if prev == 0:
            prev = 1
        return last // prev
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)