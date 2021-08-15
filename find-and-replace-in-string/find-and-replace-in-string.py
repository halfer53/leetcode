class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        arr = sorted(zip(indices, sources, targets), reverse=True)
        ret = s
        for i, s, t in arr:
            slen = len(s)
            if ret[i:i+slen] == s:
                ret = ret[:i] + t + ret[i+slen:]
        return ret