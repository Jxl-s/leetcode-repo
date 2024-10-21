class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(n)]

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        def delete_node(i):
            for j in adj[i]:
                adj[j].remove(i)
            
            adj[i].clear()
        
        nodes = n
        removed = [False] * n

        while nodes > 2:
            singles = [i for i in range(n) if len(adj[i]) == 1]
            nodes -= len(singles)

            for i in singles:
                removed[i] = True
                delete_node(i)

        return [i for i in range(n) if not removed[i]]