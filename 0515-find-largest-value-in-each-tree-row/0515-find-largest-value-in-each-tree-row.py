# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        values = []
        queue = deque([root])

        while queue:
            max_value = float('-inf')

            for _ in range(len(queue)):
                node = queue.popleft()
                max_value = max(max_value, node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            values.append(max_value)

        return values