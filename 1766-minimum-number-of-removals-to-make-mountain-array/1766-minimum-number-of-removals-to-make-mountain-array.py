class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        left_inc = [1] * n
        right_inc = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and left_inc[j] >= left_inc[i]:
                    left_inc[i] = left_inc[j] + 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j] and right_inc[j] >= right_inc[i]:
                    right_inc[i] = right_inc[j] + 1

        max_mountain = 0
        for i in range(n):
            if left_inc[i] == 1 or right_inc[i] == 1:
                continue

            max_mountain = max(max_mountain, left_inc[i] + right_inc[i] - 1)

        return n - max_mountain