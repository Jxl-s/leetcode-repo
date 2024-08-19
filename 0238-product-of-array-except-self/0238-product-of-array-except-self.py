class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # pass through the left
        cur_prod = 1
        for i in range(len(nums)):
            output[i] = cur_prod
            cur_prod *= nums[i]
        
        # pass through the right
        cur_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= cur_prod
            cur_prod *= nums[i]
        
        return output