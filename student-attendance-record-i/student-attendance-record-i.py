class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for c in s:
            if c == 'A':
                if a >= 1:
                    return False
                else:
                    a += 1
            if c == 'L':
                if l >= 2:
                    return False
                else:
                    l += 1
            else:
                l = 0
        return True