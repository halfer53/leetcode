class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums: List[int], path: List[int]):
        self.ret.append(path[:])
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                self.dfs(nums[i+1:], [nums[i]] + path)