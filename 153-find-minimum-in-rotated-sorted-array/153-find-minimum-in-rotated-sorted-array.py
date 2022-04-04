class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[-1] > nums[0]:
            return nums[0]
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) >> 1
            # print(left, right, mid)
            if mid and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif mid < n - 1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
        return -1