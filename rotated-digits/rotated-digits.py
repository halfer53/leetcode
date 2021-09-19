class Solution:
    def rotatedDigits(self, n: int) -> int:
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 2, 5, 6, 9])
        def isgood(i) -> int:
            s = set([int(j) for j in str(i)])
            return 1 if s.issubset(s2) and not s.issubset(s1) else 0
        return sum([isgood(i) for i in range(1, n+1)])