class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.ret = []
        self.backtrack([], nums)
        return self.ret
        
    def backtrack(self, track: List[int], nums: List[int]):
        if len(track) == len(nums):
            self.ret.append(track[:])
            return
        for j in range(len(nums)):
            if nums[j] in track:
                continue
            track.append(nums[j])
            self.backtrack(track, nums)
            track.pop()
        