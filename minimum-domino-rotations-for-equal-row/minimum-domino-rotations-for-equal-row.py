class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        def dfs(target: int):
            ret = 0
            l = n
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    return float('inf')
                if tops[i] == bottoms[i] == target:
                    l -= 1
                if tops[i] != target:
                    ret += 1
            return min(ret, l - ret)
        res = float('inf')
        dic = collections.Counter(tops)
        for k, v in dic.items():
            res = min(res, dfs(k))
        return res if res != float('inf') else -1
        