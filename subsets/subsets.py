class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums: List[int], path: List[int]):
        self.ret.append(path[:])
        for i in range(len(nums)):
            self.dfs(nums[i+1:], [nums[i]] + path)