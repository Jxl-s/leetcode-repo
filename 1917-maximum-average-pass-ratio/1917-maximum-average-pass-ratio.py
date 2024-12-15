class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        diff = lambda x, y: (x / y) - (x + 1) / (y + 1)

        heap = [(diff(x, y), x, y) for x, y in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            rate, x, y = heapq.heappop(heap)

            x += 1
            y += 1

            heapq.heappush(heap, (diff(x, y), x, y))
        
        return sum(x / y for _, x, y in heap) / len(heap)