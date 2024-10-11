class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        schedule = []
        for i, (a, b) in enumerate(times):
            schedule.append((a, True, i))
            schedule.append((b, False, i))

        schedule.sort()

        seat_num = 0
        seats = []
        players = {}

        for t, a, i in schedule:
            if a:
                if len(seats) > 0:
                    players[i] = heappop(seats)
                else:
                    players[i] = seat_num
                    seat_num += 1
                
                if i == targetFriend:
                    return players[i]

            else:
                heappush(seats, players[i])
                del players[i]