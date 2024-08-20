# TODO: try again next time
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}

        def dfs(i, m):
            if i >= n:
                return 0

            if (i, m) in dp:
                return dp[(i, m)]

            total = sum(piles[i:])
            max_stones = 0

            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break

                opponent = dfs(i + x, max(m, x))
                max_stones = max(max_stones, total - opponent)

            dp[(i, m)] = max_stones
            return max_stones

        return dfs(0, 1)
