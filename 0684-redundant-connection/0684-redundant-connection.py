class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parents = list(range(n))
        ranks = [0] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            
            return parents[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if ranks[root_x] > ranks[root_y]:
                parents[root_y] = parents[root_x]
            elif ranks[root_x] < ranks[root_y]:
                parents[root_x] = parents[root_y]
            else:
                parents[root_y] = parents[root_x]
                ranks[root_x] += 1
            
            return True

        for a, b in edges:
            if not union(a - 1, b - 1):
                return [a, b]