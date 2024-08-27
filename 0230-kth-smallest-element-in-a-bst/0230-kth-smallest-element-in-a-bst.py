# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def dfs(node):
            nonlocal count, result
            if not node:
                return None

            left = dfs(node.left)
            if left is not None:
                return left

            count += 1
            if count == k:
                return node.val

            right = dfs(node.right)
            if right is not None:
                return right
            
            return None

        return dfs(root)