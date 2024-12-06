class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)

        count = 0
        current = 0

        for i in range(1, n + 1):
            if i not in banned:
                current += i
                if current > maxSum:
                    return count

                count += 1

        return count