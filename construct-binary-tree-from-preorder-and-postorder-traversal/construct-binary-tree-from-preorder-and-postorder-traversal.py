# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preidx = 0
    postidx = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        root = TreeNode(preorder[self.preidx])
        self.preidx += 1
        if root.val != postorder[self.postidx]:
            root.left = self.constructFromPrePost(preorder, postorder)
        if root.val != postorder[self.postidx]:
            root.right = self.constructFromPrePost(preorder, postorder)
        self.postidx += 1
        return root
            
            