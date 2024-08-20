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

        def dfs(n):
            if not n:
                return None

            if n in memo:
                return memo[n]

            node_copy = Node(n.val)
            memo[n] = node_copy

            for neighbor in n.neighbors:
                memo[n].neighbors.append(dfs(neighbor))
            
            return memo[n]

        return dfs(node)