class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sub_n = n - k + 1

        # Find all prefix sum
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = nums[i] + prefix_sum[i]

        # Find all prefix sum for subarrays starting at i
        prefix_sub = [prefix_sum[i + k] - prefix_sum[i] for i in range(sub_n)]

        max_left = [0] * sub_n
        max_right = [0] * sub_n
        max_right[-1] = sub_n - 1

        # Find best left index from start to `i`
        for i in range(1, sub_n):
            if prefix_sub[i] > prefix_sub[max_left[i - 1]]:
                max_left[i] = i
            else:
                max_left[i] = max_left[i - 1]
        
        # Find best right index from end to `i`
        for i in range(sub_n - 2, -1, -1):
            # >= because we need smallest lexicographic one
            if prefix_sub[i] >= prefix_sub[max_right[i + 1]]:
                max_right[i] = i
            else:
                max_right[i] = max_right[i + 1]

        max_sum = 0
        max_combo = (0, 0, 0)

        for i in range(k, sub_n - k):
            left, right = max_left[i - k], max_right[i + k]

            summed = prefix_sub[left] + prefix_sub[i] + prefix_sub[right]
            if summed > max_sum:
                max_sum = summed
                max_combo = (left, i, right)
        
        return list(max_combo)