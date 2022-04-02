class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        curr = nums[0]
        for val in nums[1:]:
            curr = max(val, curr + val)
            ret = max(ret, curr)
        return ret