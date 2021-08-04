class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        divider = 5
        while divider <= n:
            i = n // divider
            ret += i
            divider *= 5
        return ret
            