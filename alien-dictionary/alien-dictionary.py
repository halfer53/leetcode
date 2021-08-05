class Solution:
    def alienOrder(self, words: List[str]) -> str:
        queue = collections.deque([])
        neighbour = collections.defaultdict(set)
        n = len(words)
        indegree = collections.defaultdict(int)
        ret = []
        prev = None
        for w in words:
            for c in w:
                if c not in indegree:
                    indegree[c] = 0
            if prev:
                i = j = 0
                m = len(prev)
                n = len(w)
                clen = min(m, n)
                if prev[:clen] == w[:clen] and m > n:
                    return ''
                while i < len(prev) and j < len(w):
                    if prev[i] != w[j] and w[j]:
                        if w[j] not in neighbour[prev[i]]:
                            neighbour[prev[i]].add(w[j])
                            indegree[w[j]] += 1
                        break
                    i += 1
                    j += 1
            prev = w
        for node, val in indegree.items():
            if val == 0:
                queue.append(node)
        print(indegree, neighbour)
        while len(queue):
            node = queue.popleft()
            ret.append(node)
            for item in neighbour[node]:
                if item == node:
                    return ''
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
                elif indegree[item] < 0:
                    return ''
        for node, val in indegree.items():
            if val > 0:
                return ''
        return ''.join(ret)
                
            