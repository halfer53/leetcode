class Solution:
    def jump(self, nums: List[int]) -> int:
        end = furtherest = 0
        n = len(nums)
        jump = 0
        for i in range(n-1):
            furtherest = max(furtherest, i + nums[i])
            if end == i:
                jump += 1
                end = furtherest
        return jump