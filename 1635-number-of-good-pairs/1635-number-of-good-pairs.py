class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        counts = defaultdict(int)

        for num in nums:
            n = counts[num]
            total += n
            counts[num] += 1

        return total