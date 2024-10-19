class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        i = 0
        longest = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[i] == 0:
                    zeros -= 1

                i += 1
            
            longest = max(longest, j - i)
        
        return longest