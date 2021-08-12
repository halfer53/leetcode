class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = collections.defaultdict(int)
        right = left = match = 0
        m = len(s)
        n = len(t)
        si = 0
        slen = float('inf')
        while right < m:
            c = s[right]
            window[c] += 1
            right += 1
            if c in need:
                if window[c] == need[c]:
                    match += 1
            while match == len(need):
                if right - left < slen:
                    si = left
                    slen = right - left
                c = s[left]
                if window[c] == need[c]:
                    match -= 1
                window[c] -= 1
                left += 1
        return s[si:si+slen] if slen != float('inf') else ''
        