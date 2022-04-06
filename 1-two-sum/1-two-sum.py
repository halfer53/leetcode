class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        ret = []
        for i in range(len(nums)):
            other = target - nums[i]
            if other in dic:
                return [i, dic[other]]
            dic[nums[i]] = i
        return []
        