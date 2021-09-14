class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        idxes = []
        for w in words:
            offset = -1
            while True:
                try:
                    i = s.index(w, offset+1)
                    idxes.append((i, i + len(w), w))
                    offset = i
                except:
                    break
        idxes.sort(key = lambda x: (x[0],x[1]))
        last = 0
        i = 0
        n = len(idxes)
        ret = []
        while i < n:
            j = i + 1
            curr = idxes[i]
            start = curr[0]
            end = curr[1]
            while j < n:
                nex = idxes[j]
                if nex[0] <= end:
                    end = max(end, nex[1])
                    j += 1
                else:
                    break
            ret.append(s[last:start])
            ret.append('<b>')
            ret.append(s[start:end])
            ret.append('</b>')
            last = end
            i = j
        if last < len(s):
            ret.append(s[last:])
        return ''.join(ret)
        