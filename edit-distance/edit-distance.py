class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= m:
                return n - j
            if j >= n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                r1 = dfs(i + 1, j)
                r2 = dfs(i, j + 1)
                r3 = dfs(i + 1, j + 1)
                return min(r1, r2, r3) + 1
        return dfs(0 , 0)