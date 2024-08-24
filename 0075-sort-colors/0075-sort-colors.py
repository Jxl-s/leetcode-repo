class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c_0, c_1, c_2 = 0, 0, 0

        for num in nums:
            if num == 0:
                c_0 += 1
            elif num == 1:
                c_1 += 1
            elif num == 2:
                c_2 += 1

        for i in range(c_0):
            nums[i] = 0
        
        for i in range(c_0, c_0 + c_1):
            nums[i] = 1

        for i in range(c_0 + c_1, c_0 + c_1 + c_2):
            nums[i] = 2
 
        return nums