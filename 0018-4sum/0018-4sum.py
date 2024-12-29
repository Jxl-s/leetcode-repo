class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = set()
        for i in range(len(nums)):
            for j in range(i + 3, len(nums)):
                real_target = target - nums[i] - nums[j]
                compl = {}
                for k in range(i + 1, j):
                    if nums[k] in compl:
                        entry = tuple(sorted([nums[i], nums[compl[nums[k]]], nums[k], nums[j]]))
                        output.add(entry)
                    else:
                        compl[real_target - nums[k]] = k

        return list(output)