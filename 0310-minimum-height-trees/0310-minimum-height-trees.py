class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = { i: set() for i in range(n) }
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        while len(adj) > 2:
            alone = []
            for node, neighbors in adj.items():
                if len(neighbors) == 1:
                    alone.append((node, next(iter(neighbors))))
            
            for node, neighbor in alone:
                del adj[node]
                adj[neighbor].remove(node)
        
        return list(adj.keys())