class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        previous_max = 0
        current_max = 0

        for i in range(len(nums)):
            if i != 0 and nums[i].bit_count() != nums[i - 1].bit_count():
                previous_max = current_max

            if previous_max > nums[i]:
                return False

            current_max = max(current_max, nums[i])

        return True