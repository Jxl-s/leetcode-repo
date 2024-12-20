# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        current = 0

        while queue:
            count = len(queue)
            for i in range(count):
                node = queue[i]

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if current % 2 == 0:
                for i in range(count):
                    if queue[i].left:
                        queue[i].left.val, queue[count - i - 1].right.val = queue[count - i - 1].right.val, queue[i].left.val

            for i in range(count):
                queue.popleft()

            current += 1

        return root