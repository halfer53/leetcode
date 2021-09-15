class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        arr.sort()
        pairs = 0
        for i, num in enumerate(arr):
            nex = num * 2
            if nex in count and num in count and (nex != num or count[nex] > 1):
                count[nex] -= 1
                if count[nex] == 0:
                    del count[nex]
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
                pairs += 1
        return pairs * 2 >= len(arr)
                    