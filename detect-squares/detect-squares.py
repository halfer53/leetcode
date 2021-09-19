

class DetectSquares:

    def __init__(self):
        self.ypoints = collections.defaultdict(list)
        self.pt = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.ypoints[x].append(y)
        self.pt[(x,y)] += 1

    def count(self, point: List[int]) -> int:
        ret = 0
        x, y = point
        for yi in self.ypoints[x]:
            if yi == y:
                continue
            sidelen = abs(y - yi)
            
            x3, y3 = x - sidelen, y
            x4, y4 = x3, yi
            ret += self.pt[(x3, y3)] * self.pt[(x4, y4)]
            
            x3, y3 = x + sidelen, y
            x4, y4 = x3, yi
            ret += self.pt[(x3, y3)] * self.pt[(x4, y4)]
        return ret


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)