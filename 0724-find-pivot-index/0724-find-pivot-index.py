class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sums = [0] * len(nums)
        cur_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            right_sums[i] = cur_sum
            cur_sum += nums[i]

        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum == right_sums[i]:
                return i

            cur_sum += nums[i]

        return -1