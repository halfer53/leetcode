class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cowset = set()
        secretdic = collections.Counter(secret)
        bull = cow = 0
        loop = dict()
        for idx, c in enumerate(guess):
            if idx < len(secret) and secret[idx] == c:
                secretdic[c] -= 1
                bull += 1
            else:
                loop[idx] = c
        for idx, c in loop.items():
            if c in secretdic and secretdic[c] > 0:
                secretdic[c] -= 1
                cow += 1
        return str(bull) + 'A' + str(cow) + 'B'