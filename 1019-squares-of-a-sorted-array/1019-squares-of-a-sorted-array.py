class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        left, right = 0, len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                out.append(nums[left] ** 2)
                left += 1
            else:
                out.append(nums[right] ** 2)
                right -= 1
        
        return out[::-1]