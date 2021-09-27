class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        for i in range(n):
            for j in range(i+2, n):
                if dp[0][i] and dp[j][n-1] and dp[i+1][j-1]:
                    return True
        return False
                
            