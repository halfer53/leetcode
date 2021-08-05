class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # O(SL) Time S = number of Seq in seqs, L is max length of seq
        # O(N) space
        
        # edge case handle
        nodes = reduce(set.union, seqs, set())
        if nodes != set(org): return False
        
        # graph processing
        n = len(org)
        out_edges = [[] for _ in range(n+1)]
        in_degrees = [0 for _ in range(n+1)]
        for seq in seqs:
            for f, t in zip(seq, seq[1:]):
                out_edges[f].append(t)
                in_degrees[t] += 1
        
        # bfs search to find the unique topological sort order
        queue = [node for node in org if in_degrees[node] == 0]
        order = []
        # O(N^2) Time O(N) space.
        while queue:
            if len(queue) != 1: return False
            node = queue.pop()
            order.append(node)
            for next_node in out_edges[node]:
                in_degrees[next_node] -= 1
                if not in_degrees[next_node]:
                    queue.append(next_node)
        return org == order