# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(node, current):
            if not node:
                return
            
            current = current + '->' + str(node.val)
            if not node.left and not node.right:
                paths.append(current[2:])
            else:
                dfs(node.left, current)
                dfs(node.right, current)

        dfs(root, '')
        return paths