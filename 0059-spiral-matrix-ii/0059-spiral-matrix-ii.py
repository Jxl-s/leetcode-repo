class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        i, j = 0, 0
        for k in range(n * n):
            mat[i][j] = k + 1

            di, dj = directions[direction]
            ni, nj = i + di, j + dj

            if ni >= n or ni < 0 or nj >= n or nj < 0 or mat[ni][nj] != 0:
                direction += 1
                direction %= 4
                di, dj = directions[direction]
                i, j = i + di, j + dj
            else:
                i, j = ni, nj
        
        return mat