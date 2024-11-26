class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        candidates = [True] * n
        for a, b in edges:
            candidates[b] = False
        
        if sum(1 if x else 0 for x in candidates) == 1:
            return candidates.index(True)
        
        return -1