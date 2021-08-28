class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7
        if n == 1:
            return 3
        if n == 2:
            return 8
        a = [0] * n
        p = [0] * n
        l = [0] * n
        
        p[0] = 1
        l[0] = 1
        l[1] = 3
        a[0] = 1
        a[1] = 2
        a[2] = 4

        for i in range(1, n):
            a[i-1] %= mod
            p[i-1] %= mod
            l[i-1] %= mod
            
            p[i] = ((a[i-1] + p[i-1]) % mod + l[i-1]) % mod
            if i > 1:
                l[i] = ((a[i-1] + p[i-1] % mod) + (a[i-2] + p[i-2]) % mod) % mod
            if i > 2:
                a[i] = ((a[i-1] + a[i-2]) % mod + a[i-3]) % mod
        return ((a[n-1] % mod + p[n-1] % mod) % mod + l[n-1] % mod) % mod