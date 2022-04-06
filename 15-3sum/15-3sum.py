class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = []
        def twosum(i: int):
            seen = {}
            j = i + 1
            while j < n:
                other = -nums[i] - nums[j]
                if other in seen:
                    ret.append([nums[i], other, nums[j]])
                    while j < n - 1 and nums[j+1] == nums[j]:
                        j += 1
                seen[nums[j]] = j
                j += 1
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                twosum(i)
        return ret