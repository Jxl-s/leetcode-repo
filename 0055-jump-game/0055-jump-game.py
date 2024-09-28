class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    dp[i + j] = True
                    if i + j == n - 1:
                        return True

        return False