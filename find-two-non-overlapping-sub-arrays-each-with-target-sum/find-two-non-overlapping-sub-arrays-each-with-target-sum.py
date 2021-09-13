class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = [float('inf')] * n
        right = [float('inf')] * n
        best = float('inf')
        dic = {0:-1}
        tsum = 0
        for i in range(n):
            tsum += arr[i]
            if (tsum - target) in dic:
                best = min(best, i - dic[(tsum - target)])
            left[i] = best
            dic[tsum] = i
            
        best = float('inf')
        tsum = 0
        dic = {0: n}
        for i in reversed(range(n)):
            tsum += arr[i]
            if (tsum - target) in dic:
                best = min(best, dic[(tsum - target)] - i)
            right[i] = best
            dic[tsum] = i
            
        ret = float('inf')
        for i in range(1, n):
            if left[i-1] != float('inf') and right[i] != float('inf'):
                ret = min(ret, left[i-1] + right[i])
        return ret if ret != float('inf') else -1