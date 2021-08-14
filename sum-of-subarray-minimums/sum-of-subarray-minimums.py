class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        n = len(arr)
        ret = [0] * n
        for i in range(n):
            while len(stack) and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if len(stack):
                j = stack[-1]
                prevless = arr[j]
                ret[i] = ret[j] + arr[i] * (i - j)
            else:
                ret[i] = arr[i] + arr[i] * i
            stack.append(i)
        return sum(ret) % mod
                