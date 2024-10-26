# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = defaultdict(int)
        heights = defaultdict(list) # cousins of the node, and their maximum depths

        def dfs(node, depth):
            if not node:
                return -1
            
            depths[node.val] = depth

            height = 1 + max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
            heights[depth].append((depth + height, node.val))

            return height

        dfs(root, 0)

        for k in heights.keys():
            heights[k].sort(reverse=True)

        output = []
        for q in queries:
            depth = depths[q]

            # if it has no cousins, its just the node's parent
            if len(heights[depth]) == 1:
                output.append(depth - 1)
                continue
            
            level_heights = heights[depth]

            h1, n1 = level_heights[0]
            h2, n2 = level_heights[1]
            # if its highest, then its 2nd, otherwise its highest
            output.append(h2 if q == n1 else h1)

        return output