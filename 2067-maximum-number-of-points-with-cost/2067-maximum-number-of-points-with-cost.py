class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0]
        for i in range(1, len(points)):
            row_left = dp[:]
            row_right = dp[:]

            for j in range(1, len(row_left)):
                row_left[j] = max(dp[j], row_left[j - 1] - 1)
            
            for j in range(len(row_left) - 2, -1, -1):
                row_right[j] = max(dp[j], row_right[j + 1] - 1)
            
            for j in range(len(row_left)):
                dp[j] = points[i][j] + max(row_left[j], row_right[j])

        return max(dp)