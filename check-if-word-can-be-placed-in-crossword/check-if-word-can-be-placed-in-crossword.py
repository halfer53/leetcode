class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wlen = len(word)
        grid = board
        
        def check(i: int, j: int, ishor: bool) -> bool:
            return backtrack(i, j, ishor, word) or backtrack(i, j, ishor, word[::-1])
        
        def backtrack(i: int, j: int, ishor: bool, s: str) -> bool:
            if ishor:
                end = j + wlen
                if end - 1 >= n:
                    return False
                for k in range(j, wlen + j):
                    c = s[k-j]
                    if c != grid[i][k] and grid[i][k] != ' ':
                        return False
                if (end < n and grid[i][end] != '#'):
                    return False
                return True
            else:
                end = i + wlen
                if end - 1 >= m:
                    return False
                for k in range(i, wlen + i):
                    c = s[k-i]
                    if c != grid[k][j] and grid[k][j] != ' ':
                        return False
                if (end < m and grid[end][j] != '#'):
                    return False
                return True
            
        for i in range(m):
            for j in range(n):
                ret = None
                if board[i][j] == '#':
                    ret = check(i+1, j, False) or check(i, j+1, True)
                if i == 0:
                    ret = ret or check(i, j, False)
                if j == 0:
                    ret = ret or check(i, j, True)
                if ret is not None and ret == True:
                    # print(i, j)
                    return ret
        return False
        
            
        