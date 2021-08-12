class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        dic = dict()
        n = len(temperatures)
        ret = [0] * n
        
        for i in range(n):
            val = temperatures[i]
            while len(stack) and stack[-1][0] < val:
                last, j = stack.pop()
                ret[j] = i - j
            stack.append((val, i))
        return ret