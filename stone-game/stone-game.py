class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.n = len(piles)
        self.piles = piles
        return self.dfs(0, self.n - 1) > 0
        
    @cache
    def dfs(self, i:int ,j: int) -> int:
        parity = (j - i - self.n) % self.n
        if i > j:
            return 0
        # Alex
        if parity % 2 != 0:
            return max(self.dfs(i + 1, j) + self.piles[i], \
                       self.dfs(i, j - 1) + self.piles[j])
        else:
            return min(self.dfs(i + 1, j) - self.piles[i], \
                       self.dfs(i, j - 1) - self.piles[j])