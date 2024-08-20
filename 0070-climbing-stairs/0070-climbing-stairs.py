class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[n - 1] + dp[n - 2]
        
        return dp[n]