class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right ) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
                