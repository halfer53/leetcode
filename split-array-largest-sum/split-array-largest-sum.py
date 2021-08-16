class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        self.nums = nums
        low = max(nums)
        high = sum(nums) + 1
        while low <= high:
            mid = (low + high) // 2
            k = self.split(mid)
            if k <= m:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
    def split(self, k: int) -> int:
        ret = 1
        curr = 0
        for val in self.nums:
            if curr + val > k:
                ret += 1
                curr = val
            else:
                curr += val
        return ret
        