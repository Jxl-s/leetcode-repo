class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        offset = 0

        for i in range(64):
            if (x >> i) & 1 == 0:
                offset ^= ((n & 1) << i)
                n = n >> 1

        return offset | x