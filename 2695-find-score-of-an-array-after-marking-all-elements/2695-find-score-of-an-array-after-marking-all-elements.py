class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        heap = []
        score = 0

        for i, n in enumerate(nums):
            heap.append((n, i))
        
        heapq.heapify(heap)
        while len(heap) > 0:
            item, index = heapq.heappop(heap)
            if index in marked:
                continue
            
            score += item
            marked.add(index)
            marked.add(index - 1)
            marked.add(index + 1)

        return score