# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        max_sum = root.val
        max_lvl = 1

        level = 0
        while len(queue) > 0:
            level += 1
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_lvl = level
        
        return max_lvl