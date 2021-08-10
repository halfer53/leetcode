# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dic = dict()
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root in self.dic:
            return self.dic[root]
        val = root.val
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        children = self.rob(root.left) + self.rob(root.right)
        ret = max(val, children)
        self.dic[root] = ret
        return ret