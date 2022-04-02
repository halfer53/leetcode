class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        right = n - 1
        ret = float('inf')
        if nums[0] < nums[right]:
            return nums[0]
        while left <= right:
            mid = (left + right) >> 1
            if mid < n - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            elif mid and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return -1