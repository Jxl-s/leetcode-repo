class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        obstacles = [[float('inf')] * n for _ in range(m)] 
        obstacles[0][0] = 0

        heap = [(0, 0, 0)] # removal, i, j
        while heap:
            removal, i, j = heapq.heappop(heap)
            if removal > obstacles[i][j]:
                continue
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue

                new_removal = removal + grid[ni][nj]
                if new_removal >= obstacles[ni][nj]:
                    continue
                
                obstacles[ni][nj] = new_removal
                heapq.heappush(heap, (new_removal, ni, nj))
        
        return obstacles[m - 1][n - 1]