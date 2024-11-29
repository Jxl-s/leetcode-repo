class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        rev = 0
        while x > 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10

        result =  sign * rev
        max_int = 2 ** 31

        if result < -max_int or result > max_int - 1:
            return 0

        return result