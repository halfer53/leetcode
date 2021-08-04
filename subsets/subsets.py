class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.backtrack([], nums, 0)
        return self.ret
        
    def backtrack(self, track: List[int], nums: List[int], i: int):
        self.ret.append(list(track))
        for j in range(i, len(nums)):
            track.append(nums[j])
            self.backtrack(track, nums, j + 1)
            track.pop()
            