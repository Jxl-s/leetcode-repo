class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        answer = '0'
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            result = ''

            for j in range(len(num2) - 1, -1, -1):
                product = int(num1[i]) * int(num2[j]) + carry

                carry = product // 10
                product %= 10

                result = str(product) + result

            # Adding remaining carry
            if carry:
                result = str(carry) + result

            result += '0' * (len(num1) - i - 1)

            # Calculate new answer
            new_answer = ''

            a = len(answer) - 1
            b = len(result) - 1
            sum_carry = 0

            while a >= 0 or b >= 0 or sum_carry:
                a_val = int(answer[a]) if a >= 0 else 0
                b_val = int(result[b]) if b >= 0 else 0

                summed = a_val + b_val + sum_carry
                sum_carry = summed // 10
                summed %= 10

                new_answer = str(summed) + new_answer

                a -= 1
                b -= 1
            
            answer = new_answer

        return answer