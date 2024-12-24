class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]

        adj = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

            degree[a] += 1
            degree[b] += 1

        queue = deque()
        remaining = n

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
                remaining -= 1

        while queue:
            if remaining == 0:
                return list(queue)

            for _ in range(len(queue)):
                node = queue.popleft()
                degree[node] = 0

                for neighbor in adj[node]:
                    if degree[neighbor] == 0:
                        continue
                    
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                        remaining -= 1