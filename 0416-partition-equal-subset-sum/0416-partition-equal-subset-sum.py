class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        memo = {}
        def dp(idx, current):
            if current == 0:
                return True

            if idx >= len(nums):
                return False

            if (idx, current) in memo:
                return memo[(idx, current)]

            if dp(idx + 1, current) or dp(idx + 1, current - nums[idx]):
                memo[(idx, current)] = True
                return True

            memo[(idx, current)] = False
            return False

        return dp(0, target)
