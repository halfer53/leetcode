class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev, pprev = 0, 0
        ret = 0
        prevval = -1
        for k in sorted(count):
            v = count[k]
            if prevval == k - 1:
                ret = max(ret, k * v + pprev)
            else:
                ret = max(ret, k * v + prev)
            pprev = prev
            prev = ret
            prevval = k
        return ret
        
        