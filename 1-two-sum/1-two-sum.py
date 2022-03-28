class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = collections.defaultdict(list)
        for i, n in enumerate(nums):
            dic[n].append(i)
        for i, n in enumerate(nums):
            other = (target - n)
            if other in dic:
                if other == n:
                    if len(dic[n]) >= 2:
                        
                        return dic[other]
                else:
                    return [i, dic[other][0]]
        return []
        