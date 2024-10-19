# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]

            leaves = []
            leaves.extend(dfs(node.left))
            leaves.extend(dfs(node.right))

            return leaves
        
        return dfs(root1) == dfs(root2)