class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        m = len(source)
        n = len(target)
        sourceset = set(source)
        targetset = set(target)
        for c in target:
            if c not in sourceset:
                return -1
        @cache
        def dfs(i: int, j: int) -> int:
            if j >= n:
                return 1
            if i >= m:
                return dfs(0, j) + 1
            if source[i] == target[j]:
                return dfs(i + 1, j + 1)
            else:
                return dfs(i + 1, j)
        return dfs(0, 0)