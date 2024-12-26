# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        counts = defaultdict(int)
        def dfs(node):
            if not node:
                return

            counts[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_occ = max(counts.values())
        return [k for k, v in counts.items() if v == max_occ]