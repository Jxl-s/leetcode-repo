class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        options = []

        def dfs(current, remaining, i):
            for c in range(i, len(candidates)):
                num = candidates[c]

                if remaining - num == 0:
                    copy = current[:]
                    copy.append(num)

                    options.append(copy)
                    continue

                if remaining - num < 0:
                    continue

                copy = current[:]
                copy.append(num)

                dfs(copy, remaining - num, c)

        dfs([], target, 0)
        return options