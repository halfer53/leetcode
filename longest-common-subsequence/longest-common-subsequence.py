class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.n = len(text1)
        self.m = len(text2)
        self.text1 = text1
        self.text2 = text2
        self.mem = [[-1] * self.m for _ in range(self.n)]
        return self.dfs(0, 0)
        
    def dfs(self, i: int, j:int) -> int:
        if i >= self.n or j >= self.m:
            return 0
        if self.mem[i][j] != -1:
            return self.mem[i][j]
        if self.text1[i] == self.text2[j]:
            self.mem[i][j] = self.dfs(i+1,j+1) + 1
        else:
            self.mem[i][j] = max(self.dfs(i + 1, j), self.dfs(i, j + 1), self.dfs(i + 1, j + 1))
        return self.mem[i][j]