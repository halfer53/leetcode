class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ret = 0
        for t in tokens:
            if t.isnumeric() or (t and t[0] == '-' and t[1:].isnumeric()):
                stack.append(int(t))
            else:
                # print(stack, t)
                v2 = stack.pop()
                v1 = stack.pop()
                val = 0
                if t == '+':
                    val = v1 + v2
                elif t == '-':
                    val = v1 - v2
                elif t == '/':
                    negative = (v1 ^ v2) < 0
                    val = abs(v1) // abs(v2)
                    if negative:
                        val *= -1
                elif t == '*':
                    val = v1 * v2
                stack.append(val)
        return stack[-1]