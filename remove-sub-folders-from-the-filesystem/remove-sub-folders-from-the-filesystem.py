class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key= lambda x: len(x))
        ret = set()
        for f in folder:
            found = False
            n = len(f)
            for i in range(n):
                if (i < n - 1 and f[i+1] == '/') or (i == n-1):
                    if f[:i+1] in ret:
                        found = True
                        break
            if not found:
                ret.add(f)
        return ret