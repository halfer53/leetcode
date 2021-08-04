class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret = []
        self.backtrack(1, [], n, k)
        return self.ret
        
    def backtrack(self, i: int, track: List[int], n: int, k: int):
        if len(track) == k:
            self.ret.append(track[:])
            return
        for j in range(i, n+1):
            track.append(j)
            self.backtrack(j + 1, track, n, k)
            track.pop()