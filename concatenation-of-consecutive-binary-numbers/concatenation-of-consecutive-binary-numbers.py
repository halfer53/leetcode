class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ret = ''.join(bin(i)[2:] for i in range(1,n+1))
        
        return int(ret,2) % (10**9 + 7)