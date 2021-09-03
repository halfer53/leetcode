# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Value:
    def __init__(self, val):
        self.val = val
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        def dfs(node: TreeNode) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            inc = dec = 1
            if node.left:
                leftdec, leftinc = dfs(node.left)
                if node.val - node.left.val == 1:
                    dec = leftdec + 1
                elif node.left.val - node.val == 1:
                    inc = leftinc + 1
            if node.right:
                rightdec, rightinc = dfs(node.right)
                if node.right.val - node.val == 1:
                    inc = max(inc, rightinc + 1)
                elif node.val - node.right.val == 1:
                    dec = max(dec, rightdec + 1)
            self.ret = max(self.ret, inc + dec - 1)
            return dec, inc
        dec, inc = dfs(root)
        return self.ret