class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums: List[int], track: List[int]):
        if len(track) == self.n:
            self.ret.append(track[:])
        for i in range(len(nums)):
            val = nums[i]
            self.dfs(nums[:i] + nums[i+1:], track + [val]  )
        