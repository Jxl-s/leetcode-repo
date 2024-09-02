class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, count in enumerate(chalk):
            if k < count:
                return i

            k -= count