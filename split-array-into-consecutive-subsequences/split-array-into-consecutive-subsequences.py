class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        p1 = p2 = p3 = 0
        prev = None
        while i < n:
            curr = nums[i]
            count = 0
            while i < n and nums[i] == curr:
                count += 1
                i += 1
            if prev is None or curr != prev + 1:
                if p1 or p2:
                    return False
                c2 = c3 = 0
                c1 = count
            else:
                if p1 + p2 > count:
                    return False
                c2 = p1
                c3 = p2 + min(p3, count - p1 - p2)
                c1 = max(0, count - p1 - p2 - p3)
            p1, p2, p3 = c1, c2, c3
            prev = curr
        return not p1 and not p2