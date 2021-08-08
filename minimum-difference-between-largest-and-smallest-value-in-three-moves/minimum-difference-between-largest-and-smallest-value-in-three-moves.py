class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def mindiff(arr: List[int]) -> int:
            if len(arr) == 0:
                return 0
            return arr[-1] - arr[0]
        nums.sort()
        r1 = mindiff(nums[3:])
        r2 = mindiff(nums[:-3])
        r3 = mindiff(nums[1:-2])
        r4 = mindiff(nums[2:-1])
        return min(r1, r2, r3, r4)