class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = collections.defaultdict(int)
        dic[0] = 1
        curr = ret = 0
        for i in range(n):
            curr += nums[i]
            rem = curr - k
            ret += dic[rem]
            dic[curr] += 1
        return ret
        