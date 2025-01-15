class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = num2.bit_count()
        x = 0

        # flip down the most significant bits
        for i in range(30, -1, -1):
            if n > 0 and (num1 >> i) & 1 == 1:
                x |= (1 << i)
                n -= 1

        # keep assigning bits to least significant positions
        for i in range(30):
            if n > 0 and (num1 >> i) & 1 == 0:
                x |= (1 << i)
                n -= 1

        return x