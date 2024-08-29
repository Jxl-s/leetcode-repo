class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        n = len(nums)
        closest = None

        for i, num in enumerate(nums):
            left = i + 1
            right = n - 1

            while left < right:
                summ = nums[left] + nums[right] + num
                if closest is None:
                    closest = summ
                elif abs(target - summ) < abs(target - closest):
                    closest = summ

                if summ == target:
                    return summ
                elif summ < target:
                    left += 1
                elif summ > target:
                    right -= 1

        return closest