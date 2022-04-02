class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        curr = nums[0]
        for val in nums[1:]:
            if val > curr:
                if val + curr > val:
                    curr += val
                else:
                    curr = val
            else:
                curr += val
            ret = max(ret, curr)
        return ret