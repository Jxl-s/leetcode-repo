class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        rev = 0
        x_rev = x
        while x_rev > 0:
            remainder = x_rev % 10
            rev = rev * 10 + remainder
            x_rev = x_rev // 10

        return x == rev