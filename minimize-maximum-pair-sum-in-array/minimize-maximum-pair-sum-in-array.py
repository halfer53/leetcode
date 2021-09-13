class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ret = 0
        for i in range(n//2):
            val = nums[i] + nums[n-i-1]
            ret = max(ret, val)
        return ret