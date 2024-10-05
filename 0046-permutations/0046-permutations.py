class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current = []
        output = []
        taken = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                output.append(current[:])
                return
            
            for i in range(len(nums)):
                if not taken[i]:
                    current.append(nums[i])
                    taken[i] = True
                    backtrack()

                    current.pop()
                    taken[i] = False

        backtrack()
        return output