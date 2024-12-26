class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i, current):
            if i >= len(nums):
                return 1 if current == target else 0
            
            return dfs(i + 1, current + nums[i]) + dfs(i + 1, current - nums[i])

        return dfs(0, 0)