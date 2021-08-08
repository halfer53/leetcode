class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r1 = self.robhouse(nums[1:])
        r2 = self.robhouse(nums[:-1])
        return max(r1, r2)
        
    def robhouse(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]