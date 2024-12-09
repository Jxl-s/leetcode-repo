class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        starts = [0]

        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                starts.append(i)

        output = []
        for start, end in queries:
            index = bisect_right(starts, start)
            if index >= len(starts):
                output.append(True)
            else:
                output.append(starts[index] > end)

        return output