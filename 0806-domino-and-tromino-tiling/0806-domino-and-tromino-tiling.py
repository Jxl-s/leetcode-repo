class Solution:
    def numTilings(self, n: int) -> int:
        a, b, c = 1, 2, 5

        if n == 1: return a
        if n == 2: return b
        if n == 3: return c

        for i in range(4, n + 1):
            result = (c * 2 + a) % (10**9 + 7)
            a, b, c = b, c, result

        return c