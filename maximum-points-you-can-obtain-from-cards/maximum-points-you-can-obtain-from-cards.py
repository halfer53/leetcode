class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ret = 0
        front = [0] * (n+1)
        back = [0] * (n+1)
        for i in range(1, n+1):
            front[i] = front[i-1] + cardPoints[i-1]
        for i in range(n-1, -1, -1):
            back[i] = back[i+1] + cardPoints[i]
        print(n)
        print(front)
        print(back)
        for i in range(k+1):
            ret = max(ret, front[i] + back[n-k+i])
        return ret