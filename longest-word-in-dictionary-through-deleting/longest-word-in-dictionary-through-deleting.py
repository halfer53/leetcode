class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        h = []
        def check(w: str) -> int:
            i = j = 0
            ret = 0
            while i < len(w) and j < len(s):
                if w[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    ret += 1
            # print(w, i, j, len(w), len(s))
            return i >= len(w)
        for w in dictionary:
            res = check(w)
            if res:
                heapq.heappush(h, (-len(w), w))
        return h[0][1] if h else ''
            