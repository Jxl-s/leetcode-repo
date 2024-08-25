class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        sign = '+'
        result = 0
        i = 0

        
        if s[0] == '-':
            sign = '-'
            i = 1
        elif s[0] == '+':
            sign = '+'
            i = 1

        while i < len(s):
            if s[i].isdigit():
                result *= 10
                result += int(s[i])
            else:
                break

            i += 1
        
        
        result = -result if sign == '-' else result
        if result < -2**31:
            return -2**31
        
        if result > 2**31-1:
            return 2**31-1
        
        return result