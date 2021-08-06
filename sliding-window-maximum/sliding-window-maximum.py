class MonotonicQueue:
    def __init__(self):
        self.queue = collections.deque()
    
    def put(self, item):
        while len(self.queue) and self.queue[-1] < item:
            self.queue.pop()
        self.queue.append(item)

    def remove(self, n):
        if self.queue[0] == n:
            item = self.queue.popleft()
    
    def max(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        ret = []
        i = 0
        n = len(nums)
        while i < n:
            if i < k - 1:
                window.put(nums[i])
            else:
                window.put(nums[i])
                ret.append(window.max())
                window.remove(nums[i - k + 1])
            i += 1
        return ret
                