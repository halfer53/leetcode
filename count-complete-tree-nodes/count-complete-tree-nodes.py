# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.counted = collections.defaultdict(bool)
        def dfs(node: TreeNode, l: int) -> Tuple[bool, int]:
            if node is None:
                return True, 0
            if not node.left and not node.right :
                return True, (1 if not self.counted[l] else 0)
            if node.left and not node.right:
                val = 1
                if not self.counted[l]:
                    val += l
                return False, val
            left = dfs(node.left, l*2)
            right = (True, 0)
            if left[0]:
                right = dfs(node.right, l*2)
            val = left[1] + right[1]
            if not self.counted[l]:
                val += l
                self.counted[l] = True
            return left[0] and right[1], val
        return dfs(root, 1)[1]
        