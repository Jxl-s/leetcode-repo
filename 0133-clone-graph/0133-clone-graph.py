"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.cloned = {}
        return self.helper(node)

    def helper(self, node):
        if not node:
            return None

        if node in self.cloned:
            return self.cloned[node]

        cloned = Node(node.val)
        self.cloned[node] = cloned

        cloned.neighbors = [self.helper(n) for n in node.neighbors]
        return self.cloned[node]