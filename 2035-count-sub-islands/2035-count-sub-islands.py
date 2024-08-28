class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        # Modify the grid1
        island_id = 2
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            grid1[i][j] = island_id
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue

                if grid1[ni][nj] == 1:
                    dfs(ni, nj)

        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    dfs(i, j)
                    island_id += 1

        # Traverse islands in grid2
        sub_count = 0
        def dfs2(island, i, j):
            grid2[i][j] = 0
            is_valid = grid1[i][j] == island
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue

                if grid2[ni][nj] == 1:
                    if not dfs2(island, ni, nj):
                        is_valid = False

            return is_valid

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] != 0:
                    if dfs2(grid1[i][j], i, j):
                        sub_count += 1

        return sub_count