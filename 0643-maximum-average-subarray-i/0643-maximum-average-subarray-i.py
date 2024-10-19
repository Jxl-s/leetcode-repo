class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        
        cur_sum = max_sum
        for i in range(len(nums) - k):
            cur_sum += nums[k + i]
            cur_sum -= nums[i]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum / k