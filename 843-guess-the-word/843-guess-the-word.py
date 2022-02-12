# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def getMatches(a: str, b: str):
            ret = 0
            for i in range(6):
                if a[i] == b[i]:
                    ret += 1
            return ret
        matches = 0
        candidate = wordlist
        for i in range(10):
            if matches != 6:
                word = random.choice(candidate)
                matches = master.guess(word)
                tmplist = []
                for other in candidate:
                    if matches == getMatches(word, other):
                        tmplist.append(other)
                candidate = tmplist
            
            