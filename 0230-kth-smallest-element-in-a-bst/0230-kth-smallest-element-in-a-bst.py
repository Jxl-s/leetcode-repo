# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        def dfs(node):
            if not node:
                return -1

            nonlocal index
            left = dfs(node.left)
            if left != -1: return left

            index += 1
            if index == k:
                return node.val

            right = dfs(node.right)
            if right != -1: return right

            return -1
        
        return dfs(root)