class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}

        def dp(i, j):
            if i > j:
                return 0

            if i == j:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]

            min_turns = dp(i, j - 1) + 1
            for a in range(i, j):
                if s[a] == s[j]:
                    min_turns = min(min_turns, dp(i, a) + dp(a + 1, j - 1))

            memo[(i, j)] = min_turns
            return min_turns

        return dp(0, len(s) - 1)