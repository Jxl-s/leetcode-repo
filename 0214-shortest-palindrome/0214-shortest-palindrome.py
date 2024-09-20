class Solution:
    def isPalindrome(self, s):
        return s[::-1] == s

    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        s2 = s[::-1]
        for i in range(len(s2)):
            if self.isPalindrome(s2[:i] + s):
                return s2[:i] + s
        