class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        ret = 0
        seen = collections.defaultdict(int)
        for i in range(n):
            ret += seen[target - arr[i]]
            for j in range(i):
                seen[arr[i] + arr[j]] += 1
        ret = ret % (10**9 + 7)
        return ret