class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = collections.defaultdict(list)
        ret = 0
        for w in words:
            dic[w[0]].append(w)
        for c in s:
            if c in dic:
                tmp = []
                i = 0
                n = len(dic[c])
                arr = dic[c]
                while i < n:
                    w = arr[i]
                    newval = w[1:]
                    if newval:
                        if newval[0] == c:
                            tmp.append(newval)
                        else:
                            dic[newval[0]].append(newval)
                    else:
                        ret += 1
                    i += 1
                dic[c] = tmp
        return ret
                    