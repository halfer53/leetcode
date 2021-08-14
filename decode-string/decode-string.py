class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        self.n = len(s)
        self.s = s
        return self.dfs()
    
    def dfs(self) -> str:
        if self.i >= self.n:
            return ''
        ret = []
        while self.i < self.n and self.s[self.i] != ']':
            if self.s[self.i].islower():
                ret.append(self.s[self.i])
                self.i += 1
            else:
                numstart = self.i
                while self.i < self.n and self.s[self.i].isnumeric():
                    self.i += 1
                num = int(self.s[numstart:self.i])
                self.i += 1
                nexrep = self.dfs()
                ret.append(nexrep * num)
                self.i += 1
        return ''.join(ret)
                