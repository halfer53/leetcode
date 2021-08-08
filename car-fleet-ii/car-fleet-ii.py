class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        stack = []
        ret = [-1] * n
        for i in reversed(range(n)):
            pos, speed = cars[i]
            while len(stack) and speed <= cars[stack[-1]][1]:
                stack.pop()
                
            while len(stack):
                ci = stack[-1]
                cpos, cspeed = cars[ci]
                time = (cpos - pos) / (speed - cspeed)
                if time < ret[ci] or ret[ci] == -1:
                    ret[i] = time
                    break
                stack.pop()
            
            stack.append(i)
        return ret
            