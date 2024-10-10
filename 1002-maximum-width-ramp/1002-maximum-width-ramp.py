class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)

        max_ramp = 0

        for i in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] <= nums[i]:
                max_ramp = max(max_ramp, i - stack.pop())

        return max_ramp