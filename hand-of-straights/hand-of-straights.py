class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand.sort()
        count = collections.Counter(hand)
        i = 0
        while i < n:
            val = hand[i]
            for j in range(groupSize):
                if (val+j) not in count:
                    return False
                count[(val+j)] -= 1
                if count[(val+j)] == 0:
                    del count[(val+j)]
            while i < n and hand[i] not in count:
                i += 1
        return True
        