class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_val = None
        second_val = None

        for i in range(len(nums)):
            if min_val is None:
                min_val = nums[i]
                continue
            else:
                min_val = min(min_val, nums[i])

            if nums[i] > min_val and (second_val is None or nums[i] < second_val):
                second_val = nums[i]

            if second_val is not None and nums[i] > second_val:
                return True
        
        return False