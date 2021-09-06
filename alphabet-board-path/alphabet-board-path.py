class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = dict()
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for i in range(len(board)):
            for j in range(len(board[i])):
                pos[board[i][j]] = (i,j)
        height = [6, 5, 5, 5, 5]
        i = 0
        x = 0
        y = 0
        ret = []
        while i < len(target):
            xx, yy = pos[target[i]]
            if xx == x and yy == y:
                ret.append('!')
                i += 1
                continue
            while xx > x and x < height[y] - 1:
                ret.append('D')
                x += 1
            while xx < x:
                ret.append('U')
                x -= 1
            while yy > y:
                ret.append('R')
                y += 1
            while yy < y:
                ret.append('L')
                y -= 1
        return ''.join(ret)
                
                