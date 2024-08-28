class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)

        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        
        left_seat = -1

        for i in range(n):
            if seats[i] == 1:
                left_seat = i

            if left_seat == -1:
                left[i] = -1
            else:
                left[i] = i - left_seat

        right_seat = -1
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                right_seat = i

            if right_seat == -1:
                right[i] = -1
            else:
                right[i] = right_seat - i

        max_dist = 0
        for i in range(n):
            if right[i] == -1 or left[i] == -1:
                max_dist = max(max_dist, max(left[i], right[i]))
            elif left[i] > 0:
                max_dist = max(max_dist, min(left[i], right[i]))

        return max_dist