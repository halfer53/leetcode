class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -float('inf')
        sell = 0
        tmp = 0
        prev = 0
        n = len(prices)
        for p in prices:
            tmp = sell
            sell = max(sell, buy + p)
            buy = max(buy, prev - p)
            prev = tmp
        return sell