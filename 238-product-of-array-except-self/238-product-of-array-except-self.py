class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        prefix = [0] * n
        suffix = [0] * n
        curr = 1
        for i in range(n):
            curr *= nums[i]
            prefix[i] = curr
        curr = 1
        for i in reversed(range(len(nums))):
            curr *= nums[i]
            suffix[i] = curr
        ret = [0] * n
        for i in range(n):
            if i == 0:
                ret[i] = suffix[i+1]
            elif i == n - 1:
                ret[i] = prefix[i-1]
            else:
                ret[i] = prefix[i-1] * suffix[i+1]
        return ret
            