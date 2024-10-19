class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rows = defaultdict(int)
        columns = defaultdict(int)

        for i in range(n):
            rows[tuple(grid[i])] += 1

            col = [0] * n
            for j in range(n):
                col[j] = grid[j][i]

            columns[tuple(col)] += 1
        
        pairs = 0
        for hashed in rows.keys():
            pairs += rows[hashed] * columns[hashed]

        return pairs