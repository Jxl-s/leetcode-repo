class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        count = 0
        longest = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1

            while count > k:
                if nums[i] == 0:
                    count -= 1

                i += 1
            
            longest = max(longest, j - i + 1)
        
        return longest