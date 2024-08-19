class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def flood(i, j):
            if i < 0 or i >= len(grid):
                return
            
            if j < 0 or j >= len(grid[i]):
                return

            if (i, j) in visited:
                return
            
            visited.add((i, j))
            if grid[i][j] == "1":
                grid[i][j] = "0"
                flood(i + 1, j)
                flood(i - 1, j)
                flood(i, j + 1)
                flood(i, j - 1)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    flood(i, j)
                    island_count += 1

        return island_count