class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ret = 0
        frontsetcards = [0] * (k+1)
        rearsetcards = [0] * (k+1)
        for i in range(k):
            frontsetcards[i+1] = cardPoints[i] + frontsetcards[i]
            rearsetcards[i+1] = cardPoints[n - i - 1] + rearsetcards[i]
        for i in range(k+1):
            val = frontsetcards[i] + rearsetcards[k - i]
            ret = max(ret, val)
        return ret