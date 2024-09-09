class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i < 0:
                return 0

            memo[i] = nums[i] + max(dp(i - 2), dp(i - 3))
            return memo[i]

        return max(dp(n - 1), dp(n - 2))