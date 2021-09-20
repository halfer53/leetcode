class TrieNode:
    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)
        self.isend = False
        self.word = ''
        
    def __repr__(self):
        return f'{self.nodes.keys()}-{self.isend}'

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.se = set()
        m = len(board)
        n = len(board[0])
        
        def insert(root: TrieNode, w: str):
            curr = root
            for c in w:
                curr = curr.nodes[c]
            curr.isend = True
            curr.word = w
        
        def dfs(i: int, j: int, curr: TrieNode, path: set):
            if not (0 <= i < m and 0 <= j < n):
                return
            if (i,j) in path:
                return
            c = board[i][j]
            if c not in curr.nodes:
                return
            last = curr.nodes[c]
            if last.isend:
                # print(curr, path)
                self.ret.add(last.word)
                if len(last.nodes) == 0:
                    return
            path.add((i,j))
            dfs(i-1, j, last, set(path))
            dfs(i+1, j, last, set(path))
            dfs(i, j-1, last, set(path))
            dfs(i, j+1, last, set(path))
        
        self.root = TrieNode()
        self.ret = set()
        for w in words:
            insert(self.root, w)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.root.nodes:
                    dfs(i, j, self.root, set())

        return list(self.ret)