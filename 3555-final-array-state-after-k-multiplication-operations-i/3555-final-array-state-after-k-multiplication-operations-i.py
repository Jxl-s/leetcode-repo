class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_item = min(nums)
            for i in range(len(nums)):
                if min_item == nums[i]:
                    nums[i] *= multiplier
                    break
        
        return nums