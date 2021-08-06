# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.dic = dict()
        self.hash = set()
        inorder = self.traverse(root)
        return [v for k,v in self.dic.items()]
        
    def traverse(self, node: TreeNode) -> List[int]:
        if node is None:
            return [None]
        arr = [node.val]
        arr += self.traverse(node.left)
        arr += self.traverse(node.right)
        tarr  = tuple(arr)
        if tarr in self.hash:
            self.dic[tarr] = node
        self.hash.add(tarr)
        return arr