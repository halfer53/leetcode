class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        color = [None] * 26
        graph = [list() for _ in range(26)]
        for eq in equations:
            if eq[1] == '=':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                graph[a].append(b)
                graph[b].append(a)
        t = 0
        for i in range(26):
            if color[i] is None:
                t += 1
                stack = [i]
                while stack:
                    curr = stack.pop()
                    for nei in graph[curr]:
                        if color[nei] is None:
                            color[nei] = t
                            stack.append(nei)
        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if a == b:
                    return False
                if color[a] is not None and color[a] == color[b]:
                    return False
        return True