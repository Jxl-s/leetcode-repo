class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            if nums[i] in arr:
                return [arr[nums[i]], i]
            
            arr[target - nums[i]] = i
