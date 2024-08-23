from collections import deque
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 'tokenize' the expression
        ops = deque()
        buff = ""

        if expression[0] != "-" and expression[0] != "+":
            ops.append("+")

        for char in expression:
            if char == "-" or char == "+":
                if buff != "":
                    num, denum = buff.split("/")
                    ops.append((int(num), int(denum)))

                buff = ""
                ops.append(char)
            else:
                buff += char

        # Add last element
        if buff != "":
            num, denum = buff.split("/")
            ops.append((int(num), int(denum)))

        # Start calculating
        result = None
        while len(ops) > 0:
            op, val = ops.popleft(), ops.popleft()
            num, denum = val
            if result is None:
                if op == "-":
                    result = (-num, denum)
                else:
                    result = (num, denum)

                continue

            temp = result[1]
            result = (result[0] * denum, result[1] * denum)

            num *= temp

            if op == "+":
                result = (result[0] + num, result[1])
            else:
                result = (result[0] - num, result[1])

        gcd = math.gcd(result[0], result[1])
        result = (result[0] // gcd, result[1] // gcd)
        return str(result[0]) + "/" + str(result[1])