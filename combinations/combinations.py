class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret = []
        nums = [i for i in range(1, n+1)]
        self.dfs(nums, [], k)
        return self.ret
        
    def dfs(self, track: List[int], path: List[int], k: int):
        if len(path) == k:
            self.ret.append(path[:])
            return
        for i in range(len(track)):
            self.dfs(track[i+1:], [track[i]] + path, k)