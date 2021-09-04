class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = '-' if num < 0 else ''
        n = abs(num)
        ret = []
        while n:
            ret.insert(0, str(n % 7))
            n //= 7
        return sign + ''.join(ret) if ret else '0'