class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.se = set(words)
        self.words = sorted(words, key=lambda x: len(x))
        # print(self.words)
        ret = ''
        for w in self.words:
            if len(w) == 1:
                val = self.dfs(w)
                # print(w, val)
                if len(val) > len(ret) or (len(val) == len(ret) and val < ret):
                    ret = val
        return ret
        
    def dfs(self, word: str) -> str:
        ret = word
        for i in range(ord('a'), ord('z') + 1):
            val = word + chr(i)
            if val in self.se:
                r2 = self.dfs(val)
                if len(r2) > len(ret) or (len(r2) == len(ret) and r2 < ret):
                    ret = r2
        return ret

            