class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        output = [[0] * n for _ in range(m)]
        for i in range(m):
            row_count = 0
            for j in range(n):
                if grid[i][j] == 1:
                    row_count += 1
                else:
                    row_count -= 1

            for j in range(n):
                output[i][j] += row_count

        for j in range(n):
            col_count = 0
            for i in range(m):
                if grid[i][j] == 1:
                    col_count += 1
                else:
                    col_count -= 1

            for i in range(m):
                output[i][j] += col_count

        return output