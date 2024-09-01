class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            num_str = str(num)
            if len(num_str) % 2 == 1:
                continue
            
            n = len(num_str) // 2

            left_sum = 0
            right_sum = 0

            for i in range(n):
                digit = num % 10
                num //= 10
                right_sum += digit

            for i in range(n):
                digit = num % 10
                num //= 10
                left_sum += digit
            
            if left_sum == right_sum:
                count += 1

        return count