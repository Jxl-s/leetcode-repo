class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]
        def dp(i, j):
            if matrix[i][j] == 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            # Check if we're at last row/col
            if i == m - 1 or j == n - 1:
                return 1

            memo[i][j] = 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
            return memo[i][j]

        output = 0
        for i in range(m):
            for j in range(n):
                output += dp(i, j)

        return output