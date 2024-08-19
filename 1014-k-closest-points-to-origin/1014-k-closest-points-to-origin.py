class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x**2 + y**2, (x, y)))

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output