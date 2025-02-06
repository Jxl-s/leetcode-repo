class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        counts = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                counts[nums[i] * nums[j]] += 1

        answer = 0
        for product, count in counts.items():
            if count <= 1:
                continue

            # i had to look up things about combinatorics i forgot that
            answer += 4 * count * (count - 1)

        return answer