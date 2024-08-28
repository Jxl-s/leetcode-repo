class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotations = {
            2: 5,
            5: 2,
            6: 9,
            9: 6
        }

        def rotate_num(num):
            original_num = num
            rotated = 0
            mult = 1

            while num > 0:
                digit = num % 10
                num //= 10

                if digit in rotations:
                    rotated += rotations[digit] * mult
                elif digit == 0 or digit == 1 or digit == 8:
                    rotated += digit * mult
                else:
                    return original_num
                
                mult *= 10
            return rotated
        
        count = 0
        for i in range(1, n + 1):
            if rotate_num(i) != i:
                count += 1
        
        return count