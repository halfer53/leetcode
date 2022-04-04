class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        point = 0
        if nums[0] < nums[-1]:
            ret = bisect.bisect_left(nums, target)
            if ret != n and nums[ret] == target:
                return ret
            return -1
        while left <= right:
            mid = (left + right) >> 1
            if mid and nums[mid-1] > nums[mid]:
                point = mid
                break
            elif mid < n - 1 and nums[mid] > nums[mid+1]:
                point = mid+1
                break
            elif nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        print(point, nums[point:])
        ret = 0
        if nums[0] <= target <= nums[point-1]:
            ret = bisect.bisect_left(nums[:point], target)
        else:
            ret = bisect.bisect_left(nums[point:], target)
            ret += point
        if 0 <= ret < n and nums[ret] == target:
            return ret
        return -1
        
                