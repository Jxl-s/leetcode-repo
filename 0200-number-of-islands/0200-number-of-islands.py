class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(m) for m in grid]
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0:
                return

            if i >= len(grid) or j >= len(grid[0]):
                return

            if visited[i][j]:
                return
            
            visited[i][j] = True
            if grid[i][j] == "1":
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    dfs(i, j)

        return count