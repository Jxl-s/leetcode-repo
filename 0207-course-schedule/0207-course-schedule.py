class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)

        visited = set()
        def dfs(course):
            if course in visited:
                return False

            visited.add(course)
            for course2 in adj[course]:
                if not dfs(course2):
                    return False
            
            adj[course] = []
            visited.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
