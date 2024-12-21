class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        count = 0
        def dfs(node, parent):
            nonlocal count

            # postorder
            current_sum = 0
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                current_sum += dfs(neighbor, node)

            current_sum += values[node]
            current_sum %= k

            if current_sum == 0:
                count += 1

            return current_sum

        dfs(0, -1)
        return count