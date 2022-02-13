# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start = 0
        def dfs(node: TreeNode, parent: TreeNode):
            nonlocal start
            if not node:
                return
            if node.val == startValue:
                start = node
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        if start is None:
            return []
        visited = set([start.val])
        q = collections.deque([start])
        path = {}
        path[start.val] = None
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.val == destValue:
                    ret = []
                    pointer = path[node.val]
                    while pointer:
                        ret.append(pointer[0])
                        pointer = path[pointer[1]]
                    return ''.join(ret[::-1])
                for direction, nextnode in [['U', node.parent], ['L', node.left], ['R', node.right]]:
                    if nextnode and nextnode.val not in visited:
                        path[nextnode.val] = [direction, node.val]
                        q.append(nextnode)
                        visited.add(nextnode.val)
        return []
            
        
                
        
        