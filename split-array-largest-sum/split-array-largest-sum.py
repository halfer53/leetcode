class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.nums = nums
        low = max(nums)
        high = sum(nums) + 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            n = self.split(mid)
            if n <= m: # can you make at-most m sub-arrays with maximum sum atmost mid 
                high = mid-1
            else:
                low = mid + 1
        return low
    
    def split(self, mid):
        ret = 1
        curr = 0
        for x in self.nums:
            if curr + x > mid:
                ret += 1
                curr = x
            else:
                curr += x
        return ret
    