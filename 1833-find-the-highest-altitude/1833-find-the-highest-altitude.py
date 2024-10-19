class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        largest = 0

        for n in gain:
            current += n
            largest = max(largest, current)
        
        return largest