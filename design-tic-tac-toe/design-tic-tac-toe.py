class TicTacToe:

    def __init__(self, n: int):
        self.board = [[None for i in range(n)] for j in range(n)]
        self.n = n
    def dfs(self, row, col, x, y, player) -> int:
        row += x
        col += y
        if not (0 <= row < self.n and 0 <= col < self.n):
            return 0
        val = self.board[row][col]
        if not val or val != player:
            return 0
        return self.dfs(row, col, x, y, player) + 1
    
    def move(self, row: int, col: int, player: int) -> int:
        # print(row, col, player, self.board)
        for idx, direction in enumerate([[[0,1],[0,-1]], [[1, 0], [-1, 0]], [[-1,-1], [1, 1]], [[1,-1], [-1,1]]]):
            left = self.dfs(row, col, direction[0][0], direction[0][1], player)
            right = self.dfs(row, col, direction[1][0], direction[1][1], player)
            # print(row, col, direction, left, right)
            if left + right + 1 == self.n:
                return player
        self.board[row][col] = player
        return 0
            


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)