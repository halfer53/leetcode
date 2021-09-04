class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rowdic = collections.defaultdict(set)
        coldic = collections.defaultdict(set)
        self.visited = dict()
        for x, y in stones:
            rowdic[x].add(y)
            coldic[y].add(x)

        def dfs(x: int, y: int):
            self.visited[(x,y)] = True
            for y2 in rowdic[x]:
                if (x,y2) not in self.visited:
                    self.visited[(x,y2)] = True
                    dfs(x, y2)
            for x2 in coldic[y]:
                if (x2, y) not in self.visited:
                    self.visited[(x2, y)] = True
                    dfs(x2, y)
        result = 0
        for x,y in stones:
            if (x,y) not in self.visited:
                dfs(x,y)
                result += 1
        return len(stones) - result