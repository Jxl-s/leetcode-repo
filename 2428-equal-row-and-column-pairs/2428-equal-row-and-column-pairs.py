class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rows = defaultdict(int)
        columns = defaultdict(int)

        for i in range(n):
            row_hashed = tuple(grid[i])
            col_hashed = tuple([grid[j][i] for j in range(n)])

            rows[row_hashed] += 1
            columns[col_hashed] += 1

        pairs = 0
        for hashed in rows.keys():
            pairs += rows[hashed] * columns[hashed]

        return pairs