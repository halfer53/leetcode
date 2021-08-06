# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        tmax = -float('inf')
        i = 0
        n = len(nums)
        if n == 0:
            return None
        for j in range(n):
            if nums[j] > tmax:
                tmax = nums[j]
                i = j
        node = TreeNode(tmax)
        left = self.constructMaximumBinaryTree(nums[:i])
        right = self.constructMaximumBinaryTree(nums[i+1:])
        node.left = left
        node.right = right
        return node