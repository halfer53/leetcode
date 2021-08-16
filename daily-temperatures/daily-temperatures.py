class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        dic = dict()
        n = len(temperatures)
        ret = [0] * n
        
        for i in range(n):
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ret[j] = i - j
            stack.append(i)
        return ret