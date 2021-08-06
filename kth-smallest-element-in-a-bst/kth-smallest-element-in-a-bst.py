# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = 0
        self.target = k
        self.ret = 0
        self.traverse(root)
        return self.ret
        
    def traverse(self, node: TreeNode):
        if node is None:
            return 0
        self.traverse(node.left)
        self.k += 1
        if self.k == self.target:
            self.ret = node.val
            return
        self.traverse(node.right)
