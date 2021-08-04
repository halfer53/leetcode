class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        self.n = len(nums)
        self.used = [False] * self.n
        self.nums = nums
        tsum = sum(nums)
        if tsum % k != 0:
            return False
        self.target = tsum // k
        return self.backtrack(k, 0, 0)
    
    def backtrack(self, k: int, bucket: int, start: int) -> bool:
        if k == 0:
            return True
        if bucket == self.target:
            return self.backtrack(k - 1, 0, 0)
        for i in range(start, self.n):
            if self.used[i]:
                continue
            if bucket + self.nums[i] > self.target:
                continue
            self.used[i] = True
            ret = self.backtrack(k, bucket + self.nums[i], i + 1)
            if ret:
                return True
            self.used[i] = False
        return False
        
            