class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ret = []
        self.n = n
        self.board = [ ['.' for i in range(n)] for _ in range(n)]
        self.backtrack(0)
        return self.ret
        
    def backtrack(self, i: int):
        # print(self.board)
        if i >= self.n:
            board = list(self.board)
            for i in range(self.n):
                board[i] = ''.join(board[i])
            self.ret.append(board)
            return
        for j in range(self.n):
            if not self.isvalid(i, j):
                continue
            self.board[i][j] = 'Q'
            self.backtrack(i + 1)
            self.board[i][j] = '.'

            
    def isvalid(self, i: int, j: int) -> bool:
        for k in range(i):
            if self.board[k][j] == 'Q':
                return False
        for k,l in zip(range(i, -1, -1), range(j, -1, -1)):
            if self.board[k][l] == 'Q':
                return False
        for k, l in zip(range(i, -1, -1), range(j, self.n)):
            # print(i,j, k, l)
            if self.board[k][l] == 'Q':
                return False
        return True