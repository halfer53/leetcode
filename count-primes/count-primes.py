class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isprime = [True] * n
        isprime[0] = False
        isprime[1] = False
        for i in range(2, math.isqrt(n) + 1):
            if isprime[i]:
                for j in range(i*i, n, i):
                    isprime[j] = False
        ret = 0
        # print(isprime)
        for i in isprime:
            if i:
                ret += 1
        return ret