class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        total = 0

        for num, c in counts.items():
            if c > 1:
                total += (c-1)*c // 2

        return total