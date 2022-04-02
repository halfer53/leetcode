class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg = nums[0]
        pos = nums[0]
        ret = nums[0]
        for val in nums[1:]:
            tmppos = val * pos
            tmpneg = val * neg
            pos = max(tmppos, val, tmpneg)
            neg = min(tmppos, val, tmpneg)
            ret = max(ret, pos)
        return ret 