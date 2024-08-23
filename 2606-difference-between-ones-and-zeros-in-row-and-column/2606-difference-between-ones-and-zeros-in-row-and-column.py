class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            total = 0

            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                else:
                    total -= 1
            
            for j in range(n):
                result[i][j] += total

        for j in range(n):
            total = 0

            for i in range(m):
                if grid[i][j] == 1:
                    total += 1
                else:
                    total -= 1
            
            for i in range(m):
                result[i][j] += total

        return result