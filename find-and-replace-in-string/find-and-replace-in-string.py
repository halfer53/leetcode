class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ret = str(s)
        for i, s, t in sorted(zip(indices, sources, targets), reverse=True):
            if ret[i:i+len(s)] == s:
                ret = ret[:i] + t + ret[i+len(s):]
        return ret