class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sub = 0

        i = 0
        j = 0
        while i < len(nums):
            while j < len(nums) and nums[i] + k >= nums[j] - k:
                j += 1

            max_sub = max(max_sub, j - i)
            i += 1

        return max_sub