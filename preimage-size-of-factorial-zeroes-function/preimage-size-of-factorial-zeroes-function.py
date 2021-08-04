class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        return self.rightbound(k) - self.leftbound(k) + 1
        
    def leftbound(self, k: int) -> int:
        left = 0
        right = 2**63 - 1
        while left <= right:
            mid = (left + right) // 2
            n = self.trailingZeroes(mid)
            if n < k:
                left = mid + 1
            elif n > k:
                right = mid - 1
            else:
                right = mid - 1
        return left
    
    def rightbound(self, k: int) -> int:
        left = 0
        right = 2**63 - 1
        while left <= right:
            mid = (left + right) // 2
            n = self.trailingZeroes(mid)
            if n < k:
                left = mid + 1
            elif n > k:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
    
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        divider = 5
        while divider <= n:
            i = n // divider
            ret += i
            divider *= 5
        return ret