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
        memo = {}
        def clone(n):
            if not n:
                return None

            if n in memo:
                return memo[n]
            
            cloned = Node(n.val)
            memo[n] = cloned

            for n2 in n.neighbors:
                memo[n].neighbors.append(clone(n2))

            return memo[n]

        return clone(node)