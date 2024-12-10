class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        current = 0

        for i in range(len(nums)):
            if total - current - nums[i] == current:
                return i

            current += nums[i]

        return -1