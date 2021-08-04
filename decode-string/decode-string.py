class Solution:
    def decodeString(self, encoded: str) -> str:
        self.n = len(encoded)
        self.i = 0
        self.encoded = encoded
        return self.dfs()
    
    def dfs(self):
        ret = []
        while self.i < self.n and self.encoded[self.i] != ']':
            if not self.encoded[self.i].isnumeric():
                ret.append(self.encoded[self.i])
                self.i += 1
            else:
                val = []
                while self.i < self.n and self.encoded[self.i].isnumeric():
                    val.append(self.encoded[self.i])
                    self.i += 1
                k = int(''.join(val))
                self.i += 1
                decode = self.dfs()
                self.i += 1
                ret.append(decode * k)
        return ''.join(ret)
                    
        
