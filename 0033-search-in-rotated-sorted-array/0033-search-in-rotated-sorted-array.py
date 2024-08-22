class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        left, right = 0, len(nums) - 1

        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1