class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stack = []
        ret = [-1] * n
        for i in reversed(range(n)):
            pos, speed = cars[i]
            while len(stack) and cars[stack[-1]][1] >= speed:
                stack.pop()
            while len(stack):
                j = stack[-1]
                xpos, xspeed = cars[j]
                time = (xpos - pos) / (speed - xspeed)
                if time < ret[j] or ret[j] == -1:
                    ret[i] = time
                    break
                else:
                    stack.pop()
            stack.append(i)
        return ret