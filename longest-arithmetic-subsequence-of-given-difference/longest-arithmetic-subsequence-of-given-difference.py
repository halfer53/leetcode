class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [1] * (n)
        dic = collections.defaultdict(list)
        for i in range(n):
            val = arr[i] - difference
            if val in dic:
                dp[i] = max([dp[k] for k in dic[val]]) + 1
            dic[arr[i]].append(i)
        return max(dp)
                
        
#         @cache
#         def dfs(i: int) ->int:
#             if i >= n:
#                 return 1
#             ret = 1
#             for j in range(i+1, n):
#                 if arr[j] - arr[i] == difference:
#                     ret = max(ret, dfs(j) + 1)
#             return ret
#         return max([dfs(i) for i in range(n)])
                