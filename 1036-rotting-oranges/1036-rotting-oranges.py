class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        oranges = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    oranges += 1
                
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        if oranges == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(queue) > 0:
            i, j, minutes = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                
                if grid[ni][nj] == 1:
                    oranges -= 1
                    if oranges == 0:
                        return minutes + 1
                    
                    grid[ni][nj] = 2
                    queue.append((ni, nj, minutes + 1))

        return -1