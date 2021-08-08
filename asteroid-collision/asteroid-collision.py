class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for item in asteroids:
            if len(stack) == 0:
                stack.append(item)
            else:
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