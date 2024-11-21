class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        matrix = [[0] * n for _ in range(m)]

        for i, j in guards:
            matrix[i][j] = 1

        for i, j in walls:
            matrix[i][j] = 1
        
        blocked = 0
        for i, j in guards:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                while 0 <= ni < m and 0 <= nj < n:
                    if matrix[ni][nj] == 1:
                        break

                    if matrix[ni][nj] == 0:
                        matrix[ni][nj] = 2
                        blocked += 1

                    ni += di
                    nj += dj

        return m * n - len(guards) - len(walls) - blocked