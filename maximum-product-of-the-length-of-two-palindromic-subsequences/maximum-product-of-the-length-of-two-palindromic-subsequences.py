class Solution:
    def maxProduct(self, s: str) -> int:
        self.palindrome = []
        self.ret = 0
        n = len(s)
        @cache
        def dfs(i: int, j: int, exclude: Tuple[int], num: int) -> int:
            if i > j:
                if num == 0:
                    ret = dfs(0, n-1, exclude, 1)
                    # print(exclude, ret, ret * len(exclude))
                    return ret * len(exclude)
                return 0
            if num == 1 and i in exclude:
                return dfs(i+1, j, exclude, num)
            if num == 1 and j in exclude:
                return dfs(i, j-1, exclude, num)
            if s[i] == s[j]:
                add = 1 if i == j else 2
                e2 = exclude
                if num == 0:
                    if i == j:
                        e2 = exclude + (i,)
                    else:
                        e2 = exclude + (i, j)
                    add = 0
                r1 = dfs(i+1, j-1, e2, num) + add
                r2 = dfs(n, 0, e2, num)
                r3 = dfs(n, 0, exclude + (j,), num)
                r4 = dfs(n, 0, exclude + (i,), num)
                r5 = dfs(i+1, j-1, exclude, num)
                # print('add', add, num, exclude, i, j, 'return', r1, r2)
                return max(r1, r2, r3, r4, r5)
            else:
                r1 = dfs(i+1, j, exclude, num)
                r2 = dfs(i, j-1, exclude, num)
                r3 = dfs(i+1, j-1, exclude, num)
                r4 = dfs(n, 0, exclude + (j,), num)
                r5 = dfs(n, 0, exclude + (i,), num)
                return max(r1, r2, r3, r4, r5)
            
        return dfs(0, n - 1, tuple(), 0)