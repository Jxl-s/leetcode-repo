class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        heap = []
        for start, end in intervals:
            if len(heap) > 0 and heap[0] < start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)