class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        debt = mean * (len(rolls) + n) - sum(rolls)
        avg_roll = debt // n
        remainder = debt % n

        if avg_roll > 6 or avg_roll < 1:
            return []

        if remainder == 0:        
            return [avg_roll] * n

        result = [avg_roll] * n

        # distribute the extra
        max_give = 6 - avg_roll
        for i in range(len(result)):
            if remainder <= 0:
                break

            give_count = min(max_give, remainder)
            remainder -= give_count
            result[i] += give_count

        if remainder > 0:
            return []

        return result