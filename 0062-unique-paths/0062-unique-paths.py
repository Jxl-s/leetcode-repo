class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == 1 or j == 1:
                return 1

            memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
            return memo[(i, j)]
        
        return dp(m, n)