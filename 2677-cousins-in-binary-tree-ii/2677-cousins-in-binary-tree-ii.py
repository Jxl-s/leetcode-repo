# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, None)])

        while len(queue) > 0:
            total_sum = 0
            parent_sums = defaultdict(int)
            level_nodes = []

            for _ in range(len(queue)):
                node, parent = queue.popleft()
                parent_sums[parent] += node.val
                total_sum += node.val
                level_nodes.append((node, parent))

                if node.left: queue.append((node.left, node))
                if node.right: queue.append((node.right, node))

            for node, parent in level_nodes:
                node.val = total_sum - parent_sums[parent]
        
        return root