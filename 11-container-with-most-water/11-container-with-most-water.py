class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0
        end = n - 1
        ret = 0
        while start <= end:
            area = (end - start) * min(height[start], height[end])
            ret = max(ret, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return ret