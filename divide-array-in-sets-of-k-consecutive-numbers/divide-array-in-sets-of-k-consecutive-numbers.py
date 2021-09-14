class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        nums.sort()
        i = 0
        n = len(nums)
        while i < n:
            curr = nums[i]
            for j in range(k):
                val = curr + j
                if val not in count:
                    return False
                count[val] -= 1
                if count[val] == 0:
                    del count[val]
            while i < n and nums[i] not in count:
                i += 1
        return len(count) == 0
            