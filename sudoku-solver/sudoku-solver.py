class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(0, 0, board)
        
    def backtrack(self, i: int, j: int, board: List[List[str]]) -> bool:
        if j >= 9:
            return self.backtrack(i + 1, 0, board)
        
        if i >= 9:
            return True
        
        if board[i][j] != '.':
            return self.backtrack(i, j+1, board)
        
        for k in range(1, 10):
            if not self.isvalid(str(k), i, j, board):
                continue
            board[i][j] = str(k)
            ret = self.backtrack(i, j + 1, board)
            if ret:
                return True
            board[i][j] = '.'
        return False
            
        
    def isvalid(self, val: str, i: int, j: int, board: List[List[str]]) -> bool:
        for k in range(9):
            if board[k][j] == val:
                return False
        for k in range(9):
            if board[i][k] == val:
                return False
        row = (i) // 3
        col = (j) // 3
        for k in range(3):
            for l in range(3):
                pi = 3 * row + k
                pj = 3 * col + l
                if pi != i and pj != j and board[pi][pj] == val:
                    return False
        return True
        