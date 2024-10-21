class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append((b, True))
            adj[b].append((a, False))
        
        seen = set()
        count = 0

        def dfs(node):
            nonlocal count
            if node is None:
                return 0
            
            if node in seen:
                return 0

            seen.add(node)
            for neighbor, correct in adj[node]:
                if neighbor in seen:
                    continue

                if correct:
                    count += 1
                
                dfs(neighbor)

        dfs(0)
        return count