class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [0] * len(nums)
        for i, n in enumerate(nums):
            heap[i] = -n

        heapq.heapify(heap)

        score = 0
        for _ in range(k):
            val = heapq.heappop(heap)
            val = -val

            score += val
            heapq.heappush(heap, -math.ceil(val / 3))
        
        return score