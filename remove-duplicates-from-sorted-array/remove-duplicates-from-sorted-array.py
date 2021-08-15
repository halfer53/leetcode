class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        n = len(nums)
        while fast < n:
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
        return slow + 1