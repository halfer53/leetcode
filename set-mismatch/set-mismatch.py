class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = loss = -1
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                dup = abs(nums[i])
            else:
                nums[idx] *= -1
        for i in range(n):
            if nums[i] > 0:
                loss = i + 1
                break
        return [dup, loss]