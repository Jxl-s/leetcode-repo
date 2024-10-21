class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        parents = list(range(n))
        rank = [0] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return
            
            if rank[root_x] > rank[root_y]:
                parents[root_y] = parents[root_x]
            elif rank[root_x] < rank[root_y]:
                parents[root_x] = parents[root_y]
            else:
                parents[root_y] = parents[root_x]
                rank[root_x] += 1
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        seen = set()
        for i in range(n):
            seen.add(find(i))
        
        return len(seen)