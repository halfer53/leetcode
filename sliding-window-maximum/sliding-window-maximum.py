class MonotonicQueue:
    def __init__(self):
        self.q = deque([])
        
    def push(self, val: int):
        while len(self.q) and self.q[-1] < val:
            self.q.pop()
        self.q.append(val)
        
    def remove(self, val: int):
        if len(self.q) and self.q[0] == val:
            self.q.popleft()
            
    def max(self)-> int:
        return self.q[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MonotonicQueue()
        k -= 1
        n = len(nums)
        ret = []
        for i in range(n):
            if i < k:
                q.push(nums[i])
            else:
                q.push(nums[i])
                ret.append(q.max())
                q.remove(nums[i-k])
        return ret