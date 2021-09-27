# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> Tuple[int, int]:
            if node is None:
                return 0, -9999, True
            lcnt, lval, lsame = dfs(node.left)
            rcnt, rval, rsame = dfs(node.right)
            count = 0
            same = False
            if lsame and rsame:
                if lval == node.val == rval or (not node.left and rval == node.val) or (not node.right and lval == node.val):
                    same = True
                    count += 1
                elif not node.left and not node.right:
                    same = True
                    count += 1
            return lcnt + count + rcnt, node.val, lsame and same and rsame
        return dfs(root)[0]
        