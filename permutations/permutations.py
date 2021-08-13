class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, available: List[int], arr: List[int]):
        if len(arr) == self.n:
            self.ret.append(arr[:])
            return
        for i in range(len(available)):
            num = available[i]
            self.dfs(available[:i] + available[i+1:], [num] + arr)