class Solution:
    ret = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ret = set()
        self.backtrack([])
        return list(self.ret)
    
    def backtrack(self, curr: List[str]):
        i = len(curr) // 2
        if i >= self.n:
            if self.isvalid(curr):
                self.ret.add(''.join(curr))
            return
        
        for c in ['(', ')']:
            curr.append(c)
            self.backtrack(curr)
            curr.pop()
            
    def isvalid(self, curr: List[str]) -> bool:
        left = right = 0
        for c in curr:
            if c == '(':
                left += 1
            elif c == ')':
                left -= 1
            if left < 0:
                return False
        return left == 0
