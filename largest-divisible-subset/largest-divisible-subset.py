class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if (dp[j] + 1) > dp[i]:
                        parent[i] = j
                        dp[i] = dp[j] + 1
        tmax = 0
        ti = -1
        # print(dp)
        # print(parent)
        for i, val in enumerate(dp):
            if val > tmax:
                tmax = val
                ti = i
        if ti == -1:
            return ret
        while ti != -1:
            ret.append(nums[ti])
            ti = parent[ti]
        return ret