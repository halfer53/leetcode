# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mem = {0: [], 1: [TreeNode()]}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n in self.mem:
            return self.mem[n]
        ret = []
        for x in range(n):
            y = n - x - 1
            for left in self.allPossibleFBT(x):
                for right in self.allPossibleFBT(y):
                    node = TreeNode()
                    node.left = copy.deepcopy(left)
                    node.right= copy.deepcopy(right)
                    ret.append(node)
        self.mem[n] = ret
        return ret
                