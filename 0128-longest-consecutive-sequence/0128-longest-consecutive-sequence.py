class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        neighbors = defaultdict(int)
        maximum = 0

        for n in set(nums):
            left = neighbors[n - 1]
            right = neighbors[n + 1]

            maximum = max(maximum, left + right + 1)

            neighbors[n - left] = left + right + 1
            neighbors[n + right] = left + right + 1
        
        return maximum