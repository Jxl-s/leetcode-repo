class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n

        def backtrack(i, current):
            if i == len(nums):
                if current == max_or:
                    return 1

                return 0

            return backtrack(i + 1, current | nums[i]) + backtrack(i + 1, current)

        return backtrack(0, 0)