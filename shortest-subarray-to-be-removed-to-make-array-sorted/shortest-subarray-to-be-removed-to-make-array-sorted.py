class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1
        while l < r and arr[l] <= arr[l+1]:
            l += 1
        if l == r:
            return 0
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        ret = min(r, n - l - 1)
        for i in range(l+1):
            if arr[i] <= arr[r]:
                ret = min(ret, r - i - 1)
            elif r < n - 1:
                r += 1
            else:
                break
        return ret