# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        queue = deque([(0, root)])

        while len(queue) > 0:
            level, node = queue.popleft()
            if len(output) <= level:
                output.append([])

            output[level].append(node.val)
            if node.left:
                queue.append((level + 1, node.left))

            if node.right:
                queue.append((level + 1, node.right))

        return output