class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr: List[int]) -> int:
            n = len(arr)
            if n < 2:
                return max(arr)
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[n-1]
        if len(nums) < 2:
            return max(nums)
        return max(helper(nums[1:]), helper(nums[:-1]))