class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = collections.defaultdict(list)
        ret = 0
        for w in words:
            dic[w[0]].append(collections.deque([c for c in w]))
        for c in s:
            if c in dic:
                wordslist = dic[c]
                idx = 0
                while idx < len(wordslist):
                    wlist = wordslist[idx]
                    if len(wlist):
                        wlist.popleft()
                        if len(wlist) == 0:
                            ret += 1
                            wordslist.pop(idx)
                            continue
                        elif wlist[0] != c:
                            wordslist.pop(idx)
                            dic[wlist[0]].append(wlist)
                            continue
                    idx += 1
        return ret