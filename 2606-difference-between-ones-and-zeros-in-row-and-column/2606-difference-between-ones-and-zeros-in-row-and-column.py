class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = [0 for _ in range(len(grid))]
        cols = [0 for _ in range(len(grid[0]))]
        result = [[0] * len(m) for m in grid]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                else:
                    rows[i] -= 1
                    cols[j] -= 1
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = rows[i] + cols[j]
        
        return result