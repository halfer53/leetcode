class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        self.n = len(s)
        self.s = s
        return self.dfs()
    
    def dfs(self):
        ret = []
        while self.i < self.n:
            if self.s[self.i] == ']':
                break
            if self.s[self.i].isnumeric():
                tmp = []
                while self.s[self.i].isnumeric():
                    tmp.append(self.s[self.i])
                    self.i += 1
                num = int(''.join(tmp))
                self.i += 1
                rep = self.dfs()
                self.i += 1
                ret.append(rep * num);
            else:
                ret.append(self.s[self.i])
                self.i += 1
                
        return ''.join(ret)
                