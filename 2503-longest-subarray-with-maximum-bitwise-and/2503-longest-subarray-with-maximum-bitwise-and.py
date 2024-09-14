class Solution:
    def longestSubarray(self, nums: List[int]) -> int: 
        max_val = max(nums)

        cur_longest = 0
        longest = 0

        for n in nums:
            if n == max_val:
                cur_longest += 1
            else:
                cur_longest = 0
            
            longest = max(longest, cur_longest)
        
        return longest