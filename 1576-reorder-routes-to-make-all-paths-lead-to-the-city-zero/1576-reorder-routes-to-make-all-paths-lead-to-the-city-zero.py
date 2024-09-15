class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in connections:
            adj[a].append((b, True))
            adj[b].append((a, False)) # not original

        count = 0

        visited = set()
        def dfs(node, flip):
            nonlocal count
            if node in visited:
                return
            
            if flip:
                count += 1

            visited.add(node)
            for neighbor, should_flip in adj[node]:
                dfs(neighbor, should_flip)
        
        dfs(0, False)
        return count