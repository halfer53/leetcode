class Solution:
	def repeatedSubstringPattern(self, s: str) -> bool:
		n = len(s)
		for i in range(1, n // 2 + 1):
			curr = s[:i]
			if (n - i) % i == 0 and curr * ((n - i) // i + 1) == s:
				return True
		return False