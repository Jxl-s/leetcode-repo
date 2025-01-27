class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[False] * numCourses for _ in range(numCourses)]
        
        for a, b in prerequisites:
            matrix[a][b] = True
        
        # Transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

        return [matrix[a][b] for a, b in queries]