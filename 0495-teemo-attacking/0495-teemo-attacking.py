class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        poisoned = 0

        for x in timeSeries:
            if poisoned > x:
                total -= poisoned - x

            poisoned = x + duration
            total += duration

        return total