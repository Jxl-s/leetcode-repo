# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = {}
        grouped = {}

        def dfs(node, depth):
            if not node:
                return -1

            depths[node.val] = depth
            height = 1 + max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

            if depth not in grouped:
                grouped[depth] = []

            grouped[depth].append((height + depth, node.val))
            grouped[depth].sort(reverse = True)
            if len(grouped[depth]) > 2:
                grouped[depth].pop()

            return height

        dfs(root, 0)
        output = [0] * len(queries)

        for i, q in enumerate(queries):
            depth = depths[q]
            options = grouped[depth]

            if len(options) == 1:
                output[i] = depth - 1
                continue

            first_height, first_node = options[0]
            second_height, _ = options[1]

            output[i] = second_height if q == first_node else first_height

        return output