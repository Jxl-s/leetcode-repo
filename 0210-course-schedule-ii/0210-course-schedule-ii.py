NONE = 0
VISITED = 1
ADDED = 2

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        
        order = []
        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == VISITED:
                return False
            
            if visited[node] == ADDED:
                return True

            visited[node] = VISITED
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = ADDED
            order.append(node)
            return True

        for node in range(numCourses):
            if visited[node] == NONE:
                if not dfs(node):
                    return []

        return order