class Solution:
    def twoEggDrop(self, nval: int) -> int:
        @cache
        def dfs(k: int, n: int) -> int:
            if k == 1:
                return n
            if n == 0 or n == 1:
                return n
            ret = float('inf')
            low = 1
            high = n
            while low <= high:
                mid = (low+high) // 2
                left = dfs(k-1, mid-1)
                right = dfs(k, n-mid)
                ret = min(ret, max(left, right) + 1)
                if left < right:
                    low = mid + 1
                else:
                    high = mid - 1
            return ret
        return dfs(2, nval)