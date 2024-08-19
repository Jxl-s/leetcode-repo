"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [(0, root)]
        prev = []
        
        while len(queue) > 0:
            level, node = queue.pop(0)

            if len(prev) <= level:
                prev.append(node)
            else:
                prev[level].next = node
                prev[level] = node

            if node.left:
                queue.append((level + 1, node.left))

            if node.right:
                queue.append((level + 1, node.right))

        return root