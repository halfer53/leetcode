class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ltiles = [c for c in tiles]
        self.ret = set()
        self.dfs(ltiles, [])
        return len(self.ret)
    
    def dfs(self, tiles: List[str], path: List[str]):
        if len(tiles) == 0:
            return
        for i in range(len(tiles)):
            newpath = [tiles[i]] + path
            self.ret.add(''.join(newpath))
            self.dfs(tiles[:i] + tiles[i+1:], newpath)
            
        