class RangeModule:

    def __init__(self):
        self.arr = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.arr, left)
        end = bisect.bisect_right(self.arr, right)
        
        newarr = []
        if start % 2 == 0:
            newarr.append(left)
        if end % 2 == 0:
            newarr.append(right)
        self.arr[start:end] = newarr

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.arr, left)
        end = bisect.bisect_left(self.arr, right)
        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.arr, left)
        end = bisect.bisect_right(self.arr, right)
        
        newarr = []
        if start % 2 == 1:
            newarr.append(left)
        if end % 2 == 1:
            newarr.append(right)
        self.arr[start:end] = newarr

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)