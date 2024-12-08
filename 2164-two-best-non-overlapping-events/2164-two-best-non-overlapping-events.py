class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        heap = []
        max_value = 0

        output = 0
        for start, end, value in events:
            while heap and heap[0][0] < start:
                max_value = max(max_value, heapq.heappop(heap)[1])

            output = max(output, max_value + value)
            heapq.heappush(heap, (end, value))

        return output