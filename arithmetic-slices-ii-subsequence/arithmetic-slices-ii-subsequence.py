class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        from collections import defaultdict
        total = 0
        dp = [defaultdict(int) for item in nums]
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += 1
                if nums[i]-nums[j] in dp[j]:
                    dp[i][nums[i] - nums[j]] += dp[j][nums[i]-nums[j]]
                    total += dp[j][nums[i]-nums[j]]
        return total