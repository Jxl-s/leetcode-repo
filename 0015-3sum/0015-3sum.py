class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    avoid = nums[left]

                    while left < right and nums[left] == avoid:
                        left += 1

        return triplets