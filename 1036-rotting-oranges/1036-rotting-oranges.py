from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_count = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    orange_count += 1

                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        if orange_count == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(queue) > 0:
            i, j, time = queue.popleft()

            # explore neighbors
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                # check bounds
                if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]):
                    # rot the orange
                    if grid[ny][nx] == 1:
                        grid[ny][nx] = 2
                        orange_count -= 1

                        if orange_count == 0:
                            return time + 1

                        queue.append((ny, nx, time + 1))

        return -1