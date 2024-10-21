# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(root, depth, went_left):
            nonlocal longest
            if not root:
                return
            
            longest = max(longest, depth)
            if went_left:
                dfs(root.right, depth + 1, False)
                dfs(root.left, 1, True)
            else:
                dfs(root.left, depth + 1, True)
                dfs(root.right, 1, False)

        dfs(root, 0, False)
        dfs(root, 0, True)

        return longest