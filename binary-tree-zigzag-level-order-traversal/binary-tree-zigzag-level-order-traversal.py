# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        isleft = True
        q = collections.deque([])
        if root:
            q.append(root)
        ret = []
        while q:
            size = len(q)
            tmp = []
            for _ in range(size):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not isleft:
                tmp = tmp[::-1]
            ret.append(tmp)
            isleft = not isleft
        return ret