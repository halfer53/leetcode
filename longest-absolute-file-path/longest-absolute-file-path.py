class Solution:
    def lengthLongestPath(self, s: str) -> int:
        stack = []
        ret = 0
        level = 0
        for line in s.split('\n'):
            n = len(line)
            i = 0
            while i < n and line[i] == '\t':
                i += 1
            level = i
            while len(stack) and i <= stack[-1][1]:
                stack.pop()
            if '.' in line:
                ret = max(ret, sum([len(x[0]) for x in stack]) + len(stack) + len(line[level:]))
            else:
                stack.append((line[level:], level))
        return ret
        