class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        curr = 0
        n = len(asteroids)
        for item in asteroids:
            if item < 0:
                last = None
                while len(stack) and stack[-1] > 0 and stack[-1] <= abs(item):
                    last = stack.pop()
                    if last == abs(item):
                        break
                if last and last == abs(item):
                    continue
                if len(stack) and stack[-1] > 0 and stack[-1] > abs(item):
                    continue
            stack.append(item)
        return stack