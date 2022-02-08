# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            if not node.left and not node.right:
                dic[0].append(node.val)
                return 0
            level = max(dfs(node.left), dfs(node.right)) + 1
            dic[level].append(node.val)
            return level
        dfs(root)
        ret = [None] * len(dic)
        for k,v in dic.items():
            ret[k] = v
        return ret
        