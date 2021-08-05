class Solution:
    dic = dict()
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.dic:
            return self.dic[expression]
        n = len(expression)
        result = []
        for i in range(n):
            c = expression[i]
            if c in ['-', '+', '*']:
                r1 = self.diffWaysToCompute(expression[:i])
                r2 = self.diffWaysToCompute(expression[i+1:])
                for j in r1:
                    for k in r2:
                        if c == '-':
                            result.append(j - k)
                        elif c == '+':
                            result.append(j + k)
                        elif c == '*':
                            result.append(j * k)
        if len(result) == 0:
            result.append(int(expression))
        self.dic[expression] = result[:]
        return result
                    
                
        