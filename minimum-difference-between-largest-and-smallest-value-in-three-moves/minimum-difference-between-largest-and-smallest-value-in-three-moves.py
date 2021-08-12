class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        def mindiff(tnums: List[int]) -> int:
            if len(tnums) == 0:
                return 0
            return tnums[-1] - tnums[0]
        r1 = mindiff(nums[0:-3])
        r2 = mindiff(nums[1:-2])
        r3 = mindiff(nums[2:-1])
        r4 = mindiff(nums[3:])
        return min(r1, r2, r3, r4)