class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = 0
        for i in range(n-1):
            curr = max(curr, i + nums[i])
            if curr <= i:
                return False
        return curr >= n - 1