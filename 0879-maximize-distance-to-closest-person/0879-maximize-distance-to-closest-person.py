class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        last_seat = -1

        n = len(seats)
        for i in range(n):
            if seats[i] == 1:
                if last_seat == -1:
                    max_dist = i
                else:
                    max_dist = max(max_dist, (i - last_seat) // 2)

                last_seat = i

        if seats[-1] != 1:
            max_dist = max(max_dist, n - 1 - last_seat)

        return max_dist