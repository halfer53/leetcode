class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        @cache
        def dfs(i: int, j: int):
            if i >= m:
                return 0
            if j >= n:
                return 0
            if text1[i] == text2[j]:
                return dfs(i+1, j+1) + 1
            else:
                return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0, 0)