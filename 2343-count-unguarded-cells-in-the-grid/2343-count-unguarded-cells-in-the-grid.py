UNGUARDED = 0
OBSTACLE = 1
GUARDED = 2

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[UNGUARDED] * n for _ in range(m)]
        for i, j in guards:
            matrix[i][j] = OBSTACLE

        for i, j in walls:
            matrix[i][j] = OBSTACLE

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i, j in guards:
            # Go all the way in all directions
            for di, dj in directions:
                ni, nj = i + di, j + dj

                while True:
                    # Boundaries
                    if ni < 0 or nj < 0: break
                    if ni >= m or nj >= n: break

                    # Obstacle
                    if matrix[ni][nj] == OBSTACLE: break

                    if matrix[ni][nj] == UNGUARDED:
                        matrix[ni][nj] = GUARDED

                    ni += di
                    nj += dj
        
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == UNGUARDED:
                    count += 1

        return count