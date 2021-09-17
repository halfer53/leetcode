class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.recursion(n)
        
    def recursion(self, n:int) -> List[str]:
        oddval = ["0", "1", "8"]
        evenval = ["11","69","88","96","00"]
        if n == 1:
            return oddval
        if n == 2:
            return evenval[:-1]
        ret = []
        if n % 2 != 0:
            r1 = oddval
            r2 = self.recursion(n - 1)
        else:
            r2 = self.recursion(n - 2)
            r1 = evenval
        for i in r2:
            for j in r1:
                n = len(i) // 2
                ret.append(i[:n] + j + i[n:])
        return ret
        