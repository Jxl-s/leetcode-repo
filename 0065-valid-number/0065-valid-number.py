SIGN = 0
DIGIT = 1
EXP = 2
DEC = 3

class Solution:
    def isNumber(self, s: str) -> bool:
        used = [False, False, False, False]

        for c in s:
            if c in '+-':
                # Can't use a sign before, and can't use digit before
                if used[SIGN] or used[DIGIT] or used[DEC]:
                    return False

                used[SIGN] = True
            elif c.isdigit():
                # Simple
                used[DIGIT] = True
            elif c == 'e' or c == 'E':
                # Can't have two exponents, and can't use before nothing
                if used[EXP] or not used[DIGIT]:
                    return False

                used[EXP] = True

                # Reset others for exponent
                used[SIGN] = False
                used[DIGIT] = False
                used[DEC] = False
            elif c == '.':
                # Can't already be decimal, and can't be in decimal
                if used[DEC] or used[EXP]:
                    return False

                used[DEC] = True
            else:
                return False

        return used[DIGIT]