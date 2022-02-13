class StockPrice:

    def __init__(self):
        self.dic = dict()
        self.maxheap = []
        self.minheap = []
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp
        self.dic[timestamp] = price
        heapq.heappush(self.maxheap, (-price, timestamp))
        heapq.heappush(self.minheap, (price, timestamp))
        

    def current(self) -> int:
        return self.dic[self.latest_timestamp]

    def maximum(self) -> int:
        price, timestamp = heapq.heappop(self.maxheap)
        while -price != self.dic[timestamp]:
            price, timestamp = heapq.heappop(self.maxheap)
        heapq.heappush(self.maxheap, (price, timestamp))
        return -price

    def minimum(self) -> int:
        price, timestamp = heapq.heappop(self.minheap)
        while price != self.dic[timestamp]:
            price, timestamp = heapq.heappop(self.minheap)
        heapq.heappush(self.minheap, (price, timestamp))
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()