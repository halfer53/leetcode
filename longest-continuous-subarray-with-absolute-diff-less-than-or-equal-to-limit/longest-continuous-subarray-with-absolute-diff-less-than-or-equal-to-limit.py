class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = []
        minq = []
        ret = i = 0
        for j, val in enumerate(nums):
            heapq.heappush(maxq, (-val, j))
            heapq.heappush(minq, (val, j))
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            ret = max(ret, j - i + 1)
        return ret