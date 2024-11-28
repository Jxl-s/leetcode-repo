class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        n = max(a.bit_length(), b.bit_length(), c.bit_length())
        count = 0

        for i in range(n):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1

            # Case 0: make both 0
            if bit_c == 0:
                if bit_a == 1: count += 1
                if bit_b == 1: count += 1

            # Case 1: make at least one 1
            if bit_c == 1 and bit_a == 0 and bit_b == 0:
                count += 1

        return count