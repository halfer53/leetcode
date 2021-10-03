class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        dp = [[ [] for i in range (target+1)] for _ in range(n+1)]
        dic = collections.defaultdict(list)
        for i in range(1,n+1):
            c = cost[i-1]
            dic[c].append(str(i))
            if c < target+1:
                dp[i][c] = dic[c]
            # print(i-1, cost[i-1], dic[cost[i-1]])
        for i in range(1, n+1):
            for j in range(target+1):
                if j < cost[i-1]:
                    tmp = dp[i][j] + dp[i-1][j]
                    if tmp:
                        dp[i][j] = [max(tmp, key=int)]
                else:
                    t1 = dp[i-1][j]
                    t2 = [str(i) + x for x in dp[i][j - cost[i-1]]]
                    t3 = dp[i][j]
                    tmp = t1 + t2 + t3
                    dp[i][j] = [max(tmp, key=int)] if tmp else tmp
        # for i in range(1, n+1):
        #     for j in range(target+1):
        #         if j >= cost[i-1]:
        #             print(cost[i-1], i,j, dp[i][j], '|', dp[i-1][j], dp[i][j - cost[i-1]] )
        #         else:
        #             print(cost[i-1], i,j, dp[i][j])
        return max(dp[n][target], key=int) if dp[n][target] else '0'