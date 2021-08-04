# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([])
        queue.append((root, 0))
        ret = float('inf')
        while len(queue):
            node, val = queue.popleft()
            val += 1
            if node.left:
                queue.append((node.left, val))
            if node.right:
                queue.append((node.right, val))
            if not node.left and not node.right:
                ret = min(ret, val)
                return ret
        return ret
            