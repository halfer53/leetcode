# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.last = None
        if not root:
            return None
        return self.traverse(root)
        
    def traverse(self, node: TreeNode) -> TreeNode:
        val = node.val
        left = node.left
        right = node.right
        self.last = node
        if left:
            l = self.traverse(left)
            node.right = l
            node.left = None
        if right:
            if self.last:
                # print(val, 'last', self.last.val)
                self.last.right = right
            r = self.traverse(right)
        return node