class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = []
        
        for word, freq in counts.items():
            heapq.heappush(heap, (-freq, word))

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])

        return output