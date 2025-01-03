class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0

        total = sum(nums)
        current = 0

        for x in nums[:-1]:
            current += x
            if current >= total - current:
                count += 1
        
        return count