class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def canfit(force: int) -> bool:
            ball = m - 1
            i = 0
            while ball > 0 and i < n:
                val = position[i]
                val += force
                i += 1
                while i < n and position[i] < val:
                    i += 1
                if i < n:
                    ball -= 1
            return ball == 0
        left = 1
        right = position[-1] - position[0] + 1
        while left <= right:
            mid = (left + right) // 2
            ret = canfit(mid)
            # print(ret, mid, left, right)
            if ret:
                left = mid + 1
            else:
                right = mid - 1
        return right 