directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j, val):
            total = val
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                
                if grid[ni][nj] == 0:
                    continue
                
                new_val = grid[ni][nj]
                grid[ni][nj] = 0
                total += dfs(ni, nj, new_val)

            return total
        
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    val = grid[i][j]
                    grid[i][j] = 0
                    answer = max(answer, dfs(i, j, val))
        
        return answer
