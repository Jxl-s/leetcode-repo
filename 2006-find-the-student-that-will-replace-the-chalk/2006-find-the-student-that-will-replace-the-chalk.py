class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i

            k -= chalk[i]
