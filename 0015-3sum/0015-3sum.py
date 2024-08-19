class Solution:
    def threeSum(self, nums):
        nums.sort()

        comb = []
        for i, num in enumerate(nums):
            # prevent duplicate
            if i > 0 and nums[i - 1] == num:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    comb.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1

        return comb