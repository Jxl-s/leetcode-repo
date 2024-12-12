class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        total = sum(gifts)

        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            value = -heapq.heappop(heap)
            total -= value

            root = floor(sqrt(value))
            total += root
            heapq.heappush(heap, -root)
        
        return total