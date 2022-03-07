class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        n = len(nums)
        prev = pprev = ret = 0
        pprevval = -1
        for k in sorted(count):
            v = count[k]
            if pprevval == k - 1:
                ret = max(ret, k * v + pprev)
            else:
                ret = max(ret, k * v + prev)
            pprev = prev
            prev = ret
            pprevval = k
        return ret
            
        
            