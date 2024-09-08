class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        cur_max = 0
        max_score = 0

        for i in range(len(nums) - 1):
            cur_max = max(cur_max, nums[i])
            max_score += cur_max

        return max_score