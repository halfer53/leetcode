class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        loop = sorted(zip(position, speed))
        speed_list = [(target - position) / speed for position, speed in loop]
        ret = 0
        curr = 0
        for speed in speed_list[::-1]:
            if speed > curr:
                ret += 1
                curr = speed
        return ret
            