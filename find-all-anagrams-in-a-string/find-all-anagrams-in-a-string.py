class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.Counter(p)
        window = collections.defaultdict(int)
        right = left = match = 0
        m = len(s)
        n = len(p)
        ret = []
        while right < m:
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    match += 1
            while match == len(need):
                if right - left == len(p):
                    ret.append(left)
                c = s[left]
                if c in need:
                    if window[c] == need[c]:
                        match -= 1
                    window[c] -= 1
                left += 1
        return ret