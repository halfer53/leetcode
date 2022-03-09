class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxsum = currsum = -float('inf')
        minsum = currmin = float('inf')
        for n in nums:
            total += n
            currsum = max(currsum + n, n)
            maxsum = max(maxsum, currsum)
            currmin = min(currmin + n, n)
            minsum = min(currmin, minsum)
        ret = max(maxsum, total - minsum)
        return ret if ret != 0 else maxsum
            
        
        
                