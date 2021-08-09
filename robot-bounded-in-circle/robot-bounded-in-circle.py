class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        x = 0
        y = 0
        for c in instructions:
            if c == 'L':
                direction = (direction - 90) % 360
            elif c == 'R':
                direction = (direction + 90) % 360
            elif c == 'G':
                if direction == 0:
                    x += 1
                elif direction == 90:
                    y += 1
                elif direction == 180:
                    x -= 1
                elif direction == 270:
                    y -= 1
        if x == 0 and y == 0:
            return True
        if direction != 0:
            return True
        return False
            
            