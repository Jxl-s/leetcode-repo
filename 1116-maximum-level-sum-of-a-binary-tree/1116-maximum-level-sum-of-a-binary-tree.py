# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 1))

        current = 0
        current_level = 1

        maximum = float('-inf')
        maximum_level = 1

        while len(queue) > 0:
            node, depth = queue.popleft()
            if current_level == depth:
                current += node.val
            else:
                if current > maximum:
                    maximum = current
                    maximum_level = current_level

                current_level = depth
                current = node.val
            
            if node.left: queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))

        if current > maximum:
            return current_level

        return maximum_level