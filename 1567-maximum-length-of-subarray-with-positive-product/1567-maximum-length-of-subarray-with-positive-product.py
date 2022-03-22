class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def maxlen(arr: List[int]) -> int:
            pos = neg = 0
            ret = 0
            for x in arr:
                if x > 0: 
                    pos, neg = 1 + pos, 1 + neg if neg else 0
                elif x < 0: 
                    pos, neg = 1 + neg if neg else 0, 1 + pos
                else: 
                    pos = neg = 0 # reset 
                ret = max(ret, pos)
            return ret
        return maxlen(nums)