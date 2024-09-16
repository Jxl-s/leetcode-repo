class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            hour, minute = timePoints[i].split(':')
            timePoints[i] = int(hour) * 60 + int(minute)

        timePoints.sort()
        smallest = float('inf')
        for i in range(1, len(timePoints)):
            smallest = min(smallest, timePoints[i] - timePoints[i - 1])

        smallest = min(smallest, 1440 + timePoints[0] - timePoints[-1])
        return smallest