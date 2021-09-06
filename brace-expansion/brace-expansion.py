class Solution:
    def expand(self, s: str) -> List[str]:
        self.ret = []
        def dfs(i: int, curr: List[str]):
            while i < len(s):
                if s[i] == '{':
                    i += 1
                    tmp = []
                    while i < len(s):
                        if s[i] == ',':
                            i += 1
                        elif s[i] == '}':
                            i += 1
                            for c in tmp:
                                dfs(i, curr + [c])
                            break
                        else:
                            tmp.append(s[i])
                            i += 1
                    return
                else:
                    curr.append(s[i])
                    i += 1
            if i >= len(s):
                self.ret.append(''.join(curr))

        dfs(0, [])
        return sorted(self.ret)
                