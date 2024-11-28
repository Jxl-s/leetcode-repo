class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        distances = [[float('inf')] * n for _ in range(m)]
        distances[0][0] = 0

        queue = deque([(0, 0)])
        while len(queue) > 0:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                
                new_distance = distances[i][j] + grid[ni][nj]
                if new_distance >= distances[ni][nj]:
                    continue
                
                distances[ni][nj] = new_distance
                if grid[ni][nj] == 0:
                    queue.appendleft((ni, nj))
                else:
                    queue.append((ni, nj))

        return distances[m - 1][n - 1]