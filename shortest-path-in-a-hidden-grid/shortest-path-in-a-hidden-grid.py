# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        direct = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        anti = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        isvalid = dict()
        
        def dfs(i: int, j: int):
            if master.isTarget():
                isvalid[(i,j)] = True
                return
            isvalid[(i,j)] = False
            for d, pos in direct.items():
                x = i + pos[0]
                y = j + pos[1]
                if (x,y) not in isvalid and master.canMove(d):
                    master.move(d)
                    isvalid[(x,y)] = False
                    dfs(x, y)
                    master.move(anti[d])
        dfs(0, 0)
        
        visited = set()
        q = collections.deque([])
        step = 0
        q.append((0, 0))
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if isvalid[(i,j)]:
                    return step
                for d, pos in direct.items():
                    x = i + pos[0]
                    y = j + pos[1]
                    if (x,y) in isvalid and (x,y) not in visited:
                        visited.add((x,y))
                        q.append((x,y))
            step += 1
        return -1
