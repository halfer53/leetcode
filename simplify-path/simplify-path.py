class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)
        while i < n:
            if path[i] == '/':
                i += 1
                namearr = []
                while i < n and path[i] == '/':
                    i += 1
                while i < n and path[i] != '/':
                    namearr.append(path[i])
                    i += 1
                name = ''.join(namearr)
                if name == '..':
                    if stack:
                        stack.pop()
                elif name != '.' and name != '':
                    stack.append(name)
            else:
                i += 1
        return '/' + '/'.join(stack)