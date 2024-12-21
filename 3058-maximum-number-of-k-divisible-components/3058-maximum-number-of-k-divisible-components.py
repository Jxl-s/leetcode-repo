class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        count = 0
        def dfs(node, parent):
            nonlocal count

            total = values[node]
            for neighbor in adj[node]:
                if neighbor != parent:
                    total += dfs(neighbor, node)

            if total % k == 0:
                count += 1

            return total
        
        dfs(0, -1)
        return count
