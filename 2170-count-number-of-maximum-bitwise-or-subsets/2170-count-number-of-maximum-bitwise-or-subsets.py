class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n
        
        subsets = 0

        def backtrack(i, current):
            nonlocal subsets
            if i == len(nums):
                if current == max_or:
                    subsets += 1

                return

            backtrack(i + 1, current | nums[i])
            backtrack(i + 1, current)

        backtrack(0, 0)
        return subsets