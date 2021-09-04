class Solution:
    def reformat(self, s: str) -> str:
        num = []
        alpha = []
        for c in s:
            if c.isnumeric():
                num.append(c)
            else:
                alpha.append(c)
        first = num if len(num) > len(alpha) else alpha
        second = alpha if num == first else num
        if abs(len(first) - len(second)) > 1:
            return ''
        ret = []
        for i in range(len(s)):
            if i % 2 == 0:
                ret.append(first.pop())
            else:
                ret.append(second.pop())
            i += 1
        return ''.join(ret)