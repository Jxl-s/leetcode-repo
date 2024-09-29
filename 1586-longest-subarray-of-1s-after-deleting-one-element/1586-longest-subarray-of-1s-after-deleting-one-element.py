class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        max_len = 0
        zero_count = 0
        i = 0

        for j in range(n):
            if nums[j] == 0:
                zero_count += 1
                while zero_count > 1:
                    if nums[i] == 0:
                        zero_count -= 1
                    
                    i += 1

            max_len = max(max_len, j - i)
        
        return max_len
            
