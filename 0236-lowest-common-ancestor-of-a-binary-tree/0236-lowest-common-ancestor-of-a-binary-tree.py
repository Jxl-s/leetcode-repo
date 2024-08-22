# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = None
        path_q = None

        def dfs(node, path):
            nonlocal path_p, path_q
            if not node:
                return
            
            if node == p:
                path_p = path[:]
                path_p.append(node)

            if node == q:
                path_q = path[:]
                path_q.append(node)

            if path_p and path_q:
                return

            copy = path[:]
            copy.append(node)

            dfs(node.left, copy)
            dfs(node.right, copy)

        dfs(root, [])
        last_good = path_q[0]
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] == path_q[i]:
                last_good = path_p[i]
            else:
                break
        
        return last_good