class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0, 1, 2, 5] + [0] * (n - 3)
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % (10**9 + 7)

        return dp[n]