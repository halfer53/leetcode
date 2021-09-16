class Solution:
    def countVowelStrings(self, n: int) -> int:
        def backtrack(n, vowels) -> int:
            if n == 0:
                return 1
            ret = 0
            for i in range(vowels, 6):
                ret += backtrack(n-1, i)
            return ret
        return backtrack(n,1)
            