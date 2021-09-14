# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.nodes = collections.defaultdict(list)
        def dfs(node: TreeNode) -> int:
            if node is None:
                return -1
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            level = max(left, right)
            self.nodes[level].append(node.val)
            return level
        dfs(root)
        ret = [list() for _ in range(len(self.nodes))]
        for k,v in self.nodes.items():
            ret[k] = v
        return ret