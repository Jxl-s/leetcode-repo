class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        
        ordering = []

        visited = [False] * numCourses
        def dfs(node):
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

            ordering.append(node)

        for i in range(numCourses):
            if not visited[i]:
                dfs(i)

        return ordering