class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        dp =   [ float('inf')] * n
        path = [[]] * n
        dp[0]   = 0    # dp[i]   = cost it takes to jump at i
        path[0] = [1]  # path[i] = path to i from first place
        for i in range(1, n):
            if coins[i] == -1:
                continue
            for j in range(max(0,i-maxJump), i):
                if dp[i] > (coins[i] + dp[j]):
                    path[i] = path[j] + [i+1] # [i+1] because indexing starts at 1
                    dp[i]   = coins[i] + dp[j]
                elif dp[i] == (coins[i] + dp[j]):    # if path costs are same 
                    if path[i] > path[j] + [i+1]: # then chose lexicographically smaller path
                        path[i] = path[j] + [i+1]
                    
        return path[n-1]
        