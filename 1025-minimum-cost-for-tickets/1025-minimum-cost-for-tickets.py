class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]

        dp = [0] * (last_day + 1)
        j = 0

        for i in range(1, last_day + 1):
            if i == days[j]:
                j += 1

                # Find best option
                a = dp[max(0, i - 1)] + costs[0]
                b = dp[max(0, i - 7)] + costs[1]
                c = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(a, b, c)
            else:
                # Not travelling; don't buy new ticket
                dp[i] = dp[i - 1]

        return dp[-1]