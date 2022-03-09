class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = -float('inf')
        tmax = ret
        for n in nums:
            if n > ret and ret < 0:
                ret = n
            else:
                ret += n
            tmax = max(tmax, ret)
        return tmax
        