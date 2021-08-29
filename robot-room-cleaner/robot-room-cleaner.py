# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Dir:
    top = 0
    left = 1
    down = 2
    right = 3
    
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        path = set()
        poslist = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(x: int, y: int, d: int):
            robot.clean()
            visited.add((x, y))
            # print('clean', x, y, visited)
            for i in range(4):
                newd = (d+i) % 4
                xx, yy = poslist[newd]
                i = x + xx
                j = y + yy
                if (i, j) not in visited and robot.move():
                    backtrack(i ,j, newd)
                    goback()
                robot.turnRight()
        backtrack(0, 0, 0)
                