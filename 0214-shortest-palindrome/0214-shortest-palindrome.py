class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        def isPalindrome(s):
            return s[::-1] == s

        s2 = s[::-1]
        for i in range(len(s2)):
            if isPalindrome(s2[:i] + s):
                return s2[:i] + s
        