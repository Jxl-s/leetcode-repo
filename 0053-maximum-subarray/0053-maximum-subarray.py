class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = max_sum
        
        for num in nums:
            cur_sum += num
            if num > cur_sum:
                cur_sum = num

            max_sum = max(max_sum, cur_sum)
        
        return max_sum