class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n - 1
        for i in reversed(range(n)):
            if i + nums[i] >= last:
                last = i
        return last == 0