class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        q = collections.deque([])
        indegree = collections.defaultdict(int)
        neighbour = collections.defaultdict(list)
        ret = []
        for i in range(n):
            for c in words[i]:
                if c not in indegree:
                    indegree[c] = 0
            if i > 0:
                prev = words[i-1]
                curr = words[i]
                length = min(len(prev), len(curr))
                if prev[:length] == curr[:length] and len(prev) > len(curr):
                    return ''
                for j in range(length):
                    if prev[j] != curr[j]:
                        neighbour[prev[j]].append(curr[j])
                        indegree[curr[j]] += 1
                        break
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        while len(q):
            c = q.popleft()
            ret.append(c)
            for nex in neighbour[c]:
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    q.append(nex)
        for k,v in indegree.items():
            if v > 0:
                return ''
        return ''.join(ret)
            