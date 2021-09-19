class Solution:
    def calculate(self, s: str) -> int:
        self.i = 0
        n = len(s)
        stack = []
        prevop = None
        while self.i < n:
            val = 0
            while self.i < n and s[self.i] == ' ':
                self.i += 1 

            while self.i < n and s[self.i].isnumeric():
                val = val * 10 + int(s[self.i])
                self.i += 1
                
            while self.i < n and s[self.i] == ' ':
                self.i += 1 
            
            if prevop == '*':
                stack[-1] = stack[-1] * val
            elif prevop == '/':
                stack[-1] = stack[-1] // val
            else:
                stack.append(val)
            
            if self.i < n:
                op = s[self.i]
                self.i += 1
                if op == '-':
                    stack.append('-')
                elif op == '+':
                    stack.append('+')
                prevop = op
        # print(stack)
        ret = 0   
        while stack:
            val = stack.pop()
            if stack:
                op = stack.pop()
                if op == '-':
                    ret -= val
                elif op == '+':
                    ret += val
            else:
                ret += val
        return ret
                        