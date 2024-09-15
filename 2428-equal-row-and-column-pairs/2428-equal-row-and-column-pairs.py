class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_hash = {}
        n = len(grid)

        for i in range(n):
            t = tuple(grid[i])
            if t in row_hash:
                row_hash[t] += 1
            else:
                row_hash[t] = 1
        
        pairs = 0
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])

            t = tuple(col)
            if t in row_hash:
                pairs += row_hash[t]

        return pairs