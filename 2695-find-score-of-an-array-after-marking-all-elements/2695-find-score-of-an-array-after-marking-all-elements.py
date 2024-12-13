class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)

        score = 0
        marked = [False] * n

        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)

        while heap:
            x, i = heapq.heappop(heap)
            if marked[i]:
                continue
            
            marked[i] = True
            if i - 1 >= 0: marked[i - 1] = True
            if i + 1 < n: marked[i + 1] = True

            score += x

        return score