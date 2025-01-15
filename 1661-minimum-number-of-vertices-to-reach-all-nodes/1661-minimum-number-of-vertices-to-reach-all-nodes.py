class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degrees = [0 for _ in range(n)] # in-degrees

        for a, b in edges:
            degrees[b] += 1

        answer = []
        for i in range(n):
            if degrees[i] == 0:
                answer.append(i)
        
        return answer