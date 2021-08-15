class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ret = []
        for i in range(len(expression)):
            c = expression[i]
            if c in ['-', '+', '*', ]:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if c == '-':
                            ret.append(l - r)
                        elif c == '+':
                            ret.append(l + r)
                        elif c == '*':
                            ret.append(l * r)
        if len(ret) == 0:
            ret.append(int(expression))
        return ret
        