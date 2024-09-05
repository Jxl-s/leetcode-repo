class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        debt = mean * (len(rolls) + n) - sum(rolls)
        avg_roll = debt // n
        remainder = debt % n

        if avg_roll > 6 or avg_roll < 1:
            return []

        result = [avg_roll] * n
        max_give = 6 - avg_roll

        if remainder > max_give * n:
            return []

        for i in range(len(result)):
            if remainder <= 0:
                break

            give_count = min(max_give, remainder)
            remainder -= give_count
            result[i] += give_count

        return result