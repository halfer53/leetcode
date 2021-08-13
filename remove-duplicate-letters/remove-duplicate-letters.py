class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        occur = {c: i for i, c in enumerate(s)}
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c in seen:
                continue
            while len(stack) and stack[-1] > c and occur[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
            seen.add(c)
            stack.append(c)
        return ''.join(stack)