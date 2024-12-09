class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        starts = [0]

        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                starts.append(i)

        output = []
        for start, end in queries:
            # Find first one starting after start
            left = 0
            right = len(starts)

            while left < right:
                mid = (left + right) // 2
                if starts[mid] < start+1:
                    left = mid + 1
                else:
                    right = mid

            if left >= len(starts):
                output.append(True)
            else:
                output.append(starts[left] > end)

        return output