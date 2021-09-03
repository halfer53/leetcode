class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se = set(nums)
        ret = 0
        for num in se:
            if num - 1 not in se:
                curr = num
                val = 1
                while curr + 1 in se:
                    curr += 1
                    val += 1
                ret = max(ret, val)

        return ret
                
                
        