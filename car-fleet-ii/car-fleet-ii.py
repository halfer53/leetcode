class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        n = len(cars)
        ret = [-1.0] * n
        for i in reversed(range(n)):
            pos, speed = cars[i]
            while len(stack) and speed <= cars[stack[-1]][1]:
                stack.pop()
            while len(stack):
                ci = stack[-1]
                xpos, xspeed = cars[stack[-1]]
                time = (xpos - pos) / (speed - xspeed)
                if time <= ret[ci] or ret[ci] < 0:
                    ret[i] = time
                    break
                else:
                    stack.pop()
            stack.append(i)
        return ret