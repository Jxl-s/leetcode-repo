class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        output = ''

        while i >= 0 or j >= 0 or carry > 0:
            digit_i = (0 if i < 0 else int(a[i]))
            digit_j = (0 if j < 0 else int(b[j]))

            digit_total = digit_i + digit_j + carry
            carry = 0

            if digit_total >= 2:
                digit_total -= 2
                carry += 1
            
            output = str(digit_total) + output

            i -= 1
            j -= 1

        return output