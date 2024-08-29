class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[False] * n for _ in range(n)]
        adj_x = {}
        adj_y = {}

        for i, (x, y) in enumerate(stones):
            if x not in adj_x:
                adj_x[x] = []
            if y not in adj_y:
                adj_y[y] = []

            adj_x[x].append(i)
            adj_y[y].append(i)

        for i in range(n):
            x, y = stones[i]

            for j in adj_x[x]:
                if i != j:
                    adj[i][j] = True
                    adj[j][i] = True
            
            for j in adj_y[y]:
                if i != j:
                    adj[i][j] = True
                    adj[j][i] = True

        visited = set()
        total_count = 0

        def dfs(i, is_root):
            nonlocal total_count
            if i in visited:
                return

            visited.add(i)
            if not is_root:
                total_count += 1

            for j in range(n):
                if adj[i][j] == True and j not in visited:
                    dfs(j, False)

        for i in range(n):
            if i not in visited:
                dfs(i, True)

        return total_count