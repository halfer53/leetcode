class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr: List[int]) -> int:
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            if n > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[n-1]
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))
    