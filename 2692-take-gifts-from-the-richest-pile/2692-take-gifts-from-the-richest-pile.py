class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            heapq.heappush(heap, -floor(sqrt(-heapq.heappop(heap))))

        return -sum(heap)