class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        mem = dict()
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            if s[i] == s[j]:
                plus = 2 if i != j else 1
                return dfs(i + 1, j - 1) + plus
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))
        return dfs(0, len(s) - 1) 