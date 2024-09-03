class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ord_a = ord('a') - 1
        converted = ''

        for c in s:
            converted += str(ord(c) - ord_a)
        
        converted = int(converted)
        for _ in range(k):
            digit_sum = 0
            while converted > 0:
                digit = converted % 10
                converted //= 10
                digit_sum += digit
            
            converted = digit_sum
        
        return converted