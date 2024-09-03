class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        result = []
        heap = []

        for x,y in queries:
            distance = abs(x) + abs(y)
            heapq.heappush(heap, -distance)

            if len(heap) > k:
                heapq.heappop(heap)

            if len(heap) < k:
                result.append(-1)
            else:
                result.append(-heap[0])

        return result