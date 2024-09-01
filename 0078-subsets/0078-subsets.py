class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current = []
        output = []

        def backtrack(level):
            if level >= len(nums):
                output.append(current[:])
                return
            
            # 1. with the item
            current.append(nums[level])
            backtrack(level + 1)
            # 2. without
            current.pop()
            backtrack(level + 1)
        
        backtrack(0)
        return output