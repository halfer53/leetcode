# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.last = None
        def dfs(node: TreeNode) -> TreeNode:
            if node is None:
                return
            right = node.right
            left = node.left
            self.last = node
            dfs(left)
            if left and self.last:
                self.last.right = right
                self.last.left = None
                node.right = left
                node.left = None
            dfs(right)
        dfs(root)