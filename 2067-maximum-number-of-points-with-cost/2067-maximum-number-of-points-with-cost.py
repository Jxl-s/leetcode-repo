class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0]
        for i in range(1, len(points)):
            left = dp[:]
            right = dp[:]

            for j in range(1, len(points[i])):
                left[j] = max(dp[j], left[j - 1] - 1)

            for j in range(len(points[i]) - 2, -1, -1):
                right[j] = max(dp[j], right[j + 1] - 1)

            for j in range(len(dp)):
                dp[j] = points[i][j] + max(left[j], right[j])
        
        return max(dp)