class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        n = len(arr)
        right = n - 1
        
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        while right > left and arr[right - 1] <= arr[right]:
            right -= 1
        ret = min(right, n - left - 1)
        tleft = left
        left = 0
        while left <= tleft and right < n:
            if arr[left] <= arr[right]:
                ret = min(ret, right - left - 1)
                left += 1
            else:
                right += 1
        return ret
        